# Exact positive spectrum and multiplicity pattern of the preferred-orientation tetrahedron
## Finding
For the unit-edge tetrahedral metric graph with the degree-three preferred-orientation coupling, the positive spectrum admits a complete exact classification. For \(k>0\) away from the points \(2\pi\mathbb N\), the energy \(k^2\) is spectral exactly when
\[
\tan^2(k/2)=k^2+2
\]
or
\[
k\tan(k/2)=\pm\sqrt3.
\]
Every root of the first equation has multiplicity exactly three. Every root of either signed second equation has multiplicity exactly one. At \(k=2n\pi\), \(n\ge1\), the multiplicity is exactly four.

For each integer \(m\ge0\), the first equation has exactly one root in each half-period \((2m\pi,(2m+1)\pi)\) and \(((2m+1)\pi,(2m+2)\pi)\). The equation with \(+\sqrt3\) has exactly one root in the first half-period, while the equation with \(-\sqrt3\) has exactly one root in the second. Consequently each interval \((2m\pi,2(m+1)\pi]\) carries total spectral multiplicity twelve.

Writing \(P_m=(2m+1)\pi\), the two triple roots adjacent to \(P_m\) obey
\[
k=P_m\pm\frac{2}{P_m}+O(P_m^{-3}),
\qquad
k^2=P_m^2\pm4+O(P_m^{-2}).
\]
Writing \(E_n=2n\pi\), the two simple roots adjacent to \(E_n\) obey
\[
k=E_n\pm\frac{2\sqrt3}{E_n}+O(E_n^{-3}),
\qquad
k^2=E_n^2\pm4\sqrt3+O(E_n^{-2}).
\]

## Assumptions and scope
The graph is the equilateral tetrahedron with six edges of length one. On every degree-three vertex the boundary condition is the cyclic preferred-orientation condition defined by the unitary cyclic shift matrix, in the normalization where the distinguished momentum is \(k=1\). Only positive energies are classified. No assertion is made here about negative spectrum. The statement includes the exceptional positive points \(k=2n\pi\) separately.

## Proof
Exner and Lipovský decompose the operator under the order-three rotation into sectors \(j=0,1,2\). Their exact secular equations for the preferred-orientation coupling are, up to nonzero scalar factors,
\[
D_0(k)=k\sin^2(k/2)A(k),
\]
\[
D_j(k)=k\sin(k/2)B_j(k)A(k),\qquad j=1,2,
\]
where
\[
A(k)=(k^2+3)\cos^2(k/2)-1,
\qquad
B_j(k)=k\sin(k/2)-(-1)^j\sqrt3\cos(k/2).
\]
For \(k\notin2\pi\mathbb N\), a zero of \(A\) is equivalent to \(\tan^2(k/2)=k^2+2\), while a zero of \(B_j\) is equivalent to \(k\tan(k/2)=(-1)^j\sqrt3\). These alternatives are disjoint: simultaneous satisfaction would force \(k^2=1\) from the two squared equations, but then \(1/2<\pi/4\) gives \(\tan^2(1/2)<1\), not \(3\).

On a half-period where \(\tan(k/2)>0\), the function \(k\tan(k/2)\) increases from zero to infinity, so the \(+\sqrt3\) equation has exactly one root. The quotient
\[
\frac{\tan(k/2)}{\sqrt{k^2+2}}
\]
is also strictly increasing there because its derivative has numerator proportional to
\[
(k^2+2)(1+t^2)-2kt,
\qquad t=\tan(k/2),
\]
whose discriminant as a quadratic in \(t\) is negative. Hence the first equation has exactly one root in that half-period. On a half-period where \(\tan(k/2)<0\), the quantity \(-\tan(k/2)/\sqrt{k^2+2}\) decreases from infinity to zero, giving exactly one root of the first equation. Also \(k\tan(k/2)\) increases from minus infinity to zero because, for \(k>\pi\),
\[
\frac{d}{dk}\bigl(k\tan(k/2)\bigr)=t+\frac{k}{2}(1+t^2)>0,
\]
so the \(-\sqrt3\) equation has exactly one root.

Every zero of \(A\) is simple. Indeed, at such a zero, with \(t=\tan(k/2)\), one has \(t^2=k^2+2\) and
\[
A'(k)=\frac{2k}{k^2+3}-t,
\]
which cannot vanish because \(k^2+2>4k^2/(k^2+3)^2\). Every zero of \(B_j\) is simple as well, since the derivative of \(k\tan(k/2)\) is nonzero at the relevant root. Therefore an \(A\)-root is a simple zero in each of the three orthogonal rotation sectors and contributes multiplicity three, while a \(B_j\)-root occurs in exactly one sector and contributes multiplicity one.

At \(k=2n\pi\), the common factor \(A(k)\) and both \(B_j(k)\) are nonzero. In the \(j=0\) reduced boundary system, substituting \(\sin k=0\) and \(\cos k=1\) leaves one independent linear relation among three amplitudes, so the kernel has dimension two. In each of the \(j=1,2\) systems, the Robin relation together with the remaining vertex equations leaves one free amplitude, so each kernel has dimension one. The total multiplicity is therefore \(2+1+1=4\).

For the asymptotics near an odd multiple \(P_m\), put \(k=P_m+\delta\). Then \(\tan(k/2)=-\cot(\delta/2)\), and the first equation with the expansion \(\cot(\delta/2)=2/\delta+O(\delta)\) gives \(\delta=\pm2/P_m+O(P_m^{-3})\). Near an even multiple \(E_n\), \(\tan((E_n+\delta)/2)=\delta/2+O(\delta^3)\), so the signed equation gives \(\delta=\pm2\sqrt3/E_n+O(E_n^{-3})\). Squaring yields the stated energy shifts.

## Verification
The accompanying `artifacts/verify.py` independently brackets the two scalar roots in every half-period for a range of periods, checks the secular factors numerically, checks the predicted multiplicity count of twelve per full momentum period, and verifies convergence of the scaled root and energy offsets to \(2\), \(4\), \(2\sqrt3\), and \(4\sqrt3\). These finite checks corroborate the analytic proof; they are not used to infer the infinite statements.

## Relationship to prior work
The primary paper gives the three exact sector secular equations and then states only a high-energy enclosure theorem for the tetrahedron: all large positive wave numbers lie within an \(O(k^{-1})\) neighborhood of integer multiples of \(\pi\). It does not state the global one-root-per-half-period classification, the exact multiplicities \(3,1,4\), or the sharp satellite energy shifts \(\pm4\) and \(\pm4\sqrt3\). A later habilitation thesis reproduces the same interval theorem as its tetrahedron summary. A 2025 paper on spectral statistics of preferred-orientation graphs studies mainly incommensurate cube and octahedron examples and does not supply this equilateral tetrahedron classification.

## Limitations
The result depends on the unit-edge equilateral geometry and the specific cyclic preferred-orientation coupling. It does not classify the negative spectrum, perturbations of edge lengths, or other vertex couplings. The originality search cannot exclude an unindexed derivation under different notation.

## References
1. P. Exner and J. Lipovský, *Spectral asymptotics of the Laplacian on Platonic solids graphs*, arXiv:1906.09091v1 (2019), especially Eqs. (10)-(11) and Theorem 3.2; DOI 10.1063/1.5116100.
2. J. Lipovský, *Quantum Graphs and Their Generalizations*, habilitation thesis (2022), Section 2.8.1 and Theorem 2.16.
3. R. Band, P. Exner, D. Goel, and A. Strauss, *Spectral statistics of preferred orientation quantum graphs*, arXiv:2508.04869 (2025).
