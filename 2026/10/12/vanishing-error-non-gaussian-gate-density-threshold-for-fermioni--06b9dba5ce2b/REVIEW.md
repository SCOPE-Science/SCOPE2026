# Review

## Correctness
PASS. The proof starts from Theorem 2 of arXiv:2609.15059v1, including the exact definitions of \(r_{d_{\mathrm F},q}\), \(s_{g,q}\), and \(t_{g,q}\). The source proof explicitly establishes \(t_{g,q}\ge1\). In the sub-distance regime, \(s_{g,q}=0\) eventually and the exponent is linear in blocklength, giving the stated logarithmic fidelity rate. In the intermediate regime, the core fraction converges to \(\sigma=q(\gamma-\Delta/(q-2))<R\), so the entropy argument has the claimed positive limit. The robust form splits on whether \(g<r\) and gives a fixed positive lower bound on the entropy argument in either branch.

## Originality
PASS. The closest source, arXiv:2609.15059v1, states a finite-size fidelity upper bound and derives a lower bound for exact codeword preparation. The inspected theorem statement and Appendix C.2 do not state the positive-rate/positive-distance asymptotic two-regime envelope or the conclusion that the exact leading gate-density threshold remains necessary for fidelity tending to one. Searches using doped-Gaussian, fermionic-codeword, vanishing-infidelity, bounded-weight, and asymptotically-good-code formulations found no statement covering this implication. arXiv:2508.09928v1 provides high-rate Majorana-code context but is not a stronger preparation-resource theorem.

## Value
PASS. Exact state preparation is fragile as a complexity criterion: an exact lower bound need not automatically survive approximation. The result shows that, for code families carrying a positive density of logical information and protection, the finite-size source inequality has a strong asymptotic consequence: reducing preparation error to zero still forces the same leading gate density as exact preparation. It also separates an exponentially suppressed regime from a constant-gap regime, making the resource obstruction quantitatively interpretable.

The result does not establish achievability at the threshold, does not cover arbitrary non-Gaussian operations, and does not assert existence of a family satisfying additional hardware constraints.

Self-review: passed. Independent audit: not yet performed.
