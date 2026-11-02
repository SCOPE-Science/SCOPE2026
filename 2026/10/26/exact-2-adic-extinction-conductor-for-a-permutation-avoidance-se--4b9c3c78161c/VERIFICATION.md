---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The preexisting Catalan coefficient formula a_n=sum_k(-1)^(n-k)2^k C_k binom(2k+1,n-k), with k>=max(0,ceil((n-1)/3)), and the exact Catalan valuation nu_2(C_k)=s_2(k+1)-1 imply every term vanishes when n>=3K_alpha+2. At n=3K_alpha+1, all k<K_alpha are forbidden by coefficient support and all k>K_alpha have valuation at least alpha by the maximality defining K_alpha; the lone surviving term -2^K C_K is nonzero. For the lower-bound equality set, reduce modulo 2^(L+1) and track minimal-k terms separately for n=3m,3m+1,3m+2; Catalan parity holds iff k=2^r-1. The alpha=1 and initial n=0,1 boundaries check. Independently compared 230 recurrence coefficients with the Catalan expansion, all sharp cutoffs alpha=1..64 and all lower-bound equality assertions on indices 0..229. Finite checking supplements the exact arithmetic proof.

## originality

PASS

Le (2005) already supplies the generating function, OEIS A109033 credits Paul Barry (2008) for the exact Catalan coefficient expansion, and the Kummer/Catalan valuation is classical. Rowland–Yassawi (2015), full Section 3.5 Example 3.24/Open Question 3.25 materially inspected, asks whether four residues ever occur; it does not provide this all-exponent cutoff. The novelty is therefore limited to the sharp uniform 2-adic least cutoff, boundary witness and complete equality pattern, not the underlying GF, coefficients or Catalan parity. Searches found no exact previously tabulated conductor, but historical coverage remains a risk.

## value

PASS

An exact eventual-zero conductor N_alpha is a natural arithmetic invariant of a nontrivial algebraic permutation-enumeration sequence. The maximal-index boundary proves minimality at every exponent rather than just eventual divisibility; the equality pattern and explicit forbidden residues address a published concrete 2-adic question. The proof is elementary but gives an all-parameter sharp classification, not a routine recomputation of initial OEIS terms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
