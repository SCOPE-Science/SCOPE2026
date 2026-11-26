---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The generator in RESULT.md has the stated directional transitions, including absorption from a singleton at the remaining extinction rate. For fixed S,c set X=(z+S+c)^2, Y=z+S+2c, D_p=zX+pY. I independently checked the determinant, resolvent numerators and the survival transform (X-p)/D_p. More directly than differentiating, for 0<p<q<=S^2/4 the difference of survival transforms is (q-p)(X/D_p)((z+Y)/D_q). The first factor after q-p inverts to survival plus p times the inverse of 1/D_p, nonnegative by the U,V cofactor ac/D_p if c>0 and by convolution of three exponentials if c=0. It is strictly positive by the no-event path. The second factor inverts to the sum of the two singleton occupation probabilities from B divided by their respective first-jump rates. Exactly one extinction and no further jump gives strict positivity at every positive time. Uniqueness of the Laplace transform and the strictly positive convolution therefore give the order, even at the balanced comparison endpoint. Since P=(S^2-(a-b)^2)/4, this proves strict imbalance ordering and the unique balanced minimum. The z=0 mean and the example also check. Only the stated positive-rate domain is required; in its closure a zero-rate patch persists forever, so the prose about positivity should not be read as excluding a strict zero-versus-positive comparison.

## originality

PASS

Pass is limited to the strict usual stochastic order at every positive deadline for extinction-rate redistribution with common positive recolonization; the zero-recolonization case is classical. The strongest same-day comparison gives a more general absorption transform and a different allocation optimum. Its symmetric specialization covers the transform and yields a Laplace-transform order, not the pointwise survival sign proved by inversion with positive kernels. No earlier or same-day full coverage of that sign was established. This is a best-of-knowledge conclusion, not a priority determination.

## value

PASS

In a canonical minimal rescue model, the ranking at one management deadline need not in general predict another from the mean alone. The theorem rules out crossings for this exact fixed total hazard comparison at any finite common rescue rate and identifies the unique worst allocation. This extends the independent-parallel case in a structurally useful way without suggesting that the fixed-budget mechanism holds in field systems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
