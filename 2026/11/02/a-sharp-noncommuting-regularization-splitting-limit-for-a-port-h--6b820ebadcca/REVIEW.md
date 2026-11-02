# Scientific review: a sharp singular-regularization splitting obstruction

## Correctness

PASS. The proposed matrices satisfy the index-one constraint and the port-Hamiltonian sign conditions. The regularized continuous-time eigenvalues and consistent initialization give convergence of the unsplit flow to the DAE. The conservative and dissipative subflows are exact and their product was reconstructed symbolically: its scaled endpoint differs uniformly in the oscillation phase from \((\cos^2\theta,\cos\theta\sin\theta)\) by a vanishing term. The phase runs through every angle infinitely often as \(\varepsilon\downarrow0\), giving the entire circle and no other accumulation points. Finally the squared weighted error reduces, uniformly in phase, to \(t^2+(1-2t)\cos^2\theta\) with \(t=e^{-h/r}\), proving both sharp accumulation limits and the \(t=1/2\) boundary. Exact energy contractivity is preserved at every \(\varepsilon,h>0\). The supplied standard-library verification program checks 80 phase cases and independent matrix products. Limitation: the theorem is only for one exact-subflow step with fixed \(h\).

## Originality

PASS under best-knowledge comparison, with independent priority verification outstanding. The directly motivating paper arXiv:2308.16736, whose complete eight-page text and pertinent displayed equations were inspected, gives the \(E+\varepsilon I\) perturbation and conservative/dissipative Strang construction, but does not supply a fixed-\(h\), \(\varepsilon\downarrow0\) error barrier, the endpoint circle, or the sharp energy-metric extremal constants. The same-author nonsingular port-Hamiltonian splitting paper arXiv:2304.01766 analyzes a different nonsingular regime. The descriptor-system paper arXiv:2208.03574 studies dynamic iteration rather than these exact split subflows. A general stiff-splitting order-reduction literature precedent is acknowledged; its broad phenomenon is not claimed as new. Available mathematical-record searches and accessible historical claim comparisons identified no covering theorem. Residual risk: equivalent older singular-perturbation/splitting calculations may exist under different notation; the abstract-only general stiff-splitting source has not been fully compared.

## Mathematical value

PASS. The example resolves a physically motivated *compatibility* question raised by combining a regularization intended to recover a constrained port-Hamiltonian DAE with an energy-dissipative operator splitting. Neither exact subflow integration nor contractivity in the natural regularized Hamiltonian norm ensures consistency as regularization vanishes at fixed step. The sharp positive lower error accumulation, exact complete circle of outcomes and phase-independent half-unit error at \(h=r\log2\) quantify the obstruction, which is stronger than an isolated numerical counterexample. It supplies a precise boundary for evaluating asymptotic-preserving claims while leaving open coupled limits \(h=h(\varepsilon)\).

## Sources and remaining risks

The complete eight-page original source arXiv:2308.16736 was checked, including its regularization, splitting equations and conclusions. The closely related arXiv:2304.01766 and arXiv:2208.03574 were read in their algorithmic and introductory portions, and targeted earlier stiff-splitting literature was compared at abstract level. The cited 2015 stiff-splitting source was not verified at full-text level, so no claim of exhaustive priority is made. Numerical checks are supportive rather than complete proofs. The scientific conclusions have not received independent review.

Self-review: passed. Independent audit: not yet performed.
