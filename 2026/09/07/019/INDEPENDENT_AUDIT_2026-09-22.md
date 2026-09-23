# Independent audit — 2026-09-22 campaign

**Record:** SCOPE-20260907-019  
**Source path:** `2026/09/07/019`  
**Audited repository state:** `28ddd3aac249e831e93e559b47e7bf072478e4d5`  
**RESULT.md blob:** `508c045b693696d13aa2e885a8265812c142bce0`  
**Review date:** 2026-09-23 UTC  
**Reviewer:** separate AI independent audit; no Lean or expert attestation is claimed.

## Claim audited

A fixed-seed finite-N GOE benchmark at N=10,20,50, with empirical KS distances to TW1, fitted centering/scaling constants, moment tables, and deterministic replay evidence.

## Correctness — PASS

I independently regenerated the Hastings–McLeod Painlevé-II TW1 CDF on [-8,8] with a fresh RK4 implementation and independently resampled the Dumitriu–Edelman beta=1 tridiagonal ensemble from SeedSequence(500020). The reproduced largest-eigenvalue means were 5.3246381372, 8.0837369688, and 13.4315142188 for N=10,20,50. The independently computed classical-scaling KS distances were 0.0895431284, 0.0702614040, and 0.0466391869, agreeing with the record. Repeating the stated two-stage grid search reproduced calibrated values (KS,mu,sigma) of (0.0073349546,6.1845553203,0.7085437518), (0.0036771242,8.8242719100,0.6130318533), and (0.0082682486,14.0721356237,0.5236057346). The numerical claims audited here are therefore reproducible.

## Originality — FAIL

The scientifically relevant phenomenon is prior art. Johnstone and Ma, *Fast approach to the Tracy-Widom law at the edge of GOE and GUE*, Ann. Appl. Probab. 22 (2012), DOI 10.1214/11-AAP819, prove for GOE that suitable centering/scaling yields an O(N^{-2/3}) Tracy-Widom approximation (Theorem 2) and report Monte Carlo validation at very small N using 10^6 replications. Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC3647289/ . Bornemann, *Asymptotic Expansions of the Limit Laws of Gaussian and Laguerre (Wishart) Ensembles at the Soft Edge*, arXiv:2403.07628, gives explicit finite-size soft-edge asymptotic expansions and simulation validation.

The record explicitly disclaims a new law and reduces its contribution to three fixed-seed tables plus an in-sample fitted affine calibration. I found no distinct theorem, estimator, algorithm, or previously uncovered regime surviving after the prior work above is subtracted. The exact seed-specific numbers may be newly generated, but arbitrary replayable random draws and fitted constants are not a scientifically original result under this campaign's criterion.

Queries included: `finite N GOE Tracy Widom centering scaling`, `Fast approach Tracy-Widom GOE GUE small N Monte Carlo`, `GOE Edgeworth finite size Tracy Widom`, and `Bornemann soft edge asymptotic expansion GOE`.

## Scientific value — FAIL

The benchmark is reproducible, but it is only three sample sizes from one seed family, with an explicitly optimistic in-sample KS fit and no exact finite-N probabilities, new rate, structural theorem, or reusable algorithm beyond standard Dumitriu–Edelman sampling plus a grid search. Johnstone–Ma already supplied much larger small-N Monte Carlo evidence tied to a proven O(N^{-2/3}) correction, while later asymptotic-expansion work provides more informative finite-size structure. The surviving fixed-seed table is therefore a routine calibration exercise rather than a substantial scientific contribution.

## Repair attempt

A bounded repair would have to replace the seed-specific table by a genuinely new statement—for example an exact finite-N distributional identity, a provably improved approximation with uniform error control, or a new reusable estimator with demonstrated advantage. No such result is present in the record, and deriving one would be unrelated new research rather than a repair of the existing claim.

## Final disposition

**FAILED.** Correctness passes, but originality and scientific value fail. The record should not remain in the accepted findings tree.
