# A variation-a.e. Brownian-LIL criterion at the critical Hölder boundary

## Result

Let \(B\) be standard Brownian motion, let \(x\ge 0\), let \(\nu<1/2\), and let \(b:[0,\infty)\to\mathbb R\) be deterministic, continuous, locally of finite variation, with \(b(0)=0\). Consider the maximum-perturbed reflected equation
\[
W_t=(1-\nu)x+B_t+\nu M_t(W)+\frac12L_t^0(W-b),
\qquad W_t\ge b(t),
\]
where \(M_t(W)=\sup_{0\le s\le t}W_s\).

For \(\nu<1/2\), the orthant Skorokhod construction gives a unique canonical regulator solution
\[
W_t=(1-\nu)x+B_t+\nu M_t(W)+K_t,\qquad W_t\ge b(t),
\]
for every continuous boundary. A previously published boundary-charge theorem shows that this canonical regulator equals \(\frac12L^0(W-b)\) whenever the Stieltjes variation \(|db|\) gives zero mass to the contact set \(\{W=b\}\).

Define
\[
c_\nu=\max\{1,1-\nu\}
\]
and, for \(t>0\),
\[
\ell_b(t)=
\limsup_{h\downarrow0,\ h<t}
\frac{(b(t)-b(t-h))^+}
{\sqrt{2h\log\log(1/h)}}.
\]

### Theorem

If
\[
c_\nu\,\ell_b(t)<1
\]
for \(|db|\)-almost every \(t>0\), then the local-time equation has a unique strong solution.

In particular, every continuous locally finite-variation boundary that is locally \(1/2\)-Hölder is admissible for every \(\nu<1/2\).

Combined with Wang's increasing \(\alpha\)-Hölder counterexamples for every \(\alpha<1/2\), this closes the universal Hölder threshold at the critical exponent \(1/2\) in the subcritical perturbation regime.

## Proof

Let \(X=W-b\ge0\) for the canonical regulator solution and put \(F=M(W)-b\).

Fix a deterministic time \(t>0\). On the event \(X_t=0\), for all sufficiently small \(h>0\),
\[
B_t-B_{t-h}
\le c_\nu\,(b(t)-b(t-h))^+.
\]

Indeed,
\[
-X_{t-h}
=
B_t-B_{t-h}
+\nu\bigl(M_t-M_{t-h}\bigr)
+\bigl(K_t-K_{t-h}\bigr)
-\bigl(b(t)-b(t-h)\bigr).
\]
The left side is nonpositive and the regulator increment is nonnegative.

If \(F_t>0\), continuity gives a backward neighborhood on which the running maximum is constant, so the maximum increment vanishes. If \(F_t=0\), then \(M_t=b(t)\) and
\[
0\le M_t-M_{t-h}\le (b(t)-b(t-h))^+.
\]
For \(0\le\nu<1/2\) this yields the bound with \(c_\nu=1\); for \(\nu<0\) it yields the bound with \(c_\nu=1-\nu\).

For each fixed deterministic \(t>0\), the backward Brownian law of the iterated logarithm gives
\[
\limsup_{h\downarrow0}
\frac{B_t-B_{t-h}}
{\sqrt{2h\log\log(1/h)}}=1
\qquad\text{almost surely}.
\]
Therefore, if \(c_\nu\ell_b(t)<1\), the contact event \(X_t=0\) has probability zero.

On every compact interval, \(|db|\) is a deterministic finite measure. Fubini's theorem now gives
\[
\mathbb E\!\left[\int \mathbf1_{\{X_t=0\}}\,|db|(t)\right]
=
\int \mathbb P(X_t=0)\,|db|(t)=0,
\]
so the contact set has zero \(|db|\)-mass almost surely. The previously published boundary-charge criterion therefore identifies the regulator with half the local time, proving existence and pathwise uniqueness.

If \(b\) is locally \(1/2\)-Hölder, then
\[
(b(t)-b(t-h))^+\le C\sqrt h
\]
locally, hence \(\ell_b(t)=0\) for every \(t>0\). The endpoint corollary follows.

## Originality boundary

An earlier published result on the same model already established an exact regulator/local-time defect formula for \(\nu<1/2\), the corresponding zero-contact-charge criterion, and the fact that every locally absolutely continuous finite-variation boundary is admissible. Those statements are prior work and are not claimed here.

The contribution retained here is the variation-a.e. Brownian-LIL criterion above and its critical \(1/2\)-Hölder consequence. Wang's primary 2026 result assumes the stronger uniform condition that the upward boundary modulus is \(o(\sqrt h)\), and it constructs increasing \(\alpha\)-Hölder counterexamples for every \(\alpha<1/2\). The LIL argument closes the missing critical endpoint within the locally finite-variation class.

## Limitations

The result is restricted to \(\nu<1/2\), deterministic continuous locally finite-variation boundaries, and a strict LIL inequality. The equality case \(c_\nu\ell_b(t)=1\) is unresolved. No claim is made for arbitrary \(1/2\)-Hölder boundaries of infinite variation or for the regime \(\nu\ge1/2\).

## References

1. C. Wang, *Perturbed Brownian motion reflected at a time-dependent boundary*, arXiv:2609.20491v1 (2026).
2. *Boundary-charge criterion for subcritical perturbed Brownian reflection*, published 18 September 2026, https://github.com/Resultary/2026/blob/main/2026/9/18/SCOPE-subcritical-perturbed-brownian-boundary-charge--b83c5c0d9612/RESULT.md
3. R. J. Williams, *Semimartingale reflecting Brownian motions in the orthant*, in *Stochastic Networks* (1995).
