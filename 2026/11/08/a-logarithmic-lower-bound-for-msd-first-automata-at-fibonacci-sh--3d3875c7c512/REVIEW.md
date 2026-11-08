# Scientific review

## Correctness — PASS
The finite-word recurrence gives an inductive proof that conjugate products have their first disagreement at the penultimate position. It identifies the first mismatch of \(f(n+F_k)\) and \(f(n)\) at \(F_{k+1}-2\); for \(k\ge4\) this index has a Zeckendorf encoding of exactly \(k-1\) digits. Intersecting the two-output discrepancy test with the four-state canonical-validity automaton yields at most \(8s_k\) states. A shortest accepted word of length \(k-1\) forces at least \(k\) states, establishing \(s_k\ge\lceil k/8\rceil\). The verification script checks finite instances independently of the proof. No computed finite case is taken as a proof of an infinite statement.

## Originality — PASS, with residual priority uncertainty
The 2026 primary paper by Moradi–Popoli–Shallit–Vukusic proves MSD-first \(O(\log c)\), but its exact minimality theorem applies to LSD-first inputs. It supplies no matching bound specialized to MSD-first Fibonacci shifts. The companion 2026 paper discusses shifts and arithmetic automata but does not establish this lower bound. Earlier structural almost-commutation is acknowledged as background, not credited as new. Search comparisons against research databases and accessible previous records did not identify an overlapping automaton-state claim. Unindexed works, a thesis, or an implicit derivation not recognized in inspected literature remain priority risks.

## Value — PASS
The result supplies a uniform infinite family for which the logarithmic MSD-first upper bound is genuinely necessary. The first-disagreement formula isolates a precise, structural explanation linking Fibonacci-word combinatorics with deterministic state complexity, addressing the unquantified MSD-first minimality direction left by the source paper. The constant \(1/8\) is not claimed optimal.

Self-review: passed. Independent audit: not yet performed.
