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

PASS applies to the repaired RESULT.md, not the frozen complex equality. Frozen line 9 says c=e^(−κt)f, but line 47 fixes c as the coefficient on |0><1| and line 35 correctly evolves |vacuum><j| with the conjugate amplitude. This is an actual phase error: with H_1=gσ_x, E_0=0, and t=π/(2g) for transfer between two sites, f=−i but c=+i exp(−κt). The repair gives the conjugate on |0><1| and f on its adjoint. Independently rederived the final statement: only site m flips sign on |vacuum><m|, so the rate on that invariant operator sector is −κ, and noiseless left-vacuum/right-excitation evolution gives e^(−itE_0)<j|e^(itH_1). Tracing all but k kills m≠k. Excitation conservation gives output populations (1−p,p) for input |1> and a pure vacuum output for |0>. For the normalized Choi matrix partially transposed on the output, the uncoupled entries are 1/2 and p/2, and the |01>,|10> block is one half of [[0,c],[conj(c),1−p]]. Its determinant is −|c|²/4. If c=0, the Choi state is diagonal and separable; otherwise the block is NPT. The damping factor is nonzero at finite κt, so the EB criterion is unchanged. With |f|=1 at τ=π/J, the negative eigenvalue has the stated form; at fixed |c|>0 it increases in 1−p, giving the displayed upper bound at 1−p=1, uniform in length for fixed J and κ. The frozen regression grid only tests magnitude-dependent algebra and is not evidence for the phase identity or the infinite family.

## originality

PASS

Reassessed for the repaired convention. The distinct contribution supported by the comparison is the exact invariant-sector formula for common-rate chain dephasing and its universal finite-time EB test and mirror-chain consequence. The finite-size numerical observation, the effective-model observation, and the channel-level Choi and PPT theorems are prior. Correcting the conjugation changes neither the mathematical scope of this non-overlap nor the norm-based criterion.

## value

PASS

The repaired result turns a published numerical observation into a uniform finite-rate theorem and identifies which invariant block controls the answer without solving population transport. The exact characterization at arbitrary transfer times, including zeros of the noiseless amplitude, and the explicit finite-rate Choi witness distinguish EB from low transfer fidelity. The value survives the correction because both the factor's modulus and its zero set are unchanged.

The dated certificate retains the supplied scientific assessment, sources and limitations.
