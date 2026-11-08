---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Write Q={su+tv:-1<=s,t<=1}, a=|u|, b=|v|, c=u·v, L=4(a+b), A=4sqrt(a²b²−c²). Exact edge integration gives I_f(Q)=2b∫f(a²+b²t²+2ct)dt +2a∫f(b²+a²t²+2ct)dt over [-1,1]. Pairing t and −t with Jensen shows skew c cannot reduce any convex f(squared radius). For c=0, the rectangle integral is G_f=4∫0^a f(x²+b²)dx+4∫0^b f(y²+a²)dy; varying b at fixed a+b produces derivative 8ab∫0¹[f′(a²t²+b²)−f′(b²t²+a²)]dt≤0 for a>=b, with strictness for strictly convex C¹ f. Consequently equal-perimeter square is minimal in convex order, and E(r²)=L²/48 is constant. Power exponents p outside [0,2] minimize, inside maximize at square, with endpoints constant; boundaries exclude origin so p<0 finite. Exact quartic integration gives E4=L⁵/1280−LA²/12, explicitly known from earlier fourth-chord boundary m4 calculation. For shape-independent C² f, varying c and taking its second derivative at c=0, then b→0, yields ∫0^a z² f′′(z²)dz=0 for all a>0, hence f′′≡0; conversely affine f is invariant. Independently rationally integrated E2/E4 in representative orthogonal and skew systems and inspected symbolic verifier; these finite points corroborate, never prove, the convex-order functional inequality.

## originality

PASS

Best-of-knowledge originality: final statement and implication level compared to overlapping primary literature and published mathematical records, including already-known subcases. The audited result implies all convex f inequalities and power-weight reversal/rigidity, strictly beyond the existing invariant and distinct from chord-distribution laws.

## value

PASS

This is a distributional comparison for every convex weight, including nonmonotone tests, not merely a known quadratic invariant or a single polynomial moment. The sharp power-exponent phase transition and C² rigidity explain which weighted perimeter measurements are shape-sensitive in a natural four-sided geometric family; the mathematical question is motivated without a need for a paper-sized downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
