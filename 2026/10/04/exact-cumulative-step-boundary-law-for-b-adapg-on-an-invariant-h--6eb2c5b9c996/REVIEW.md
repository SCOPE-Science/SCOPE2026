# Same-model review

## Correctness
**PASS.** The final claim reduces the Bregman proximal-gradient optimality condition exactly on an invariant radial line. For the Hellinger-ball kernel, \(\nabla\phi(tu)=t(1-t^2)^{{-1/2}}u\), which yields the stated scalar recursion. Positivity of the generated B-adaPG steps makes \(t_k\) strictly increasing. The inspected primary source proves the objective-infimum equality under its basic assumptions even without the Bregman-zone condition; applying that equality to the monotone scalar objective forces \(t_k\to1\). The remaining statements follow by telescoping, a contradiction if cumulative step mass were finite, weighted Cesàro convergence, and the elementary inverse-map asymptotic. The standalone numerical checker only tests these algebraic constants and is not used as proof.

Risk: the proof is special to collinear initialization and a radial quadratic. No statement is made about angular perturbations or generic boundary-active instances.

## Originality
**PASS, with a stated residual literature risk.** The primary B-adaPG paper explicitly identifies the same nonseparable Hellinger-ball kernel as violating its Bregman-zone assumption and uses it numerically on boundary-active least squares, but it does not state this invariant-ray theorem. Azizian--Iutzeler--Malick--Mertikopoulos already explain Hellinger boundary-rate phenomena and cumulative-step bounds in a broader Bregman framework; that general phenomenon is not claimed as new. The non-covered component located here is the method-specific combination of B-adaPG's unconditional objective-infimum guarantee with the exact radial dual recursion, which forces its own cumulative step mass to diverge and supplies the exact leading constants. Focused published-finding corpus queries found no matching published published-finding corpus statement. A recent broad paper, arXiv:2608.05536, was screened by abstract only because full-text retrieval failed; this is retained as a residual risk rather than treated as evidence of novelty.

## Value
**PASS.** The source paper singles out boundary-active problems outside its Bregman-zone assumption as a regime where its strongest sequence-convergence conclusion is unavailable and provides only proof-of-concept experiments. The present theorem supplies a clean analytic benchmark in exactly that regime: it explains convergence on a canonical radial least-squares instance, proves that the adaptive cumulative step mass cannot stall, and gives exact leading-order boundary and objective laws. This is useful as a sanity check and as a sharply solvable model for future analysis of nonseparable boundary kernels, while its symmetry limitations are explicit.

Same-model review: passed. Independent audit: not yet performed.
