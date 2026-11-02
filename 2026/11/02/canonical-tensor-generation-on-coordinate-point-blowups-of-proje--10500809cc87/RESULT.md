# Canonical tensor generation on coordinate-point blowups of projective space

## Finding
Let \(k=\mathbb C\). For integers \(n\ge2\) and \(0\le t\le n+1\), let \(X_{n,t}\) be the blowup of \(\mathbb P^n_k\) at any \(t\) distinct coordinate points. A line bundle \(L\) is **tensor-generating** when its full collection of integer powers \(\{L^{\otimes j}:j\in\mathbb Z\}\) generates \(\operatorname{Perf}(X_{n,t})\) as a thick triangulated category.

**Theorem.** The canonical bundle \(\omega_{X_{n,t}}\) is tensor-generating if and only if
\[
(n=2)\ \text{or}\ (n=4)\ \text{or}\ (n=3\text{ and }t\le1)\ \text{or}\ (n\ge5\text{ and }t\le2).
\]
Moreover, if \(n\ge4\), \(t\ge2\), and the bundle is tensor-generating, then it is neither nef nor anti-nef.

The dimension-four exception is sharp: blowing up *every* coordinate point of \(\mathbb P^4\) still yields a tensor-generating canonical bundle; starting in dimension five, three such points prevent tensor-generation.

## Assumptions and scope
All varieties are smooth, projective, geometrically integral over \(\mathbb C\). The points are chosen among the \(n+1\) coordinate vertices, not general points. The zero-center case denotes \(\mathbb P^n\). Write \(\pi:X_{n,t}\to\mathbb P^n\), \(H=\pi^*\mathcal O_{\mathbb P^n}(1)\) and \(E_i\) for the exceptional divisors. We use the toric restriction criterion of Ito–Zeng–Zeng [1, Theorem 1.1]: on a proper toric variety, a line bundle is tensor-generating precisely when its restriction to **each** torus-orbit closure is big or anti-big. Bigness on a positive-dimensional projective toric variety means that its section polytope has full dimension (equivalently, maximal Iitaka dimension). Both the criterion and the classification below are about tensor-generation, not about ampleness.

## Proof
**1. Canonical class and orbit closures.** The point-blowup formula gives
\[
K_{X_{n,t}}=-(n+1)H+(n-1)\sum_{i=1}^{t}E_i.
\]
The blowup is a smooth projective toric variety. Every positive-dimensional torus-orbit closure is either (a) a coordinate linear subspace of some \(E_i\cong\mathbb P^{n-1}\), or (b) the strict transform of a coordinate linear subspace \(\mathbb P^q\subset\mathbb P^n\) of dimension \(1\le q\le n\). To see exhaustiveness, map an orbit closure through \(\pi\): the image is an invariant coordinate subspace; if the image has positive dimension the closure dominates it and is the unique strict transform, while orbit closures mapped to a blown-up point lie in its exceptional projective space. Zero-dimensional orbits impose no condition.

On each exceptional \(E_i\), the restrictions are \(H|_{E_i}=0\) and \(E_i|_{E_i}=\mathcal O_{E_i}(-1)\). Therefore
\[
(-K_{X_{n,t}})|_{E_i}=\mathcal O_{\mathbb P^{n-1}}(n-1),
\]
which is ample on every positive-dimensional coordinate subspace of \(E_i\). Thus exceptional orbit closures never obstruct.

**2. Restrictions to strict transforms.** Take a coordinate \(\mathbb P^q\) spanned by \(q+1\) vertices, of which exactly \(m\) are blown up. For \(q\ge2\), its strict transform is \(Y=\operatorname{Bl}_{m\mathrm{\ points}}\mathbb P^q\); when \(q=1\), it is \(\mathbb P^1\). With \(h\) the hyperplane pullback and \(e_j\) the selected exceptional divisors, the restriction is
\[
(-K_{X_{n,t}})|_Y=(n+1)h-(n-1)\sum_{j=1}^{m}e_j.
\]
For \(q=1\), this has degree
\[
d(n,m)=(n+1)-m(n-1),\qquad m\in\{0,1,2\}.
\]
A line bundle on \(\mathbb P^1\) is big or anti-big exactly when its degree is nonzero. The only zero for \(n\ge2\) and the indicated \(m\) is \(n=3\), \(m=2\). Thus a coordinate line joining two centers obstructs exactly in dimension three.

**3. The higher-dimensional polytope.** Fix \(q\ge2\). In homogeneous coordinates on \(\mathbb P^q\), a degree-\(n+1\) monomial \(z_0^{a_0}\cdots z_q^{a_q}\) vanishes at a selected vertex \(j\) to order \((n+1)-a_j\). Sections of the restricted anticanonical divisor therefore have exponent polytope
\[
\mathcal P_{n,q,m}=\left\{(a_0,\ldots,a_q)\in\mathbb R_{\ge0}^{q+1}:\ \sum_{j=0}^{q}a_j=n+1,\quad a_j\le2\text{ for the }m\text{ selected vertices}\right\}.
\]
Its dimension is \(q\) exactly when
\[
m<q+1\quad\text{or}\quad n+1<2(q+1).
\tag{*}
\]
Indeed, when at least one vertex is unselected, assign tiny strictly positive exponents to all constrained coordinates and absorb the remaining degree among unconstrained coordinates; this yields a relative interior point of the degree hyperplane. When every vertex is selected, an interior point exists precisely when the degree \(n+1\) is strictly less than the total upper capacity \(2(q+1)\). If equality holds, the feasible set is a single point; if the degree exceeds that capacity, it is empty.

