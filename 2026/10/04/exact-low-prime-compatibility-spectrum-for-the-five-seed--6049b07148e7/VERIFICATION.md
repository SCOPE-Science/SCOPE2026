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

For \(m=5\), every signed residual has denominator dividing 60 and numerator \(A=12-60w_1-30w_2-20w_3-15w_4\). Independent exact enumeration of all 81 coefficient choices reproduced the repository's 32 absolute reduced numerators and their complete prime-divisor union, with maximum numerator 137. Thus every prime above 137 is automatically compatible and the ten compatible primes through 137 are exactly the displayed list. The propagation proof is a correct p-adic localization argument: after isolating indices divisible by \(p^k\), every remaining term has positive p-adic valuation after multiplication, forcing p to divide the reduced residual numerator, contradicting compatibility. The final doubling equivalence follows directly from the two translates defining \(E_N\).

## originality

PASS

The primary source defines \(\mathcal U\), compatibility, and the propagation lemma, but for the seed 5 it only uses the coarse sufficient condition \(p>g_5=137\). Its text explicitly exhibits one exceptional low prime for seed 4, not the complete low-prime spectrum for seed 5. The audited 81-case exact census therefore refines, rather than restates, the published mechanism. Resultary returned the assigned finding as the only direct exact hit.

## value

PASS

The seed \(m=5\) is not arbitrary: it is explicitly used in the current recursive lower-bound construction with the coarse threshold 137. Computing its exact compatibility spectrum identifies every low-prime exception and converts nine of them into infinite doubling rays. Even without changing the leading asymptotic constant, this is a natural exact local invariant of the published mechanism and can support sharper finite or hybrid constructions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
