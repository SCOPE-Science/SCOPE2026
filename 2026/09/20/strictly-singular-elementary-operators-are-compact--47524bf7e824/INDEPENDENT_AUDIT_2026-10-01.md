# Independent audit — 2026-10-01

## Final claim

For finite elementary operators on any normalized Banach norm ideal of compact operators, compactness, finite strict singularity, strict singularity, and compact--compact coefficient representability are equivalent; every noncompact such operator is bounded below on a one-complemented infinite-dimensional rank-one Hilbert subspace.

## Correctness — PASS

The proof is internally sound. A fixed rank-one column is isometric to \(H\), and its image lies in a finite-support slice of the ideal where the ideal norm is equivalent to the Hilbert--Schmidt norm. Hence strict singularity makes each such restriction compact. Choosing a basis of the left-coefficient span whose Calkin classes are independent, compactness of every evaluated column restriction forces all corresponding right coefficients to vanish; this leaves a representation with compact left coefficients. The symmetric row argument then forces compact right coefficients. Compact--compact coefficients give a norm limit of finite-rank superoperators. Running the same reductions contrapositively produces a noncompact row or column restriction, which on Hilbert space is bounded below on an infinite-dimensional subspace; the rank-one slice is contractively complemented. Thus noncompactness contradicts strict singularity and yields the Bernstein-number witness.

Checked sources:
- Assigned package RESULT.md at the assigned Git snapshot.
- L. A. Fialkow, R. Loebl, Elementary mappings into ideals of operators, Illinois J. Math. 28 (1984); bibliographic and later-paper descriptions inspected, full text unavailable after open-access and authorized institutional attempts.
- C. Apostol, L. Fialkow, Structural Properties of Elementary Operators, Canad. J. Math. 38 (1986), bibliographic/reference material inspected.
- B. Magajna, A System of Operator Equations, Canad. Math. Bull. 30 (1987), bibliographic/full searchable material inspected.
- Published 2026-09-20 finding on one-sided/two-sided multipliers on symmetric norm ideals, complete RESULT inspected.
- Published-record semantic search for strictly singular elementary operators on norm ideals.

Residual risks:
- None.

## Originality — PASS

Best-of-knowledge originality passes, with a named access risk. The exact published-record search found no earlier theorem for finite elementary sums on arbitrary normalized Banach norm ideals. A same-date public finding proves the \(m=1\) multiplier case on symmetrically normed ideals, which is a genuine special case but does not imply the Calkin-reduction theorem for finite sums. The highly relevant Fialkow--Loebl 1984 paper could not be read in full after lawful access attempts, so it is retained as a residual risk rather than treated as noncovering.

### Equivalent formulations

Searches:
- Published-record semantic query: strictly singular elementary operators Banach norm ideals compact rank one witness
- Web query: Elementary mappings into ideals of operators strictly singular
- Web query: strictly singular elementary operator Schatten ideal compact

Evidence:
- The assigned finding was the only exact finite-sum collapse hit.
- A published 2026-09-20 multiplier result covers only a single term on symmetrically normed ideals and explicitly treats its qualitative compact/SS consequence as prior-art-adjacent.

Reasoning: Equivalent formulations include compactness of every strictly singular finite elementary sum, compact-coefficient representability, and a complemented rank-one Hilbert witness for noncompactness.

### Broader coverage

Searches:
- Fialkow--Loebl 1984 bibliographic/later-source inspection
- Apostol--Fialkow 1986
- Magajna 1987
- Same-date one-term multiplier theorem

Evidence:
- Older work concerns elementary maps into ideals, structural equations, or compactness; accessible material did not state the finite-sum ordinary strict-singularity collapse.
- The one-term result is strictly narrower in both number of summands and ideal class.

Reasoning: No accessible broader theorem was found that mechanically implies the finite-sum Calkin-basis reduction.

### Exact database or table

Searches:
- Published-record exact-topic search
- Same-date multiplier quantitative result

Evidence:
- No exact database theorem for all finite sums was located.
- The one-term special case has flat \(s\)-number formulas but does not determine cancellation among multiple elementary terms.

Reasoning: No finite table is relevant; the comparison is by class and implication.

### Claim versus prior implication

