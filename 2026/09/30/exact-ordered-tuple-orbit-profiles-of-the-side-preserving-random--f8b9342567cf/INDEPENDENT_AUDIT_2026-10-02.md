# Independent scientific audit — SCOPE-20260930-f8b9342567cf

Audited at: 2026-10-02T00:16:07.579488Z

Disposition: **passed**

## Correctness — PASS

After fixing which \(a\) tuple coordinates lie on the left side and \(b=k-a\) on the right, homogeneity reduces the injective orbit problem to an \(a\times b\) binary cross-edge matrix. Global complement, left switches, right switches, and two-sided switches translate by subspaces of dimensions \(1\), \(a\), \(b\), and \(a+b-1\), respectively, so the quotient counts are \(2^{ab-1}\), \(2^{a(b-1)}\), \(2^{(a-1)b}\), and \(2^{(a-1)(b-1)}\). Summing over side assignments and adding the all-left/all-right cases gives the five formulas. Equality-pattern decomposition gives the all-tuple Stirling transform, and balanced binomial summation gives the stated logarithmic growth rates.

### Correctness sources

- assigned RESULT.md
- assigned verify.py
- Yun Lu, arXiv:1101.1947
- Harman–Snowden, DOI:10.1007/s00222-026-01452-2

### Correctness risks

- The finite matrix verifier checks only bounded rectangles and profile values; the general theorem rests on the switch-action quotient proof.

## Originality — PASS

Lu's full primary text classifies the side-preserving reducts and gives the switch/parity descriptions needed to identify the finite translation actions. It does not state the exact ordered-tuple orbit formulas, their asymptotic growth, or the all-arity equality of the distinct left- and right-switch group profiles. Targeted corpus searches found no earlier equivalent formula.

### Equivalent formulations

No equivalent finite-matrix quotient profile theorem was located.

Searches:
- published-corpus query: side preserving random bipartite graph reduct orbit profile row switch column switch exact formulas
- literature query: random bipartite graph reduct oligomorphic orbit counts switch groups

Evidence:
- The exact corpus hit was the assigned theorem; nearby hits concerned Rado-graph and random-poset reduct profiles.
- Lu's classification contains the switch groups but no matching orbit-profile formulas in the inspected full text.

### Broader coverage

The audited formulas are quantitative consequences specialized to Lu's groups, not statements supplied by the broader theories.

Searches:
- arXiv:1101.1947
- DOI:10.1007/s00222-026-01452-2

Evidence:
- Lu gives the complete side-preserving reduct classification and finite parity/switch characterizations.
- Harman–Snowden develop broad oligomorphic-group/tensor-category theory rather than these five explicit counts.

### Exact database or table

The formulas explain and extend the finite values to every arity; the verifier is not the source of the theorem.

Searches:
- published-corpus queries on the initial profiles \(1,2,4,14,82\) and \(1,2,4,11,46\), plus the left/right collision

Evidence:
- No earlier exact table with all five profiles or their all-arity collision was located.

### Claim versus prior implication

The orbit-profile theorem requires performing that quotient count and asymptotic analysis; it is not an immediate quoted classification result.

Searches:
- full-text comparison with Lu's switch definitions and parity characterizations

Evidence:
- Lu's finite switch operations determine which binary-matrix translations are allowed, but the quotient-space dimensions and sum over labeled side assignments are not stated there.

### Sources inspected

- **Reducts of the random bipartite graph** — https://arxiv.org/abs/1101.1947. Trigger: Exact primary classification of the five side-preserving groups. Material read: Full accessible arXiv text, including switch definitions, parity characterizations, and classification sections. Method: Lawful open primary full text. Assessment: COVERING_INGREDIENT. Evidence: It supplies the group and switch structure, not the five exact ordered-tuple profile formulas or left/right profile collision.
- **Oligomorphic groups and tensor categories** — https://doi.org/10.1007/s00222-026-01452-2. Trigger: Modern broad oligomorphic-group work cited as a possible stronger framework. Material read: Accessible theorem/overview material concerning general oligomorphic groups and tensor categories. Method: Publisher/open scholarly text. Assessment: NOT_COVERING. Evidence: The inspected material does not specialize to or compute Lu's five side-preserving random-bipartite orbit profiles.

### Checked sources

- https://arxiv.org/abs/1101.1947
- https://doi.org/10.1007/s00222-026-01452-2
- published-result corpus search

### Residual risks

- A model-theory source focused specifically on profile growth of these reducts could be poorly indexed; no such source was found in the targeted searches.

## Value — PASS

The result gives exact and asymptotic oligomorphic profiles across an entire natural reduct lattice and exhibits two distinct closed groups with identical profiles in every arity. That collision is a substantive limitation on the distinguishing power of orbit profiles.

### Value sources

- arXiv:1101.1947
- DOI:10.1007/s00222-026-01452-2

### Value risks

- The result is restricted to side-preserving groups; groups interchanging the two sides are outside scope.

## Limitations

- The named bipartition sides are preserved setwise.
- Only the five groups in Lu's side-preserving classification are covered.
- The finite verifier supports the matrix quotient arithmetic but does not replace the general proof.
