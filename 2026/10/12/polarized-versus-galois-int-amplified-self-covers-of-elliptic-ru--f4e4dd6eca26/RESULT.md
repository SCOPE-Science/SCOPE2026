# Polarized versus Galois int-amplified self-covers of elliptic ruled surfaces
## Finding
Let \(E\) be any elliptic curve over \(\mathbb C\), let \(L\in\operatorname{Pic}^0(E)\), and let \(X_L=\mathbf P_E(\mathcal O_E\oplus L)\), where projective bundles parameterize rank-one quotients. Then:

1. For each integer \(m\ge2\), there is a finite int-amplified Galois self-map \(f_m\) of \(X_L\) over \([m]:E\to E\). Its fiber degree is \(m\), total degree \(m^3\), and deck group is \((\mathbb Z/m\mathbb Z)^3\). The two eigenvalues of \(f_m^*\) on numerical divisor classes are \(m\) and \(m^2\).
2. The surface \(X_L\) admits a polarized surjective endomorphism **if and only if** \(L\) has finite order in \(\operatorname{Pic}^0(E)\). If the order is \(N\), any integer \(m\ge2\) satisfying \(m\equiv1\pmod N\) provides a polarized Galois map \(F_m\) over \([m]\) of fiber degree \(m^2\), total degree \(m^4\), and deck group \((\mathbb Z/m\mathbb Z)^2\times(\mathbb Z/m^2\mathbb Z)\). If \(L\) is nontorsion, *no* polarized self-map exists, even without requiring it to be Galois.

This is a sharp separation between Galois int-amplification and polarization within a geometrically natural class of toric fibrations over elliptic curves.

## Assumptions and scope
All varieties and morphisms are over \(\mathbb C\). A \(q\)-polarized morphism means a finite surjective endomorphism \(h\) with \(h^*H\simeq H^{\otimes q}\) for some ample line bundle \(H\) and integer \(q>1\). An endomorphism is *int-amplified* if \(h^*H\otimes H^{-1}\) is ample for some ample \(H\). A finite morphism is *Galois* when its function-field extension is Galois; its deck group is the automorphism group over the target. Put \(\pi:X_L\to E\) and \(\xi=c_1(\mathcal O_{X_L}(1))\). For a degree-one divisor \(B\) on \(E\), let \(F=\pi^*B\) numerically. The numerical intersection pairing satisfies \(\xi^2=F^2=0\) and \(\xi\cdot F=1\). A class \(a\xi+bF\) with \(a,b>0\) is ample. In particular, for a symmetric ample line bundle \(A\) on \(E\), the bundle \(\mathcal O_{X_L}(1)\otimes\pi^*A\) is ample.

## Proof
**Step 1: universal Galois int-amplified maps.** Every degree-zero holomorphic line bundle on an elliptic curve admits unitary flat multipliers. Choose \(E^{\mathrm{an}}=\mathbb C/\Lambda\) and a unitary character \(\rho:\Lambda\to\mathbb C^*\) representing \(L\). Write the analytic bundle as
\[
X_L^{\mathrm{an}}=(\mathbb C\times\mathbf P^1)/(z,[u:v])\sim(z+\lambda,[u:\rho(\lambda)v]).
\]
For any integer \(m\ge2\), the formula
\[
(z,[u:v])\longmapsto(mz,[u^m:v^m])
\]
descends: \(\rho(m\lambda)=\rho(\lambda)^m\). This is a holomorphic map between projective algebraic varieties, hence algebraic by GAGA. It is finite: the base isogeny \([m]\) has degree \(m^2\) and the map on each fiber has degree \(m\), so \(\deg f_m=m^3\).

The pullbacks are \(f_m^*\mathcal O_{X_L}(1)\simeq\mathcal O_{X_L}(m)\) and \(f_m^*\pi^*A\simeq\pi^*[m]^*A\). For symmetric \(A\), \([m]^*A\simeq A^{\otimes m^2}\), whence \(f_m^*(\xi+\pi^*c_1(A))-(\xi+\pi^*c_1(A))=(m-1)\xi+(m^2-1)\pi^*c_1(A)\) is ample. Thus \(f_m\) is int-amplified, with the asserted eigenvalues.

