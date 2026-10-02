# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260918-157a5c0304a5`

## Correctness — PASS

The variable-radius lemma is a correct equivalent characterization of full Assouad dimension: equal-radius bad packings give the lower direction, while dyadic grouping of arbitrary radii and any exponent strictly above \(\dim_A\) makes the normalized sum geometrically summable. In the holomorphic-motion proof, quasisymmetry normalizes the image sizes; the diameter-ratio and implicit-function results produce inf-harmonic reciprocals \(1/s_n\); quasiconformal images of the disjoint source balls contain uniformly comparable centered disks, so the transferred variable-radius sums diverge whenever the trial exponent is below \(1/u(\lambda)\). This proves the touching-majorant inequality and hence the inf-harmonic envelope. The symmetric variant uses the same mechanism with the real-line symmetric inputs and the curve-crossing diameter bound.

### Correctness sources

- research package RESULT.md
- Menssen--Younsi arXiv:2609.19522
- Fuhrer--Ransford--Younsi, J. Math. Pures Appl. 177 (2023)
- Fraser, Assouad Dimension and Fractal Geometry

### Correctness residual risks

- The proof invokes standard quasiconformal inradius/quasisymmetry estimates and the cited inf-harmonic compactness/implicit-function machinery rather than reproving those results.
- No higher-dimensional or endpoint-regularity statement is established.

## Originality — PASS

Menssen and Younsi prove the analogous theorem for quasi-Assouad dimension and explicitly pose the full-Assouad extension as Question 1.11; the current source version still advertises the quasi-Assouad result. Fresh Resultary and literature searches found no earlier or later source answering that question. The already-known two-point quasiconformal distortion inequalities for Assouad dimension do not imply the full inf-harmonic parameter dependence.

### equivalent_formulations

Searches:
- Resultary: full Assouad inf-harmonic holomorphic motion
- arXiv:2609.19522 Question 1.11
- full Assouad holomorphic motion inf-harmonic

Evidence:
- The exact theorem-level semantic match found was the audited record.
- The motivating source states the result for quasi-Assouad dimension and poses the full-Assouad version as open.

Reasoning:
The equivalent formulations as an inf-harmonic reciprocal and as existence of touching positive-harmonic majorants were considered.

### broader_coverage

Searches:
- Chrontsios Garitsis--Tyson Assouad distortion
- Fuhrer--Ransford--Younsi holomorphic-motion dimension machinery

Evidence:
- These sources give two-point distortion or general inf-harmonic machinery, not the full-Assouad holomorphic-motion theorem.

Reasoning:
A Harnack-type consequence is weaker than identifying the entire parameter function as inf-harmonic.

### exact_database_or_table

Searches:
- Resultary and web search for a full-Assouad solution to Question 1.11

Evidence:
- No database/table or later published finding covering the theorem was located.

Reasoning:
The claim is a structural functional theorem rather than a finite invariant; database lookup is not the natural coverage mechanism.

### claim_vs_prior_implication

Searches:
- claim versus Menssen--Younsi quasi-Assouad theorem and known planar QC distortion

Evidence:
- The source's proof needs an extra scale-gap argument for quasi-Assouad and explicitly does not state the full-Assouad theorem.

Reasoning:
The audited variable-radius transfer supplies the missing implication; the known two-point inequalities cannot recover inf-harmonicity.

### source_inspections
- **Holomorphic motions, Assouad dimension and quasiconformal mappings** — https://arxiv.org/abs/2609.19522. Trigger: Exact motivating paper and open question. Material read: Current abstract plus accessible statement-level material identifying the quasi-Assouad theorem and Question 1.11. Method: Primary-source scope/open-question comparison. Assessment: Does not cover the full-Assouad theorem; it motivates it as an open extension. Evidence: The abstract advertises reciprocal quasi-Assouad inf-harmonicity, not full Assouad.
- **Assigned full-Assouad proof** — research package RESULT.md. Trigger: Proposed resolution of Question 1.11. Material read: Complete file. Method: Line-by-line reconstruction of the variable-radius lemma and transfer argument. Assessment: The unrestricted-scale packing lemma removes the scale-gap obstruction and supports the claimed extension. Evidence: Divergent target variable-radius sums imply the required Assouad lower bound at every parameter.

### checked_sources

- https://arxiv.org/abs/2609.19522
- https://doi.org/10.1016/j.matpur.2023.07.009
- https://doi.org/10.1112/blms.12727
- research package RESULT.md
- fresh Resultary semantic search

### residual_risks

- The motivating preprint is extremely recent, so an unindexed contemporaneous solution remains possible.
- Not every classical auxiliary source was reread in full; the audit relies on their standard stated lemmas for inf-harmonic and quasiconformal machinery.

## Scientific value — PASS

The theorem answers an explicit current open question and strengthens known two-point Assouad distortion into a full holomorphic-parameter law. The variable-radius transfer isolates why full Assouad dimension is actually easier than quasi-Assouad for this purpose, and the symmetric version has a concrete quasicircle consequence.

### Value sources

- Menssen--Younsi Question 1.11
- known Assouad quasiconformal distortion results
- research package variable-radius transfer proof

### Value residual risks

- The auxiliary packing lemma itself is elementary and not independently valuable; the value lies in its use to close the open holomorphic-motion problem.

## Limitations

- Bounded planar sets only.
- The auxiliary variable-radius packing criterion is not claimed as a separate novelty.
- Originality is best-of-knowledge with material near-simultaneous-work risk.

## Disposition

**PASSED**
