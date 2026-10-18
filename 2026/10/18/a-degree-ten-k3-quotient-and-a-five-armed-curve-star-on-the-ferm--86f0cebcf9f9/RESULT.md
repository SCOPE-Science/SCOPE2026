# A degree-ten K3 quotient and a five-armed curve star on the Fermat quintic surface

## Finding
Let \(X\subset\mathbb P^3_{\mathbb C}\) be the Fermat quintic surface
\[
X=\{x^5+y^5+z^5+w^5=0\}
\]
and let \(\tau\) interchange \(x\) and \(y\). This is one of the thirty order-two reflections attached to the quasi-Galois points classified in [1]. Put \(Y=X/\langle\tau\rangle\) and let \(f:S\to Y\) be the minimal resolution. Define \(u=x+y\), \(v=x-y\), and \(t=v^2\) with weights \(\deg u=\deg z=\deg w=1\), \(\deg t=2\).

**The quotient and its K3 resolution.** There is an isomorphism
\[
Y\cong\bigl\{u^5+10u^3t+5ut^2+16z^5+16w^5=0\bigr\}\subset\mathbb P(1,1,1,2).
\]
The surface \(Y\) has precisely one singularity, the \(A_1\) point \(o=[0:0:0:1]\), and \(S\) is a K3 surface. The divisor \(H=f^*\mathcal O_Y(2)\) is a base-point-free primitive nef polarization of degree \(H^2=10\) (genus six); it contracts the exceptional curve \(E=f^{-1}(o)\), which is a smooth rational \((-2)\)-curve.

**An explicit six-curve configuration.** For the five distinct roots \(\beta\in\mathbb C\) of \(\beta^5=-1\), let \(C_\beta\subset Y\) be the image of the line
\[
L_\beta=\{x+y=0,\ z=\beta w\}\subset X,
\]
and let \(R_\beta\subset S\) be its strict transform. The five curves \(R_\beta\) are pairwise disjoint smooth rational \((-2)\)-curves, each meeting \(E\) transversely exactly once, at five distinct points of \(E\). Thus the six curves \(E,R_\beta\) form the star intersection graph \(K_{1,5}\), and the lattice they generate has rank six, signature \((1,5)\), and determinant \(-16\).

**The reducible polarization and the branch curve.** With \(R=\sum_{\beta^5=-1} R_\beta\), the full integral divisor relation is
\[
\boxed{\ H\sim 2R+5E\ },\qquad H\cdot E=0,\quad H\cdot R_\beta=1.
\]
The fixed plane quintic \(\{x=y\}\cap X\) maps isomorphically onto a smooth genus-six curve \(B\subset Y\), cut out by \(t=0\), and its strict transform belongs to \(|H|\). All thirty quasi-Galois reflection quotients of the Fermat quintic surface are isomorphic as surfaces equipped with these distinguished constructions, by conjugacy under diagonal and permutation automorphisms.

## Assumptions and scope
All geometry is over \(\mathbb C\), and the quintic is the *smooth Fermat surface*, not a general quintic. A quotient means the normal geometric quotient by the specified order-two automorphism. The line bundles \(\mathcal O_Y(2)\) and their pullbacks are understood on the weighted hypersurface, which meets the singular point of the ambient weighted projective space. A primitive polarization here is a primitive nef and big class, not an ample class on the resolution: the exceptional curve \(E\) has intersection zero with \(H\). The exceptional-point resolution is the minimal resolution of the unique rational double point. No claim is made that the six-curve lattice exhausts \(\operatorname{NS}(S)\), or that the K3 surface is generic in its polarization moduli.

## Proof
**1. Quotient equation and branch/fixed locus.** The Fermat quintic is smooth: its four homogeneous partial derivatives vanish simultaneously only at the forbidden all-zero vector. The coordinate involution sends \(v\mapsto-v\) and fixes \(u,z,w\). The polynomial identity
\[
16(x^5+y^5)=u^5+10u^3v^2+5uv^4
\]
shows that the homogeneous invariant coordinate ring is
\[
\mathbb C[u,z,w,t]/(u^5+10u^3t+5ut^2+16z^5+16w^5),
\qquad \deg t=2.
\]
Indeed, taking invariants of the quotient by the invariant Fermat equation is exact in characteristic zero, and the polynomial ring invariants under the sign on \(v\) are \(\mathbb C[u,z,w,v^2]\). Taking \(\operatorname{Proj}\) yields the claimed normal weighted quotient. An invariant point on \(X\) is fixed projectively either when \(v=0\), or when \(u=z=w=0\). The first locus is the smooth plane Fermat quintic \(F=\{v=0,\ u^5+16z^5+16w^5=0\}\), while the latter is the unique point \(P=[1:-1:0:0]\). They are disjoint.

