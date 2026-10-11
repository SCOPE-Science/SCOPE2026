# Independent mathematical audit

## correctness

PASS

Each resolution update replaces every participant row by the union of participant views and leaves other rows fixed; these maps preserve componentwise unions. Therefore the suffix acts on an arbitrary input view tuple by taking the union over the contributor indices computed from singleton initial views. Applying this once to the prefix tuple and once after the occurrence \(B\) gives exactly \(F_a\) versus either \(F_a\) or \(F_a\cup U_B\), proving the criterion. If views differ, a coordinate-equality Kripke model makes distinct contributor index sets induce distinct intersection relations, proving model-independent necessity. For an empty suffix, the condition reduces to equality of participant views. Greedy deletion of immediately redundant events preserves the entire current view tuple, and every retained event strictly raises \(\sum_a |V_a|\) from \(n\) toward at most \(n^2\), giving the compression bound. The inspected verifier exhausts all groups with up to four agents for short prefixes/suffixes as a consistency check.

## originality

PASS

Balbiani--van Ditmarsch--Lerouvillois introduce the exact asynchronous-resolution history semantics and the view recursion needed here, while older gossip work treats different pairwise call models and redundancy notions. Neither the inspected primary material nor Resultary supplied the arbitrary-occurrence prefix/suffix current-relation deletion criterion or the resulting \(n(n-1)\) view-state compression bound.

## value

PASS

The exact test answers the natural operational question of whether an arbitrary earlier group resolution can be deleted without changing the final current knowledge relations, not merely whether a final repetition is locally uninformative. The finite compression bound is a useful global consequence and the scope distinction from history-sensitive equivalence is clearly maintained.

The dated certificate retains the supplied scientific assessment, sources and limitations.
