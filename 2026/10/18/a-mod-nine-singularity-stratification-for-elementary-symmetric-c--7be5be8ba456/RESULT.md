# A mod-nine singularity stratification for elementary-symmetric cubic hypersurfaces in characteristic three

## Finding

Let \(k\) be an algebraically closed field of characteristic \(3\), let \(n\geq4\), and set
\[
F_n=e_3(x_1,\ldots,x_n)=\sum_{1\leq i<j<\ell\leq n}x_ix_jx_\ell,
\qquad X_n=V(F_n)\subset\mathbb P^{n-1}_k.
\]
These hypersurfaces are geometrically integral and normal. The entire reduced singular locus, and its local scheme structure when it is zero-dimensional, are determined by \(n\bmod9\).

Define \(\mathbf1_S\in k^n\) as the indicator vector of a subset \(S\subseteq[n]\), and define
\[
B_n=\sum_{\substack{1\leq r\leq n\\r\equiv1\ (\mathrm{mod}\ 9)}}\binom nr.
\]
If \(n\not\equiv2\pmod9\), the singular locus is finite. It contains precisely the points \([\mathbf1_S]\) with \(|S|\equiv1\pmod9\), and has the following additional, disjoint points:

* If \(n\equiv8\pmod9\), add \([\mathbf1_S-\mathbf1_{S^c}]\) for every unordered bipartition \(\{S,S^c\}\) with \(|S|\equiv|S^c|\equiv4\pmod9\).
* If \(n\equiv5\pmod9\), add the same signed bipartition points with both sizes congruent to \(7\pmod9\).
* In all other residue classes, add nothing.

The number of geometric singular points is \(B_n+E_n\), where
\[
E_n=\begin{cases}
\tfrac12\displaystyle\sum_{\substack{1\leq r<n\\r\equiv7\ (\mathrm{mod}\ 9)}}\binom nr,&n\equiv5\pmod9,\\
\tfrac12\displaystyle\sum_{\substack{1\leq r<n\\r\equiv4\ (\mathrm{mod}\ 9)}}\binom nr,&n\equiv8\pmod9,\\
0,&\text{otherwise}.
\end{cases}
\]
For \(n\equiv0,1,3,4,6,7\pmod9\), every point is an ordinary quadratic double point and the Jacobian singular scheme is reduced. For \(n\equiv5,8\pmod9\), every singular point has a **curvilinear Jacobian local algebra of length three**, isomorphic to \(k[t]/(t^3)\). Thus its zero-dimensional Jacobian singular scheme has total length \(3(B_n+E_n)\).

If \(n\equiv2\pmod9\), the reduced singular locus is instead exactly the union of the projective lines
\[
L_S=\mathbb P\big(\operatorname{span}(\mathbf1_S,\mathbf1_{S^c})\big),
\qquad |S|\equiv|S^c|\equiv1\pmod9,
\]
where \(L_S=L_{S^c}\). The number of distinct components is exactly \(B_n/2\). Every two distinct components meet **only** at \([1:\cdots:1]\), and the Jacobian singular scheme is generically reduced along each line. No assertion is made about the entire nonreduced local scheme at their common intersection.

For illustration, the isolated singular-point counts at \(n=5,8,10,14\) are respectively \(5,43,11,2731\); for \(n=11\) there are eleven singular lines, and for \(n=20\) there are \(92398\) such lines. Every geometric singular support point in the isolated cases is already \(\mathbb F_3\)-rational.

## Assumptions and scope

All geometry is over an algebraically closed field of characteristic \(3\). Scheme-theoretic claims concern the projective Jacobian singular scheme defined by \((F_n,\partial_1F_n,\ldots,\partial_nF_n)\); the curvilinear local statement applies only when \(n\not\equiv2\pmod9\). Ordinary double points mean nondegenerate quadratic tangent cones in characteristic different from two. Empty sums have value zero. The integer parameter satisfies \(n\geq4\), and the binomial sums are integer counts (not coefficients reduced modulo three).

