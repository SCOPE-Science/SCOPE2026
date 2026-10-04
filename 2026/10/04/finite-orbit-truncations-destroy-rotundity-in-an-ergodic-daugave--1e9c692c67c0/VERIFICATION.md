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

The finite-window statement was checked symbolically from its definitions. For nonempty finite \(F\), an integer \(q\notin F-F\) exists. Irrationality of \(\theta\) makes the finitely many points indexed by \((-F)\cup(q-F)\) distinct on \(\mathbb T\), so a sufficiently short interval has pairwise disjoint required translates. The resulting normalized indicators satisfy the exact identity
\[
N_F(\alpha u+\beta v)=|\alpha|+|\beta|,
\]
which directly verifies the isometric \(\ell_1^2\) obstruction.

The uniform approximation estimate was checked by the chain
\[
0\le N(f)-N_F(f)
\le\int\left(\sum_{k\notin F}a_k|f\circ T_\theta^k|^2\right)^{1/2}
\le\left(\sum_{k\notin F}\sqrt{a_k}\right)\|f\|_1.
\]
No numerical computation, finite enumeration, or asymptotic extrapolation is used.

The properties of the full norm were checked against arXiv:2609.12562v1: its norm uses positive weights at every integer orbit coordinate, its ergodic case is wMLUR and Gâteaux smooth and therefore strictly convex, and atomless measure gives the Daugavet property. The first public source date and primary classification were checked from the source record.

Limits: this verification does not prove a corresponding truncation obstruction for every ergodic transformation, and it does not determine the Daugavet property of \(N_F\).
