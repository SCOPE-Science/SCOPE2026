---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

On an arbitrary Grassmann chart after permuting coordinates, write [s:t:as+ct:bs+dt]. In characteristic 3 the restricted quartic has exactly coefficient equations 1+a^4+b^4=0, 1+c^4+d^4=0, a^3c+b^3d+lambda ab=0, ac^3+bd^3+lambda cd=0, lambda(ad+bc)=0. For lambda≠0 the zero/nonzero coordinate cases lead to contradictions; when all entries nonzero, ad+bc=0 implies (c,d)=u(a,-b), u^4=1 and the two mixed equations force lambda ab=0. At lambda=0 classify coordinate-pair lines (three partitions times 4^2=48), and nonzero configurations (a,d,r)∈mu_4^3 giving 64. On smooth quartic each line has N_{L/X}=O(-2), thus four-coordinate restricted Jacobian injective rank 4; formal implicit elimination of first four equations gives lambda q(lambda). At coordinate-pair q(0) nonzero, local ring k; at [s:t:s+t:s-t] q(0)=0, independently recomputed tangent derivatives (-1,1,1,1) and q′(0)=1 in F_3, giving k[epsilon]/epsilon²; diagonal mu_4 symmetry covers 64. Independent modular Jacobian check confirms local obstruction and orbit counts; finite F9 source verifier is supporting evidence, not proof over algebraic closure. Count 48+64·2=176.

## originality

PASS

Best-of-knowledge PASS for the full relative Fano scheme, including local nonreduced deformation lengths and absence of lines on all nonzero members of a specified coefficient-marked pencil. The 112 Fermat lines and the Dwork geometry are prior results; neither implies this family scheme calculation.

## value

PASS

A naturally defined relative Hilbert scheme of an important quartic K3 pencil has a subtle 112-support versus 176-length discrepancy. The distinction of 48 immediate obstructions and 64 first-order yet second-order obstructed lines is a substantive geometric deformation invariant, independent of classifying all K3 deformations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
