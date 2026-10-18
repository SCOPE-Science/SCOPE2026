# Independent mathematical audit

## correctness

PASS

For 6 cyclic bit positions, pair-distance<4 iff any two distinct words differ only within some two adjacent coordinates; therefore the six 4-coordinate puncturings are injective exactly for d_pair>=4. With 16 words each puncturing is bijective; Singleton bound |C|<=16 follows. Each of 64 candidate words covers one column for each of six puncturings; an admissible C is precisely an exact cover of the 96 (index, remaining4-bit value) columns using 16 word-rows. Inspected finite algorithm: minimum-size uncovered-column recursion branches through all compatible rows, no exact cover skipped; independent locally implemented it, reproducing exactly 685 recursion nodes, 76 distinct 16-sets, 44 XOR-affine and 32 nonaffine. Independently enumerated bit translations and 12 dihedral coordinate permutations: five disjoint orbit sizes 4,32,24,12,4 with identical five lexicographically least representatives to source. The independent C++ 16-clique enumeration, whose monotone candidates ensure uniqueness, visits 391978 nodes. This is a genuine exhaustive finite proof at n=6 only, not extrapolated beyond it.

## originality

PASS

Chee et al arXiv:1211.1728 establish Singleton-type bound and existence of binary MDS pair codes of even length with d_pair=4, so those aspects are prior. Ding et al arXiv:1605.08859 emphasize constructions of linear MDS codes, not unconstrained 16-word sets. Resultary nearest exact-census source treats length FIVE, with 20 affine codes; this is length SIX and first nonaffine orbit, 76 labeled sets. No located source gives this precise complete nonlinear census, affine breakdown and full translation-dihedral orbits; priority remains best-of-knowledge.

## value

PASS

All equality cases at the smallest even length beyond the fully affine n=5 classification are intrinsically useful in symbol-pair coding: 32 of 76 maximal codebooks are not affine, disproving an affine-only expectation, and the five metric-isometry orbits are a complete moduli inventory. A natural finite optimum enumeration, not arbitrary sampled strings; no larger-n generalization is required for value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
