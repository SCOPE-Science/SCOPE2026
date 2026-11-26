# Independent mathematical audit

## correctness

PASS

The transposition metric is 5 minus the number of cycles: a swap changes the cycle count by one and any cycle of length l can be built with l-1 swaps. Distinct words of the same parity must consequently differ by a 5-cycle, hence cannot agree in any position. There are at most five of each parity. The independently reproduced equality census uses BFS-checked distances, enumerating the four nonidentity even words among the 24 five-cycles and then all compatible odd five-sets, so it exhausts normalized maxima without relying on the uploaded maximal-clique histogram. It finds precisely six even halves (the order-five subgroups) and exactly two normalizer generator cosets for each. In translation coordinates on F_5 the normalizer consists of ax+b; the multiplier quotient is F_5*, and the two generators 2 and 3 give odd 4-cycles with one fixed point. Thus these cosets construct size 10 and all their differences with H have type (4,1); the 20 within-parity pairs have type (5). Alternatively, an odd word has exactly five total positional agreements against the five even words, while each relative distance-3 odd permutation has at most one fixed point; every mixed pair therefore has one. Counting incidences with a distinguished word gives (120*12)/10=144 labeled codes. Conjugation relates all six H, inversion interchanges the two generator cosets, and translation removes normalization. The left-right action is faithful because S_5 is centerless; inversion cannot be one of those maps (otherwise it would be an inner automorphism on a nonabelian group). This gives 28800 maps and stabilizer 200, as checked directly. Replay: python3 /workspace/branches/19ede26b-3375-4bd9-abfa-520504275776/independent_reproduction.py; recorded summary independent_reproduction.txt in the same directory. The frozen verification and uploaded checker were inspected without executing that checker; the decision concerns the stated group, not maximality of the isometry group.

## originality

PASS

Credit the usual Cayley metric and the published arbitrary-transposition sphere-packing bound, which already implies the upper bound 10 here. The distinct result is the complete equality structure, including the normalized subgroup and quotient-coset description, the labeled count, and the declared-action orbit. Inspected neighboring censuses differ in their generators or relation, not just notation. No claim of absence is made about the inaccessible Chee–Vu primary paper.

## value

PASS

In the natural single-arbitrary-transposition correction problem on S5, the result exposes the exact affine subgroup structure behind equality, not just a small code size or a benchmark replay. It lets a researcher generate all optima without rerunning a general clique search and shows that the apparent normalized alternatives are equivalent under explicit metric symmetries. The structure, pair constraints and census together justify the finite scope; no extension to larger symmetric groups is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
