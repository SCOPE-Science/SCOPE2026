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

Phi(n)=sum_{d|n}mu(d)*2^(n/d) counts nonempty subsets A of [n] with gcd(n,gcd(A))=1, equivalently primitive binary words of length n for n>=2. For odd n>=3, uniquely smallest exponent n/rad(n) occurs with coefficient +/-1 in Mobius sum, so nu_2(Phi(n))=n/rad(n), odd, excluding squares. For n=2m, excluded strings are bounded by 2^m + r*2^(2m/3), r number of odd distinct primes dividing m. For m>=3, r<=m/3<=2^(m/3)-1, giving 2^(2m)-Phi(2m)<2^(m+1)-1 and hence consecutive-square bounds (2^m-1)^2<Phi(2m)<(2^m)^2; m=1,2 treated directly. These two arguments cover all n>=2, exclude every even-exponent perfect power. Independent direct gcd-subset enumeration n=2..16 and Mobius exact tests n=2..300 confirmed both alternatives. Source RESULT.md blob 3b78bc8c0d11f5594a36614d358a48b0946644c3 and verify.py blob c883b60918ea8b7cb638381cef084d0ab2d696b3 inspected.

## originality

PASS

Tang 2010 Remark 6 proves nonsquare/noncube for Phi(p) and Phi(pq), not all indices. Pongsriiam 2013 Question 3.4 explicitly asks if Phi(n) or D(n) can be perfect powers, contrasting Ayad-Kihel square exclusion for the different f(n). The displayed valuation+consecutive-square arguments extend square exclusion uniformly. OEIS A038199/A027375 list the sequence or primitive-word interpretation but do not by themselves resolve perfect powers. No stronger direct published theorem was identified in the inspected material.

## value

PASS

This closes the even-perfect-power branch of a published question for a natural arithmetic/combinatorial counting function; the two uniform alternatives are structural valuation and Diophantine gap theorems, not a finite-table observation. Odd powers (e.g. cubes), and D(n), remain open under this claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