At a point of \(F\), the automorphism acts as a smooth reflection in a normal coordinate, so the local quotient is smooth and branched along the image \(B\). At \(P\), work on the affine chart \(v=1\); the equation becomes
\[
u^5+10u^3+5u+16z^5+16w^5=0.
\]
Because its derivative with respect to \(u\) at the origin is \(5\ne0\), \(z,w\) form local analytic coordinates on \(X\) at \(P\). After the projective rescaling returning the swapped coordinates to \(v=1\), the involution acts on \((z,w)\) by \((-z,-w)\). Its quotient has local analytic ring
\[
\mathbb C[[z,w]]^{\{\pm1\}}\cong
\mathbb C[[a,b,c]]/(ac-b^2),\qquad a=z^2,\ b=zw,\ c=w^2,
\]
so \(o\) is precisely an \(A_1\) singularity. There are no other nontrivial stabilizers; hence \(o\) is the only singular point of \(Y\).

**2. K3 and polarization.** The weights in the ambient weighted projective threefold add to five, exactly the weighted degree of the defining polynomial. Since the defining affine cone is nonsingular away from the origin and the hypersurface is well formed, weighted adjunction gives \(\omega_Y\cong\mathcal O_Y\). The only singularity is a rational double point, so its minimal resolution is crepant: \(\omega_S\cong\mathcal O_S\). A smooth quintic surface has \(H^1(X,\mathcal O_X)=0\), by the standard hypersurface cohomology sequence in \(\mathbb P^3\). Since the quotient map is finite in characteristic zero and has an invariant Reynolds projection, \(H^1(Y,\mathcal O_Y)\cong H^1(X,\mathcal O_X)^\tau=0\). Rational double points preserve this cohomology on resolution, whence \(H^1(S,\mathcal O_S)=0\). Therefore \(S\) is a K3 surface.

The sections \(u^2,uz,uw,z^2,zw,w^2,t\) show that \(\mathcal O_Y(2)\) is globally generated even at \(o\), so \(H=f^*\mathcal O_Y(2)\) is nef and base-point-free. Weighted intersection theory on a degree-five hypersurface in \(\mathbb P(1,1,1,2)\) gives
\[
\bigl(c_1(\mathcal O_Y(1))\bigr)^2=\frac{5}{1\cdot1\cdot1\cdot2}=\frac52,
\quad H^2=4\cdot\frac52=10.
\]
The pullback of an ample Cartier bundle is big; it has zero intersection with exceptional curves and the exceptional locus here is just \(E\). On a K3, the intersection form is even. If \(H=kD\) in \(\operatorname{Pic}(S)\) for \(k\ge2\), then \(10=k^2D^2\), with \(D^2\) even, which is impossible. Thus \(H\) is primitive. The strict transform of \(t=0\) is the plane quintic \(B\), disjoint from \(o\), smooth of genus \((5-1)(5-2)/2=6\), and \(B\sim H\).

**3. The five lines and their resolution.** The hyperplane \(u=0\) on \(X\) splits into the five lines \(L_\beta\), because it imposes \(z^5+w^5=0\). These lines have a common point \(P\) and otherwise are pairwise disjoint. Each is preserved by \(\tau\). On a line, in coordinates \([v:w]\), the action is \([v:w]\mapsto[-v:w]\); the two fixed points are the common point \(P\) and the point \(v=0\), which lies on \(F\). Thus the quotient \(C_\beta=L_\beta/\langle\tau\rangle\) is a rational smooth curve, and all five \(C_\beta\) meet only at \(o\).

In the local uniformizing coordinates \((z,w)\) at \(P\), the tangent of \(L_\beta\) is the line \(z=\beta w\). The minimal resolution of \(\mathbb A^2/\{\pm1\}\) replaces the origin by \(E\cong\mathbb P^1\), which parameterizes tangent directions. As the five \(\beta\)'s are distinct, the strict transforms \(R_\beta\) are smooth, pairwise disjoint, and meet \(E\) transversely at distinct points. Since the K3 canonical class is trivial, adjunction gives \(E^2=R_\beta^2=-2\). The Gram matrix, ordered as \(E,R_{\beta_1},\ldots,R_{\beta_5}\), is
\[
M=\begin{pmatrix}
-2&1&1&1&1&1\\
1&-2&0&0&0&0\\
1&0&-2&0&0&0\\
1&0&0&-2&0&0\\
1&0&0&0&-2&0\\
1&0&0&0&0&-2
\end{pmatrix}.
\]
Its Schur complement in the central entry is \(-2+5/2=1/2\); hence \(\det M=(-2)^5(1/2)=-16\), and the inertia consists of one positive and five negative eigenvalues. The curves therefore generate a nondegenerate rank-six sublattice.

