---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Under point Palm, A,B,C are independent rate-λ gaps and mutuality to the right is exactly B<min(A,C), ignoring zero-probability ties. Condition first on B=b: acceptance weights its density by e^(−2λb), and memorylessness makes the two excesses, conditional on acceptance and b, independent iid rate-λ variables with distribution not depending on b. Normalization is 1/3 and gives B|M rate 3λ. Half-excesses are rate 2λ, giving the claimed common-summand law and product Laplace transform. Its means, variance, covariance and correlation follow from the independent summands; before selection only B/2 is shared, giving correlation 1/2. The smaller selected length is a sum of independent exponentials of rates 3λ and 4λ (the latter from the smaller half-excess), which gives the printed diagonal survival directly. Independently check the posterior by conditioning on the sum A+B=2v: B is uniform on (0,2v), the right event is B<v and C>B, and the disjoint left event has equal probability. Thus P(J|V=v)=(1/v)∫_0^v e^(−λb)db, a strictly decreasing continuous version with the claimed limits. P(J)=2/3. All statements are under the specified sampling law, including at u=0; no numerical simulation is needed for the formulas. The frozen numerical verifier was inspected, not executed.

## originality

PASS

The distinct portion is the bias caused by mutual-neighbor selection in the law of actual adjacent full cell lengths and in the point-Palm posterior given cell length. The selection frequency, shared-gap law, marginal typical-cell law and exponential input are prior or immediate baselines. The strongest inspected prior pair results use a different notion of volume; the strongest general face-Palm theorem describes the configuration before MNN selection and does not evaluate the selected full-cell or size-dependent statistics.

## value

PASS

The nearest-neighbor selection rule is canonical, and a pair of genuine cells is different from the more easily measured shared edge length. The exact joint law quantifies how selecting mutual pairs changes the dependence between adjacent cells. The strictly decreasing posterior further gives a continuous and explicit ascertainment bias for selection by mutuality as a function of cell size, which cannot be read off from the fraction of selected points or the unconditional typical-cell law. These quantities provide a usable exact baseline for selected tessellation statistics; no novel technique or general-dimensional consequence is needed or asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
