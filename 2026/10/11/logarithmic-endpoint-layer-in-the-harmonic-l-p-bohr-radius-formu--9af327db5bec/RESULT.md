# Logarithmic endpoint layer in the harmonic \(L^p\) Bohr-radius formula

## Finding

Let
\[
1\le p\le\infty
\]
and let
\[
q
\]
be its conjugate exponent. Define
\[
C_q
=
\left(
\frac{1}{2\pi}
\int_0^{2\pi}
|\cos t|^q\,dt
\right)^{1/q}
\]
for finite
\[
q,
\]
with
\[
C_\infty=1.
\]

The recent harmonic \(L^p\)-boundary theorem gives the Bohr-radius expression
\[
r_p=\frac{1}{1+2C_q}.
\]
For
\[
1<p<\infty,
\]
the cosine moment has the exact beta-integral form
\[
C_q
=
\left[
\frac{\Gamma((q+1)/2)}
{\sqrt{\pi}\,\Gamma((q+2)/2)}
\right]^{1/q}.
\]

Consequently,
\[
p\longmapsto r_p
\]
is real-analytic and strictly increasing on
\[
(1,\infty).
\]
It extends continuously to
\[
[1,\infty]
\]
with the exact values
\[
r_1=\frac13,
\qquad
r_2=\sqrt2-1,
\qquad
r_\infty=\frac{\pi}{\pi+4}.
\]

The lower endpoint is singular. As
\[
p\downarrow1,
\]
\[
r_p
=
\frac13
+
\frac{p-1}{9}
\left(
\log\frac1{p-1}
+
\log\frac{\pi}{2}
\right)
+
o(p-1).
\]
Equivalently, as
\[
q\to\infty,
\]
\[
r_p
=
\frac13
+
\frac{\log q+\log(\pi/2)}{9q}
+
O\!\left(
\frac{(\log q)^2}{q^2}
\right).
\]

At the opposite endpoint,
\[
p\to\infty,
\]
the convergence is regular:
\[
r_p
=
\frac{\pi}{\pi+4}
-
\frac{
4\pi(\log\pi-1)
}{
(\pi+4)^2
}
\frac1{p-1}
+
O\!\left(
\frac1{(p-1)^2}
\right).
\]

Thus the full exponent dependence is monotone but strongly asymmetric: near
\[
p=1
\]
the first improvement above the radius
\[
1/3
\]
has the larger scale
\[
(p-1)\log\frac1{p-1},
\]
whereas the approach to the
\[
p=\infty
\]
radius is inverse-linear.

## Assumptions and scope

The radius analyzed here is the quantity
\[
r_p=\frac{1}{1+2C_q}
\]
appearing in Theorem 2.2 of the cited 2026 preprint on harmonic mappings induced by
\[
L^p(\mathbb T)
\]
boundary data.

The theorem there defines
\[
C_q
=
\left(
\frac{1}{2\pi}
\int_0^{2\pi}
|\cos(nt)|^q\,dt
\right)^{1/q}.
\]
The value is independent of the positive integer
\[
n
\]
by periodicity, so the present analysis uses
\[
n=1.
\]

The result is an exact parameter analysis of the published radius formula. It does not add a new claim about extremizers for the underlying coefficient inequality, nor does it re-prove the source theorem's global sharpness assertion.

## Proof

For
\[
1\le q<\infty,
\]
periodicity and symmetry give
\[
\frac1{2\pi}
\int_0^{2\pi}
|\cos t|^q\,dt
=
\frac2\pi
\int_0^{\pi/2}
\cos^q t\,dt.
\]
The beta integral yields
\[
\int_0^{\pi/2}
\cos^q t\,dt
=
\frac{\sqrt\pi}{2}
\frac{
\Gamma((q+1)/2)
}{
\Gamma((q+2)/2)
},
\]
hence
\[
C_q
=
\left[
\frac{\Gamma((q+1)/2)}
{\sqrt\pi\,\Gamma((q+2)/2)}
\right]^{1/q}.
\]

Now regard
\[
|\cos t|
\]
as a nonconstant random variable on the normalized circle. Its
\[
L^q
\]
norm is strictly increasing in
\[
q.
\]
Therefore
\[
C_q
\]
is strictly increasing in
\[
q.
\]
Since
\[
q=\frac{p}{p-1}
\]
is strictly decreasing in
\[
p,
\]
the composition
\[
r_p=\frac{1}{1+2C_q}
\]
is strictly increasing in
\[
p.
\]
The gamma quotient proves real analyticity for finite interior exponents.

The endpoint values are immediate:
\[
C_\infty=1
\]
gives
\[
r_1=\frac13,
\]
while
\[
C_1=\frac2\pi
\]
gives
\[
r_\infty=\frac{\pi}{\pi+4}.
\]
Also
\[
C_2=\frac1{\sqrt2},
\]
so
\[
r_2=\frac1{1+\sqrt2}=\sqrt2-1.
\]