Searches:
- One-term multiplier theorem versus finite elementary sums
- Apostol--Fialkow/Magajna structural literature

Evidence:
- For a single \(AXB\), compactness/strict-singularity behavior is already known or adjacent to prior art.
- For a sum \(\sum A_jXB_j\), cancellation requires the two Calkin-independence reductions used in the assigned proof.

Reasoning: The assigned theorem is not a mechanical corollary of the one-term case; the inaccessible 1984 primary source remains the specific unresolved comparison.

### Source inspections

- **Elementary mappings into ideals of operators** — Plausible overlap risk, but inaccessible material alone is not treated as a novelty failure. Material read: Bibliographic record and descriptions/citations in later primary papers; full article text was unavailable after open-access and authorized institutional attempts. Method: Primary-source access attempt plus later-source cross-check; no human-verification bypass. Evidence: Later papers cite it for elementary mappings into ideals; the accessible material did not expose a strict-singularity theorem for finite elementary sums.
- **Structural Properties of Elementary Operators** — Relevant structural prior art, but no matching strict-singularity collapse was located in accessible statements. Material read: Bibliographic/reference and accessible text material. Method: Primary-source search/inspection. Evidence: The paper develops structural properties of elementary operators and cites Fialkow--Loebl.
- **Flat classical s-number profiles for one-sided multiplication on symmetric norm ideals** — Covers the one-term multiplier special case only; it does not cover arbitrary finite sums. Material read: Complete RESULT.md. Method: Published finding full-text inspection. Evidence: It states that a nonzero two-sided multiplier is compact/FSS/SS exactly when both coefficients are compact, with rank-one witnesses.

Checked sources:
- Assigned package RESULT.md at the assigned Git snapshot.
- L. A. Fialkow, R. Loebl, Elementary mappings into ideals of operators, Illinois J. Math. 28 (1984); bibliographic and later-paper descriptions inspected, full text unavailable after open-access and authorized institutional attempts.
- C. Apostol, L. Fialkow, Structural Properties of Elementary Operators, Canad. J. Math. 38 (1986), bibliographic/reference material inspected.
- B. Magajna, A System of Operator Equations, Canad. Math. Bull. 30 (1987), bibliographic/full searchable material inspected.
- Published 2026-09-20 finding on one-sided/two-sided multipliers on symmetric norm ideals, complete RESULT inspected.
- Published-record semantic search for strictly singular elementary operators on norm ideals.

Residual risks:
- The 1984 Fialkow--Loebl paper is the strongest unresolved access risk: full text could not be obtained after open-access and authorized institutional attempts, so whole-document noncoverage is not asserted.
- Older compact-elementary-operator literature may contain an equivalent result under different terminology; no decisive implication was found.

## Scientific value — PASS

The finite-sum extension is mathematically motivated because cancellation between terms defeats reduction to the one-term multiplier case. The result gives a complete class-level compact/FSS/SS boundary and a complemented rank-one witness for every noncompact operator, with immediate quantitative Bernstein consequences. That is a substantive structural theorem if not already present in the inaccessible older source.

Checked sources:
- Assigned package RESULT.md at the assigned Git snapshot.
- L. A. Fialkow, R. Loebl, Elementary mappings into ideals of operators, Illinois J. Math. 28 (1984); bibliographic and later-paper descriptions inspected, full text unavailable after open-access and authorized institutional attempts.
- C. Apostol, L. Fialkow, Structural Properties of Elementary Operators, Canad. J. Math. 38 (1986), bibliographic/reference material inspected.
- B. Magajna, A System of Operator Equations, Canad. Math. Bull. 30 (1987), bibliographic/full searchable material inspected.
- Published 2026-09-20 finding on one-sided/two-sided multipliers on symmetric norm ideals, complete RESULT inspected.
- Published-record semantic search for strictly singular elementary operators on norm ideals.

Residual risks:
- The 1984 Fialkow--Loebl paper is the strongest unresolved access risk: full text could not be obtained after open-access and authorized institutional attempts, so whole-document noncoverage is not asserted.
- Older compact-elementary-operator literature may contain an equivalent result under different terminology; no decisive implication was found.

## Conclusion

The unchanged final claim passes correctness, best-of-knowledge originality, and scientific value.
