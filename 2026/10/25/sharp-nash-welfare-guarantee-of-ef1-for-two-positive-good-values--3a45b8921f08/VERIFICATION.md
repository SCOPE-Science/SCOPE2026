---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification record

## Analytic checks
1. Positive goods and \(m\ge n\) force every EF1 bundle to be nonempty.
2. EF1 implies integer bundle loads within two units of each other.
3. Each auxiliary replacement of extreme values \((L,L+2)\) by \((L+1,L+1)\) raises product by at most \(4/3\), and at most \(\lfloor n/2\rfloor\) replacements are required.
4. A balanced integral load vector maximizes all nonnegative integral products at the same sum, so the unrestricted optimum is bounded by the same envelope.
5. The explicit \(a\)- and \(2a\)-valued construction is EF1 and has precisely the claimed ratio to a feasible optimum.

## Executed finite check
With Python 3, `python3 CHECK.py` enumerated every allocation up to indistinguishability of identically valued goods, for \(n=2,3,4,5\), all \(m\) from \(n\) through 10, and every available split of the inventory into value-one and value-two goods. Using exact integer products and rational comparisons, 6,497 EF1 allocation count vectors passed the inequality; at least one equality case was observed at every tested \(n\). This check is finite and is not a substitute for the proof.

## Limits
The code assumes integer values after a common positive scaling. The mathematical theorem handles arbitrary positive real \(a\) by the initial scaling argument. The reported review is not independent validation.
