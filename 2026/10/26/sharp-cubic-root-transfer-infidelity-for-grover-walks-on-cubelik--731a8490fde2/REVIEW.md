# Scientific review: sharp cubic-root transfer infidelity

## Correctness — PASS

The theorem has two logically independent parts: a universal inequality over arbitrary distinct nonzero Boolean generators and an asymptotically matching connected family. The universal claim uses the **exact** Grover-coin Fourier rotation identity and exact character second moment, both explicitly reconstructed in `RESULT.md`. The sole new analytic estimate bounds \(1-\cos\rho\) by \(8\Delta^{2/3}m^2\), leading to the stated constant \(16\). This estimate accommodates Fourier modes with \(|m|=1\); the small-mode Taylor estimate is used only below the threshold \(\Delta^{-1/3}\). The cases \(\Delta<8\) are handled directly by the trivial probability bound.

The sharpness graph spans the full ambient Boolean group and has nonzero XOR target. Its Fourier character sum is exactly \(h\mathbf1_{\{\alpha=0\}}S_b+\xi\); the exceptional event has probability \(h^{-1}\). The conditional central limit theorem and cubic arcsine expansion give a nonzero Gaussian-phase defect. Crucially, the proof bounds the coin component *orthogonal* to the uniform coin by \(O(h^{-1})\), so it transfers the scalar-amplitude limit to the full position measurement with an \(O(h^{-2})\) remainder. This last step is necessary: a scalar overlap alone would not establish an asymptotically matching probability deficit.

The standalone finite checks compare the reduction against direct evolution for \(h=2\), and evaluate the exact finite sums for seven distinct \(h\). Those checks support, but do not substitute for, the infinite-dimensional-family limit and uniform proof. The limiting integral is positive without reliance on a decimal approximation.

## Originality — PASS (best knowledge)

The closest inspected result is J. Mulherkar, arXiv:2609.04503v1, Sections 3–5. It gives the exact Fourier formula and proves the weaker uniform estimate \(1-p_T=O(\Delta^{-1/5})\). Its concluding discussion explicitly identifies possible rate improvement as an open direction. The new estimate exploits the nonlinear phase defect directly rather than replacing the original threshold with a different arbitrary cut; more decisively, the construction gives a matching **lower bound on full position infidelity**, with a positive Gaussian cubic constant. Neither conclusion follows from the source's stated theorem alone.

Kempe, arXiv:quant-ph/0205083v1, Theorem 1, proves one-shot bounds for hypercubes, a proper subfamily with stronger symmetry; this does not cover the connected product-set examples. Mulherkar–Rajdeepak–Sunitha, arXiv:2108.13769v1, Section 5.3, numerically studies selected graph classes and states a general conjecture, but does not prove a uniform sharp exponent or construct a cubic-phase saturator. Continuous-time cubelike state-transfer claims use a different unitary evolution. Relevant research-index comparisons did not identify a matching universal upper-and-lower sharpness statement; search non-detection is not a uniqueness guarantee.

Residual risk: a general previously published character-sum concentration or Grover-transfer theorem not retrieved here could imply one or both bounds. No global publication-priority or independently certified novelty claim is made.

## Value — PASS

A central physical and algorithmic question is how reliably a parity-matched Grover walk reaches its distinguished XOR displacement after a number of steps linear in its degree. The prior work established asymptotically reliable transfer without the optimal general error scale. The new result determines the **best possible uniform algebraic exponent** and exhibits a constructive family that explains why arbitrary generator geometry can be substantially worse than a hypercube. The Gaussian cubic phase supplies a structural mechanism behind the worst-case obstruction rather than only a numerical refinement. The result also distinguishes unrestricted cubelike graphs from graph classes with much faster transfer.

The conclusion is confined to the prescribed one-shot observation window. It does not claim optimality among all times or noise-resistant behavior. These limitations do not weaken the sharpness assertion within the stated model.

Self-review: passed. Independent audit: not yet performed.
