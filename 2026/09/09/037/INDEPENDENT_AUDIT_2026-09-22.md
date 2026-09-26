# Independent audit — 2026/09/09/037

Date: 2026-09-26. Disposition: retain accepted.

## Correctness — PASS

I constructed (S_8(i,j)=(-1)^{operatorname{popcount}(imathbin{&}j)}) independently. Enumerating all 255 nonempty column subsets and all their signings gives the claimed discrepancy histogram (1:8,2:42,3:112,4:85,5:8); the full eight-column discrepancy is 4 and exactly the eight seven-column sets attain hereditary discrepancy 5. I separately enumerated all (sum_{k=1}^8inom8k^2=12869) nonempty square submatrices and computed exact Bareiss determinants. Their per-size maxima are (1,2,4,16,32,128,512,4096). Comparing (M_k^{1/k}) gives (2sqrt2) at (k=8), hence the exact ratio (5/(2sqrt2)). The candidate's 12869 count corrects its own earlier proposal typo. This is a complete finite certificate for the specified matrix.

## Originality — PASS, narrowly

The Lovász–Spencer–Vesztergombi determinant lower bound and the later asymptotic gap results are prior; Hadamard orthogonality and the full determinant are elementary. The checked Matoušek, Jiang–Reis and Li–Nikolov sources do not give this exact order-eight joint discrepancy, hereditary discrepancy and determinant spectrum. The contribution is an exact small calibration point, not a new gap theorem.

## Scientific value — PASS, bounded

The strict ratio (5sqrt2/4) with full subset and determinant certificates gives a transparent test case for discrepancy algorithms and the determinant bound. Its order-eight scope prevents asymptotic conclusions.

## Sources

- Matoušek, *The determinant bound for discrepancy is almost tight*, arXiv:1101.0767: https://arxiv.org/abs/1101.0767
- Jiang and Reis, *A Tighter Relation Between Hereditary Discrepancy and Determinant Lower Bound*, arXiv:2108.07945: https://arxiv.org/abs/2108.07945
- Li and Nikolov, *On the Gap between Hereditary Discrepancy and the Determinant Lower Bound*, arXiv:2303.08167: https://arxiv.org/abs/2303.08167
- Candidate `RESULT.md`; independent complete signing and determinant scans above.
