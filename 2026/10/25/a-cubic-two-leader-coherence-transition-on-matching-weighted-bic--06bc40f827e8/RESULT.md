# A cubic two-leader coherence transition on matching-weighted bicliques

## Finding

Let \(n\geq3\) be an integer, let \(t\geq0\) be real, and partition \(2n\) vertices into \(U=\{u_1,\ldots,u_n\}\) and \(V=\{v_1,\ldots,v_n\}\). Give each cross-part edge \(u_i v_j\) conductance \(1\) when \(i\ne j\), and conductance \(t\) when \(i=j\); there are no within-part edges. When \(t=0\), the zero-conductance matching is absent. The graph is connected for every specified parameter. For any unordered pair of noise-free leaders \(S\), let \(F\) be its complement and define the unscaled grounded-Laplacian coherence
\[
 C(S)=\operatorname{tr}\bigl(L_{FF}^{-1}\bigr).
\]

Define the cubic
\[
 P_n(t)=2(n+2)t^3+(4n^2-n-14)t^2+2(n-2)(n^2-n-4)t-(n-2)(n^2-3).
\]
It has exactly one nonnegative root \(c_n\), and \(0<c_n<1/2\). **The complete optimal two-leader classification** is:

* If \(0\leq t<c_n\), the only optimal sets are the \(n\) matched cross-part pairs \(\{u_i,v_i\}\).
* If \(t=c_n\), precisely those \(n\) matched pairs and the \(n(n-1)\) same-part pairs are optimal (\(n^2\) sets altogether).
* If \(t>c_n\), precisely the \(n(n-1)\) pairs contained in one part are optimal.

No unmatched cross-part pair \(\{u_i,v_j\}\), \(i\ne j\), minimizes coherence for any \(t\geq0\). The exact minimum at any parameter is given by the formula in the proof, applied to the winning pair type.

There is a distinct and strictly smaller transition for the resistance-maximizing pair:
\[
 r_n=\frac{\sqrt{n(n-2)}-(n-2)}2,
 \qquad 0<r_n<c_n<\frac12.
\]
For \(r_n<t<c_n\), same-part pairs uniquely maximize effective resistance but matched cross-part pairs uniquely minimize coherence. Thus **a resistance-maximizing pair need not be a coherence-optimal pair even though the network is vertex-transitive and all nodes have equal information centrality**. At \(n=3\), \(t=2/5\), the exact differences are
\[
 R_{\rm same}-R_{\rm matched}=\frac1{108}>0,
 \qquad C_{\rm same}-C_{\rm matched}=\frac5{342}>0.
\]
As \(n\to\infty\), the disagreement interval has the sharp width asymptotic
\[
 \lim_{n\to\infty}n(c_n-r_n)=\frac14.
\]

## Assumptions and scope

All conductances are symmetric. The Laplacian is the **unnormalized weighted combinatorial Laplacian** \(L=D-A\); no degree normalization is used. The two noise-free leaders are pinned at zero, while the \(2n-2\) followers retain the original diagonal Laplacian degrees. The stationary total variance under independent unit-intensity white noise is \(C(S)/2\), so minimizing this physically scaled variance is equivalent to minimizing \(C(S)\). Effective resistances use reciprocal conductances. The result concerns exactly two leaders, not noisy leaders or heterogeneous edge weights beyond the stated matching weight.

## Proof

Write \(N=2n\), \(p=n-2+2t\) and \(q=2(n-1+t)\). The \(n\times n\) cross-part adjacency block is \(J_n+(t-1)I_n\), so the nonzero eigenvalues of \(L\) are \(p\) with multiplicity \(n-1\), \(n\) with multiplicity \(n-1\), and \(q\) with multiplicity one. All are positive for \(n\geq3\), \(t\geq0\). In particular, the graph is connected.

Let \(H=L^+\) be the Moore–Penrose inverse, whose diagonal entries have the common value \(d\) by vertex transitivity. For distinct vertices \(a,b\), define
\[
 R_{ab}=(e_a-e_b)^TH(e_a-e_b),\quad
 B_{ab}=(e_a-e_b)^TH^2(e_a-e_b).
\]
To derive a two-leader identity, first pin vertex \(a\). On the remaining vertices the Green matrix has entries \(U_{ij}=H_{ij}-H_{ia}-H_{aj}+d\). Its trace is \(2Nd\), since \(H\mathbf1=0\) and \(H_{ii}=d\). Moreover \(U_{bb}=R_{ab}\). Pinning \(b\) is a Schur-complement update, so
\[
 C(\{a,b\})=\operatorname{tr}(U)-\frac{\|U_{\cdot b}\|^2}{U_{bb}}
 =2\operatorname{tr}(H)-\frac{B_{ab}}{R_{ab}}-\frac{N}{4}R_{ab}.
\]
Here the zero-padded column \(U_{\cdot b}=H(e_b-e_a)+(R_{ab}/2)\mathbf1\) has squared norm \(B_{ab}+NR_{ab}^2/4\). Thus minimizing coherence is equivalent to maximizing \(\Phi=B/R+nR/2\).

