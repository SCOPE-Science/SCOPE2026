# Independent mathematical audit

## correctness

PASS

The general cubic cut-edge count for a locating-total dominating set S in a 2n-vertex cubic prism gives 2(2n-|S|)-|S| <= E_cross <= 2|S|, so |S| >= ceil(4n/5). The explicit cyclic column-mask word B Q^t with B=(3,1,0,3,0,3,0,0), Q=(3,0,3,0,0), n=8+5t has 7+4t selected vertices. Identical nonempty outside fingerprints can only come from same-rail distance-two or opposite-rail neighboring columns: the five-column locality lemma checks these collisions and total domination. Exactly ten five-column factors occur; checking B,BQ,BQQ covers every possible within-block/interface window, because each window length 5 is no longer than each repeated block. This proves n>=8 throughout the n=3 mod 5 progression, not by finite extrapolation. Independent implementation checked ten factors, direct prisms for t=0..17, and absence of any size-six solution at n=8.

## originality

PASS

Bounded best-of-knowledge scientific comparison: The 2021 conjecture is contradicted by 7+4t, so cannot itself establish it. Earlier bounds for residues 0,2,4 mod 5 neither cover n=3 mod5 nor imply the constructed word BQ^t. Ordinary domination of prisms is an inequivalent invariant. The targeted Resultary query and primary works were compared on objects, hypotheses, implication and parameters, not simply titles. No decisive prior-coverage theorem identified; this is not a proof of historical priority.

## value

PASS

This constructs an explicit infinite family of optimal locating-total dominating sets that refutes the n congruent 3 mod 5 branch of a concrete 2021 prism conjecture. It identifies a sharp natural domination invariant on an infinite vertex-transitive-by-layers graph family, with an independent matching lower bound and reproducible finite local certificate; not an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
