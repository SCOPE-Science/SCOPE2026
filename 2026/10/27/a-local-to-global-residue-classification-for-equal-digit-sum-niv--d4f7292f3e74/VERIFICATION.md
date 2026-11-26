---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Independently checked the all-parameter construction and its boundary cases. In a padded k-digit block, the base-b digit sum of d is ≤d with equality exactly for d<b, so equality across blocks requires every B-digit below b. Reduction modulo m_0 then sees just v low blocks. For the converse fix an allowed prefix c and its digit sum d, and write c-d=(B-1)T. By CRT there are unbounded s≡r mod m_1 prime to B (use s≡1 mod rad(b)); set N=lcm(s,m_1) and q=N/gcd(N,B-1). For R=(-T) mod q, the repunits U_j=(B^j-1)/(B-1), starting at U_1=1, satisfy U_{j+1}=BU_j+1. In descending greedy division each remainder entering its U_j step is less than U_{j+1}, so its quotient is at most B. The number of scales is at most log_B(1+(B-1)R) for R>0; an empty sum suffices at R=0. As N≤sm_1, this correction uses O(log(s+1)) unit slots, fewer than s-d for large allowed s. Place those slots at pairwise distinct exponents ≥v in the prescribed congruence classes modulo ord_N(B), and put the remaining slots at distinct exponents congruent to zero. This changes neither the prefix nor the overall digit-sum count s. Modulo N the resulting number is s+(B-1)(T+R)≡s; this simultaneously gives divisibility by s and the residue r modulo m_1. The prefix gives r modulo m_0, and unbounded distinct sums yield infinitely many distinct positive integers. v=0 gives c=d=T=0; the trivial modulus/order convention and R=0 include the boundary cases. At m=B^v the prefix map is injective and has b^v values. This analytic replay verifies the universal theorem; the supplied modular checker was inspected, not executed.

## originality

PASS

Credit Kominers for the entire coprime-modulus subcase, including unbounded equal sums. The supported distinction is the exact arbitrary-modulus residue criterion and noncoprime sufficiency preserving a prescribed permitted prefix, not general existence of power-related simultaneous Niven numbers or single-base repunit identities.

## value

PASS

Removing coprimality from the existing power-related progression problem introduces a real obstruction, not just a change of parameters: some classes cannot contain any equal-sum numbers, while every permitted class has simultaneous Niven witnesses with unbounded sums. The exact low-prefix decision and preservation of that prefix while enforcing divisibility solve this natural local-to-global problem for arbitrary mixed or base-supported moduli.

The dated certificate retains the supplied scientific assessment, sources and limitations.
