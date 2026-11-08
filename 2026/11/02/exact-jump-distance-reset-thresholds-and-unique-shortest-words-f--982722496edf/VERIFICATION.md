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

For n>=2 and 1<=d<n, b:x↦x+1 mod n and a:0↦d (other states fixed). A common reset image requires x+B+dK_x constant mod n; gcd(n,d)>1 preserves initial difference modulo gcd and forbids synchronization. When gcd=1, effective-a counts K_x occupy all n residues mod n, forcing a trajectory with >=n-1 jumps and >=(n-2)(n-d) intervening b letters, giving |w| >=1+(n-2)(n-d+1). T=ab^(n-d) fixes 0 and subtracts d from other states; T^(n-2)a attains the bound. Equality leaves no spare a/b and forces the literal word a(b^(n-d)a)^(n-2), including n=2. Fresh subset-automaton BFS independently compared all 45 cases n=2..10 and shortest multiplicities (and noncoprime failures). Finite checks corroborate only finite n, proof supplies general n.

## originality

PASS

GCD synchronization criterion and (n-1)^2 bound are earlier results, as is the d=1 classical Cerny extremal. The exact d-dependent reset threshold and literal uniqueness across all coprime d are not supplied by the inspected primary results; original assertion is thus the sharper family-specific classification only.

## value

PASS

Reset threshold and number of shortest reset words are natural algorithmic invariants of synchronizing automata. The theorem classifies an entire two-parameter explicit family, refines a uniform quadratic upper bound with a sharp jump-dependent value, and establishes optimal-word rigidity; this is more than a relabelled classical Cerny case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
