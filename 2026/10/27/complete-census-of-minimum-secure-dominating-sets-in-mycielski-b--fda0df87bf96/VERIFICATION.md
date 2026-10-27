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

# Verification record

Two executable Python 3 sources are included. Run them from the directory containing these files.

`python3 verify_profiles.py` exhausts the complete integer-profile domain for each guard count zero through five. It checks the candidate/dominating/secure count triples \((1,0,0)\), \((5,0,0)\), \((14,0,0)\), \((30,6,0)\), \((55,19,0)\), and \((91,41,6)\), tests equality of all six secure profiles, and cross-checks polynomial summands. Successful output begins `PROFILE_VERIFY_OK`.

`python3 verify_graph.py` constructs original-and-shadow Mycielski adjacency lists independently and for five host pairs exhaustively tests every chosen vertex set of size three, four and five by direct guard substitution and domination checking. It confirms no secure sets below size five, and minimum-set counts \(2225\), \(3435\), \(5301\), \(4970\), \(7665\). Successful output ends `DIRECT_VERIFY_OK`.

These scripts were executed. The graph-level checks are finite corroboration; the theorem's infinite scope rests on the exact twin-class reduction and fully exhaustive finite profile enumeration. The main prose provides both equivalences and a cap-uniformity argument. Neither script constitutes an independent audit, and no independent review evidence is claimed.
