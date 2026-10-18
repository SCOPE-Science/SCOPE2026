---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Reconstructed identities B_n=P_{2n}/2, C_n=Q_{2n} and X_n=8Y_n+k. Exact Pell telescoping gives X_{n+1}-X_n=2P_{2k}P_{2k+4n+4}, Y difference=(P_{2k}/4)P_{2k+4n+4}. For even k, strong divisibility gives gcd_{n>=0}P_{2k+4n+4}=P_4=12, hence increment gcds 48B_k and 6B_k. First-window identities reduce the infinite gcd to gcd(X_0,48B_k) and gcd(Y_0,6B_k). At 3, nu_3(B_k)=1+nu_3(k); at 2, u=B_k/k≡3 (mod 16), C_k≡1 (mod 16), leading to nu2(X0)=nu2(k), nu2(Y0)=nu2(k)-1; odd p valuations from first-window congruences. Therefore gcd X=gcd(k,B_k), gcd Y=gcd(k,B_k)/2 for all even k>0. Independently computed windows for k=2..22 and many starting n, matching both formulas; infinite proof is symbolic.

## originality

PASS

PASS best-of-knowledge: Mbirika–Schrader–Spilker 2023 Section 6.1, Question 30 explicitly asks for formulas for square-window GCDs, and notes factor two experimentally for even k; the assigned two exact formulas prove that relation and fully evaluate both values. Older sum-of-squares and Pell divisibility identities alone do not present these outer translated-window gcds. No identical completed formula was found among actual searches; potential unindexed later solutions remain possible.

## value

PASS

PASS: This solves the natural even-window subproblem from a published explicit open question about balancing and Lucas-balancing sums-of-squares GCDs. The exact unrestricted arithmetic invariant gcd(k,B_k), with proved 2-adic and 3-adic cases, is independently useful for recurrence divisibility studies; it is neither a parameter renaming nor a finite-table computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
