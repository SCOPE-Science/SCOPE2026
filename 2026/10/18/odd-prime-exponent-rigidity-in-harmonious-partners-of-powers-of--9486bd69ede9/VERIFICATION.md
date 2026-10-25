---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Write Y=2^k, X=2^r, S=Σ_{j=0}^s p^j. Harmonious means Y/(2Y−1)+Xp^s/((2X−1)S)=1. If k=1 then first term is 2/3 but second is strictly greater than (p−1)/(2p)≥1/3, impossible. For k≥2 clearing denominators gives Xp^s(2Y−1)=(Y−1)(2X−1)S; gcd(Y−1,X(2Y−1))=1 forces Y−1=p^j (1≤j≤s). If j is even then p^j=1 mod8 whereas Y−1=3 or 7 mod8; if j≥3 odd then (p^j+1)/(p+1) is an odd integer >1 dividing Y=2^k, impossible. Thus p=Y−1. Cancel p and observe p∤S, so p^{s−1}|2X−1. Set t=(2X−1)/p^{s−1}≥1; elementary exact algebra gives 2p+1=t(p^{s−1}+2Σ_{j=0}^{s−2}p^j). When s=2 the parenthesis is p+2, strictly between half and all of 2p+1, requiring 1<t<2; when s≥3 it is >2p+1. Hence s=1 and t=2p+1, yielding X=p+1=Y, r=k; direct substitution proves all Mersenne-prime cases. Independent exact cross-multiplication over k,r∈1..9, odd primes p≤67, s∈1..5 checked 7,290 cases and exactly three predictions, while algebra proves all exponents. The theorem does NOT cover multiple distinct odd primes such as partner 120 of 2.

## originality

PASS

The exact s=1 classification is ALREADY a published mathematical finding and is not credited as new. The candidate new claim is exponent-uniform IMPOSSIBILITY for every s≥2 with one odd-prime support, completing the entire natural 2-prime-support slice. Kozek et al (2015) give the definition and sparsity/discordance rather than this fixed support classification; Bishop et al 2021 give general feebly amicable abundancy conditions but not this exclusion in inspected mathematical results. Priority remains best-of-knowledge in the face of alternate aliases and potential unindexed converse theorems.

## value

PASS

The power-of-two harmonious-partner problem is a classical divisor-sum Diophantine identity. Restricting the partner to two prime supports is the minimal nontrivial arithmetic layer; the previously known result settled only exponent one on its odd prime. Here a clean rigid divisibility/factorization argument proves no repeated odd-prime factor can occur for ANY positive exponent, completing the entire exponent direction and making the positive Mersenne family exhaustive. This closes an intrinsic natural boundary with an all-parameter proof, not a numerical increment or trivially substituted identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
