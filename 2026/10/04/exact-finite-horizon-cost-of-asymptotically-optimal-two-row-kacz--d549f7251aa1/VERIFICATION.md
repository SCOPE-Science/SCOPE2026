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
# Verification

The algebraic checker reconstructs \(T_\omega\) from the two relaxed row projections and verifies:

- \(\|T_\omega a^\perp\|_2^2=c^2+s^2(\omega-1)^2\), which certifies the unique one-sweep minimizer \(\omega=1\).
- \(\operatorname{tr}(T_\omega)=c^2\omega^2-2\omega+2\), \(\det(T_\omega)=(1-\omega)^2\), and the factorized characteristic discriminant.
- At \(\omega_\star=2/(1+s)\), the decomposition \(T_{\omega_\star}=qI+N\) satisfies \(N^2=0\) and the stated exact Frobenius norm.
- The power-norm formula is replayed for several exact rational values of \(s\) and integer horizons by comparing it with the largest singular value obtained from \((T^k)^\top T^k\).
- The small-angle expansion of \(\log R_k(s)\) under \(k=\alpha/\sqrt{s}\) has leading coefficient \(\alpha(1-4\alpha^2/3)s^{3/2}\).

The finite replays are consistency checks only. The proof of the all-horizon result is the nilpotent identity \(N^2=0\), not enumeration. No claim is made for more than two rows, inconsistent systems, randomized selection, or row-dependent relaxation.
