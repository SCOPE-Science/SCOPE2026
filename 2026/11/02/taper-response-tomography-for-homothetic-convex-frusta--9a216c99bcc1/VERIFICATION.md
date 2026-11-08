---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The statement concerns exact population mean projection widths of F_s=conv((1+s)K at +H/2,(1-s)K at -H/2), with compact full-dimensional origin-containing planar convex K and known H. For u=(sqrt(1-t²)v,t), t>=0, the support-max calculation gives w_s=a[(1+s)p+(1-s)q]+Ht+(2saq-Ht)_+, where p=h_K(v), q=h_K(-v). Averaging p-q over uniform v cancels the first-order term; the elementary hinge integral equals (b/2)atan(b/H) with b=2s q. This proves E(W_s-W_0)=s E[h_K(V)atan(2s h_K(V)/H)]. Compact-support moment determinacy of positive h² makes the entire response exactly equivalent to its support-value histogram; it does not reconstruct K. Pointwise convexity in the taper and reflection symmetry of the width distribution yield increasing-convex order, strict for strictly increasing convex tests; K=-K gives pointwise order. Independent direct support maxima and numerical hinge integrals on an asymmetric triangle at four s matched the formula. Numerics do not replace analytic proof.

## originality

PASS

The mean-width arctangent response and all-even-moment recovery for homothetic frusta appear not to be supplied by the inspected prior volume and unlabeled-projection papers; classical support/convexity facts are acknowledged and not treated as new. Best-of-knowledge original with specific stereological priority risk.

## value

PASS

Exact one-parameter population measurements recover the complete distribution of support heights for every planar convex base, a natural and nontrivial geometric tomography fact. The even-moment readout and precise non-identifiability boundary are useful beyond basic convexity, despite no finite-sample or shape reconstruction theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
