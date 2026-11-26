# Independent mathematical audit

## correctness

PASS

To reach all five four-subsets, at least one letter must have rank four. If neither letter is a permutation, a four-subset reached at the last letter is the full image of that letter, giving at most two targets. With one permutation, each attainable four-subset is a cyclic shift under that permutation of the rank-four image, by looking at the last rank-four letter. Thus the omitted state must have a full length-five orbit and the permutation is a five-cycle. Conversely write e for the missing output and d for the doubled output. For each proper nonempty target S some shift S' of S excludes e and contains d: if not, the equal-size sets of shifts containing d and e would be identical, forcing S to be invariant under the nonzero displacement d-e, impossible on the five-cycle. The rank-four preimage of S' has size |S|+1, so induction reaches S using one rank-four letter and at most four cyclic steps per unit decrease in size. Each state relabeling bringing the permutation to the standard cycle leaves only rotations as residual conjugacies; fixing the missing output to 0 selects a unique representative. There are 10 choices of the duplicate input pair and 24 bijective assignments of outputs to the four fibres in each representative. As the two letters have different ranks, letter exchange cannot be an automorphism, so every class has 240 ordered labeled representatives. Independent replay enumerates exactly these 240 tables, computes all subset distances by edge relaxation, matches all 13 histogram entries and cardinality maxima, and tests the claimed length-20 word and target distance for the extremal map. The reported extremal map has ordinary reset threshold 16, not 20; the asserted 20 is a longest shortest length to a specified target.

## originality

PASS

Pass is for the full reaching-diameter distribution and its gap, not the population, known reaching bounds, or extremal uniqueness viewed separately. The de Bondt–Don–Zantema reset classification, combined with the cyclic-letter extension bound, already limits any R=20 candidate to the Černý class. The separate gap at reaching diameter 19 and the profile at every diameter are not supplied by that reset table.

## value

PASS

Complete reachability is a canonical restriction, and the largest shortest distance over every specified subset is an intrinsic diameter. A complete small-prime census supplies a benchmark beyond existence or maximum reset length and shows a genuine missing diameter immediately below the sharp top. Credit for this value is the full all-target distribution and gap, not an allegedly new extremal class or a new general upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
