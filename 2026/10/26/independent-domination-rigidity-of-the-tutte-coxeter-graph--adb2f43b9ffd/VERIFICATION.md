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
# Exact reproducibility

The two Python programs are standalone, use only the standard library, and include all input graph constructions. Execute `python3 verify_duad_syntheme.py` and `python3 verify_symplectic.py` from the directory containing these files. The accompanying text files record their expected terminal outputs.

The first verifier enumerates exactly \(2^{15}=32768\) edge masks and tests the necessary-and-sufficient completion equation. It checks all \(90\) minimum sets and every possible one-vertex exchange, their \(45\) paired four-cycle witnesses, and all \(720\) natural label permutations. Its terminal marker is `VERIFY_OK`.

The second verifier enumerates \(15\) points and \(15\) totally isotropic lines in four-dimensional binary symplectic space, checks all \(45\) incidences under its explicit vertex bijection against the duad–syntheme graph, generates independent sets recursively, tests maximality by closed-neighborhood domination, and exhaustively checks the one-token exchanges. Its independent cardinality distribution for all maximal independent sets is recorded in `symplectic_output.txt`. It confirms the optimum layer and \(45\) token-slide edges.

**Limitations.** This is exact exhaustive finite verification, not a computer-assisted proof for an infinite family. The graph-presentation isomorphism is checked explicitly. No external human validation is represented by this package.
