---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For the specified regular paperfolding convention, a_(2m)=a_m,a_(4m+1)=+1,a_(4m+3)=-1 for a_n=1-2p_n. Prefix balance S(N)=∑_{j≤N}a_j satisfies S(2m)=S(m)+1_(m odd), S(2m+1)=S(m)+1_(m even), exactly the recurrences and base case of binary-run count R(N). Therefore [x+1,y] is Dyck iff R(y)=R(x) and R(t)≥R(x) for x≤t≤y. All repunit endpoints x=2^i-1,y=2^k-1 with 1≤i<k have common height one and supply canonical lengths 2^k-2^i. Conversely an interval crossing a binary-length boundary forces baseline one and repunit endpoints; at equal length, the two integers at the first changed 0/1 bit bound run counts, giving only two suffix patterns with length 2^d-2^a, with 1≤a<d. The i=0 printed conjecture branch would give odd lengths and is correctly excluded. Independently enumerated all endpoint intervals through 4096 and checked S(N)=R(N) through 100000; no finite test is substituted for infinite classification.

## originality

PASS

Mol--Rampersad--Shallit, Dyck Words, Pattern Avoidance, and Automatic Sequences, Section 6 Conjecture 6.5, explicitly pose the power-of-two difference characterization for paperfolding Dyck factor lengths; its printed i=0 option is incompatible with Dyck parity. The present **explicitly corrected** range 1≤i<k supplies a complete structural proof, not an attempted acceptance of that literally false printed endpoint. Searches for an existing proof in the same-paper later versions, binary-run wording and indexed results found no covering theorem. The original primary full-paper conjecture was read; historical unindexed-priority risk remains.

## value

PASS

Directly resolves a published natural combinatorics-on-words conjectural length classification, with a surprisingly simple invariant (binary runs) and canonical witnesses for every allowed length. This covers infinitely many factor lengths with a structural iff theorem, rather than a bounded Walnut experiment or arbitrary finite census. It also precisely corrects the unavoidable even-length boundary in the conjecture's statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
