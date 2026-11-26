# Independent mathematical audit

## correctness

PASS

The frozen two-rank result is correct: exact extension sets characterize each EF position by back-and-forth, and an independent rotational-orbit replay over every move for 3≤n≤24 reproduced both partitions. In the frozen infinite bridge, truncated cyclic gaps are initialized with n−1,m−1≥3·2^(q−1)−1; splitting a long gap of length ≥2t+1 can match one short side or leave both sides ≥t. At terminal t=2, an arc of length at most two is detectable from gaps of length zero or one, including two consecutive zero gaps, so adjacency and equality are preserved. The independent finite boundaries and bridges are 10≠11 and 11≡₃12,24; 18≠19 and 19≡₄20,24. Replay: /workspace/branches/ad743f7d-f9c4-4598-a2f4-347ad3ed6098/replay_ef.py with --rank 3 or --rank 4 and --max-n 24; corresponding rank3_full.out and rank4_full.out. No uploaded code was executed. The final repaired proof is independently checkable without computation: transitivity reduces rank three to the spectrum of one-round pair types; for distinct pairs these are the adjacency bit and positivity of c, 4−e−c and n−10+2e+c, where c is the number of common neighbours. The positive/negative difference multiplicities 2,1,2,1 at distances 1 through 4 give each row of the repaired table, including the unbounded n≥11 row where no negative difference can wrap into the short arc. Repeated pairs are uniform for n≥6 and the three complete graphs are indistinguishable in three moves. These checks establish the corrected exact seven-class partition.

## originality

PASS

PASS applies to the repaired rank-three finding only. The original two-rank finding fails originality as bundled: a distinct same-day indexed result already states the complete rank-four partition for n≥5 in exactly the same vocabulary, including sharp threshold 19, and the exceptional rank-four additions at 3 and 4 are immediate clique-size comparisons. This is affirmative overlap, not a conclusion about intraday priority. The lower-rank exact partition is a genuine surviving result. The ordinary-cycle upper-bound implication is credited, and neither the available rank-four theorem nor the upper bound establishes the necessary finite rank-three separations.

## value

PASS

The surviving rank-three census is a complete exact classification for the first nontrivial cycle power in the unlabeled graph vocabulary. The third move can probe the extension of a selected pair; the exact pattern table shows that the eventual-equivalence upper bound is sharp and identifies every exceptional graph size, including the clique block. These are distinguishing-resource facts not delivered by a large-size bound or by the rank-four table. Extending the overlapping rank-four result only by the two small clique sizes would not provide a comparable new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
