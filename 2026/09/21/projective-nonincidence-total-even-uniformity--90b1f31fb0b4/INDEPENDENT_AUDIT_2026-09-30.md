# Independent audit — 2026-09-30

**Record:** `2026/09/21/projective-nonincidence-total-even-uniformity--90b1f31fb0b4`  
**Audited source tree:** `24b32e221552819454cdc643a56b6f23fec3ae8e`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

## Correctness — PASS

PASS. I reconstructed the proof from the graph definition. In a total dominating sequence, legality of a point vertex depends only on the earlier point vertices: the undominated hyperplanes are exactly those containing their span. A new point is legal exactly when it raises that span by one, and completion on the hyperplane side occurs exactly when the point span is all of F_q^d. Hence every completed sequence has exactly d point vertices. Dually, each legal hyperplane lowers the intersection dimension by one and completion forces exactly d hyperplanes. Thus every total dominating sequence has length 2d. The degree count [d]_q-[d-1]_q=q^(d-1), connectivity, false-twin separation, and the recursive deletion isomorphism were also rechecked. The supplied finite-field verifier was inspected and its snapshot and current Git blob are identical.

## Originality — PASS

PASS, with the usual search-limit qualification. Bahadır–Gözüpek–Doğan (2021) prove odd k impossible and exhibit a connected total 8-uniform graph, while leaving the general connected even-k existence direction open. Dravec–Jakovac–Kos–Marc (2022) cover the bipartite total-4 case and the regular bipartite total-6/projective-plane case. I found no source extending those statements to the arbitrary-dimensional point–hyperplane nonincidence family or completing the connected existence spectrum. The projective nonincidence graphs themselves are classical and are correctly not claimed as new.

## Scientific value — PASS

PASS. The result gives an elementary infinite family for every even parameter and closes a concrete published existence question, while also supplying regularity, false-twin-freeness, explicit order and a compatible recursive reduction. That is substantive graph-theoretic value even though the finite geometries are classical.

## Independent checks

- Reproved the point-span and hyperplane-intersection legality criteria directly.
- Checked the q-binomial degree/order formulas and the false-twin/connectivity arguments.
- Checked the deletion map K↦K∩H under V=P⊕H.
- Inspected the prime-field verification code and deterministic output; both are unchanged from the assigned snapshot.

## Literature evidence

- https://doi.org/10.1016/j.disc.2021.112492 — Bahadır, Gözüpek and Doğan (2021): odd-k nonexistence, a connected total 8-uniform graph, and the remaining even-k direction.
- https://doi.org/10.1007/s00010-021-00776-z — Dravec, Jakovac, Kos and Marc (2022): equal total/Grundy total domination, including the low even bipartite cases.
- https://arxiv.org/abs/1601.07525 — Brešar, Henning and Rall: foundational Grundy total domination framework.

## Limitations

- Existence only; it does not classify all total k-uniform graphs or prove minimum order/degree.
- Originality remains subject to differently indexed finite-geometry or hypergraph-covering literature.

The assigned record package was compared file-by-file against the current default-branch package for its research, review, verification, and listed artifact files; the inspected Git blobs are unchanged. No GitHub write was performed by this audit chat. The guarded change-set below only stages independent-audit evidence and the independent-audit channel of `VERIFICATION.md`.
