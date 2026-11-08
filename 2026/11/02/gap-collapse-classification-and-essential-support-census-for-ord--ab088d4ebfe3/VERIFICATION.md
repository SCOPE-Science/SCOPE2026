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

The stabilizer of a finite ordered set S in Aut(Q,<) independently acts transitively on each of its k+1 dense open gaps. Invariance and equivalence transitivity force each gap to be entirely discrete singleton classes or one collapsed block; a discrete gap cannot merge externally. Selecting j collapsed gaps and a set partition of the k+j named units yields F_k=sum_j binom(k+1,j)B_(k+j), including F_0=2. The standard least finite-support theorem for the ordered-atom symmetry justifies inclusion-exclusion for exact essential supports H_k=sum_t (-1)^(k-t)binom(k,t)F_t. Log-convexity and the Bell-ratio asymptotic give 1-H_k/F_k <= k B_(k-1)/B_(k+1)=O((log k)^2/k). Independent Bell convolutions and finite proxy orbit checks reproduced first counts; a finite proxy does not prove the Q homogeneous-action argument.

## originality

PASS

The F_k numerical sequence already occurs as OEIS A208782, and existence/uniqueness of least supports for order atoms is established prior theory. The candidate original claim is the normal-form bijection to supported equivalence relations plus the essential-support H_k census and probability-one essentiality. No searched source implied this combination or gave those semantic counts under the same ordered atom action.

## value

PASS

An explicit complete invariant and exact essential parameter-support enumeration for a central oligomorphic symmetry is a natural classification useful for nominal set semantics and finite-support combinatorics, not a naked recomputation of an OEIS sequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
