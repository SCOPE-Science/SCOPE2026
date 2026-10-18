# Mean-length Minkowski asymmetry for weighted cyclic simplex sums

## Finding

Let \(n\ge3\) be an integer, and let \(w_2,\ldots,w_{n-1},\lambda\ge0\), not all zero. Number the vertices of an \(n\)-cycle modulo \(n\). For every nonempty \(I\subseteq[n]\), put \(\Delta_I=\operatorname{conv}\{e_i:i\in I\}\), and write \(I_{a,j}\) for the cyclic interval of length \(j\) starting at \(a\). Define the length-homogeneous cyclic simplex sum
\[
K=K_n(w,\lambda)=\sum_{j=2}^{n-1}w_j\sum_{a=1}^{n}\Delta_{I_{a,j}}+\lambda\Delta_{[n]}.
\]
Let \(W=\sum_{j=2}^{n-1}w_j\). The Minkowski asymmetry of a convex body \(P\) is the least \(s\ge1\) such that \( -(P-c)\subseteq s(P-c)\) for some \(c\in P\). Then
\[
\boxed{s(K)=\frac{\sum_{j=2}^{n-1}(j-1)w_j+(n-1)\lambda/n}{W+\lambda/n}.}
\]
The optimal Minkowski center is unique and equals \(c=(W+\lambda/n)\mathbf1\). In particular, \(K\) is centrally symmetric if and only if \(\lambda=0\) and \(w_j=0\) for every \(j\ge3\). This includes the cyclic graphical-zonotope case.

For the cyclic \(m\)-graph polytopes \(Q_{C_n,m}\) of Pešović and Stojadinović (2022), with \(1\le m\le n-1\), the result becomes
\[
\boxed{s(Q_{C_n,m})=\begin{cases}(m+1)/2,&1\le m\le n-2,\\ (n-1)/2+1/[2(n-1)],&m=n-1.\end{cases}}
\]
Thus the asymmetry rises by exactly \(1/2\) at each intermediate stage, but the last added whole-cycle simplex increases it by only \(1/[2(n-1)]\). The unique Minkowski center is \((m+1)\mathbf1\) for \(m\le n-2\), and \((n-1+1/n)\mathbf1\) at the final cyclohedral stage, in the original convention including all singleton simplices.

## Assumptions and scope

Every \(w_j\) and \(\lambda\) is a finite real number and is nonnegative; \(W+\lambda>0\). The body \(K\) has intrinsic dimension \(n-1\), lying in the affine hyperplane of coordinate sum \(T=nW+\lambda\). Its center above is an intrinsic Minkowski center. No Euclidean-radius, volume, or combinatorial-type assertion is claimed for arbitrary weights. The collection of cyclic intervals of any fixed length between \(2\) and \(n-1\) contains exactly \(n\) distinct subsets, including for \(n=3\).

## Proof

**1. Exact subset inequalities.** For every \(S\subseteq[n]\), set \(z(S)=\min_{x\in K}\sum_{i\in S}x_i\). A simplex \(\Delta_I\) has minimum subset sum \(1\) if \(I\subseteq S\) and \(0\) otherwise. Consequently
\[
z(S)=\sum_{j=2}^{n-1}w_j\#\{a:I_{a,j}\subseteq S\}+\lambda\mathbf1_{S=[n]}.
\]
Moreover,
\[
K=\{x\in\mathbb R^n:\sum_i x_i=T,\ \sum_{i\in S}x_i\ge z(S)\text{ for all }\varnothing\ne S\subsetneq[n]\}.
\]
To prove completeness rather than merely necessity of these inequalities, order the components of an arbitrary linear functional \(u\) as \(u_{i_1}\le\cdots\le u_{i_n}\). Express \(u=u_{i_1}\mathbf1+\sum_{k=2}^{n}(u_{i_k}-u_{i_{k-1}})\mathbf1_{\{i_k,\ldots,i_n\}}\). For every summand simplex, its minimum against \(u\) equals its constant-sum term plus precisely the indicator contribution when that simplex is contained in the corresponding nested suffix. Thus the subset lower bounds imply \(u\cdot x\ge\min_{y\in K}u\cdot y\) for every \(u\), and separation proves the displayed identity.

**2. Cyclic-run formula.** If \(S\) is nonempty and proper, its distinct maximal cyclic runs of consecutive selected vertices have lengths \(\ell_1,\ldots,\ell_r\). Tubes contained in \(S\) cannot cross a missing vertex; a run of length \(\ell\) contains \(\max(\ell-j+1,0)\) length-\(j\) intervals. Hence
\[
z(S)=\sum_{a=1}^r\sum_{j=2}^{\ell_a}(\ell_a-j+1)w_j.
\]
The unique point fixed by cyclic rotation in the affine hull is \(c=c_0\mathbf1\), where \(c_0=W+\lambda/n>0\). For \(1\le t\le n-1\), put
\[
f(t)=t c_0-\sum_{j=2}^{t}(t-j+1)w_j.
\]
The lower centered subset-support gap is
\[
A(S):=c(S)-z(S)=\sum_{a=1}^r f(\ell_a).
\]
By the fixed-total-sum condition, the upper gap \(B(S):=\max_{x\in K}x(S)-c(S)\) equals \(A(S^c)\). The complementary cyclic runs number exactly \(r\) and have lengths \(h_1,\ldots,h_r\). Also
\[
f(t+1)-f(t)=\sum_{j=t+2}^{n-1}w_j+\lambda/n\ge0,
\quad f(1)=c_0>0,
\quad f(n-1)=\sum_{j=2}^{n-1}(j-1)w_j+(n-1)\lambda/n.
\]
Therefore \(f(1)\le f(t)\le f(n-1)\), and for every nontrivial \(S\)
\[
\frac{A(S)}{B(S)}=\frac{\sum_a f(\ell_a)}{\sum_a f(h_a)}\le \frac{f(n-1)}{f(1)}.
\]
Equality holds when \(S\) consists of all except one coordinate, because then its run length is \(n-1\), and the complement's run length is \(1\).

