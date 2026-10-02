# Independent scientific audit — SCOPE-20260930-73eb54babf15

Audited at: 2026-10-02T00:16:07.579488Z

Disposition: **passed**

## Correctness — PASS

For a tuple \(a\), evaluation from the free \(n\)-generated distributive lattice \(F_n\) onto the generated finite sublattice has a kernel congruence. Equal kernels give an isomorphism of the generated sublattices preserving each coordinate, which ultrahomogeneity extends to an automorphism; every congruence is realized because its finite quotient embeds into the Fraïssé limit. For finite distributive \(L\), congruences are in bijection with subsets of \(J(L)\). In the binary lattice language, \(J(F_n)\) consists exactly of the meet monomials indexed by nonempty proper subsets of \([n]\), so \(|J(F_n)|=2^n-2\). Hence the ordered \(n\)-tuple orbit count is \(2^{2^n-2}\), including the edge case \(n=1\).

### Correctness sources

- assigned RESULT.md
- assigned verify.py
- Kechris–Sokić, DOI:10.4064/fm218-1-4
- finite Birkhoff representation/congruence theory

### Correctness risks

- The finite checker reaches only small ranks; it is not used as proof of the general congruence count.

## Originality — PASS

The primary random-distributive-lattice paper establishes the Fraïssé setting and studies automorphism-group dynamics, but the inspected full text does not state the tuple-kernel classification or the exact orbit count. Standard finite distributive-lattice duality supplies the congruence count once the orbit-kernel identification is made; no earlier exact formula was located.

### Equivalent formulations

No equivalent oligomorphic-profile formula was located.

Searches:
- published-corpus query: random distributive lattice ordered tuple orbits automorphism congruence free distributive lattice \(2^{2^n-2}\)
- literature query: random distributive lattice orbit count tuple congruence kernel

Evidence:
- The precise corpus query returned the assigned theorem as the exact hit and no earlier equivalent result.
- The primary dynamical paper does not state the orbit-count formula in its inspected full text.

### Broader coverage

The two ingredients do not by themselves state the tuple-orbit classification; the audited argument connects a tuple's generated sublattice to a free-algebra congruence and realizes every congruence.

Searches:
- Kechris–Sokić, DOI:10.4064/fm218-1-4
- Grätzer, General Lattice Theory

Evidence:
- Kechris–Sokić cover the Fraïssé limit and automorphism-group dynamics; classical lattice theory covers finite distributive representation and congruences.

### Exact database or table

The theorem is an exact all-\(n\) classification, not a finite table extrapolation.

Searches:
- published-corpus exact query on \(2^{2^n-2}\) with random distributive lattice

Evidence:
- No earlier orbit-growth table or database record with this formula was located.

### Claim versus prior implication

The audited kernel-realization step is necessary to combine the two prior ingredients and yields the exact oligomorphic invariant.

Searches:
- full-text comparison with Kechris–Sokić's Fraïssé/ultrahomogeneity statements and standard finite Birkhoff duality

Evidence:
- Ultrahomogeneity alone does not count tuple types; Birkhoff duality alone does not identify those types with \(\operatorname{Con}(F_n)\).

### Sources inspected

- **Dynamical properties of the automorphism groups of the random poset and random distributive lattice** — https://doi.org/10.4064/fm218-1-4. Trigger: Primary paper defining the same random distributive lattice and automorphism group. Material read: Full accessible PDF sections defining the Fraïssé class/language, ultrahomogeneity, and the paper's automorphism-group dynamical results. Method: Lawful open full text with page-level inspection. Assessment: NOT_COVERING. Evidence: The inspected article establishes the random distributive lattice in the binary lattice language but does not give the ordered-tuple congruence classification or \(2^{2^n-2}\) orbit count.
- **General Lattice Theory** — Grätzer, 1998. Trigger: Standard source for the finite distributive-lattice ingredient. Material read: Relevant finite Birkhoff-representation and congruence facts. Method: Standard monograph theorem inspection. Assessment: COVERING_INGREDIENT. Evidence: It supplies classical lattice theory, not the random-structure tuple-orbit theorem.

### Checked sources

- https://doi.org/10.4064/fm218-1-4
- Grätzer, General Lattice Theory
- published-result corpus search

### Residual risks

- An explicit model-theoretic orbit-profile computation could exist in an unindexed source, but none was found after checking the primary random-lattice paper and exact-formula searches.

## Value — PASS

The theorem computes the complete ordered-tuple orbit profile of a canonical oligomorphic automorphism group and gives a canonical classification by free-algebra congruences. This is a natural exact invariant useful for subsequent model-theoretic and permutation-group work.

### Value sources

- Kechris–Sokić, DOI:10.4064/fm218-1-4
- classical finite distributive-lattice theory

### Value risks

- The result is specific to the pure binary lattice language; naming bounds changes the free algebra and orbit profile.

## Limitations

- The language contains only the binary operations \(\wedge,\vee\), with no named bounds.
- The claim concerns ordered tuples with repetitions allowed.
- The theorem does not classify unordered finite subsets or stabilizer isomorphism types.
