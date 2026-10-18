---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Verified against Bogachev–Rozikov primary equations (2.35)-(2.41), viewed rendered pages 18 and 58: set b=theta(theta+q-2)/(q-1), b_c=((k+1)/(k-1))^2, roots x_±=rho+(k-1)(b-b_c)/2 ±sqrt(k(b-b_c)+(k-1)^2(b-b_c)^2/4). On folds log a(x)=k log((k-1)x-1)-k log k-(k+1)log x. At rho=(k+1)/(k-1), Lprime=0, Ldoubleprime=-(k-1)^2/[k(k+1)] and Ltripleprime=2(k-1)^3(2k+1)/[k^2(k+1)^2]. The symmetric root difference cancels order sqrt epsilon and yields (k-1)^4/(3 sqrt k (k+1)^2) epsilon^(3/2), and bprime(theta_c)=(2theta_c+q-2)/(q-1). Dividing by log theta_c yields stated C>0 for all k,q>=2. Independent symbolic differentiation and numerical k,q examples corroborated; remainder O(delta^2) is valid (weaker than next order), q=2 halves use source antisymmetry. Not a statement about other multi-colour Gibbs phases.

## originality

PASS

Bogachev–Rozikov 2019 primary text provides *exact* fold functions and identifies cusp, and Proposition 6.17 obtains only derivative zero (little-o linear) at q=2. The primary source does not state the exact first nonzero 3/2 width term or all-(k,q) amplitude. The proposed calculation is a natural quantitative refinement of the known fold curves, and contains a cancellation requiring a third derivative; prior exact formulas are acknowledged completely. Best-of-knowledge PASS for the explicit normalized leading cusp invariant, with a substantive implication risk that an editor may regard expansion of known closed folds as a routine derivation.

## value

PASS

The fold separation is the exact width of the three-positive-root field strip studied in the original phase diagram. Its critical exponent 3/2 and positive all-parameter amplitude quantify a physically natural cusp degeneracy and sharpen the original q=2 little-o bound. The source motivated this local invariant before computation; no global Gibbs-measure count is suggested.

The dated certificate retains the supplied scientific assessment, sources and limitations.
