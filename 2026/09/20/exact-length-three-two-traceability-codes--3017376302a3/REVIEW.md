# Review status

Fresh independent audit completed on 2026-10-01 UTC.

- Correctness: **PASS** — The fiber-privacy lemma is valid: a proper repeated fiber in one coordinate forces each member to use symbols globally unique in the other two coordinates, otherwise a descendant has an outside codeword tied with or closer than a parent. Consequently repeated-fiber memberships are disjoint across coordinates. Counting used symbols gives \(R_i-G_i\ge n-q\), and for \(n>q\), \(G_i\ge1\), whence \(3(n-q)\le n-3\). The diagonal and three-group constructions meet the resulting bound. An independent direct descendant check verified the constructions for \(2\le q\le18\); this finite check is supplementary to the symbolic proof.
- Originality: **PASS** — The 2010 construction gives the odd-alphabet length-three family of size \(3(q-1)/2\), while Owen--Ng (2015) explicitly says the best constant remained open and turns to a length-four upper bound. Searches did not locate an exact all-\(q\) length-three optimum, the even-\(q\) construction, or the fiber-privacy upper bound.
- Scientific value: **PASS** — The maximum size of a strength-two length-three traceability code is a natural exact extremal invariant. The theorem proves the known odd-alphabet construction optimal, settles every even alphabet, and determines the exact leading constant \(3/2\) at this length, making it a useful base case for traceability-code bounds.

The original same-model assessment remains preserved in `AUDIT.json`; the independent assessment is documented in `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
