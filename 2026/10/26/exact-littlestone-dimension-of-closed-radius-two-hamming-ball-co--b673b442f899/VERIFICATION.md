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

# Verification procedure and limits

The proof is in `RESULT.md`. The adjacent JSON file `witnesses.json` contains explicit complete binary decision trees for ambient dimensions \(3,4,5,6\), with target depths \(1,3,4,5\). A tree node records an integer query (the corresponding bit vector), and each leaf records an integer witness centre. The zero/one edge label is the truth value of \(\operatorname{dist}_H(\mathrm{query},\mathrm{centre})\le2\).

Run `python3 verify.py` using standard Python 3 from the same directory as `witnesses.json`; no packages or external files are needed. The script checks every complete root-to-leaf path, including all branch responses and distinct leaf witnesses. It also independently computes the exact recursive Littlestone depths for dimensions one through six by exploring all possible query cuts and checks the intersection-branch structural cases for dimensions five through eight. `verification_output.txt` records observed successful output.

The full ambient-dimension result is not inferred from this computation. Its unbounded upper bound is given by Lemmas 1–4 and the root-positive-child argument in `RESULT.md`. The infinite lower-bound family follows from coordinate padding of the explicit dimension-six tree. These steps are mathematical arguments, not an external infinite formal certificate.

Publication priority has residual uncertainty; the calculation has not received an independent scientific audit.