To compute its deck group, represent a base torsion point by \(\delta\in m^{-1}\Lambda\) modulo \(\Lambda\). For any choice of \(c\in\mathbb C^*\) satisfying \(c^m=\rho(m\delta)\), the translation-and-scaling map
\[
(z,[u:v])\longmapsto(z+\delta,[u:cv])
\]
descends to a deck transformation of \(f_m\). Different \(\delta\)'s give \(m^2\) classes; each admits \(m\) choices of \(c\). The resulting \(m^3\) commuting transformations are distinct and exhaust the possible deck group because \(\deg f_m=m^3\). Each has order dividing \(m\): its \(m\)-th power changes \(z\) by \(m\delta\in\Lambda\) and scales the second coordinate by \(c^m=\rho(m\delta)\), exactly the lattice identification. The finite abelian group has order \(m^3\) and exponent dividing \(m\), and its quotient by the vertical cyclic subgroup has type \((\mathbb Z/m\mathbb Z)^2\). More directly, lifts of the two standard generators of \(E[m]\) together with a generator of vertical \(\mu_m\) give three independent elements of order \(m\). Therefore the deck group is \((\mathbb Z/m\mathbb Z)^3\), and the function-field extension is Galois.

**Step 2: torsion bundles admit polarized Galois maps.** Suppose \(L\) has order \(N\), equivalently \(\rho\) may be chosen with values in \(\mu_N\). Select \(m\ge2\) with \(m\equiv1\pmod N\) and set \(q=m^2\). Because \(\rho(\lambda)^m=\rho(\lambda)^q\), the formula
\[
(z,[u:v])\longmapsto(mz,[u^q:v^q])
\]
descends to an algebraic self-map \(F_m\) of \(X_L\). It is finite of total degree \(m^2q=m^4\). It satisfies \(F_m^*\mathcal O_{X_L}(1)\simeq\mathcal O_{X_L}(q)\) and \(F_m^*\pi^*A\simeq(\pi^*A)^{\otimes q}\) for symmetric ample \(A\). Thus \(F_m\) is \(q\)-polarized by \(\mathcal O_{X_L}(1)\otimes\pi^*A\).

Its deck transformations again have the form \((z,[u:v])\mapsto(z+\delta,[u:cv])\), now with \(\delta\in m^{-1}\Lambda/\Lambda\) and \(c^q=\rho(m\delta)\). They give \(m^2q=m^4\) distinct commuting transformations. Choose a basis \(\lambda_1,\lambda_2\) of \(\Lambda\); the lifts \(\delta_i=\lambda_i/m\) can be given scalars \(c_i\) satisfying \(c_i^m=\rho(\lambda_i)\), which also ensure \(c_i^q=\rho(\lambda_i)\) because \(m\equiv1\pmod N\). Each lift has order \(m\), the two lift independently, and the fiberwise roots of unity form \(\mu_q\). This gives a direct product \((\mathbb Z/m\mathbb Z)^2\times\mathbb Z/q\mathbb Z\), exhausts the degree, and proves the stated Galois group.

**Step 3: nontorsion bundles admit no polarized maps.** Suppose instead that \(L\) has infinite order and that \(f:X_L\to X_L\) is a \(q\)-polarized surjective endomorphism, \(q>1\). Every map \(\mathbf P^1\to E\) is constant, so \(f\) induces a finite surjective map \(g:E\to E\). Restricting a polarization to a fiber shows that the degree on every fiber is \(q\). The projective-bundle Picard decomposition then gives
\[
f^*\mathcal O_{X_L}(1)\simeq\mathcal O_{X_L}(q)\otimes\pi^*M
\]
for some \(M\in\operatorname{Pic}(E)\). Squaring numerically, using \(\xi^2=0\) and \((f^*\xi)^2=(\deg f)\xi^2=0\), gives \(2q\deg M=0\), hence \(\deg M=0\). Because an ample divisor class on \(X_L\) has positive coefficients in the \(\xi,F\) basis, the \(q\)-polarization relation forces \(\deg g=q\).

