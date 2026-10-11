---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Invariance applied to arbitrary antiderivatives of continuous functions of \(z\) gives \(\mathbb E[y^2-a\mid z]=0\), hence \(\mathbb E[y^2]=a\). This immediately excludes \(a<0\); for \(a=0\), \(y=0\) almost surely and the exact identity \(L(xy)=y^2-x^2-xyz\) forces \(x=0\), leaving precisely the equilibrium line. For \(a\ne0\), the exact pointwise identity \(LQ=-2az\) yields \(\mathbb E[z\mid Q]=0\). Integrating \(L(zQ)=(y^2-a)Q-2az^2\) gives the covariance identity. Strict positivity for \(a>0\) follows because \(z=0\) almost surely on an invariant compact support would force \(y^2=a\), constant nonzero \(y\), and then unbounded \(x\). Zero means plus nondegeneracy yield both signs of \(y\), \(z\), and \(y^2-a\); periodic continuity gives two crossings. The inspected verifier checks all load-bearing polynomial identities exactly.

## originality

PASS

The full 2017 same-object paper proves the complete \(a=0\) invariant-sphere foliation and explains that for \(a\ne0\) those spheres cease to be invariant algebraic surfaces; the 2018 paper proves absence of invariant algebraic surfaces/polynomial first integrals and studies periodic/KAM dynamics. Those results do not imply the audited conditional stationary-temperature law, the shellwise condition \(\mathbb E[z\mid Q]=0\), or the strict covariance identity for every compact invariant probability. Thermostat literature makes the integrated temperature balance natural, but no checked source supplied the stronger conditional and radial statements.

## value

PASS

The result gives a natural statistical replacement for the exact spherical first integral present at \(a=0\): a shellwise zero-drift law and a strictly positive radial--kinetic covariance for every compact recurrent statistical state. It also completely settles existence of compact invariant probabilities for \(a\le0\) and forces concrete recurrence crossings for \(a>0\), which is meaningful structural information in a classical thermostat/chaotic-flow model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
