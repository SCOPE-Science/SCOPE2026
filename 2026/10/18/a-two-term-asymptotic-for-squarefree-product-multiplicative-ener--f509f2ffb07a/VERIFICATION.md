---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

With U=gcd(A,C), divide it out to obtain coprime X,Y. Then X B=Y D gives B=VY and D=VX with a unique monic V. Squarefreeness of UVXY is exactly individual squarefreeness and pairwise coprimality of the four components; equal input degrees force component degrees (k,k,n-k,n-k). Unique factorization therefore gives one empty and four single-slot choices at each prime, and factoring off the four geometric series gives the stated H_q. A coefficient indexed by j contributes q^(2n)h_q(j) for each integer k from max(j1,j2) through n-max(j3,j4), including the degree-zero endpoints. On any common radius R<sqrt(q) the Euler product converges normally because all linear local terms cancel and the total bound on local deviations is a constant times sum_d (R^2/q)^d. At R=q^(1/4), Cauchy gives exponential coefficient decay q^(-|j|/4). Replacing the positive part by its linear argument only changes indices with |j|>n; using at most binom(m+3,3) indices of weight m and an O(m+n+1) multiplier proves the stated O_q((n+1)^4 q^(-n/4)) error. The two untruncated sums are H_q(1,1,1,1) and the displayed b_q. The leading product is positive since every factor is positive and the sum of squared prime reciprocals converges. Independent replay `python3 /workspace/audit_recompute.py 2` compared the exact positive-part coefficient identity to direct squarefree-product multiplicities in 19 cases: the 15 stated test cases plus four over F4. The frozen AUDIT.json count of 17 is a bookkeeping discrepancy, not a theorem failure; RESULT.md, VERIFICATION.md and the actual loop ranges specify 15. Finite checks do not prove the asymptotic.

## originality

PASS

The assessed claim is the fixed-field two-term law, including the absolutely convergent secondary coefficient and exponential normalized remainder, for collisions with squarefree common product. The closest sources count unrestricted collisions, coprime tuples, or collisions with individually squarefree inputs. The last has substantially overlapping coefficient machinery, but a distinct prime-local rule and no corresponding secondary evaluation for this count. No priority is inferred from a same-day listing.

## value

PASS

Squarefree common products are a natural stratum of multiplicative energy and have a different local prime-allocation law. At fixed field the exact secondary coefficient separates true boundary contributions of the degree balance from a generic bounded error. The exact coefficient identity and exponentially small remainder are useful quantitative statements beyond a finite census or the known unrestricted formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