The morphism of projective bundles is defined by a surjection
\[
\pi^*g^*(\mathcal O_E\oplus L)\twoheadrightarrow\mathcal O_{X_L}(q)\otimes\pi^*M.
\]
Its two components are relative homogeneous binary forms of degree \(q\). Using \(\pi_*\mathcal O_{X_L}(q)=\bigoplus_{j=0}^q L^{\otimes j}\), their coefficients lie, respectively, in
\[
\bigoplus_{j=0}^q H^0(E,M\otimes L^{\otimes j}),\qquad
\bigoplus_{j=0}^q H^0(E,M\otimes(g^*L)^{-1}\otimes L^{\otimes j}).
\]
On an elliptic curve a degree-zero line bundle has a nonzero section only when it is trivial. Since \(L\) has infinite order, at most one coefficient in each displayed direct sum is nonzero. Both forms must therefore be single monomials. To have no common zero anywhere on the \(\mathbf P^1\) fibers, the only two monomials must be the two pure powers \(u^q,v^q\). Their coefficient-line-bundle equalities imply
\[
g^*L\simeq L^{\otimes q}\quad\text{or}\quad g^*L\simeq L^{\otimes(-q)}.
\]
Every finite self-map of \(E\) is a translation composed with an isogeny \(\varphi\). Translation acts trivially on \(\operatorname{Pic}^0(E)\), and \(g^*L=\widehat\varphi(L)\). Thus \((\widehat\varphi\mp[q])(L)=0\). Every nonzero endomorphism of an elliptic curve has finite kernel, whereas \(L\) is nontorsion; consequently \(\widehat\varphi=\pm[q]\). This forces \(\deg g=q^2\), contradicting \(\deg g=q>1\). No polarized \(f\) exists. All possibilities for \(E\), including complex multiplication, are covered by the finite-kernel argument.

## Verification
The construction can be independently checked using a lattice basis \(\lambda_1,\lambda_2\) and a character \(\rho\). For universal \(f_m\), verify \(\rho(m\lambda)=\rho(\lambda)^m\), and for each \(\delta\in\tfrac1m\Lambda/\Lambda\), verify \(c^m=\rho(m\delta)\). The count \(m^2\cdot m=m^3\) matches the finite morphism degree and three commuting standard lifts independently generate the deck group. For torsion \(\rho^N=1\) and \(m\equiv1\pmod N\), repeat with fiber exponent \(q=m^2\), obtaining \(m^2q=m^4\) and the claimed product group. The obstruction is a universal algebraic argument, not a finite numerical enumeration: compute the two relative coefficient sums, use vanishing of sections of nontrivial degree-zero bundles, and compare \(\deg g=q\) with \(\deg g=q^2\). No external executable certificate is needed for the stated proof.

## Relationship to prior work
Jiang--Luo (arXiv:2610.05248v1, Theorem 1.1) gives a general necessary toric-fibration structure for smooth projective varieties with int-amplified Galois self-maps; it does not state the existence or the sharp polarization criterion here. Nakayama (2002, Proposition 5, Case (1)) already constructs nontrivial self-maps on elliptic ruled surfaces by a symmetric-power construction, which accounts for the **existence** portion at the unpolarized level; mere existence of those maps is not asserted to be new. Nakayama's later treatment of elliptic ruled surfaces and their group actions provides additional related constructions. The contribution here is the uniform **Galois deck-group determination** together with the exact **torsion if-and-only-if criterion for polarization**, including a proof that rules out *all* polarized endomorphisms in the nontorsion case.

## Limitations
Only decomposable degree-zero elliptic ruled surfaces over \(\mathbb C\) are treated. The result makes no classification of all possible int-amplified maps, nor of indecomposable ruled surfaces, higher-dimensional toric fibrations, positive characteristic, or the full automorphism groups. The Galois descriptions concern the displayed specific self-maps. An older differently worded dynamical criterion might imply the polarizability dichotomy; this is a residual literature-comparison risk and not a mathematical assertion of established novelty.

## References
- Zhiyuan Jiang and Yujie Luo, *Varieties Admitting Polarized Galois Endomorphisms*, arXiv:2610.05248v1 (first public October 4, 2026), https://arxiv.org/html/2610.05248v1 .
- Noboru Nakayama, *Ruled surfaces with non-trivial surjective endomorphisms*, Kyushu Journal of Mathematics 56 (2002), Proposition 5, https://www.jstage.jst.go.jp/article/kyushujm/56/2/56_2_433/_pdf .
- Noboru Nakayama, *On the structure of normal projective surfaces admitting non-isomorphic surjective endomorphisms*, RIMS preprint 1934, sections on elliptic ruled surfaces and finite-group-equivariant endomorphisms, https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1934.pdf .
- Noboru Nakayama and De-Qi Zhang, *Polarized endomorphisms of complex normal varieties*, arXiv:0908.1688, https://arxiv.org/pdf/0908.1688 .
