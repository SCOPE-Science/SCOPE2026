# Independent Audit — 2026-09-29

**Record:** `2026/09/19/absorbing-term-collapse-schreier-ring-varieties--f1e486876901`  
**Title:** Locally finite Schreier ring and fixed-field algebra corollaries  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Disposition:** **REPAIRED**

## Three-axis assessment

- **Correctness — PASS:** The ring and fixed-field classifications are correct. The needed collapse follows from the established locally-finite Schreier main claim: if a term depends on one variable then that variable is recoverable by another term from its value and the remaining variables. An absorbing value in a distinct coordinate makes such recovery impossible in a nontrivial variety, so a term absorbing in two coordinates is constant. Multiplication therefore vanishes; the one-generated free ring has finite cyclic additive group, and permutationality excludes composite exponent, leaving exactly the zero-multiplication exponent-p varieties. The fixed-field conclusions follow analogously.
- **Originality — REPAIRED:** The original record overclaimed originality of the two-coordinate absorbing-term theorem. A publicly posted 2023 Kearnes–Kompatscher–Moorhead–Szendrei slide deck already states the stronger main claim that every term depending on a coordinate admits a term-theoretic recovery of that coordinate; the absorbing-term collapse is an immediate corollary. The repair attributes that mechanism to prior work and narrows the contribution to the explicit ring and fixed-field classifications. Burgin’s 1974 theory already supplies residue-field restrictions and trivial-multiplication Schreier examples, but the inspected prior sources did not state these locally finite ring classifications.
- **Scientific value — PASS:** After narrowing, the exact classification is still useful: all nontrivial locally finite Schreier varieties of possibly nonassociative nonunital rings are precisely zero-multiplication F_p-vector-space varieties, while unital versions are trivial; the same argument gives the finite-field/infinite-field dichotomy for fixed-field algebras.

## Independent checks

- Used the 2023 public slide deck’s recovery main claim directly to derive the two-coordinate collapse, rather than treating it as new.
- Checked the cyclic one-generator free-ring argument and the composite-exponent unary polynomial obstruction.
- Checked both inclusions V⊆R_p and R_p⊆V via the p-element zero ring.
- Checked the fixed-field subvariety argument and local-finiteness dichotomy.

## Literature and evidence

- Kearnes–Kompatscher–Moorhead–Szendrei, Locally finite Schreier varieties (PALS slides, 2023) — Public 2023 slides state the recovery main claim for every term depending on a coordinate; this makes the absorbing-term collapse a direct corollary.
- Kearnes–Moorhead–Szendrei, Locally finite Schreier Varieties — 2026 paper gives the finite 〈0,1〉-minimal/permutational characterization used in the classification.
- Burgin, Schreier varieties of linear Ω-algebras — Prior homogeneous linear-Ω theory and residue-field restrictions; not credited as new in the repair.

## Limitations

- The repaired novelty claim excludes the absorbing-term collapse itself, which is an immediate corollary of a public 2023 main claim.
- Burgin 1974 is close prior art for linear Ω-algebras and residue fields; the exact locally finite ring specialization was not found there.
- Originality of the remaining ring corollary is to the best of the inspected sources.

**Independent-audit disposition:** repaired.
