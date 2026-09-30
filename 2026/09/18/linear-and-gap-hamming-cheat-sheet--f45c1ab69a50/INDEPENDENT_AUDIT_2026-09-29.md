# Independent audit — 2026-09-29

**Record:** `2026/09/18/linear-and-gap-hamming-cheat-sheet--f45c1ab69a50`  
**Title:** Near-square-root rectangle bounds from a linear-AND Gap-Hamming promise circuit  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `d9aa6b680a61e96fcc4e7e9dac92ea18494ffc8d`  
**Disposition:** **PASSED**

## Correctness

**PASS** — The circuit substitution and parameter propagation check. A full adder uses two AND gates; the balanced population-count tree costs exactly 4m−2k−4 ANDs per block. Two fixed-threshold comparators cost at most 4(k+1) ANDs, so the k-block promise circuit plus conjunction/final-gate overhead is <5km for k≥12 and can be padded to d=5km. Wang–Wu's source arithmetizes an arbitrary ordered XOR/AND/NOT circuit by treating each AND output as a certificate variable, so the fully linear PCP interface and uniqueness induction survive the replacement. Substituting d=5km into their encoding gives N=40k^2m^2−3km, and their unchanged rectangle exponent m/(8k) yields the stated 1/(51 log_2^2 N) near-square-root bound.

## Originality

**PASS** — Balanced counters and constant comparators are standard and are properly excluded from novelty. Wang–Wu's current report explicitly uses d=k(m(m+3)+1)=Θ(km^2) AND gates for the promise circuit. Targeted current searches found no prior insertion of an O(km)-AND counter into this cheat-sheet construction or the resulting 2^{-Ω(√N/log^2N)} rectangle-density statement. The novelty is therefore a quantitative strengthening of a very recent construction rather than a new circuit primitive.

## Scientific value

**PASS** — Although the local circuit idea is elementary, removing an entire factor of m from the certificate-driving gate count changes the construction's input scaling from Θ(k^2m^3) to Θ(k^2m^2). This upgrades the final rectangle and P^{NP^cc}/P^{RP^cc} lower bounds by a major exponent and is scientifically useful within the source's separation framework.

## Findings

- The fixed-threshold comparator recurrence is Boolean-correct; its XOR update uses disjoint states.
- The balanced-tree sum of ripple-adder costs is exactly 4m−2k−4.
- The ECCC source explicitly labels the original d=k(m(m+3)+1) AND gates in evaluation order and arithmetizes AND as field multiplication, XOR as addition, and NOT as 1+a.
- The N_k formula and constant 51 follow algebraically from the source encoding and 8√40<51.

## Independent checks

- Exhaustively checked the full-adder and comparator truth tables for small word lengths.
- Re-derived the gate-count sum and the k≥12 padding inequality.
- Inspected the Wang–Wu ECCC full text/PDF at Lemma 3.3 and the ordered-AND arithmetization interface.
- Recomputed the field-soundness and N-to-m conversion and searched for current overlapping quantitative improvements.

## Sources

- https://eccc.weizmann.ac.il/report/2026/190/ — Wang–Wu report and authoritative current source for the cheat-sheet construction.
- https://arxiv.org/abs/2609.20763 — ArXiv version of Wang–Wu; current searches found no v2.
- https://eprint.iacr.org/2019/188 — Fully linear PCP background; the audited novelty does not claim this machinery.

## Limitations

- The result is a construction-specific quantitative improvement and does not prove optimality or a matching rectangle lower bound.
- The new ingredient is an application of standard Boolean-circuit components rather than a new circuit theorem.
- The motivating report is only days old, so near-simultaneous discovery or a later author revision remains a material originality risk.

This audit is independent of the repository's pre-existing same-model review. GitHub was read only as evidence; no repository changes were made by this audit run.
