---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For n≥4, the local mask condition F_t(a,b,c) counts the two vertical plus four intercolumn occupied neighbors of each occupied site and is equivalent to stability. Its 64 ordered mask-pair transfer graph encodes EVERY cyclic frozen configuration by closed walks of length n, independent of small enumerations. An independent implementation reconstructed all 512 triple tests: threshold 4 has one cycle-bearing SCC with 31 states and 79 arrows; threshold 5 has a seven-state 10-arrow SCC plus isolated empty loop. Exact SymPy integer characteristic polynomials factor as x^7(x−1)P9P14 and x^4(x³−x²−3), verifying the full displayed P9,P14. Transfer traces independently matched physical occupancy brute counts n=4,5,6 and yielded n=7: Z4=(151,455,1754,5997), Z5=(14,17,47,86). The t=5 SCC encodes three row choices of vacancy and cyclic separation by two wholly occupied columns. Perron primitiveness/analytic weighted transfer plus Chebyshev imply density limits and void probability; independent eigenvectors give threshold4 α=3.4541747197759363, density=.7969487456890813, void=.00833835118453382; threshold5 α=1.8637065278191889, density=.9198294099517191, empty-column probability zero asymptotically. The exact small finite graph computation plus Perron theory proves all n≥4 and limit n→∞; short brute checks alone do not.

## originality

PASS

The width-three triangular Potts antiferromagnet transfer results count proper graph colorings, not threshold-stable occupancy subsets. Published bootstrap percolation simulations concern bulk transitions or final dynamical percolation rather than the exact uniform stationary fixed-state ensemble. The 4-vs-5 neighbour exact polynomials, hard-core vacancy classification, and positive-to-zero empty-column limit were not found in current primary searches, with a distinct unresolved bibliographic risk from the 1981 Kogut–Leath article.

## value

PASS

The six-regular three-row toroidal triangular graph is a natural smallest nontrivial periodic strip for high-neighbour bootstrap culling. Its adjacent thresholds 4 and 5 show a sharp structural change: entire empty columns survive in the four-frozen ensemble but are forbidden except for the all-empty state at five. Exact entropy, vacancy density, and finite transfer spectra form a motivated complete classification of this finite-width family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
