# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260921-bd312a6bbfdc`

## Correctness — PASS

The Lie bracket is the stated one-dimensional central quotient of Burde–Dekimpe–Vercammen's 13-dimensional three-step example, so Jacobi and three-step nilpotence descend. Assuming a Novikov product, the lower-central-series ideal restrictions, commutator identity, cyclic Novikov identity, and operator identity are all necessary linear constraints on the left multiplications. The exact rational elimination leaves 50 free variables and then forces the right-multiplication commutator entry \([R_2,R_3]_{11,2}=-1/4\), contradicting the Novikov requirement that all right multiplications commute. The fetched verification program was independently re-executed from its exact equations and reproduced ranks \(1088,1376,1504,1678\), 50 free variables, and the constant \(-1/4\).

### Correctness sources

- assigned RESULT.md
- artifacts/verify.py
- Burde–Dekimpe–Vercammen arXiv:0705.1316 full text

### Correctness risks

- The theorem is characteristic zero and does not prove minimality below dimension 12.

## Originality — PASS

The 2008 primary source was read in full through its obstruction construction. Proposition 3.3 gives the 13-dimensional four-generated three-step counterexample and its elimination proof; it does not contain the audited 12-dimensional central quotient. Current Resultary and web searches for 12-dimensional three-step Novikov obstructions found only the audited record. The quotient therefore lowers the explicit dimension bound by one to the best of current evidence.

### equivalent_formulations

Searches:
- Resultary query: 12-dimensional three-step nilpotent Lie algebra no Novikov structure central quotient
- web query: "12-dimensional" "Novikov structure" Lie algebra
- Burde–Dekimpe–Vercammen arXiv:0705.1316 full text

Evidence:
- The primary Proposition 3.3 explicitly states dimension 13.
- No located source gives this 12-dimensional quotient or another 12-dimensional three-step counterexample.

Reasoning:
The comparison was restricted to three-step nilpotent Lie algebras; lower-dimensional counterexamples of larger nilpotency class do not cover the claim.

### broader_coverage

Searches:
- Burde–Dekimpe–Vercammen 2008
- current Resultary Novikov findings
- later citations to the 13-dimensional obstruction

Evidence:
- The strongest prior explicit three-step obstruction located is dimension 13; the same paper proves all three-generated three-step algebras admit Novikov structures.

Reasoning:
The 12-dimensional quotient is a genuine strengthening of the explicit upper bound for the natural minimum-dimension problem.

### exact_database_or_table

Searches:
- current Resultary algebra records
- web exact-dimension searches

Evidence:
- No classification table or smaller published example was located.

Reasoning:
The claim is an explicit structural counterexample with exact certificate, not a known database entry.

### claim_vs_prior_implication

Searches:
- claim-versus-Proposition 3.3 bracket comparison

Evidence:
- The audited brackets arise by imposing one central relation on the 13-dimensional example; nonexistence of a Novikov structure does not automatically descend to an arbitrary quotient, so the new elimination is necessary.

Reasoning:
The prior 13-dimensional theorem does not imply the quotient obstruction; quotients can acquire algebraic structures absent upstairs.

### source_inspections

- **Novikov algebras and Novikov structures on Lie algebras** — https://arxiv.org/html/0705.1316v1. Trigger: Primary source of the classical 13-dimensional three-step obstruction and the necessary identities used in the certificate. Material read: Complete relevant full-text sections, including the structural lemmas, free three-step case, Proposition 3.3 bracket table, and its elimination proof. Method: Primary full-text bracket and theorem comparison. Assessment: PARTIAL PRIOR ART; not covering the 12-dimensional quotient. Evidence: Proposition 3.3 gives dimension 13 and ends with a right-multiplication contradiction; no 12-dimensional quotient theorem appears.
- **Assigned exact symbolic certificate** — artifacts/verify.py. Trigger: Critical nonstandard elimination. Material read: Complete source; the exact constraint system was independently executed. Method: Exact rational replay. Assessment: Verified. Evidence: The four linear ranks and the final forced commutator entry agree exactly with RESULT.md.

### checked_sources

- Burde–Dekimpe–Vercammen full text
- current Resultary Novikov search
- web exact-dimension search
- assigned exact verifier

### residual_risks

- An unindexed or differently phrased 12-dimensional or smaller three-step example could exist.
- No minimality at dimension 12 is claimed.

## Scientific value — PASS

The smallest known dimension of a three-step nilpotent obstruction is a natural boundary question. Showing that the classical 13-dimensional example has a 12-dimensional central quotient that still forbids every Novikov structure improves that boundary and, importantly, shows the obstruction survives a nontrivial quotient via a compact exact certificate.

### Value sources

- Burde–Dekimpe–Vercammen 13-dimensional example
- assigned 12-dimensional quotient certificate

### Value risks

- The one-dimension improvement is valuable as a boundary result, not as a claim of final minimality.

## Limitations

- Characteristic zero only.
- No claim that dimension 12 is minimal.
- Originality is best-of-knowledge with an explicit smaller-example risk.

## Disposition

**PASSED**
