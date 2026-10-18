# Independent mathematical audit

## correctness

PASS

The six explicit W(E6) simple-reflection permutations in Shimada Eq.(2.5) generate a group of exact order 51840 on 27 marked lines. Independent SymPy Schreier–Sims enumeration exhausted all 51840 elements for S1={1,2,3,4,5}, S2={1,2,3,4,21}, T1={1,2,3,4,5,27}, T2={1,2,3,4,21,26}. Setwise stabilizer sizes are 120,240,120,120 and pointwise kernel sizes 1,2,1,1, consistent with orbit sizes 432,216,432,432. The marked image in each case is full S5. In S2 its kernel is the involution sigma6 from printed sixth generator, checked central; derived subgroup has order60 and adjoining explicit tau=(1 4)(7 13)(8 16)(10 19)(11 20)(22 25) gives an order120 complement intersecting kernel trivially, so group = C2×S5. Other groups faithful S5. Exact complete finite group calculation, not heuristic sampling; independent rerun was performed, not blind trust in VERIFY_OK.

## originality

PASS

Shimada primary Zariski pairs on cubic surfaces fully identifies four orbit representatives and orbit cardinalities; these imply group stabilizer orders but not the kernel/image structure or the splitting C2×S5 vs a nonsplit central extension. The linked primary calculation data logs orbits, not this classification. Classical 27-line and Weyl groups may encode isomorphic subgroups, but targeted semantic searches yielded no four-case concrete hidden-kernel theorem. Best-of-knowledge PASS with classical subgroup literature risk.

## value

PASS

For the two natural Zariski-pair arrangements, a complete finite monodromy-isotropy classification explains the factor-two difference between the five-line orbit sizes by an invisible central Weyl involution fixing all marked lines. This is an exact natural orbit invariant tied to deformation geometry; not claimed as projective automorphisms of a fixed cubic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
