# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The central identity is exact. Under the uniform measure on the hypercube,
\[
\tau(a)=\mathbb E\left|\frac{\prod_i(1+a_i\varepsilon_i)-\prod_i(1-a_i\varepsilon_i)}2\right|.
\]
The bracket is precisely the odd Walsh part of the product. Removing its degree-one part leaves orthogonal Walsh monomials of odd degree at least three, so Parseval gives an exact squared remainder norm. Bounding elementary symmetric polynomials by \(q^k/k!\) yields the uniform \(O(q^{3/2})\) additive error. The denominator satisfies \(q(1-q/2)\le\Delta^2\le q\), which upgrades this to the stated \(O(q)\) relative-profile approximation. No probabilistic approximation is used in this first theorem.

For the subsequential theorem, sorted unit \(\ell_2\) coefficient vectors have coordinatewise subsequential limits. The standard triangular-array characteristic-function argument separates persistent Rademacher coordinates from an infinitesimal tail, whose missing variance becomes Gaussian. Uniform \(L_2\) boundedness gives convergence of first absolute moments. The sharp \(p=1\) Khintchine inequality supplies the lower endpoint \(1/\sqrt2\), Cauchy--Schwarz gives the upper endpoint 1, and every intermediate value is realized by a two-coordinate profile. The diffuse constant is the standard \(\mathbb E|N(0,1)|=\sqrt{2/\pi}\).

The Bernoulli-product corollary was checked separately. With the midpoint product measure, each signed one-coordinate contrast has mean zero and exact variance \(v_i/(2-v_i)\), where \(v_i=\lambda_i a_i^2\). The same odd-product orthogonality controls all nonlinear terms, while \(|c_i|\le a_i\) turns the displayed assumption into a Lindeberg condition. This yields \(d_{TV}(P,Q)\sim\sqrt{V/\pi}\). Applying the statement to the doubled product doubles \(V\), giving \(\sqrt{2V/\pi}\) and ratio \(\sqrt2\). The standalone artifact reproduces finite-dimensional identities and several asymptotic checks.

## Originality

Smirnov's arXiv:2609.19222v1 is the closest source. It defines the same mirror product distributions and proves \(\tau\asymp\Delta\) by an unspecified absolute constant. Its proof already invokes a Rademacher sum through the exponential parametrization, so neither the appearance of Khintchine's inequality nor the general idea of using Rademacher variables is claimed as new. The source does not give the weak-signal expansion, the normalized profile dependence, the Rademacher--Gaussian subsequential classification, the exact interval \([1/\sqrt2,1]\), or the diffuse constants.

Haagerup's sharp Khintchine theorem is prior art and supplies the classical \(1/\sqrt2\) constant. Triangular-array central limit theory and local asymptotic normality are also prior art. The originality claim is deliberately restricted to their specialization and synthesis for the newly introduced mirror-product subproblem, together with the explicit \((\lambda_i,a_i)\)-coordinate Bernoulli-product corollary.

Searches using combinations of “mirror product”, “Bernoulli product total variation”, “Rademacher”, “computational basis distinguishability”, “weak signal”, “Khintchine”, and “sqrt(2/pi)” did not locate an equivalent statement in the scientific literature inspected.

The main residual originality risk is explicit in Smirnov's paper itself: it states that the underlying quantum statement will be discussed elsewhere. No separate public paper or identifier for that announced treatment was located, so it cannot be checked. Older binary product-state discrimination work and generic local-asymptotic-normality literature are secondary risks, but the searched sources did not expose the displayed mirror-profile formulas. Accordingly originality is assessed only **to the best of our knowledge**.

## Value

The result sharpens a brand-new constant-factor theorem in a nontrivial way. It shows that there is no single weak-signal efficiency constant: sparse, balanced, and diffuse signals have different limiting losses, and all values from \(1/\sqrt2\) to 1 are possible. The profile compactification explains the transition continuously, while the diffuse corollary converts the recent efficiently computable comparison quantity into an exact first-order total-variation constant under a natural Lindeberg regime.

## Limitations

The \(2q\) theorem is local and does not prove a global optimal constant in Smirnov's Theorem 4.1. The complete profile classification applies to the mirror-product conditional problem; full non-diffuse Bernoulli products may have additional asymmetric one-coordinate structure. The direct product asymptotic requires \(V\to0\) and a Lindeberg-type maximum-coordinate condition. The announced future quantum treatment in the source is not publicly inspectable and remains a concrete originality uncertainty. Numerical checks support but do not replace the proofs.
