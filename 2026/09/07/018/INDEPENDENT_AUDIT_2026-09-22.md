# Independent audit — 2026-09-22 campaign

**Record:** SCOPE-20260907-018  
**Source path:** `2026/09/07/018`  
**Audited repository state:** `1182b71328a408a740c274616869ab885009b620`  
**RESULT.md blob:** `69b83d4b04771ec67a79782dae525dc37f30dfd7`  
**Review date:** 2026-09-23 UTC  
**Reviewer:** separate AI independent audit; no Lean or expert attestation is claimed.

## Claim audited

The record gives an exact symmetry-orbit census of all opposite-colour two-monomer dimer counts on `6xN` rectangles for `N=6,...,10`, 762 orbits total, with agreement between a per-punctured-graph Kasteleyn/Pfaffian method and an independent profile-DP method, plus exact maximizers.

## Correctness — PASS

The computational claims were independently rechecked during this audit campaign by a separate implementation of the width-6 transfer/profile DP. The orbit counts `45,123,156,198,240` and the tabulated pure-dimer baselines and maximizer counts agree with the record, and sampled punctured-board counts agree with exact Pfaffian values. The parity-zero statements follow directly from bipartite colour balance. The record's correction that an orientation Kasteleyn for the unpunctured rectangle need not remain Kasteleyn after deleting bulk vertices is also correct: punctures alter the face structure, so per-punctured-graph verification is required.

## Originality — PASS, narrowly scoped

General exact methods for fixed monomers are prior art. In particular Allegra and Fortin, *Grassmannian representation of the two-dimensional monomer-dimer model* (arXiv:1402.5512), give an exact finite-lattice treatment for an arbitrary fixed finite set of monomer positions, and related Pfaffian formalisms are well known. Therefore no novelty is attributed to the existence of an exact two-monomer method itself.

The surviving contribution is instead the explicit, symmetry-reduced finite benchmark dataset: all 762 inequivalent opposite-colour pairs on five `6xN` rectangles, with exact integer counts, dual independent certification, maximizers and concrete witnesses. Searches for `6xN two monomer exact table`, `monomer correlation rectangle exact orbit census`, `fixed monomer square lattice 6xN`, and the cited dimer literature did not locate this complete finite table or an equivalent published orbit-by-orbit dataset. Originality is thus limited to the dataset/certificate bundle, not the underlying Pfaffian theory.

## Scientific value — PASS

The dataset is large enough to be more than an isolated example and has a clear reusable role: it provides 762 exact regression targets for dimer/Pfaffian/transfer-matrix software, catches the inherited-orientation pitfall on punctured domains, and supplies exact finite-size monomer-correlation benchmarks across several aspect ratios. The dual algorithms reduce the risk that a single implementation convention generated the table. No thermodynamic-limit theorem is claimed.

## Final disposition

**PASSED.** The methods are classical, but the exhaustive finite benchmark table and its independent certification appear original relative to checked sources and have concrete reuse value.