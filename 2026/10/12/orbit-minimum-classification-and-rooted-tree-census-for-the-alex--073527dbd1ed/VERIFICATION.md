---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Closure in an upset Alexandrov chain is downward closure and F is zero-inclusive eventual orbit reachability. For any singleton valuation {f^t(y)}, Alex at x<=y forces some forward iterate of x to be <=f^t(y), hence q_f(x)<=q_f(y). Conversely monotone minimum q_f lets x visit its minimum, proving the full all-valuations implication. The orbit minimum is regressive q(x)<=x and idempotent; when monotone it is the floor retraction onto its fixed roots 0=s1<...<sk, with consecutive fibers B_i. Every nonroot x∈B_i must stay within B_i until reaching s_i, yielding a unique oriented spanning tree, while root s_i may send to any vertex at or above s_i; such choices give exactly q_f as the block-floor map in reverse. There are τ(b)=b^(b−2) rooted trees of each b>=2 and n−s_i root successors, so composition-product census and recurrence count without overcounting. Independent enumeration of all n^n functions through n=6 gave [1,4,24,188,1825,21420], and independently evaluated every valuation for n<=4; analytic proof covers all n.

## originality

PASS

Vooijs–Fernández-Duque establish monotone/continuous temporal maps validate Alex as used in ordinary dynamic-topological semantics; here f is arbitrary, including discontinuous, and all-valuations validity is classified precisely by monotonicity of orbit minima, followed by a labeled tree census. Previous continuous-map axiomatization does not imply the unrestricted endofunction classification.

## value

PASS

The exact boundary between topological continuity and validity of the prominent Alex closure/eventuality axiom is a structural modal-logic question. Its orbit-minimum criterion characterizes a substantial class of discontinuous maps; the novel rooted-tree decomposition and explicit integer census make that boundary calculable for all finite chains. The result is a natural complete classification, not a mere reparameterization of the standard Cayley formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
