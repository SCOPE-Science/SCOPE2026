---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

At p=65537 (prime by exact trial division), every a=46256,...,46268 has a^16384 in {256,65281} and its square equals -1 mod p; thus a^32768=-1 and a has exact order 2^16=p-1, since the ambient prime-field multiplicative group is of order 2^16. Odd-degree M_m=(p^m-1)/(p-1) is odd; therefore the same a has order p-1<q-1, so nonprimitive, and a^((q-1)/2)=(-1)^M_m=-1, so nonsquare. For odd prime degrees ell, the odd repunit M_ell has only prime divisors r with ord_r(p)=ell and thus r≡1 mod ell; factoring q-1=2^16 M_ell gives theta=1/2∏(1-1/r). Since their count s<ell logp/log(ell+1), 0<1/2-theta<ell logp/[2(ell+1)log(ell+1)]→0. For ANY odd finite field theta≤1/2 and equality eliminates all NSNP elements; hence sharp unattained supremum 1/2 for each 3≤k≤13. Boundaries: m is any odd integer≥3 for the block; ell ranges only odd rational primes for convergence; characteristic p>13 ensures distinct additive constants; m=1 not included.

## originality

PASS

Best-of-knowledge: prior work gives general sufficient NSNP criteria and low-density thresholds, and OEIS already tabulates the exact 65537 primitive roots. The audited mathematical contribution is the paired high-density infinite-field construction plus sharp unattained density supremum for 3≤k≤13; that implication was not identified in the fully inspected primary statements or indexed published results. The existence of the known finite table is credited and no uniqueness/absolute priority is asserted.

## value

PASS

The invariant theta_q and NSNP run-existence threshold are natural in finite-field multiplicative combinatorics. The theorem supplies a sharp but unattained HIGH-density extremum for 11 block lengths 3 through 13, showing a vanishing ambient fraction of NSNPs can retain a fixed run of 13; it clarifies the conceptual distinction between universal low-density guarantees and extremal high-density counterexamples. The finite witness is already available in an established primitive-root table, so the contribution is the uniform odd-extension persistence and sharp infinite-family density boundary, not a new primality table, novel algorithm or generic textbook lemma. The independently checked maximum length 13 in this PARTICULAR prime field motivates the natural cutoff; no maximality across all fields is asserted. This is an exact self-contained extremal result, not a claim to solve general longest-run growth.

The dated certificate retains the supplied scientific assessment, sources and limitations.
