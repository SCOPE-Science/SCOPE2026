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

# Reproducibility and limits

Run `python verify.py` with standard Python 3. No external packages or downloaded materials are required. The checker builds all perfect matchings of complete graphs on six and eight vertices from first principles and represents edge sets by integer masks. It obtains closure by intersection of all perfect-matchings-as-models extending the input, independently of the closed-form classification. It constructs each of the two proposed classes of rule premises separately and applies their conclusions using the original input (one synchronous pass).

For \(n=3\), it exhausts \(2^{15}=32768\) possible edge subsets. For \(n=4\), it tests every predicted closed set and an additional 15000 reproducible samples. Every interval in the finite inclusion lattice is independently evaluated using the Möbius recurrence: 138 intervals when \(n=3\), and 2502 when \(n=4\). The observed closed-set counts are 32 and 345, and the indispensable-premise counts are 105 and 588, respectively. These verify the small cases of the rank, implication, and Hermite-formula claims.

The checker does not mechanically prove the infinite parameter range, homotopy equivalence, uniqueness in the external literature, or any independent certification. The all-parameter correctness argument is the mathematical proof in RESULT.md; the topological step invokes the stated poset fiber lemma on explicitly exhibited contractible lower fibers.
