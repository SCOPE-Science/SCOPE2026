# Independent mathematical audit

## correctness

PASS

Given length r=2m−1 and n vertices, precisely n−1 labels are the unique forward edges E_{s,s+1}, leaving r−n+1 loop labels. If any vertex carries three loops, two label positions have the same odd/even parity. Exchanging these equal matrix units yields a distinct parity-preserving permutation with unchanged nonzero identity-order product, contradicting isolation. Hence at most two loops per vertex, r−n+1≤2n and 2m≤3n, or n≥ceil(2m/3). In Arhancet §7.1, v_k=1+floor(k/3), F_k=E_{v_{k−1},v_k}, k=1..2m−1 gives n=ceil(2m/3) and the proof establishes that the chosen Fourier coefficient/(1,n) entry has only identity parity-compatible ordering. Boundary n=1 and small m covered by the count; no claim about global minimal complete-contractivity level. The argument is exact, not dependent on truncated enumeration.

## originality

PASS

Best-of-knowledge PASS: Arhancet arXiv:2610.03375v1 Theorem 7.1 supplies sufficiency at N_m and its specific matrix-unit construction, expressly without claiming global N_m optimality, but does not quantify universally over all parity-isolating loop-chain encodings or prove the corresponding necessity. The pigeonhole converse is a new restricted-architecture statement; earlier Schatten 2-contractivity concerns different representations and does not contradict it. Search of Resultary and the focal paper found no identical architecture-wide lower bound. Easy-observation folklore risk remains.

## value

PASS

PASS with a narrow but natural motivation: proving the precise combinatorial resource cost of the explicit Fourier/matrix-unit extraction technique identifies why its sharp construction cannot be compressed by repacking the same path/loops; this can guide genuinely different approaches to reducing contractivity matrix levels. The bound is not promoted to a general operator-algebra level theorem, and its elementary pigeonhole proof is transparently acknowledged.

The dated certificate retains the supplied scientific assessment, sources and limitations.
