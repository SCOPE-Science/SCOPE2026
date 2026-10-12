# A one-transition curvature law for Pfaffian rank degrees
## Finding
Let
\[
Y_{n,r}
=
\{[A]\in\mathbb P(\bigwedge^2\mathbb C^n):\operatorname{rank}(A)\le 2r\}.
\]
Put
\[
s=n-2r-1.
\]
Thus \(s\equiv n-1\pmod2\). For a proper nonzero Pfaffian rank locus, \(s\ge1\) when \(n\) is even and \(s\ge2\) when \(n\) is odd. Write
\[
D_{n,s}=\deg(Y_{n,r}).
\]
For the full ambient-space endpoint, set
\[
D_{n,-1}=1
\]
when \(n\) is even and
\[
D_{n,0}=1
\]
when \(n\) is odd.

For every admissible interior value of \(s\), namely one for which \(s-2\) and \(s+2\) are also in this extended rank tower,
\[
\boxed{
\frac{D_{n,s+2}D_{n,s-2}}{D_{n,s}^2}
=
\frac{(n^2-s^2)(n^2-(s+1)^2)}
{16(2s-1)(2s+1)^2(2s+3)}
}.
\]

Define
\[
Q_n(s)
=
(n^2-s^2)(n^2-(s+1)^2)
-
16(2s-1)(2s+1)^2(2s+3).
\]
Then
\[
\boxed{
Q_n(s+2)-Q_n(s)
=
-4(2s+3)\bigl(n^2+255s^2+765s+701\bigr)<0
}.
\]
Hence, as corank increases through the admissible parity class, the degree sequence can change logarithmic curvature at most once: it can pass from log-convex to log-concave, but it can never return.

Moreover, if \(n\to\infty\) through any parity-compatible sequence and
\[
\frac{s}{n}\longrightarrow\theta\in(0,1),
\]
then
\[
\frac{D_{n,s+2}D_{n,s-2}}{D_{n,s}^2}
\longrightarrow
\frac{(1-\theta^2)^2}{256\theta^4}.
\]
Therefore the sharp bulk phase boundary is
\[
\boxed{\theta=\frac1{\sqrt{17}}}.
\]
For \(\theta<1/\sqrt{17}\) the Pfaffian rank degrees are eventually strictly log-convex at that bulk corank, while for \(\theta>1/\sqrt{17}\) they are eventually strictly log-concave.

## Assumptions and scope
The base field is \(\mathbb C\). The ambient projective space is
\[
\mathbb P(\bigwedge^2\mathbb C^n),
\]
whose points are nonzero skew-symmetric \(n\times n\) matrices modulo scalar.

Only the natural rank stratification is considered. Since skew-symmetric ranks are even, adjacent nontrivial rank levels differ by two; equivalently the parameter \(s=n-2r-1\) changes by two.

The ambient-space endpoint is adjoined only to make the first curvature comparison uniform. It has degree \(1\).

## Proof
The classical multiplicity formula for a Pfaffian ring gives, in projective-geometric language,
\[
D_{n,s}
=
\prod_{1\le i\le j\le s}
\frac{n-s-1+i+j}{i+j}
\]
for \(s\ge1\). The empty product gives \(D_{n,0}=1\), while \(D_{n,-1}=1\) is the full even-dimensional ambient endpoint.

Group the factors by \(j\):
\[
D_{n,s}
=
\prod_{j=1}^{s}
\frac{(n-s+2j-1)!}{(n-s+j-1)!}
\frac{j!}{(2j)!}.
\]
Comparing the formulas for \(s\) and \(s-2\), cancelling the common factorial factors, and simplifying gives
\[
\frac{D_{n,s}}{D_{n,s-2}}
=
\frac{\prod_{k=-(s-1)}^{s-1}(n+k)}
{(2s)!\,C_{s-1}},
\]
where
\[
C_m=\frac1{m+1}\binom{2m}{m}
\]
is the \(m\)-th Catalan number. The same identity holds at the first admissible value \(s=1\) or \(s=2\) with the ambient endpoint convention above.

