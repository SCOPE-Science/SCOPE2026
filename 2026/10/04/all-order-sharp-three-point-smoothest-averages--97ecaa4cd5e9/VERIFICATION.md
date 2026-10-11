---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For a symmetric normalized radius-one kernel, write endpoint weight \(a\) and \(b=4a\). Plancherel reduces the norm exactly to \(2^k\max_{0\le t\le1}t^r|1-bt|\). When \(b\le1\), pointwise monotonicity in \(b\) forces the best value at \(b=1\), and differentiation gives the unique interior maximum \(c_r\); Fourier nonnegativity is exactly \(b\le1\). When \(b>1\), the positive branch has maximum \(c_rb^{-r}\) at \(t=r/((r+1)b)\), while the negative branch is increasing and has maximum \(b-1\) at \(t=1\). Their unique crossing gives the unique global minimizer and the displayed equation. Setting \(y=r(b_r-1)\) gives \(y(1+y/r)^r=rc_r\to e^{-1}\), hence \(y\to W(e^{-1})\) and the two asymptotics follow. The packaged numerical verifier is consistent with these exact branch formulas but is not needed for the proof.

## originality

PASS

The highly relevant 2026 primary paper was read in full HTML through its introduction and main theorem statements. It establishes unrestricted orders \(1,2,3\) (with earlier sources for \(1,2\)) and Fourier-nonnegative orders \(2,4,6\) for arbitrary support radius, together with a general relation, but it does not state the all-order radius-one minimax formula. The older Kravitz--Steinerberger and Richardson results cover the low-order specializations. Resultary searches found no prior equivalent all-\(k\), three-tap formula or Lambert-\(W\) asymptotic.

## value

PASS

Support radius one is the first nontrivial averaging window and gives a natural boundary of the general smoothest-average problem. Solving it for every derivative order provides exact sharp constants and optimizers in rows where arbitrary-radius questions remain substantially harder, and the Lambert-\(W\) limit gives a clean quantitative comparison between unrestricted and Fourier-positive smoothing. This is a natural complete classification, not an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
