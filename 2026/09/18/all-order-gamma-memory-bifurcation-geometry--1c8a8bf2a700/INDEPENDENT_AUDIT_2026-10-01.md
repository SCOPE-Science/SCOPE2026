# Independent scientific audit — SCOPE-20260918-1c8a8bf2a700

Audited at: 2026-10-01T07:11:57.147372Z

Disposition: **passed**

## Correctness — PASS

The Erlang chain gives the modal determinant \(P_k(z)=(z+X)(z+M)(z+B)^{k+1}+C\). On \(z=i\omega\), both phase and modulus are strictly increasing, so each admissible phase level is attained once. Counting odd and positive even multiples of \(\pi\) below the limiting phase \((k+3)\pi/2\) reproduces the stated crossing counts; an independent count check for the first ten orders matched both formulas. The logarithmic derivative has positive real part at every nonzero crossing, proving simplicity and transversality. Since every negative oscillatory threshold has modulus larger than \(R_k(0)\), the stationary threshold is the first negative-side loss, and the fixed-mean limit follows from the standard exponential limit of the Erlang factor.

## Originality — PASS

The full source paper was inspected. It defines the full Gamma family, but explicitly says it studies the weak \(k=0\) and strong \(k=1\) kernels and develops equivalent systems and bifurcation analysis for those two cases. No all-order phase-count theorem or fixed-mean spectral ladder is stated there or in the searches performed.

### Equivalent formulations

No equivalent all-order statement was found.

### Broader coverage

The generic chain trick does not by itself supply the crossing counts, primary stability interval, or source-specific modal classification.

### Exact database or table

The claim is an analytic classification rather than a tabulated invariant.

### Claim versus prior implication

The final theorem requires a genuine all-order elimination and phase argument, not a parameter substitution into a published theorem.

## Value — PASS

The all-order result turns a sequence of increasingly high-degree stability problems into one exact geometric classification, identifies when secondary crossings first appear, and links finite Gamma chains to the fixed-delay spectral limit. This is a motivated structural theorem for the same model family.

## Sources inspected

- Bifurcation Analysis of a Reaction-Diffusion System with a Cognitive Map Memory Kernel — https://arxiv.org/abs/2606.02250. NOT_COVERING_ALL_ORDER: The paper explicitly identifies \(k=0\) and \(k=1\) as the weak and strong cases studied and constructs only those two delay-free systems.

## Checked sources

- https://arxiv.org/abs/2606.02250
- https://doi.org/10.1007/s00285-019-01412-w
- Resultary semantic search

## Residual risks

- A general delay-equation source may contain analogous phase counting for scalar product forms, but no source-specific theorem implying this PDE statement was located.
- The spectral crossing theorem is not by itself a nonlinear Hopf theorem at simultaneous or degenerate crossings.

## Limitations

- This is a local spectral theorem at the normalized positive equilibrium. A full PDE Hopf bifurcation additionally needs simple-mode and nonlinear nondegeneracy hypotheses. Only integer Gamma orders are represented by a finite chain, and the fixed-mean limit is spectral rather than a nonlinear trajectory-convergence theorem.
