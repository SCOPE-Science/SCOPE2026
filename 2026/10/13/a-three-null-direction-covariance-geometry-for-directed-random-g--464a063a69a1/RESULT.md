# A three-null-direction covariance geometry for directed random-graph degree histograms

## Finding
Let \(n\ge2\) be an integer and \(0<p<1\). In a directed simple random graph on vertex set \(\{1,\ldots,n\}\), each ordered arc between different vertices occurs independently with probability \(p\). Let \(I_k\) and \(O_k\) count vertices with in-degree and out-degree \(k\), respectively, for \(0\le k\le n-1\). Let \(b_k=\binom{n-1}{k}p^k(1-p)^{n-1-k}\), \(D=\operatorname{diag}(b_k)\), and define unit vectors
\[
 u_k=\sqrt{b_k},\qquad v_k=\frac{k-(n-1)p}{\sqrt{(n-1)p(1-p)}}\sqrt{b_k}.
\]
Write \(\Sigma=\operatorname{Cov}((I_0,\ldots,I_{n-1},O_0,\ldots,O_{n-1}))\), and whiten it by \(\operatorname{diag}(D^{-1/2},D^{-1/2})\). The exact matrix is
\[
 \boxed{\Sigma_{\mathrm{white}}=n\begin{pmatrix}\operatorname{Id}-uu^\top&vv^\top\\vv^\top&\operatorname{Id}-uu^\top\end{pmatrix}.}
\]
Its eigenvalues, with multiplicities, are \(0\) (three), \(2n\) (one), and \(n\) (\(2n-4\)). These multiplicities remain valid at \(n=2\), when the final block is empty. In particular,
\[
 \boxed{\mathbb E\!\left[\sum_{k=0}^{n-1}\frac{(I_k-O_k)^2}{2n b_k}\right]=n-2.}
\]

## Assumptions and scope
The arcs in opposite directions for a fixed vertex pair are **independent**, both may occur, and loops are forbidden. There is no conditioning on total arcs or connectedness. Probabilities satisfy \(0<p<1\), ensuring every \(b_k\) is positive. The statistics concern two marginal histograms, not the joint distribution of the in-degree/out-degree pair at each vertex. The result is a finite-sample covariance statement; it does not imply a chi-square limiting law.

## Proof
First, the incoming arc sets at different vertices are disjoint, so their in-degrees are independent and each has law \(\operatorname{Bin}(n-1,p)\). Hence
\[
 \operatorname{Cov}(I_k,I_l)=n(\delta_{kl}b_k-b_kb_l).
\]
The same holds for the out-degree histogram \(O\), because outgoing arc sets at different vertices are disjoint.

For the mixed block, an in-degree at vertex \(i\) and an out-degree at vertex \(j\) are independent when \(i=j\); the two sets of incident arcs then have no common directed edge. When \(i\ne j\), exactly one arc \(j\to i\) is shared. Conditioning on that Bernoulli arc leaves all other incident arcs independent and each residual degree has law \(\operatorname{Bin}(n-2,p)\). Define \(h_k=\mathbb P(\operatorname{Bin}(n-2,p)=k)\) and set \(h_{-1}=h_{n-1}=0\). The law of total covariance gives
\[
 \operatorname{Cov}(\mathbf1\{\deg^-(i)=k\},\mathbf1\{\deg^+(j)=l\})
 =p(1-p)(h_{k-1}-h_k)(h_{l-1}-h_l),\qquad i\ne j.
\]
Consequently
\[
 \operatorname{Cov}(I_k,O_l)=n(n-1)p(1-p)a_ka_l,\quad
 a_k=h_{k-1}-h_k=\frac{b_k(k-(n-1)p)}{(n-1)p(1-p)}.
\]
After conjugating by \(D^{-1/2}\), the diagonal blocks become \(n(\operatorname{Id}-uu^\top)\) and the mixed blocks become \(nvv^\top\), proving the displayed matrix identity. Binomial normalization gives \(u^\top u=v^\top v=1\) and \(u^\top v=0\).

The three mutually orthogonal zero modes are \((u,0)\), \((0,u)\), and \((v,-v)\). The mode \((v,v)\) has eigenvalue \(2n\). Every vector orthogonal to these four directions has eigenvalue \(n\), which completes the spectrum. The zero modes correspond respectively to \(\sum_k I_k=n\), \(\sum_k O_k=n\), and \(\sum_k kI_k=\sum_k kO_k\) (both latter sums count all directed arcs).

Finally \(\mathbb E[I_k-O_k]=0\), and the whitened difference block has covariance \(2n(\operatorname{Id}-uu^\top-vv^\top)\). Taking its trace, dividing by \(2n\), and using orthonormality yields \(n-2\). No asymptotic or probabilistic normal approximation is required.

## Verification
The accompanying standalone `verify.py` exhaustively enumerates every directed graph on \(n=2,3,4\) vertices, at each of the two rational probabilities \(p=1/3\) and \(p=2/3\). It computes the complete joint degree-histogram covariance with exact rational arithmetic, compares every entry against the theorem, and checks the Pearson-contrast expectation. This totals \(2(2^2+2^6+2^{12})=8{,}328\) graph-probability cases. Execute `python3 verify.py` from the extracted file directory. Finite enumeration supports, but does not replace, the proof for all \(n\).

## Relationship to prior work
Chen and Olvera-Cravioto (2012, arXiv:1207.2475v1) treat directed random graphs with prescribed in-/out-degree distributions via a configuration model. Their degree balancing and asymptotic graphicality results are for a different probability mechanism and do not state the present exact Bernoulli-arc histogram covariance spectrum. Wang and Resnick (2015, arXiv:1510.00290v1) prove asymptotic normality of joint in-/out-degree **pair** counts in a directed preferential-attachment process; their dependent growing-network model and limiting covariance do not provide the exact finite identity here. The older McKay–Wormald treatment of undirected random-graph degree sequences addresses asymptotic degree-sequence approximations, not this paired directed histogram projection. The elementary one-shared-arc covariance mechanism is classical; the proposed contribution is its exact two-histogram spectral reduction and finite goodness-of-fit consequence, not a claim to discover degree-count dependence.

## Limitations
The result is restricted to independent arcs without loops. It does not apply unchanged to random tournaments, reciprocated dyad dependence, conditioned edge totals, or directed configuration models. It does not determine the distribution or asymptotic normality of the Pearson-contrast statistic. Historical literature on row- and column-sum contingency statistics could implicitly contain equivalent finite covariance formulas; independent historical-priority assessment remains warranted.

## References
1. N. Chen and M. Olvera-Cravioto, *Directed Random Graphs with Given Degree Distributions*, arXiv:1207.2475v1, first posted 2012-07-10, https://arxiv.org/html/1207.2475v1.
2. T. Wang and S. I. Resnick, *Asymptotic Normality of In- and Out-Degree Counts in a Preferential Attachment Model*, arXiv:1510.00290v1, first posted 2015-10-01, https://arxiv.org/html/1510.00290v1.
3. B. D. McKay and N. C. Wormald, *The degree sequence of a random graph. I. The models*, Random Structures & Algorithms **11** (1997), 97–117, https://research.monash.edu/en/publications/the-degree-sequence-of-a-random-graph-i-the-models.
