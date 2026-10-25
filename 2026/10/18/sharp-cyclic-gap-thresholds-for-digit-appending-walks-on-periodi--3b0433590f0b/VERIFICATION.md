---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Given a_n=b^n+u_(n mod h), b≥2, finite U=max|u_r|, select M with b^M>4(U+1). For a digit-append step from m≥M with index jump k and append length t, the inequality 0≤a_(m+k)−b^t a_m<b^t forces k=t: for k>t the normalized digit difference exceeds 1, and for k<t it is negative, uniformly even if t grows. For k=t an edge is legal exactly when 0≤u_(r+t)−b^t u_r<b^t. On any finite residue-state directed cycle positive correction values would strictly increase and values≤−2 strictly decrease, while zero cannot lead to negative and −1 cannot lead to nonnegative. Hence cycles lie wholly in correction 0 or −1 states; all positive increments connecting two states of the same one of these levels are allowed. Such a subset supports a bounded-increment residue cycle iff the maximum circular gap is ≤N (lift a hypothetical cycle past its largest missing interval). Thus N*=min(g(S0),g(S−1)); both sets empty excludes infinite walks even for unbounded digit lengths. When N<N*, the eventual graph is acyclic with at most h−1 edges after index M, and at most M earlier edges, so all walks have ≤M+h−1 steps. Independent finite graph tests evaluated 22,500 base/period/cap parameter triples under exact digit inequalities; every cycle existence matched N*. These do not prove the unrestricted theorem.

## originality

PASS

Digit-appending walk papers primarily treat Fibonacci and Lucas dominant roots that are nonintegral and unrelated to the appended base. The present resonant dominant root exactly b with arbitrary periodic integer corrections admits infinite walks and a zero/minus-one cyclic-gap classification; no matching prior implication appeared in searched primary literature.

## value

PASS

Classifies all infinite walks and sharp bounded-digit thresholds for a natural full class of integer-base exponential recurrences with periodic corrections, including cycles invisible to the usual Fibonacci termination arguments. The simple circular-gap invariant precisely answers the natural existence decision for each recurrence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
