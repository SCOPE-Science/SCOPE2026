# Certified lift-16 (3,4)-regular QC instance obstruction for Q16 (n=400, k=28)

## Object

Use lift `L=16` and shift matrix

`A=[[14,1,9,6],[12,10,6,0],[4,4,8,3]]`.

The expanded classical base matrix `H_A` is 48x64. The symmetric lifted-product CSS matrices `H_X,H_Z` are 192x400.

## Exact results

1. **CSS parameters.** `rank(H_X)=rank(H_Z)=186`, `H_X H_Z^T=0`, hence `[[400,28]]` at the dimension level. The base Tanner graph has no 4-cycles.
2. **Spectral interval.** Exact rational inertia gives exactly one eigenvalue of `M=H_A H_A^T` above `2.73^2`, while at `2.70^2` it gives nine. Since the trivial singular value is `sqrt(12)`, the second singular value satisfies `2.70 < s2 <= 2.73`; numerically `s2=2.72800676...`.
3. **Corrected transfer obstruction.** For the particular Tanner transfer expression `c^2/s2^2` with `c=3`, the *lower* spectral bound `s2>2.70` is the direction needed for an upper bound on that expression:
   `9/s2^2 < 9/2.70^2 = 100/81 ≈ 1.23457 < 3/2`.
   Thus this specific `c^2/s2^2` route cannot reach the `3/2` distance threshold (nor the larger `9/4` SSF threshold) for this instance. The previous text incorrectly used the upper bound `s2<=2.73` to claim an upper bound of `1.2076`; that inequality direction is repaired here.
4. **Classical distance.** The length-64 base code has exact distance 8: all words of weight <=7 are excluded by a meet-in-the-middle syndrome exhaustion, and `{18,22,26,30,34,38,42,46}` is a weight-8 codeword.
5. **Quantum upper bound.** `W={0,80,160,240,256,320,384}` has zero syndrome under both CSS checks and lies outside both relevant row spaces, so it gives genuine weight-7 X- and Z-logicals and `d(Q16)<=7`. No quantum lower bound is claimed.
6. **Decoder logs.** The committed BP/SSF numbers are finite-shot experimental operating points only.

## Reproducibility

The exact pieces are separated into `build_q16.py`, `inertia_cert.py`, `check_270.py`, `classical_d8.py`, `quantum_w7.py`, and the corrected `transfer_void.py`. An independent audit rebuilt the matrices, recomputed ranks/orthogonality, singular values, both inertia counts, the distance-8 syndrome exhaustion, and the weight-7 logical.

## Limitations

- The transfer statement is only about the stated `c^2/s2^2` spectral route; it is not a theorem that no other distance/soundness argument can work.
- The earlier random/annealing search near 2.728 is empirical and is not used to prove a lift-16 window-wide optimum.
- Only `d<=7` is certified for the quantum code.
- Decoder results depend on one finite-shot decoder configuration.

## Related work

Finite-length lifted-product design criteria: Raveendran–Declercq–Vasic, arXiv:2503.07567. Moderate-length quantum Tanner constructions: Guemard–Zemor, arXiv:2502.20297.
