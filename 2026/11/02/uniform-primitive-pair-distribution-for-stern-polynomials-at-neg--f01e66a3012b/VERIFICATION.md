---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The two binary transitions on (B_n(−2),B_{n+1}(−2)) have determinant −2, a unit at every odd m, so primitivity is invariant. Multiplying the displayed matrices verifies P^{-1}(AB^{-1})²P=E_{12}(−4) and P^{-1}A(AB^{-1})²A^{-1}P=E_{21}(−2). These yield all shears; local-ring elimination and CRT generate SL₂, including at repeated prime powers. A primitive pair extends to a determinant-one basis, so transitivity is on exactly the primitive pairs. The positive-word orbit equals the group orbit by finiteness. The two transitions are permutations and the accessible (0,1) has an A-self-loop; the walk thus mixes to uniform. The prefix-cylinder argument bounds discrepancies of cylinders of free length ≥L by their total size times the uniform mixing error and treats shorter cylinders by a total size <2^L, proving natural density at arbitrary endpoints. CRT counts the marginal fibers as stated. A fresh direct recurrence and BFS over m=3,9,25,27,45,75,125 through a prefix of 65,536 checked the exact orbit sizes 8,72,600,648,1728,4800,15000 and all marginal fiber sizes. Prefix frequencies were finite corroboration, not an exact density test; replay: branches/9b74cb2e-5a23-415a-abcb-70fa0f5af4a2/independent_check.py.

## originality

PASS

Deshouillers–Schinzel already prove the density mechanism for invertible digit automata, and their Stern result at t=1 has exactly the same form. The supported distinct result is reachability of the full primitive orbit for the t=−2 generators at every odd modulus, via the opposite shears, and hence the law for that specialization. The inspected earlier primitive-orbit proof uses different generators and does not supply this input.

## value

PASS

The orbit calculation gives a complete exact modular law at a natural nonordinary specialization with invertible odd-modulus digits. It resolves all composite odd moduli, including repeated prime factors, and supplies exact scalar densities that are not all equal. The opposite-unit-shear argument explains why full primitive support holds uniformly rather than just displaying frequencies in small moduli.

The dated certificate retains the supplied scientific assessment, sources and limitations.
