---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

In the explicitly restricted bank, each online operation is determined by a subset S of r distinct fixed eigenphase kickbacks, with total residue the subset sum modulo N=2^n−1. At most h active units yields <=sum_{j<=h} C(r,j) distinct subsets and hence residues, proving the exact covering obstruction. For h=r, 2^r>=2^n−1 forces r>=n for n>=2. For r=n, omitting activation levels n−1 and n leaves at most 2^n−n−1<2^n−1 residues, so h>=n−1. Source labels a*2^i modulo N (gcd(a,N)=1) attain both because every residue has n-bit representative m<=2^n−2 and therefore at most n−1 ones. Independently enumerated all target residues and optimal activation counts for n=2..9, finding universal coverage with maximum n−1; finite enumeration is not the all-n proof.

## originality

PASS

The source construction already supplies n power-of-two catalysts and suggests needing n copies; later work uses one catalyst with target-dependent controlled powers and explicitly escapes the fixed on/off bank model. The new statement is only an optimality certificate for the preexisting selectable-bank architecture, not a general catalyst lower bound. Generic pigeonhole information bounds are known as a method; the specialization and sharp simultaneous register/activation optimum were not located as a theorem in the inspected primary sources.

## value

PASS

A narrowly defined but physically motivated architecture leaves an explicit resource-optimality question open in its originating construction. Matching lower bounds show exactly when the source’s n^2 catalyst qubits and n−1 worst-case uses are unavoidable under independent on/off activation, and precisely where the later lower-resource architecture changes the assumptions. Though the counting is elementary, it resolves an actual proposed resource-efficiency claim rather than an arbitrary parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
