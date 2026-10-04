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

The analytic proof was checked at the level of definitions, index contractions, quantifiers, and boundary assumptions.

For the convention \(R(X)_{ik,jl}=X_{ij,kl}\), direct contraction gives the two partial-trace identities used in the proof. For locally maximally mixed states these force an orthogonal identity/traceless block split. The resulting relation \(r_k(\rho)=r_k(\widetilde\rho)+1/(d_A d_B)^k\) is exact for every positive integer \(k\).

The bundled `verify.py` constructs deterministic positive examples with maximally mixed marginals in local dimensions \(2\times2\), \(2\times3\), and \(3\times4\). It checks positivity, the marginals, the two null directions, power-sum identities through order four, and \(\sqrt G+1/\sqrt{d_A d_B}\le1\). Successful execution prints `VERIFY_OK`.

These finite computations are implementation checks only. They do not establish the theorem for arbitrary dimensions or moment order; the proof in `RESULT.md` does.
