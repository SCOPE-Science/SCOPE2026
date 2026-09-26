# Independent audit — 2026/09/09/028

Date: 2026-09-26. Disposition: retain accepted.

## Correctness — PASS

I independently expanded the defining product through degree 970 using exact integer arithmetic and the logarithmic-derivative recurrence (n d_4(n)=sum_{k=1}^n(13sigma_1(k)-8sigma_1(k/2))d_4(n-k)), with (sigma_1(k/2)=0) for odd (k). This gives the reported initial coefficients (1,13,100,585,2862). I compared every one of the 343 mod-343 and 49 mod-49 witness rows with the resulting coefficients modulo 49, and checked each witness is the first nonzero one in its residue class. The largest mod-343 witness is at 970. In particular, the residues for 39, 235, 284, 627, 970 are respectively 14, 21, 0, 0, 14 modulo 49. One exact finite witness for each class proves the stated absence of uniform mod-49 congruences on those steps. The finite computation is distinct from the candidate's product-convolution verifier.

## Originality — PASS, narrowly

Baruah–Das–Talukdar, Theorem 6.1(6.8), already proves the three mod-7 progressions at step 343. Its adjacent mod-49 statement (6.7) concerns (d_3), not (d_4). Chen–Xu–Yin's 7-power towers concern (d_3,d_5). The present negative mod-49 result for (d_4), with complete residue witnesses at steps 343 and 49, was not in these checked sources. This is a finite sharpness result, not an infinite congruence or new tower.

## Scientific value — PASS, bounded

The 343 explicit counterexamples settle whether the known (d_4) mod-7 step 343 can lift uniformly to mod 49; the third advertised residue requires looking beyond two terms. This usefully narrows a specific proposed tower. It says nothing about a finer step such as 2401, other primes, or higher powers. The finite scan of mod-7 residues is not proof of uniqueness at all indices.

## Sources and replay

- Baruah, Das, Talukdar, *Congruences for k-elongated plane partition diamonds*, arXiv:2207.06264, Theorem 6.1: https://arxiv.org/html/2207.06264v1
- Chen, Xu, Yin, *Congruences modulo powers of 7 for k-elongated plane partitions*, arXiv:2508.09723: https://arxiv.org/abs/2508.09723
- Candidate `RESULT.md`, `output/artifacts/witness_table.json`, `output/artifacts/witness_table49.json`, `output/artifacts/verify.py`. Independent exact recurrence and all row comparisons performed in this audit.
