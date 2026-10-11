# Three-point extreme Sidon sets are exactly the order-three and order-four torsion patterns
## Finding
Let \(G\) be a discrete abelian group and let \(E\subset G\) have exactly three elements. Define its Sidon constant by
\[
S(E)=\sup_{0\ne\mu\in M(E)}\frac{\|\mu\|_1}{\|\widehat\mu\|_\infty}.
\]
Then the maximal possible value \(S(E)=\sqrt3\) occurs if and only if, after translation, exactly one of the following holds:

1. \(E=\{0,d,2d\}\) with \(3d=0\) and \(d\ne0\); equivalently, \(E\) is a coset of a subgroup of order \(3\).
2. \(E=\{0,d,2d\}\) with \(4d=0\) and \(2d\ne0\); equivalently, \(E\) consists of three points of a coset of a cyclic subgroup of order \(4\).

Thus no three-point subset of a Klein four subgroup is extreme, and no other three-point support in any abelian group has Sidon constant \(\sqrt3\).

## Assumptions and scope
The group is discrete abelian and the dual group carries normalized Haar measure. The measure \(\mu\) is supported on exactly the three points of \(E\). Translation of \(E\), multiplication of \(\mu\) by a scalar of modulus one, and modulation by a character do not change the Sidon ratio.

The statement classifies only the extremal boundary \(S(E)=\sqrt{|E|}\) for three-point supports. It does not give the exact nonextremal value of \(S(E)\) for every other three-point subset.

## Proof
For \(E=\{x_0,x_1,x_2\}\) and \(\mu=\sum_j c_j\delta_{x_j}\), Cauchy--Schwarz and Plancherel give
\[
\|\mu\|_1\le \sqrt3\,\|\mu\|_2
 =\sqrt3\,\|\widehat\mu\|_2
 \le\sqrt3\,\|\widehat\mu\|_\infty.
\]
Hence \(S(E)\le\sqrt3\). If equality holds, compactness of the coefficient sphere gives an extremizing \(\mu\), and equality in both displayed inequalities forces
\[
|c_0|=|c_1|=|c_2|
\]
and \(|\widehat\mu|\) to be constant on the dual group. After scaling, assume all three coefficient moduli are one.

Translate the support to \(E=\{0,a,b\}\). Write the normalized coefficients as \(1,p,q\), where \(|p|=|q|=1\). Then
\[
|1+p\chi(a)+q\chi(b)|^2
\]
has Fourier support in the six directed differences
\[
\pm a,\qquad \pm b,\qquad \pm(a-b).
\]
If this squared modulus is constant, the coefficient at every nonzero difference must vanish. In particular, no nonzero difference may have a unique ordered representation by two points of \(E\).

The difference \(a=a-0\) must therefore have another representation. Checking the other five ordered pairs shows that one of
\[
2a=0,
\qquad b=-a,
\qquad b=2a
\]
must hold. If \(b=-a\) or \(b=2a\), then after reordering
\[
E=\{0,d,2d\}.
\]
Its directed differences are \(d\) twice, \(-d\) twice, \(2d\) once, and \(-2d\) once before torsion identifications. The difference \(2d\) can be repeated only when
\[
3d=0\quad\text{or}\quad4d=0.
\]
Distinctness excludes orders one and two, leaving exactly orders three and four.

It remains to analyze the branch \(2a=0\). Repeating the difference \(b=b-0\) forces either \(2b=0\) or \(a=2b\). The second case is again the order-four progression above. In the first case \(a\) and \(b\) are distinct involutions, so \(E\) lies in a Klein four subgroup. Constancy would require the three nontrivial Fourier coefficients of the squared modulus to vanish:
\[
p+\overline p=0,
\qquad q+\overline q=0,
\qquad p\overline q+\overline p q=0.
\]
The first two equations give \(p,q\in\{i,-i\}\), but then \(p\overline q\in\{1,-1\}\), contradicting the third equation. Hence the Klein four pattern is impossible.

Conversely, both surviving torsion patterns are extreme. If \(d\) has order three, put \(\omega=e^{2\pi i/3}\) and use coefficients
\[
(1,1,\omega)
\]
on \(\{0,d,2d\}\). The nonconstant coefficient of the squared modulus is proportional to
\[
1+\omega+\omega^2=0,
\]
so \(|\widehat\mu|\equiv\sqrt3\). If \(d\) has order four, use
\[
(1,e^{-\pi i/4},i).
\]
The coefficients at the order-four and order-two differences vanish because
\[
e^{-\pi i/4}+i e^{\pi i/4}=0,
\qquad i-i=0.
\]
Again \(|\widehat\mu|\equiv\sqrt3\). In both cases \(\|\mu\|_1=3\), so the Sidon ratio is \(\sqrt3\), completing the classification.

## Verification
The proof is algebraic and applies to every discrete abelian group. The accompanying `artifacts/verify_extreme3.py` exhaustively checks normalized three-point supports in product groups \(\mathbb Z_m\times\mathbb Z_n\) across a broad small range. It verifies that every support passing the necessary repeated-difference test is of order-three, order-four, or Klein-four type; it then checks explicit flat witnesses for the order-three and order-four cases. The Klein-four exclusion is the exact three-equation contradiction proved above.

A replay from the packaged path reports

`VERIFY_OK triples=8176 multiplicity_candidates=169 good_C3_C4=133 V4_obstructions=36`

The finite replay is corroborative only; it is not used to infer the universal theorem.

## Relationship to prior work
Neuwirth determines the exact Sidon constant of every three-element subset of integer frequencies on the circle. His theorem concerns torsion-free integer frequency geometry; in particular, every three-element integer set has Sidon constant at most \(\sqrt2\), so it cannot exhibit the finite-torsion extremal value \(\sqrt3\).

Graham's work on extremal Sidon sets gives the general flatness criterion: an extreme measure has equal coefficient moduli and Fourier transform of constant modulus. It also records the useful necessary condition that every nonzero support difference must occur with multiplicity at least two. The present result closes the complete three-point case by classifying those repeated-difference patterns and proving that the remaining Klein-four candidate cannot satisfy the phase cancellation equations.

A published finite-cyclic theorem gives the exact Sidon constant of \(\{0,1,2\}\subset\widehat{\mathbb Z_N}\) for every even \(N\ge4\); its value reaches \(\sqrt3\) only at \(N=4\). That theorem is consistent with the order-four branch here but does not classify arbitrary three-point subsets of arbitrary abelian groups.

## Limitations
The theorem only classifies when a three-point set reaches the maximal possible Sidon constant. It does not compute the exact smaller constant in the nonextreme cases. The literature comparison did not locate a prior theorem stating this complete order-three/order-four classification, but older extremal-measure literature may encode the same small-support case implicitly.

## References
1. Stefan Neuwirth, *The Sidon constant of sets with three elements*, arXiv:math/0102145, first public version 2001-02-19; primary MSC 42A05.
2. Colin C. Graham, *A beastiary of sets having extremal Sidon constant, or, there must be more than one theorem somewhere here*, arXiv:1910.00924, first public version 2019-10-01.
3. *Exact Sidon constant of three consecutive characters on even cyclic groups*, public record `2026/10/4/SCOPE-exact-sidon-constant-of-three-consecutive-characters-on-even-cyc--b76331aa4281`.
