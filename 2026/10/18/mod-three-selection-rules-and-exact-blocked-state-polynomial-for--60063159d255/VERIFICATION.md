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

Checked the repaired statement and proof with the original mathematical formulas unchanged. A flip changes exactly three terms even at N=3, so a strictly blocked word has at most one defect in every cyclic triple. Over F_2 the homogeneous relation gives b_{i+3}=b_i, hence a trivial kernel if 3 does not divide N and a two-dimensional kernel otherwise. In the latter case each of the three defect residue sums equals the total spin-bit sum; these are two independent compatibility constraints, hence sufficient by the kernel calculation. A cyclic admissible word corresponds to exactly one closed memory-state path (the all-plus word stays in the last state). On divisible lengths the four-term projector precisely cancels the fourfold spin preimage factor, and the three nontrivial weights are cyclic rotations of the signed three-step transfer block. This proves the blocked polynomial. Two physical defects at divisible lengths must be in a single residue class; their cyclic gaps are at least three, giving 4 times 3 binom(N/3,2) blocked first excitations for N>=6. The N=3 excited word is all minus and is not blocked. The unrestricted polynomial follows by dropping the local constraint, consistent with the cited prior transfer calculation. The characteristic polynomials u^3-u^2-1 and u^3-u-1 each have one real root greater than one; their two conjugate roots have modulus the inverse square root of that root by the product relation. Since lambda^3>2>p, the stated error and common entropy follow. Independent direct enumeration by bitwise products and individual flips agreed coefficient by coefficient with both polynomial formulas for N=3 to 14. Replay: python3 /workspace/review_evidence/3-check.py.

## originality

PASS

The frozen presentation overcredited the periodic-image rule to the new calculation and omitted a directly equivalent unrestricted enumeration. Turban already gives the same parity projector and multiplicity on divisible lengths; the unrestricted density polynomial follows for all lengths from his equations. The corrected principal claim is the parity-projected transfer matrix restricted to strictly blocked physical spin states and its explicit subleading plastic-constant term. The repaired file credits the known inputs, reports the excitation counts as consequences, and corrects its description of Kisker's discussion of the ground states. The scoped principal claim is not explicitly stated or already evaluated in the compared sources.

## value

PASS

The corrected result determines the exact energy-resolved number of strictly blocked physical states, not merely the admissible local words or the equilibrium partition function. This is a natural finite-size invariant for a classic metastable chain: commensurability removes entire physical sectors, and the signed transfer quantifies an exponentially growing subleading blocked-state term that does not change the known entropy. Neither a small exception nor a recomputation of the unrestricted formula is the surviving contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
