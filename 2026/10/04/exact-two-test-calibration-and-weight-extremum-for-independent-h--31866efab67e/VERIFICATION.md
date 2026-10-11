---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The event geometry was reconstructed directly. For \(0<h<1\) and \(0<w<1\), conditioning on \(U=u\) gives a single lower threshold for \(V\) above \(a=hw/[1-h(1-w)]\); exact integration yields the displayed CDF. Setting \(t=w(1-w)\) makes the excess \(h^2 t\log(1+A/t)\), \(A=(1-h)/h^2\). Its derivative is \(h^2[\log(1+x)-x/(1+x)]>0\) for \(x=A/t>0\), so the unique maximum is at \(w=1/2\). Independent numerical integration at several interior parameter pairs reproduced the closed form; the endpoint weights reduce to a single uniform p-value. The equal-weight value at \(h=0.05\) and calibrated root also reproduce the stated numbers.

## originality

PASS

Originality passes for the arbitrary normalized two-weight law and strict weight extremum, not for qualitative anti-conservatism or the equal-weight specialization. Chen et al. prove strict sub-uniformity of weighted harmonic means under independence, so the sign of the calibration error is prior. Li's thesis is credited with the equal-weight two-uniform formula. The inspected sources and targeted/Resultary searches did not supply the exact arbitrary-weight distribution, its reduction to \(w(1-w)\), or the theorem that equal weighting uniquely maximizes finite-sample inflation for every threshold.

## value

PASS

Two-test combination is the smallest nontrivial finite HMP setting, and exact null calibration is operationally important because direct HMP interpretation is known to be anti-conservative. The theorem quantifies the full deterministic-weight dependence and identifies the uniquely worst weighting, furnishing a precise finite-sample benchmark rather than a routine restatement of sub-uniformity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
