# Independent mathematical audit

## correctness

PASS

In the repaired scope, each clique column has 0, 1 or m omissions because any selected vertex sees all omitted neighbors in its clique. A full run has length at most two and gaps between runs have length at least two. A singleton cannot be at distance one or two from a full column; distance two makes the intervening column empty and violates the cap in the singleton's row. If there are f full columns in b blocks, then n≥f+2b≥2f and n=4q+2 excludes f=2q+1 since it would require b≥q+1. Thus f≤h. The gap bound gives at most (n−f−2b−2)_+ singleton columns, at most 2(h−f) since n−2h≤2. Therefore |S|≤mh−(m−2)(h−f) and equality with a full column requires f=h and no singleton. Without full columns |S|≤n, with a tie n=mh only at (3,6) in the repaired scope, where consecutive singleton rows must agree and all three fixed rows are feasible. The allowed binary words are feasible by the direct conditions. Counting a distinguished block and dividing by b gives n in residues 1 and 3 and n(q+1)/2+nq/2=n²/4 in residue 2. This also proves attainment. The original n=3 tie and residue-zero counts agree with the credited results. The supplied finite-check source was inspected, not executed; the all-size conclusion is symbolic.

## originality

PASS

For the corrected claim only, the strongest inspected sources cover the base cycle, bounds, the excluded rook slice and neighboring variants, but do not determine the clique-cycle optimum and rigidity for m≥3, n≥5, 4∤n. The base word count is not claimed to be independently original.

## value

PASS

The surviving structured classification resolves whether product minimizers must arise from base-cycle patterns even when generic capacity bounds do not meet. It also identifies a genuine smallest exception outside the rook slice, where a different geometric shape ties, and supplies exact labelled counts for future extremal and enumeration work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