For the lower endpoint, put
\[
q\to\infty.
\]
The standard gamma-ratio expansion gives
\[
\frac{
\Gamma((q+1)/2)
}{
\sqrt\pi\,\Gamma((q+2)/2)
}
=
\sqrt{\frac{2}{\pi q}}
\left(
1+O\!\left(\frac1q\right)
\right).
\]
Taking the
\[
q
\]
th root,
\[
\log C_q
=
-\frac{
\log q+\log(\pi/2)
}{
2q
}
+
O\!\left(\frac1{q^2}\right).
\]
Therefore
\[
C_q
=
1
-
\frac{
\log q+\log(\pi/2)
}{
2q
}
+
O\!\left(
\frac{(\log q)^2}{q^2}
\right).
\]
Substitution into
\[
r_p=\frac1{1+2C_q}
\]
gives
\[
r_p
=
\frac13
+
\frac{
\log q+\log(\pi/2)
}{
9q
}
+
O\!\left(
\frac{(\log q)^2}{q^2}
\right).
\]

Since
\[
q=\frac{p}{p-1},
\]
we have
\[
\frac1q
=
p-1+O((p-1)^2)
\]
and
\[
\log q
=
\log\frac1{p-1}+O(p-1).
\]
This yields
\[
r_p
=
\frac13
+
\frac{p-1}{9}
\left(
\log\frac1{p-1}
+
\log\frac{\pi}{2}
\right)
+
o(p-1).
\]

For the upper endpoint, write
\[
q=1+\delta,
\qquad
\delta=\frac1{p-1}.
\]
Let
\[
L(q)
=
\log
\frac{
\Gamma((q+1)/2)
}{
\sqrt\pi\,\Gamma((q+2)/2)
},
\qquad
G(q)=\frac{L(q)}q=\log C_q.
\]
At
\[
q=1,
\]
\[
L(1)=\log\frac2\pi.
\]
Using
\[
\psi(1)=-\gamma
\]
and
\[
\psi(3/2)=-\gamma-2\log2+2,
\]
we obtain
\[
L'(1)=\log2-1
\]
and hence
\[
G'(1)
=
L'(1)-L(1)
=
\log\pi-1.
\]
Thus
\[
C_q
=
\frac2\pi
\left[
1+(\log\pi-1)\delta+O(\delta^2)
\right].
\]
Expanding
\[
(1+2C_q)^{-1}
\]
gives
\[
r_p
=
\frac{\pi}{\pi+4}
-
\frac{
4\pi(\log\pi-1)
}{
(\pi+4)^2
}
\delta
+
O(\delta^2),
\]
which is the stated
\[
p\to\infty
\]
formula.

## Verification

The beta-integral formula was checked directly against the source's normalized cosine moment.

Strict monotonicity does not rely on differentiating special functions: it follows from the strict monotonicity of
\[
L^q
\]
norms on a probability space for a nonconstant function. This also verifies the direction of the parameter dependence independently of the gamma representation.

The special value
\[
p=2
\]
was checked from
\[
(2\pi)^{-1}\int_0^{2\pi}\cos^2t\,dt=\frac12.
\]

For the endpoint expansions, the only non-elementary inputs are the standard first gamma-ratio asymptotic and the digamma values at
\[
1
\]
and
\[
3/2.
\]
The resulting constants were independently checked against numerical evaluations of the exact gamma formula, but those numerical checks are not used as proof.

## Relationship to prior work

Ahamed and Hossain give
\[
r_p=\frac1{1+2C_q}
\]
as the \(L^p\)-dependent Bohr-radius formula and explicitly record the endpoint coefficient constants
\[
C_\infty=1
\]
and
\[
C_1=2/\pi.
\]
Their paper asks how the \(L^p\) nature of the boundary data influences the Bohr radius, but the inspected text does not give the gamma-function closed form, prove strict monotonicity in
\[
p,
\]
or derive endpoint asymptotics.

Shi, Li, and Lian establish the sharp harmonic Hardy coefficient estimate from which the same cosine
\[
L^q
\]
constant arises. That coefficient theorem supplies the analytic background for the radius formula but does not state the Bohr-radius exponent phase derived here.

A later 2026 paper on sharp constant problems for harmonic mappings studies extremizers and Hardy-space constants closely related to the same cosine moment. Its publicly accessible abstract does not state this Bohr-radius monotonicity or either endpoint expansion; full-text comparison was unavailable in the present source access, so this remains a residual literature risk.

## Limitations

The theorem analyzes the radius expression stated in the cited Bohr theorem. It deliberately does not re-assess the separate sharpness argument of that source.

The expansion at
\[
p=1
\]
is first-order on the natural logarithmic scale. Higher terms can be obtained from a longer Stirling expansion.

The expansion at
\[
p=\infty
\]
is displayed through first order in
\[
1/(p-1).
\]
No convexity or complete-monotonicity property of
\[
p\mapsto r_p
\]
is claimed.

## References

1. M. B. Ahamed and R. Hossain, *Bohr Radius and Landau-type Theorems for Harmonic Mappings with Boundary Functions in Lebesgue Spaces*, arXiv:2604.14217v1, first posted 12 April 2026.
2. Q. Shi, X. Li, and X. Lian, *Estimates on the Schwarz Lemma and Landau Theorem for a Harmonic Mapping with a Given Boundary Function in Lebesgue Space*, Computational Methods and Function Theory (2026), DOI: 10.1007/s40315-025-00600-8.
3. S. Chen, M. Huang, L. Jin, and Q. Li, *Sharp constant problems for harmonic mappings*, arXiv:2609.33159v1, first posted 27 September 2026.
