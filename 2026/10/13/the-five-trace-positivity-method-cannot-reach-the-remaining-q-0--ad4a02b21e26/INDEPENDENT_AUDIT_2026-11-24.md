# Independent mathematical audit

## correctness

PASS

Tafazolian's (4.12) supplies 2Δ relative eigenvalues of modulus √q and power sums −(d−1)q³ for i=1,…,5; Corollary 4.4 and (4.11) supply the ceiling for d>1. Normalize eigenvalues by √q. For P=|Q|² with deg Q≤5, write B_i=Σ_r c_(r+i) conj(c_r) and S=Σ|c_r|². The constant, positive-frequency and negative-frequency terms give 0≤2ΔS−2(d−1)q³Σ_i q^(−i/2) Re B_i. Dividing by 2(d−1)q²S gives c*Tc/S with exactly the stated half off-diagonals. Fejér–Riesz exhausts even complex-coefficient tests, and a top eigenvector realizes the optimal raw bound. Independently, the exact ceiling at q0=9 is 921685/59049>15. Replace √3 by its rational upper bound 97/56 in the nonnegative entries of T to get a majorant B, and use v=(8,14,17,17,14,8). The row sums of diag(v)^−1 B diag(v) are, up to reversal, 86857265/5878656, 5547481/381024 and 764741/51408, all below 15. Thus the infinity norm for the diagonally similar T is below 15 as well, proving λmax(T)<U without the uploaded determinant code. Independent all-rational replay: python3 -B /workspace/audit-evidence/3_positive_vector.py; output in /workspace/audit-evidence/3_replay.txt. The result bounds this family of positivity inequalities; it is not a realization claim for Frobenius spectra or a result about q0=3.

## originality

PASS

The closest paper compares one chosen degree-five test with the ceiling at q0=9. Neither that calculation, the earlier conditional characterization, nor the classical factorization gives the bound for the whole cone of degree-at-most-five tests. No materially overlapping Resultary record was identified in the targeted search.

## value

PASS

The exact field size is picked out by the initiating proof: its geometry reaches q0=9, but its final test does not. Ruling out the entire coefficient optimization of that test, not merely exhibiting another failed polynomial, removes a concrete line of attack on the genus-and-point-count characterization. The conclusion is useful precisely as a method boundary, not as a proof or disproof of the characterization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
