# Independent mathematical audit

## correctness

PASS

This decision assesses the repaired equality classification. The known optimum 10 and the known obstruction system also replay correctly. For each pair x,y, the full set of words in its box other than x is a same-descendant coalition exactly if each differing coordinate has some alternative word in the box carrying x's symbol there; y already supplies all other required symbols. Checking the same criterion for y gives an exact test for both endpoints. Singletons cannot fail. I implemented that test independently of the frozen forbidden-hypergraph search, exhaustively enumerated normalized codes containing 000, and confirmed 20 valid ten-word codes and no larger ones. Pruning only drops invalid partial sets and branches with too few words left to reach the target. Every label class has a normalization at some codeword. The full group orbit of the stated representative has 54 elements, and its slice containing 000 equals the whole independently enumerated normalized census. This proves completeness and yields stabilizer 1296/54=24. The profile counts are invariant under the group and correct on the representative. The independent method also recovered 891 minimal bad sets of size four; that auxiliary count is not a new assertion in the repair.

## originality

PASS

For the original novelty claim, the exact maximum and 891 minimal four-word obstructions are demonstrably covered by distinct Resultary record fc51dbba75e2; they are not accepted as new. Its witness belongs to the verified orbit, but the record does not establish that every optimum belongs to this orbit and explicitly disclaims such a classification. The repaired claim credits the known facts and asserts only the complete equality census and its structural consequences. No compared source gives or implies that remainder.

## value

PASS

The known size and example alone would not qualify as a new exact result. The repaired claim answers a distinct question about the geometry of all extremizers: whether multiple inequivalent structures occur at the natural first ternary parameter of the length-three strong-separability problem. It gives a complete equality census, reduces all maxima to one representative, and gives invariants valid for any maximum. That is useful independently of producing an improved size bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
