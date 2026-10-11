---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the zero-frequency criterion

The analysis in the accompanying result is the proof for infinitely many coordinates. In particular, the key coordinatewise conclusion \(x_n^{(k)}\to\lambda\) is used only with the finite formula for each output coordinate, while the converse needs the explicitly uniform bound

\[
\|W_cu^{(k)}-b\|_\infty\le\sup_{n>k}|b_n|+\sum_{j\ge0}|c_j|\min\{1,j/k\}.
\]

Absolute summability makes both the operator series and the dominated-convergence bound legitimate. Strict positivity of \(a\), not merely nonnegativity, is necessary for rigidity of every coordinate. The strict gap \(\|c\|_1<A\) forces the scalar component to control the norm. The distance proof explicitly maintains the coefficient norm bound and attains the infimum for real and complex coefficients.

As a supplemental finite numerical check only, use the ramp \(u_n^{(k)}=\max\{0,\min\{1,2-n/k\}\}\) with \(k=200\), and truncate the third example's geometric coefficient sequence at index \(54\). Direct finite-array evaluation gives the maximal convolution-to-partial-sums deviations \(1\) for \(c=(1,0,\dots)\), \(0.0050000000000001155\) for \(c=(1,-1,0,\dots)\), and \(0.010000000000000129\) for the truncated zero-sum geometric coefficients; the scalar component with \(a_n=3\cdot2^{-n}\) differs from its norm by below displayed machine precision. The first deviation is not predicted to vanish because its symbol sum is nonzero. These finite calculations are illustrations, not proof or an exhaustive certificate, and truncation of the geometric example introduces a negligible nonzero symbol sum; the exact infinite geometric series is used in the theorem.

The motivating paper was read through its freely accessible full journal text and original preprint record. Specific compared results were Proposition 4.3, Proposition 5.4, Section 6, and Problem 7.3; the last remains an open density question unaffected by the stated relative-family theorem. Equivalent formulations outside the available published literature are not ruled out. The scientific review is a same-model review only; independent audit remains unperformed.
