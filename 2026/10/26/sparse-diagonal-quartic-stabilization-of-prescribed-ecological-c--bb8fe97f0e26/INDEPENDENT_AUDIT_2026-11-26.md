# Independent mathematical audit

## correctness

PASS

Independently reconstructed the proof. Write the fixed per-capita residual at the target as R_i=r_i+(Sz)_i. The equilibrium condition eliminates alpha_i by alpha_i=beta_i z_i-R_i/z_i^2. This leaves the off-diagonal Jacobian z_i S_ij unchanged and the diagonal equal to z_i S_ii-2R_i-beta_i z_i^3. Since z_i>0, increasing beta_i makes alpha_i positive and the rightmost edge of the row Gershgorin disc strictly less than -gamma. Polynomial local uniqueness and invariant coordinate hyperplanes give nonnegativity. With M=max_i x_i, at a maximizing coordinate the derivative is at most M(R+LM+UM^2-BM^3), where R=max_i|r_i|, L=max_i sum_j |S_ij|, U=max_i alpha_i and B=min_i beta_i>0. At and above the stated K>max(1,4R/B,4L/B,4U/B), the upper Dini derivative is at most -BM^4/4, giving an invariant, finite-entry box and excluding finite-time escape. For the worst case S=0, r_i=-1, z_i=1, no monomial fails equilibrium and a lone c x_i^p requires c=1 and gives positive eigenvalue p, on every coordinate. This is a support lower bound in the stated self-only class, not a claim of global attraction or unrestricted support optimality. The package's rational checker is a finite spot check; I inspected but did not execute it.

## originality

PASS

Credit the existing fixed-r,S prescription with unrestricted tensors and the close indexed self-only construction. Neither source establishes the complete sharp self-only support and orthant-wide finite-entry absorbing-box result. The distinct mathematical content is the universal sharp sparse realization with dissipativity, not the general existence of stabilizing higher-order terms, a new interpolation method, or independent novelty of arbitrary targets and margins.

## value

PASS

The restriction to own-density terms answers a specific feasibility question left open by allowing arbitrary mixed tensors. The sharp worst-case support cost and the guaranteed absorbing box give usable information under arbitrary fixed, possibly destabilizing pairwise data; they are not benefits inferred from numerical examples or claims of global coexistence. Value is in the constraint and its sharp guarantee, not the standard Gershgorin or polynomial comparison tools.

The dated certificate retains the supplied scientific assessment, sources and limitations.
