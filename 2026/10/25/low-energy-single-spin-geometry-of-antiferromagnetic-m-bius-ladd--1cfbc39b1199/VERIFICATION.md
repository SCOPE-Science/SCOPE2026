---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The proof folds the 2n-vertex cubic Möbius ladder into n antipodal columns; every uniform column contributes one bad chord, mixed interfaces one bad cycle edge, and matched split-split links zero or two with a twisted seam. At even n>=4 the all-split parity obstruction gives minimum two defects, exactly 2n ground states; a single uniform column produces the 4n states at three defects and exactly two neighboring grounds each, with each ground connected to four such intermediates. Swapping a chord pair moves the sole defective link; one n-step circuit produces spin reversal and the 2n ground graph is a cycle with every edge doubled by two length-two paths. For odd n>=3 the graph is bipartite: states correspond to flipped subsets S and u(s)=|delta(S)|. The folded boundary classification identifies exactly two 0-defect states, 4n three-defect states, n(n+3) four-defect states, two connected B_n components and n(n-3) isolated 4-defect states. Sequentially flipping complete antipodal columns achieves at most five defects between the two grounds, and level-four disconnection proves sharpness. Independent exhaustive direct enumeration of all 2^(2n) spin configurations at n=3,4,5,6,7 reproduced all levels/component counts and even 2n-cycle doubled two-step adjacency. The graph geometry for every n follows from the parity/cut proof rather than the finite scan.

## originality

PASS

Even-width frustrated-ground counts and the odd Möbius-ladder cutwidth-five layout are previously known, acknowledged as premises/context. The complete level-3 even necklace transition graph, level-4 odd incidence-component/isolated-band classification and exact single-spin connectivity thresholds as a unified all-width theorem are not in the inspected Greeni–Rajasingh cutwidth proof or Kalinin–Berloff magnetic-ground source. Published Möbius-ladder Resultary hits concern matching/independence homology, not the spin-flip sublevel graph. Best-of-knowledge PASS; a specialized metastability or energy-landscape paper using different language remains a priority possibility.

## value

PASS

The antiferromagnetic Möbius ladder is a canonical frustrated cubic spin graph. Its low-energy single-spin transition network is an intrinsic dynamical invariant important for barriers and metastability, unlike merely determining ground-state degeneracy or cutwidth. The result supplies an exact topological graph description with isolated traps at a natural energy cutoff and a sharp communication barrier. The odd-even parity switch gives a meaningful structural phase split and a complete natural finite-energy window without requiring a general dynamics theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
