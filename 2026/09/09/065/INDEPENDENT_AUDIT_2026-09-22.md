# Independent audit — 2026/09/09/065

## Correctness — PASS, computational with stated tree premise

I compiled and ran the committed independent recursive Engine C to the full 520,000,000 bound: it visited 4,219,560,868 child births, marked 4,999,652 distinct window curvatures, and returned FNV 73b4bb3c821b2bd3. Its bitmap SHA-256 is a3e7646a0a7a5230011c0f98b962f210d2dc5bc64df65a3192c4ba52f6cc12b6, matching the record. I independently diffed all 20,000,000 window integers against the bitmap and the six permitted residues; there are 5,000,001 admissible integers and exactly 349 missing, byte-for-byte equal to the committed exception list, first 500004300 and last 519931204. Its residue breakdown is 101/101/74/73 in 12/0/4/16 and zero in 13/21. The list is sorted, unique and entirely in the claimed window.

Fuchs–Sanden's open Lemma 3.3(ii) independently confirms the six residue classes, and their Section 4 describes pruning the Descartes tree by increasing maximal curvature. I checked the Vieta involution and root equation algebraically; Engine C verifies Descartes at each birth. The full-bound reproduction tests the computational claim, although it shares the record's tree traversal premise and is not a formal proof of unique-parent geometry. Bitmaps were omitted from the accepted package, but the exact SHA is independently reproduced.

## Originality — PASS, finite extension

Fuchs–Sanden report Coins computations only below 5×10^8 and documented exceptions there. The checked prior texts do not provide this 5×10^8-to-5.2×10^8 exact block. This is new numerical data with a reproducible full-bound traversal, not a proof of the local-global conjecture.

## Scientific value — PASS

The 349 further admissible exceptions give a concrete lower bound on any eventual local-global threshold for this packing and a residue-resolved benchmark for thin-orbit computations. No asymptotic inference or completeness beyond 520,000,000 follows.

## Sources

- Original RESULT.md, METADATA.json, committed Engine C and exception list; independent full-bound run and bitmap diff above.
- Fuchs–Sanden, Lemma 3.3 and Section 4, https://arxiv.org/pdf/1001.1406 .
- Graham et al., https://arxiv.org/abs/math/0009113 .
