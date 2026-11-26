# Independent mathematical audit

## correctness

PASS

Reassessed the actual replacement for the standard object: distinct cyclic starting positions yield distinct windows, and no window is a reversal of any window (including itself). Both closed walks give balance with 2m distinct edges, and at a symmetric vertex its union out-degree is twice the forward walk out-degree. Removing abba leaves divergence +1 at aab for a≠b, −1 at abb, zero elsewhere. Thus omitted pair divergence over P totals k(k−1). The only +2 pairs are aacc/ccaa, at most binom(k,2); each omitted pair incident to a uniform triple contributes −1, and even k forces ≥k such distinct pairs. Other pairs give at most +1. Therefore r≥binom(k,2)+2k, giving the claim after subtracting from (k⁴−k²)/2. The bounded replay /workspace/branches/independent_replay.py checks the original counterexample and local contributions for k=4,6,8; the argument, not that enumeration, proves the universal bound. Independently generated every cyclic window from the two exact published witness.txt files at local snapshot 36a7204b5741b75430355c38bf9bf0ef7468c2a4: lengths and numbers of canonical reversal representatives were (106,106) and (603,603), with both alphabet checks and all nonpalindrome checks passing. The repaired verification notes give the short replay for these two exact corollaries.

## originality

PASS

Best-of-knowledge pass for the uniform upper bound in the repaired standard scope. The degree framework is established, but no inspected statement implies this sharper upper bound across every even k≥4. Credit the two existing lower-bound constructions and distinguish the later indexed k=4 overlap from the uniform claim.

## value

PASS

The repair retains a meaningful uniform improvement for an established extremal problem. It closes two small-alphabet gaps once the pre-existing verified witnesses are credited, and exposes a structural obstruction from divergence plus parity even where the maximum is unknown. It is not just a finite table recalculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
