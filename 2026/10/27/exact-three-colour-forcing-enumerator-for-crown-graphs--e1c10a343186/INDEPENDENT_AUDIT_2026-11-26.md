# Independent mathematical audit

## correctness

PASS

A colour shared across the bipartition occurs at just one matched pair. Two shared colours would leave at least two indices (n>=4) whose remaining vertices would all have the third colour and create a monochromatic edge. This exhausts the terminal colourings into monochromatic opposite sides, one bichromatic side in disjoint colours, or one shared matched pair with monochromatic remainders. In the first type no vertex can be forced; in the second the entire bichromatic side is compulsory and an opposite vertex is compulsory exactly if its excluded partner is a singleton colour class. There are 2n onto colourings with such a singleton for each specified pair of colours. In the third type both shared-colour vertices are compulsory, and one further seed on either side suffices: it forces the opposite side except possibly its matched partner, after which n-2>=2 distinct newly available opposite vertices permit the forces on the original side and then the last partner. Additional compatible seeds cannot obstruct this process. Each step must agree with every proper extension of the seed, so a successful restriction is counted once. The resulting counts give the stated polynomial, its z^3 coefficient, and its top coefficient. Independent per-vertex initial-state probabilities give the stated polynomial substitution, including its endpoint by continuity. For K_{n,n}, no colour is shared across sides, and the whole bichromatic side is necessary and sufficient in a terminal colouring using three colours; the two-colour terminal case requires all vertices. An exhaustive independent replay at n=4 counts 144,396,672,720,432,114 assignments of sizes 3 through 8, with zeros below and agreement for both greedy scan orders. At n=3 it gives 12,162,180,66 for sizes 3 through 6, confirming the excluded boundary. Replay via python3 /workspace/branches/57a1add4-bd6c-45b6-976d-75e77fa34f12/replay_record2.py. The structural proof, not the replay, gives all n>=4.

## originality

PASS

The supported distinct contribution is the crown forcing enumerator for n>=4 and its minimum-seed census. The forcing framework and probability substitution are prior, and the complete bipartite half of the contrast follows from an existing polynomial. The inspected closest same-host and same-rule results concern other invariants or do not apply to these crowns.

## value

PASS

Forcing on a crown is a natural test of sensitivity to removing a single incident edge per vertex from the complete bipartite host. The exact distribution describes more than the minimum: it separates singleton-neighbour effects from the new matched-pair seeds. The minimum drops from n to three while the degree decreases by only one, which is an unbounded change on a standard graph family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
