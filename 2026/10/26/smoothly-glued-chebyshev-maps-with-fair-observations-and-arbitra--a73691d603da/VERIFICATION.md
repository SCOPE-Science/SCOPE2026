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

# Reproduction and limits

Run `python verify.py` with a standard Python 3 interpreter. The checker constructs the exact rational monotone-branch intervals, checks their inverse-width normalization and sign frequencies for degree pairs `(2,2)`, `(2,6)`, `(6,10)`, `(2,10)`, and `(10,22)`. For all sign words through length six it sums inverse-branch cylinder widths exactly, recovering \(2^{-r}\) at length \(r\). It also checks the entropy-gap formula and the maximal-entropy sign bias.

The observed output is `VERIFY_OK: 5 polynomial-degree pairs; 630 exact sign-word probabilities; full-branch counts, conservation, Perron bias and gap checked`.

These are finite corroborations, not a substitute for the stated mathematical proof. The unrestricted conclusion relies on the full-branch decomposition and the generating Bernoulli itinerary argument. The unique absolutely continuous measure argument uses exactness of a generating iid full-branch coding; the unique maximal-entropy measure argument uses the unique uniform Bernoulli maximizing the full-shift entropy. Boundary endpoints form only a countable entropy-zero exceptional set. An independent audit is not performed.
