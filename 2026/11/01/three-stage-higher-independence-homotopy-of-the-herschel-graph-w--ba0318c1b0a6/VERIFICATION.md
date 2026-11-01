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

Run `python3 verify_herschel_higher_independence.py`. It uses only the Python standard library and reads no external data. Its actual output is `verification_herschel_output.txt`, terminating in `HERSCHEL_HIGHER_INDEPENDENCE_1_2_3_INTEGRAL_OK`.

The program checks all \(2^{11}\) subsets independently for each of the three cutoff values, both by induced-component exploration and by the absence of a connected induced \((r+1)\)-set. Both constructions agree on every face. The augmented face counts are 124, 346, and 658.

For cutoffs one, two, and three respectively, the program checks 349, 1,150, and 2,536 directed Hasse incidences and 61, 168, and 327 disjoint match pairs. All matched incidences are reversed and the resulting directed graphs are topologically sorted without cycles. Critical cells occur exclusively as two dimension-two cells; ten dimension-three cells; and three dimension-four plus one dimension-five cells.

Exact alternating-sign boundary matrices are reduced by all 556 elementary integral unit-pivot cancellations. Every pivot is exactly \(+1\) or \(-1\), and the final Morse differential is zero over the integers at all three cutoffs. In particular, the unique last five-cell's boundary is the zero integer column, not a modular numerical observation. Independent direct mod-two simplicial boundary ranks corroborate the resulting homology.

The proof of the homotopy type invokes discrete Morse reduction and, at cutoff three, the Hurewicz isomorphism for the four-skeleton. Computation alone does not establish broader-family theorems, and no stage beyond cutoff three is claimed. Independent external audit has not been performed.
