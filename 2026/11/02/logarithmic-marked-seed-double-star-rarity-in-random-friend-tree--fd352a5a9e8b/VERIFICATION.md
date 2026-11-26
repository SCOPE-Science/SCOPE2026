---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The seed attachment probabilities follow by splitting on the sampled vertex. A star must be centered at one of the seeds because their edge persists. Each star orientation has mass 1/(m-1), and from it the unique seed leaf becomes a second hub with probability 1/[m(m-1)], giving total entrance mass 2/[m(m-1)^2]. Interior survival is at least (m-2)/m per step. Substitution of g(k+1)/g(k)=1-1/[k(k+1)] shows that the killed transition of g(a)g(b) equals (1-2/m)g(a)g(b) minus the two positive cross terms displayed. The weight is at least one and starts at K g(m-2). The telescoping product and sum therefore give both finite bounds, including the empty-product case n=4. The logarithm of the product tail is O(1/k), so the upper sum differs from the lower harmonic sum by O(1), which suffices for the normalized bounds and conditional probability. At n=4 and n=5 the recurrence gives R_n=1/6 and 13/72. Inspected but did not execute checker.py; its recorded 720 finite checks are corroboration only. No limit for the normalized constant was inferred.

## originality

PASS

The closely related unmarked result and interior transition are prior coverage, not new here. The supported distinction is the two-sided logarithmic estimate for the original seed bridge, obtained from the rarer ingress and a weighted, uniform size-to-size survival bound not established by the unmarked estimates. Best of available evidence, not a priority certification.

## value

PASS

The original bridge is a canonical marked edge, not an arbitrary filter. Its retention isolates a logarithmic correction invisible in the much more common unrestricted two-hub event. The positive weight proves a uniform critical survival estimate and all-size bounds, not just finite enumeration or relabeling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
