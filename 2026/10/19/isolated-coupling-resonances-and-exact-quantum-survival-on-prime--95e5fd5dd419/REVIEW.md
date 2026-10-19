# Review — Isolated coupling resonances on prime-prism ladders

## Correctness — PASS

The projection onto the eigenspaces orthogonal to the localized sink is the only nondecaying sector for positive sink strength, by a strict imaginary-eigenvalue argument on its orthogonal complement. The opposite-rung source and sink have opposite signs in the two Fourier parity bands, leading to the nonnegative collision identity. For a prime cycle, a cyclotomic minimal-polynomial argument proves all differences of distinct cosine levels are unique. The exact momentum multiplicities then give the two claimed survival fractions; no energy overlap occurs elsewhere. Normalization, signs of hopping, the smallest prime, and strictly positive coupling and sink strengths have been checked. The finite dense-matrix and no-jump propagator verifier corroborates but is not used to replace these proofs.

## Originality — PASS, provisional priority

The dark spectral projector is classical prior work, especially Krovi–Brun (quant-ph/0606094), Novo et al. (1412.7209), and Razzoli et al. (2011.13794). The Thiel et al. (1906.08112) general bright-projector formula concerns stroboscopic measurements; Xu (0812.3452) considers another cycle family; Mareš et al. (1908.10173) consider a different coined open ladder. The inspected material does not provide the evaluated exceptional positive rung-coupling set for the weighted odd-prime Cartesian prism with opposite-rung capture. Its uniqueness and the exact two surviving weights require a separate prime-cyclotomic argument. An unlocated broader theorem or literature treating exactly these resonances remains a publication-priority risk.

## Mathematical value — PASS

A single source adjacent to a perfect absorber would suggest robust capture, yet every odd-prime two-ring network admits exactly \((p^2-1)/8\) isolated coupling strengths with protected amplitude and two distinct, exact surviving fractions. At ordinary equal-magnitude edge weights, complete absorption returns. The exceptional set, its cardinality, and the state-resolved weights are natural, nontrivial invariants of the family that distinguish resonant transport from the generic regime. Discontinuous infinite-time trapping is not a guarantee of experimentally robust finite-time suppression; no such claim is made.

## Reproducibility and limits

The exact proof and definitions are in `RESULT.md`; `verify.py` requires packages specified in `requirements.txt`. The dense spectral checks cover six odd primes and both signs of hopping, and selected direct loss evolutions. Exhaustion of all larger primes, other initial states and finite-time decay rates is not claimed. No independent scientific or publication-priority audit was performed.

Self-review: passed. Independent audit: not yet performed.
