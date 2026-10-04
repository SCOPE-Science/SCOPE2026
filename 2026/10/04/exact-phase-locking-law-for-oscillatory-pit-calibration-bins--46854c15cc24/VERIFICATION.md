---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof can be replayed from four exact identities: direct integration over a shifted bin; the sine-difference formula; the integral \(\int_0^1|\cos(2\pi kx)|\,dx=2/\pi\) for integer \(k\ge1\); and the finite cosine sums on reduced residue classes.

For the aligned grid, reduce by \(g=\gcd(k,N)\). The reduced modulus \(m=N/g\) is odd or even. In the odd case, coprimality permutes all residues and yields \(\csc(\pi/(2m))\). In the even case, the reduced frequency is odd and permutes odd residues, yielding \(2\csc(\pi/m)\) when \(m\equiv0\pmod4\) and \(2\cot(\pi/m)\) when \(m\equiv2\pmod4\). The only zero reduced cases are \(m=1\) and \(m=2\), equivalent to \(N\mid2k\).

The special case \(N=2k\) reduces exactly to \(E_{2k}(\tau)=\varepsilon_\infty|\sin(2\pi k\tau)|\). Thus the aligned phase is zero, the half-bin phase is maximal, and the uniform phase mean is \(2/\pi\) of the continuous discrepancy.

Supplementary finite numerical comparisons were performed against direct bin integration and against numerical phase averaging. They agreed with the closed forms in the tested cases, but the theorem does not depend on those experiments. No claim is made about empirical finite-sample ECE or adaptive binning.
