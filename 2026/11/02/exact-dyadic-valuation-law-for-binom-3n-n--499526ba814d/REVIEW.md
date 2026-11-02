# Research review

## Correctness — PASS
The Kummer carry count is exact for \(n+2n\), including the terminal zero input. Each merged automaton state has the same outgoing weighted transitions and the same terminal weight as its constituent states, and exact inversion yields the displayed rational function. Differentiation gives the mean; the primitive matrix has a simple leading root and verified first two derivatives, yielding the variance coefficient and Gaussian limit. The finite standalone checks reproduce 131,071 valuations, but unrestricted correctness rests on the proof. Mathematical scope is expressly restricted to binary valuations in dyadic intervals.

## Originality — PASS within inspected evidence
The closest related published results cover distributions *inside one fixed row* of Pascal's triangle (Spiegelhofer–Wallner, 2017–2018), divisibility of a more elaborate binomial quotient (Yang 2017), fibbinary indexing (Lindroos–Sills–Wang 2018), and analytic reciprocal series for the same coefficient family (Adegoke–Frontczak–Goy 2023). None of the inspected statements entails the exact full dyadic-window distribution along \(\binom{3n}{n}\), its reduced length-three recurrence, or its explicit Gaussian parameters. General Kummer digit methods and generic digital-transfer theory are acknowledged as antecedents. Unindexed work and an unidentified stronger general specialization remain possible; a negative search is not a proof of absolute priority.

## Mathematical value — PASS
A complete counting polynomial for all valuations and all initial dyadic block lengths is a natural refinement of the familiar fibbinary zero-valuation set. The exact rational denominator gives a minimal three-state recurrence; exact means and a nondegenerate central-limit law quantify divisibility beyond parity. These are infinite structural conclusions for a canonical binomial sequence rather than an arbitrary truncated table.

## Boundaries and evidence
Reproduce with `python3 verify.py` (standard library). Computational evidence is exact but finite, supplementary to the proof in `RESULT.md`. The comparison with the general fixed-row theory may require continued bibliographic review. A separate independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
