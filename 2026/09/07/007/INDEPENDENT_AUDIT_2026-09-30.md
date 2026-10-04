# Fresh audit — SCOPE-20260907-007

Date (UTC): 2026-09-30

## Final claim

Among binary 8-state one-cluster automata with a fixed 5-cycle first letter and permutation second letter, the exhaustive canonical sub-slice maximum reset length is 34, uniquely attained by the stated canonical automaton; the same automaton gives a valid lower bound 34 for the larger arbitrary-second-letter slice.

## Correctness

**PASS** — A fresh independent exhaustive program generated all 14 canonical first-letter types under cycle rotation and permutation of the three off-cycle states, enumerated all 40,320 permutation second letters for each type, and computed shortest reset length by exact BFS on the 256 subset states. It reproduced 564,480 total automata, 550,796 synchronizing automata, maximum reset length 34 with one canonical maximizer, and exactly the stated maps. A separate package witness verifier and stored distance table were inspected.

Residual risk: The result is exhaustive only for the permutation-second-letter sub-slice; the larger arbitrary-second-letter maximum is expressly not claimed.

## Originality

**PASS** — Steinberg's prime-cycle one-cluster theorem gives a general upper bound, including the Cerny bound, but does not determine the exact 8-state 5-cycle maximum. Semantic published-results search found this record as the exact match and no stronger exact census for this finite sub-slice.

Residual risk: Specialized computational automata tables outside indexed sources may exist.

The originality comparison explicitly checked equivalent formulations, broader coverage, exact databases/tables, and whether prior results imply the present claim.

## Value

**PASS** — The slice sits directly inside a theorem-level Cerny-conjecture regime; an exact extremal reset length and exhaustive permutation-letter catalog provide a motivated finite boundary datum rather than a free-standing arbitrary enumeration.

Residual risk: The exhaustive theorem is for a restricted second-letter class, so its broader structural impact is limited.

## Sources inspected

- https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/07/007/RESULT.md — Full result inspected.
- https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/07/007/artifacts/replay_verify.py — Actual 256-subset forward/reverse BFS verifier inspected.
- https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/07/007/artifacts/witness_main.json — Witness maps and length-34 word inspected.
- https://github.com/Resultary/2026/tree/main/2026/9/7/SCOPE007 — Exact semantic search; own record was the only direct match.
- https://arxiv.org/abs/1107.3051 — Steinberg paper inspected, including theorem giving the prime-cycle one-cluster upper bound; it does not give the exact finite maximum 34.
- https://arxiv.org/abs/1309.0044 — Extremal synchronizing-automata search literature checked for overlap; no exact same sub-slice table found.

## Overall disposition

PASS
