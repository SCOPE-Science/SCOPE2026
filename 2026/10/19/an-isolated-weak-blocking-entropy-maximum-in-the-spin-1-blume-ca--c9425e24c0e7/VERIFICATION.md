---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

At each site the three energies up to a common constant are δu²−(a+c)u. Minimization allows the matching nonzero sign iff |a+c|≥δ and zero iff |a+c|≤δ. Thus ties matter at 1 and 2, and above 1 any nonzero site forces identical neighbours, proving counts 3 through 2 and then 1. The overlap-pair transfer trace counts labelled cyclic words without rotation quotients; for n=3 the two neighbours remain distinct. In the regime below 1 the six states traversed by the cycle ++,+0,0−,−−,−0,0+ are the nonconstant strongly connected component with a self-loop, and 00 is a separate loop. At δ=1 the same component connects in both directions to 00; mixed opposite-sign adjacent states contribute no periodic words. The run weights give Perron equations z³/(1−z)=1 and z³(1+z)/(1−z)²=1 respectively, with z the reciprocal growth. Primitivity and the exact polynomials give simple strictly dominant roots and trace coefficient one. The critical polynomial is −2 at the lower root and the renewal weight strictly decreases as the candidate growth λ=1/z increases, so the entropy maximum is strict. The sum of squared differences plus (δ−1)∑s_i² gives the exact ground-state contrast. Independent integer enumeration compares 30 finite counts to transfer traces and reproduces all characteristic factors; it does not replace the all-length argument.

## originality

PASS

Best-of-knowledge PASS for the complete exact zero-field weak one-site count and entropy classification on labelled Blume–Capel cycles, particularly the tie-induced entropy peak. Binary one-spin stability and transfer-matrix counting, and the Blume–Capel Hamiltonian, are prior. Neither the binary studies nor the inspected spin-1 nucleation passages compare precisely the three recolourings with weak inequalities and recover these ring sequences. The nearest catalogue analogue uses a binary next-nearest-neighbour Ising model and different growth polynomials, so the overlap is conceptual, not the same census.

## value

PASS

The complete positive-field classification gives an isolated entropy peak from equality moves that differs both from nearby blocked counts and from the true ground-state count. The exact growth constants and trace formulas characterize a motivated constraint problem on the full parameter axis, rather than an arbitrary finite ring or a thermal phase transition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
