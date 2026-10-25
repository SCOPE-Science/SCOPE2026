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

Every nonempty finite sampling window T separates according to its residue support S mod m. Exactly one possible active residue is binary for each starting phase that hits the binary coordinate, and the observed marker/binary alphabets are disjoint; thus active phases have disjoint languages and cannot collide with silent all-marker signatures. Uniform recurrence of x ensures a one-step base-index carry does not remove any sampled pattern. Therefore p_y(T)=sum_{r in S}p_x(U_r)+D_w(S). Since each base window size n_r independently attains p_x^*(n_r)=2n_r, one may choose arbitrary support S with |S|<=k, positive n_r summing k and obtain p_y^*(k)=2k+max_S D_w(S), with no extrapolation. In one-defect marker template A^(m-2)B, each distinct silent-phase signature is either a unique-B coordinate at an occupied->unoccupied cyclic transition or all-A if complement has adjacent pair, so D_w(S)=b(S)+1_{m-|S|>b(S)}. Sharp alternating runs attain max correction min{k+1,ceil(m/2)}. Independently exhaustively enumerated all supports of m=3..9 and direct phase signatures for all m and sampled k to m+1, confirming analytic formula; finite tests not proof for arbitrary m or irrational x.

## originality

PASS

Schlortt 2025 Theorem1.3 already proves eventual 2k+C for one binary pattern-Sturmian residue interleaved with constant marker residues; his examples already show some exact cases and a four-letter excess greater than alphabet-bound 2. These are credited, including existence of such larger offsets. The assessed result computes the COMPLETE all-k correction for EVERY marker template as a finite cyclic-signature optimization, plus unbounded excess ceil(m/2) at fixed four-symbol alphabet using single exceptional marker, including sharp finite onset. Le–Pavlov–Schlortt 2025 structural classification of recurrent low-complexity subshifts concerns allowed interleavings, not an evaluated all-template complexity function in relevant sections. General one-hole Toeplitz research could cover intersecting special bases; its complete 2006 full text was not read and is a material risk, though Toeplitz special instances do not dominate arbitrary uniformly recurrent binary pattern Sturmian bases.

## value

PASS

This closes an exact natural combinatorics question left open by the 2025 eventual-linearity structure theorem: which additive constant C occurs, when does it begin, and how does periodic skeleton geometry influence the complete function p_y^*(k)? A phase-signature formula for all templates and fixed four-letter unbounded correction is structural, broad in marker period and k, and independent of specific base realization. It is not a cosmetic new invariant or a repetition of the known 2k baseline and occasional special examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
