---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Computational verification

Run `python3 verify.py` from a directory containing the standalone artifact. The script uses only the Python standard library and builds finite operation tables from explicit definitions rather than importing precomputed counting sequences. The completed replay reported:

```
VERIFY_OK 304 parameter identities, exact operation tables and finite axioms
```

It constructs all \(d\)-element generalized Sugihara chain parameters via positive compositions and skeletal radii, then constructs the reflected involutive De Morgan multiplication and the rigorous extensions. It checks the algebra cardinality and exact distribution of the number of non-idempotent elements against the formula for every size through \(21\). For examples of size through \(16\), it checks the generated multiplication/involution signatures for noncollisions, identity, commutativity, order monotonicity, square-increase, and all triples in the residuation law. Through size \(12\), associativity and generation by the negative cone are checked directly. Independently, positive compositions are enumerated for generalized Sugihara chains through size \(20\) and compared with Fibonacci counts. The code's assertion tally is an aggregate of outer test stages, not a count of all inner quantified-operation checks. Printed intermediate lines show the exact checked finite-size distributions.

Separately, an independent two-state polynomial recurrence \(P_d(v)=P_{d-1}(v)+vP_{d-2}(v)\), with \(P_1=P_2=1\), was compared against \(\sum_kinom{d-k-1}{k}v^k\) for all \(1\le d\le35\); all comparisons passed. This independent recurrence check was run outside the included standalone script and is not included in its printed assertion count.

**Scope limits.** Testing small finite models cannot establish that every finite chain has the normal form or that no distinct abstract parameters become isomorphic in larger orders. Those facts are obtained from intrinsic recovery of the 2022/2024 structural representation, proved in `RESULT.md`. No independent review, external proof assistant, or formal certification is claimed.
