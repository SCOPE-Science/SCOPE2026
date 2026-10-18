---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Fix positive integer n=ord_e(q), with coprime q,e>=2, and let m(q,e) be the least number of q-power summands with repetitions allowed producing zero modulo e. If m(q,e)=3 and 3 does not divide n, normalize exponents to 0<=a<=b<n and form F(X)=1+X^a+X^b. F and X^n-1 have no common complex root: three unit complex numbers summing to zero must be a regular 3-gon, whose ratios force a cubic root of unity and hence 3|n. Thus their nonzero integral resultant is divisible by e; each factor F(zeta) for zeta^n=1 has modulus<=3, so e<=3^n. If 3|n, F_n(X)=1+X^{n/3}+X^{2n/3} vanishes at primitive n-th roots, so Phi_n(X) divides F_n(X). For all sufficiently large integer bases q, nonzero resultants of Phi_n(X) with X^d-1 (d proper divisor of n) ensure ord_{Phi_n(q)}(q)=n. If n odd choose e=Phi_n(q), and no 2-sum is possible in an odd-order group. If n even, hence 6|n, choose q>=2 congruent 1 mod3 and e=3Phi_n(q); since Phi_n(1)=1 for such n, gcd(q,e)=1, order remains n, 1+q^{n/3}+q^{2n/3} vanishes mod e, and no 2-sum exists because every q-power is 1 mod3. Infinitely many growing moduli result. Independent exact resultant tests for 3-free orders and construction samples n=3,6,9,12,15 matched. The n=1 and n=2 finite-side boundaries are included in the general argument.

## originality

PASS

The published 2021 Breuer–Héthelyi–Horváth–Külshammer Lemma 2.11 gives m(q,p^k)=3 when the odd multiplicative order has a factor three, so the odd-order infinite construction is substantially covered in spirit and follows from that lemma together with primes congruent 1 mod n. This is credited; it is NOT the claimed new core. That same lemma gives m=2 for even order on odd prime-power moduli, so it cannot imply the new even-order three-sum construction with composite modulus 3Phi_n(q). Jacob–Külshammer Proposition 11 establishes finiteness only with the extra hypothesis e|Phi_n(q) and a smaller length threshold, whereas this theorem fixes ord_e(q)=n over arbitrary composite moduli and supplies the explicit bound 3^n for every n not divisible by three. Lam–Leung classifies weight sets of complex root-of-unity sums in characteristic zero, not these modular residue zero sums or their bounded moduli. Comparisons were by hypotheses and implications, including the genuine earlier odd-order coverage. No all-order exact finite/infinite statement for arbitrary modulus was identified in full relevant primary sources or mathematical-record search.

## value

PASS

The invariant m(q,e) is central in a published modular power-sum problem, and multiplicative order is its natural arithmetic organizing parameter. The theorem identifies an exact all-order finite/infinite boundary at divisibility by three, provides an explicit bound for every order outside the infinite regime, and constructs infinitely many genuinely composite moduli for the even-order regime where prime-power results cannot have minimal length three. These are structural classifications, not a single example; their value persists even though earlier papers cover the odd-order existence subcase.

The dated certificate retains the supplied scientific assessment, sources and limitations.
