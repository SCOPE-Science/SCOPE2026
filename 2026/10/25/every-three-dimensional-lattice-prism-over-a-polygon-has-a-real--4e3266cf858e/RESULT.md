# Every three-dimensional lattice prism over a polygon has a real-rooted Ehrhart numerator

## Finding
For every full-dimensional lattice polygon \(P\) and integer \(k\ge1\), the Ehrhart \(h^*\)-polynomial of \(P\times[0,k]\) has exclusively negative real zeros. If \(I\) and \(B\) are the numbers of interior and boundary lattice points of \(P\), then
\[
H_{I,B,k}(t)=1+\big((k+1)(I+B)-4\big)t+\big(4kI+(2k-1)B-6k+3\big)t^2+(k-1)It^3.
\]
All zeros are distinct except when \((I,B,k)=(1,3,1)\), in which case \(H(t)=(1+2t)^2\). The degree is one when \(I=0,B=3\), two when \(I=0,B\ge4\) or \(k=1,I\ge1\), and three otherwise.

## Assumptions and scope
A lattice polygon is a two-dimensional convex polygon with integer vertices. Its boundary lattice count satisfies \(B\ge3\); its interior lattice count \(I\) is a nonnegative integer. The prism uses the ambient product lattice \(\mathbb Z^2\times\mathbb Z\). These are the only geometric facts about \(P\) needed in the proof, so the coefficient statement in fact holds formally for every pair of integers \(I\ge0\), \(B\ge3\) and every integer \(k\ge1\). Real-rootedness refers to all zeros of the polynomial, not those of the Ehrhart counting polynomial.

## Proof
Pick's theorem gives
\[
L_P(n)=\left(I+\frac B2-1\right)n^2+\frac B2n+1.
\]
By the product rule for lattice-point counts,
\[
L_{P\times[0,k]}(n)=(kn+1)L_P(n).
\]
Express the latter in the standard degree-three Ehrhart basis
\[
\sum_{n\ge0}L_{P\times[0,k]}(n)t^n=\frac{H_{I,B,k}(t)}{(1-t)^4}.
\]
Expanding yields exactly the displayed formula, with no asymptotic qualification.

The four coefficients of \(H\) are nonnegative, and each nonzero coefficient is positive: the coefficient of \(t\) is at least two; if \(I\ge1\), the coefficient of \(t^2\) is at least four for \(k\ge1,B\ge3\); if \(I=0\), the latter coefficient is \((2k-1)(B-3)\). Its leading coefficient is positive precisely in the degree regimes stated above. It remains to prove real-rootedness.

For a general cubic \(1+At+Ct^2+Dt^3\), its discriminant is
\[
\Delta=A^2C^2-4C^3-4A^3D-27D^2+18ACD.
\]
Insert \(A=(k+1)(I+B)-4\), \(C=4kI+(2k-1)B-6k+3\), and \(D=(k-1)I\). The following *finite integer-coefficient identities* establish nonnegativity on every admissible parameter triple. In chamber \(I=1+a\), \(B=3+b\), \(k=1+s\), the expanded discriminant \(\Delta(1+a,3+b,1+s)\) has exactly 72 nonzero monomials, all with strictly positive integral coefficients, except that its constant coefficient is zero. In the remaining chamber \(I=0\), \(B=4+b\), \(k=1+s\), the expanded discriminant has 25 nonzero monomials, all with strictly positive integral coefficients and with constant coefficient 12. The exact checker in the accompanying file `prism_root_certificate.py` verifies the identities by symbolic polynomial arithmetic, checks the full monomial coefficient lists, and gives independently checkable assertions for their positivity. The first chamber's degree-zero term vanishes only when \(a=b=s=0\), because, for example, its first-degree coefficients of \(a,b,s\) are respectively \(0,192,288\), while its coefficient of \(a^2\) is 64. Hence its discriminant vanishes only at \((I,B,k)=(1,3,1)\) and is strictly positive otherwise.

The exceptional corner \(I=0,B=3\) reduces to \(H(t)=1+(3k-1)t\) and has a single simple negative zero. In every other degree-two case the standard quadratic discriminant agrees with the displayed polynomial discriminant after setting \(D=0\), so positivity gives two distinct real zeros. In the degree-three case strict positivity gives three distinct real zeros. Because the constant coefficient is positive and all nonzero coefficients are positive, no zero is nonnegative, proving the desired negative-root assertion.

## Verification
The standalone `prism_root_certificate.py` uses exact symbolic arithmetic to calculate the discriminant, expand both parameter chambers, certify the numbers and signs of every monomial coefficient, and test 1,848 admissible integer parameter triples. It also checks the exceptional factorizations, including \(H_{1,3,1}=(1+2t)^2\). The symbolic polynomial identities, not the finite sample sweep, establish the unrestricted theorem. The checker requires Python 3 and SymPy.

## Relationship to prior work
Nill, *Lattice polytopes of large width have real-rooted Ehrhart* \(h^*\)*-polynomials* (arXiv:2608.03635, first public 4 August 2026), proves real-rootedness under a sufficiently large lattice-width hypothesis. The present theorem covers lattice prisms of arbitrarily small minimum width, regardless of whether the planar base itself is real-rooted. A previously recorded result, *Lattice-segment factors preserve Ehrhart* \(h^*\)*-log-concavity* (2026), establishes a weaker coefficient-preservation phenomenon: log-concavity does not by itself force real-rootedness. Feihu Liu's *Ehrhart Properties under Operations on Lattice Polytopes* (arXiv:2610.06338, 5 October 2026) addresses operations including Cartesian products and real-rootedness. Its available abstract and an article-level synopsis did not identify the unrestricted polygon-by-segment strengthening. Its full primary text was inaccessible during comparison and remains a material priority risk, not a certified absence of overlap.

## Limitations
The theorem concerns Cartesian products of planar lattice polygons with integer lattice segments, not all three-dimensional lattice polytopes or products of higher-dimensional factors. A finite exact polynomial certificate is supplied, but no independent human audit or exhaustive priority determination is claimed. The published Cartesian-product literature may contain an equivalent assertion not identified in the accessible material.

## References
1. B. Nill, *Lattice polytopes of large width have real-rooted Ehrhart h-star polynomials*, arXiv:2608.03635 (first public 2026-08-04), https://arxiv.org/abs/2608.03635.
2. F. Liu, *Ehrhart Properties under Operations on Lattice Polytopes*, arXiv:2610.06338 (first public 2026-10-05), https://arxiv.org/abs/2610.06338.
3. *Lattice-segment factors preserve Ehrhart h-star-log-concavity* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-lattice-segment-factors-preserve-ehrhart-h-log-concavity--5724d44ac8d4.
