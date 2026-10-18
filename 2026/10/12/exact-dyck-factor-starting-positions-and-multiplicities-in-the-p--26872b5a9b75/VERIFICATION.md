---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

PASS. For regular paperfolding p_n determined by odd(n) mod4, signed prefix height H(N) equals weight of the reflected binary Gray code N xor floor(N/2). Its reflected-half recursion proves all crossing Dyck intervals are [2^r-1,2^K-1] with lengths 2^K-2^r, 1<=r<K. For each such L, reflection of the two canonical intervals forces the only start residues a=2^r-1 or 2^K modulo 2^(K+1); odd-part invariance on the interior proves both residues always give Dyck factors. The two canonical words coincide only at L=2,4, and two starts per modulus give density 2^(-K) and exact dyadic prefix occurrence count 2^(M-K) for M>=K+1. Independently enumerated all Dyck intervals at finite levels 2..10 and verified exact residues and multiplicities; induction establishes all levels.

## originality

PASS

PASS with defined scope. Mol–Rampersad–Shallit Section 6/Conjecture 6.5 concerns possible Dyck-factor lengths of the regular paperfolding word, not the complete arithmetic set of every starting position, distinct-factor multiplicities or occurrence densities. Known length support is weaker existential information and is credited; even an established length theorem would not supply the positional iff. Reflected Gray-code recursion is standard, but the two-residue occurrence classification and one-versus-two word count require the dedicated interval analysis. Fresh Resultary search found unrelated paperfolding factor properties but no exact covering positional theorem. Older unindexed Gray-weight work remains possible.

## value

PASS

PASS. This gives a complete natural occurrence census for Dyck factors of a standard automatic sequence, not merely a language of permitted lengths: each candidate factor can be recognized by one modular test, with exact distinct-factor types, occurrence density and exact dyadic-prefix counts for unbounded lengths. The problem is explicitly motivated by a published Dyck-factor question, and the Gray-code structure explains all parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
