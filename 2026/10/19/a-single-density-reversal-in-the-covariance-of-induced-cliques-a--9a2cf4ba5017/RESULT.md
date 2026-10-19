# A single density reversal in the covariance of induced cliques and one-edge-defect cliques

## Finding
Fix integers \(r\ge3\) and \(n\ge r+1\). In the binomial random graph \(G(n,p)\), let \(Y_r\) be the number of \(r\)-vertex subsets inducing a clique, and let \(X_r\) be the number inducing a graph with exactly one absent edge. There is **exactly one** \(p_{n,r}\in(0,1)\) such that
\[
\operatorname{Cov}(X_r,Y_r)>0\quad(0<p<p_{n,r}),\qquad
\operatorname{Cov}(X_r,Y_r)<0\quad(p_{n,r}<p<1).
\]
At the threshold the covariance equals zero. With \(a=\binom r2\), the threshold satisfies
\[
0<p_{n,r}<1-\frac1a,
\qquad p_{r+1,r}=\left(\frac2{r+1}\right)^{1/\binom{r-1}2},
\]
and for every fixed \(r\) as \(n\to\infty\),
\[
p_{n,r}=1-\frac1a-\frac{(r-2)^2(3a-1)}{3a(a-1)^2}\frac1n+O_r(n^{-2}).
\]
For \(r=3\), this transition is exactly \(p_{n,3}=2(n-3)/(3n-8)\). For \(n=r\), the two counts are mutually exclusive and their covariance is negative throughout \(0<p<1\); thus the condition \(n\ge r+1\) is necessary.

## Assumptions and scope
Graphs are simple, undirected, labeled on \([n]\); their \(\binom n2\) edge indicators are independent Bernoulli\((p)\). Each induced motif is counted once per vertex subset, not once per labeling or automorphism. Both \(r\) and \(n\) are integer; \(p\) lies strictly between zero and one. An \(r\)-vertex near-clique means **exactly** one missing edge; no condition is imposed on edges joining the subset to the outside. All stated sign assertions are strict except at their stated zero. The asymptotic is for fixed \(r\), not for \(r\) growing with \(n\).

## Proof
Put \(a=\binom r2\), \(b_s=\binom s2\), and \(A_s=\binom rs\binom{n-r}{r-s}\), interpreting an out-of-range binomial coefficient as zero. Let \(I_S\) indicate the one-edge-defect event on an \(r\)-subset \(S\), and \(J_T\) the clique event on an \(r\)-subset \(T\). For \(|S\cap T|=s\le1\), the indicators depend on disjoint edge sets and are independent.

For \(2\le s\le r\), a common-edge set has \(b_s\) edges. Under \(J_T=1\), those edges must be present. The sole missing edge for \(I_S=1\) must therefore lie among the \(a-b_s\) edges of \(S\) outside their overlap. Independence gives
\[
\mathbb E[I_SJ_T]=(a-b_s)(1-p)p^{2a-b_s-1},\quad
\mathbb EI_S=a(1-p)p^{a-1},\quad \mathbb EJ_T=p^a.
\]
Consequently the **exact finite covariance** is
\[
\boxed{\operatorname{Cov}(X_r,Y_r)=\binom nr(1-p)p^{a-1}
\sum_{s=2}^{r} A_s\left[(a-b_s)p^{a-b_s}-ap^a\right].}
\]
This also covers \(s=r\): the product \(I_SJ_S\) is identically zero.

Since \(0<p<1\), the sign equals the sign of
\[
F_{n,r}(p)=\sum_{s=2}^{r-1} A_s(a-b_s)p^{-b_s}-a\sum_{s=2}^{r}A_s.
\]
Its derivative is
\[
F'_{n,r}(p)=-\sum_{s=2}^{r-1} A_s(a-b_s)b_s p^{-b_s-1}<0.
\]
Indeed \(A_{r-1}=r(n-r)>0\) and \(a>b_{r-1}\). Thus \(F\) decreases strictly; the \(r-1\) term yields \(F(0+)=+\infty\), while \(F(1)=-\sum_{s=2}^{r}A_sb_s<0\). There is exactly one simple crossing.

Put \(p_0=1-1/a\). Bernoulli's inequality yields \(p_0^{b_s}\ge1-b_s/a\), strictly for \(b_s\ge2\), so every \((a-b_s)p_0^{-b_s}-a\le0\), and the \(s=r\) term is strictly negative. Hence \(F(p_0)<0\) and \(p_{n,r}<p_0\).

