---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The endpoint Markov presentations for a=3/7 and a=4/9 have characteristic polynomials respectively (lambda-1)(lambda+1)(lambda^2-lambda-1)(lambda^2-lambda+1) and (lambda-1)(lambda+1)^3 times the same quadratics. Both Perron roots are phi; survivor inclusion proves constant entropy over the interval and an expanding-cylinder Frostman argument proves dim_H=log(phi)/log2. Refinement by both endpoint grids yields only three recurrent SCCs; any periodic point in either newly retained open annulus must follow the forced six-cycle. Its six-step affine branch has unique fixed point at the OLD forbidden boundary, so no intermediate periodic points enter. At a=4/9 exactly two primitive boundary three-cycles are newly retained. Orientation-reversing side-address corrections give tr A3^n-P_n=(-1)^n and tr A4^n-P_n=3(-1)^n-6 1_{3|n}, which yield the stated rational zeta functions; 0 is one circle fixed point. Independently reassembled both exact matrices and enumerated all geometric periodic points for periods 1..12 at both endpoints and a sample interior parameter; the all-period assertion rests on the SCC and boundary argument, not this finite test.

## originality

PASS

Ding–Steiner–Sun arXiv:2610.03327 already gives the positive-entropy golden-mean value at the 4/9 kneading endpoint and a general dimension framework, which is explicitly excluded from new priority. The assessed contribution is the entire [3/7,4/9) frozen geometric periodic-point set and explicit two-three-cycle endpoint jump, not merely an entropy plateau. Qualified PASS against examined statements, with specialized past dynamical-zeta literature as residual risk.

## value

PASS

A natural pair of rational Markov hole boundaries yields a sharp distinction between entropy plateaux and Artin–Mazur zeta plateaux: entropy stays positive and constant while the entire geometric period census remains fixed and then jumps only at one endpoint. The exact Lucas/cosine fixed-point count is a useful dynamical invariant invisible to entropy and dimension alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
