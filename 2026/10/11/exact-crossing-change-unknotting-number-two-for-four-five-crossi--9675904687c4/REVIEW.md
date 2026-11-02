# Independent mathematical audit

## correctness

PASS

The final claim is exactly u(K)=2 (crossing changes only; virtual Reidemeister/detours cost zero) for Green knots 5.40, 5.107, 5.880, 5.1238 represented by their specified source signed Gauss codes, not an all-five-crossing classification. Independently transcribed all four primary Appendix 6.2 10-token signed codes. Their chord endpoint parities give odd crossings {1,2,4,5} and negative signs on all four, so J=-4 in each code. Kauffman Theorem 2 establishes J is invariant under virtual isotopy; one classical crossing change swaps arrow O/U and sign but leaves chord endpoints/parity fixed, changing J by at most 2; unknot has J=0, so u>=2. Independently implemented code transforms crossings 1 and 4 and verifies each Gauss-code RII cancellation has adjacent over endpoints, adjacent under endpoints and opposite signs and RI has adjacent opposite O/U endpoints. For 5.40/5.107: RII(4,5), RI(3), RII(1,2); for 5.880/5.1238: RII(1,2), RI(3), RII(4,5). All four end with empty code and thus u<=2, proving equality. Independently computed canonical source tree sha exactly. This is a complete finite diagram proof and is not mere package VERIFY_OK.

## originality

PASS

Acu–Pongtanapaisan–Singhal (2026) prints the exact four Gauss codes but deliberately gives only u<=2 for each. Kauffman (2004) and Kaur–Kamada–Kawauchi–Prabhakar (2017/2019) furnish the invariant and general odd-writhe lower bound. The specific signed parity calculation J=-4 and explicit two-change cancellations fill four as-yet non-exact table values. Three Resultary searches found an indexed copy of this very finding (excluded as independent priority evidence) and unrelated knot entries, not a separate prior exact statement. Targeted web and known-table searches found no independent published four-row exact-value assessment. Originality is a qualified exact table computation, not novelty for the invariant, the inequality, or the upper-bound certificates; an equivalent earlier table/census remains possible.

## value

PASS

The crossing-change unknotting number is a natural exact invariant for named low-complexity virtual knots. The newest focused published table visibly leaves each of these four Green entries unresolved at u<=2, with slice-genus intervals [1,2]. Establishing a matching two-move obstruction for a uniform four-entry motif gives directly reusable exact knot-table values and distinguishes them from a possible one-change knot; future knot-table comparisons require precisely these entries. This is small finite mathematical work, not a claim of a new method or a general theorem. Its value is confined to making four explicit non-exact published entries exact using an independently checkable code calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
