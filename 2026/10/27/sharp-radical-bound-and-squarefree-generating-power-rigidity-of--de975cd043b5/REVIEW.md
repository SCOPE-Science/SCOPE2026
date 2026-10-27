# Scientific review

## Correctness
**PASS.** For each prime divisor \(p\mid n\), the power \(\sigma^{n/p}\) partitions the orbit into prime cycles. On one prime orbit, the second-smallest point has a unique smaller image, which forces every signature-preserving unit to equal one modulo \(p\). Independently, the explicit CRT least-significant-digit-first order makes the first changed digit, and its value, identical under increments \(t\) and \(ut\) for any unit \(u\equiv1\pmod{\operatorname{rad}(n)}\). These two directions prove the maximum for all integers \(n\ge2\). The embedded verifier checks the construction through \(n=80\) and all cycles through \(n=8\); neither finite search is the infinite proof.

## Originality
**PASS within the searched and materially inspected literature.** Fuhrmann–Gröger–Passeggi prove prime-cycle reconstruction and acknowledge unrelated signature collisions at composite lengths, without counting signature-preserving generating powers across all lengths. The published quadratic-time reconstruction result treats prime lengths. A previously recorded theorem solves the prime-power subcase, and that subcase is explicitly excluded as an independent novelty assertion. The full mixed-prime classification and the squarefree-composite rigidity criterion are not implied by prime-power cases alone: constructing a single compatible order over different prime-power components requires the CRT digit argument. Searches for radical, squarefree, composite-power, and orbit-comparison aliases found no direct all-length claim. Unindexed equivalent work remains a priority risk.

## Value
**PASS.** This resolves a natural sharp arithmetic extremal problem for a dynamical invariant introduced in recent interval-map rigidity work. It exhibits a substantive squarefree/non-squarefree dichotomy: for squarefree composite lengths, an orbit signature always distinguishes all generating powers, even though distinct unrelated cycles may have the same signature. The universal exact answer and explicit attaining orders give a natural complete classification at the stated level, rather than a small numerical refinement.

## Source and scope limitations
Source material actually inspected: Fuhrmann–Gröger–Passeggi, primary arXiv HTML text, introduction and the full Section 2 definition/lemma/proof; published quadratic-time prime-cycle reconstruction, entire `RESULT.md` document. The separately recorded prime-power result was read for claim overlap only, not re-reviewed. Historical priority under alternative terminology is not ruled out; there is no classification of unrelated cycles.

Self-review: passed. Independent audit: not yet performed.
