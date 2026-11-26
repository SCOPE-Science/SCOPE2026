---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Every vertex sees exactly the opposite shore, so its update depends only on its color and the opposite support. Updating each color present gives an exact map on 15² ordered nonempty support pairs, with no multiplicity assumption. Independently, review_evidence/reproduce.py 5 constructs reverse adjacency from set-valued updates and traverses backwards from the four recurrent pairs (three cycles). Their forward images close on the stated cycles; the reverse search reaches all 225 pairs, proving no further cycles, and computes exact distance to entry. The three basin sizes are 170, 1 and 54, with maximum tails 5, 0 and 6. The frozen CSV agrees in all 80 nonzero rows, with every other coefficient zero. Periodic supports cannot be entered later than periodic labelled states. Conversely, on the two nonzero support cycles every present zero is excited, so every label advances modulo four at all subsequent times, with exact least period four. The zero support is already the fixed all-resting configuration. Thus support tail equals labelled tail. Depth six occurs only at ordered sizes (3,4),(4,3); extinction depth five is attained with (1,2) and its transpose, with maximum four when both shores have one vertex. Feasibility is exactly having enough vertices to realize each prescribed support; each such realization count is U_i(a)U_j(b). The weighted coefficients therefore prove the census at every positive size. Summing nonzero basins and expanding the balanced expression symbolically verifies the seven-term identity and the leading 4(9/16)^n probability. As a separate check, explicit labelled adjacency simulation independently compares the full joint histograms of entry time and eventual period (not just basin totals) for all 115600 initial configurations with shores through size four. The arbitrary-size argument is the proof of the exact quotient and lift.

## originality

PASS

Best-of-knowledge pass for the frozen October contribution about transient basins and entry depths, not for recurrent-state classification. A distinct November entry gives the same four-state basin and sharp-transient theorems for both shores at least two. Its companion per-support table in fact encodes the full frozen histogram, even though its prose does not claim an explicit grouped census. The recorded catalogue publication date is 2026-11-01 versus 2026-10-26 for the frozen record. Thus the overlap is real and there is no new histogram information relative to that later table, but it does not show anticipatory publication. No absolute priority or independence claim follows. The same-day all-color recurrent theorem is credited for exactly the part it covers, without inferring any within-day priority.

## value

PASS

Four states is the natural next case after the three-state full census, and the biclique geometry permits an exact classification across all shore sizes. The useful increment beyond periodic states is the distribution of attraction and entry times from arbitrary initial colors. The sharp five-versus-six distinction separates the latest extinction from entry to persistent excitation, and the balanced exponent quantifies how rare extinction becomes, not merely how many periodic configurations already exist. This is mathematically useful as an exact benchmark and is not presented as a result for arbitrary networks or contact thresholds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
