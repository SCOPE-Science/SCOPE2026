# Scientific review: destination-marked stationary-observation hitting times

## Correctness — PASS

An explicit Markov-renewal construction with independent visits and finite second moments defines the equilibrium aged law. The first-return physical-time normalization establishes source-independent entrance Kemeny sums. A separate stationary marked-interval size bias gives residual mean \(u_i/(2m_i)\) and next-mark probability \(b_{ik}/m_i\). Subtracting first-step equations yields the stated exact correction. In the three-state Gamma/exponential example, exact-rational calculations produce the two opposite stationary-observation sums \(15/7\) and \(17/7\), both compared with entrance \(16/7\). The minimality statement follows because a no-self-jump two-state chain has deterministic next destinations. The provided verifier reproduces the witness and finite algebraic cross-checks. Finite tests do not prove the theorem; the complete argument is in RESULT.md.

## Originality — PASS, subject to historical-priority risk

Hunter's 2018 Markov-renewal Kemeny theorem and Voits's 2026 graph-theoretic counterpart concern fresh-entrance initialization. Their constancy is incorporated, not contradicted. Khorshidian and Fathizadeh (2022) already give age-conditioned first-passage machinery; the residual-life first-step identity is not novel in isolation. A related mathematical result already characterizes equality of fresh-entrance second hitting-time moments with a pseudo-rate Markov chain by the same first/second holding moments and a three-state witness. The mathematical implication comparison is: it does not state stationary-observation Kemeny values or construct two kernels sharing the **entire unmarked** laws and entrance first-passage matrix with **oppositely directed** aged Kemeny defects; the new witness has deliberately nonzero marked-duration discrepancy, unlike the earlier second-moment-matching witness. The assessed contribution is the exact destination-marked correction as a means to expose the minimal three-state opposite-defect **nonidentifiability** under equal full unmarked sojourn laws, embedded transitions, stationary state laws and entire entrance first-passage matrix. Relevant primary full texts and scientific claim searches did not identify that specific structural implication. The 2025 follow-up on conditional hitting-time/state-dependent measures could not be inspected fully and remains a material, explicitly unresolved priority risk; there is no claim of exhaustive historical uniqueness.

## Mathematical value — PASS

Network hitting-time summaries are routinely computed from transition probabilities and per-state holding laws. The exact pair demonstrates an unexpected limit of those reductions when measurement begins at an arbitrary physical-time observation rather than on entry: a hidden duration/next-destination association changes the weighted passage time, even for marginal hold distributions with unit squared coefficient of variation. The minimal-three-state obstruction provides a natural boundary and the general correction identifies the missing marked statistic. No classification for other kernels is claimed.

## Scope and references

Finite irreducible Markov-renewal networks with positive sojourns and finite second moments; no embedded self-jumps; zero at already-reached target. Main sources: arXiv:2610.13505v1 (2026), arXiv:1802.08330 (2018), DOI:10.21203/rs.3.rs-2184300/v1 (2022), and uninspected later DOI:10.1080/03610926.2025.2483291 (2025). Independent mathematics review and historical priority checking remain outstanding.

Self-review: passed. Independent audit: not yet performed.
