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
# Reproducibility and proof checks

The provided `VERIFY.py` is a self-contained Python 3 script using only exact integer arithmetic. It checks the direct quotient gap criterion \(pn\notin\langle a,a+1\rangle\) against the finite residue-minimum formula on 3,234 pairs \(2\le p\le50\) and \(p<a<3p+15\), and checks every proper-divisor witness in this range. It verifies the rigid branch on multiples of \(p\). The check also tests larger divisor-witness ranges through \(p=200\). Execution prints `VERIFY_OK` with counts and exits nonzero on any discrepancy.

To reproduce: extract all packaged files to a directory and execute `python3 VERIFY.py`. No network, external packages, symbolic algebra, or floating point are required.

For the infinite proof, inspect the admissible gap map, the inequality \(ia+j<pa\) for \(i<p\), the identity \(p-1-(d+p/d-2)=(d-1)(p/d-1)\), the modular congruence of the witness, and the CRT polynomial-branch argument. Finite verification is not a certificate that a formula holds for all \(p\).

No independent audit or independent validation has been performed. The checked scientific hypotheses are fixed integer \(p\ge2\) and all integer \(a>p\). The result does not classify general two-generator semigroup quotients or the number of distinct branches.
