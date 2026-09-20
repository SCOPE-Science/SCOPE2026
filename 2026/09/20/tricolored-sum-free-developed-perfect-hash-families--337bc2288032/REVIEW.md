# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The forward construction was checked symbolically. Tri-colored sum-freeness forces each coordinate list to be injective. Consequently any two distinct developed columns collide in at most one row. If three columns were unseparated, the three row-collisions must use the three different pairs; eliminating the translation parameters produces an off-diagonal equation x_i+y_j+z_k=0, contradicting tri-colored sum-freeness.

For the converse, diagonal translation invariance gives a unique normalized representative (0,r_i,s_i) for each orbit. The PHF property plus the availability of every translate rules out repetition in any of the three derived coordinates (-s_i,r_i,s_i-r_i). Any all-distinct off-diagonal zero-sum relation then explicitly constructs three unseparated columns, while a relation with exactly two equal indices would force a repeated derived coordinate. Hence the orbit seeds are tri-colored sum-free.

The asymptotic corollary is a direct substitution of the known tri-colored sum-free upper and lower bounds into the exact identity D_G=|G|M_3(G). The finite-field specialization was independently checked by the included script: GF(81) is constructed from x^4-x-1, the fourth-power subgroup has 20 elements and no nontrivial zero-sum triple, the developed array has 1620 columns, no column pair collides in two rows, and the collision graph contains no bad three-column triangle.

## Originality — PASS, to the best of our knowledge

The closest older construction located is Walker–Colbourn (2007), which develops progression-free subsets of the cyclic group Z_v. The present theorem recovers that construction as the diagonal tri-colored special case and enlarges the seed object to arbitrary tri-colored sum-free sets in any finite abelian group. Searches for combinations of “tri-colored/tricolored sum-free”, “perfect hash family”, “translation-invariant”, “group-developed”, “induced matching”, and “3-dimensional matching” did not locate a source stating this correspondence.

Shangguan–Ge (2016) is a particularly important neighboring source: it connects perfect hash families with hypergraph Turan problems and additive solution-free sets, and its later generalization by Wei–Zhang–Ge (2025) constructs columns (y+b_1m,...,y+b_tm) from one-dimensional solution-free sets. These results materially reduce the novelty margin, because they show that additive-hypergraph formulations of PHFs are established prior art. However, the inspected statements do not identify arbitrary diagonal-translation orbit families with tri-colored sum-free sets, nor do they derive the exact developed-class capacity |G|M_3(G) and its fixed-characteristic exponent from tri-colored sum-free theory.

The online historical PHF tables cited by later work could not be inspected. That access limitation can affect any claim that PHF(3;1620,81,3) is a record, so no such claim is made. It does not directly threaten the structural equivalence theorem. A residual originality risk remains that the same equivalence appears under different terminology in literature on group-developed triple systems or induced matchings.

## Value — PASS

The correspondence is not just a construction: it exactly characterizes a natural symmetry class of three-row PHFs. It transfers both upper and lower results from tri-colored sum-free theory, yielding the exact exponential growth rate of the developed subclass over F_p^n. Combined with the known unrestricted q^{2-o(1)} behavior, it also gives an impossibility statement: full diagonal translation symmetry is asymptotically too restrictive to attain the unrestricted scale in fixed characteristic.

The F_81 corollary supplies a concrete reusable instance, PHF(3;1620,81,3), and exceeds the 1296-column v=81 construction explicitly reported by Walker–Colbourn. The finite instance is secondary to the structural theorem and is deliberately not presented as a global current record.

## Scientific limitations

The theorem is specific to N=t=3 and diagonal translation symmetry. Higher-strength analogues would require a different multi-colored additive condition. The asymptotic exponent is for the structured developed subclass, not for all PHFs. Current PHF parameter tables were not fully accessible, so finite-record status remains unresolved. Originality is therefore stated only to the best of our knowledge.
