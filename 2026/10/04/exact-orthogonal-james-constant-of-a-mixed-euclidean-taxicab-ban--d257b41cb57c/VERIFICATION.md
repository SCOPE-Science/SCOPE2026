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

The unit sphere is exhausted by smooth Euclidean arcs, interiors of taxicab segments and the four nonsmooth axis junctions. On a Euclidean arc, the unique norming functional forces the orthogonal direction and gives a contribution at most \(\sqrt2\). On a taxicab segment, the corresponding diagonal orthogonal direction again gives at most \(\sqrt2\). At \(x=(1,0)\), using the full support-functional interval reduces every admissible orthogonal unit vector to \(y=(a,\sqrt{1-a^2})\), \(0\le a\le1/\sqrt2\), with \(F(a)=\sqrt{2(1+a)}\) increasing and \(G(a)=1-a+\sqrt{1-a^2}\) decreasing. Their unique crossing is therefore the global axis maximum, and the substitution \(t=\sqrt{(1-a)/(1+a)}\) converts it to \(t^4+2t^3-1=0\). The positive-root monotonicity and independent algebraic elimination reproduce the stated exact constant and equivalent polynomial.

## originality

PASS

The defining primary source studies exactly this mixed Euclidean--taxicab plane in Example 5.4, says the calculation of \(J_\perp\) is nontrivial, and records only \(J_\perp\approx1.626\) with an approximate extremizing coordinate \(a\approx0.321\). It omits the exact algebraic value, a derivation, and a proof that all sphere branches have been globally exhausted. The audited theorem supplies that missing exact support-functional classification and algebraic crossing. Resultary returned the assigned exactification as the only exact match for this example.

## value

PASS

This is the specific nontrivial example singled out in the paper studying the orthogonal James parameter. Replacing a source-level unexplained decimal by a rigorous exact algebraic value, a complete branch classification and an explicit maximizing orbit gives a natural exact invariant for a canonical mixed Banach plane rather than an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
