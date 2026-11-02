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

# Reproducible checks and proof boundaries

The standalone `CHECK.py` uses only Python 3 standard-library modules. Run `python3 CHECK.py` from the extracted package directory. The expected successful output is:

`VERIFY_OK n2=16 n3=46656 equal=39672 proper=6984 cross-regret-pairs=3504 regret-subset-egal=1200 n4-stable=3 padding=5,6`

For \(n=2,3\) it constructs all \((n!)^{2n}\) labeled strict profiles and all \(n!\) full matchings, tests stability by explicit blocking pairs, obtains exact integer products of \(n-r\) and worst ranks, builds both complete optimizer sets, and checks the asserted counts. The recorded \(3{,}504\) comparisons are all pairs of distinct-regret stable matchings within all three-pair profiles. No sampling, randomness, floating-point tolerance, solver bound or timeout serves as a proof of absence.

For the four-pair witness, the checker enumerates all \(24\) complete matchings, identifies exactly the three stable ones displayed in `RESULT.md`, and verifies their utility products and unique opposing optima. It also verifies the explicit padding at sizes five and six. The accompanying **analytical** forced-mutual-top-pair argument, not those two examples, proves persistence for every larger size. The proof and certificate require labeled strict complete lists, balanced bipartite markets, positive rank utilities \(n-r\), and the ordinary blocking-pair definition of stability. These checks are self-review; no independent scientific audit or formal proof-assistant certification has been performed.
