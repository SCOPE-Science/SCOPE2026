# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260917-56689eab9f84`

## Correctness — PASS

The proof is sound. Power-boundedness of an isometry excludes nontrivial Jordan chains, so an algebraic isometry has a square-free minimal polynomial with unimodular eigenvalues. If no iterate of the disk automorphism up to the polynomial degree were the identity, one can choose an interior point with a length-(degree+1) orbit and interpolate a scalar polynomial that leaves only the leading term of the annihilating polynomial, a contradiction. After conjugating the finite-order disk automorphism to a rotation, multiplication by the conjugating function injectively intertwines the isometry with its root-of-unity multiple, forcing complete spectral orbits. Orbit size then gives the divisor law, and the displayed finite-dimensional coefficient-space construction realizes every divisor sharply.

### Sources
- assigned RESULT.md
- Lin's surjective-isometry representation
- independent reconstruction of the interpolation and orbit arguments

### Risks
- The proof assumes the standard Lin representation theorem for surjective vector-valued Hardy-space isometries.

## Originality — PASS

No inspected source states the Hardy-space disk-symbol order divisibility by minimal-polynomial degree or the full root-of-unity spectral factorization. The closest finite-spectrum-isometry paper is broader in Banach-space scope but its accessible abstract only gives necessary spectral conditions and a two-point-spectrum result. The complete article remained inaccessible through both the public route and the institutional retrieval attempt, so it is recorded as a genuine residual risk rather than silently treated as non-covering.

### equivalent_formulations

Searches:
- algebraic surjective isometry Hardy space disk automorphism order divides minimal polynomial degree
- finite spectrum vector Hardy isometry root of unity orbits

Evidence:
- The exact semantic result was only the audited record; no equivalent divisor theorem was located.

Reasoning:
Searches used finite-spectrum, periodic-isometry, weighted-composition, and generalized circular-projection formulations.

### broader_coverage

Searches:
- Botelho–Ilišević On isometries with finite spectrum
- Botelho–Jamison algebraic properties isometry group vector-valued analytic spaces
- Kumar–Kumar–Abu Baker generalized tri-circular projections

Evidence:
- Accessible abstracts concern general finite-spectrum necessary conditions, algebraic properties of isometry groups, and a cubic classification respectively; none states the arbitrary-degree Hardy disk-symbol divisor law.

Reasoning:
These are the most plausible broader sources; their visible statements do not imply the exact theorem.

### exact_database_or_table

Searches:
- finite-spectrum isometry classification databases
- periodic isometry spectrum analytic function spaces

Evidence:
- No exact database/table containing the divisor law was located.

Reasoning:
The target is a structural theorem rather than a tabulated invariant.

### claim_vs_prior_implication

Searches:
- comparison with finite-spectrum and tri-circular prior results

Evidence:
- The cubic prior is a special structured projection problem; the audited theorem applies to every algebraic surjective isometry and explains the cubic root-of-unity phenomenon by a general orbit law.

Reasoning:
The inspected prior statements do not entail the arbitrary-degree theorem.

### source_inspections

- **The isometries of \(H^p(K)\)** — https://doi.org/10.1017/S1446788700032523. Trigger: Representation theorem used in the proof. Material read: Primary abstract stating the weighted-composition/unitary form. Method: Primary-source theorem-scope comparison. Assessment: Provides the representation, not the audited algebraic spectral divisor theorem. Evidence: Every surjective isometry has the disk-automorphism/unitary weighted-composition form.
- **On isometries with finite spectrum** — https://doi.org/10.7900/jot.2020apr11.2270. Trigger: Most plausible prior source for finite-spectrum isometry restrictions. Material read: Primary journal abstract; attempted full PDF returned the journal's moving-wall placeholder, and the institutional retrieval route returned the same placeholder. Method: Primary-source access attempt plus abstract comparison. Assessment: Residual-risk source: the visible abstract does not state the Hardy-space divisor theorem, but full text was not available to inspect. Evidence: The abstract advertises necessary conditions for finite spectra and a two-point-spectrum result on a class of Banach spaces.
- **Generalized tri-circular projections on some vector-valued spaces of analytic functions** — https://arxiv.org/abs/2609.10718. Trigger: Recent exact-space cubic classification. Material read: Primary abstract and stated scope. Method: Claim comparison. Assessment: Covers a cubic projection setting; no arbitrary-degree divisor law appears in inspected material. Evidence: The paper characterizes generalized tri-circular projections on vector-valued Hardy spaces and other analytic spaces.
- **Assigned theorem** — RESULT.md. Trigger: Final claim under audit. Material read: Complete assigned file. Method: Line-by-line proof reconstruction. Assessment: The divisor and factorization argument is self-contained once Lin's representation is granted. Evidence: Interpolation forces finite disk-symbol order and the multiplication intertwiner forces full spectral orbits.

### checked_sources

- Lin 1991
- Botelho–Jamison 2015 abstract
- Botelho–Ilišević 2021 abstract and failed full-text access
- arXiv:2609.10718
- Resultary semantic search
- assigned RESULT.md

### residual_risks

- The full text of Botelho–Ilišević 2021 was inaccessible and could contain closer finite-spectrum restrictions.
- The full Botelho–Jamison 2015 article was also not available in the inspected route.
- Originality is best-of-knowledge, not a priority certificate.

## Scientific value — PASS

The theorem gives a clean arbitrary-degree structural invariant for algebraic Hardy-space isometries, a sharp realization for every divisor, and a direct explanation of the cubic root-of-unity phenomenon. This is a reusable structural theorem rather than a narrow numerical specialization.

### Sources
- Lin's representation theorem
- recent tri-circular projection literature

### Risks
- The theorem is specific to the weighted-composition structure of vector Hardy spaces and is not asserted for arbitrary Banach spaces.

## Limitations

- Originality has a material access risk from two older articles whose full text was unavailable.
- The result relies on Lin's standard representation theorem.
- No computational artifacts are needed.

## Disposition

**PASSED**
