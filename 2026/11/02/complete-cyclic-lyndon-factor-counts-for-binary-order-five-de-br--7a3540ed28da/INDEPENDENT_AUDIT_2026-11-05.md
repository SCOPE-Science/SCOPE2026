# Independent mathematical audit

## correctness

PASS

Every binary order-five de Bruijn cycle corresponds uniquely to a Boolean table on 16 four-bit suffixes: the feedback state permutation F_g(16a+s)=2s+(a XOR g_s) is a single 32-cycle exactly when it represents a de Bruijn sequence. Anchoring at the unique all-zero 5-block prevents rotational double counting. The 65536 tables exhaust all possibilities and exactly 2048 produce valid cycles. The inspected checker.py additionally reconstructs that same canonical set as Euler tours using every five-bit edge. For each of the 2048 cycles all 32 cuts are factored by Duval's algorithm AND by longest-Lyndon-prefix definition with nonincreasing order validation; independent alternative enumeration and factor implementation reproduced the 65536 rooted count spectrum and 2048 max-by-cycle spectrum, including exactly two 16-factor roots. Every cycle has one L=1 root by primitive-necklace uniqueness. All statements are finite exact classification with complete enumeration and injectivity, not inferred beyond order five.

## originality

PASS

Fredricksen–Maiorana and FKM theory construct individual de Bruijn sequences by concatenating Lyndon words; Kociumaka–Radoszewski–Rytter address efficient ranking/decoding of the lexicographically least sequence. Daykin/Duval give algorithms for Lyndon factorization of a given word. Neither construction nor per-word algorithm enumerates CFL factor counts over all 2048 cycles and all 32 rotations. A full published order-five table remains an indexing risk.

## value

PASS

All 2048 binary order-five de Bruijn necklaces form a canonical complete, manageable finite class, and the number of factors in the unique Chen–Fox–Lyndon decomposition is an intrinsic ordered-word statistic. Two full distributions, unique single-factor cut per cycle, sharp 16-factor cutoff and explicit extremal cycles answer a natural finite classification question; value does not depend on a higher-order generalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
