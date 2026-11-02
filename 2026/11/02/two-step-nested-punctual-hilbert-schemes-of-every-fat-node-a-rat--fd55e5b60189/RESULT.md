# Two-step nested punctual Hilbert schemes of every fat node: a rational Euler series

## Finding

For positive integers \(u,v\), let
\[
R_{u,v}=\mathbb C[[x,y]]/(x^u y^v).
\]
For every integer \(n\ge0\), let \(\mathcal N_n(u,v)\) be the punctual incidence scheme of pairs of finite-colength ideals \(I\subset J\subset R_{u,v}\) satisfying
\[
\dim_{\mathbb C}(R_{u,v}/I)=n+2,\qquad
\dim_{\mathbb C}(R_{u,v}/J)=n.
\]
This is the **unweighted two-step** nested Hilbert scheme: it does not include a choice of an intermediate ideal of colength \(n+1\). Write
\[
Z_{u,v}(q)=\sum_{n\ge0}\chi_c(\mathcal N_n(u,v))q^n,
\qquad (q;q)_k=\prod_{j=1}^{k}(1-q^j).
\]
Define rational functions \(P_k,D_k,T_k\) for \(k\ge0\), with \(P_{-1}=D_{-1}=T_{-1}=0\), by
\[
P_k=\frac{1}{(q;q)_k},\qquad
D_k=P_k\sum_{j=1}^{k}q^j,
\]
\[
T_k=P_k\left[
\sum_{1\le i<j\le k}q^{i+j}
+\sum_{j=1}^{k}q^{2j}
+\sum_{j=2}^{k}q^j(1-q^{j-1})\right].
\]
Here \(P_0=1\) and \(D_0=T_0=0\). Then, **for every** \(u,v\ge1\),
\[
\boxed{\begin{aligned}
Z_{u,v}(q)=\frac1{q^2}\Bigg\{&
\sum_{r=0}^{v}q^{ur}\bigl[
(T_r-T_{r-1})P_u
+(P_r-P_{r-1})T_u
+(D_r-D_{r-1})D_u\bigr]\\
&+P_{u-1}\sum_{r=1}^{v}q^{(u+1)r}P_{r-1}
\Bigg\}.\end{aligned}}
\]
The apparent negative power cancels. The answer is a rational function with denominator dividing \((q;q)_u(q;q)_v\), and it obeys \(Z_{u,v}=Z_{v,u}\).

The first genuinely nonreduced symmetric node gives the explicit closed expression
\[
\boxed{Z_{2,2}(q)=\frac{2-q+2q^3+q^4+q^5+3q^6+2q^8}{(1-q)^2(1-q^2)^2}.}
\]
Its first eleven coefficients, for \(n=0,1,\ldots,10\), are
\[
2,3,8,13,25,39,66,97,149,207,294.
\]
For each fixed positive pair \((u,v)\), the large-colength growth is
\[
\boxed{\chi_c(\mathcal N_n(u,v))
\sim\frac{(u+v)(u+v+1)}{2u!v!(u+v-1)!}\,n^{u+v-1}.}
\]
The leading asymptotic is understood as \(n\to\infty\) with \(u,v\) fixed.

## Assumptions and scope

All schemes and Euler characteristics are over \(\mathbb C\); \(\chi_c\) denotes compactly supported topological Euler characteristic. The punctual schemes parametrize ideals in the complete local ring of the plane-curve germ, equivalently length-supported subschemes of a sufficiently large infinitesimal neighborhood of the origin. The two-step incidence is the reduced or nonreduced scheme defined by the usual closed ideal-inclusion relation; Euler characteristic depends only on its underlying topological space. The variables \(u,v\) are **positive** integers and \(n\) is any nonnegative integer.

## Proof

**1. Reduction to pairs of diagrams.** The two-dimensional algebraic torus acts by scaling \(x\) and \(y\), preserves \(x^uy^v\), and hence acts on each punctual incidence scheme. These schemes are of finite type and proper (a closed incidence locus in products of punctual Hilbert--Chow fibers). Torus localization for topological Euler characteristic gives \(\chi_c(\mathcal N_n)=\chi_c(\mathcal N_n^{(\mathbb C^*)^2})\). Each torus-stable finite-colength ideal is monomial, since its torus weight spaces in the ambient power-series ring are one-dimensional. Such ideals are encoded by Young diagrams \(\lambda\), with cell \((i,j)\) corresponding to the monomial \(x^iy^j\) absent from the ideal. The relation \(x^uy^v\in I_\lambda\) means exactly that \((u,v)\notin\lambda\), equivalently \(\lambda_v\le u\) with zero-indexed row \(v\). If \(I_\lambda\subset I_\mu\), then \(\mu\subset\lambda\); the colength difference is \(|\lambda|-|\mu|=2\). Thus the desired coefficient is the number of pairs of partitions \(\mu\subset\lambda\) with \(|\mu|=n\), \(|\lambda|=n+2\), and \(\lambda_v\le u\).

