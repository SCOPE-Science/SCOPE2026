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

Run `python3 verify.py` beside `certificate.json`.

The verifier reconstructs the local two-symbol and three-symbol support tables used in the proof. It then fixes the first arch and exhausts every second permutation for each alphabet size \(2\le\sigma\le8\), comparing direct length-\(3\) subsequence enumeration with the exact formula
\[
3\binom{\sigma}{2}+A(Q)+4\binom{\sigma}{3}+E(Q).
\]
For every tested size the reverse permutation is the unique minimizer.

A separate labeled census checks every ordered pair of permutation arches for \(\sigma=4\) and \(\sigma=5\), finding exactly \(\sigma!\) extremizers, all of the form \(P P^R\).

The finite computations supplement the symbolic proof; they are not used to infer the theorem for untested alphabet sizes.

Independent audit has not been performed.
