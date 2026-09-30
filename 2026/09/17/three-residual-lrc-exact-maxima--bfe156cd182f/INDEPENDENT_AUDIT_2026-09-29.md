# Independent audit — 2026-09-29

**Record:** `2026/09/17/three-residual-lrc-exact-maxima--bfe156cd182f`  
**Audited source tree:** `6dfdb365d1d4ec181ff4c21021b1c92866009502`  
**Repository snapshot:** `SCOPE-Science/SCOPE2026@253a0fe5d0217455660a277f9adb940030e567ad`  
**Disposition:** **PASSED**

## Correctness — PASS

PASS. Kang--Xiong's Definition II.1 uses d(C|T)=0 for fewer than two projected words, so an all-symbol (1,3) recovery view with local distance at least three necessarily has exactly three coordinates. The record's coordinate-partition lemma is therefore valid even for nonlinear codes: all coordinates in a recovery triple induce the same equality partition, each resulting equivalence class has size at least three, representatives determine codewords injectively, and Hamming distance becomes the weighted number of differing classes. This gives A_2(15,5;1,3)<=16 and A_3(7,3;1,3)<=9, with the displayed repetition constructions attaining both. For the binary (14,4,2,2) row, the published three-block LP value 1359968/8555<256 forces linear dimension at most seven. I independently enumerated all 128 words of the displayed 7x14 binary generator: its exact weight enumerator is 1+16z^4+12z^5+18z^6+24z^7+23z^8+28z^9+6z^10, and each of the five stated local triples punctures to the [3,2,2] parity code and together covers all 14 coordinates. Hence K_2(14,4;2,2)=7. The same LP table gives 96/5<32 and 81/7<27 for the other two rows, while the new size-16 and size-9 constructions force linear dimensions four and two.

## Originality — PASS

PASS, with the contribution correctly narrowed to exact closure rather than construction novelty. Kang--Xiong's Corollary V.2 explicitly leaves exactly (2,14,4,2,2), (2,15,5,1,3), and (3,7,3,1,3) outside its exact linear-dimension conclusion. The binary [14,7,4;2] LRC was already known, and locality-one optimal linear constructions have substantial prior coverage; the record discloses both. What is new in the inspected evidence is combining the September 2026 LP values with elementary nonlinear locality-one structure and the known/explicit constructions to close all three residual rows, with nonlinear exactness for two of them. No current indexed source located those three exact conclusions together before this record.

## Scientific value — PASS

PASS. The result completes the finite table that motivated the three-block LP paper and strengthens two of the three residual rows from linear-dimension statements to exact maximum code sizes for arbitrary nonlinear codes. The nonlinear partition lemma is short but useful because it avoids linearity assumptions and cleanly explains why the two locality-one gaps collapse.

## Sources checked

- https://arxiv.org/abs/2609.16044 — Kang and Xiong, Linear Programming Bounds for Locally Recovery Codes II; locality convention, exact three-block LP values, and Corollary V.2 excluding precisely these three rows.
- https://doi.org/10.1007/s12095-023-00626-6 — Yang et al., prior existence of a binary [14,7,4;2] locally recoverable code.
- https://doi.org/10.1109/ACCESS.2019.2934769 — Xia and Chen, prior characterization context for optimal linear locality-one LRCs.

## Limitations

- The nonlinear maximum A_2(14,4;2,2) is still not determined; the record establishes only K_2=7 there.
- The novelty claim is a recent exact synthesis/closure, not novelty of each individual construction.

No GitHub content was modified during this audit. This file records an independent evidence review; it is not a peer-review or priority guarantee.
