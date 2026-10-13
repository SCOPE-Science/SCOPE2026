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

The proof is analytic. The following checks were carried out against the packaged claim.

1. Reconstructed the source symmetric translation-invariant equation and verified that it becomes \(P(s)=c_1s^{k+1}-c_2s^k+s-1\) with \(c_1,c_2>0\).
2. Differentiated \(q(s)=c_1s+(s-1)/s^k\) and verified \(q'(s)=H(s)/s^{k+1}\), where \(H(s)=c_1s^{k+1}-(k-1)s+k\).
3. Located the unique minimum of \(H\) and derived the exact threshold \(c_1^*=((k-1)/(k+1))^{k+1}\).
4. Eliminated \(c_1\) at a stationary point to obtain the exact fold parameterization and checked the ordering of the two folds from the monotonicity intervals of \(q\).
5. At the merger point, checked \(P=P'=P''=0\) and \(P^{(3)}=k(k-1)((k-1)/(k+1))^2>0\), proving exact triple multiplicity.
6. Replayed the bundled `verify.py`. It checks the cusp identities exactly for orders \(2\) through \(20\), representative fold configurations and numerical root counts for several orders, and reconstruction of positive physical coefficients. The script prints `VERIFY_OK cusp_orders=2..20 fold_orders=2,3,4,6,10`.

Finite numerical checks are corroborative only and do not establish the all-order theorem.
