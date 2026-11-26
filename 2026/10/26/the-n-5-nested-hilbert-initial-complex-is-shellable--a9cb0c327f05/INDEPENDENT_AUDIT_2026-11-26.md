# Independent mathematical audit

## correctness

PASS

A facet is precisely the complement of an inclusion-minimal transversal of the 14 given monomial supports on 30 vertices. Independent enumeration used an unrestricted minimal-transversal recursion, so it could detect larger minimal covers; it agreed with the separate exhaustive check of all 27,405 four-subsets and returned 130 covers, all of size four. The frozen JSON contains each exactly once. For every earlier/current facet pair the independent checker found an earlier facet whose intersection with the current facet is a ridge containing the given pair intersection (8,385 pairs). This makes the intersection with the preceding union pure of codimension one at each step. Pure shellability gives Cohen–Macaulayness over any field. This proves the finite case only. Replay: python3 -B /workspace/branches/9c130b87-3191-42d6-8492-c3876e4e7ba6/independent_n5_check.py; output in independent_n5_check_output.txt in the same directory. The frozen verifier was not used to generate independent evidence.

## originality

PASS

Credit the explicit n=5 shelling and its consequence in arbitrary characteristic, not the known purity or count. The primary paper asks for shellability of exactly this complex, and the bounded comparisons found no shelling of the same complex or stronger covering result.

## value

PASS

This exact finite witness answers the published shellability question at the explicitly displayed n=5 example of the same natural family. It proves the field-independent CM consequence there and provides a reproducible comparison point for general shelling strategies. The value is the structural shelling, not re-counting known facets or extrapolating from one n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
