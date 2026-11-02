---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

The audited theorem uses Euclidean ellipse E_{a,b} with a>=b>0 and bisections by boundary-to-boundary simple curves; neither equal-area pieces nor nonlinear minimizer uniqueness is assumed. Frozen seven Git blob identities reproduce tree 320a733b712eef5039cae3e0808422f603f62a40, and current GitHub files match their snapshot blobs. The chord identity |r(t)-r(s)|²=4sin²d(a²sin²m+b²cos²m) holds for r(t)=(a cos t,b sin t), m=(t+s)/2, d=(t-s)/2. On the minor-axis half ellipse m ranges [pi/2+d,3pi/2-d], the maximum bracket occurs at arc endpoints and the diameter squared becomes max_{u∈[0,1]}4u[a²-(a²-b²)u]. If a²<=2b², max=4b² at u=1; otherwise the vertex u*=a²/(2(a²-b²)) gives a^4/(a²-b²). Every other central cut at t0<pi/2 is strictly worse for noncircular ellipses: the cut chord L(t0)>=2b handles the round regime; for a²>2b², cuts t0<=d* have L(t0)²>=L(d*)²=2a²>M², while d*<=t0<pi/2 admit boundary pair s=t0,t=pi+2d*-t0 of squared distance 2a²sin²(pi/2+d*-t0)>M². The published 2018 Proposition 3.1 transfers the centerline optimum to all admissible bisections. The circle a=b and threshold a²=2b² agree continuously. Independent SymPy evaluations checked the endpoint quadratic, vertex, chord formula and transition, but are not used as an infinite proof; packaged verify.py and its saved log are not treated as primary evidence.

## originality

PASS

Best-of-knowledge and narrowly scoped: 2004 endpoint-farthest-point and 2018 arbitrary-bisection center-line reduction/minor-axis optimality are prior. The 2018 full text contains neither an explicit all-eccentricity semiaxis value nor the sharp switch at a/b=sqrt(2) nor the strict uniqueness argument for noncircular center cuts. Searches of exact algebraic formula, alias terminology, Resultary and general bisection sources found no independent quantitative-and-rigidity covering statement. That the formula is a short, fairly direct corollary of the 2018 endpoint-max formula is a substantive residual priority/value concern; this verdict does not claim an independent optimization reduction or historical priority certainty.

## value

PASS

Maximum relative diameter is precisely the fencing invariant in the cited literature, and ellipses are a canonical complete one-parameter family for which the 2018 source specifically identifies the optimal cut without quantifying its performance. The exact all-aspect-ratio curve identifies a genuine active-farthest-pair phase change at sqrt(2) and gives strict optimal centerline orientation for every noncircular ellipse. It is a closed geometric benchmark rather than an arbitrary parameter slice, though it uses known qualitative reduction and elementary calculus and makes no claim of wider theory or nonlinear minimizer classification. As an explicit natural-family invariant and sharpened orientation classification, it meets the narrow self-contained-value threshold; it is not represented as a large new theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
