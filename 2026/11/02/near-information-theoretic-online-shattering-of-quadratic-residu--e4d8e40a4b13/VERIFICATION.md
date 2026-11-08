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

For any center version space A size m, quadratic character chi with chi(0)=0 satisfies exact sum_x(sum_{c in A} chi(x-c))^2=m(q-m), using sum_x chi((x-a)(x-b))=-1 for distinct a,b and q-1 diagonals. Thus some query x has |X_A(x)|<=sqrt m. Exact zero-difference convention gives 2N_A(x)=m+X_A(x)-1[x in A], so both branch populations exceed (m-sqrt m-1)/2. The T_d=8*2^d-7*2^(d/2) inequality (T_d-sqrt T_d-1)/2>=T_(d-1) for d>=1 follows from concavity and monotonicity; it recursively constructs a full depth-d adaptive tree for q>=T_d. Concept count gives Ldim<=floor(log2 q), and d=floor(log2 q)-3 gives lower bound. Independent exact character-moment checks across odd primes up to 31 and memoized exact Littlestone recursion for q=3,5,7,11,13,17,19,23,29,31 corroborate observed maximal small depths. Composite prime powers covered by the general character proof, not by these prime tests.

## originality

PASS

Targeted Resultary semantic searches and primary literature comparisons, with specific mathematical implication checks and residual priority risks, support qualified best-of-knowledge originality of the final scoped claim.

## value

PASS

A uniform additive-3 defect from the information-theoretic ceiling for the online Littlestone dimension of a natural finite-field translate class is a substantive improvement over a constant-fraction static VC-dimension lower bound, with a useful exact second-moment adaptive splitting lemma that holds for arbitrary version spaces.

The dated certificate retains the supplied scientific assessment, sources and limitations.
