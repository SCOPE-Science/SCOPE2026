# Scientific review: sharp species–diffusion cutoff for alternating frozen waves

## Correctness — PASS

The nonlinear source equations, the exact quadratic interaction sum and the alternating sine initial state were reconstructed from arXiv:2601.06314v1, equations (6) and (21)–(23). Direct substitution gives the scalar Allen–Cahn evolution \(z_t=Dz_{xx}+(-a/N)z(1-z^2)\) on the invariant alternating-species manifold. Reflection and half-period anti-symmetry reduce that scalar evolution to a strictly positive Dirichlet initial-value problem on a half-circle. Poincaré and the energy differential inequality prove homogenization at and below the exact first-mode threshold, including the equality endpoint. Above it, comparison with a strictly positive sine subsolution excludes zero, while the strict monotonicity of the Jacobi half-period supplies exactly one positive Dirichlet equilibrium. The Allen–Cahn energy and parabolic compactness prove convergence to that equilibrium. Substituting the squared elliptic sine into the linearization produces an explicit positive Lamé eigenfunction and the displayed positive eigenvalue.

The extraction and polynomial identities were independently verified by `verification.py`: 22,610 finite assertions passed with Python's exact rational arithmetic for the core source algebra and elementary numerical tests for elliptic periods. Independent Fourier-periodic integrations separately agreed with the predicted two branches; these computations are **not** used as proofs of the infinite-dimensional dynamics. Primary scientific limitations: only even species, equal diffusion, \(-1<a<0\), the specified sine initialization, and periodic spatial domain are covered.

## Originality — PASS, with priority qualifications

The closest source is Visomirski–Griffin, *Coherent Structures and Travelling Waves in Spatial Replicators from a Biased Volterra Lattice*, arXiv:2601.06314v1 (posted 9 January 2026), Section 4.2, Conjecture 2, and Appendix A. It provides the defining model and numerical finite-even examples and conjectures persistent frozen waves at all even sizes for the sine initialization. Its inspected full HTML text does not give the exact alternating Allen–Cahn reduction, the if-and-only-if cutoff, the Jacobi selection formula or the explicit positive instability eigenvalue. These results are not implied by its numerical instances, and the large-even homogenization case directly separates the theorem from the conjectural unrestricted extension.

The pre-existing Allen–Cahn gradient-flow theory is background mathematics rather than a novelty claim; Westdickenberg (2020/2021) describes standard scalar energy and metastability, and NIST DLMF supplies Jacobi and Lamé identities. The present source-specific multi-species reduction and cutoff require a distinct structural comparison. Searches of published published-finding corpus findings and the broader literature located related but non-covering Allen–Cahn numerical methods and different reaction–diffusion models. The later July 2026 journal version was identified bibliographically but not read line by line; earlier independent derivations of the same reduction may exist. No independent priority guarantee is asserted.

## Mathematical value — PASS

This is not a free-parameter curiosity: it gives an exact finite-species obstruction to an explicit published broad conjecture. The threshold \(-aL^2=4\pi^2ND\) identifies when the paper's prescribed sine-patterned ecological niches persist versus wash out, with the equality case included. The nontrivial branch has an exact selected profile for every permitted supercritical parameter and an explicit positive growth exponent proving instability under unconstrained perturbations. The \(N=52\), \(a=-1/2\), \(D=1/100\), \(L=2\pi\) example belongs to the source's natural parameter range and sharply contrasts with its \(N=4,6,8\) numerical examples. This clarifies a real dynamical gap and the meaning of visually stationary numerical patterns.

## Closest literature and limitations

- M. Visomirski and C. Griffin, arXiv:2601.06314v1, §§2, 4.2 and Appendix A; later *Chaos, Solitons & Fractals* **208** (2026), 118260. Accessible preprint full text inspected; journal bibliographic details verified.
- M. G. Westdickenberg, *On the Metastability of the 1-d Allen–Cahn Equation*, *J. Dyn. Diff. Equat.* **33** (2021), 1853–1879; foundational scalar Allen–Cahn methods and metastability, not this multi-species source-specific cutoff.
- NIST Digital Library of Mathematical Functions, Chapters 22 and 29; known Jacobi and Lamé identities, not a prior multi-species theorem.
- Published published-finding corpus near-neighbor records on stabilized Allen–Cahn discretizations, porous and catalytic reaction–diffusion systems, and other parity-restricted models do not state or imply the alternating biased Volterra model classification.

This theorem does not classify every possible frozen-looking state, the full-system basin structure, or traveling waves. The elliptic patterns are attractive only within a fixed-node symmetry class and **unstable** in the larger full periodic alternating class. Full journal-version text comparison and independent mathematical validation remain open.

Same-model review: passed. Independent audit: not yet performed.
