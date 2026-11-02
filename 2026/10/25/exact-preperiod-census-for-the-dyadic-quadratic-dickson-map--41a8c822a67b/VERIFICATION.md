---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Parity is preserved by x²−2. For odd x the first iterate y satisfies y≡−1 (mod 8), and v2(f(y)+1)=v2(y+1)+1, producing exact pointwise time 1+max(0,k−v2(x²−1)) except x fixed. For x≡2 mod4, v2(f(x)−2)=v2(x²−4), after which each iterate increases distance-to-2 valuation by two; for x≡0 mod4, after two iterations the valuation is 2+2v2(x). These yield the two even pointwise branches. Four odd roots of unity modulo 2^s yield O0=1,O1=3,O_t=2^t for 2≤t≤k−2. The even valuation-window A_k and x≡0 mod4 count B_k exhaust and partition all even residues. Boundary moduli k=1,2 and special k=3,4 are separated explicitly; the infinity convention is harmless under modulus clipping. Fresh direct functional-graph iteration on every residue mod 2^k for k=1..12 (8,190 residues) agreed with the pointwise and even histogram formulas. Universal proof uses valuation identities, not a finite census.

## originality

PASS

A fresh closest-prior comparison finds no accessible theorem or database record implying the final all-parameter conclusion. The exact overlap/special-case antecedents are credited and remaining literature-access or terminology risks are recorded; PASS is a best-of-knowledge judgment, not external historical certification. Exact preperiod census for the dyadic quadratic Dickson map: For every k≥1, f(x)=x²−2 mod 2^k has only the odd fixed point −1 and even fixed point 2 as recurrent states; exact pointwise first-arrival valuations and separate odd/even depth histograms are given for every k, and maximum transient depth is k−2 for k≥4.

## value

PASS

The pointwise least-arrival law and complete basin-depth distribution constitute an exact, naturally defined arithmetic-dynamical invariant for the smallest nonpermutation Dickson map on nonreduced dyadic rings. Its striking odd versus even growth rates and sharp maximal transient are not given by permutation-cycle results. It does not classify higher Dickson degrees or other prime powers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
