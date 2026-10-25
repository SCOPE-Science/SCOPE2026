---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Pass to log-odds t=log(x/(1-x)), set S(t) sigmoid, T=t-a(S(t)-b+cq), Q=(1-k)q+k(p0+p1*S(t)). Eliminating q from the second gives exact one-dimensional fiber equation h_B(t)=t-B*S(t)=z with B=a(1-c*k*p1/(1-k)) and z=T-ab+ac(Q-kp0)/(1-k). Each real t solves for one unique real q. Since h_B prime=1-B*S*(1-S) and max S(1-S)=1/4, B<4 yields analytic global diffeo, B=4 a strictly monotone cubic critical point at t=0 (h4=-2+t^3/12+O(t^5)) and inverse Hölder exponent sharp 1/3. For B>4 there are two simple turning points ±2 atanh(sqrt(1-4/B)), with 3 real inverse roots inside their height strip, 2 on edges and 1 elsewhere. Width Bd-4atanh(d)>0 with leading (B-4)^(3/2)/3. For physical (x,q) in (0,1)^2, local fold paired roots retain q in (0,1) by continuity, proving noninjectivity iff B>4, while B<=4 implies global injectivity. Rearranging B<=4 gives k_inj=(a-4)/(a-4+a*c*p1) for a>4; k>=1/(1+c*p1) ensures B<=0 for every a>0. Domain includes k strictly less than 1; do not conflate ambient 3 with 3 physical preimages. Independently checked 15 numerical log-odds inverse elimination and strip-root cases; analytic calculus establishes all real parameters.

## originality

PASS

Best-of-knowledge statement-and-implication originality check after current primary reading and published-Resultary search. Equivalent forms, broader theorems, exact tables, and prior implication are assessed separately; residual risks are not hidden. An elementary 1D logistic slope criterion implies the form h_B prime after independently deriving the correct 2D inverse reduction; prior dynamics papers do not supply that reduction or sharp physical embedding threshold for this model.

## value

PASS

Global inverse multiplicity and sharp adaptation-dependent injectivity for the exact published risk-sensitive belief-learning model isolate folding independently from stability/chaos. It is mathematically motivated to know when belief feedback restores invertibility even at arbitrarily large learning intensity; the full fold strip, physical restriction and cubic cusp refine familiar one-dimensional logistic slope calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
