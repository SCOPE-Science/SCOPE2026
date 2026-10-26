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

# Exact verification and reproduction

Run `python3 verify_marker_balance.py` with a standard Python 3 interpreter and no dependencies. The program independently executes an explicit eight-orbit integer-polynomial multiplication and a direct exhaustive construction of all tables satisfying the three defining inequalities. It tests each of the sixteen inputs for every table, computes each nucleotide's output frequency, and checks the transpose condition. Expected output includes `Admissible tables: 2304`, `GC input-pair profile: [(7, 512), (8, 1280), (9, 512)]`, `Fully symbol-balanced tables: 80`, `Transpose-symmetric admissible tables: 576`, `Fully balanced and transpose-symmetric tables: 16`, and `VERIFY_OK`.

The finite exhaustive proof requires only eight independent two-element complement orbits. The program's dynamic coefficient calculation starts from eight explicit lists of admissible ordered outputs; its second implementation derives allowed outputs from the inequalities and enumerates the Cartesian product. Thus the two routes have separate constraint encodings. Arithmetic is exact. One balanced transpose-symmetric witness is displayed in `RESULT.md` and verified again by the program.

Scientific limits: the result concerns lookup-table output statistics, and its stated probabilistic interpretation assumes uniformly distributed flank pairs. It does not verify a full synchronization decoder, an end-to-end DNA storage system, or a GC-balance property for arbitrary codeword ensembles. Independent external audit has not been performed.
