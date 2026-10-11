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

Two truncation hyperplanes from distinct selected vertices cannot meet inside the cube because selected corners have Hamming distance at least two and all depths are below one. Thus the vertices are exactly the untruncated cube vertices together with the \(n\) new edge-cut vertices at each selected corner. Every untruncated cube vertex retains its original tangent orthant, so distinct such vertices require distinct illumination directions, giving the lower bound \(2^n-|T|\). For the matching upper bound, use the negatives of all untruncated cube vertices. At a new cut vertex, independence guarantees that the neighboring original cube corner obtained by flipping the cut coordinate is untruncated; its negative direction strictly enters all active coordinate facets and decreases the active cut inequality by \(n-2>0\). The scaled-cube sandwich gives the Banach--Mazur estimate, and a parity class supplies independent sets of every size through \(2^{n-1}\). The package verifier checks all local inequalities exactly in representative dimensions; the theorem is analytic.

## originality

PASS

Livshyts--Tikhomirov prove the general near-cube upper bound \(2^n-1\) for nonparallelotopes and give a sharp one-corner perturbation with exactly that value. That does not determine simultaneous truncations or any smaller exact value. The audited independent-set construction gives an all-dimensional exact law and realizes the entire high-half spectrum down to \(2^{n-1}\). Targeted Resultary and web searches found no equivalent simultaneous-corner theorem.

## value

PASS

The cube is a central extremal object in the illumination problem, and the cited local theorem leaves open how far exact illumination values can fall under structured arbitrarily small perturbations. The construction gives a complete high-half spectrum near the cube and a sharp combinatorial mechanism controlling it, including the dramatic drop from eight to four in dimension three.

The dated certificate retains the supplied scientific assessment, sources and limitations.
