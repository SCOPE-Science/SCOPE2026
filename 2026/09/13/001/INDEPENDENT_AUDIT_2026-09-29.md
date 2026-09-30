# Independent audit — 2026-09-29

Record: `2026/09/13/001`  
Audited source tree: `65f3b669f4a56bfa5899ab85459727a284d450d4`  
Disposition: **repaired**

## Correctness

The no-extinction certificate for the named eight-member shell survives independent checking. The retained log certifies sup Re A below -0.01160 for all non-frozen members and -0.011812 for frozen members, comfortably stronger than the claimed -0.0075 threshold; hence |A|>=0.0075 and, with the record's density normalization, I=|A|^2/16>=3.515625e-6. Pure-point stability under equivariant deformations is supported by Baake-Lenz. A reproducibility defect was found in artifacts/certify_ring1.py: its trigonometric coefficient routine represents i sin rather than sin, so the product for odd powers has an extra minus sign. Consequently the printed diagonal M1 sign and the imaginary phase are reversed, while even moments and the real-part bound are unchanged. The staged repair multiplies the moment coefficient by (-1)^j, corrects the script's intensity comment, replaces the log's affected imaginary signs, and corrects RESULT.md to M1≈-0.03743.

## Originality

Deformed-model-set diffraction and stability of pure point diffraction are established literature. The contribution is the explicit certified non-extinction calculation for this chosen Ammann-Beenker shell and deformation. The label 'first observable' is convention-dependent because the Fourier module is dense; the repaired record keeps that limitation explicit.

## Scientific value

The interval-style bound gives a concrete quantitative example where an equivariant deformation cannot extinguish the named shell throughout the stated amplitude interval; the sign repair does not weaken the certificate.

## Limitations

- The rigorous certificate is for the fixed displacement direction u=(1,0).
- 'First observable shell' is not an intrinsic smallest-wavevector statement because Pell-unit shells approach zero wavevector.
- The interval engine itself is software evidence rather than a separately machine-verified theorem.
- The repaired odd-moment sign changes phase information but not the certified real-part lower bound on |A|.

## Evidence and literature

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/13/001
- https://arxiv.org/abs/math/0404155
- https://doi.org/10.1524/zkri.2006.221.9.621
- https://arxiv.org/abs/1904.08285
