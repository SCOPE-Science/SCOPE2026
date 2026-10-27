# Sharp fourth moment and complete complex equality cases for the tetrahedral squarefree Fourier chaos

## Finding
For the six squarefree degree-two Fourier characters supported on the edges of the tetrahedron, the exact fourth-power \(L^2\)-to-\(L^4\) norm is \(5/2\):
\[
\int_{\mathbb T^4}\left|\sum_{1\le i<j\le4}a_{ij}z_i z_j\right|^4\,dm(z)
\le\frac52\left(\sum_{i<j}|a_{ij}|^2\right)^2.
\]
The constant is attained, and all nonzero equality cases have equal coefficient magnitudes and satisfy the complex matching relation
\[
a_{12}a_{34}=a_{13}a_{24}=a_{14}a_{23}.
\]
Equivalently, each equality array has \(a_{ij}=\lambda u_i u_j\) for one nonzero scalar \(\lambda\) and unit phases \(u_i\).

## Assumptions and scope
The domain is \(\mathbb T^4=\{z\in\mathbb C^4:|z_i|=1\}\), endowed with normalized Haar measure. Coefficients \(a_{ij}\in\mathbb C\) are arbitrary; \(S=\sum_{i<j}|a_{ij}|^2\). Parseval gives \(\|P\|_2^2=S\). The zero array gives trivial equality and is excluded from the nonzero classification. Characters have their usual distinct monomial exponents in \(\mathbb Z^4\); the result need not hold unchanged after low-order torsion identifications.

## Proof
Put \(u=a_{12}a_{34}\), \(v=a_{13}a_{24}\), and \(w=a_{14}a_{23}\). Distinct unordered edge pairs have distinct vector sums except for the three perfect matchings, whose two-edge sums all equal \((1,1,1,1)\). Fourier orthogonality applied to \(P^2\) therefore gives the *exact* identity
\[
\|P\|_4^4=2S^2-\sum_{i<j}|a_{ij}|^4
   +8\operatorname{Re}(u\overline v+u\overline w+v\overline w).
\tag{1}
\]
For the three matchings let
\[
b_1=|a_{12}|^2+|a_{34}|^2,\quad
b_2=|a_{13}|^2+|a_{24}|^2,\quad
b_3=|a_{14}|^2+|a_{23}|^2.
\]
Then \(b_1+b_2+b_3=S\). By two-term Cauchy–Schwarz, the fourth-power sum for each matching is at least \(b_j^2/2\), with equality precisely when its two coefficients have equal magnitudes. By the arithmetic–geometric mean inequality, \(|u|\le b_1/2\), \(|v|\le b_2/2\), \(|w|\le b_3/2\), again with precisely the same magnitude equality conditions. Hence (1) implies
\[
\|P\|_4^4
\le2S^2-\frac12\sum_{j=1}^3b_j^2
  +2\sum_{1\le i<j\le3}b_i b_j
=3S^2-\frac32\sum_{j=1}^3b_j^2
\le\frac52 S^2.
\]
The last inequality is Cauchy–Schwarz, \(\sum b_j^2\ge S^2/3\). Equality requires \(b_1=b_2=b_3=S/3\), equal magnitudes within each matching, and equality in all three cross-product real-part bounds. For \(S>0\) this means every \(|a_{ij}|=\sqrt{S/6}\) and \(u,v,w\) have identical phase, hence \(u=v=w\). Conversely these conditions make every displayed bound an equality, proving completeness.

For the equivalent factorization, normalize all coefficients to unit modulus, choose a unit square root \(u_1\) of \(a_{12}a_{13}/a_{23}\), and define \(u_j=a_{1j}/u_1\) for \(j=2,3,4\). Then \(u_2u_3=a_{23}\) by construction. The relations \(a_{12}a_{34}=a_{13}a_{24}=a_{14}a_{23}\) give \(u_2u_4=a_{24}\) and \(u_3u_4=a_{34}\). Restoring the common positive magnitude gives the stated factorization.

## Verification
The standalone `checker.py` enumerates ordered edge pairs and their exponent-vector sums, checks the unique three-matching collision, verifies (1) for 500 deterministic randomly chosen integer coefficient arrays, and checks the sharp equality witness using exact rational arithmetic. Run it with `python checker.py`; no external Python package is needed. The analytical Cauchy–Schwarz and phase-equality argument above, not the finite sampling tests, proves the theorem for all complex coefficients.

## Relationship to prior work
Iosevich, Koh, and Lewko develop Fourier extension estimates via additive-energy control (2017 preprint, arXiv:1712.05549); this finding addresses a separate exact small-spectrum complex torus norm. Ciccone and Gonçalves study arithmetic restrictions and sharp Fourier extension on the Euclidean circle (2022 preprint, arXiv:2208.09441), rather than this tetrahedral fourth-moment optimization. The existing exact four-point single-additive-collision result addresses spectra with only **one** colliding pair of pair sums; here **three** distinct perfect matchings share the same sum, so its constant and equality characterization do not follow. Analogous quadratic Walsh chaos estimates concern order-two characters, for which additional exponent cancellations change the moment identity.

## Limitations
No sharp fourth-moment formula is claimed for five or more torus variables, for sparse proper subgraphs with other incidence patterns, or for coefficient groups of exponent two. General-purpose hypercontractivity bounds may be stronger or weaker in different regimes and are not asserted to be sharp here. Although searched references did not disclose this exact theorem, an equivalent older quadratic-chaos or graph-polynomial inequality cannot be excluded without an independent bibliographic audit. No external independent mathematical validation has been performed.

## References
1. A. Iosevich, D. Koh, and M. Lewko, *Finite field restriction estimates for the paraboloid in high even dimensions*, arXiv:1712.05549 (first posted 2017-12-15), https://arxiv.org/abs/1712.05549.
2. V. Ciccone and F. Gonçalves, *Sharp Fourier Extension on the Circle Under Arithmetic Constraints*, arXiv:2208.09441 (first posted 2022-08-19), https://arxiv.org/abs/2208.09441.
3. *Sharp \(L^2\)-to-\(L^4\) constants for a single additive collision*, publicly indexed mathematical research result, 2026. Its one-collision hypothesis excludes the tetrahedral triple collision studied here.
