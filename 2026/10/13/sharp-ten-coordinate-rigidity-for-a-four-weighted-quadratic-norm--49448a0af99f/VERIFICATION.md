---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For the positive norm x²+4y², any two representations impose the exact linear collision s_x+4s_y=s_u+4s_v. The eight displayed integer norm collisions inside indices 1..10 yield an 8x10 matrix with first-eight-column minor det -608, hence row rank 8 and two-dimensional kernel spanned by constant and k² vectors; this forces G(k)=Ak²+B at k<=10. The norm identity (n+8)²+4(n+3)²=n²+4(n+5)² propagates via G(n+8)=G(n)+4G(n+5)−4G(n+3) for n>=3. The F formula on E4 follows and conversely works. Independently enumerating every collision group for N=3..10 gave ranks [0,1,1,2,3,4,6,8], so N=9 has extra kernel dimension and explicit G(5)=1 witness. No finite enumeration is relied on for the infinite propagation.

## originality

PASS

PASS best-of-knowledge for the *minimal finite rigidity cutoff* 10, not novelty of the general nonlinear functional equation. You–Chen–Yuan–Shen (2016) already use some same norm collisions for a nonlinear linked equation and Khanh (2017) analyzes a broad auxiliary two-function equation via periodic characters; neither inspected result establishes the exact complete finite collision rank jump between N=9 and 10, nor its sharpness. Overlapping collisions and implicit derivations are flagged.

## value

PASS

The least finite window forcing a quadratic solution to a natural weighted norm representation equation is a meaningful rigidity invariant. The jump from nullity 3 at N=9 to nullity 2 at N=10 is sharp and explicitly certifiable; this is not a mere restatement of the previously solved infinite nonlinear equation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
