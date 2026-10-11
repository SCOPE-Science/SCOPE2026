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

The Hilbert coordinate \(\psi_K(x)=\tfrac12\log((x-a)/(b-x))\) is an isometry from \((a,b)\) to the real line, and \(G\) becomes a closed coordinate interval of length \(D_H\). For an ordered convexified-separated sequence on a line, each new point outside the convex hull of its predecessors must extend the running span by at least \(\alpha\), so at most \(\lfloor D_H/\alpha\rfloor+1\) points occur; a monotone equally spaced sequence attains this bound, proving equality with ordinary packing. Direct cross-ratio algebra shows the polar interval pair has the same Hilbert diameter. Arya--Mount Lemma 4.3 then becomes the claimed fully convexified square because ordinary and convexified factors coincide and monotonicity absorbs the \(\eta/2\) factor into \(\eta/4\). Fresh numerical cross-ratio checks on several asymmetric nested interval pairs independently reproduced exact primal--polar equality.

## originality

PASS

Arya--Mount explicitly leave the fully convexified diagonal-product estimate as Problem 5.1 and their Lemma 4.3 retains one ordinary-packing factor. The one-dimensional equality \(M_H=\widehat M_H\) is not stated there and is exactly what removes that factor. The older convexified-packing paper develops the general notion and entropy duality but does not give this Hilbert-interval formula. A targeted Resultary search returned the assigned record as the direct match and no earlier one-dimensional theorem.

## value

PASS

The result resolves the exact one-dimensional base case of a current explicitly stated convexified-diagonal packing problem and identifies the precise mechanism that removes the ordinary-packing factor. Exact primal--polar equality and the closed floor formula give a reusable sanity benchmark for higher-dimensional conjectures rather than a one-off numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
