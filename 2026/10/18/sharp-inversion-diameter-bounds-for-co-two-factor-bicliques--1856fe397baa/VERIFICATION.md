---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

An inversion of a vertex subset toggles bipartite edge bits by one outer product over F2, so t inversions iff completed prescribed edge data factor through F2^t. Every deleted 2-factor gives a loopless 2-regular multigraph T of two missing row indices per right column (including 2-cycles with parallel edges); proper 3-colouring assigns distinct nonzero F2^2 vectors to every omitted pair. Kernel basis Q of 2-by-n parity-check matrix restricts invertibly to the n-2 surviving rows of every column, permitting n-2 binary factors for any orientation difference. In Hamiltonian case the n-2 prescribed bits at offsets +2 form a triangular all-diagonal-one rank lower bound for any completion.

## originality

PASS

Best-of-knowledge original contribution is the specific additional statement, not reused techniques or credited general facts; four comparative checks and actual source material below. Neither earlier statement logically forces that every 2-factor complement admits the n-2 completion, or sharpness of Hamilton lower minor.

## value

PASS

A sharp degree-matching inversion bound for an infinite regular bipartite graph family, constructive across disconnected deletion factors, is mathematically motivated by inversion diameter versus maximum degree. Hamiltonian lower-bound certificate makes a complete sharp result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
