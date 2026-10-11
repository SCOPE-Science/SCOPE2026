# Sharp eighth-moment norm at the first fourth-order resonance
## Finding
For
\[
F(t)=a+b e^{2\pi i t}+c e^{8\pi i t},\qquad t\in\mathbb T=\mathbb R/\mathbb Z,
\]
with normalized Haar measure, the sharp constant in
\[
\|F\|_{L^8(\mathbb T)}\le K_{014}\bigl(|a|^2+|b|^2+|c|^2\bigr)^{1/2}
\]
is
\[
K_{014}^8=7.98907574969577216970045944396471238998\ldots,
\qquad
K_{014}=1.29661806292010189814543058072792764\ldots.
\]
Set \(x=|a|^2/|b|^2\) and \(r=|c|/|a|\) when all coefficients are nonzero. Define
\[
Q(x,r)=r^8x^4+16r^6x^4+16r^6x^3+36r^4x^4+144r^4x^3+36r^4x^2+16r^2x^4+144r^2x^3+144r^2x^2+16r^2x+8rx^2+x^4+16x^3+36x^2+16x+1
\]
and
\[
\Phi(x,r)=\frac{Q(x,r)}{(1+x(1+r^2))^4}.
\]
The pair \((x_*,r_*)\) is the unique positive common zero of
\[
F_1(x,r)=3r^8x^3+24r^6x^3+6r^6x^2+36r^4x^3-18r^4x^2-6r^4x+4r^3x^2+24r^2x^3-18r^2x^2-48r^2x-3r^2+4rx^2-4rx+3x^3+6x^2-6x-3
\]
and
\[
F_2(x,r)=3r^7x^4+3r^7x^3+6r^5x^4+48r^5x^3+6r^5x^2-6r^3x^4+18r^3x^3+18r^3x^2-6r^3x+7r^2x^2-3rx^4-24rx^3-36rx^2-24rx-3r-x^2-x.
\]
It satisfies
\[
r_*\in(0.98759,0.98761),\qquad
x_*=0.9880153848895182488949808390\ldots.
\]
Then \(K_{014}^8=\Phi(x_*,r_*)\). Every nonzero extremizer is characterized exactly by
\[
\frac{|a|^2}{|b|^2}=x_*,\qquad
\frac{|c|}{|a|}=r_*,\qquad
4\arg b-3\arg a-\arg c\equiv0\pmod{2\pi}.
\]

## Assumptions and scope
The statement concerns the continuous circle and arbitrary complex coefficients. The spectrum is exactly \(\{0,1,4}\); translation and multiplication of all frequencies by a nonzero integer do not change the constant. The result does not claim a formula for other three-frequency spectra or for other exponents.

The support \(\{0,1,4}\) is a natural first-resonance example: sums of at most three selected frequencies have no nontrivial collision, while at four summands the relation \(4\cdot1=3\cdot0+1\cdot4\) appears.

## Proof
Write \(A=|a|\), \(B=|b|\), and \(C=|c|\). Parseval applied to \(F^4\) gives the eighth moment. Among the fifteen multinomial terms in \(F^4\), the only distinct exponent triples with the same frequency sum are \((0,4,0)\) and \((3,0,1)\), because equality of two frequency sums forces their difference to be an integer multiple of \((-3,4,-1)\), and the degree-four simplex allows only this pair. Therefore
\[
\|F\|_8^8=M_0(A^2,B^2,C^2)+8A^3B^4C\cos(4\arg b-3\arg a-\arg c),
\]
where \(M_0\) is the collision-free three-variable Steinhaus moment. Hence every interior maximizer must satisfy phase alignment
\[
4\arg b-3\arg a-\arg c\equiv0\pmod{2\pi}.
\]

By homogeneity set \(B=1\), put \(x=A^2\) and \(r=C/A\), and impose the phase alignment. Direct expansion then gives \(\Phi(x,r)\) above. Differentiation gives
\[
\partial_x\Phi=-\frac{4F_1(x,r)}{(1+x(1+r^2))^5},
\qquad
\partial_r\Phi=-\frac{8xF_2(x,r)}{(1+x(1+r^2))^5}.
\]
Thus every positive stationary point is a positive common zero of \(F_1,F_2\).

