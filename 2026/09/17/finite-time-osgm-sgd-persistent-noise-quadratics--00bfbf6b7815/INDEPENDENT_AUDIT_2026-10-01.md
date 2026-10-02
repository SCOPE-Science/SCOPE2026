# Independent mathematical audit — SCOPE-20260917-00bfbf6b7815

Final disposition: **passed**.

## Correctness
**PASS.** For the scalar quadratic, differentiating the exact-objective hypergradient feedback gives the projected update p+ = Proj[x/(a x+B)]. Inside |a x|<b_min, an opposite-sign noise atom makes the trial step worse for every p in [0,1/a] and the hypergradient update resets p to zero. A subsequent same-sign atom leaves x unchanged at p=0 while setting p=x/(a x+B); repeating that same atom makes the next trial exactly zero. Finite nonzero mean-zero support necessarily contains both signs. Independent three-step blocks therefore succeed with probability at least q=min(q_- c_+,q_+ c_-), giving P(T>3m)≤(1-q)^m and E T≤3/q. The basin is invariant because the null step never increases the exact objective.

## Originality
**PASS.** The full OSGM-SGD v2 paper was inspected. It explicitly warns that naive in-sample feedback can fail, analyzes an out-of-sample large-batch method, and leaves convergence with non-vanishing gradient noise open. The audited result is narrower and uses exact full-objective feedback plus finite discrete noise, but it supplies a different reset-and-repeat mechanism that is not stated in the source paper. Targeted searches found no earlier theorem with this exact finite-time absorption mechanism on a smooth quadratic.

## Value
**PASS.** This is a sharply delimited positive boundary case for a newly explicit persistent-noise question: persistent stochastic-gradient noise coexists with almost-sure finite-time exact absorption because the adaptive feedback first resets and then identifies the exact one-step stepsize. The explicit geometric tail makes the mechanism mathematically informative beyond a simulation anecdote.

## Source inspections
- **Zhang, Gao, Ye, Udell, Stochastic Gradient Methods with Online Scaling, arXiv:2609.11751v2** — Full 36-page PDF inspected. Section 3 distinguishes out-of-sample OSGM-SGD from naive in-sample feedback; the conclusion explicitly asks whether convergence can be shown under non-vanishing gradient noise. Consequence: The source motivates the audited special case but does not state it; it also limits how broadly the OSGM-SGD name should be interpreted.
- **Targeted optimization literature searches on hypergradient descent and persistent-noise SGD** — Searches covered hypergradient feedback, stochastic stepsize adaptation, persistent gradient noise, and finite-time convergence on quadratics. Consequence: No prior reset-and-repeat finite-time theorem matching the stated hypotheses was located.

## Originality comparison
- **Equivalent formulations.** Searches: hypergradient finite-time absorption quadratic persistent noise; adaptive stepsize repeated noise atom exact hit. Evidence: The proof reduces to a reset event followed by two repeats of one same-sign atom. Reasoning: Equivalent descriptions as adaptive exact line-hit or repeated-atom absorption were searched because the OSGM terminology may not be used in older work.
- **Broader coverage.** Searches: OSGM-SGD non-vanishing gradient noise convergence; stochastic hypergradient convergence persistent noise. Evidence: The source paper’s conclusion still lists non-vanishing-noise convergence as open. Reasoning: The source has broader algorithmic scope but does not cover this noise regime; the audited theorem has narrower hypotheses and a stronger finite-time conclusion.
- **Exact database or table.** Searches: exact theorem phrases and finite-support noise terms; Resultary search for OSGM persistent noise quadratic. Evidence: No exact prior record was found. Reasoning: The PASS does not rely on absence alone; it rests on full-text comparison with the motivating paper and a definition-level reconstruction of the distinct mechanism.
- **Claim versus prior implication.** Searches: source Algorithm 2 out-of-sample feedback; source in-sample counterexample. Evidence: The source paper explicitly separates its analyzed out-of-sample algorithm from in-sample feedback and gives no finite discrete-noise absorption theorem. Reasoning: Neither the large-batch convergence theorem nor the in-sample failure example implies the audited reset-and-hit theorem.

## Residual risks
- The theorem applies to a one-dimensional equal-curvature quadratic with exact objective values and discrete nonzero noise support.
- Terminology risk remains because the source paper reserves OSGM-SGD for its analyzed out-of-sample feedback; the mathematical update in the audited result is self-contained and should be read literally.

## Limitations
One-dimensional local result for an equal-curvature quadratic with exact full-objective values, finite nonzero discrete gradient-noise support, candidate stepsizes [0,1/a], and hypergradient learning rate 1/a. It does not cover nonatomic noise, general smooth objectives, unknown curvature, or noisy objective values. The source paper distinguishes its analyzed out-of-sample OSGM-SGD from naive in-sample feedback, so the audited theorem should be read as a special exact-objective stochastic-feedback mechanism rather than a theorem for the source paper’s full general algorithm.
