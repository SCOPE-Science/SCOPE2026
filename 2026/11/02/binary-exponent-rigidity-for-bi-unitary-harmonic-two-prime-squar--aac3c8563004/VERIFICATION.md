---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For distinct primes p,q and integer t>=2, set e=2^t and b=e/2 even. Reconstructed sigma**(r^{2b})=(r^b-1)(r^{b+1}+1)/(r-1), tau**(r^{2b})=2b. Harmonic divisibility would force (p^2+1) B |2e p^2 q^e, B=(q^b-1)(q^{b+1}+1)/(q-1). Because b even, both (q^b-1)/(q-1) and q^{b+1}+1 vanish mod q+1, hence (q+1)^2|B. For q=2, (p^2+1)/2 has a forbidden odd divisor; for p=2, q=5 from p^2+1=5 but q+1 forces forbidden factor 3. For odd primes, odd divisor of p^2+1 implies q|p^2+1 and q=1 mod4; m=(q+1)/2 odd has m^2|p^2 (by (q+1)^2 and coprime support), forcing m=p and q=2p-1. Mod q, 4(p^2+1)=(q+1)^2+4 gives q|5, hence p=3,q=5. Then 5^{b+1}+1 >=126 cannot divide the 2*3^2 factor (its 2-adic order=1), contradiction. Independent exact prime-pair finite calculations corroborate 2310 combinations; the unrestricted proof is the divisor argument.

## originality

PASS

No inspected current-priority source states or unambiguously implies the precise new theorem; methods and covered neighbors are credited explicitly, and residual inaccessibility/overlap risks remain. Best-of-knowledge originality, not world-priority certification.

## value

PASS

A structural all-primes/all-binary-exponent nonexistence theorem in the natural two-prime bi-unitary harmonic classification problem. The forced squared q+1 divisor and arithmetic prime-support rigidity solve an infinite family not implied by neighboring odd-even exponent exclusions; not a low-level finite instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
