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

The claim was checked directly from the definitions.

For fixed nonzero \(\eta\), the projective orbit map \(G\to H\cdot[\eta]\) has uniform fiber size
\[
|K|\,|\operatorname{Stab}_H([\eta])|=\frac{|G|}{m(\eta)}.
\]
For nonzero \(f\in\mathbb C^2\), the condition \(\langle f,\pi(g)\eta\rangle=0\) is equivalent to the single ray condition \([\pi(g)\eta]=[f^\perp]\). Hence a coefficient zero set is either empty or one full projective-orbit fiber, and choosing \(f\) orthogonal to an orbit ray realizes the nonempty case. This proves the exact zero proportion.

For the minimization, each nonidentity element of the faithful finite projective image \(H\subset PU(2)\) has at most two fixed rays in \(\mathbb{CP}^1\). Their finite union cannot exhaust \(\mathbb{CP}^1\), so a ray with trivial stabilizer exists and has orbit size \(|H|\).

Boundary checks: when \(|H|=1\), every coefficient family has a nonzero vector orthogonal to the unique orbit ray and \(p_0=1\); when \(m(\eta)=1\), the same reasoning gives an identically zero coefficient for a suitable nonzero test vector. No numerical or exhaustive computation is needed.

The literature check materially inspected the open-access primary source sections defining \(p_0\), its projective-kernel reduction, sampling interpretation, and later estimate. The later 2025 finite-group phase-retrieval paper was available only through metadata and indexed keywords, which is recorded as a residual originality risk rather than treated as whole-document negative evidence.
