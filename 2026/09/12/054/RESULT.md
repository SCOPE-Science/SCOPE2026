# Disproof of the equal-volume cross-polytope versus box acceptance–Rényi tradeoff at an ML-DSA-44 parameter tuple

## Context
Consider the canonical uniform-mask membership-overlap abort model: draw `y` uniformly from a masking body `S`, accept iff `y+v` remains in `S`, and output `z=y+v`. The submitted tradeoff claim says that replacing the box by an equal-volume `l1` ball (cross-polytope) should simultaneously improve acceptance by a factor of at least 1.5 and not increase Rényi-2 divergence. The original file used a hybrid `(tau,eta,l,gamma1)` tuple that does not correspond to any standardized ML-DSA parameter set. The repaired witness uses the actual ML-DSA-44 values from FIPS 204.

## Definitions
Let `N=256*l`. For ML-DSA-44, FIPS 204 gives `(k,l)=(4,4)`, `tau=39`, `eta=2`, `beta=tau*eta=78`, and `gamma1=2^17`. Hence `N=1024`.

- Box: `S_box=[-gamma1,gamma1]^N`.
- Cross-polytope: `C={y: ||y||_1 <= R}` with equal volume, so `R=gamma1*(N!)^(1/N)`.
- Shift: `v=beta e_1`, which has `||v||_infty=beta`.

## Exact acceptance and divergence formulas
For the canonical abort model, the accepted distribution is uniform on `T=S∩(S+v)`. Therefore for every Rényi order `alpha>0`, `alpha != 1`, and also for KL,

`D_alpha(U(T)||U(S)) = -log(delta)`, where `delta=|T|/|S|`.

For the single-coordinate shift,

`delta_box = 1-beta/(2 gamma1)`.

The cross-polytope volume is `(2R)^N/N!`; slicing the overlap in the shifted coordinate gives

`delta_cross = (1-beta/(2R))^N`.

## ML-DSA-44 witness
With `N=1024`, `gamma1=131072`, `beta=78`, and `(N!)^(1/N)=378.325067768656...`:

- `delta_box = 0.9997024536132812`;
- `delta_cross = 0.9991949648934448`;
- `delta_cross/delta_box = 0.9994923602337854 < 1.5`;
- `D_2(box) = 0.0002975906624278`;
- `D_2(cross) = 0.0008053593213184`;
- `D_2(cross)/D_2(box) = 2.7062654276 > 1`.

Thus both proposed inequalities fail at an actual standardized ML-DSA-44 parameter tuple.

The divergence reversal also has an analytic certificate. Let `x=beta/(2 gamma1)` and `M=(N!)^(1/N)`. Using `-log(1-t)>=t`, `-log(1-x)<=x/(1-x)`, and the AM–GM bound `M<=(N+1)/2`,

`D_2(cross)/D_2(box) >= N(1-x)/M >= 2N(1-x)/(N+1) > 1`.

## Originality and scope
The identity `D_alpha=-log(delta)` for a uniform accepted subset and the elementary overlap formulas are standard calculations. The useful content is the explicit refutation of this proposed equal-volume `l1`-ball versus box tradeoff under the stated canonical model. Contemporary FSwA polytope work studies broader rejection-sampling constructions and different bodies; this record should not claim that cross-polytopes or polytope masking were previously unstudied.

## Limitations
The result is specific to uniform masking with membership-overlap acceptance and the equal-volume calibration. It does not address nonuniform masking, different rejection rules, or other radius calibrations.

## Reproducibility
Run `python3 artifacts/refutation.py` from the record directory. The script checks a Robbins/Stirling bracket for `(1024!)^(1/1024)` and prints the acceptance and Rényi values above.

## References
- NIST FIPS 204, *Module-Lattice-Based Digital Signature Standard*, Table 1 (ML-DSA-44 parameters): https://doi.org/10.6028/NIST.FIPS.204
- H. Bambury, H. Beguinet, T. Ricosset, E. Sageloli, *Polytopes in the Fiat-Shamir with Aborts Paradigm*, IACR ePrint 2024/411.
