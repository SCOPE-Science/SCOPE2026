# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The source profile equation and leading tail were checked directly in arXiv:2609.20397v1. After the exact substitution

\[
f(\xi)=c_*\xi^{-\sigma/(p-1)}F(\log\xi),
\]

the profile equation reduces to Eq. (1) in `RESULT.md`. Its constant diffusion forcing is

\[
c_*^{m-1}mr(mr-N+2)e^{-qt}.
\]

The source paper's far-field center-manifold reduction has the two stable exponents

\[
q=\frac{L}{p-1},\qquad h=\frac{L}{m-p},
\]

and its independent-variable definitions imply exactly that the desingularized time differs from \(\log\xi\) only by an additive constant. Variation of constants in the normalized equation therefore gives the three claimed cases. The symbolic artifact independently rechecks all coefficient identities used in this derivation.

Adversarial checks included the cases \(m<2p-1\), \(m=2p-1\), \(m>2p-1\), and the cancellation surface \(mr=N-2\). The latter is not a removable algebraic accident: on that surface \(f_s=c_*\xi^{-r}\) is an exact profile on \(\xi>0\), because \(f_s^m\propto\xi^{2-N}\) is radial harmonic and the remaining terms cancel.

## Originality

**PASS, to the best of our knowledge.** The full HTML of arXiv:2609.20397v1 was inspected, including Theorem 1.1 and the far-field center-manifold reduction in Lemma 2.3. The paper proves only the leading limit

\[
\xi^{\sigma/(p-1)}f(\xi)\to c_*,
\]

and displays the two stable eigenvalues in its reduced system, but it does not state the comparison of those rates at \(m=2p-1\), a second-order tail formula, a far-field logarithmic correction, the universal coefficient, or the harmonic cancellation surface. Searches of the source text for `2p-1` returned no match; its mentions of logarithmic resonance concern a different classical critical-exponent problem in the complementary literature.

External searches were made for the exact source, `m=2p-1`, weighted-absorption second-order asymptotics, logarithmic tail corrections, and equivalent porous-medium/absorption formulations. No source-specific equivalent of the trichotomy or coefficient formulas was located. The 2025 Iagar--Munteanu paper treats the complementary range \(p>m\) and establishes leading tail classes, not the present \(1<p<m\) second-order resonance.

The most plausible older sources capable of containing related asymptotic information are McLeod--Peletier--Vázquez (1991), *Solutions of a nonlinear ODE appearing in the theory of diffusion with absorption*, and Kamin--Peletier--Vázquez (1992), *A nonlinear diffusion-absorption equation with unbounded data*. Their full texts were not inspected here. They concern the homogeneous-absorption setting \(\sigma=0\), for which the weighted forcing mechanism isolated here degenerates because \(r=0\), so they are a residual originality risk rather than concrete evidence of coverage. Galaktionov--Vázquez (1991) contains logarithmic corrections from a different critical-exponent resonance; general resonance phenomena are therefore explicitly excluded from the novelty claim.

Novelty is restricted to the source-specific second-order tail trichotomy, explicit coefficients, eventual-side consequence, and harmonic cancellation for the weighted \(1<p<m\) model.

## Value

**PASS.** The result converts the source's common leading tail into a sharp next-order classification. It identifies a previously unstated codimension-one resonance surface, supplies a universal correction and sign in one full parameter regime, distinguishes when profile memory survives at leading correction order, and exhibits a second exact surface where the diffusion forcing vanishes. These refinements are directly relevant to comparison and matched-asymptotic arguments for the associated large-time problem.

## Verification state

The symbolic checks were executed successfully. They are reproducibility evidence only and are not independent validation.
