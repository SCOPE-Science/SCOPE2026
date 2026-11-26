# Independent mathematical audit

## correctness

PASS

The primary integrator source confirms the placement of the exponential inside the jump Kraus factors. The Kraus completeness relation is e^(-hD) + integral_0^h D e^(-sD) ds = I. On diagonals the map is I-L diag(f_h(d)), with positive holding probabilities and an irreducible support; its fixed probability is proportional to 1/f_h(d) by the connected Laplacian kernel, or detailed balance. Applying it to the uniform vector and using strict decrease of f_h proves the regularity equivalence for every h>0. On each two-entry coherence block, the eigenvalues are exp(-hs) ± w_ij f_h(s), s=(d_i+d_j)/2. They have modulus below one for n>=3 since s>w_ij on each edge. For n=2 the symmetric coherence has eigenvalue one and sufficiently small real coherence on I/2 gives non-diagonal stationary densities. The one-step diagonal displacement is h^2 Ld/(2n)+O(h^3), whereas the stationary displacement is h(d-bar(d)1)/(2n)+O(h^2). The entropy deficit at uniform has quadratic term n/2 times the squared norm of the displacement, giving the stated h^4 and h^2 coefficients and the numerical example. A fresh finite check compared direct jump and block matrices, stationary residuals, iteration, and high-precision entropy ratios on the weighted three-vertex witness, and included a regular control. It corroborates the algebra without certifying the universal theorem.

## originality

PASS

The method, positivity, trace preservation, and diagonal detailed-balance argument are not new. The supported distinct content is the exact all-step phenomenon on weighted undirected edge-flip graphs: irregularity creates degree-biased equilibrium, with convergence of the quantum state despite the possibility of coherences, and distinct explicit leading entropy defects at one step and at equilibrium. The closest same-method indexed result treats a uniform directed jump cycle rather than the irregular Hermitian family.

## value

PASS

It identifies and quantifies a persistent equilibrium error in a positivity- and trace-preserving integrator. The bias is first order in step size although the local entropy signal at the unbiased state is fourth order, so checking only one step can obscure the long-run distortion. The all-step regularity criterion and minimal irregular example make the conclusion actionable for this natural family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