If \(n=r+1\), only overlaps \(s=r-1,r\) occur. The equation \(F=0\) is \(r(r-1)p^{a-b_{r-1}}=a(r+1)p^a\), giving \(p^{\binom{r-1}2}=2/(r+1)\).

For fixed \(r\) and \(n\to\infty\), write \(g_s(p)=(a-b_s)p^{a-b_s}-ap^a\). The sign equation becomes \(A_2g_2(p)+A_3g_3(p)+O_r(A_2 n^{-2})=0\), uniformly on a fixed neighborhood of \(p_0\), because \(A_s/A_2=O_r(n^{-(s-2)})\) for \(s\ge4\). Also \(A_3/A_2=(r-2)^2/[3(n-2r+3)]=(r-2)^2/(3n)+O_r(n^{-2})\), \(g_2(p_0)=0\), \(g'_2(p_0)=-(a-1)p_0^{a-2}\ne0\), and \(g_3(p_0)=-(3a-1)p_0^{a-3}/a^2\). Strict monotonicity and these uniform expansions give \(p_{n,r}=p_0+O_r(n^{-1})\), and a one-term Taylor expansion gives the coefficient stated in the Finding. For \(r=3\), the same algebra is valid: the \(s=3\) term is the \(s=r\) diagonal contribution.

## Verification
The accompanying `verify.py` contains two independent finite computations: an exact-rational edge-state enumeration on all graphs of orders four through six for selected motif sizes and probabilities, and independent overlap-formula evaluations over integer ranges. It also checks the sign boundary, the \(n=r+1\) root, and fixed-\(r\) asymptotic predictions by numerical bisection. Run `python verify.py` using Python 3; no nonstandard dependencies are needed. These finite computations test but do not establish the infinite-parameter theorem, which follows from the proof above.

## Relationship to prior work
Classical work on subgraph statistics establishes overlap decompositions, marginal motif counts, and asymptotic limit laws. Picard, Daudin, Koskas, Schbath, and Robin (2008) give an analytic mean/variance procedure for motif counts; an author presentation explicitly formulates motif self-overlap moments, without stating the present mixed clique/defect-clique sign threshold. Coulson, Gaunt, and Reinert (2015 preprint) examine Poisson approximations for counts of copies of a fixed graph, not this induced mixed covariance or a density crossing. Harshaw and coauthors (2016 preprint) employ induced graphlet count vectors for detection, but provide no corresponding exact covariance sign theorem. General earlier subgraph fluctuation frameworks could in principle imply the finite overlap expression; the claim of additional substance here is the **all-size strict uniqueness theorem and the first-order location of its zero**.

## Limitations
The probability model assumes independent edges; the theorem does not transfer automatically to fixed-edge-count, correlated-edge, or configuration-model graphs. It concerns exactly one absent edge and fixed motif order, not arbitrary induced pairs of patterns. The analytic finite overlap formula is a specialization of standard moment methodology rather than a new general enumeration principle. Full copies of Janson's 1990 treatment and the 2008 Picard article were not available for full comparison; implicit earlier results on joint motif covariance and sign could remain. The presentation of the earlier method and accessible primary articles do not establish exhaustive novelty. Independent scientific review has not occurred.

## References
- F. Picard, J.-J. Daudin, M. Koskas, S. Schbath, and S. Robin, *Assessing the Exceptionality of Network Motifs*, Journal of Computational Biology **15** (2008), 1–20. DOI: 10.1089/cmb.2007.0137. Author presentation: https://franckpicard.github.io/assets/pdf/presentations/netmotifs.pdf.
- M. Coulson, R. E. Gaunt, and G. Reinert, *Poisson approximation of subgraph counts in stochastic block models and a graphon model*, preprint arXiv:1509.07754 (first submitted September 25, 2015), https://arxiv.org/abs/1509.07754.
- C. R. Harshaw et al., *GraphPrints: Towards a Graph Analytic Method for Network Anomaly Detection*, preprint arXiv:1602.01130 (first submitted February 2, 2016), https://arxiv.org/abs/1602.01130.
- S. Janson, *A functional limit theorem for random graphs with applications to subgraph count statistics*, Random Structures & Algorithms **1** (1990), 15–37, DOI: 10.1002/rsa.3240010103.
- C. Fretter, M. Müller-Hannemann, and M.-T. Hütt, *Subgraph fluctuations in random graphs*, Physical Review E **85** (2012), 056119, DOI: 10.1103/PhysRevE.85.056119.
