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

PASS: For the explicitly defined Stern recurrence and Q_k=B_(53*2^k-3), the decomposition Q_k=(1+2 sum_{j=1}^{k-2}t^j)(1+4t+5t^2+3t^3)+(1+t)(t^2+2t^3+2t^4) is verified against recurrence. For all even k>=14, exact differentiation at t=-13/20 gives [80(82203k+108923)(13/20)^(k-2)-1026127]/17424000; the geometric factor is strictly decreasing on even k>=14 and is already negative at k=14. For even k=2,4,6,8,10,12, exact rational Sturm derivative sequences have no real roots and derivative at zero positive, so all are strictly increasing on R. Independently rebuilt polynomial recurrence and exact Sturm checks for each of six finite positive cases, confirmed exact negative witness k=14,16,18,20,22; infinite k>=14 proven by displayed monotone bound. Slice n=3 only, not eventual behavior in n.

## originality

PASS

PASS best of knowledge: Ulas’s Conjecture 4.2(1) (2019) proposes cutoffs c_(2i)=3 for a finite sample and eventual monotonicity separately; the submitted sharp fixed n=3 classification shows that sample cutoff false for every even k>=14 and gives a uniform negative-derivative witness, without refuting eventual n-behavior. Standard Stern identities and zero theorems precede the work but do not state this threshold. Later equivalent proofs remain a search risk.

## value

PASS

PASS: Resolves exactly which even-index parameter values satisfy monotonicity at the first conjecturally claimed bound n=3 and supplies an infinite family of counterexamples to the reported sharp cutoff, correcting mathematical expectations without overstating the separate eventual-monotonicity conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
