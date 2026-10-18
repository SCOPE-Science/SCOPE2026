---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Use B_n=P_{2n}/2 and C_n=Q_{2n}. The Pell square identities reduce sums of k consecutive squares to (B_k Q_{4n+2k+2}-k)/16 and (B_k Q_{4n+2k+2}+k)/2 respectively. Consecutive block differences and strong divisibility of Pell numbers give gcd of B-square differences B_k, and gcd of C-square differences 8B_k. For odd k, B_k odd and relevant residue modulo 4 makes C initial block sum odd, giving both gcds gcd(B_k,k). Independently regenerated sequences and verified direct 9-window GCDs for every odd k<=101. The proof uses infinite GCD of successive differences, not bounded windows.

## originality

PASS

The primary 2023 article posed both square-sum cases as Question 30 and reported the odd branch equality as computational evidence only. Earlier generalized Fibonacci square-sum formula treats recurrence x_n=x_{n-1}+x_{n-2}, not balancing recurrence 6x_{n-1}-x_{n-2}.

## value

PASS

Answers the entire odd branch of two explicit open problems for natural classical recurrence sequences, with a sharp exact sequence-index GCD formula rather than a finite sampling result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