**3. Optimal containment and its lower bound.** For a possible center \(a\) in the affine hull, inclusion \(-(K-a)\subseteq s(K-a)\) is equivalent, using the complete subset inequalities from step 1 and the fixed-total-sum identity, to both inequalities \(A_a(S)\le sB_a(S)\) and \(B_a(S)\le sA_a(S)\) for every nonempty proper \(S\), where \(A_a(S)=a(S)-z(S)\) and \(B_a(S)=T-z(S^c)-a(S)=A_a(S^c)\). Step 2 proves inclusion at \(a=c\) with \(s=f(n-1)/f(1)\). Conversely, averaging any feasible center over all cyclic coordinate rotations gives the invariant center \(c\); the feasible-center set for fixed \(s\) is convex because the containment inequalities are linear in \(a\). Hence no smaller value than the ratio at \(c\) is possible.

**4. Uniqueness.** Write \(s=f(n-1)/f(1)\). For each co-singleton subset \(S=[n]\setminus\{i\}\), equality \(A_c(S)=sB_c(S)\) holds. Every optimal center \(a\) must satisfy the same necessary affine inequality \(A_a(S)\le sB_a(S)\), whose right-hand side is fixed and is saturated at \(c\). Thus \(a(S)\le(n-1)c_0\), giving \(a_i\ge c_0\) for every \(i\). Since \(\sum_i a_i=T=nc_0\), equality holds coordinatewise: \(a=c\).

**5. Specialization and symmetry.** Subtracting denominator from numerator gives \(\sum_{j=3}^{n-1}(j-2)w_j+(n-2)\lambda/n\). Since all parameters are nonnegative and \(n\ge3\), this vanishes exactly for sums of length-two intervals, which are sums of centrally symmetric segments up to translation. The cyclic \(m\)-graph polytope includes all singleton simplices, adding \(\mathbf1\) to \(K\) but changing neither asymmetry nor uniqueness. For \(m\le n-2\), use \(w_2=\cdots=w_{m+1}=1\), all other parameters zero; this yields \((m+1)/2\). For \(m=n-1\), use \(w_2=\cdots=w_{n-1}=1\) and \(\lambda=1\); the displayed terminal fraction simplifies to \((n-1)/2+1/[2(n-1)]\). The center coordinates follow from \(c+\mathbf1\). This completes the proof.

## Verification

The accompanying standard-library checker `check_weighted_cyclic.py` independently enumerates every cyclic interval, computes all proper-subset minimum values as exact rational numbers, tests the maximal reflection-support quotient and the co-singleton witnesses, and checks the full discrete filtration. Run it with `python3 check_weighted_cyclic.py`. It reports 770 exact profiles for \(3\le n\le9\), including degenerate and random positive rational weights. For 333 profiles with all length weights positive, the code additionally verifies that precisely the \(n\) co-singleton subsets maximize the directed ratio. These finite tests corroborate but do not replace the universal analytical proof. The convexity/uniqueness argument is proved symbolically above, not inferred from enumeration.

## Relationship to prior work

Pešović and Stojadinović introduced the finite \(m\)-graph-polytope filtration and its graphical-zonotope and graph-associahedron endpoints (2022, Definition 2.1). The present statement uses that pre-existing family and adds its affine-invariant reflection-dilation profile and all minimizing centers. Lam and Postnikov studied the simplex-sum and cyclic-interval realization of cyclohedra and more general polypositroids (2020 preprint; Section 3.3); their studied facet and deformation geometry does not itself state this Minkowski-asymmetry formula. Padrol, Pilaud and Poullot analyzed graph-associahedral and nestohedral deformation cones (2021); those results concern realizations and deformations rather than optimal reflected containment. None of these standard source results is claimed anew.

## Limitations

This theorem concerns Minkowski asymmetry and its optimizing centers in the specified length-invariant nonnegative simplex-sum realization. It does not determine the asymmetry of arbitrarily position-dependent cyclic-interval weights, nor Euclidean inradii, nor all other graph associahedra. An undiscovered equivalent characterization in older convex-geometry or submodular-function literature remains possible. Finite checking cannot rule out such prior coverage. No independent mathematical validation has been performed.

## References

1. M. Pešović and T. Stojadinović, *Between graphical zonotope and graph-associahedron*, arXiv:2209.12053v1, publicly posted 2022-09-24. https://arxiv.org/abs/2209.12053
2. T. Lam and A. Postnikov, *Polypositroids*, arXiv:2010.07120v1, publicly posted 2020-10-14, especially §3.3. https://arxiv.org/abs/2010.07120
3. A. Padrol, V. Pilaud and G. Poullot, *Deformation cones of graph associahedra and nestohedra*, arXiv:2109.09200v1, publicly posted 2021-09-19. https://arxiv.org/abs/2109.09200
4. A. Postnikov, *Permutohedra, associahedra, and beyond*, arXiv:math/0507163v1, 2005. https://arxiv.org/abs/math/0507163
