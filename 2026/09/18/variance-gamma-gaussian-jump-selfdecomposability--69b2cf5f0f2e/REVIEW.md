# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.**

Two independent characterizations give the same threshold.

First, the Lévy density of the symmetric variance-gamma component is
\[
\beta e^{-|x|/b}|x|^{-1},
\]
while the Gaussian compound-Poisson component contributes
\[
\lambda\varphi_\sigma(x).
\]
Thus the positive-half-line canonical function is
\[
k(x)=\beta e^{-x/b}+\lambda x\varphi_\sigma(x).
\]
The classical one-dimensional class-\(L\) criterion reduces self-decomposability exactly to \(k'(x)\le0\). For \(x\ge\sigma\) this is automatic; on \(0<x<\sigma\), rescaling \(x=\sigma y\) yields the displayed minimization problem.

The logarithmic derivative of the threshold integrand is
\[
-r+\frac{y(3-y^2)}{1-y^2}.
\]
The latter rational function is strictly increasing because
\[
\frac{d}{dy}\frac{y(3-y^2)}{1-y^2}
=
\frac{y^4+3}{(1-y^2)^2}>0.
\]
This proves uniqueness of \(y_r\) and the exact critical activity, including equality at the boundary.

Second, the Wang-Yin background-driving criterion applies because the characteristic function is positive and
\[
t\Psi'(t)\to0 \text{ at }0,\qquad
t\Psi'(t)\to2\beta \text{ at infinity}.
\]
Its candidate characteristic function has inverse Fourier density
\[
j_{\lambda,\sigma}(x)
=
\frac{e^{-|x|/b}}{2b}
-\frac{\lambda}{2\beta}
\left(1-\frac{x^2}{\sigma^2}\right)\varphi_\sigma(x).
\]
The condition \(j_{\lambda,\sigma}\ge0\) is exactly the same threshold inequality. This independently verifies both the boundary and the background-driving jump law.

For the scale optimization, the envelope derivative is
\[
d(\log G)/dr=1/r-y_r.
\]
Combining the stationary condition with the saddle equation gives
\[
y^4-4y^2+1=0,
\]
hence \(y^2=2-\sqrt3\) and \(r_*=\sqrt{2+\sqrt3}\). Substitution gives the stated maximal activity. The small- and large-scale expansions were checked by direct asymptotic inversion of the saddle equation.

The weak-perturbation statement follows because the compound-Poisson Gaussian perturbation converges to zero in probability as \(\sigma\downarrow0\), while the exact critical rate is asymptotic to \(\beta\sqrt{2\pi}\sigma/b\).

No unsupported implication from self-decomposability to stochastic ordering, tail ordering, or option values is asserted.

## Originality

**PASS, to the best of our knowledge.**

The search included the classical canonical-density criterion for self-decomposability, recent characteristic-function criteria, known self-decomposability results for variance-gamma/generalized gamma convolution families, parameter-threshold results in other infinitely divisible families, convolution-factor literature for class \(L\), and applied variance-gamma models augmented by compound-Poisson jumps.

The recent Wang-Yin work develops a characteristic-function test and background-driving representation, but does not state the Gaussian compound-Poisson perturbation threshold derived here. Buchmann-Lu-Madan establishes self-decomposability for broad weak variance generalized gamma convolution constructions, but the inspected metadata and summaries did not identify this independent finite-activity Gaussian-jump phase diagram. Pakes demonstrates that exact parameter thresholds for self-decomposability are a known phenomenon in other families, so no novelty is claimed for the general idea of a threshold.

Ivanov-Ano provides a directly relevant modeling precedent combining variance-gamma dynamics with additional compound-Poisson shocks. The searchable text inspected did not contain a self-decomposability analysis. Iksanov-Jurek-Schreiber studies factorization properties of self-decomposable measures, but no matching Gaussian-jump threshold was located.

Targeted searches combined the terms `variance gamma`, `generalized Laplace`, `self-decomposable`, `compound Poisson`, `Gaussian jumps`, `normal jumps`, `class L`, `convolution factor`, `background driving`, and `perturbation`. No source was located that states the exact threshold
\[
\lambda_c(\beta,b,\sigma),
\]
the unique Goldilocks scale
\[
\sigma/b=\sqrt{2+\sqrt3},
\]
the maximal activity, the narrow-jump weak-perturbation fragility, or the explicit background-driving density as one result.

The general identity
\[
k_\lambda'=k_0'+\lambda(xg(x))'
\]
is an immediate consequence of the classical canonical-density criterion and is explicitly **not** claimed as a new general theorem.

No inaccessible paper was identified whose title or abstract specifically signals the same variance-gamma plus Gaussian compound-Poisson self-decomposability problem. The principal residual originality risk is older class-\(L\), convolution-factor, or parametric infinitely divisible literature under different terminology, where an equivalent special case could have appeared without the modern variance-gamma naming.

## Value

**PASS.**

The result gives a complete phase diagram inside a natural family that is infinitely divisible for every parameter value: it identifies exactly when the stronger self-decomposability property survives a finite-activity perturbation.

The phase diagram is structurally informative. Self-decomposability survives neither arbitrarily narrow nor arbitrarily broad Gaussian shocks at fixed positive activity; there is a unique optimal scale and a finite maximal activity. The weak-perturbation corollary gives an explicit mechanism showing that class \(L\) can fail under perturbations whose variance vanishes and whose laws converge weakly to a point mass.

The explicit background-driving jump density adds a constructive probabilistic interpretation rather than only a monotonicity certificate.

## Sources inspected

- Wang and Yin, “Self-decomposability of α-Cauchy distributions”, arXiv:2609.18536 (2026), including the characteristic-function/background-driving criterion.
- Sato, *Lévy Processes and Infinitely Divisible Distributions*, for the classical one-dimensional self-decomposability criterion.
- Pakes, “On generalized stable and related laws”, JMAA 411 (2014), for parameter-threshold and \(k\)-function methods.
- Buchmann, Lu and Madan, “Self-decomposability of weak variance generalised gamma convolutions”, SPA 130 (2020).
- Fischer, Gaunt and Sarantsev, “The Variance-Gamma Distribution: A Review”, Statistical Science 39 (2024).
- Ivanov and Ano, “Option pricing in time-changed Lévy models with compound Poisson jumps”, VMSTA 6 (2019).
- Iksanov, Jurek and Schreiber, “A new factorization property of selfdecomposable probability measures”, Annals of Probability 32 (2004).

## Scientific limitations retained

The result is one-dimensional and symmetric and treats centered Gaussian compound-Poisson jumps. It does not classify multivariate perturbations or arbitrary jump densities beyond the direct canonical derivative criterion, and it makes no stochastic-order or pricing claim. The older class-\(L\) literature creates a residual originality risk despite the targeted search.
