# Independent mathematical audit

## correctness

PASS

One-letter deletion receiver counts each diagonal pair once and off-diagonal pair twice, giving ell+2r<=2q, ell<=q and Dq=floor(3q/2); diagonal plus oriented matching attains it. For insertions, a balanced bipartition A∪B and both directed cross-part pairs yield 2floor(q²/4), since every triple has a same-part pair. For q2, 010 rules out full four-code; size-three witness. For q3, six permutations of all-distinct triples bound offdiagonal count e<=4; if e=4, a digon excludes two diagonal words, limiting total <=5; if e<=3, total <=6, attained by three loops plus a directed 3-cycle. Independent exhaustive enumeration of all 16 q2 and 512 q3 codebooks verified (3,3),(4,6). No exact Iq for q>=4 asserted.

## originality

PASS

Best-of-knowledge original joint exact short-block list-two alphabet frontier: D_q=floor(3q/2) for all alphabets, I2=3 and I3=6, separation first at q=3, plus growing insertion family >=2 floor(q^2/4). The original Kiah–Wei–Zeng (2026) full preprint and earlier Haeupler/Guruswami works establish general insertion/deletion list-decoding asymmetry and rate bounds, not this exact ordered-pair q=2,3 extremal census. Preserve the pre-existing qualitative asymmetry credit.

## value

PASS

Pinpoints the first nonempty-deletion-output list-two alphabet size at which insertion and deletion capacities differ, and supplies an unbounded ratio construction while keeping symbols, list size and edit budget fixed. This is a meaningful natural finite coding frontier rather than a cherry-picked experiment; the exact larger-alphabet insertion optimum remains open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
