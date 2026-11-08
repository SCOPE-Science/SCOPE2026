---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The resident boundary x=0 gives logistic F(n)=mu n(1-n) and a period-two pair n±=(mu+1 ±sqrt((mu-3)(mu+1)))/(2mu). The two-step resource multiplier 4+2mu-mu² has modulus<1 exactly for 3<mu<1+sqrt(6). At x=0 both type-I and type-II strategy maps have derivative S(n)=(1-n)alpha+n sigma and zero derivative in n, so the monodromy is lower triangular; transverse multiplier equals S(n-)S(n+)=[alpha²+(mu+1)(mu-2)alpha sigma+(mu+1)sigma²]/mu². It increases strictly in alpha, crosses one uniquely at alpha*>1; hyperbolic attraction/saddle claims follow in the stated strict regions, not at equality. Algebra gives the exact mean-variance identity Lambda_C=S(nbar)^2 -(alpha-sigma)^2(mu-3)(mu+1)/(4mu²), hence alpha_mean<alpha*. Under sigma>2/(mu+1) the strict physical interval exists. Independently evaluated exact rational witness mu=16/5,d=1/10,alpha=9/5,sigma=3/5 yielding 1593/1600 transverse, 4/25 longitudinal, 81/80 mean-game factor, and checked positive invariance bound (mu+d)²<4mu. These computations corroborate, not replace, Floquet proof.

## originality

PASS

Qualified best-of-knowledge originality: compared exact claim and possible implications with relevant primary literature and two actual semantic published-record searches; a failed search is not proof of novelty. The source paper proposes a mean-game substitution. The finite-amplitude variance identity shows the squared mean exceeds the exact geometric product; if the original paper already derived the full product, priority would be covered, but accessible metadata alone does not settle that. Current O is conditional best knowledge with substantive named risk.

## value

PASS

An exact biologically admissible counterexample demonstrates why averaging the environment before stability testing can give the wrong evolutionary invasion verdict. The exact threshold and common applicability to two update rules are useful for parameter analysis, despite reliance on standard Floquet-product and logistic-cycle identities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
