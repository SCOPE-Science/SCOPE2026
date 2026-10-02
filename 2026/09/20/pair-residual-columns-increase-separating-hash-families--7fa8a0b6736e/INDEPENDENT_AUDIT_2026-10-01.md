# Independent scientific audit — SCOPE-20260920-7fa8a0b6736e

Audited at: 2026-10-01T20:13:40.771389Z

Disposition: **passed**

## Correctness — PASS

The construction uses one duplicated source column in the top block and \(x\) fresh constant symbols in the bottom block. If selected special columns meet at most one target class, projecting them to the source column and padding that single projected class preserves disjointness and fits because \(n\ge W\). If they meet at least two classes, choosing any two such classes lowers their required ordinary sizes by one each; the actual ordinary sets can be padded to the corresponding pair-residual type inside the \(n-1\) ordinary columns, and the pair-residual auxiliary separates them while the \(x\) distinct special symbols separate all selected specials. Zero residual parts and the one-part vacuous case are consistent, and the symbol budget is exactly at most \(m\).

### Correctness sources

- assigned RESULT.md
- Gregory Zaverucha, 2010 thesis, Section 3.1.2, pp. 39-41
- Martirosyan-van Trung 2008 perfect-hash recurrence

### Correctness risks

- A compound pair-residual auxiliary can require more rows than a full-type auxiliary in some numerical regimes; the theorem claims weaker separation strength, not universal row savings.

## Originality — PASS

The primary thesis section has been inspected directly. Its Theorem 3.13 gives the reduced one-column construction only for two-class types; Theorem 3.14 treats arbitrary type but explicitly keeps the full original type in the auxiliary; Theorem 3.15 gives the strength-two reduction for perfect hash families; and Theorem 3.16 gives arbitrary-width column increase for arbitrary separating type but again with a full-type auxiliary, followed by the statement that improvements should be possible. The audited pair-residual compound auxiliary is exactly the missing arbitrary-type reduction and extends the two-class reduced mechanism to arbitrary duplication width.

### Equivalent formulations

No equivalent formulation was found; the closest source explicitly identifies the unreduced auxiliary as a deficiency.

### Broader coverage

The audited theorem combines the arbitrary-type and reduced-strength features without assuming the perfect-hash symmetry that makes the residual unique.

### Exact database or table

The claim is a construction theorem rather than a database invariant; exact theorem-level comparison is decisive.

### Claim versus prior implication

The new conclusion is a natural strengthening of the prior construction but is not the prior theorem itself; it replaces a full-strength compound requirement by the exact family of strength-\(W-2\) residual requirements.

### Sources inspected

- Hash Families and Cover-Free Families with Cryptographic Applications — https://uwspace.uwaterloo.ca/items/73fdcd45-2ba4-4d2b-851c-e5ec75e05ad6. NOT_COVERING: Theorem 3.13 has the reduced two-class case; Theorem 3.14 says the arbitrary-type auxiliary is unfortunately not reduced; Theorem 3.16 retains full type for arbitrary width and explicitly notes room for improvement.
- Explicit constructions for perfect hash families — https://doi.org/10.1007/s10623-007-9138-6. COVERING_SPECIAL_CASE: It covers perfect-hash types, where all pair residuals coincide, not arbitrary separating types.

### Checked sources

- https://uwspace.uwaterloo.ca/items/73fdcd45-2ba4-4d2b-851c-e5ec75e05ad6
- https://doi.org/10.1007/s10623-007-9138-6
- https://doi.org/10.1016/j.jcta.2010.11.006
- https://doi.org/10.1137/15M103827X
- https://doi.org/10.1016/j.tcs.2019.10.014
- https://doi.org/10.1016/j.jcta.2025.106075

### Residual risks

- Equivalent recursive constructions may exist under compound-type or distributing-hash terminology, but the primary predecessor and later broad SHF searches did not locate one.

## Value — PASS

The theorem fills an explicit structural gap in a standard recursive construction: for arbitrary separating type it lowers every required auxiliary residual from total strength \(W\) to \(W-2\), recovers known special cases, and yields concrete small-row auxiliaries such as the logarithmic type \(\{1,1,2\}\) case. This is a motivated construction lemma rather than an arbitrary parameter tweak.

### Value sources

- Zaverucha thesis Section 3.1.2
- Martirosyan-van Trung 2008

### Value risks

- The weaker residual requirement does not guarantee a numerical row-count improvement for every parameter set.

## Limitations

- The theorem weakens the auxiliary separation requirement but does not guarantee fewer rows in every parameter regime.
- A vertical stack for several residual types may be nonoptimal.
- The frameproof lifting is a corollary; the principal contribution is the arbitrary-type pair-residual construction.
