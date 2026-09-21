# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** Direct differentiation gives
\(\dot R=2\gamma R+8xyz\) and
\(\dot W=2\gamma R-8\alpha z\). The sign decomposition uses the exact multiplicative formula for \(z(t)\) and stationarity of the Lie derivative on compactly supported invariant measures. The conditional identity is justified with cutoffs away from \(z=0\); compact support gives domination. The logarithmic radial identity is likewise justified by first proving that the positive invariant component has zero mass on \(R=0\) and using \(|xy|/R\le1/2\). The square-defect and mean-height formulas then follow algebraically.

The equality case was checked adversarially. Vanishing defect forces \(y=-x\) almost surely on a full-measure invariant set. Tangency gives \(z=x^2-1\), and consistency reduces \(q=x^2\) to the finite root set of \(3q^2-(\alpha+\gamma+3)q+\alpha\). Continuity makes \(q\) constant; the remaining equations force \(q=\alpha=1+\gamma/2\) and yield exactly the two equilibria stated. The converse is immediate. Symbolic residual checks are supplied in the compact verification artifact.

Potential hidden-hypothesis checks included the invariant plane \(z=0\), the positive \(z\)-axis, mixtures with the origin, the possibility that equality might support a nonstationary orbit, and the distinction between a stationary conditional expectation and a pointwise trajectory identity.

## Originality

**PASS, to the best of our knowledge.** The 1979 primary paper was inspected at the relevant theorem/equation level: it already contains the conservative energy integral, the invariant plane \(z=0\), and numerical study of limit cycles and complex motion, so none of those are claimed as new. Tsegel'nik's 2016 conference abstract was also checked at theorem level; its Theorem 3 gives the special nonautonomous first integral \(x^2+y^2+4z=C e^{2at}\) when the conventional parameters satisfy \(a=-b\), which is the closest analytical predecessor and is explicitly excluded from the novelty claim.

The 2016/2017 hidden-attractor papers, the 2019 bifurcation study, the 2022 generalized-model paper, and a 2026 statistical parameter-space study were checked through accessible abstracts/full text where available. Their stated methods and results focus on numerical dynamics, bifurcation structure, generalized equations, hidden attractors, or statistical diagnostics. Targeted searches for invariant-measure, time-average, conditional-height, mean-height, and the exact algebraic forms in this record did not locate an equivalent theorem.

Residual risk remains because the Rabinovich–Fabrikant literature spans older Russian-language and application literature, and not every cited paper was exhaustively checked line by line. The elementary nature of some global-average identities also means independent rediscovery is plausible. The originality claim is therefore limited to the combined heightwise conditional balance, exact square defects, equality rigidity, and universal recurrence/periodic-orbit barriers, not to the underlying model or previously known first integrals.

## Value

**PASS.** The result converts a model usually studied numerically into parameter-exact stationary constraints valid for arbitrary compact invariant statistical states. The conditional law is stronger than a single global average, while the square-defect identities provide sharp radial and height floors with a complete equality classification. The periodic-orbit corollary supplies orbit-independent amplitude and height barriers that can be used to reject spurious computed cycles or constrain rigorous existence searches.

## Scientific limitations

Compact support is essential in the invariant-measure argument as stated. The theorem supplies necessary constraints and rigidity, not attractor existence, uniqueness, ergodicity, or a chaos criterion. It does not classify unbounded trajectories. The 2016 journal article and some older application literature were not exhaustively inspected theorem by theorem, so priority uncertainty is not zero.