## Proof

**1. Critical points have at most two coordinate values.** Write \(e_1,e_2\) for the first two elementary symmetric polynomials in the \(n\) coordinates. Direct differentiation gives
\[
\partial_iF_n=e_2-x_ie_1+x_i^2.
\]
All coordinates of a critical point are roots of the same monic quadratic \(T^2-e_1T+e_2\). If there are two distinct values \(a,b\), occurring \(m,n-m\) times, subtracting their two gradient equations yields \(e_1=a+b\), and substitution yields \(e_2=ab\). In characteristic three the identities for the first two power sums imply
\[
(m-1)a+(n-m-1)b=0,\qquad
(m-1)a^2+(n-m-1)b^2=0.
\]
Subtracting multiples of these equations gives \((m-1)a=0\) and \((n-m-1)b=0\), because \(a\ne b\).

**2. The projective support.** If precisely one of \(a,b\) is zero, its nonzero-value support has cardinality \(r\equiv1\pmod3\). The equation \(F_n=0\) is \(\binom r3=0\) in \(k\); Lucas's theorem, or the coefficient of degree three in \((1+t)^r\), makes this equivalent to \(r\equiv1\pmod9\). This gives all indicator points. If all coordinates are the same nonzero value, criticality and \(F_n=0\) hold simultaneously exactly for \(n\equiv1,2\pmod9\). The first case already appears among indicator points with full support; the second supplies the diagonal point of every line below.

If \(a,b\) are both nonzero and distinct, the preceding linear equations force \(m\equiv n-m\equiv1\pmod3\). Write \(m=1+3u\) and \(n-m=1+3v\). The generating function identity
\[
(1+at)^m(1+bt)^{n-m}
=(1+at)(1+bt)(1+a^3t^3)^u(1+b^3t^3)^v
\]
shows that \(F_n=ua^3+vb^3\), with \(u,v\) reduced modulo three. When both residues vanish, \(F_n\) vanishes identically on the two-value line; these are precisely the partitions with sizes \(1\pmod9\), possible when \(n\equiv2\pmod9\). When exactly one residue vanishes, \(F_n=0\) forces one of \(a,b\) to vanish, already covered. When both are nonzero, the condition is either \(a=b\) (already the diagonal case) or \(a=-b\), the latter occurring exactly for \(u=v=1\) or \(u=v=2\), giving the signed points and their size residues \(4\) or \(7\pmod9\). This exhaustive split proves the support classification and the component-count formulas. Distinct two-block lines share only the all-ones direction: otherwise their indicator vectors would yield the same unordered bipartition.

**3. Hessian ranks and local lengths.** The Hessian has diagonal entries zero and off-diagonal entries \(H_{ij}=e_1-x_i-x_j\). At an indicator point with support size \(r\equiv1\pmod9\), the Hessian is block diagonal with blocks \(I-J\) of size \(r\) and \(J-I\) of size \(n-r\). Its rank is \(n-1\) when \(n\not\equiv2\pmod3\), and \(n-2\) when \(n\equiv2\pmod3\). If \(r=n\), the first block alone has rank \(n-1\), as required for \(n\equiv1\pmod9\). At a signed point, the mixed block vanishes and the two diagonal blocks are nonzero scalar multiples of \(J-I\), each with size \(1\pmod3\), so the rank is \(n-2\). At the all-ones point for \(n\equiv1\pmod9\), the Hessian again has rank \(n-1\). These ranks are computed in homogeneous coordinates; the Euler radial direction accounts for one kernel vector at every critical point.

