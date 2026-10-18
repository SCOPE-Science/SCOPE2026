---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The gradient of f_p(x)=product_i(x_i/sqrt(p_i))^p_i is f_p(x)(p_i/x_i)_i. For V={a·x=0} with a mixed-sign normal, everywhere orthogonality along V∩S_p is sum_i a_i p_i/x_i=0. Positive homogeneity extends the identity to all positive x in V. With y_i=a_i x_i (a_i>0) and z_j=-a_j x_j (a_j<0), equal masses and equal reciprocal sums must hold for all positive redistributions; a sum c_r/t+c_s/(C-t) is not constant for any two positive coefficients. Hence exactly one positive and one negative a_i, and a_i²p_i=a_j²p_j gives the weighted pair seam. Converse by direct gradient evaluation, yielding exactly binomial(d,2). Tested representative d=2..9 gradient identities and nonpair reciprocal obstructions; analytic simplex argument proves all d and weights.

## originality

PASS

Makarov–Protasov Proposition 3 constructs a weighted pairwise-coordinate seam for the canonical smooth self-dual antinorm, but does not prove that arbitrary orthogonal linear hyperplane seams must be of this form. This result supplies the converse through independent variation of reciprocal sums. Resultary search found exact self only; other weighted norm/duality findings do not cover the full seam classification.

## value

PASS

A full natural classification of everywhere orthogonal linear seams in an explicit canonical antinorm family, establishing exact rigidity and identifying the scope of admissible lifting geometry; motivated by a stated broader open nonadmissible-splitting question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
