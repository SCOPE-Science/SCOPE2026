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
# Reproducible checks and their scope

With Python 3 and no extra dependencies, run `python3 verify_wdle_mode.py` in the same directory. The script separately evaluates the paper's original parent mass and long wrap sums; compares them with the derived closed-form residue mass; checks normalization and global maximizing residues for a finite parameter grid; and verifies the stated transition decimal approximations using bisection. Its final output is `CHECK_OK: direct wrap, normalization, modes, roots, sector ceiling`.

**Analytic checks beyond finite replay.** The accompanying proof derives the adjacent comparison \(r<H_m(\varphi)\), proves \(H_m'(\varphi)<0\) for every \(\varphi>0\), computes both limiting endpoints and applies the intermediate value theorem. Those steps, not numerical root-finding, establish the all-dimension existence and uniqueness of transitions and the half-circle mode bound.

**Limits.** This verification uses the published fixed-origin WDLE parent distribution, integer \(m\ge2\), and real \(\varphi>0\). It does not examine statistical fit quality or the mode of a location-augmented family. Decimal root values are illustrative. Primary-publisher PDF access was restricted, and scientific priority still requires independent scholarly review; independent audit has not been performed.
