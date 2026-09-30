# Independent Audit — Exact two-prime-support criterion and a lower bound for lambda-star practical numbers

**Audit date:** 2026-09-30 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `b29e06b4508e1aa03d6f64722cab5f7a347f7046`  
**Audited current source tree:** `b29e06b4508e1aa03d6f64722cab5f7a347f7046`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` directory tree exactly matches the assigned source-tree SHA. GitHub was used only as read-only evidence. The dated independent-audit marker files were absent when this guarded change set was prepared.

## Correctness — PASS

PASS. The 2-power Carmichael weights are 1,1,2,2,4,8,... and sum to S0=2^(a-1)+2. For p-adic exponent j>=1, every weight is p^(j-1)q times the normalized multiset lcm(q,lambda(2^i))/q, which consists of initial 1s followed by powers of two and has exactly the stated sum C. Since that normalized block is itself complete, the complete-sequence criterion reduces exactly to requiring its least weight p^(j-1)q not exceed one plus the total from all earlier blocks, namely S0+C(p^(j-1)-1). The two cases C>=q and C<q, the b=1 threshold, and the counting lower bound follow algebraically. I independently enumerated the actual divisor-weight multisets for 3<=a<=9, odd primes p<100 and 1<=b<=4 and found zero mismatches with the theorem.

## Originality — PASS

PASS. Schwab–Thompson introduce lambda-star practical numbers and explicitly report that, although computation suggests X/log X scale for the Carmichael case, they could not obtain a sharp lower bound. Targeted searches for lambda-star practicality of 2^a p^b, the threshold p<=2^(a-1)+3, and polynomial lower bounds found no prior exact classification or square-root-order counting lower bound. The complete-sequence criterion and basic Carmichael formulas are prior work and receive no novelty credit.

## Scientific value — PASS

PASS. The theorem completely classifies a natural infinite two-prime-support family and converts that family into a rigorous lower bound of order sqrt(X)/log X, supplying substantial polynomial-order growth where the source literature only had an upper bound and computational evidence for the global count. It does not settle the conjectural X/log X order, which is correctly left open.

## Independent checks

- Re-derived the normalized p-block and both cases of the closed formula for C.
- Re-derived the exact block-gap criterion directly from the complete-sequence subset-sum lemma, including necessity.
- Independently enumerated lambda(d) for all divisors of 2^a p^b on a test grid 3<=a<=9, p<100 prime, 1<=b<=4; every direct subset-sequence verdict matched the theorem.
- Rechecked the b=1 parity simplification and the prime-counting construction with z the least power of two above sqrt(X).
- Compared with Schwab–Thompson’s Carmichael section, which says computational evidence suggests X/log X but no sharp lower bound was obtained.
- Current main tree equals the assigned source tree; the UTC/local-date audit pair is absent and VERIFICATION.md is unchanged.

## Limitations

- The exact criterion is restricted to support {2,p} with a>=3.
- The lower bound remains far below the empirically suggested X/log X global scale.
- Originality is asserted after exact and synonymous searches but different terminology for Carmichael subset-sum completeness remains a residual bibliographic risk.

## Evidence and references

- https://arxiv.org/abs/1701.08504
- https://doi.org/10.1142/S1793042118500902
- https://oeis.org/A336508
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/20/lambda-star-practical-two-prime-support--fc59e27647cf

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
