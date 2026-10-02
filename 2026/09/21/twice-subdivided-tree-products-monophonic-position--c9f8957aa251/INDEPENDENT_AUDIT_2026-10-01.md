# Independent audit — 2026-10-01

## Final claim

For any two nontrivial finite trees \(T_1,T_2\), the Cartesian product of their twice-subdivisions has monophonic position number exactly two; likewise \(P_m\square S_2(T)\) has value two for \(m\ge4\).

## Correctness — PASS

The full proof of Theorem 3.18 in the primary product paper establishes that any maximum monophonic-position set of size at least three in connected triangle-free factors must be layered over a leaf and that its projection consists of pairwise distance-two vertices. In a tree, three pairwise distance-two vertices share one common neighbor. In a twice-subdivided tree, such a common neighbor of three projected vertices is an original branch vertex with three length-three arms, while a leaf of the other factor has a length-three inward chain. The displayed 19-vertex product path is then induced and contains any selected projected triple, contradicting monophonic position. The asymmetric path-factor corollary follows by the same obstruction or by impossibility of three pairwise distance-two vertices in a path. The package verifier checks the local path construction on 1872 bounded instances but is not used as an infinite proof.

Checked sources:
- Chandran, Klavžar, Neethu and Tuite, Computational and Applied Mathematics 46, article 44 (2027), published online 11 September 2026; open full text, Theorems 3.16 and 3.18 inspected.
- Thomas, Chandran, Tuite and Di Stefano, Discrete Applied Mathematics 354 (2024); monophonic-position foundations.
- Resultary semantic query for twice-subdivided tree Cartesian products and monophonic position; assigned finding was the exact hit.
- Package obstruction verifier: 13 base trees, 169 ordered pairs, 1872 oriented local obstructions.

Residual risks:
- None.

## Originality — PASS

Best-of-knowledge originality passes. The very recent primary product paper supplies the layered/pairwise-distance-two structure and a maximum-degree upper bound, but it does not state the twice-subdivision collapse theorem; indeed its star-by-star example shows the same upper bound can be tight. No stronger Resultary finding or exact tree-subdivision specialization was located.

### Equivalent formulations

Searches:
- Resultary query: monophonic position Cartesian product twice subdivided trees exact two induced path
- Chandran--Klavžar--Neethu--Tuite Theorem 3.18

Evidence:
- The assigned record is the exact Resultary hit.
- Theorem 3.18 gives only \(\operatorname{mp}(G\square H)\le\max\{2,\sigma(G)\Delta(H),\sigma(H)\Delta(G)\}\) for triangle-free factors.

Reasoning: The audited theorem is an exact collapse family extracted by combining the source structure with a new induced-path obstruction, not a renamed source bound.

### Broader coverage

Searches:
- Theorems 3.16 and 3.18 of the 2026 product paper
- Star-by-star sharpness example in that paper

Evidence:
- The source treats arbitrary Cartesian products and gives upper bounds.
- Its star products can have large monophonic position, so the new twice-subdivision phenomenon is not forced by the broad theorem alone.

Reasoning: No inspected broader theorem determines the exact value two for all twice-subdivided tree pairs.

### Exact database or table

Searches:
- Resultary exact-topic search
- Bounded obstruction census in the package

Evidence:
- No prior parameter table/classification for subdivided-tree products was located.
- The finite census validates the explicit obstruction only.

Reasoning: There is no known table whose recomputation would make the result routine; the theorem is an infinite structural family.

### Claim versus prior implication

Searches:
- Primary pairwise-distance-two structure versus explicit 19-vertex obstruction

Evidence:
- Theorem 3.18 stops after converting the projection geometry into a maximum-degree bound.
- The new argument uses the length-three subdivision arms in both factors to build an induced path through an arbitrary triple.

Reasoning: The exact collapse is not a mechanical numerical specialization of the source bound; it requires a new structural obstruction exploiting subdivision depth.

### Source inspections

- **Monophonic position sets of Cartesian and lexicographic products of graphs** (https://doi.org/10.1007/s40314-026-03901-3): trigger — Immediate primary source for the Cartesian-product structure used in the proof; material read — Open full text of the Cartesian-product section, including Theorems 3.16 and 3.18 and the complete proof of Theorem 3.18; method — Primary full-text inspection; assessment — Supplies the structural reduction but not the twice-subdivision theorem.; evidence — The proof shows the layered-over-a-leaf and pairwise-distance-two projection properties; the stated conclusion remains a maximum-degree upper bound.

Checked sources:
- Chandran, Klavžar, Neethu and Tuite, Computational and Applied Mathematics 46, article 44 (2027), published online 11 September 2026; open full text, Theorems 3.16 and 3.18 inspected.
- Thomas, Chandran, Tuite and Di Stefano, Discrete Applied Mathematics 354 (2024); monophonic-position foundations.
- Resultary semantic query for twice-subdivided tree Cartesian products and monophonic position; assigned finding was the exact hit.
- Package obstruction verifier: 13 base trees, 169 ordered pairs, 1872 oriented local obstructions.

Residual risks:
- The product paper is extremely recent; differently indexed contemporaneous follow-up work remains a residual priority risk.
- The theorem is a sufficient infinite family, not a classification of all tree products with monophonic position two.

## Scientific value — PASS

The result gives a broad exact family parameterized by arbitrary tree pairs and demonstrates arbitrarily large slack in the current triangle-free maximum-degree bound despite both factors having leaves. The subdivision obstruction is a natural structural phenomenon likely useful in sharpening product bounds, not an arbitrary finite slice.

Checked sources:
- Chandran, Klavžar, Neethu and Tuite, Computational and Applied Mathematics 46, article 44 (2027), published online 11 September 2026; open full text, Theorems 3.16 and 3.18 inspected.
- Thomas, Chandran, Tuite and Di Stefano, Discrete Applied Mathematics 354 (2024); monophonic-position foundations.
- Resultary semantic query for twice-subdivided tree Cartesian products and monophonic position; assigned finding was the exact hit.
- Package obstruction verifier: 13 base trees, 169 ordered pairs, 1872 oriented local obstructions.

Residual risks:
- The product paper is extremely recent; differently indexed contemporaneous follow-up work remains a residual priority risk.
- The theorem is a sufficient infinite family, not a classification of all tree products with monophonic position two.

## Conclusion

The unchanged final claim passes correctness, best-of-knowledge originality, and scientific value.
