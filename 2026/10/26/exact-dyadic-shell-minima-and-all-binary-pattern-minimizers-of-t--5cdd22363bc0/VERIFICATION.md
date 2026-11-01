---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For unpadded binary-digit cumulative deficit a(n), Baruchel's exact Takagi identity and the Takagi quarter-map identities convert each shell minimum into a finite dyadic-grid maximum. The global Takagi bound 2/3 and the grid witness τ(3/8)=5/8 rule out outer quarters for depths >=3. Prefixing 01 and 10 bijects all maximizing words with those two levels below; H_1=1,H_2=2,H_l=2^(l−1)+H_(l−2)=floor(2^(l+1)/3). The first-half transfer j=n−2^k+1 has value 2^k−1−H_(k−1), while the second half is strictly worse. The parity-dependent maximizing word grammar follows inductively, and k=1 is checked directly. Independent exact digit sum enumeration verified full minimizing sets for shells k=1..14, including k=5 indices 36,37,38,40,41,42. Finite checks do not replace the induction.

## originality

PASS

Baruchel studies the exact same sequence and gives its Takagi representation. His §6.6 explicitly gives only a shell-minimum bound and says attainment was not proved. Krüppel establishes the continuous Takagi global maximum set (base-four digits 1 or 2) and local extremal structure, distinct from exact finite-grid maximizers, while Monroe gives dyadic rational Takagi identities. The complete finite-grid maximizer grammar and the resulting all-shell minimum and every minimizing index constitute the assessed increment, though broader literature may derive them implicitly. Resultary semantic search returned unrelated binary extremal records.

## value

PASS

The cumulative deficit A268289 and dyadic shells are canonical arithmetic objects. The exact all-shell minimizers answer a gap explicitly identified in the motivating paper and give a nontrivial self-similar classification and exact counts, beyond merely detecting a small minimum value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
