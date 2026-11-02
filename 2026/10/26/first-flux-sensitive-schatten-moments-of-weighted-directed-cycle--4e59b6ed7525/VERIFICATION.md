---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Direct multiplication produces B_theta=R*R=D+ts(exp(2i theta)W^2+exp(-2i theta)(W*)^2), with diagonal D. A trace word of length j can have nonzero Fourier exponent only if 2(a-b) is divisible by n. For 1<=j<k=n/gcd(n,2), no nonzero value of a-b is possible; at j=k only all-forward and all-backward words produce the frequency, with traces nQ^r and n conjugate(Q)^r. AM-GM for |w_j|^2 yields |Q|^r <=(H/n)^k, with exact equality iff all n moduli coincide when H>0; if any weight is zero all phase-sensitive closed walks vanish. Verified 24 independently generated weighted shifts across n=3...8 with zero-weight and complex-weight cases. The combinatorial divisibility argument is the unrestricted proof.

## originality

PASS

The full Pal–Chandok 2026 arXiv HTML develops Schatten numerical-radius inequalities and Aluthge estimates, not a weighted-cycle phase onset theorem. A known magnetic-graph closed-walk trace identity is a genuine generic antecedent, and earlier published three- and four-cycle moment cases supply individual special cases. The audited all-n parity threshold, exact product amplitude, recoverability and AM-GM equality statement are not explicitly given in material inspected; broad magnetic-walk or weighted-cycle formulae remain priority risks.

## value

PASS

The first Fourier-detectable flux moment for every weighted directed cycle, together with exact recovery of its edge product from phase oscillation and a sharp fixed-Hilbert–Schmidt bound, is a natural structural classification of a standard cyclic-shift test family. Neither a chosen dimension nor just a numerical verification, it identifies the parity-dependent threshold and optimizer rigidity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