The *canonical* restriction is never big for \(q\ge2\): its divisor class is \(-(n+1)h+(n-1)\sum e_j\). Since point centers have codimension at least two, the pushforward of \(\mathcal O_Y(r(n-1)\sum e_j)\) is \(\mathcal O_{\mathbb P^q}\) for every positive integer \(r\), giving
\[
H^0\bigl(Y,\mathcal O_Y(rK_{X_{n,t}}|_Y)\bigr)=H^0\bigl(\mathbb P^q,\mathcal O_{\mathbb P^q}(-r(n+1))\bigr)=0.
\]
Hence for \(q\ge2\) the criterion is equivalent to \((*)\).

**4. Exact case distinction.** When \(n=2\), every coordinate line has nonzero degree, and for the coordinate plane \(q=2\), even \(m=3\) satisfies \(n+1=3<6\); all \(t\) work. When \(n=3\), two centers yield the zero-degree line in step 2, whereas \(t\le1\) has no such line and satisfies \((*)\) for all \(q\ge2\). When \(n=4\), the two-center line has degree \(-1\), and every \(q\ge2\) satisfies \(n+1=5<2(q+1)\) if all its vertices are selected; thus all \(t\) work. When \(n\ge5\) and \(t\ge3\), take the coordinate plane through three selected vertices, giving \(q=2,m=3\) and \(n+1\ge6=2(q+1)\): the anticanonical restriction is not big and the canonical restriction is not big either. If \(n\ge5\) and \(t\le2\), no \(q\ge2\) has all \(q+1\) vertices selected, and no line has degree zero. This completes the tensor-generation classification by the toric restriction criterion.

**5. Neither nef nor anti-nef.** For \(n\ge4\), let \(\ell\) be the strict transform of the coordinate line joining two selected points, and \(f\) a line in any exceptional divisor. Intersections give
\[
K_{X_{n,t}}\cdot\ell=n-3>0,\qquad K_{X_{n,t}}\cdot f=-(n-1)<0.
\]
Therefore neither \(K_{X_{n,t}}\) nor its negative is nef whenever \(t\ge2\). This is compatible with tensor-generation for all \(t\) when \(n=4\), and for \(t=2\) when \(n\ge5\). \(\square\)

## Verification
A standalone Python file `verify_coordinate_blowups.py` enumerates integer points of the restricted anticanonical polytopes for every \(2\le n\le8\), every possible \(t\), every coordinate-subspace dimension, and every realizable number of selected vertices. It computes the affine rank of the lattice-point sets and checks the formula \((*)\), then verifies the full classification. Execution returned `VERIFY_OK: 567 orbit-subspace tests; all n=2..8, all t`. These finite tests are consistency checks; the proof above establishes all dimensions.

## Relationship to prior work
Ito–Zeng–Zeng [1, Theorem 1.1] establish the general toric restriction criterion and [1, Proposition 6.7] classify *line-centered* blowups of \(\mathbb P^3\). The present result instead classifies the canonical bundle on *coordinate-point-centered* blowups of \(\mathbb P^n\) for every \(n\ge2\); the explicit dimension-four exception and dimension-five surface obstruction are not stated in [1]. Ito–Olander [2, Proposition 5.25 and Theorem 5.26] treat blowups at points when a positive ample pullback is twisted by positive exceptional divisors, and canonical bundles of blowups of bases with **ample** canonical class. Their hypotheses do not apply to the anti-ample canonical class of \(\mathbb P^n\). This theorem uses their broader derived Nakai–Moishezon ideas through [1], but no priority claim is made beyond the comparisons actually inspected.

## Limitations
The centers must be distinct torus-fixed coordinate points; arbitrary configurations or infinitely near blowups are not classified. The argument relies on the published toric restriction criterion; it is not an independent proof of that criterion. All assertions concern complex varieties. The finite checker does not certify the infinite theorem. Independent mathematical review and exhaustive historical priority determination have not been performed.

## References
[1] D. Ito, M. R. Zeng, and X. Zeng, *Tensor-generating line bundles on toric varieties*, arXiv:2610.22279v1 (first submitted 2026-10-15), https://arxiv.org/html/2610.22279v1 , especially Theorems 1.1, 3.1 and Proposition 6.7.

[2] D. Ito and N. Olander, *A derived category analogue of the Nakai–Moishezon criterion*, arXiv:2507.17681v2 (2025), https://arxiv.org/html/2507.17681v2 , especially §5.3, Proposition 5.25 and Theorem 5.26.
