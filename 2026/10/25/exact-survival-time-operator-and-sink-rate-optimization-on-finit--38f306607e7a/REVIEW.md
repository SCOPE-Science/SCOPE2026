# Supported scientific assessment

## Correctness (C): PASS
All complex eigenvalues of the surviving-state generator have negative real part because the absorber drains the first site and path connectivity forbids a dark eigenvector. The integral of the survival norm is therefore the unique Hermitian Lyapunov solution. The claimed parity-dependent matrix satisfies the full Lyapunov equation with the correct terminal and sink boundary conditions, yielding the expectation for any initial pure or mixed state. Strict convexity of the local mean in the loss rate gives the unique optimizer for all injection indices at least two. The standalone `verify.py` passed 1,309 independent checks, including comparisons to direct integrated propagation. Numerical tests do not establish all-dimensional statements; the proof does.

## Originality (O): PASS, with residual priority risk
Riberi (arXiv:2605.08056) studies the same boundary sink on a semi-infinite line. Zhang et al. (arXiv:1706.09524) already derive the all-length end-to-end mean absorption time in Eq. (17), and the middle-initial-state three-site instance in Eq. (33) at zero dephasing. These cases are not novel. The assessed new claim is the exact matrix of integrated lifetimes for arbitrary coherent initial conditions and, as a consequence, the complete finite-path interior-site optimization rule. Targeted published-finding corpus queries and full primary-source comparisons found no stronger general closed matrix. General first-passage and Lyapunov theory could conceal equivalent prior coverage; independent literature review remains important.

## Value (V): PASS
Site-selective excitation makes the absorber's optimal strength a natural, physically controllable quantity. The exact all-size independence of the optimum from the number of sites beyond the injection point is a structural fact not available from an endpoint-only mean. The off-diagonal entries additionally quantify the influence of prepared phases on absorption time.

## Scientific limitations
The statement is restricted to finite homogeneous paths and one autonomous terminal Lindblad sink. No absorption-time variance, dephasing robustness or disorder classification is claimed. The self-review cannot substitute for independent checking.

Self-review: passed. Independent audit: not yet performed.
