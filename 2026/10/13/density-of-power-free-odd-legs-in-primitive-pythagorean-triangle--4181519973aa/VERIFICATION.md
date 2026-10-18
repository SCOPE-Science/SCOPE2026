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

Euclidean primitive parametrization bijects m>n coprime opposite parity to odd coprime 0<u=m-n<v=m+n, with hypotenuse (u²+v²)/2 and odd leg uv. Because gcd(u,v)=1, k-power-freeness of uv is equivalent to that of u and v. The sector 0<u<v, u²+v²<=2X has area pi X/4; both odd imposes factor 1/4; at p>2 admissibility is lambda_(p,k)=1-p^-2-2*p^-k*(1-p^-1)=(1-p^-2)*(1-2/(p^(k-1)*(p+1))). For fixed z the CRT sieve gives density, while uniform large-prime tails O_k(X/z+sqrt(X)log X) justify z->infty after X->infty, proving T_k(X)=X/(2pi)*prod_{p>2}(1-2/(p^(k-1)(p+1)))+o_k(X). Independent Euclid-vs-odd-factor enumeration agrees for all 9 (X,k) pairs X=50,500,10000 and k=2,3,4; product through 200000 gives P2 approximately .70752146, matching reported normalization. Infinite asymptotic follows only from the analytic sieve, not experiments.

## originality

PASS

Classical Euclid parametrization and squarefree constraints in Zelator (2008), alternative parametrization Overmars-Ntogramatzidis (2015), fixed-leg divisor counts Ochieng (2019) and Burson (2020) are acknowledged. Their inspected statements concern existence, parametrization or fixed odd legs, not density by increasing hypotenuse with an explicit prime product for every k>=2. This analytic density could conceivably be an immediate corollary of a broader sieve counting theorem for primitive lattice points in sectors, but a generic sieve supplies methodology rather than this exact specialized motivated invariant as a published conclusion. Best-of-knowledge originality with substantial unindexed-folklore risk.

## value

PASS

Power-free arithmetic properties of the unique odd leg are natural: a primitive triangle always has its even leg divisible by 4, so its squarefreeness is impossible. The theorem identifies the exact positive proportion (including squarefree P2~.70752) among all primitive triangles ordered by hypotenuse and extends coherently to each fixed k, a meaningful quantitative invariant not a contrived finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
