# Independent mathematical audit

## correctness

PASS

KKT on face S gives a_i x_i=1/Z_S for active coordinates and zero inactive gradient, forcing an unseen vertex as any vertex linear-minimization solution when S is incomplete. Since old and new supports are disjoint, f((1−gamma)x^S+gamma e_j)=(1−gamma)^2/(2Z_S)+a_j gamma²/2; exact 1-D minimization yields gamma=a_j^−1/(Z_S+a_j^−1). Substitution equals inverse-curvature weights on enlarged support, proving induction to full support. I inspected the actual nested artifacts/verify_fw_diagonal_simplex.py with exact Fraction arithmetic and independently checked several positive-diagonal examples and the four-coordinate chain (1,2,3,6). Formula and uniqueness require aligned coordinates, positive a_i, a VERTEX oracle and initial face minimizer; arbitrary convex combinations of tied vertices are explicitly excluded.

## originality

PASS

The result pinpoints an exact geometric case where algorithms generically distinguished in Jaggi and Clarkson coincide iteratively. The equal-curvature simplex squared-norm case appears in Jaggi as a toy setup; the arbitrary heterogeneous positive diagonal formula, invariance of weighted face minimizers and exact tie-independent termination are not stated in inspected primary sources. Elementary independent-derivation risk is acknowledged.

## value

PASS

A clean exact algorithmic collapse (ordinary line search equals fully corrective optimization) with m−1 finite termination from a vertex is a motivated and reusable structural benchmark. It explains when the computationally cheaper update automatically produces globally reoptimized weights, provides exact objective/gap values and a boundary to generic FW sublinear iteration results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
