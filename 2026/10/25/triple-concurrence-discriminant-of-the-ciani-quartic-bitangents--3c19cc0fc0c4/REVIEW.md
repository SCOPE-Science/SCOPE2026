# Review of the Ciani-pencil bitangent incidence classification

## Correctness — PASS
The 28 explicit lines are verified by square restrictions of the quartic, and distinctness holds on the exact smooth parameter domain. For all 3276 three-line choices the determinant in \(\mathbb Q[t]\) is generated and factored; algebraic resultants group them into 16 parameter strata, of which three are singular. Pair-by-pair exact incidence reconstruction yields all 27 smooth exceptional parameter values and the table in the result. The full calculation was replayed successfully with the embedded `verify.py`; no floating-point inference, partial census or timeout claim is used.

## Originality — PASS, with residual literature risk
Janasz–Pokora–Zieliński explicitly give only three special bitangent arrangements and a lower bound on quadruple concurrency for all smooth members; no all-parameter triple discriminant appears in the inspected §3 and paper-wide searches. Their three examples have zero triple points. Classical bielliptic-involution and quartic-automorphism results control quadruple points, not triple incidence. Targeted published-record searches and accessible claim comparisons found no equivalent or dominating all-parameter polynomial classification. Nineteenth- and twentieth-century specialized sources may contain unindexed related incidence data; a negative search does not establish uniqueness.

## Mathematical value — PASS
The source paper explicitly motivates understanding the incidence structure of symmetric quartic bitangents. The new result identifies exactly 24 previously unreported smooth parameters where ordinary triple points occur, gives their complete 4/12/24 stratification, and characterizes the generic locus as having no triple points. It supplies a reusable rational parametrization of all 28 lines and a compact determinant/resultant calculation; this is a natural family-wide classification, not an arbitrary finite slice.

## Closest literature and scientific limits
Source: M. Janasz, P. Pokora, M. Zieliński, arXiv:2308.16514 (2023; revised 2024), §3, especially Propositions 3.1–3.3 and 3.7–3.8. The result is restricted to smooth complex fibers and unlabeled multiplicity counts. No independent reproduction beyond the presented exact checker, peer review, or external validation has been performed.

Self-review: passed. Independent audit: not yet performed.