In the rank-\(n-1\) cases, the Jacobian ideal cuts out a reduced point on a projective affine chart. The nondegenerate quadratic tangent cone yields an ordinary double point. In the rank-\(n-2\) isolated cases (necessarily \(n\equiv5\) or \(8\pmod9\)), the gradient subscheme is smooth of dimension one at the point: its tangent dimension is one and it contains the corresponding two-block line, hence it equals that line locally. On an indicator line the restriction of \(F_n\) is \(v b^3\) with \(v=(n-r-1)/3\ne0\) in \(k\); on a signed line it is \(u(a+b)^3\) with \(u\in\{1,2\}\). In either case the unique zero is a triple point on the smooth critical line. Quotienting its regular one-dimensional local ring by this cubic gives exactly \(k[t]/(t^3)\). Along the generic points of the \(n\equiv2\pmod9\) lines, the gradient Hessian has projective rank \(n-2\), and the hypersurface restriction vanishes identically, proving generic reducedness.

**4. Geometric integrality and normality.** Since \(F_n\) is multilinear, in any nontrivial factorization variables must partition between two factors. Every monomial in such a factorization would use a fixed number of variables from either side. Selecting two remaining indices and exchanging one index between the two sides produces two monomials of \(e_3\) with different counts, a contradiction for \(n\ge4\). Thus \(F_n\) is irreducible over every extension field. Its hypersurface coordinate ring is Cohen--Macaulay, hence satisfies Serre's \(S_2\). The singular support is at most one-dimensional, and in the one-dimensional case \(n\ge11\), so it has codimension at least two inside \(X_n\). Hence \(R_1\) holds, giving normality by Serre's criterion.

## Verification

The standalone `verify.py` enumerates **all** projective \(\mathbb F_3\)-points for \(4\le n\le11\), compares the cubic-plus-gradient singular condition with the stated support criterion, checks the exact isolated-point counts and Hessian ranks through \(n=10\), and verifies the \(n=11\) eleven-line star. It uses integer arithmetic modulo three and no third-party packages. Run `python3 verify.py`, expecting `VERIFY_OK`. Enumeration over a finite field does not prove the algebraic-closure statement; the preceding two-root and Hessian arguments supply that proof. Combinatorial counts for \(n=14,17,20\) follow from the displayed finite binomial formulas, not extrapolation from the checker.

## Relationship to prior work

Cafure, Matera, and Privitelli (2011 preprint) establish the symmetric-hypersurface singularity framework and partition restrictions but not these exact component and local-scheme formulas. Orzel (2025 preprint) gives a general dimension bound for order-two loci. Xie (2026 preprint) gives sharper all-degree dimension formulas, identifies extremal partition components and gives generic multiplicities of coordinate components. In particular, **the dimension transition, existence of extremal partition lines, and generic coordinate multiplicity three are prior results and are not asserted to be independently new**. The present classification determines the complete reduced support in degree three and characteristic three, including the noncoordinate signed points, exhaustive counts, and local length at every isolated point; it also determines the common-intersection geometry of all line components. Xie's article expressly does not classify all smaller-dimensional components. The possibility that a comparable specialization appears implicitly in other literature remains.

## Limitations

This is a characteristic-three result for \(e_3\), not a classification of all elementary symmetric hypersurfaces. For \(n\equiv2\pmod9\), only the reduced singular support and generic Jacobian reducedness are asserted, not the complete nonreduced singular scheme at the common diagonal point. The evidence supports no claim about positive characteristics other than three,.

## References

1. A. Cafure, G. Matera, M. Privitelli, *Singularities of symmetric hypersurfaces and an application to Reed--Solomon codes*, arXiv:1109.2265v1 (first posted 2011-09-10), Sections 3--4, https://arxiv.org/html/1109.2265v1.
2. I. Orzel, *Computing the Elementary Symmetric Polynomials in Positive Characteristics*, arXiv:2509.05009 (first posted 2025-09-05), Section 2, https://arxiv.org/html/2509.05009v3.
3. Y. Xie, *Derivative and multiplicity loci of elementary symmetric polynomials in positive characteristic*, arXiv:2610.00259v1 (2026-09-24), Theorems 1.1--1.4 and Sections 2, 4, 6, 7, https://arxiv.org/html/2610.00259v1.
