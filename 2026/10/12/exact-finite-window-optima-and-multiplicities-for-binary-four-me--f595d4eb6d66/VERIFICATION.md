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

Unrestricted binary words of length L correspond to walks of L−3 edges in the order-three de Bruijn digraph, removing precisely the edges for U. A directed cycle gives arbitrary avoiding lengths. An acyclic remainder has at most seven edges on any path, so the longest avoiding word has length at most ten, including length three when there are no remaining edges. Each rotation class gives periodic avoiders unless hit, so size at least six is necessary at every L≥4, and six-element candidates are the 128 labeled transversals. I inspected both bundled verification programs and independently ran `python3 /workspace/reproductions/four_mer_reproduction.py`. That exact-integer census counts the occurring four-mer masks of every binary word at each L=4,…,11 and uses a subset zeta transform to obtain the number of avoiders for every complement of U. Across all 65,536 masks the computed (size,count) rows are (16,1),(10,2),(9,50),(7,8),(7,52),(6,10),(6,14),(6,30). Of 128 transversals the exact maximum avoiding lengths are 8, 9, 10 for 10, 4, 16 choices respectively, and the 98 others fail at length 11, hence have cycles. The length-11 row therefore persists for all longer windows at size six, not by extrapolation. This is exhaustive finite computation with an analytic tail, not a theorem prover certificate.

## originality

PASS

The supported distinct claim is the joint exact labeled profile, especially the finite-window cardinalities and multiplicities before size six becomes attainable and the finer multiplicities at that transition. Neither the eventual thirty-set count nor the extremal path range or the first window attaining size six is credited as independently novel.

## value

PASS

The cardinality versus guaranteed window is the natural UHS tradeoff, and this is a complete sharp profile for a small standard de Bruijn instance rather than an isolated word length. The multiplicities say how much choice an exact design has at the optimum: ten size-six designs attain the shortest possible six-set window, fourteen work one position later, and all thirty work at eleven. The shorter-window larger optima provide additional exact benchmarks for optimization and enumeration; the known total and endpoint range do not supply them. No large-alphabet or algorithmic performance claim is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
