# Integral topology and vanishing Brauer group of the index-66 K3–elliptic threefold

## Finding
Let \(S\) be the complex elliptic K3 surface with Weierstrass equation
\[
y^2=x^3+t(t^{11}-1),
\]
with its smooth minimal projective model. Put \(\zeta=\exp(2\pi i/66)\), and let
\[
g(x,y,t)=(\zeta^2x,\zeta^3y,\zeta^6t).
\]
For any complex elliptic curve \(E\) and a point \(P\in E\) of exact order \(66\), define the diagonal quotient
\[
V=(S\times E)/\langle(g,+P)\rangle.
\]
Then \(V\) is smooth and projective and its **complete integral cohomology profile** is
\[
H^k(V,\mathbb Z)\simeq\mathbb Z^{b_k},\quad
(b_0,b_1,b_2,b_3,b_4,b_5,b_6)=(1,2,3,4,3,2,1).
\]
In particular, the groups have no integral torsion, \(\pi_1(V)\simeq\mathbb Z^2\), and the cohomological and Azumaya Brauer groups over \(\mathbb C\) vanish:
\[
\operatorname{Br}(V)=0.
\]
The canonical bundle \(K_V\), while of exact torsion order \(66\), is topologically trivial: \(c_1(K_V)=0\) in \(H^2(V,\mathbb Z)\), and \(K_V\in\operatorname{Pic}^0(V)[66]\). The nonzero low-degree Hodge numbers are \(h^{1,0}=1\), \(h^{1,1}=3\), \(h^{2,1}=2\), while \(h^{2,0}=h^{3,0}=0\).

## Assumptions and scope
The base field is \(\mathbb C\). The K3 surface is its smooth minimal elliptic model; the indicated automorphism extends to this model. The point \(P\) must have exact order \(66\), ensuring a free diagonal action. The computation is uniform in \(E\) and \(P\). The term Calabi–Yau is used in the torsion-canonical sense \(K_V\sim_{\mathbb Q}0\), not in the stricter sense of trivial canonical line bundle. The source establishes the exact canonical order; the new statement concerns integral cohomology, fundamental group, Hodge profile, and Brauer vanishing.

## Proof
**1. The integral action on the K3 lattice.** All terms in \(y^2=x^3+t^{12}-t\) transform by \(\zeta^6\), so \(g\) is a well-defined automorphism. The holomorphic two-form transforms as
\[
g^*(dt\wedge dx/y)=\zeta^{6+2-3}(dt\wedge dx/y)=\zeta^5(dt\wedge dx/y).
\]
Because \(\gcd(5,66)=1\), this eigenvalue has exact order \(66\). Kondō's determination of this surface, recalled in Festi–Nijgh–Platt, gives \(\operatorname{NS}(S)\cong U\), the rank-two unimodular hyperbolic plane. The elliptic fibre and zero section are both preserved by \(g\) and generate \(\operatorname{NS}(S)\), so \(g^*\) is the identity on that lattice.

The inclusion \(\operatorname{NS}(S)\hookrightarrow H^2(S,\mathbb Z)\) is primitive. Since the K3 lattice and its sublattice \(U\) are unimodular, there is an **integral** orthogonal decomposition
\[
H^2(S,\mathbb Z)=U\oplus T,
\qquad \operatorname{rank}T=20,
\]
where \(T\) is stable under \(g^*\). The primitive-eigenvalue vector \(H^{2,0}(S)\subset T\otimes\mathbb C\) forces the cyclotomic polynomial \(\Phi_{66}\) to divide the characteristic polynomial of \(g^*|_{T\otimes\mathbb Q}\). Because \(\deg\Phi_{66}=\varphi(66)=20=\operatorname{rank}T\), this characteristic polynomial is exactly \(\Phi_{66}\). In particular,
\[
\det(1-g^*\mid T)=\Phi_{66}(1)=1.
\]
Thus \(1-g^*\) is an automorphism of the **integral** free group \(T\), and
\[
\ker(1-g^*\mid H^2(S,\mathbb Z))\cong U,
\qquad
\operatorname{coker}(1-g^*\mid H^2(S,\mathbb Z))\cong U.
\]
The latter is torsion-free; the integral, rather than merely rational, determinant statement is essential.

**2. Mapping-torus model and cohomology.** Write \(E=\mathbb C/\Lambda\). Since \(P\) has exact order \(66\), a change of integral lattice basis writes it as one sixty-sixth of the first primitive period. Consequently the lattice of \(E/\langle P\rangle\) has generators corresponding to translation by \(P\) and the untouched second period. The quotient \(V\) is therefore diffeomorphic to the product of a mapping torus \(M_g\) of the K3 diffeomorphism \(g\) and a circle:
\[
V\simeq M_g\times S^1.
\]
Equivalently, it is a smooth K3 bundle over a two-torus with monodromy \(g\) along one generator and identity along the other. Since \(S\) is simply connected, its homotopy long exact sequence gives \(\pi_1(V)\cong\mathbb Z^2\).

