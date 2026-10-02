# Independent audit — Exact maximum size of q-ary 2-traceability codes of length three

Audited at: 2026-10-01T18:04:30Z

Disposition: **passed**

## Correctness

**PASS** — The fiber-privacy lemma is valid: a proper repeated fiber in one coordinate forces each member to use symbols globally unique in the other two coordinates, otherwise a descendant has an outside codeword tied with or closer than a parent. Consequently repeated-fiber memberships are disjoint across coordinates. Counting used symbols gives \(R_i-G_i\ge n-q\), and for \(n>q\), \(G_i\ge1\), whence \(3(n-q)\le n-3\). The diagonal and three-group constructions meet the resulting bound. An independent direct descendant check verified the constructions for \(2\le q\le18\); this finite check is supplementary to the symbolic proof.

## Originality

**PASS** — The 2010 construction gives the odd-alphabet length-three family of size \(3(q-1)/2\), while Owen--Ng (2015) explicitly says the best constant remained open and turns to a length-four upper bound. Searches did not locate an exact all-\(q\) length-three optimum, the even-\(q\) construction, or the fiber-privacy upper bound.

### equivalent_formulations

Searches: Resultary: q-ary 2-traceability code length three exact maximum M_TA(3,q,2) fiber privacy; web search: M_TA(3,q,2), 2-TA length 3 exact maximum.
Evidence: Resultary returns the audited record as the only exact length-three all-alphabet match.
Reasoning: The search included both traceability and 2-TA notation and formula variants; no equivalent theorem was located.

### broader_coverage

Searches: Blackburn--Etzion--Ng 2010 DOI:10.1016/j.jcta.2010.02.009; Owen--Ng 2015; Kabatiansky 2019; Chang--Hsu 2026.
Evidence: The older sources provide constructions and general/asymptotic bounds; Owen--Ng explicitly describes the best constant question as open and proves an upper bound at length four.
Reasoning: No inspected stronger theorem implies the exact length-three all-\(q\) cardinality.

### exact_database_or_table

Searches: Resultary published findings search; traceability-code exact-cardinality searches.
Evidence: No table/database result matching \(\max\{q,\lfloor(3q-3)/2floor\}\) was found.
Reasoning: The repository verifier checks finitely many constructions only and is not used as novelty evidence.

### claim_vs_prior_implication

Searches: Owen--Ng 2015 full accessible article text; Blackburn--Etzion--Ng 2010 cited construction.
Evidence: Owen--Ng records the length-three lower construction but states that the best constant was not known, and its new upper bound is for length four.
Reasoning: The prior odd-\(q\) construction does not imply optimality or the even-\(q\) formula; the audited fiber-counting lemma supplies a new upper-bound mechanism at length three.

### Source inspections

- **A note on an upper bound of traceability codes** (Owen--Ng, Australasian Journal of Combinatorics 62 (2015), 140--146): NOT_COVERING; it records the length-three lower construction but proves an upper bound for length four. Material read: Accessible full article text including abstract/introduction and stated main result. Trigger: Primary follow-up source discussing the length-three construction and the unresolved constant. Evidence: The article states that the best possible constant remained open and gives the known length-three size \(3(q-1)/2\).
- **Traceability Codes** (DOI:10.1016/j.jcta.2010.02.009): PARTIAL_COVERAGE: lower construction only, not the exact all-\(q\) optimum. Material read: Bibliographic/abstract-level material and its statement as quoted in the 2015 primary follow-up. Trigger: Original source for the odd-alphabet length-three construction. Evidence: The 2015 paper attributes the length-three \(3(q-1)/2\) construction to this source.

Checked sources: DOI:10.1016/j.jcta.2010.02.009; Owen--Ng 2015 open article; DOI:10.1134/S0032946019030074; DOI:10.1016/j.tcs.2023.113800; DOI:10.1007/s10623-025-01748-z; Resultary published findings search.
Residual risks: An older thesis or paper using different traceability notation could contain the same length-three optimum; no specific such source was identified..

## Scientific value

**PASS** — The maximum size of a strength-two length-three traceability code is a natural exact extremal invariant. The theorem proves the known odd-alphabet construction optimal, settles every even alphabet, and determines the exact leading constant \(3/2\) at this length, making it a useful base case for traceability-code bounds.

## Limitations

- Specific to strength two and length three.
- Finite construction checks are supplementary to the symbolic proof.
- Originality is best-of-knowledge with residual terminology risk.

This file records a scientific assessment only; it does not claim formal verification or expert attestation.
