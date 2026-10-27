# Mathematical review

## Correctness — PASS

The claim is stated for all real mean multipliers and integer windows \(m\ge2\), and all admissible within-step equicorrelations. The companion-matrix calculation gives an exact identity \(\mathcal K(P_0)-P_0=(F-1)e_1e_1^\top\). Nonnegative \(F-1\) prevents decay; negative \(F-1\), together with an explicit full-rank \(m\)-step reachability sum, gives strict matrix Lyapunov decay. A separate characteristic-root argument supplies the exact deterministic interval \(-m<a<1\). The unique stationary covariance follows from the exact discrete Lyapunov equation. An independently implemented exact-rational checker tests 1080 parameter cases; universal assertions depend on the proof, not that finite check. The critical boundary is excluded; no infinite-horizon conclusion is inferred merely from finite experiments.

## Originality — PASS, subject to bibliographic uncertainty

The RCA(p) model class and its generic second-order stationarity criteria are established mathematics: the 2019 full-text paper of Benmoumen, Allal, and Salhi explicitly recalls earlier Nicholls–Quinn / Andel spectral conditions and AR-like autocorrelations. The 2026 motivating Epperlein–Wirth paper addresses deterministic moving averages, as far as its accessible abstract establishes; its full technical text could not be read. The scientific claim assessed here is the *explicit* all-window correlation-dependent threshold, a sharp constructive Lyapunov certificate, a flat-lag law, and a sign-reversing optimum. The implicit general RCA(p) criterion is acknowledged and is not presented as new. Exact prior derivations in less accessible specialized RCA literature are a nonzero residual risk. The source identifiers and mathematical distinctions are recorded in the accompanying audit.

## Value — PASS

An arbitrary-order window normally requires a growing second-moment stability calculation; the single closed formula provides a directly usable threshold across all window lengths and correlation parameters. Positive and negative feedback favor opposite noise-correlation endpoints, and maximally negative correlation retains a positive noise budget \(m+a\) as the positive-feedback deterministic stability frontier is approached from below. The exact stationary variance and all short-lag correlation values make the result relevant to tuning noisy delayed-feedback averaging, beyond renaming a generic model.

## Limitations and literature

The proof assumes IID noise vectors over time and equal deterministic averaging coefficients. Gaussianity is not necessary. The available primary 2026 paper excerpt was insufficient to assess the entire preprint, and older RCA literature may contain an equivalent explicit result. No claim is made for independent external assessment or practical stability under inexact arithmetic. Closest primary publications: Epperlein–Wirth (2026), arXiv:2609.21442; Benmoumen–Allal–Salhi (2019), DOI:10.1155/2019/8479086.

Self-review: passed. Independent audit: not yet performed.
