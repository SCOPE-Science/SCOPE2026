# Review

## Correctness
PASS.  The claim is scoped to the source's \(128\)-map Theorem 4.5 family and fixed information set.  The lower bound uses a necessary subset of the \(2\)-PD requirements: the \(64\) vertical coordinate pairs.  Exactly three vertical fibers are wholly check fibers, so a map with first-coordinate translation \(a\) covers exactly the three vertical fibers indexed by \(a+T\), where \(T\) is a three-point subset of a four-element \(\mathbb F_2\)-subspace.  The \(16\) affine cosets therefore force at least two distinct translations each, hence at least \(32\) maps.  The included exact verifier reconstructs the source point set and information/check split and confirms that the explicit \(32\)-map witness covers all \(8128\) unordered coordinate pairs.

## Originality
PASS.  The primary source gives a \(128\)-element partial \(2\)-PD family and explicitly names smaller PD sets as future work, but it does not state a smaller subfamily or an optimum for Example 4.6.  Searches by source identifier, code parameter, curve equation, PD-set terminology, vertical-fiber language, and exact candidate size found no statement equivalent to the \(32\)-map minimum.  The earlier Hermitian/norm-trace paper supplies related automorphism-derived PD sets, and design-code literature supplies examples of shrinking large PD sets, but neither implies this exact code-specific incidence bound or witness.

## Value
PASS.  PD-set cardinality enters the number of automorphisms/syndrome tests in permutation decoding, so reducing the source's only fully explicit arbitrary-two-position example from \(128\) maps to the exact optimum \(32\) directly sharpens the decoding workload within the proposed method.  The result also identifies the geometric obstruction responsible for the optimum: three-point translates inside \(16\) affine four-point fiber blocks.  This is a natural complete optimization of the source construction, not an arbitrary finite slice.

## Closest literature and limitations
Castellanos--Tizziotti--Olaya-León is the same-object source and is the closest comparison; it proves coverage by all \(128\) maps but leaves smaller PD sets open.  Lichtenwalner--López--Matthews--Seneviratne proves analogous PD-set constructions for Hermitian and norm-trace codes, including a Hermitian \(2\)-PD set of size \(q(q^2-1)\), but does not cover this generalized-Hermitian example or its fixed source information set.  Crnković--Mostarac shows that smaller PD sets can sometimes be extracted from larger automorphism-derived sets for design codes, establishing that the broad optimization idea is prior art while leaving this exact statement untouched.

The minimum is not asserted over the entire permutation automorphism group or over alternative information sets, and absolute novelty cannot be guaranteed against unindexed material.

Self-review: passed. Independent audit: not yet performed.
