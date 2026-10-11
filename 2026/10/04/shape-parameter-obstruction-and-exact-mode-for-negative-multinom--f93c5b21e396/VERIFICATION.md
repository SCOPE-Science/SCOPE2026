---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For integer m, Gamma(r+m)/Gamma(r)=prod_{j=0}^{m-1}(r+j). Therefore the log derivative is sum 1/(r+j)+log q and the second derivative is strictly negative. It runs from +infinity to log q<0, yielding one mode and immediate failure of complete monotonicity for m>=1; m=0 is the exponential q^r. The digamma expansion with r=qm/(1-q)+1/2+b/m gives b=-(1-q^2)/(24q), and the derivative of the mode equation is order 1/m, upgrading the residual to the stated O(m^-2) root error. Independent numerical roots at q=0.2,0.5,0.8 and m through 1000 agreed with the expansion at the expected scale.

## originality

PASS

Ouimet's open-access 2023 paper explicitly asks whether the negative multinomial distribution is completely monotonic in its parameters. The earlier positive theorem concerns multinomial probabilities along a different scaling path. No inspected source gives the fixed-cell ordinary-shape obstruction, the exact harmonic mode equation or its composition-invariant asymptotic. This therefore answers a stated open direction negatively for the retained shape coordinate and replaces monotonicity by an exact one-dimensional profile.

## value

PASS

The theorem gives a decisive obstruction to an explicit published complete-monotonicity question and replaces it with an exact mode law and asymptotics. The short proof does not make the result routine in value: it resolves a named natural property of the negative multinomial family for every nonzero cell.

The dated certificate retains the supplied scientific assessment, sources and limitations.
