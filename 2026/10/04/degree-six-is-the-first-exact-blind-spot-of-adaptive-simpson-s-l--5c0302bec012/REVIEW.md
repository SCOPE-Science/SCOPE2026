# Same-model review

## Correctness
PASS. The claim reduces to three exact linear functionals on \(\mathcal P_6\). Their values on \(t^4\) and \(t^6\) determine the only nontrivial coefficients because both Simpson rules are exact through degree three and all three functionals vanish on odd monomials. Substitution gives the kernel condition \(4a_4+5a_6=0\) and the missed-error law \(-a_6/21\). The positive witness factors as \(t^4(5/4-t^2)+1/84\), proving a uniform positive lower bound on the interval. Exact-rational replay independently checks every displayed value and affine scaling.

## Originality
PASS with residual literature risk. The closest primary source already proves the broad phenomenon of premature termination and gives a degree-ten polynomial whose five sampled values all vanish. Gonnet separately identifies accidental cancellation between quadrature estimates as a cause of false-small error estimates. Those broader facts are treated as prior work. The inspected sources do not state the complete degree-six kernel, its exact missed-error functional, or a strictly positive degree-six witness with nonzero sampled values. Targeted semantic searches for degree-six, equal one/two-panel Simpson values, cancellation, and false-zero estimators returned no implication-equivalent result.

## Value
PASS. This is a natural sharp boundary for a classical stopping criterion, not an arbitrary polynomial slice. It distinguishes two qualitatively different failure mechanisms: a previously documented high-degree example that vanishes at every sampled node versus the minimal-degree cancellation mechanism here, which survives strict positivity and nonzero sample values. The exact kernel and \(1/5\) relative-error witness are compact regression tests for adaptive-integration safeguards and clarify precisely what information the local Richardson signal loses at its first possible degree.

Same-model review: passed. Independent audit: not yet performed.