There are exactly three pair orbits: **same** (two vertices in one part), **matched** (\(u_i,v_i\)), and **cross** (\(u_i,v_j\) with \(i\ne j\)). Decompose each vector \(e_a-e_b\) into the restricted antisymmetric \(p\)-eigenspace, restricted symmetric \(n\)-eigenspace, and bipartition-sign \(q\)-eigenspace. Their squared-projection weights in that order are
\[
 \begin{array}{c|ccc}
 &p&n&q\\\hline
 \mathrm{same}&1&1&0\\
 \mathrm{matched}&2-2/n&0&2/n\\
 \mathrm{cross}&1-2/n&1&2/n
 \end{array}.
\]
Consequently the resistance \(R\) and biharmonic quadratic form \(B\) for each orbit are obtained by dividing the tabulated weights by \(p,n,q\) and by their squares, respectively:
\[
\begin{aligned}
 R_s&=1/p+1/n,& B_s&=1/p^2+1/n^2,\\
 R_m&=(2-2/n)/p+2/(nq),&B_m&=(2-2/n)/p^2+2/(nq^2),\\
 R_x&=(1-2/n)/p+1/n+2/(nq),&B_x&=(1-2/n)/p^2+1/n^2+2/(nq^2).
\end{aligned}
\]
These formulas give the explicit coherence for every type via
\[
 C_\alpha=2\left((n-1)/p+(n-1)/n+1/q\right)-\Phi_\alpha,
 \qquad \Phi_\alpha=B_\alpha/R_\alpha+nR_\alpha/2.
\]
Exact simplification gives
\[
 \Phi_m-\Phi_s=-\frac{P_n(t)}{n(n+t-1)(n+2t-2)(2n+2t-3)}
\]
and
\[
 \Phi_s-\Phi_x=\frac{(n-2)t^2+[2n(n-1)+4]t+n(n-1)^2-2}
 {(n+t-1)(n+2t-2)(2n^2+4nt-5n+2t^2-4t+2)}.
\]
Every denominator is positive: each linear factor is positive, while the final quadratic polynomial equals \(n(n+t-1)(n+2t-2)R_x\), which is positive. The last numerator is strictly positive because each coefficient is positive for \(n\geq3\). Hence \(\Phi_s>\Phi_x\) throughout. The coefficient of \(t^3\), of \(t^2\), and of \(t\) in \(P_n\) is strictly positive for \(n\geq3\). Thus \(P_n\) is strictly increasing on \([0,\infty)\), with \(P_n(0)=-(n-2)(n^2-3)<0\) and \(P_n(1/2)=n-1>0\). This proves uniqueness of \(c_n\) and the entire coherence classification, including the exact tie counts.

To compare effective resistance, the same spectral formulas yield
\[
 R_m-R_s=-\frac{Q_n(t)}{n(n+t-1)(n+2t-2)},\quad
 Q_n(t)=2t^2+2(n-2)t-(n-2),
\]
and
\[
 R_s-R_x=\frac1{(n+t-1)(n+2t-2)}>0.
\]
The sole nonnegative root of \(Q_n\) is \(r_n\) as stated. Polynomial division gives the exact identity
\[
 P_n(t)=A_n(t)Q_n(t)-\frac{n(n-2)}2
\]
where \(A_n(t)=n^2+(n+2)t-n/2-3\), hence \(P_n(r_n)=-n(n-2)/2<0\), proving \(r_n<c_n\) and the disagreement interval. Direct substitution proves the displayed rational witness.

Finally \(P_n'(t)/n^3\to2\) uniformly for \(t\in[0,1/2]\). By the mean-value theorem, \(1/2-c_n=P_n(1/2)/P_n'(\xi_n)\sim1/(2n^2)\) for some \(\xi_n\in(c_n,1/2)\). The explicit radical implies \(1/2-r_n\sim1/(4n)\). Subtracting proves the limit of \(n(c_n-r_n)\).

## Verification

Run `python verify.py` after installing the single listed dependency in `requirements.txt`. The program performs exact SymPy simplification of the two \(\Phi\)-gap identities, the resistance-gap identities, and the cubic division identity. It also forms rational grounded Laplacians directly and verifies \(1470\) exact pairwise inverse-trace identities for \(3\leq n\leq7\) and six nonnegative rational matching weights per order. All three pair orbits, optimal-pair comparisons, and the \((n,t)=(3,2/5)\) rational witness are checked. The infinite-family proof uses the displayed identities and positivity arguments; finite computations alone would not prove it.

## Relationship to prior work

Fitch and Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569 (first posted 7 July 2014), derive joint-centrality formulas for general graphs, including contributions from both resistance and biharmonic distance, and solve cycle/path cases. Their general identity underlies the score reduction here but does **not** give this matching-weighted biclique cubic classification. A resistance-only inference for equal-information-centrality vertices, stated informally in that paper, is insufficient in the present family: the explicit rational witness distinguishes the two objectives without challenging their general joint-centrality formula.

Patterson, Yi, and Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873 (first posted 23 August 2017), derive resistance-based coherence identities and explicit results for paths, cycles, and tree cases. Their inspected results and appendices do not include matching-weighted complete bipartite graphs. Previous exact six-vertex weighted-circulant disagreement findings involve a different conductance family and do not imply this all-order cubic threshold or its \(1/(4n)\) width law. A general spectral formula alone does not amount to an implicit proof of the orbit comparisons, strict cubic threshold, and all-optima counts given here.

## Limitations

The classification holds only for precisely the stated uniform cross conductances and one uniform matching conductance; it is not an assertion about arbitrary weighted bipartite graphs, noisy leaders, or three or more leaders. The asymptotic statement concerns the width of the disagreement interval, not a universal phenomenon on vertex-transitive graphs. The proof and finite verification are internal mathematical checks, not independent verification. An unindexed special-case result or a stronger result not captured by the inspected primary sources could affect the originality assessment.

## References

1. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, first submission 2014-07-07, https://arxiv.org/abs/1407.1569; see the two-leader corollary and cycle/path sections.
2. S. Patterson, Y. Yi, and Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873, first submission 2017-08-23, https://arxiv.org/abs/1708.06873; see grounded-inverse theory and special-family results.
3. A. Clark, L. Bushnell, and R. Poovendran, *On Leader Selection for Performance and Controllability in Multi-Agent Systems*, IEEE CDC 2012, DOI:10.1109/CDC.2012.6426973 (background on grounded-Laplacian objective and algorithms).
