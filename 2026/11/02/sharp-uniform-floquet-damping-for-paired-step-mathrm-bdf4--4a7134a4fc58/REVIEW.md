# Scientific assessment

## Correctness — PASS

The four-step difference monodromy is constructed from genuine degree-four Lagrange interpolation, so the constant solution is removed without frozen-coefficient substitution. The three characteristic coefficients are reproduced exactly in `VERIFY.py`. The scaled cubic Schur tests reduce to four explicit positive polynomial numerators, with a complete coefficient argument for \(t=r+r^{-1}\ge2\). The two singular limits give a nonzero conjugate pair of modulus \(1/\sqrt{21}\), proving sharpness. The independent role of finite numerical samples is explicitly limited to supplementary checks.

## Originality — PASS on inspected evidence, with specialist access risk

The closest materially read primary treatment is Wang–Ruuth (2008), particularly its derivation of VSSBDF4 and its Section 3.3, which quotes general adjacent-step sufficient restrictions and does not state a uniform sharp spectral radius for the repeating paired four-step pattern. This theorem covers arbitrary ratios outside those restrictions and supplies a new exact coefficient/certificate calculation. Older papers by Calvo–Grande–Grigorieff (1990), Calvo–Lisbona–Montijano (1987), and Skeel–Jackson (1983) were only available at abstract/metadata level; historical priority remains uncertain and these papers have not been declared definitively non-covering. The general Schur test itself is classical; only the sharp full paired-grid result is assessed as original. Earlier exact results for alternating BDF4 and a special three-periodic grid concern different step words and do not imply this finding.

## Mathematical value — PASS

The unboundedly heterogeneous step pattern \((h,rh,rh,h)\) has a *sharp ratio-independent damping margin* rather than merely fixed-r stability. This is a natural test of whether grouping equal steps into two-step bursts suppresses the neutral/unstable parasitic effects that can appear under other periodic mesh patterns. The explicit cubic and finite polynomial certificate can be reused as an exact numerical-analysis benchmark. The claim is restricted to homogeneous fixed-periodic zero stability, not arbitrary mesh or inhomogeneous convergence.

## Limits and priority risks

The coefficient and Schur proof establish the exact spectral claim, but not uniform matrix norm or forcing bounds over all ratios. Historical specialist BDF papers with incomplete full-text access may contain unlocated periodic-grid classifications. Further external mathematical and bibliographic auditing is appropriate.

Self-review: passed. Independent audit: not yet performed.
