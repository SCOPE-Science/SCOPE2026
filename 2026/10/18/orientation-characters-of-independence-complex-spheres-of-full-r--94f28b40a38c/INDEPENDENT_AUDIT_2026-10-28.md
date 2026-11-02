# Independent mathematical audit

## correctness

PASS

For b>=2 and h>=0, the exact signed-root recurrence A_0=1,B_0=-1, A_{k+1}=(A_k+B_k)^b, B_{k+1}=-A_k^b has period 3 for even b and 6 for odd b, and Z=A+B vanishes exactly at h divisible by 3. Ehrenborg--Hetyei Corollary 6.1 supplies the forest contractible-or-single-sphere dichotomy, hence the nonzero signed sum forces one sphere. The selected levels P={depth h-1-3j>=0} dominate the rooted tree; one child q(v) per selected vertex has mutually disjoint closed neighborhoods, giving gamma=|P|. Marietti--Testa gives dimension gamma-1. For any automorphism g, the signed fixed-face Hopf trace equals -Z_g where each invariant independent orbit contributes (-1) per vertex cycle, so the degree of g on the unique integral homology group is Z_g/Z_identity. Local child swaps produce the quotient tree with b-1 branches at the swapped vertex. Their root-state pair is multiplied by lambda=-1 exactly for even b, t=h-j congruent 2 mod3, or odd b, t congruent 2,3,4 mod6; otherwise +1. The same lambda is the sign of the two permuted P-blocks, exponent N=sum_{h-1-3a>j} b^(h-1-3a-j-1). Such swaps generate the full root-preserving automorphism group, proving every character value. Boundaries: h=0 is a point, h=1 has trivial action on reduced H_0, h divisible3 is contractible, h>=2 nondivisible3 has a negative generator. Independently enumerated actual invariant independent sets by vertex-orbit cycles for seven (b,h) cases (including 21 local swaps and contractible h=3), independently checked graph domination numbers for five small spherical cases, and checked 6084 local state/selected-block parity identities for 2<=b<=13 and h<40. Finite tests corroborate, not prove, the general argument.

## originality

PASS

Best-of-knowledge novelty holds for the full rank-one integral orientation character of the rooted automorphism group on Ind(T_{b,h}), not for the nonequivariant sphere/contractible pattern or dimension. Theorem 5.6 of Deshpande--Singh is directly applicable at r=1 and provides stronger higher-independence homotopy coverage, but no canonical rooted automorphism character. Ehrenborg--Hetyei and Marietti--Testa address general forests, likewise with nonequivariant conclusions. An equivalence Ind(T)≃S^d does not specify whether an automorphism acts by +1 or -1 on its integral top homology. Targeted Resultary searches, published SCOPE repository code search and broad external literature searches located no covering orientation-character theorem. This is a qualified assessment, not proof of historical priority. Kawamura full text remained inaccessible; an unindexed equivariant result remains possible.

## value

PASS

The complete b-ary rooted tree is a standard natural infinite graph family with a canonical large iterated-wreath-product symmetry group. Its independence complex is a single sphere or contractible by earlier topology, but the exact integral homology action is extra information a researcher studying symmetry-sensitive topology would need. The sign formula for every rooted automorphism has nontrivial cases for every spherical h>=2, gives a clear generator criterion, and distinguishes automorphisms invisible to Betti ranks. It is an exact uniform natural representation invariant, not a one-off computation, routine restatement of sphere dimensions, or an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
