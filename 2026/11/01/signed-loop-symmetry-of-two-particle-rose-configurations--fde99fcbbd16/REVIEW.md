# Scientific review: signed-loop symmetry of two-particle rose configurations

## Correctness — PASS

The claim is one full rational signed-petal character for every integer \(m\ge2\), together with the integral one-skeleton collapse and two invariant dimensions as consequences. The complete unordered cubical cell census \(c_0=m(2m+1)\), \(c_1=3m(2m-1)\), \(c_2=5\binom m2\) is supported by explicit cells. Two elementary-collapse families remove all squares, leaving a connected graph of first Betti number \(1+3\binom m2\). For every orientation-preserving or -reversing petal symmetry, counting fixed cells with edge and square orientations yields the exact Lefschetz character and, by group averages, invariant dimensions two and zero. The attached standalone program exhausts 4,282 symmetries through five petals and rechecks every listed collapse, but the unlimited theorem follows from the symbolic enumeration in `RESULT.md`, not from extrapolation.

## Originality — PASS, qualified

The closest foundations are Ghrist, arXiv:math/9905023 (homological dimension bounds); Farley–Sabalka, arXiv:math/0410539 (cubical models); Chettih–Lütgehetmann, arXiv:1612.08290 (ordered configurations on trees with loops); and Maciążek–Sawicki, arXiv:1606.03414 (homology calculations on one-connected graphs). None of their inspected relevant assertions gives the complete signed-petal class function for ordinary first homology of the unordered two-particle rose. Lütgehetmann, arXiv:1701.03490 (representation stability), and Gadish–Hainaut, arXiv:2202.12494 (compactly supported ordered-configurations) concern distinct functors or incomplete symmetry descriptions. Searches of alternative names, full signed permutations, Borel–Moore objects, and potentially stronger coverage did not locate an implication that eliminates this computation. The last paper's full coverage and potentially unindexed mathematics remain residual risks; no absolute uniqueness is asserted.

## Value — PASS

The rose gives the basic cyclic graph with one essential vertex, where the two-particle configuration space describes graph-braid motions. The all-petal class character is more informative than the known Betti number and isolates a structural effect: the \(S_m\)-fixed rational first homology has dimension two while the \(B_m\)-fixed part vanishes. A uniform explicit character of a natural graph-automorphism group is not a routine reparametrization of ranks or an arbitrary finite slice.

## Limitations

Only two distinct unordered particles, rational symmetry characters, and the ordinary homotopy type are covered. No integral representation-lattice splitting, higher-particle assertion, or independent expert confirmation is included. See `RESULT.md`, `AUDIT.json`, and `VERIFICATION.md` for the claim-to-evidence proof and finite checks.

Self-review: passed. Independent audit: not yet performed.
