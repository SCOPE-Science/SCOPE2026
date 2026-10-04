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
The proof has three exact stages.

First, every subgroup is either a kernel subgroup \(P_i\) or a subgroup
\[
H_{i,t}=P_i\langle x^t y\rangle.
\]
At level \(i\), parameters are taken modulo \(P_i\), giving exactly \(p^{a-i}\) subgroups.

Second, two \(q\)-containing subgroups permute exactly when they are comparable. An incomparable pair has intersection with no \(q\)-part, so if its product were a subgroup then its order would be divisible by \(q^2\), contradicting the complete subgroup classification.

Third, a subgroup \(H_{j,t}\) has:
- all \(a+1\) kernel subgroups as partners;
- \(S_j\) \(q\)-containing subgroups below it;
- \(a-j\) \(q\)-containing supergroups.

Hence its exact partner count is
\[
2a-j+1+S_j.
\]
Summing these counts over the subgroup lattice of \(H_{i,t}\) yields the formula in the finding.

The packaged checker `artifacts/verify.py` constructs the semidirect products for
\[
(p,a,q)=(3,2,2),\ (3,3,2),\ (5,2,2),\ (7,2,3),
\]
tests every listed subgroup pair for permutability by direct set products, and verifies every relative degree. In the first case it also exhausts all one- and two-generator subgroups.

It returns `VERIFY_OK`.

Finite enumeration is not used to prove the universal theorem.