**4. Integral divisor identity.** The equation \(u=0\) is a weighted degree-one Weil divisor on \(Y\). As a reduced divisor it equals \(D=\sum C_\beta\). It is not Cartier at the \(A_1\) point, but \(2D\) is Cartier, linearly equivalent to \(\mathcal O_Y(2)\), because its equation is \(u^2=0\) of weighted degree two. For a single branch \(C_\beta\), its rational pullback to the minimal resolution is \(R_\beta+\tfrac12E\): indeed, writing \(f^*C_\beta=R_\beta+aE\), the projection formula gives \(0=(f^*C_\beta)\cdot E=1-2a\), hence \(a=1/2\). Summing the five branches and multiplying by two gives the *integral* linear equivalence
\[
H=f^*(2D)\sim 2\sum_{\beta^5=-1}R_\beta+5E.
\]
Consequently \(H\cdot E=2\cdot5+5(-2)=0\), and \(H\cdot R_\beta=2(-2)+5=1\). The same Gram matrix gives \(H^2=10\), independently verifying the weighted intersection calculation. These are scheme-theoretic Cartier and divisor-class statements, not merely numerical coincidences.

**5. Uniformity across thirty involutions.** The thirty order-two quasi-Galois reflections in [1, Theorem 1.8 and Proposition 4.5] interchange a pair of coordinates up to a fifth-root-of-unity twist. Permutations of the four coordinates and diagonal fifth-root scalings preserve \(X\) and conjugate each such reflection to \(\tau\). The quotient, its crepant resolution, polarizing divisor, fixed branch curve, and five-line star are preserved up to the resulting isomorphism. This establishes the assertion uniformly for every one of the thirty quasi-Galois involutions.

## Verification
The standalone exact-arithmetic script `artifacts/check_fermat_quintic_star.py` reproduces the fifth-power invariant expansion, weighted degree and branch genus computations, and the six-curve intersection matrix, including its determinant and the integral polarization identity. The script prints `FERMAT_QUINTIC_K3_STAR_EXACT_OK` on success. Those calculations support, but do not replace, the proof of smoothness, local quotient type, K3 cohomology, or the geometrically determined intersection numbers; these are proved above. All formulas hold in characteristic zero and rely on no finite-field sampling.

## Relationship to prior work
Miura and Takahashi [1] classify order-two quasi-Galois reflections of Fermat varieties and count thirty for the Fermat quintic surface. Their Theorem 1.8, Example 4.3, Proposition 4.5, and Remark 4.7 provide the involutions and transposition geometry; they do not determine the quotient surface, its minimal resolution, or the five-armed exceptional configuration. Miura and Taki [2] study quasi-Galois points of *quartic* surfaces, including K3 geometry of the original quartics, which is a different degree and different quotient construction. Classical invariant theory, quotient singularities and weighted hypersurface adjunction are standard ingredients, not separate novelty claims. The added result is the simultaneous **quintic reflection-quotient K3 realization, exact five-curve star, and integral degree-ten polarization degeneration**.

## Limitations
The six specified curve classes need not form the full Picard group; their primitive closure and the full transcendental lattice are not determined. The polarization is nef and big, not ample, because it contracts \(E\). The result is special to the Fermat quintic and its thirty order-two quasi-Galois reflections; it does not classify arbitrary quintic involutions. The literature comparison covers the initiating full-text article, the relevant quartic preprint abstract, focused geometric and invariant-ring searches, and published mathematical-record comparisons, but older equivalent special weighted-K3 constructions may exist. No independent scientific audit has been performed.

## References
[1] K. Miura and T. Takahashi, *Projective Lifting Theorem, Complex Reflection Groups, and Quasi-Galois Points for Fermat Varieties*, arXiv:2610.09331v1 (first public 2026-10-07), especially Theorem 1.8, Example 4.3, Proposition 4.5 and Remark 4.7. https://arxiv.org/html/2610.09331v1

[2] K. Miura and S. Taki, *Quasi-Galois points for quartic surfaces*, arXiv:2608.25445v1 (first public 2026-08-26). https://arxiv.org/abs/2608.25445
