---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For n=prod p^{a_p}, D(n)/n=sum a_p/p, and integrality D(n)/n=k forces p|a_p for each p by reducing n|D(n) modulo p^{a_p}; conversely if a_p=p c_p then sum c_p=k. Thus all solutions come from a composition of k into r<=k positive integers. Leading r=k solutions have c_p=1 and log n=sum_{j=1}^k p_j log p_j with distinct primes. By PNT, B(L)=#{p:p log p<=L}~L/(log L)^2, regularly varying index 1. Product weak convergence on simplex sum t_i<=1 yields k-fold ordered volume 1/k!, and division by k! distinct permutations gives B(L)^k/(k!)^2. Repeated primes and r<k solutions O(B(L)^{k-1}), so A_k(x)~(log x)^k/[(k!)^2(loglog x)^{2k}] for fixed positive integer k. Independent direct exact sieve enumerated n<=1,400,000 for k=1..4 and agreed structural equivalence; this does not prove the analytic limit.

## originality

PASS

Ufnarovski--Åhlander 2003 Theorem 1 defines D(n)/n and Theorem 6 classifies k=1 as n=p^p; Barbeau's 1961 criterion concerns integrality of D(n)/n. Full Ufnarovski paper (24pp) materially read at Theorems 1,4-6,9 and equation sections: no fixed-k counting asymptotic in those statements. Resultary fixed-k D(n)=kn searches retrieved this target, other arithmetic-derivative dynamics and unrelated prime-weight results, but not a prior general counting law. Asymptotic claim is a new PNT/regular-variation consequence, not the credited structural lemma. Best-of-knowledge PASS with obscure aliases possible.

## value

PASS

The arithmetic derivative's integer logarithmic-derivative fibers are a natural number-theoretic classification. Exact asymptotics with leading constants for every fixed k and concentration on maximal distinct prime support add meaningful distribution information to the previously known k=1 solution and exponent divisibility criterion; prime-weight simplex counting is a substantive analytic step.

The dated certificate retains the supplied scientific assessment, sources and limitations.
