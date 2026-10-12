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

The universal proof is sheaf-theoretic and topological, not computational.

For \(n\ge3\), the minimal type-\(A\) nilpotent orbit \(U_n\) is the complement of the zero section in \(T^*\mathbb P^{n-1}\), hence deformation retracts to an \(S^{2n-3}\)-bundle over \(\mathbb P^{n-1}\). Because \(2n-3\ge3\), the low-degree Serre--Gysin sequence gives
\[
H^1(U_n;\mathbb C)=0,\qquad H^2(U_n;\mathbb C)\cong\mathbb C.
\]
Juteau's integral cohomology table independently confirms these groups.

The cone \(X_n\) is contractible, so the localization sequence identifies the first nonzero vertex-local group with
\[
H^3(i^!\mathbb C_{X_n})\cong H^2(U_n;\mathbb C)\cong\mathbb C.
\]
Xu's Proposition 3.3 therefore gives \(S_3\) and failure of \(S_4\).

For the categorical statement, \(U_n\) is simply connected. Xu's Proposition 3.5 turns every \(S_2\) constructible sheaf into the direct image of a local system on \(U_n\); all such local systems are constant, so every \(S_2\) object is a finite direct sum of \(\mathbb C_{X_n}\). The same degree-three local group excludes every nonzero direct sum from MCM.

`verify.py` checks only the dimension and degree inequalities used in this reasoning for a broad finite regression window. It does not certify the infinite theorem and is not used as a replacement for the proof.