**2. Two-box deletion statistic.** For a partition \(\lambda\), write \(d(\lambda)\) for the number of distinct positive part sizes, \(h(\lambda)\) for the number of positive part sizes whose gap to the next smaller distinct size (or to zero) is at least two, and \(b(\lambda)\) for the number of part sizes occurring at least twice. Then the number \(t_2(\lambda)\) of partitions obtained by removing precisely two boxes is
\[
t_2(\lambda)=\binom{d(\lambda)}2+h(\lambda)+b(\lambda).
\]
Indeed, the removed skew diagram has two incomparable boxes, both originally removable corners (choose any two distinct corners), or one horizontal domino removed from a row (one for each gap of at least two), or one vertical domino removed from two equal-length final rows (one for each repeated part size). The cases are disjoint and exhaustive. This counts \(\mu\) rather than intermediate chains; the latter would count two different deletion orders for incomparable boxes.

**3. Unrestricted bounded-part generating functions.** Let \(\mathcal P_k\) be the partitions with every part at most \(k\). Their generating functions weighted by \(1,d,t_2\) are, respectively, \(P_k,D_k,T_k\) as in the finding. To see this, each part size \(j\) has an independently chosen multiplicity with generating function \((1-q^j)^{-1}\). Requiring a part size \(j\) to occur contributes a relative factor \(q^j\), and requiring multiplicity at least two contributes \(q^{2j}\). Two different present sizes \(i<j\) contribute \(q^{i+j}\). A horizontal gap of at least two at size \(j\ge2\) is the event that size \(j\) occurs but size \(j-1\) does not; it contributes \(q^j(1-q^{j-1})\). Multiplying these sums by \(P_k\) proves the three displayed formulas.

**4. Decomposition at the forbidden rectangle.** A partition avoiding \((u,v)\) has exactly \(r\) rows of length greater than \(u\), with \(0\le r\le v\). Subtracting \(u\) from those \(r\) long rows gives a partition \(\alpha\) with exactly \(r\) positive parts; the remaining rows give an independent partition \(\beta\) with parts at most \(u\). The size identity is \(|\lambda|=ur+|\alpha|+|\beta|\). Conjugating \(\alpha\) identifies it with a partition into parts at most \(r\) containing at least one part of size \(r\). Conjugation preserves both the number of corners and the total \(h+b\) (it exchanges horizontal and vertical two-box removals). Therefore the generating functions for \(\alpha\) weighted by \(1,d,t_2\) are \(P_r-P_{r-1}\), \(D_r-D_{r-1}\), and \(T_r-T_{r-1}\).

The distinct part sizes of \(\lambda\) split between \(\alpha\) and \(\beta\), and no vertical domino crosses the split because the corresponding row lengths are respectively greater than \(u\) and at most \(u\). For horizontal dominoes there is one possible boundary correction: the shortest long row of \(\lambda\) may have a gap of at least two to the longest short row even if the shortest part of \(\alpha\) is one. This happens precisely when \(r\ge1\), the shortest part of \(\alpha\) is one, and the largest part of \(\beta\) is at most \(u-1\). The generating function for this exceptional event, including the \(ur\) size shift, is
\[
q^{ur}\cdot q^r P_{r-1}P_{u-1}=q^{(u+1)r}P_{r-1}P_{u-1}.
\]
Here the shortest part of \(\alpha\) being one means that the conjugate partition has **exactly one** part of size \(r\).

Except for this boundary correction,
\[
t_2(\lambda)=t_2(\alpha)+t_2(\beta)+d(\alpha)d(\beta).
\]
Multiplying the independent generating functions, summing \(r=0,\ldots,v\), and dividing by \(q^2\) because \(|\lambda|=n+2\), yields the formula in the finding. This is an identity of formal power series: the numerator has no terms of degree below two. Exchanging \(x,y\) proves symmetry in \(u,v\). Each summand has denominators dividing \((q;q)_u(q;q)_v\); multiplying by that product yields a polynomial after cancellation of the initial \(q^2\).

