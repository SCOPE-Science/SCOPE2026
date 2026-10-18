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

# Reproducibility and scope

Run `python3 check_three_gap_maw.py` using a standard Python 3 installation. The program constructs the cyclic factor language through the primitive period for all \(1\le a<b<c\le24\); for each tested triple it compares the exhaustive set of minimal absent factors with the explicitly predicted complete set and count. It also applies a second direct cyclic-index construction to five test instances and confirms rotation invariance on three example cycles.

A minimal absent factor of a circular word can be tested at length at most the primitive period for this family, as supplied by the general circular/doubled-word theory in Fici–Restivo–Rizzo. The proof in RESULT.md separately rules out *every longer possible minimal absent factor* using interior phase uniqueness and therefore does not rely on any finite length bound.

The finite enumeration cannot prove universal correctness or absolute historical originality. No independent scientific review or external certification has been performed.
