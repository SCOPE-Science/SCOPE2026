# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The proof was checked at each of its three nontrivial bridges.

First, the cap self-convolution computation is valid for every real
\(\lambda>0\), exactly the range in which the Gegenbauer product formula has
the integrable density \((1-u^2)^{\lambda-1}\). With normalized Gegenbauer
weight
\[
dm_\lambda(y)
=
\frac{\Gamma(\lambda+1)}
{\sqrt\pi\,\Gamma(\lambda+\frac12)}
(1-y^2)^{\lambda-\frac12}\,dy,
\]
the product-formula normalization is
\[
\kappa_\lambda
=
\frac{\Gamma(\lambda+\frac12)}
{\sqrt\pi\,\Gamma(\lambda)}.
\]
After changing from the product-formula variable to the second cap
coordinate, the factor involving \(1-y^2\) cancels. The linear change
\[
y=\cos(r/2)p+\sin(r/2)q,\qquad
z=\cos(r/2)p-\sin(r/2)q
\]
has Jacobian \(\sin r\) and transforms
\[
1-\cos^2r-y^2-z^2+2(\cos r)yz
\]
to
\[
\sin^2r(1-p^2-q^2).
\]
All powers of \(\sin r\) therefore cancel. The remaining polar integral
gives
\[
(\chi_\beta *_\lambda\chi_\beta)(\cos r)
=
\frac{\cos^{2\lambda}\beta}{\pi}
\int_{r/2}^{\beta}
(\tan^2\beta-\tan^2u)^\lambda\,du.
\]
The constant is exact because
\(a_\lambda\kappa_\lambda/\lambda=1/\pi\).
For ordinary sphere parameters this agrees with the normalized
spherical-cap intersection formula.

Second, strictness under mixing was checked rather than inferred merely from
nonnegativity. The cap self-convolution has \(n\)-th transform equal to the
square of the cap transform. For \(n>0\), the latter is proportional to
\[
(\sin\beta)^{2\lambda+1}C_{n-1}^{\lambda+1}(\cos\beta),
\]
so for fixed \(n\) it has only finitely many zeros in
\((0,\pi/2)\); the \(n=0\) coefficient is positive. Lu defines a positive
mixture using a measure that charges every nonempty open subset of its
parameter domain. Consequently, integrating the nonnegative squared cap
coefficient against any of the mixture measures used in the proof gives a
strictly positive result.

For \(0<\beta<\pi/2\), Lu's Lemma 3.3(iii) converts
\((\beta^2-u^2)_+^\lambda\) into a full-support mixture of
\((\tan^2s-\tan^2u)_+^\lambda\), and Lemma 3.4 with parameter \(1/2\)
converts \((\beta-u)_+^\lambda\) into a full-support mixture of
\((s^2-u^2)_+^\lambda\). Tonelli therefore transfers strict coefficient
positivity first to
\[
E_{\lambda,\beta}(r)
=
\int_{r/2}^\infty(\beta^2-u^2)_+^\lambda\,du
\]
and then to
\[
P_{\lambda,\beta}(r)
=
\frac1{\lambda+1}(\beta-r/2)_+^{\lambda+1}.
\]

The endpoint \(\beta=\pi/2\) was checked separately. Lu's Lemma 3.3(iv)
makes \((\pi/2-\arctan\sqrt{x})^\lambda\) a nonconstant completely monotone
function; the same paper's Laplace-mixture step represents it as a
full-support positive mixture of \((t-x)_+^\lambda\). The substitutions
\(x=\tan^2u\), \(t=\tan^2s\) therefore express
\(P_{\lambda,\pi/2}\) directly as a positive mixture of cap
self-convolutions with \(s<\pi/2\). This avoids relying on a limit that could
in principle lose strict positivity.

Third, the identification with the target integral has only positive
normalization factors. With \(t=2\beta\),
\(P_{\lambda,\beta}\) is a positive scalar multiple of
\((t-r)_+^{\lambda+1}\), so its \(n\)-th Gegenbauer transform has the sign of
\(F_n^{\lambda,\lambda+1}(t)\). For
\(\delta>\lambda+1\), the displayed beta-kernel identity expresses
\(F_n^{\lambda,\delta}\) as a positive fractional integral of the boundary
case, preserving strict positivity.

The cases \(n=0\), \(r=0\), \(t=\pi\), and arbitrarily small
\(\lambda>0\) were checked explicitly. No integer-dimensional step is used
in the cap identity.

## Originality — PASS, to the best of our knowledge

The direct source, Beatson--zu Castell--Xu (2014), states Conjecture 1.4 for
every real \(\lambda>0\) and explicitly remarks that this is greater
generality than needed for the sphere application. The conjectured
sufficiency boundary is \(\delta=\lambda+1\).

The most relevant later primary sources were compared at theorem-statement
level.

- Xu (2018) proves a Jacobi integral theorem for
  \(\alpha,\beta\in\mathbb N_0\). Its Gegenbauer specialization therefore
  gives a discrete parameter family, not arbitrary real \(\lambda>0\).
- Beatson--zu Castell (2017) develops the Gegenbauer convolution
  \(*_\lambda\) for arbitrary \(\lambda>0\), proves transform
  multiplicativity, and gives the cap coefficient antiderivative used here.
  It does not state the all-real Pólya boundary theorem.
- Lu (2025) proves the truncated-power result on ordinary spheres in every
  integer dimension and develops the positive-mixture lemmas used here.
  The spectral Gegenbauer parameter in the spherical theorem is tied to an
  integer dimension. The paper does not state positivity for an arbitrary
  real Gegenbauer spectral parameter.

Targeted searches through the current literature used the exact conjecture,
the integral \(F_n^{\lambda,\delta}\), Gegenbauer/Pólya terminology,
truncated powers, positive definite spheres, and continuous real
Gegenbauer-parameter formulations. No source was located that states the
continuous-\(\lambda\) conclusion proved here.

There is a nomenclature ambiguity worth recording: later papers sometimes
say that “the conjecture” of Beatson--zu Castell--Xu was proved, referring to
the sphere-relevant discrete parameter cases. Because the 2014 source
literally states a broader all-real-\(\lambda\) conjecture, the present
originality claim is deliberately restricted to that continuous-parameter
extension and not to the already solved spherical cases.

A residual risk remains that the same extension appears under hypergroup or
special-function terminology not captured by the searches.

Repository searches for Gegenbauer, Pólya, truncated-power, hypergroup, and
all-real-\(\lambda\) formulations found no overlapping SCOPE record.

## Value — PASS

The result closes the sufficiency half of a literal parameter range that the
original source explicitly identified as broader than its geometric need.
It also isolates a reusable mechanism: the ordinary spherical-cap
self-convolution formula extends exactly, with normalized constant \(1/\pi\),
to the continuous Gegenbauer hypergroup. This converts discrete
dimension-dependent positivity arguments into analytic statements for every
real \(\lambda>0\).

The cap identity can be useful independently whenever positivity of
Gegenbauer coefficients is established through self-convolution and then
transported by completely monotone or positive-mixture representations.

## Limitations

- The necessity direction for \(\delta<\lambda+1\) is not established.
- The result concerns the continuous Gegenbauer parameter itself; it does
  not add new integer-dimensional sphere cases beyond the later literature.
- The positive-mixture lemmas are taken from Lu (2025), including their
  complete-monotonicity proofs.
- A differently formulated or poorly indexed continuous-parameter result
  may exist.
- Independent audit has not been performed.
