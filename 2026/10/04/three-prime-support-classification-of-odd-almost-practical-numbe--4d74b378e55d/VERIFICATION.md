---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

PASS: Stewart's odd divisor-gap criterion and its prime-multiplication closure (precisely restated in Jokar Proposition 3.6 and Proposition 3.10) reduce three-support odd almost practical numbers to 3^a5^b7^c. If a=1, divisor jump 7 to 15 fails at partial sum 16; n=315=(2,1,1) fails last transition 315>307. Direct ordered-divisor gap checks establish bases 945=(3,1,1), 1575=(2,2,1), 2205=(2,1,2), and closure yields all a>=2 with a+b+c>=5. Independent reconstruction checked every 216 exponent triples 1<=a,b,c<=6 and three base sums, corroboration only.

## originality

PASS

PASS (qualified): Jokar's full primary arXiv text contains Stewart's criterion and closure, and explicitly states the a>=3 subfamily, but does not provide the sharp a=2 boundary or exclude every a=1 case. The original 1954 Stewart paper was unavailable in full, even after authorized Oxford retrieval returned vpn_disconnected, so the possibility of an equivalent earlier boundary corollary is a named residual risk, not an automatic failure. Complete exponent-stratum classification is best-of-knowledge new.

## value

PASS

PASS: The minimal possible odd three-prime-support family is an intrinsic classification problem; a>=2 and the unique missing 315 boundary are natural finite obstructions, and closure certifies an infinite collection without finite extrapolation. A full boundary rather than a reparameterization of the a>=3 sufficient family is mathematically reusable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
