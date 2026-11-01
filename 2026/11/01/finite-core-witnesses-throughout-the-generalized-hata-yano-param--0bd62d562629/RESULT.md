# Finite core witnesses throughout the generalized Hata–Yano parameter interval

## Finding

For every real parameter \(0<\delta\leq 1/6\), the generalized Hata–Yano random interval map of Nakamura--Nakano--Toyokawa--Yano has a choice of core and an explicit finite, irreducible, stationary core probability assigning positive mass to both outer core strips. The core is a reflected simple random walk on a path of even order. This answers the generalized Hata–Yano portion of Problem 1.7 of the 2022 preprint [1] (renumbered Problem 1.8 in the 2023 revision) for every nonzero allowed parameter, including \(0<\delta<1/8\), which is not covered by the deterministic-core construction in [1]. It does not answer the separate question there about arbitrary piecewise-linear Gharaei--Homburg maps.

By Theorem 1.2 and Remark 1.5 of [1], for each of the finitely many explicitly given deterministic initial points, the fraction of time in the right half of the original random interval map converges in distribution to the ordinary arcsine law with density \(1/(\pi\sqrt{u(1-u)})\) on \((0,1)\). The limit-law theorem itself belongs to [1]; the newly established result is the verification of its previously unresolved core-measure hypothesis for all generalized Hata–Yano parameters.

## Assumptions and scope

Fix \(\delta\in(0,1/6]\). On \([0,1]\), independently choose with equal probabilities the maps

\[
 f_0(x)=\begin{cases}x/2,&0\leq x<1/2+\delta,\\ 2x-1,&1/2+\delta\leq x\leq1,\end{cases}
 \qquad
 f_1(x)=\begin{cases}2x,&0\leq x<1/2-\delta,\\ (x+1)/2,&1/2-\delta\leq x\leq1.\end{cases}
\]

These are exactly the generalized Hata–Yano maps in [1, Section 1.2.2]. Choose any integer \(r\geq1\) sufficiently large that
\[
 a:=\frac{1}{3\cdot2^r}<4\delta.
\]
Choose a core parameter \(c\) satisfying
\[
 a<c<\min\{2a,4\delta\};
\]
for example, the midpoint of the two displayed bounds. Define
\[
 I^-=[c/2,c),\quad I^0=[c,1-c),\quad I^+=[1-c,1-c/2),\quad Y=[c/2,1-c/2).
\]
With \(g_0=f_0|_{[c,1-c/2)}\), \(g_1=f_1|_{[c/2,1-c)}\), the core transformations are the maps of [1, equation (1.4)]:
\[
 h_0(x)=\begin{cases}g_1(x),&x\in I^-,\\g_0(x),&x\in I^0\cup I^+,\end{cases}
 \qquad
 h_1(x)=\begin{cases}g_1(x),&x\in I^-\cup I^0,\\g_0(x),&x\in I^+.\end{cases}
\]
The chosen \(c\) satisfies \(0<c<1/3\) and \(c<4\delta\). The restriction ranges required by [1, equation (1.3)] do hold: \(g_0([c,1-c/2))\subset[c/2,1-c)\) and \(g_1([c/2,1-c))\subset[c,1-c/2)\). In particular \(h_0,h_1:Y\to Y\) are defined on the full half-open core.

## Proof

**Core admissibility.** Since \(c<2a\leq1/3\) and \(\delta\leq1/6\), the external formulas of [1, equation (1.3)] hold on \([0,c)\), \([0,c/2)\), \([1-c/2,1]\) and \([1-c,1]\), respectively. On the remaining restriction of \(f_0\), the lower values from the right branch are at least \(2\delta>c/2\), whereas the upper values from the left branch are at most \(1/4+\delta/2\leq1/3<1-c\); the right branch ends below \(1-c\). On the remaining restriction of \(f_1\), the left branch begins at \(c\) and ends below \(1-2\delta\leq1-c/2\), whereas the right branch begins at \(3/4-\delta/2\geq2/3>c\) and ends below \(1-c/2\). All range bounds hold also at the declared branch boundaries. Thus the stipulated core is valid.

**Finite path.** Write
\[
 x_j=2^j a\quad(0\leq j\leq r),\qquad x_r=1/3,
\]
set \(L=2r+2\), and order the \(L\) distinct points by
\[
 v_j=x_j\quad(0\leq j\leq r),\qquad v_{r+1+k}=1-x_{r-k}\quad(0\leq k\leq r).
\]
All lie in \(Y\), because \(a\in(c/2,c)\), the remaining left points lie in \([c,1/3]\subset I^0\), their reflections lie in \(I^0\cup I^+\), and \(1-a\in I^+\). In fact \(I^-\cap\{v_j\}=\{v_0\}\) and \(I^+\cap\{v_j\}=\{v_{L-1}\}\).

