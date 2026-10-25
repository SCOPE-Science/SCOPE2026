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

## Reproduction

Run `python check.py` in a directory containing the attached file. No third-party Python libraries or files are required. Expected terminal line: `RANK_ONE_RB_OK`.

## Actual checks and boundaries

Over \(M_2(\mathbb F_2)\) and \(M_2(\mathbb F_3)\), all decomposable presentations of rank-one linear operators were enumerated, tested using all pairs of standard matrix units, and deduplicated. Counts: \(15\) and \(56\). Over \(M_3(\mathbb F_2)\), all nonzero decomposable presentations were screened by the necessary condition that the image generator has square proportional to itself; the Rota–Baxter equation was then tested on each surviving presentation. The \(651\) valid presentations split into \(315\) with square-zero image and \(336\) with idempotent image. The reduction of arbitrary-field assertions is purely algebraic and appears in `RESULT.md`; it is not computer-certified.

The checker operates over prime fields \(\mathbb F_2\) and \(\mathbb F_3\). Extension-field claims and arbitrarily large dimensions rely on the written proof. Publication-priority searches are not a certification of uniqueness.
