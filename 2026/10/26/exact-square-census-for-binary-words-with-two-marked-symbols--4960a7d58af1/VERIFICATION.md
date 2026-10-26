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
# Reproduction and limitations

Run `python3 scripts/check_square_census.py` using Python 3 and no dependencies. It directly enumerates all literal square factors for the 2600 words with \(0\le m\le23\), checks the separate combinatorial coefficients and maximum-attaining counts over 302621 triples with \(0\le m\le120\), and checks the two sharpness constructions for 500 more values of \(m\). All three checks succeeded before delivery.

The proof of (1) is the literal square-root classification. The rational generating function follows by disjoint square types and an invertible four-parameter encoding. The extrema follow from the constraint \(M+2t\le m\), the lower-bound split at \(M=m/2\), and an exact slack classification. Only these symbolic steps establish claims for all \(m\); neither the checker nor a finite sampling log is an infinite proof.

The earlier global inequality is attributed to the cited literature. Historical priority of the new exact refinements is assessed from the accessible sources only and is not independently certified.
