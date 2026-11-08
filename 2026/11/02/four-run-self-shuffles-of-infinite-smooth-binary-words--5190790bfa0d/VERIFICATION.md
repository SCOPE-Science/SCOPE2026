---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Reconstructed the smooth derivative with deletion of singleton boundary runs, factoriality, ten parity-return atoms of length at most eight, and greedy even-Parikh cut blocks. The first parity cut after distance 38 must lie in {38,40,42,44}; each block has a bounded-4 self-shuffle coloring. Swapping both colors between blocks forces a color change at block boundaries and preserves the two equal infinite output streams. Independently generated exactly 22,194 nonempty smooth words through length 44 and rechecked ALL 2,764 TSV positive certificates (length counts 538,674,682,870), with exact root equality and maximum monochromatic run four. Exhaustive independently implemented prefix-comparable residual-state search certified all twelve stored negative witnesses, including the length-38 bound-three obstruction and shorter four-length windows. These finite certificates prove the finite window; the infinite theorem additionally requires the parity-atom argument and infinitely many even-Parikh prefixes.

## originality

PASS

Best-of-knowledge new exact bounded-color-run control 4 for an infinite smooth self-shuffle and sharp finite-window threshold 38, not the earlier shuffle-square existence, parity-atom classification, or a claim of infinite optimality. The accessible full Kilpatrick primary text gives an explicit weaker 48 run bound; Zwierzyński primary abstract gives even-Parikh criteria but complete text remained inaccessible, so originality retains a direct same-object risk.

## value

PASS

A substantive controlled infinite-shuffle construction for a canonical low-complexity word family. The sharp four-length finite window and nontrivial bounded-color certificate serve as reusable combinatorial structure, not a renamed parity-only existence result; the quantitative reduction from 48 to 4 is mathematically meaningful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
