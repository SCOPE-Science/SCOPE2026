# Self-review

## Correctness
**PASS.** For five firms at fixed common integer total \(S\), \(CR_4\) is determined only by the smallest firm while HHI is determined by the square sum. A strict reversal with \(S\le12\) would require a profile with minimum at least \(2\) to have larger square sum than a profile with minimum \(1\). Exact extremal bounds give maximum-versus-minimum square sums \(20<22\), \(25<27\), and \(32=32\) at \(S=10,11,12\), while \(S<10\) cannot support minimum \(2\). At \(S=13\), \((5,2,2,2,2)\) has square sum \(41\), and exactly two minimum-\(1\) profiles fall strictly below it: \((4,3,3,2,1)\) and \((3,3,3,3,1)\). The packaged verifier independently reconstructs the full finite domains and returns `VERIFY_OK`.

Risk: the boundary is a rational lattice-complexity invariant; it is not a claim about a privileged physical sales unit.

## Originality
**PASS.** Prior work explicitly compares concentration ratios with HHI and explains that HHI sees firm-size dispersion that the top-four ratio suppresses. That qualitative difference is not claimed as new. The accepted claim is the exact first strict reversal geometry for positive rational five-firm markets, including the sharp common scale \(13\), the complete two-pair boundary, and two infinite exact families. Published-result searches, exact-vector searches, and exact-boundary web searches did not locate equivalent coverage.

Risk: failed search is not proof of bibliographic uniqueness. The highly relevant 1986 Sleuwaegen–Dehandschutter paper could not be read in full; its exact contents remain a specific residual risk.

## Value
**PASS.** \(CR_4\) and HHI are canonical market-concentration screens and were explicitly contrasted in antitrust policy because they react differently to share dispersion. The smallest strict reversal gives a compact exact benchmark for that policy-relevant difference: one metric reacts only to the fifth firm's share in a five-firm market, while the other can be dominated by one large leader. The infinite families show that the disagreement is structural rather than a one-off enumeration artifact.

Self-review: passed. Independent audit: not yet performed.
