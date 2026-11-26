# Independent mathematical audit

## correctness

PASS

For the repaired finite theorem, the only adjacent letter pairs are 00,01,10: neither substitution image contains 11, both begin with zero, and all three allowed pairs appear in σ³(0). Every window of length at most ten is in two consecutive aligned length-16 images and conversely every prescribed slice occurs, including the two boundary cases of the start offset. The supplied proof computes all signatures by choosing increasing position sets. Independently, `python3 -B /workspace/reproduce_frozen.py 1` uses p_i=v_2(i+1) mod 2 (from p_(2j)=0 and p_(2j+1)=1−p_j), a prefix of 128 letters certified complete here by the adjacent-pair cover, and direct tuple counting. It verifies the factor counts 2,3,5,6,8,10,11,12,14,16, equality with the signature counts until 16 versus 15 at ten, and exactly the two named words in the one nonsingleton class. The common full signature and the 0001 counts 21 and 15 also agree. The frozen infinite statement is mathematically sound: image subsequence positions group into ordered source blocks, giving a linear combination of counts of source patterns of no greater length; the distinct uniform images decode uniquely and occur in the fixed point. It is prior work, not part of the repaired theorem. The uploaded verifier was inspected, not executed. The repaired RESULT.md and VERIFICATION.md state the finite scope and distinguish the script's corroborative checks of the prior witness.

## originality

PASS

For the repaired claim only: credit the earlier exact witness, order-four separation, and full dyadic propagation, which were not credited as prior equivalents in the frozen finding. Originality of the frozen finding as presented fails on that part; the repair removes the unbounded assertion as a contribution and retains the exact proof that ten is first and that its nonsingleton class is unique. Neither a known witness at ten nor experimental strictness proves those exclusions. The thesis reports order-three computations including this range, so priority for first computation or observation is not claimed. The pass is for the explicit exhaustive first-collision classification after statement-level comparison, not for novelty of every number in the table.

## value

PASS

The repaired finite boundary answers a reconstruction question raised by earlier work on a canonical automatic word: it quantifies exactly when counting scattered patterns through order three loses information and characterizes all failures at that shortest length. The range is dictated by the first obstruction, not an arbitrary cutoff. This would be useful as a precise benchmark for later descriptions of third- or fourth-binomial complexity. It is not valuable merely for giving another proof of the already known propagation family, which the repair no longer claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
