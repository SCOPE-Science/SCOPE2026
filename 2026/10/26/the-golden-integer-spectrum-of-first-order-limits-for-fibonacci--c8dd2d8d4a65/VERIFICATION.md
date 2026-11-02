---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Uniform length-n 11-avoiding words number F_{n+2}. A fixed legal prefix u of length k has exact count F_{n-k+2} if u ends 0 and F_{n-k+1} if ends 1; limiting cylinder mass c(u)=phi^-k or phi^-(k+1). Perron decomposition of primitive Fibonacci transfer matrix gives exponentially asymptotically independent fixed prefixes and suffixes. Every fixed legal centered block appears >=t times with probability 1-O(exp(-c n)) by uniform positive probability of prescribing 0 v 0 at spaced positions. Effective bounded-degree Hanf locality for directed successor paths with unary P makes any fixed FO sentence, with exponentially small exception, a Boolean function of bounded prefixes/suffixes; hence its limit is a finite sum of products c(u)c(v) in Z[phi], convergence exponential. Conversely for alpha=m+d phi in (0,1), Fibonacci integer coefficient expansion of alpha phi^(k+1)=a_k phi+b_k with b_k=a_{k-1} satisfies 0<=a_k<=F_{k+1}, 0<=b_k<=F_k for large k. Choosing exactly those counts of length-k admissible prefixes ending respectively 0 and 1 gives a FO-definable cylinder event with limit alpha. Trivial endpoints 0,1; irrationality gives only rational 0 and 1; dense Z[phi]∩[0,1]. Independently checked finite cylinder counts, endpoint pair transfer counts, and exact conjugate integer realizations.

## originality

PASS

Prior bounded-degree Hanf locality, Fibonacci transfer matrix cylinder measures, and Perron/Parry probabilities are explicitly credited. Marström–Räty 2026 studies logical limit laws of permutation classes/regular languages, with possible extensions; the available description does not give the exact attainable golden-integer arithmetic spectrum for uniformly sampled no-11 words with successor only. Natural clopen measure-value theory for golden mean shift could cover the reverse inclusion; no decisive covering statement was identified in actual searches. Best-of-knowledge qualified novelty concerns the exact FO probability set, not machinery.

## value

PASS

The exact dense but rationally trivial FO limit spectrum is a natural and surprising model-theoretic invariant of a canonical regular language, and the theorem effectively produces a sentence for every algebraic integer in Z[phi]∩[0,1]. It connects finite-model locality and Fibonacci Perron arithmetic in a way genuinely distinct from a generic convergence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