The integral Wang sequence for \(S\to M_g\to S^1\), together with \(H^j(S,\mathbb Z)=\mathbb Z\) for \(j=0,4\), \(\mathbb Z^{22}\) for \(j=2\), and zero for other \(j\), yields
\[
(H^0,H^1,H^2,H^3,H^4,H^5)(M_g;\mathbb Z)
\cong (\mathbb Z,\mathbb Z,U,U,\mathbb Z,\mathbb Z).
\]
There is no torsion or hidden extension since the relevant kernel and cokernel are free. Integral Künneth with \(S^1\) now gives the seven claimed cohomology groups. The Betti polynomial is
\[
1+2t+3t^2+4t^3+3t^4+2t^5+t^6.
\]

**3. Hodge numbers and the Brauer group.** Translation acts trivially on the cohomology of \(E\). The action on \(H^{2,0}(S)\) is by the primitive eigenvalue \(\zeta^5\), while \(H^{1,1}(S)^g\) has dimension \(2\), represented by the invariant \(U\). The invariant Künneth decomposition of \(S\times E\) thus gives
\[
h^{1,0}(V)=1,\quad h^{2,0}(V)=h^{3,0}(V)=0,\quad
h^{1,1}(V)=2+1=3,\quad h^{2,1}(V)=2.
\]
In particular, \(H^2(V,\mathcal O_V)=H^{0,2}(V)=0\). The analytic exponential sequence contains
\[
H^2(V,\mathcal O_V)\longrightarrow H^2(V,\mathcal O_V^*)
\longrightarrow H^3(V,\mathbb Z).
\]
The left term vanishes and the right is \(\mathbb Z^4\), so the middle group has no torsion. Its torsion subgroup, equal to the cohomological Brauer group of smooth projective \(V\), is zero. The Azumaya Brauer group injects into the cohomological group, so it also vanishes. Finally, the known relation \(K_V^{\otimes66}\cong\mathcal O_V\) forces \(c_1(K_V)\) to be torsion, hence zero in the free group \(H^2(V,\mathbb Z)\); the exponential sequence for line bundles places \(K_V\) in \(\operatorname{Pic}^0(V)\).

## Verification
The standalone standard-library checker \(\texttt{artifacts/verify_integral_cohom.py}\) reconstructs the cyclotomic polynomial \(\Phi_{66}\) by monic integer-polynomial division, verifies \(\Phi_{66}(1)=1\) and \(\deg\Phi_{66}=20\), verifies the Weierstrass scaling and primitive two-form multiplier, and reconstructs all cohomology ranks from the Wang sequence and Künneth formula. Run it using \(\texttt{python3 artifacts/verify_integral_cohom.py}\). The mathematical proof of the lattice decomposition and of the mapping-torus model is given above; computation is a check, not a substitute for those arguments.

## Relationship to prior work
Singh, *Smooth Calabi–Yau varieties with large index and Betti numbers*, arXiv:2502.07031v1 (10 February 2025), describes the smooth index-66 quotient \((S\times E)/\mu_{66}\). Its Betti-number extremality theorem for the separate varieties \(W^{(n)}\) is not an integral cohomology computation for this quotient \(V\). Festi–Nijgh–Platt record Kondō's identification \(\operatorname{NS}(S)\simeq U\), the integral lattice input used here. Hashimoto–Kanazawa compute Brauer groups for eight threefolds with *trivial* canonical bundle and \(H^1(\mathcal O)=0\); their type-K theorem does not cover this quotient with exact-order-66 canonical bundle and \(h^{1,0}=1\). The source methods of integral monodromy, the Wang sequence, and the exponential sequence are standard; the contribution is their explicit combination into a complete torsion-sensitive classification for this extremal quotient.

## Limitations
The result applies to the specified cyclic order-66 quotient, not to arbitrary K3–elliptic quotients or higher-dimensional constructions in Singh's paper. No assertion is made about the cup-product ring, integral Hodge conjecture, derived equivalence or arithmetic Brauer groups over nonclosed fields. The cohomological calculation uses the established Picard lattice \(U\) and the explicit automorphism; changing either may introduce torsion. Although focused sources were compared, a prior computation under different terminology cannot be ruled out without a comprehensive independent bibliographic review.

## References
1. J. Singh, *Smooth Calabi–Yau varieties with large index and Betti numbers*, arXiv:2502.07031v1 (2025), https://arxiv.org/html/2502.07031v1 ; published as *Math. Z.* 312, 105 (2026), DOI 10.1007/s00209-026-03984-y.
2. D. Festi, W. Nijgh, D. Platt, *K3 surfaces with two involutions and low Picard number*, *Geom. Dedicata* 218, 55 (2024), DOI 10.1007/s10711-024-00900-8, proof of Theorem 1.1 on \(S_{66}\).
3. J. Keum, *K3 surfaces with an automorphism of order 66, the maximum possible*, arXiv:1402.6803 (2014).
4. K. Hashimoto, A. Kanazawa, *Calabi–Yau threefolds of type K (II): mirror symmetry*, arXiv:1511.08778v4 (2016), Introduction and §3.3 on Brauer groups.
