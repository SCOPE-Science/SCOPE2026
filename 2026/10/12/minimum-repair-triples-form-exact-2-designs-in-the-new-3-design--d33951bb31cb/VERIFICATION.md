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
`artifacts/verify.py` uses only the Python standard library.

It constructs the source's smallest instance
\[
p=3,\quad m=2,\quad s=1,\quad q=9,\quad \ell=1
\]
over \(\mathbb F_{81}\).

The field is realized as a quartic extension of \(\mathbb F_3\). An element of order \(10=q+1\) is found and used to reconstruct the four source generator rows.

The script checks rank \(4\), then exhausts all
\[
\binom{10}{4}=210
\]
four-coordinate subsets. Exactly \(30\) are dependent. Every three-coordinate subset lies in exactly one dependent four-subset, so these supports form a
\[
3\text{-}(10,4,1)
\]
design.

For each coordinate, the incident four-blocks are derived to triples. The verifier checks exactly \(12\) repair triples, helper degree \(4\), and pair codegree \(1\), hence a
\[
2\text{-}(9,3,1)
\]
design.

It separately verifies the general counting and availability formulas for the three source examples
\[
(q,\lambda)=(9,1),\ (25,3),\ (81,7),
\]
giving guaranteed disjoint-repair counts at least \(2\), \(3\), and \(10\).

Successful replay prints `VERIFY_OK`.
