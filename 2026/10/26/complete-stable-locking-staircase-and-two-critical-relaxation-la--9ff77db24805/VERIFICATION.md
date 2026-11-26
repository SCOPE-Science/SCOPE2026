---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

With coupling K per neighbor, equilibrium forces constant sine on each parity and their odd-minus-even difference is a/K. The signed cycle form is evaluated on exactly the zero-sum space of edge differences. Two negatives, or a negative and a zero, are excluded by equal opposite edge differences. Against a single conductance −c, the other m−1 edges of that parity have +c; taking differences 1 on the negative edge and −1/(m−1) on those gives −c+c/(m−1)<0. Vanishing conductances alone delete an entire parity and create extra zero modes. Thus strict stability requires acute increments. The winding condition and monotone sine difference for d∈(0,π−|2πq/m|) give precisely one labelled phase class per q with 2|q|<m and K>K_q, excluding threshold equality. The Fourier blocks give both spectral bands; all minus modes lie at or below −(u+v), and r=1,m−1 in the plus band gives the slowest nonzero rate. At q=0 both conductances equal sqrt(K²−a²/4); at nonzero q the weak conductance is aε/sin(2π|q|/m)+O(ε²) while the other stays positive. Expanding the exact full gap yields the stated coefficients, powers and remainder orders, with fixed m,q,a. Winding signs interchange the two conductances.

## originality

PASS

Pass is for the repaired paired sharp full-space spectral relaxation laws and the winding-resolved coefficients. General signed-cycle stability and previously known alternating branch relations cover the underlying stability exclusion and threshold method; those and the standard period-two Fourier formula are not claimed independently. The same-family primary source treats reduced stability exchanges and discusses the need for a full-space classification, but the inspected passages do not give the least transverse eigenvalue's paired sharp laws over all windings.

## value

PASS

Two different critical slowing-down rates occur on stable branches of the same homogeneous cycle with the same detuning pattern. The exact winding and size dependence of the slowest transverse time scale distinguishes all-link collapse from weak links between surviving dimers, even in the presence of multiple vanishing modes at a threshold. The full-space coefficient is useful for estimating the slow approach of perturbations and is not given by a reduced stability exchange. Standard Fourier band formulas or the already-covered branch count alone are not the basis of this value judgment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
