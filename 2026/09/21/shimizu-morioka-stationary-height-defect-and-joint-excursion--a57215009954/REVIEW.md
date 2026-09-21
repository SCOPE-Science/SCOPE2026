# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof uses only invariant-measure generator identities, one explicit polynomial coboundary, compact-support invariance, and elementary positivity.

For a compactly supported invariant probability measure \(\mu\), applying stationarity to an arbitrary antiderivative \(H(z)\) gives
\[
\int h(z)(x^2-bz)\,d\mu=0
\]
for every continuous \(h\) on the \(z\)-projection. This is exactly
\[
\mathbb E[x^2\mid z]=bz.
\]
Since \(x^2\ge0\) and \(b>0\), it also excludes negative \(z\) from the support. Taking \(h=1,z\) gives the stated moment and covariance identities.

The displayed polynomial
\[
W=xy-z+\frac12z^2+\frac a2x^2
\]
has the exact Lie derivative
\[
LW=y^2-bz(z-1),
\]
verified algebraically in the accompanying artifact. Averaging yields both the \(z(z-1)\) balance and the completed-square defect. No simulation is used in the proof.

Equality in the defect forces \(y=0\) on the support. The maximal complete bounded dynamics inside \(y=0\) consists only of \(O\) and \(E_\pm\): if \(x\ne0\), invariance forces \(z=1\) and then \(x^2=b\); if \(x=0\), the remaining axis equation \(z'=-bz\) has no nonzero complete bounded orbit. Hence the equality measures are exactly the three-equilibrium simplex.

The joint excursion statement was stress-tested separately from the height defect. A non-equilibrium measure has positive mass above \(z=1\). On that set the conditional law gives
\[
\int_{z>1}x^2\,d\mu=b\int_{z>1}z\,d\mu>b\,\mu(z>1),
\]
so \(x^2\le b\) almost surely there is impossible. This establishes positive mass where both strict inequalities hold simultaneously.

Boundary checks included the three equilibrium Dirac measures and arbitrary mixtures of them, for which the defect is exactly \(1/4\); the strictness of the periodic-orbit corollary; and the singular limit \(b=0\), which is intentionally excluded because the argument and equilibrium structure degenerate there.

## Originality

**PASS, to the best of our knowledge.** Shimizu--Morioka (1980) is the source of the model and its early symmetry-breaking analysis; no novelty is claimed for that material. The original 1980 article was not fully inspected at theorem level, which remains a priority risk.

Messias--Gouveia--Pessoa (2012) was inspected at theorem level in the accessible full text. Its principal exact results describe the Poincaré compactification, dynamics at infinity, the \(\alpha=0\) line of equilibria, and associated heteroclinic structures. Targeted text searches did not locate invariant-measure or time-average statements matching the present result.

The accessible Llibre--Pessoa (2015) preprint was read through its principal theorem and singular-point analysis. It studies codimension-one and codimension-two Hopf bifurcations and their periodic-orbit stability. Searches of that full text for measure, average, and moment formulations did not locate the conditional law or square defect proved here.

Capiński--Turaev--Zgliczyński (2018) rigorously proved existence of a Lorenz attractor for an open parameter set. Huang--Shi--Li (2020) studies integrability and the scaling relation to a Rucklidge system; the complete article was not inspected, so equivalent-formulation priority risk remains there and in the broader Rucklidge literature. Searches using both Shimizu--Morioka and Rucklidge terminology did not locate the exact stationary height law, equality simplex, or simultaneous threshold.

Current-status checks also included the 2025 Lorenz-attractor cascade work and the 2026 computer-assisted heteroclinic-orbit study. These confirm continued work on global bifurcation geometry but did not yield a stronger result covering the stationary identities here.

The general fact \(\int LF\,d\mu=0\) for invariant measures is standard and is not claimed as new. The novelty claim is the model-specific synthesis: the exact conditional law, the square defect, complete equality rigidity, and the resulting simultaneous \(z>1,\ |x|>\sqrt b\) barrier valid for every compactly supported invariant measure and all \(a,b>0\).

Residual priority risks are the incompletely inspected 1980 original paper, older Russian Shilnikov literature on the model, and the full equivalent Rucklidge literature. No available statement gave concrete evidence that these exact claims are already covered.

## Value

**PASS.** The Shimizu–Morioka system is a standard Lorenz-like model with parameter-dependent fixed points, periodic orbits, homoclinic structures, and Lorenz attractors. The result supplies a parameter-uniform geometric constraint on all compact stationary statistics rather than on a particular numerically observed attractor.

The heightwise identity is stronger than a single global moment relation: at almost every stationary height it fixes the conditional \(x^2\)-energy exactly. Combining it with the polynomial defect makes the two nonzero equilibria the sharp threshold for genuinely non-equilibrium recurrent statistics. Any nonconstant periodic orbit, and more generally any non-equilibrium compact stationary state, must enter the region \(z>1,\ |x|>\sqrt b\) with both inequalities simultaneously. This gives an analytic diagnostic that is independent of the damping parameter \(a\) and requires no knowledge of the detailed bifurcation regime.

The equality classification is also structurally useful: failure to cross above \(z=1\) is not merely restrictive but forces the entire invariant measure to be a convex combination of equilibria.

## Scientific limitations

Compact support is essential to the stated invariant-measure framework and to the equality-support argument. The theorem does not establish dissipativity for all initial conditions, existence of a Lorenz attractor, or uniqueness/ergodicity of a physical measure. It does not say that every transient orbit crosses the thresholds, nor does it give a pointwise barrier for arbitrary nonperiodic bounded trajectories. The bounded-trajectory formulas are time-average balance laws, not convergence theorems.

The case \(b=0\) is excluded. The literature search was targeted rather than exhaustive, and the original 1980 paper, older Russian bifurcation literature, and the complete 2020 integrability paper were not all inspected at theorem level. Originality is therefore explicitly qualified as to the best of our knowledge.
