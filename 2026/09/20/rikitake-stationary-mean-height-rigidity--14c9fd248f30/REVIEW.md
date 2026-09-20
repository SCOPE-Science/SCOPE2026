# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** Four exact Lie-derivative identities yield \(\langle xy\rangle=1\), \(\mu(U-V)=a\), and \(m=\mu U=a+\mu V\) for every compactly supported invariant probability measure. These imply the factored moment gap
\[
UV-1=\frac{(m-z_+)(m-z_-)}{\mu^2}.
\]
Cauchy--Schwarz gives \(UV\ge1\), while \(m\ge0>z_-\), hence \(m\ge z_+\). The stronger identity
\[
m-z_+=\frac{\mu}{1+r^2}\int(y-rx)^2\,d\nu
\]
was checked algebraically and gives the exact equality set.

For \(a>0\), invariance makes that equality set rigid. On \(y=rx\), the transverse derivative is \((ar/\mu)x(z-z_+)\). A compact invariant support cannot contain \(x=y=0\), since that orbit moves linearly along the z-axis and is unbounded. Thus tangency forces \(z=z_+\), and then \(\dot z=0\) forces \(x^2=1/r\), leaving only the two equilibria. At \(a=0\), the same calculation correctly loses rigidity because \(x=y\) becomes invariant; the known periodic families there provide a sharp stress test. Symbolic verification reproduced every stated polynomial/algebraic identity with zero residual.

The bounded-forward-orbit corollary uses only compactness of the orbit closure and the standard invariance of empirical-measure limits. It does not assume that an individual time average converges.

## Originality

**PASS, to the best of our knowledge.** The original 1958 paper introduces the coupled-disc reversal model; Cook--Roberts (1970) studies its global geometry and asymptotics; Barge (1984) studies invariant manifolds; Llibre--Valls (2008) classifies Darboux integrability and invariant algebraic surfaces; and Llibre--Messias (2009) gives a global Poincare-compactification analysis, including unbounded z-axis motion and the \(a=0\) invariant planes. Kono (1987), Frick--Pleshkov (2024), and Herein--Kuslits--Janosi (2026) study statistical or reversal behavior rather than exact stationary moment constraints for the autonomous system.

Exact and synonymous searches were made for invariant measures, stationary moments, time averages, balance laws, periodic-orbit averages, and Rikitake/disk-dynamo formulations. The accessible 2009 full text was checked at theorem level and by average/mean/integral terminology. No checked source states the invariant-measure identities as a package, the exact nonnegative defect law, the \(a>0\) equilibrium-only equality classification, or the three resulting excursion barriers.

Residual risk remains because the complete theorem-level contents of Rikitake (1958) and Cook--Roberts (1970) were not fully inspected from the available copies. Their accessible abstracts and later citations concern reversals, limit surfaces, stability, and asymptotics, but an equivalent short average identity could have appeared without being indexed. The originality claim is therefore intentionally limited to "to the best of our knowledge."

## Value

**PASS.** The result converts the finite equilibria into a sharp global stationary floor valid for every compact invariant statistical state, not just for a particular numerically observed attractor. The defect formula quantifies exactly how excess mean height equals mean-square departure from the equilibrium current ratio. For \(a>0\), any non-equilibrium recurrent measure and every nonconstant periodic orbit must exceed all three equilibrium coordinate magnitudes somewhere. The \(a=0\) periodic families show that the rigidity transition is structurally sharp rather than an artifact of the proof. The bounded-orbit corollary gives a directly testable long-time diagnostic.

## Scientific limitations

The theorem supplies necessary constraints, not existence, uniqueness, or ergodicity of a Rikitake attractor. Some trajectories are unbounded, so no unconditional global time-average statement is made. The coordinate excursion barriers need not be attained simultaneously. The equality classification is sharp only as stated: when \(a=0\), nonconstant periodic measures on \(x=y\) attain the floor. Non-autonomous forced Rikitake variants are outside the claim.
