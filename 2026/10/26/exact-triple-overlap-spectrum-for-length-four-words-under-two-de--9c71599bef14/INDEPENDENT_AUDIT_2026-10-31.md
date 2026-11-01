# Independent mathematical audit

## correctness

PASS

Each ordered triple of four-letter center words yields exactly one equality partition of twelve labeled letter positions, canonically encoded as a restricted-growth sequence, and conversely every such partition plus an injective q-symbol relabeling yields all triples realizing that pattern. The partitions are a finite exhaustive domain of size B_12=4,213,597, independent of q. Excluding equal four-position blocks leaves 4,201,207 admissible ordered-center patterns. For each pattern, the 6 surviving index pairs per center are represented as ordered-pair bitsets; the intersection of all three bitsets counts distinct common two-letter outputs exactly, with duplicate outputs collapsed. An independent C++ enumerator written separately from the package visited all 4,213,597 patterns, reproduced all 4,201,207 admissible patterns, all 28 displayed coefficient cells (including zeros) and all no-overlap cells, and confirmed maximum 4. A pattern with k classes contributes exactly (q)_k alphabet injective assignments; each unordered triple is counted six times, proving the all-q polynomial identities rather than extrapolating q=2,3,4,5. Witness (0101,0110,1001) has all four possible binary pairs in the intersection, while the table has no k>4 contribution at maximum. The original direct q=2..5 table and first-moment identity were also checked for consistency.

## originality

PASS

Zhu’s primary 2025/26 binary-deletion theorem already gives the maximum intersection 4 for three centers at these parameters; that binary sharp bound is explicitly not claimed as new. Zhu §4 raises the arbitrary-alphabet extension. The assessed distinct contribution is a complete all-q, triple-center, length-four/two-deletion overlap distribution including a sharp extremizer population polynomial and exact quaternary spectrum, which neither a binary maximum nor q-ary two-center or Hamming-ball intersections implies. Junnila et al. 2025 treats larger alphabets and reconstruction but does not enumerate this triple deletion population in inspected relevant sections. Complete priority across older specialized code tables remains a qualified risk.

## value

PASS

This is the first admissible n=t+ℓ−1 boundary for the three-center two-deletion extension highlighted in a primary paper. The complete alphabet-dependent overlap spectrum and exact rarity of worst-case triples quantify natural ambiguity patterns, including the four-letter/DNA alphabet, beyond a bare known binary maximum. The exhaustive 12-position equality-pattern method proves a natural exact finite structural classification for all q; no claim of general code-rate gains or arbitrary n is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
