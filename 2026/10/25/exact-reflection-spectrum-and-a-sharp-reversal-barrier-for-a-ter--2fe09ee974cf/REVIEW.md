# Scientific review

## Correctness — PASS

The fixed point is well-defined because the substitution maps `0` to a word beginning in `0`. The proof uses precisely the relevant two published premises: factor complexity \(2n+1\) for every positive length and avoidance of the ten specified factors, of which the displayed seven are a subset. The finite obstruction is exhaustive: all \(9840\) possible strings of lengths one through eight are enumerated, with pattern avoidance checked in both orientations. The resulting short reflected-factor table is witnessed inside the explicit prefix \(h^7(0)\). The empty length, palindromes and nonpalindromic two-element reversal classes are treated separately. No finite experiment is used to infer an infinite statement; the length-eight forbidden-factor property extends to every longer length by taking a subfactor.

## Originality — PASS, with residual uncertainty

The directly relevant 2022 primary paper supplies the morphism, all-length factor counts and avoidance list, but does not state the exact reflection spectrum or the sharp length-eight barrier. The 2024 primary paper introduces reflection complexity and proves qualitative *eventual* disappearance of reflected factors for uniformly recurrent non-reversal-closed words; it does not give this sequence's exact threshold or small-length values. The related 2017 source concerns the \(2n+1\) complexity family rather than reflection counts. Searches for the exact morphism, reflected-factor cutoff, reversible factors and reflection-complexity values in the public literature and the mathematical-record index uncovered no equivalent formula, but incompleteness of indexing remains a risk. The finding is a new explicit classification and finite obstruction, not a claim to have invented the general dichotomy or ordinary factor-complexity formula.

## Mathematical value — PASS

Reflection complexity is a recently formalized invariant, and this well-studied nonuniform ternary substitution is a natural benchmark with linear ordinary factor complexity and non-reversal-closed language. The classification finds the *least possible* point at which the reflection quotient stops identifying any two factors, gives the complete earlier orbit spectrum, and shows that seven local forbidden patterns alone enforce a sharp universal reversal barrier. These are exact structural facts about a naturally motivated invariant, beyond the qualitative eventual theorem. No broader substitution-family theorem is asserted; the computational component is small but complete and tied to the structural finite-type obstruction.

## Boundaries

The dependency on previously published all-length properties is explicit. No independent mathematical audit has been conducted. Unlocated equivalent treatments of this morphic word are a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
