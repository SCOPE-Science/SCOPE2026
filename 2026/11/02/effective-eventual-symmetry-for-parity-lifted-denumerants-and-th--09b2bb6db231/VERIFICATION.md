---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Parity bijection gives d_{2a,2b,c}(2t)=H(t)=d(2t+c), H for (a,b,c), all t≥0. Root-of-unity partial fractions for pairwise coprime three generators yield exact H(t+L)-H(t)=t+(L+a+b+c)/2 and Δ(t+L)=Δ(t)+1, L=abc. Hence after explicit U=L max(0,1-min_{r<L}Δ(r)), H is strictly increasing and bounded initial levels give an effective p threshold. The translated ideal and ell,g,n formulas follow by parity. For (a,b,c)=(3,4,7), an exact 84-residue negative-difference table (only indices 0,4,7,28), together with the shift identity and direct low-t counts, leaves only p=0,1,7 non-ray levels; p=0,7 symmetric but p=1 not. Independent rational/integer recurrence checked 84 rows, shift, and 181 thresholds; infinite tail follows from algebra.

## originality

PASS

Komatsu–Ying 2022 papers define p-symmetry and give low-p results for arithmetic triples; Komatsu 2024 Watanabe-type transfer requires c∈<a,b> and does not provide the all-high-p translated ideal or exact all-p (6,7,8) spectrum. The latter is also claimed in assigned record 5, but record 4 has strictly broader parameters including c outside <a,b>; thus 5 does not dominate 4. The broad all-p structural theorem survives the known-method overlap.

## value

PASS

The computable all-high-p threshold ideal and exact generalized Frobenius/genus for an infinite non-gluing family address a natural multiplicity problem. The full (6,7,8) exception classification, especially p=7 symmetric despite nonray, is a motivated sharp boundary, not a sample-only calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
