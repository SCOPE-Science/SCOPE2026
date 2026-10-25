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

A rotation with three 1 symbols is unbordered iff its first and last letters differ. For v=1 0^a 1 0^b 1 0^c, a direct border argument proves unbordered iff a<c, with the reversed companion lemma. Each inequality of cyclic consecutive zero gaps gives precisely one unbordered rotation, yielding U(w)=[a!=b]+[b!=c]+[c!=a] in {0,2,3}. Counting nonnegative gap triples summing n-3: one all-equal if 3|n and 3(floor((n-3)/2)+1-[3|n]) triples with exactly two equal. Marking one of three occurrences of 1 gives n/3 cyclic positions per gap triple, yielding C0=n[3|n]/3, C2=n(floor((n-3)/2)+1-[3|n]) and C3=binom(n,3)-C0-C2. Handles periodic all-equal and n=3. Independently enumerated direct proper-border tests on all 2380 three-one strings for n=3,...,16 and checked every formula; all-length proof is combinatorial, not finite enumeration.

## originality

PASS

Best-of-knowledge PASS for the complete fixed-weight-three histogram at every length, not for characterizing all binary words with two unbordered conjugates. Holub–Müller 2015 supplies a broader structural classification of words with exactly two conjugates; Clokie–Gabric–Shallit 2019 proves maximum/existence/expected-number statements without the fixed-three-one distribution in checked sections. Older fixed-weight border-correlation papers not fully accessible remain priority risks.

## value

PASS

The first binary sparse weight where a third unbordered rotation is possible admits a sharp, nontrivial trichotomy and explicit all-n counts. A natural restricted joint histogram can be useful for word-conjugacy enumeration even if the proof is elementary; it is not an arbitrary single-length slice or known table replay.

The dated certificate retains the supplied scientific assessment, sources and limitations.
