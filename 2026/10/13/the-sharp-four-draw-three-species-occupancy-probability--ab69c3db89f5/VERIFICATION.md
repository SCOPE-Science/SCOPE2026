---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For a fixed repeated atom i, the probability for the two ordered singleton draws to avoid it and differ is (1−p_i)^2−sum_{j≠i}p_j^2, also with diffuse mass. The six choices of paired positions are disjoint on the event, giving q/6=s2−2s3+2s4−s2^2. Inserting a+b=s and ab=t cancels the t^2 terms and gives slope c=−2+6s−4s^2+4R2. At any finite-simplex maximizer of minimal support an unequal positive pair can be equalized to gain if c>0, merged to gain if c<0, or merged to reduce support if c=0. Thus a uniform maximizer exists; among all integer supports r, 6(r−1)(r−2)/r^3 is zero at 1,2, increases through the relevant integer cases 3,4,5 and decreases for r≥5 (turning point 3+√3, with 4 versus 5 checked exactly), attaining 72/125 only at 5. A nonuniform finite equality law would have a chain of flat unequal-pair merges to this uniform law, but the last merge has s=1/5 and R2=4/25, hence c=−8/25 and strictly improves the value, a contradiction. Approximating the remaining mass after any finite atomic prefix by N equal masses gives convergence of all power sums of orders 2–4 (first N→∞, then the prefix grows); this passes the bound to arbitrary directing laws, including diffuse mass. Standard-Borel de Finetti then transfers it to infinite exchangeability and the uniform five-point law attains it. No uniqueness beyond finite i.i.d. laws is needed. The bundled finite checker was inspected, not executed, and is not used to certify the universal step.

## originality

PASS

The strongest inspected convex-hull, exact-law and coincidence-count statements do not give the sharp coordinate bound with unrestricted directing laws or its finite-support equality classification. No equivalent result was found in the checked evidence; priority is not established exhaustively.

## value

PASS

The outcome with one repeated pair is the interior coordinate of the four-draw distinct-count law, a natural first case beyond the known complete three-draw description. Its exact ceiling is a new constraint on unrestricted directing laws, not a finite-support experiment or just a comparison within the uniform family. The flat-merge argument additionally forces a unique finite parent up to relabeling. No claim to resolve the full four-draw hull problem is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
