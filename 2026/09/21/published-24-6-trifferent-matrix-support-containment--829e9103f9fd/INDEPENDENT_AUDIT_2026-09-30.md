# Independent audit — 2026-09-30

**Record:** `2026/09/21/published-24-6-trifferent-matrix-support-containment--829e9103f9fd`  
**Audited source tree:** `4f9049920a7785b4ca9df5f34f8579be68fca5e7`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

## Correctness — PASS

PASS. The published 2024 JLMS article explicitly prints the six-row length-24 ternary generator matrix and calls its row space an [24,6]_3 trifferent code. Using those printed rows, I independently recomputed a=r2+r3=100112202000102002022001 and b=r1+r4=211221201011101002221122. Their supports have sizes 12 and 19 with strict containment Supp(a)⊊Supp(b). Therefore the code is not minimal; directly, the three distinct codewords (a,b,-a) have no coordinate containing all three symbols 0,1,2, so the code is not trifferent. I also checked that the stated first-six-column minor is nonzero mod 3. This invalidates the displayed witness as used, but correctly does not rule out some other [24,6]_3 trifferent code.

## Originality — PASS

PASS as a narrowly stated correction/obstruction. The current full text of the 2024 paper still prints the same matrix in the proof of Theorem 1.7, and targeted searches did not surface a corrigendum or an independently published support-containment certificate. The later 2026 strong-blocking-set paper does not supply a correction of this matrix in the material located. The audit does not claim that the whole theorem is false—only that this public matrix cannot certify the argument as written.

## Scientific value — PASS

PASS. A short exact certificate detecting a flaw in a published explicit construction has clear scientific value: it is independently reproducible, pinpoints the affected proof step, and carefully separates failure of the printed witness from nonexistence of a corrected witness.

## Independent checks

- Recomputed both codewords from the printed matrix over F_3.
- Verified strict support containment and the direct trifference failure of (a,b,-a).
- Verified rank 6 via the nonzero first-six-column determinant modulo 3.
- Inspected the repository verifier and deterministic output; both match the assigned snapshot.

## Literature evidence

- https://doi.org/10.1112/jlms.12938 — Bishnoi, D'haeseleer, Gijswijt and Potukuchi (2024), including the printed [24,6]_3 matrix in the proof of Theorem 1.7.
- https://arxiv.org/abs/2301.09457 — Preprint/version history of the same work.
- https://doi.org/10.1007/s00493-026-00202-5 — Bishnoi and Tomon (2026), later explicit strong-blocking/minimal-code work.

## Limitations

- This establishes failure only of the displayed matrix, not nonexistence of every [24,6]_3 trifferent code.
- A non-indexed author correction or replacement witness could exist outside the searched channels.

The assigned record package was compared file-by-file against the current default-branch package for its research, review, verification, and listed artifact files; the inspected Git blobs are unchanged. No GitHub write was performed by this audit chat. The guarded change-set below only stages independent-audit evidence and the independent-audit channel of `VERIFICATION.md`.
