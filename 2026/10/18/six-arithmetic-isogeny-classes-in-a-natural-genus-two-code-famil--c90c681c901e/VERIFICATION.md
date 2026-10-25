---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For the EXACT finite family over F19, y^2=x^6+a x^3+1, the exhaustive admissibility test excluding a=±2 and rational sextic roots gives A={0,3,4,5,6,7,8,9,10,11,12,13,14,15,16}. Each squarefree monic sextic defines a smooth genus-2 curve with two rational points at infinity. The involution β:(x,y)->(1/x,y/x^3) fixes t=x+x^-1 and w=y(x+1)/x^2, yielding E_a:w²=(t+2)(t³-3t+a) with genus one and rational branch point (-2,0). ζ=7 in F19 is primitive cube root; α:(x,y)->(ζx,y) conjugates β to another involution whose fixed differential lines on <dx/y,x dx/y> differ because ζ!=ζ². The two F19 elliptic quotient pullbacks are tangent-independent and induce an F19-isogeny Jac(C_a)~E_a². Full 19-term quadratic character sums for every a give exactly traces {-7:[7,12],-4:[5,14],-1:[9,10],2:[4,6,8,11,13,15],5:[3,16],8:[0]}, hence L_C(T)=(1-τ_a T+19 T²)² and six isogeny classes by the finite-field abelian-variety Frobenius isogeny criterion. A separate, simple independent Python finite calculation regenerated the fifteen admissible parameters and this entire trace partition and verified first power traces. The archived 15-row certificate further checks F361 values, but those finite checks alone do not imply the all-extension zeta factorization: the isogeny does.

## originality

PASS

A finite, natural parameter-to-arithmetic-isogeny-class partition associated with the published code-hull comparison; prior abstract elliptic quotient theorems and published seven hull profiles do not state this exact six-class map.

## value

PASS

The published coding study isolates all fifteen admissible equations and gives seven hull profiles, with a concrete nonisomorphic equal-profile pair. Classifying every member by arithmetic Jacobian isogeny gives a different intrinsic exact invariant, a six-class partition and every extension-field point-count numerator. This complete natural finite classification has a motivated object/invariant and precise future use in arithmetic code-curve comparisons; it is not merely a random small modular table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
