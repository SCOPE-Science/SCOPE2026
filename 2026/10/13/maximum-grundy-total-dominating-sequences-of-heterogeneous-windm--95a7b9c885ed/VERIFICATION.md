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

# Verification

The analytic proof establishes the theorem for every \(r\ge2\) and every profile \((m_1,\ldots,m_r)\) with \(m_i\ge2\). The included `verify.py` is a finite replay check rather than evidence for extrapolation.

For each tested graph, the verifier forms every vertex subset. It precomputes the union of open neighborhoods of each subset and uses subset dynamic programming to count all legal orderings of that exact subset. It then selects the subsets whose open neighborhoods cover the whole graph, determines the maximum sequence length, and checks:

- the maximum length is \(2r\);
- a maximum set without the center has exactly two vertices in every blade;
- a maximum set with the center has exactly one one-vertex blade and two vertices in every other blade;
- every no-center maximum set supports exactly \((2r)!\) legal orderings;
- every center-containing maximum set supports exactly \((2r-1)!\) legal orderings, necessarily with the center last;
- the closed formulas for the number of maximum sets and maximum sequences agree with exhaustive counts.

The tested family contains all profiles with \(2\le r\le4\) and every \(m_i\in\{2,3\}\), plus five additional heterogeneous profiles containing a blade of size \(4\). The largest checked graph has order \(13\).

Replay output:

`VERIFY_OK profiles=33 subset_masks=49151 append_checks=278544 classification_checks=5633 maximum_set_checks=2130 sequence_checksum=17321556 max_order=13`

Unproved by computation: no finite replay establishes the theorem for larger profiles. Those cases are covered only by the combinatorial proof in `RESULT.md`.
