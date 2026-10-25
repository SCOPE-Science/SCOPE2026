# Scientific review

**Claim reviewed:** The complete clean two-agent binary-Nash-welfare multiplicity formula, its exact nonuniqueness criterion, sharp independent Bernoulli \(m^{-1/3}\) threshold, Gaussian critical probability, and critical multiplicity-entropy distribution as stated in `RESULT.md`. This review applies to that one integrated theorem, not to unconstrained allocations or deterministic tie-broken outputs.

## Correctness — PASS

The binary allocation problem has exactly three valued-good categories: one exclusive to each agent, and jointly approved goods. All exclusive goods are forced by non-redundancy and minimal completeness, so the utility pair is \((a+t,b+c-t)\). Under the two-agent Nash/leximin convention, the optimal splits minimize \(|a-b-c+2t|\). Each minimizing split contributes \(\binom ct\) allocations, yielding the exact formula and criterion \(K_m>1\iff |a-b|<c\). The \(c=0\) and odd-parity \(c=1\) cases have been handled separately; the proof never treats a numerical experiment as an infinite proof.

The random event reduces to comparing \(C_m\sim\operatorname{Binomial}(m,p_m^2)\) with the exclusive-approval difference \(D_m\), which has variance \(2mp_m(1-p_m)\). Chebyshev, Markov, and the bounded-increment central limit theorem establish the subcritical, supercritical, and critical assertions. Uniform binomial entropy bounds plus a continuous mapping argument establish the limiting logarithmic multiplicity law. The standalone `verify.py` checks all \(21{,}845\) labeled approval profiles for \(0\le m\le7\), including exact probabilistic generating-function cross-checks. A second unrestricted ternary-allocation enumeration verified the reduction on all \(341\) profiles for \(m\le4\). Residual correctness risk is concentrated in the chosen clean, untied correspondence definition, which is explicit and necessary.

## Originality — PASS, qualified

Brandl–Suksompong–Teh, arXiv:2607.10064v1 (Sections 2–4), characterize the underlying binary MNW/leximin rule and constraints on consistent tie-breaking; they neither count random inputs with multiple cleaned optima nor derive a \(m^{-1/3}\) threshold or entropy law. Suksompong–Teh, arXiv:2204.03803v1 (Sections 2–3), study selected weighted-Nash outcomes and monotonicity; Halpern–Procaccia–Psomas–Shah, arXiv:2007.06073 (Sections 3–4), study deterministic tie-breaking and randomized **outputs**, not iid random **approval profiles**. Their mathematical conclusions do not imply the present random-ensemble multiplicity laws without the new Bernoulli balance analysis. Closest mathematical-results records concerned distinct committee/assignment or Bernoulli entropy settings and did not state this model's event, threshold, or distribution. Unindexed or undiscovered equivalent prior work is the remaining publication-priority risk.

## Value — PASS

Multiplicity is an intrinsic diagnostic of how much choice is left before an allocation rule resolves ties. In this recently characterized binary-fair-division setting, random sparse demand creates two competing scales: the number \(mp_m^2\) of jointly approved goods and the \(\sqrt{mp_m}\) fluctuation of exclusive demand. Their equality defines a nontrivial, parameter-free cube-root exponent; the exact Gaussian transition and positive-part entropy law quantify both the chance of a choice and its exponential size. This is stronger than the basic binomial split-count identity or an arbitrary finite census. A deterministic priority rule always outputs one allocation; this theorem intentionally characterizes the optimal correspondence prior to priority selection.

## Source comparison and limitations

Full-text scientific sections of the 2026 and 2022 source articles were inspected, as were the 2020 article's deterministic and randomized sections. The cited work on randomized mechanisms randomizes **the allocation conditional on a fixed instance**, whereas the present theorem randomizes **the valuation instance**. The overlap checks exclude discovered covered claims but cannot establish global uniqueness or eliminate unindexed preprints. The theorem does not cover more than two agents, correlated approvals, or assignments of unapproved goods. Numerical finite checks do not prove central limit or entropy convergence. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