**5. Leading asymptotic.** Only the summand \(r=v\) can have pole order \(u+v\) at \(q=1\). Since \(P_k\sim [k!(1-q)^k]^{-1}\), \(D_k/P_k\to k\), and \(T_k/P_k\to k(k+1)/2\), its leading coefficient is
\[
\frac{v(v+1)/2+u(u+1)/2+uv}{u!v!}
=\frac{(u+v)(u+v+1)}{2u!v!}.
\]
The remaining summands have lower pole order; other roots of unity also have strictly smaller pole order. Extracting coefficients from the pole \((1-q)^{-(u+v)}\) gives the asserted asymptotic. Substituting \(u=v=2\) into the finite formula and canceling factors gives the displayed rational function.

## Verification

The standalone standard-library program `verify.py` evaluates the rational formula as exact truncated integer power series. Independently it enumerates all partitions of the two colengths and checks the Young-diagram inclusion relation, without using the two-box statistic. It compares \(14\) coefficients for each of the \(16\) parameter pairs \(1\le u,v\le4\), verifies the formula for the two-box statistic on every partition of size from \(2\) through \(18\), checks symmetry to the computed cutoff, and confirms the displayed \((2,2)\) coefficients and the reduced-node boundary case. Execute with `python3 verify.py`. Its successful completion prints `VERIFY_OK`. These finite computations test the formulas; the universal statement is proved by the preceding partition argument.

## Relationship to prior work

Luan (arXiv:2604.03111, 2026) studies **single** punctual Hilbert schemes on \(x^uy^v=0\), including weak diagonal partition stratifications and cohomological formulas in specified ranges. Zhao (arXiv:2606.08120, 2026) treats nested Hilbert schemes with **one-box** difference on the smooth affine plane. Huang--Jiang--Oblomkov (arXiv:2610.34676, public 2026-10-26) compute the unrefined motivic Hilbert series of **single ideals** on all fat nodes. The latter date is later than the qualifying literature anchor and is cited as relevant independent context, not as the first source. Ran (arXiv:math/0410037) and Lee (arXiv:0906.3097) study flags of ideals on the **reduced** node; their reduced-node results are not claimed new.

A previously recorded generator-refined single-ideal Euler series counts ideals by \(\dim I/(x,y)I\). The present two-box incidence statistic is not a specialization of that invariant: on \(x^2y^2=0\), the diagrams \((4)\) and \((2,2)\) both have colength four and two admissible one-box extensions, but have four and five distinct admissible two-box extensions, respectively. Counting intermediate one-box chains would also yield a different answer because a disconnected skew pair has two possible orders. The result claimed here is the exact two-step incidence series, not any of the cited single-ideal or one-step formulas.

## Limitations

This is a statement about topological Euler characteristics, not a motivic, Poincaré, or Betti-number formula. It does not describe scheme singularities, deformations, or irreducible components of the incidence schemes, and does not count intermediate flags. Historic priority is provisional: earlier work on flags of reduced nodes and broader punctual nested-Hilbert identities may imply some special cases; their possible stronger formulations are not exhaustively ruled out. In particular the full text of Lee's older article was not available for comprehensive comparison. All claims assume complex coefficients and positive multiplicities.

## References

- Y. Luan, *Hilbert scheme of points on non-reduced nodal curves*, arXiv:2604.03111 (first public 2026-04-03), https://arxiv.org/abs/2604.03111.
- C. Zhao, *Deformation Theory and Torus-Fixed Geometry of the Nested Hilbert Scheme of Points*, arXiv:2606.08120 (2026-06-06), https://arxiv.org/abs/2606.08120.
- Y. Huang, R. Jiang, A. Oblomkov, *Sheaves on nodal singularities I*, arXiv:2610.34676 (public 2026-10-26), https://arxiv.org/abs/2610.34676.
- Z. Ran, *A note on Hilbert schemes of nodal curves*, arXiv:math/0410037 (2004), https://arxiv.org/abs/math/0410037.
- H. Lee, *The Full Flag Hilbert Scheme of Nodal Curves and the Punctual Hilbert Scheme of Points of the Cusp Curve*, arXiv:0906.3097 (2009), https://arxiv.org/abs/0906.3097.
- R. Ramkumar, A. Sammartano, *Rational singularities of nested Hilbert schemes*, arXiv:2109.09002 (2021), https://arxiv.org/abs/2109.09002.
