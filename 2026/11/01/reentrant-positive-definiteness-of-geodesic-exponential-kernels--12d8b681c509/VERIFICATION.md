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
# Verification of six-cycle reentrant positivity

## Reproduction
Run `python3 verify_cycle_reentrant.py` with a standard Python 3 installation. Only the standard-library `fractions` module is needed. On success, the last output line is `ALL_UNIFORM_REENTRANT_C6_CHECKS_OK`.

The program uses positive integer powers to compare \(2^{647/300}\), \(2^{653/300}\), \(3^{647/300}\) and \(3^{653/300}\) to consecutive rationals with denominator \(10^6\), then exploits monotonicity over the full exponent interval. It encloses \(\exp(-x)\) from below by its odd Taylor polynomial of degree \(71\) and from above by its even Taylor polynomial of degree \(70\). The signed Lagrange remainder theorem establishes those inequalities for every \(x\ge0\), not just the tested arguments.

The script builds exact rational intervals for all four Fourier eigenvalues, at each of the three exact rational bandwidths. It verifies the sign vector \((+,+,+,+)\) at \(7/25\), \((+,+,+,-)\) at \(2/5\), and \((+,+,+,+)\) at \(3/5\). The multiplicities of the four eigenvalues are \((1,2,2,1)\) by the discrete Fourier diagonalization. Therefore the full matrix at the middle bandwidth has precisely one negative eigenvalue and five positive eigenvalues.

## Checked exact margins
For every \(p\in[647/300,653/300]\), the exact enclosures imply \(L_2(7/25)>0.004\), \(L_3(7/25)>0.002\), \(L_3(2/5)<-0.017\), and \(L_3(3/5)>0.033\). All other sectors have certified positive bounds, reported in the verifier output.

## Limits
No floating-point eigenvalue table is used as proof. The calculation does not classify the exact transition locations, other cycles, other exponents or the number of positive-definite components. Scientific significance and originality rely on separate argument and literature comparison, not on the checker alone. Independent audit has not been performed.
