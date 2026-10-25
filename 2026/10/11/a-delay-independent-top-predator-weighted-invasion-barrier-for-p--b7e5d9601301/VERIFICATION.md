---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For the precise three-equation Wang–Shao–Chai delay system, all parameters r,k,b,a,alpha,m,beta,d,theta,v,p,q,eta,e are strictly positive, both delays nonnegative, and the assumed solution is strictly positive and T-periodic. Integrating x3 prime over a complete period makes the delayed birth integral equal its undelayed counterpart. Normalizing by integral x3 defines dnu=x3 dt/integral x3; hence e/eta=int x2/(v+p*x2+q*x3) dnu. Since q*x3>0, this is strictly below int f(x2)dnu with f(u)=u/(v+pu), strictly concave because f double prime = -2pv/(v+pu)^3<0. Jensen yields e/eta<f(M3)=M3/(v+p*M3)<1/p. Thus eta>pe, and M3>ve/(eta-pe), where M3=int x2*x3/int x3. When tau2=0, division by current x3 and period integration of d log(x3)/dt instead supplies the ordinary-time version. That step is correctly NOT used for tau2>0. The result is conditional on strictly positive periodic solutions and does not assert existence, attraction, Hopf continuation, or an unweighted bound at positive tau2. Strict q and positive x3 matter.

## originality

PASS

Best-of-knowledge, source-specific novelty: the motivating Wang–Shao–Chai 2023 full paper has the static coexistence and local-invasion threshold ve/(eta-pe) but not a universal finite-amplitude periodic weighted-mean barrier, nor the tau2=0 ordinary-mean version. Open full-text comparisons to related delay/Hopf papers use distinct functional responses and do not imply the same-system result. Fresh searches of published findings detected the same assigned record (explicitly EXCLUDED as independent priority evidence) and related mean laws in distinct equations rather than dominating same mathematical model theorems. The Jensen method alone is classical; only the precise model-specific periodic consequence and static-threshold alignment are credited. The 2014 interference/gestation-delay article remains a full-text access risk, NOT evidence of absence.

## value

PASS

The Wang–Shao–Chai source studies Hopf-driven nonstationary predator coexistence and identifies the top-predator invasion level only at equilibria. An explicit necessary bound on the natural x3-weighted abundance of its intermediate predator along EVERY positive finite-amplitude periodic state, valid for arbitrary gestation delays, is a motivated nonlocal invariant of the published model, not a random parameter slice. The same exact threshold as local invasion makes it interpretable and usable as an analytic consistency check for proposed oscillatory branches. The tau2=0 ordinary mean statement clarifies a structurally important boundary in delay placement. It is a precise but modest self-contained mathematical fact: the proof is elementary once the right observable is chosen, it does not yield existence/stability or general permanence, and those limits do not erase its specific usefulness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
