---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

For 1<p<=2 let q=p/(p-1), A=||kappa x+tau y||p, B=||kappa x-tau y||p. The standard Clarkson conjugate-exponent inequality yields A^q+B^q<=2(kappa^p+tau^p)^(q/p); AM-GM then yields sqrt(A B)<=(kappa^p+tau^p)^(1/p). Unit vectors on disjoint coordinates achieve equality in both signs. At p=1 the triangle inequality A,B<=kappa+tau and the same disjoint pair is sharp. For p=infinity the triangle inequality gives kappa+tau and x=e_i+e_j,y=e_i-e_j achieves it for both signs. At p=2 the formula matches 2^(-1/p)((kappa+tau)^p+|kappa-tau|^p)^(1/p). Quantification requires only two coordinates, arbitrary positive parameters and real standard ell_p; no finite sampling extrapolation.

## originality

PASS

Best-knowledge PASS for the complete sub-Hilbert two-parameter product law; the 2025 paper publicly introduces this two-parameter invariant and the frozen research package attributes to its Example 1 the p>2 formula. Its primary arXiv abstract was accessible, but its full text could not be independently read, so no whole-document NOT_COVERING finding is claimed. A published exact generalized James min-type law and skew arithmetic-mean ell4 law have different objectives and do not logically supply the product upper bound for 1<=p<=2. The older 2008 ancestor is one-parameter and remains a real equivalent-formulation risk. Absence of full focal text or completed Resultary search is a material risk, not novelty proof.

## value

PASS

Completes the natural missing 1<=p<=2 portion of the recently defined two-parameter geometric-mean constant for the canonical ell_p sequence family, including both norm endpoints. Equality changes from disjoint supports to balanced two-coordinate geometry at p=2 when combined with the cited super-Hilbert branch. A natural full exact family is a reusable geometric benchmark, not an arbitrary finite instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
