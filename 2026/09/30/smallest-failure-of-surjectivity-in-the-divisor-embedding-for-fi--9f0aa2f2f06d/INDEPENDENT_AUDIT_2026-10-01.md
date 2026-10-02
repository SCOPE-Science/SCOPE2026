# Independent audit — 2026-10-01

## Final claim

The divisor-lattice frequency embedding for proper congruences of a finite reflexive line first fails to be surjective on \(L_5\); exactly the two side-rest congruences \(\langle1;1\rangle\) and \(\langle1;3\rangle\) fail there, each missing divisor \(2\).

## Correctness — PASS

The complete folding classification from the primary source gives the possible congruences and frequencies through \(L_5\). The source theorem gives gcd/lcm behavior of frequencies, hence the divisor-lattice embedding. A fresh replay of the actual set-partition verifier directly tested every bisimulation equivalence through six vertices and returned exactly two defects: \(\langle1;1\rangle\) and \(\langle1;3\rangle\), each with image \(\{1,4\}\) and missing divisor \(2\). It also verified surjectivity through \(L_4\) and the unique frequency-two congruence \(\langle2;2\rangle\), which is incomparable with the two defective congruences.

Checked sources:
- Areces--Campercholi--Penazzi--Sánchez Terraf, The Lattice of Congruences of a Finite Line Frame, arXiv:1504.01789 / J. Logic Comput. 27 (2017), complete 31-page primary PDF inspected.
- Published-record semantic search for frequency-embedding surjectivity, missing divisor two, and the six-vertex obstruction.
- Fresh replay of the package exhaustive set-partition verifier through \(L_5\).

Residual risks:
- The finite minimality statement is completely exhausted through \(L_5\); no claim is made about all larger lines.

## Originality — PASS

Best-of-knowledge originality passes. The complete 31-page primary paper was inspected: it proves that each principal interval embeds into the divisor lattice and develops the frequency gcd/lcm formulas, but does not state that the embedding is always surjective or identify the first failure. Semantic searches found no earlier six-vertex obstruction or stronger surjectivity criterion covering it.

### Equivalent formulations

Searches:
- Resultary query: finite line frame divisor embedding frequency surjectivity L5
- Full-text inspection of arXiv:1504.01789

Evidence:
- The assigned finding is the only exact semantic hit.
- The source states “embeds into” the divisor lattice and Theorem 40 gives gcd/lcm formulas.

Reasoning: Equivalent formulations are the missing-divisor obstruction, a failure of interval/divisor-lattice isomorphism, and the two mirror side-rest cases; none was located as prior theorem.

### Broader coverage

Searches:
- Areces--Campercholi--Penazzi--Sánchez Terraf complete classification and Theorem 40

Evidence:
- The source is broader on the full congruence lattice and frequency arithmetic but stops at an embedding theorem.

Reasoning: A lattice embedding can have a proper image; the source theorem does not imply surjectivity or its minimal failure.

### Exact database or table

Searches:
- Source classification plus exhaustive small-line table

Evidence:
- No prior exact table identifying the two \(L_5\) defects was found.
- Fresh exhaustive enumeration independently reproduces the claimed first failure.

Reasoning: The finite enumeration proves the small cutoff, while novelty rests on source comparison and searches.

### Claim versus prior implication

Searches:
- Primary embedding theorem versus audited sharpness result

Evidence:
- The source theorem permits proper sublattices of the divisor lattice and gives no converse existence for every divisor.

Reasoning: The audited claim is a sharp boundary counterexample to a natural strengthening, not a corollary of the embedding statement.

### Source inspections

- **The Lattice of Congruences of a Finite Line Frame** — Provides all structural inputs but not the first nonsurjectivity result. Material read: Complete 31-page primary PDF, including the folding classification and Theorem 40 on frequency gcd/lcm. Method: Primary full-text and rendered-page inspection. Evidence: The abstract states only an embedding into a divisor lattice; Theorem 40 gives join/meet frequency formulas.

Checked sources:
- Areces--Campercholi--Penazzi--Sánchez Terraf, The Lattice of Congruences of a Finite Line Frame, arXiv:1504.01789 / J. Logic Comput. 27 (2017), complete 31-page primary PDF inspected.
- Published-record semantic search for frequency-embedding surjectivity, missing divisor two, and the six-vertex obstruction.
- Fresh replay of the package exhaustive set-partition verifier through \(L_5\).

Residual risks:
- A differently phrased later note on the same lattice remains a best-of-knowledge risk.

## Scientific value — PASS

The result answers a natural sharpness question left by a structural embedding theorem: it identifies the smallest line where “embedding” cannot be strengthened to “onto” and completely classifies the first obstruction. Such a minimal counterexample and boundary classification are independently useful even without a general all-\(n\) criterion.

Checked sources:
- Areces--Campercholi--Penazzi--Sánchez Terraf, The Lattice of Congruences of a Finite Line Frame, arXiv:1504.01789 / J. Logic Comput. 27 (2017), complete 31-page primary PDF inspected.
- Published-record semantic search for frequency-embedding surjectivity, missing divisor two, and the six-vertex obstruction.
- Fresh replay of the package exhaustive set-partition verifier through \(L_5\).

Residual risks:
- The result does not classify nonsurjective intervals for larger lines.

## Conclusion

The unchanged final claim passes correctness, best-of-knowledge originality, and scientific value.
