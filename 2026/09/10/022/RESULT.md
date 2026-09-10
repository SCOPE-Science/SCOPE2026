# Named-family sail-Ramsey threshold 15 -> 19 for Steiner triple systems

## Context

The sail (fan) S with blocks 123, 345, 561, 147 is the unique undecided
unavoidable <=4-block Ramsey case in the Gyarfas-Sarkozy linear-triple-systems
program: Granath et al. (JCD 2018) leave exactly the sail C15 undecided, and
Sarkozy II (Discrete Math 2023) poses sail t-Ramsey as open Problem 1.3,
proving only the one-sail asymmetric theorem (S,C,...,C).
Whether the sail is 2-Ramsey (every 2-coloring of every large STS(n) yields a
monochromatic sail) remains open, as does the preset fallback (S,S,W) 3-Ramsey
with explicit N0. This record reports the strongest self-contained fragment
actually established: an exact finite-order threshold on named systems.

## Definitions

- Sail S: 4 blocks on 7 vertices, up to isomorphism 123, 345, 561, 147.
  Vertex 1 (center) has degree 3; blocks through the center are
  123, 345, 561 and the closing block 147 is a transversal picking one
  private vertex from each through-block.
- Triangle T = {123, 345, 561} with closing pairs 14, 36, 52.
- STS(n): Steiner triple system of order n (n = 1,3 mod 6): n(n-1)/6 triples,
  every pair in exactly one block.
- Monochromatic sail in a red-blue block-coloring: a sail all of whose 4
  blocks share one color. Sail-free coloring: no monochromatic sail in either
  color. NAE-4-SAT encoding: for each sail {a,b,c,d}, clauses
  (a v b v c v d) (not all blue) and (~a v ~b v ~c v ~d) (not all red).
- Named systems: STS(7) Fano plane (0-indexed list in DRAFT);
  STS(9) = AG(2,3); STS(13) cyclic mod 13 from bases (0,1,4),(0,2,7);
  STS(15) = point-line design of PG(3,2); STS(19) cyclic mod 19 from bases
  (0,1,4),(0,2,9),(0,5,11).

## Result

Theorem 1 (sail census, dual-enumerator). The named systems contain
respectively 28, 72, 260, 420, 912 sails. Two independent enumerators agree
on every system: (A) center/trio/transversal scan; (B) 4-subset isomorphism
test (7 vertices, degree profile 3,2,2,2,1,1,1, center with 3 through-blocks
plus a transversal closing block).

Theorem 2 (sail-free witnesses to order 15). Each of STS(7), STS(9),
STS(13), STS(15) as defined above admits a sail-free 2-coloring. Witnesses
are archived in output/artifacts/sail_smallsts.json (orders 7/9/13) and
output/artifacts/sail_target_part2.json (key STS15_seed7_witness), with
red/blue splits 3/4, 9/3, 13/13, 15/20 and 0 monochromatic sails each.

Theorem 3 (named cyclic STS(19) is sail-Ramsey). Every red-blue coloring of
the named cyclic STS(19) (57 blocks) contains a monochromatic sail. The
forcing certificate is a closed DPLL refutation of the 912-sail NAE-4-SAT
instance (57 variables, 1824 clauses; 276 nodes, 552 decisions,
277 conflicts, 5251 unit propagations) with an independent trace replay
checker; archived trace output/artifacts/sts19_unsat_trace.json (6632
entries) satisfies the closed-binary-tree identity
conflicts = decisions/2 + 1 (277 = 276 + 1).

Lemma 1 (closing-pair automaticity). With T and closing pairs as above, none
of the closing pairs is covered by T, and for every closing pair and every w
in T distinct from its endpoints, w spans a T-covered pair with some
endpoint (exhaustive 3x6 check). Hence in an STS each closing pair lies in a
unique block whose third vertex is automatically outside T; a monochromatic
triangle plus a same-color closing block is a monochromatic sail, and in a
sail-free 2-coloring every monochromatic triangle has all three closing
blocks in the opposite color.

Proposition 2 (symmetric density obstruction). The Latin-square construction
(V = X u Y u Z, |X|=|Y|=|Z|=m, blocks (x,y,x+y)) is linear with m^2 = n^2/9
blocks and zero sails. Since STS(n) has n(n-1)/6 blocks, a balanced
2-coloring gives each class ~n^2/12 < n^2/9: neither class exceeds the sail
extremal number. Thus the one-sail asymmetric majority-counting proof has no
symmetric analogue (2*(1/9) > 1/6); density alone cannot force a
monochromatic sail.

## Proof / evidence

Stdlib Python 3 only. From the record root:

```
python3 output/artifacts/verify_all.py
```

Expected output ends with VERIFY_ALL_OK, including: STS axiom checks (pair
counts 21/36/78/105/171) and difference-cover check for STS(19);
dual-enumerator agreement (28/72/260/420/912); witness block-set equality
(symdiff 0) and mono = 0 for orders 7/9/13/15; clause-set equality
(1824 clauses); trace replay with the closed-tree identity. The auditor
independently re-executed this verifier (VERIFY_ALL_OK) and additionally
re-solved the STS(19) NAE instance from scratch with a different DPLL
heuristic, also obtaining UNSAT.

## Limitations

- Does NOT decide the full sail 2-Ramsey claim over all STS(n), n >= n0.
- Does NOT prove the (S,S,W) 3-Ramsey fallback with explicit N0.
- Forcing at order 19 is proved only for the named cyclic STS(19), not for
  every STS(19); no claim about orders 16, 17, 18, 21+ or non-cyclic systems
  at order 19.
- Heuristic SA/WalkSAT minima are search logs only, not theorems.

## Reproducibility

Artifacts: output/artifacts/verify_all.py (master verifier),
output/artifacts/sail_smallsts.json, output/artifacts/sail_target_part2.json
(witnesses), output/artifacts/sts19_unsat_trace.json (UNSAT trace, 6632
entries). Per-system logs are described in DRAFT section 6.

## References

- Granath, Gyarfas, Hardee, Watson, Wu, Ramsey theory on Steiner triples,
  J. Combin. Designs 2018. https://doi.org/10.1002/jcd.21585
- Gyarfas, Sarkozy, Turan and Ramsey numbers in linear triple systems,
  Discrete Math 2021. https://doi.org/10.1016/j.disc.2020.112258
- Sarkozy, Turan and Ramsey numbers in linear triple systems II, Discrete
  Math 2023. https://doi.org/10.1016/j.disc.2022.113182
- Solymosi, Wickets in 3-uniform Hypergraphs, arXiv:2305.01193, 2023.
  https://arxiv.org/abs/2305.01193
- Furedi, Gyarfas, The linear Turan number of the k-fan, arXiv:1710.03042.
  http://arxiv.org/abs/1710.03042