Let
\[
R_{n,s}=\frac{D_{n,s}}{D_{n,s-2}}.
\]
Then
\[
\frac{D_{n,s+2}D_{n,s-2}}{D_{n,s}^2}
=
\frac{R_{n,s+2}}{R_{n,s}}.
\]
The numerator product in \(R_{n,s+2}\) contributes four new factors,
\[
(n-s)(n+s)(n-s-1)(n+s+1)
=
(n^2-s^2)(n^2-(s+1)^2).
\]
The denominator ratio is
\[
\frac{(2s+4)!\,C_{s+1}}{(2s)!\,C_{s-1}}
=
16(2s-1)(2s+1)^2(2s+3).
\]
This proves the exact curvature formula.

The sign of logarithmic curvature is the sign of \(Q_n(s)\). Direct expansion and subtraction at spacing two give
\[
Q_n(s+2)-Q_n(s)
=
-4(2s+3)\bigl(n^2+255s^2+765s+701\bigr).
\]
Every factor except the leading minus sign is positive for the admissible \(n,s\). Therefore \(Q_n(s)\) is strictly decreasing along the parity-compatible rank tower. It follows that there is at most one sign change, necessarily from positive to negative. Positive \(Q_n(s)\) is equivalent to
\[
D_{n,s}^2<D_{n,s-2}D_{n,s+2},
\]
and negative \(Q_n(s)\) is equivalent to the reverse strict inequality.

Finally, if \(s/n\to\theta\in(0,1)\), divide numerator and denominator of the exact curvature ratio by \(n^4\). The limit is
\[
\frac{(1-\theta^2)^2}{256\theta^4}.
\]
Since \(0<\theta<1\), this is greater than \(1\) exactly when
\[
1-\theta^2>16\theta^2,
\]
equivalently
\[
\theta<\frac1{\sqrt{17}}.
\]
The opposite strict inequality holds when \(\theta>1/\sqrt{17}\).

## Verification
The bundled checker independently evaluates the Pfaffian degree product using exact rational arithmetic for every
\[
4\le n\le120
\]
and every admissible rank level.

It verifies the adjacent-ratio identity, the exact curvature formula, the strict two-step decrease of \(Q_n(s)\), and the asserted relation between the sign of \(Q_n(s)\) and log-convexity or log-concavity. It also checks the endpoint conventions against the Pfaffian hypersurface and the full ambient space.

These finite checks are regression evidence only. The theorem for all \(n\) is proved symbolically above.

## Relationship to prior work
Ghorpade and Krattenthaler give the closed multiplicity formula for Pfaffian rings and explain its projective-degree interpretation through skew-symmetric degeneracy loci. That product formula is the numerical input here.

Raicu studies the rank stratifications of general, symmetric, and skew-symmetric matrix spaces from algebraic geometry and \(\mathcal D\)-module theory; the paper is classified primarily under algebraic-geometry MSC codes including \(14\mathrm F10\) and \(14\mathrm M12\).

The closest located degree-curvature results concern generic square determinantal varieties and symmetric determinantal varieties. They exhibit related rank-profile transitions and the same asymptotic constant \(1/\sqrt{17}\), but neither statement covers skew-symmetric rank loci. The Pfaffian degree product has a different parity-restricted rank parameter and yields the exact rational curvature formula displayed above.

Targeted literature searches for Pfaffian or skew-symmetric determinantal degree log-concavity, log-convexity, adjacent ratios, curvature, and the constant \(1/\sqrt{17}\) did not locate an equivalent published statement.

## Limitations
The result concerns projective degrees of the standard skew-symmetric rank loci only. It does not address arbitrary skew-symmetric matrix Schubert varieties.

At the exact critical scale \(s/n\to1/\sqrt{17}\), the bulk limit equals \(1\); the theorem does not assert a universal second-order sign there.

The originality search cannot rule out an unindexed arithmetic observation obtained previously from the same classical Pfaffian degree product.

## References
Sudhir R. Ghorpade and Christian Krattenthaler, *The Hilbert Series of Pfaffian Rings*, arXiv:math/0105151, first submitted 17 May 2001; in *Algebra, Arithmetic and Geometry with Applications*, Springer, 2004, 337--356.

Claudiu Raicu, *Characters of equivariant \(\mathcal D\)-modules on spaces of matrices*, arXiv:1507.06621, first submitted 23 July 2015; *Compositio Mathematica* 152 (2016), 1935--1965, DOI 10.1112/S0010437X16007521.
