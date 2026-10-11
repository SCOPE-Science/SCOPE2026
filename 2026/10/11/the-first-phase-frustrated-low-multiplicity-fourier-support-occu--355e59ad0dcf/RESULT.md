# The first phase-frustrated low-multiplicity Fourier support occurs at six points

## Finding

Let \(A\subset\mathbb Z\) be finite, with no nontrivial three-term arithmetic progression, and suppose every integer has at most two representations as an unordered sum of two distinct elements of \(A\). Write \(m=|A|\), let \(R(A)\) be the number of sums with exactly two such representations, and set
\[
\mu_4(A)=\min_{|c_a|=1}\int_{\mathbb T}\left|\sum_{a\in A}c_a e^{2\pi iat}\right|^4\,dt .
\]
Then, for \(m\le5\),
\[
R(A)\le1,\qquad \mu_4(A)=2m^2-m-8R(A).
\]
The bound ceases to be universally attainable at \(m=6\). For
\[
A_*=\{0,1,3,4,9,10\},
\]
there are exactly three nontrivial pair-sum collisions and
\[
\mu_4(A_*)=54,
\]
whereas separate minimization of the three collision terms would give \(42\).

## Assumptions and scope

The torus \(\mathbb T=\mathbb R/\mathbb Z\) carries normalized Haar measure. The coefficients are phase-only: \(|c_a|=1\). A nontrivial three-term arithmetic progression means three distinct points \(x,y,z\in A\) with \(x+z=2y\). The pair-sum multiplicity hypothesis concerns unordered pairs of distinct elements only.

The result does not classify arbitrary six-point supports, supports containing three-term progressions, or supports with pair-sum multiplicity greater than two.

## Proof

Write \(A=\{a_1,\ldots,a_m\}\) and \(c_j=e^{i\theta_j}\). Parseval applied to the square of
\[
P(t)=\sum_{j=1}^m c_j e^{2\pi ia_jt}
\]
gives
\[
\|P\|_4^4=\sum_s\left|\sum_{a_i+a_j=s}c_ic_j\right|^2,
\]
where the inner sum is over ordered pairs.

Because \(A\) has no nontrivial three-term progression, a diagonal sum \(2a_i\) never coincides with an off-diagonal sum. Every unique unordered off-diagonal pair contributes \(4\), and a collision
\[
a_i+a_j=a_k+a_\ell
\]
between two distinct unordered pairs contributes
\[
|2c_ic_j+2c_kc_\ell|^2
=8+8\cos(\theta_i+\theta_j-\theta_k-\theta_\ell).
\]
Therefore
\[
\|P\|_4^4
=2m^2-m+8\sum_{r=1}^{R(A)}\cos\phi_r.
\]

For \(m\le5\), two distinct collision quadruples would have to share at least three points. Fix three ordered points \(a<b<c\). Any fourth point completing them to a collision must be one of
\[
a+b-c,\qquad a+c-b,\qquad b+c-a,
\]
whenever the indicated number has the required order position. Any two of these three completions, together with one of \(a,b,c\), form a nontrivial three-term arithmetic progression: the pairwise sums of the completions are respectively \(2a\), \(2b\), or \(2c\). Hence at most one collision is possible. With zero collisions the moment is fixed, and with one collision its phase can be chosen to equal \(\pi\), proving
\[
\mu_4(A)=2m^2-m-8R(A).
\]

For \(A_*=\{0,1,3,4,9,10\}\), the three collisions are
\[
0+4=1+3,\qquad 0+10=1+9,\qquad 3+10=4+9.
\]
Their phase differences \(\phi_1,\phi_2,\phi_3\) obey
\[
\phi_1-\phi_2+\phi_3\equiv0\pmod{2\pi},
\]
so all three cannot equal \(\pi\). Conversely this is the only relation among the three collision rows. Thus
\[
\mu_4(A_*)=66+8\min_{\alpha,\gamma\in\mathbb R}
\bigl(\cos\alpha+\cos(\alpha+\gamma)+\cos\gamma\bigr).
\]
Set \(x=(\alpha+\gamma)/2\) and \(y=(\alpha-\gamma)/2\). Then
\[
\cos\alpha+\cos\gamma+\cos(\alpha+\gamma)
=2\cos x\cos y+\cos(2x).
\]
For fixed \(x\), the minimum over \(y\) is
\[
\cos(2x)-2|\cos x|
=2\left(|\cos x|-\frac12\right)^2-\frac32.
\]
Hence the minimum is \(-3/2\), giving \(\mu_4(A_*)=66-12=54\). Taking
\[
(c_0,c_1,c_3,c_4,c_9,c_{10})=(\omega^2,1,\omega,1,1,1),
\qquad \omega=e^{2\pi i/3},
\]
produces collision phases \(2\pi/3,4\pi/3,2\pi/3\), so equality is attained.

## Verification

The accompanying verifier reconstructs all unordered pair sums of \(A_*\), confirms the three collision fibers and their unique integer dependency, checks the proposed coefficient phases, and independently evaluates the fourth moment from pair-sum convolution. It also checks the progression-free hypothesis and the normalization.

The computational checks are corroborative only. The cardinality-five bound and the exact value \(54\) are proved analytically above.

## Relationship to prior work

Neuwirth's treatment of metric unconditionality expands even Fourier moments as polynomials in additive relations and explicitly analyzes the one-relation \(L^4\) cases. That framework supplies the natural literature context for asking when several collision phases can or cannot be minimized simultaneously. The inspected paper does not state the five-point no-frustration threshold, the six-point obstruction above, or the exact value \(54\).

The \(B_2[g]\) literature studies bounded pair-sum representation multiplicity as an additive-combinatorial condition. The present statement uses the \(g=2\) low-multiplicity regime to isolate a phase interaction in a Fourier fourth moment rather than a density extremum.

## Limitations

The result is deliberately local to the first possible frustration threshold. It does not give a general formula for \(\mu_4(A)\) beyond six points, and the pair-sum multiplicity and progression-free assumptions are essential to the simple cosine decomposition used here. Older literature may contain equivalent finite-support calculations under unconditionality or merit-factor terminology; the targeted searches and inspected primary source did not reveal one.

## References

1. Stefan Neuwirth, *Metric unconditionality and Fourier analysis*, arXiv:math/9707211, first public version 1997-07-28.
2. Stefan Neuwirth, *The Sidon constant of sets with three elements*, arXiv:math/0102145, first public version 2001-02-19.
3. Melvyn B. Nathanson, *On the ubiquity of Sidon sets*, arXiv:math/0304496, first public version 2003-04-30.