The branch formulas give
\[
 h_0(v_0)=h_1(v_0)=v_1,\qquad
 h_0(v_{L-1})=h_1(v_{L-1})=v_{L-2},
\]
and, for each \(1\leq j\leq L-2\),
\[
 h_0(v_j)=v_{j-1},\qquad h_1(v_j)=v_{j+1}.
\]
To check the only delicate central transitions, \(h_1(1/3)=2/3\) and \(h_0(2/3)=1/3\) hold throughout \(0<\delta\leq1/6\), including equality at \(\delta=1/6\) where the corresponding branch switches occur exactly at these points. At all other left interior points the two selected affine branches are \(x\mapsto x/2\) and \(x\mapsto2x\); the right-side transitions are their reflections.

Thus the core random iteration restricted to the finite set is exactly the reflecting simple symmetric nearest-neighbor walk on the length-\(L\) path, with deterministic steps inward from its endpoints. This chain is irreducible (though of period two). Let
\[
 w_j=\begin{cases}\dfrac{1}{2(2r+1)},&j=0\ \text{or}\ j=L-1,\\[3pt]
 \dfrac{1}{2r+1},&1\leq j\leq L-2.\end{cases}
\]
Detailed balance holds along every edge because the inward transition probability at an endpoint is one and the outward transition probability at its neighboring vertex is one half; along every other edge both probabilities are one half. Since \(\sum_jw_j=1\),
\[
 \nu_\delta=\sum_{j=0}^{L-1}w_j\,\delta_{v_j}
\]
is stationary for the averaged pushforward operator \((h_0)_*/2+(h_1)_*/2\). Irreducibility implies the annealed metric transitivity required in [1]: any two positive-\(\nu_\delta\) Borel sets contain path vertices connected by a finite word of core maps, which has positive selection probability. Finally,
\[
 \nu_\delta(I^-)=\nu_\delta(I^+)=\frac{1}{2(2r+1)}>0.
\]
This verifies every hypothesis of [1, Theorem 1.2]. By that theorem and its Remarks 1.3 and 1.5, the stated ordinary arcsine limit law holds when starting at any \(v_j\). This last inference invokes an established limit theorem; it is not an independent reproof.

## Verification

The accompanying self-contained `core_path_checker.py` uses exact rational arithmetic to reconstruct the finite path and stationary weights for several rational parameters, including tiny values, dyadic transition values, \(1/8\) and the endpoint \(1/6\). It checks both core transformations at every support point, the Markov transitions, the full stationary vector, membership in the half-open core and the two positive outer-strip masses. The continuous-parameter assertion is proved above by inequalities, not by numerical sampling.

## Relationship to prior work

The source [1] defines the core maps, proves the conditional generalized arcsine law in Theorem 1.2, and explicitly poses Problem 1.7 of the 2022 preprint (Problem 1.8 of the revision), asking whether the required core probability exists for all nonzero generalized Hata–Yano parameters and for an additional distinct family of piecewise-linear Gharaei--Homburg maps. Section 1.2.2 of [1] exhibits deterministic-core measures for \(\delta\geq1/8\) but does not construct measures for every \(0<\delta<1/8\). The present finite reflecting-path construction supplies those missing witnesses for **all** nonzero generalized Hata–Yano parameters. It also produces a concrete symmetric, finite-supported initial distribution for their previously established arcsine law.

Hata--Yano [2] studies the earlier unperturbed model \(\delta=0\) via a countable Markov partition, so that result neither constructs the nonzero-parameter core probabilities nor supplies this particular finite path. Inoue--Toyokawa [3] concerns Lebesgue-equivalent, often infinite, invariant measures of random piecewise-convex maps, a different object from the atomic stationary probabilities of this induced core. Literature and indexed-record searches did not locate an equivalent construction; that negative search result is not proof of publication priority.

## Limitations

The second half of Problem 1.7 (arbitrary piecewise-linear Gharaei--Homburg maps) remains unresolved here. The construction establishes existence, not uniqueness, and its number of atoms can grow as the parameter tends to zero. The arcsine convergence follows from the cited source for initial points in the displayed finite support (or distributions absolutely continuous with respect to the constructed \(\nu_\delta\)); no claim of pointwise convergence for every initial point or of a new limit theorem is made. Independent scientific validation and exhaustive priority checking have not been performed.

## References

[1] F. Nakamura, Y. Nakano, H. Toyokawa, K. Yano, *Arcsine law for random dynamics with a core*, arXiv:2206.00226, first posted 2022-06-01; *Nonlinearity* 36 (2023), 1491–1509. Relevant: equations (1.3)--(1.4), Theorem 1.2, Remarks 1.3 and 1.5, Section 1.2.2, Problem 1.7 of the original preprint (Problem 1.8 in the revision). https://arxiv.org/abs/2206.00226

[2] G. Hata, K. Yano, *Arcsine and Darling--Kac laws for piecewise linear random interval maps*, arXiv:2108.01332, first posted 2021-08-03. https://arxiv.org/abs/2108.01332

[3] T. Inoue, H. Toyokawa, *Invariant measures for random piecewise convex maps*, arXiv:2303.10873, first posted 2023-03-20. https://arxiv.org/abs/2303.10873
