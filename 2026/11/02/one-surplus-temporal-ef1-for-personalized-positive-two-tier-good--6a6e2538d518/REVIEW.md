# Scientific review: one-surplus temporal EF1

## Correctness — PASS

The theorem has quantified assumptions \(n\ge2\), \(m\le n+1\), and \(0<\ell_i<h_i\) with additive singleton values in those tiers. The first \(n\) assignments are to distinct agents. The earliest low-tier recipient \(j\) is universally unenvied: if another agent \(i\) also receives a low-tier good later, \(i\) was available when \(j\) got their good and must value that good at \(\ell_i\); all high-tier recipients already value their own singleton maximally. Removing the final arriving good from the anchor's two-good bundle proves the only nontrivial EF1 inequalities. No low anchor means every first recipient is high and any anchor works. The exact checker obtained `VERIFY_OK cases=3908208 prefix_checks=21778368`, but finite enumeration is explicitly not the proof of the unlimited-\(n\) real-tier statement.

## Originality — PASS, with priority risk

Directly inspected primary materials include Choi--Li's arXiv:2601.12835v3 (Table 1 marks bi-valued exact temporal EF1 as open and Section 4.3.5 establishes approximate TEFX), Elkind et al.'s arXiv:2410.14593v1 (Theorems 3.6-3.7 use two global item types or generalized binary values), Wang--Wei's arXiv:2505.24321v2 (Theorem 6 uses \(n-1\) identical binary agents and one personalized bi-valued agent), and Amanatidis et al.'s arXiv:2607.01159v1 (full personalized-\(k\) temporal EF1 uses a buffer). An additional n+1-good impossibility uses more than two positive values, and the two-value impossibility for EFX addresses a different, stronger property (arXiv:2610.34625v1). Actual research-record searches for unenvied anchors, bivalued first-surplus allocations and equivalent online EF1 formulations did not return implication-equivalent coverage. This evidence supports novelty to the extent checked; unindexed or unstated prior derivations remain a residual risk.

## Value — PASS

One surplus good is the first horizon at which prefixwise EF1 is not automatic from distributing distinct singleton goods. Positive two-tier values form a substantively motivated domain singled out in recent temporal allocation literature. The universal unenvied-anchor lemma gives a strong and usable explanation for the algorithm, while a two-agent, three-good profile demonstrates that a naive one-good-per-agent first phase may be unrecoverable. No welfare, efficiency, larger-horizon or exact EFX result is claimed.

Self-review: passed. Independent audit: not yet performed.