The exact elimination certificate in `verify.py` computes the resultant of \(F_1,F_2\) with respect to \(x\) and factors it as a strictly positive polynomial for \(r>0\), times \(P(r)\), where
\[
P(r)=30375r^{21}+8100r^{20}+294840r^{19}+68499r^{18}+7884r^{17}-60237r^{16}-759429r^{15}-321336r^{14}-325152r^{13}+155736r^{12}+323484r^{11}+248886r^{10}+742505r^9+97182r^8+20062r^7-162720r^6-303994r^5-36804r^4-30665r^3-2709r^2+90r+3.
\]
Sturm counting shows that \(P\) has exactly four positive roots, isolated in
\[
(0.0406,0.0407),\quad (0.9336,0.9337),\quad (0.98759,0.98761),\quad (1.1470,1.1471).
\]
The linear subresultant gives the unique common \(x\)-root over each such \(r\). Exact sign checks on the four isolating intervals show that the corresponding \(x\) is negative for the first, second, and fourth roots and positive only for the third. Hence \((x_*,r_*)\) is the unique positive stationary point.

On every boundary face one coefficient vanishes, leaving a two-frequency polynomial. Its sharp eighth-moment ratio is
\[
2^{-4}\binom{8}{4}=\frac{35}{8}.
\]
At the interior test point \(A=B=C\) with aligned phase, the ratio is
\[
\frac{639+8}{3^4}=\frac{647}{81}>\frac{35}{8}.
\]
Therefore a global maximizer cannot lie on the boundary. Compactness after \(L^2\)-normalization guarantees a maximizer; it is interior, hence stationary, hence the unique positive stationary point found above. This proves the sharp constant and the magnitude ratios. The phase condition is forced by strict positivity of the resonant cross term at an interior extremizer.

## Verification
Run `python verify.py`. The verifier reconstructs the degree-four convolution, checks that the only collision is \((0,4,0)\leftrightarrow(3,0,1)\), derives \(Q,F_1,F_2\), factors the exact resultant, uses Sturm root counts on rational intervals, checks the signs supplied by the linear subresultant, verifies the two-frequency boundary value, and evaluates the unique positive stationary point numerically to high precision.

## Relationship to prior work
Michels defines the classical \(\Lambda(p)\) constant \(K_p(\Lambda)\) for character sets and studies structural characterizations of sets that are \(\Lambda(p)\) for all \(p>2\), rather than exact constants for a fixed finite spectrum. Peskir proves Schur-concavity for even moments of sums of independent complex Steinhaus variables. That theorem controls the collision-free baseline but does not contain the deterministic fourth-order resonance \(b^4\) against \(a^3c\) that shifts the optimizer here.

A published exact phase-moment result for three-frequency unimodular sums identifies \(\{0,1,4}\) as first becoming phase-sensitive at the eighth moment. Its coefficients are constrained to equal magnitude, so it gives the value of the resonant phase response on one slice but not the arbitrary-amplitude \(L^2\to L^8\) norm or its extremizing amplitude ratios.

## Limitations
The originality search cannot exclude an older equivalent finite-\(\Lambda(p)\) computation hidden under substantially different notation. The proof is exact, but the compact algebraic description of \((x_*,r_*)\) is by a rational polynomial system and an isolating interval rather than by radicals. No claim is made for finite cyclic sampling, where additional aliasing can occur.

## References
1. C. Michels, “\(\Lambda(p)\)-sets and the limit order of operator ideals,” arXiv:math/9904176v1, first public 1999-04-30. The arXiv metadata lists MSC 43A46 among the primary classes.
2. G. Peskir, “Best constants in Kahane–Khintchine inequalities for complex Steinhaus functions,” Proceedings of the American Mathematical Society 123 (1995/1996 publication record), DOI 10.2307/2160667. The inspected full text includes the Schur-concavity theorem for even Steinhaus moments.
