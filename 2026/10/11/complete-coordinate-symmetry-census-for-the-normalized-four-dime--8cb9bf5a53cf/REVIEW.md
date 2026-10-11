# Same-model review

## Correctness

PASS. The proof reduces a \(\Gamma\)-invariant assignment to one parity-constrained permutation per \(\Gamma\)-orbit of outer blocks, centralizing the point stabilizer. This gives an exact product formula for every subgroup of \(S_4\). A three-cycle fixes a weight-one outer block but has an all-even centralizer, proving the structural zero. Burnside's lemma gives the full coordinate-relabeling quotient, and descending subgroup-lattice subtraction gives exact stabilizers. The bundled checker regenerates all \(30\) subgroups of \(S_4\) and reproduces every number independently of a stored subgroup table.

## Originality

PASS. The primary source reports only selected structured symmetry families and its public search program evaluates one supplied subgroup at a time. The inspected paper explicitly leaves broader subgroup-based symmetry reduction unfinished. Searches for the source identifier, frame-assignment terminology, conjugation action, Burnside quotient, and the exact family-size fingerprints found no complete census or three-cycle obstruction.

## Value

PASS. The four-dimensional problem has an enormous finite candidate space, and the source specifically identifies symmetry as a useful search reduction. The result completes the normalized coordinate-symmetry census, shows that all three-cycle symmetry is impossible before any expensive geometric closure test, and gives the exact number of inequivalent symmetric candidates remaining. It is a structural search-pruning classification, not merely a recomputation of one table row.

Same-model review: passed. Independent audit: not yet performed.

## Closest literature and limitations

The closest source is Kamenetsky, arXiv:2610.00916v1, together with its `symsearch4.py` implementation. Its structured counts \(32\), \(768\), and \(6912\) are recovered exactly, but the source does not give the full subgroup table, Burnside orbit count, or exact stabilizer strata.

A separate three-dimensional Chair44 symmetry-phase theorem concerns symmetries of completed tilings, not candidate four-dimensional frame assignments.

The theorem is confined to the normalized search slice used by the source's symmetry program. It does not decide coarsening closure for the remaining candidates and does not solve the full unnormalized \(12^{15}\) open problem.
