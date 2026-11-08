# Independent mathematical audit

## correctness

PASS

The full RESULT.md proves the all-dimension necessary-and-sufficient inverse-source classification for stable dX=-AX dt+sqrt(2D)dW with whole-vector independent Poisson resetting: the stationary adjoint equation forces mu=p-r^{-1}L*p, with p=N(m,S), Q=(AS+SA^T)/2-D, h=Am, tau=tr(S^{-1}Q). Gaussian differentiation gives rho=p[1+(y^T Q y+h^Ty-tau)/r], y=S^{-1}(x-m), and expectation identities prove normalization. A quadratic polynomial is globally nonnegative exactly when Q>=0, h lies in Ran Q and r>=tau+h^T Q^+h/4, with the equality singular boundary. A last-reset resolvent/coupling establishes existence and uniqueness, while isotropic covariance optimization separates r<dk, r=dk with unattained large-displacement boundary, and r>dk where any displacement is attainable by choosing finite S. Independently checked a nontrivial two-dimensional diagonal example: for A=diag(1,2), D=diag(1,2), S=diag(2,3), m=(1,0), the source positivity threshold is exactly 25/12; at the minimizing y its tilt is zero. Script verify_gaussian_reset.py was read but its claimed 71-check log was not treated as proof. Boundaries d>=1, D,S positive definite and stable A are stated.

## originality

PASS

Compared exact full claim, not generic resetting: Olsen 2023 (arxiv:2310.04840) derives forward OU moments from supplied random refresh laws; Trajanovski et al. 2023 (arxiv:2301.12304) analyze fixed reset points and comb OU. These do not state a multivariate inverse *positive probability source* criterion including pseudoinverse/range and the sharp isotropic attainable-mean transition. Classical Fokker-Planck inversion is pre-existing and is not claimed as independent novelty. Resultary semantic research hits concern OU sensing and stationary moment constraints, not a matching inverse design. Best knowledge PASS with explicit broader inverse-generator literature risk.

## value

PASS

A natural inverse nonequilibrium-control question asks which Gaussian stationary states are realizable by randomized resets despite non-Gaussian refresh mechanisms. The theorem supplies a complete continuously parameterized necessary/sufficient matrix criterion, a uniquely forced positive law with singular boundary, and a sharp transition in attainable mean displacement when target variance is free. These are nontrivial structural reachable-set facts with practical parameter-selection implications beyond forward OU moments or textbook completion squares. It does not address nonlinear drifts, time-dependent reset laws or cost optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
