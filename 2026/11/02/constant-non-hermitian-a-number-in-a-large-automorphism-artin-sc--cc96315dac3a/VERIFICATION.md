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

For algebraically closed k of odd prime characteristic p≥5, y^p-y=x^(p+1)+a x² has one pole of order p+1 and genus p(p-1)/2; the holomorphic differential basis x^i y^j dx (i+j≤p−2) follows from valuations at infinity. The explicit Cartier expansion has source weight i+2j and output weight t=i+2j−(p−1). For a=0 every possible term includes a positive power of a^(1/p), giving zero rank. For a≠0, invertible row/column rescaling transforms each t-block into evaluation of the polynomial basis P_k(u)=∏_(h=k+1)^K(u+h) at distinct u∈{1,...,N} in F_p; its rank is min(K+1,N), K=floor(t/2), N=(p−1)/2−ceil(t/2). Summing t=0...p−3 gives rank (p²−1)/8 and hence a-number (p−1)(3p−1)/8. A separate direct modular expansion/elimination (not executing the package script) for p=5,7,11 and a=0,1,2 recovered ranks 0/3, 0/6, 0/15. The all-prime claim rests on the evaluation argument.

## originality

PASS

The exact curve family is already in Arakelian–Kian 2026 for large automorphisms; Zhou 2019 proves p=3 nonzero case, intentionally excluded. Farnell–Pries 2013 constant-rank theorem applies only p≡1 modulo pole-order L, impossible for L=p+1, while its own text discusses monomial a-number formulas. No located result computes the entire nonzero-parameter p≥5 block rank. Nevertheless original Arakelian–Kian manuscript was not fully accessible (arXiv/OA unavailable and Oxford VPN disconnected), leaving a serious possibility of a stronger formula in its full text or appendices.

## value

PASS

The a-number is a canonical finer Jacobian invariant after genus and p-rank. In a natural large-automorphism Artin–Schreier deformation family, a complete all-primes coefficient-independent formula for all a≠0 and the exact jump at the Hermitian boundary gives a meaningful infinite classification. It is neither just a normalization check nor a finite experiment; the p=3 previously known case is excluded.

The dated certificate retains the supplied scientific assessment, sources and limitations.
