---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The actual RESULT.md defines the nonabsorbing longest-prefix automaton A for an arbitrary word w, including borders and zero-probability irrelevant letters. Its upper-Hessenberg zero pattern and fixed one-step superdiagonal make the (0,m-1) inverse entry a triangular cofactor z^(m-1) times the product of the first m-1 letter probabilities. Thus E[z^(T-m)]=p_w/det(I-zA), including m=1. Every block of m letters hits the target with conditional probability at least p_w, so ||A^m||∞<=1-p_w and rho(A)<1. Normalization at z=1 gives det(I-A)=p_w, and -logdet(I-zA)=sum_k tr(A^k) z^k/k converges absolutely; all diagonal entries of A^k are nonnegative. This proves exact nonnegative finite Lévy intensity, not merely an approximate or finite-prefix law. When p_w=1 the process is deterministic zero. Kumulants via exponential moment analyticity are sums k^r nu_k. Inspected word_wait_checker.py constructs KMP automata, rational Newton identities and independent short-word enumeration; listed 498 word tests and 365 exhaustive short checks are supplemental, not a universal proof.

## originality

PASS

Compared the all-word exact infinite-divisibility statement, not the availability of a rational PGF alone. Sankaran–Midhu has full Markov embedding and hitting-law formulae, but not trace-positive logarithm or exact compound-Poisson all-word assertion in the inspected full sections. Johnson–Fu uses compound-Poisson approximation for counts of patterns, not the exact law for T_w-m. Oh–Park–Kim concerns success runs, a subfamily, and recurrence rather than infinite divisibility. Semantic research search gives nearby automata/renewal findings but no covering same stopping time. A historical unindexed all-word infinite-divisibility formulation remains a real risk, not ruled out by search failure.

## value

PASS

The result is a structural exact law for the natural first-occurrence waiting time of every single word, including overlapping patterns and nonuniform sources; explicitly nonnegative matrix-trace jump measures and the complete cumulant family go materially beyond solving a rational recurrence. It explains a broad probabilistic property that may fail for multiple target words or dependent letters; the natural object and invariant are motivated before calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
