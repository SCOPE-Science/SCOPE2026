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

The result is proved for all integer \(m\ge2\) and all strict radii \(0<r<s<1\). The core argument is analytic and does not rely on extrapolation from finite tests. Critical checks: expand \((1-z\overline w)^{-1}\) or \((1-z\overline w)^{-2}\) in the monomial basis, select degree residues via an \(m\)-point DFT, evaluate each two-by-two Gram block, differentiate its off-diagonal squared modulus with respect to \(\cos(m\phi)\), and apply pairwise convex majorization. In the Bergman case the derivative numerator \(2abtD+4tN\) is strictly positive for \(a=k+1>0\), \(b=m-k-1\ge0\), \(t>0\), \(D>0\), and \(N\ge0\). Direct Vandermonde independence prevents zero Gram eigenvalues, including aligned phases and arbitrarily close unequal radii.

The standalone `verify.py` requires Python 3 and NumPy and reconstructs independent full complex Gram matrices, compares the spectra with the analytic DFT block formulas, checks finite majorization consequences and the exact Hardy phase-deficit identity, and tests the explicit Bergman derivative positivity on finite parameter grids. Its recorded invocation is `python verify.py`, with the expected run output in `verification_output.txt`. This output checks the implementation and examples, not completeness over a continuum of radii/angles nor priority in historical literature.

Scientific limits: the claim covers only two equally sized cyclic orbits at distinct positive radii and only kernel powers one and two. Majorization is relative to angular rotations of the outer orbit, not to all possible sampling configurations. Historical priority is assessed to best knowledge only; independent audit is unperformed.
