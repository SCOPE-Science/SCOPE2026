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

For n>=1, n*2^n+1 is odd. If y^k=n2^n+1 with k>=3 odd, then y is odd and (y^k-1)/(y-1)=sum_{j=0}^{k-1}y^j is odd, so v_2(y-1)=n+v_2(n). Consequently y>2^n and y^k>2^{3n}>n2^n+1, contradiction. If k is even, y^k=z^2, z odd. For n=2^t m with m odd and n>=2, the consecutive coprime integers A=(z-1)/2,B=(z+1)/2 satisfy AB=m2^{n+t-2}. One has v2=n+t-2, the other is odd dividing m; since |A-B|=1 this forces 2^{n+t-2}<=m+1, impossible for n>=4 (check n=4 separately and induct through n>=5 using 2^{n-2}>n+1). Direct n=1,2,3 values 3,9,25 give exactly (2,3,2),(3,5,2). Higher even exponents would make a square already excluded except these whose exponents have gcd 2. An independent finite scan n<=200 for squares and odd exponents k=3,5,7,9 yielded only n=2,3 square indices and no odd powers; it is corroboration, not the general proof.

## originality

PASS

The 2023 BMO1 Question 4 fully proves the square branch, thus all even exponent cases of the new statement are covered as prior work and cannot be described as independent novelty. The new odd-exponent exclusion is the elementary but not identical all-odd-power component that makes the natural complete perfect-power classification. The full Grau–Luca Lehmer-property paper and Marques Fibonacci-intersection paper address different arithmetic predicates, not arbitrary kth powers; OEIS A002064 is a sequence table and does not assert an all-exponent theorem. Bounded phrase and Resultary searches found no prior general Cullen perfect-power statement, but absence of a hit cannot establish absolute novelty.

## value

PASS

The statement classifies a natural intrinsic property—exact perfect powers in the entire classical Cullen sequence—rather than an arbitrary cutoff. Its value lies in closing the mathematically natural complement to the known square classification; the odd-exponent lemma is short and elementary, so this is a modest self-contained Diophantine fact, not a new technique, a generalization to arbitrary bases, or a large theoretical advance. Natural completeness and a clear unproved odd-exponent branch are sufficient here; the already published square branch is explicitly not claimed as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
