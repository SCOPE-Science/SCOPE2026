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

For each fixed integer k>=2, Euclid parameterizes primitive right triangles uniquely by coprime m>n>=1 opposite parity with P=2m(m+n). If P=t^k and m odd, v2(P)=1, impossible; hence m even and s=m+n odd, gcd(2m,s)=1. Unique factorization gives 2m=(2u)^k and s=v^k, v odd, gcd(u,v)=1. Thus m=2^(k-1)u^k and 2^(1-1/k)u<v<2u, 2uv<=X^(1/k). The bounded wedge uv<=Y=X^(1/k)/2 has area Y log2/(2k), and requiring odd v halves lattice density with O_k(sqrt(Y)) boundary discrepancy. Odd Möbius inversion for gcd(u,v)=1 multiplies by prod_{p>2}(1-p^-2)=8/pi^2, and its sqrt(Y) tail plus O(sqrt(Y) logY) sum give N_k(X)=log2/(k*pi^2)*X^(1/k)+O_k(X^(1/(2k))log(2X)). The positive leading constant proves infinitude for each fixed k. Independent exact enumerations of all Euclid m<500 and the power-parameter wedge agreed for k=2,3,4,5, with respective solution counts 28,2,0,0; these bounded counts only check the bijection, not asymptotic.

## originality

PASS

Best-of-knowledge first all-prime-support count with explicit main term and error for primitive right triangles whose perimeter is a perfect fixed kth power. The classical Lehmer and Lambek–Moser primitive triangle perimeter asymptotic counts all perimeters <=X, not perimeters restricted to kth powers, and cannot be specialized by replacing X by X^(1/k). Yiu §6.2 gives exactly the k=2 power parametrization and a table but no all-support asymptotic; published fixed-prime-support square-perimeter studies count different fixed-support logarithmic families. The new sieve is elementary but supplies the previously unestablished thin-subsequence density for all fixed k. Residual possibility of an earlier unindexed analytic number theory derivation.

## value

PASS

Perfect powers form a sparse, natural number-theoretic perimeter condition. An exact power-law exponent, leading constant log2/(k*pi^2), explicit error, and infinitude for every fixed k have independent Diophantine counting value; the unbounded prime-support family is not determined by existing total perimeter counts or square-perimeter examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
