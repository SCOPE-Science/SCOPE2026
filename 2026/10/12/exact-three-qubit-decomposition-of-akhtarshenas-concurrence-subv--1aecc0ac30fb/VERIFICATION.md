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

The proof uses exact finite-dimensional identities. The critical chain is:
\[
A_{ij}^2=\operatorname{Tr}(ho_{ij}\widetilde{ho}_{ij})
=1-\operatorname{Tr}ho_i^2-\operatorname{Tr}ho_j^2+\operatorname{Tr}ho_k^2
=rac12(T_i+T_j-T_k).
\]
Substitution of the three CKW equalities yields
\[
A_{ij}^2=c_{ij}^2+rac{	au}{2}.
\]
Summing yields
\[
A_{\mathrm{tot}}^2=rac12(T_1+T_2+T_3)=rac{3Q}{2}.
\]

The normalization was checked against the defining source's GHZ, W, and Bell-pair-product examples. A direct floating-point evaluation on randomly generated normalized three-qubit amplitudes also checked the spin-flip/purity identity for all three pairs to machine precision; that experiment is only a sanity check and is not used as proof.

The result does not verify any mixed-state extension, higher-party formula, or general LOCC-monotonicity conjecture.
