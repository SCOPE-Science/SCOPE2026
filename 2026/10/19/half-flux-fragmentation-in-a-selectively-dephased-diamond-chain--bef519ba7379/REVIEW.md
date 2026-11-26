# Independent mathematical audit

## correctness

PASS

For n≥3, the bridge-to-backbone row Gram matrix has diagonal 4 and cycle off-diagonal 1+exp(−iφ) in the stated gauge. Its Fourier eigenvalues are bounded below by 4−4|cos(φ/2)|>0 in the open flux interval. The dissipative Hilbert–Schmidt identity with all rates positive forces every peripheral operator to commute with all backbone site projectors; it is then backbone-diagonal plus an unrestricted bridge block. The Hamiltonian commutator of such an operator is block off-diagonal, excluding a nonzero imaginary eigenvalue. In the fixed algebra the backbone diagonal must commute with the Gram matrix, hence is constant on the whole connected cycle for φ≠π and arbitrary for φ=π. The bridge action on im Q† is determined by T Q†=Q† A, and there is no mixing with ker Q. Contractivity excludes a Jordan block at zero; the adjoint generator has the same fixed algebra, so the limit is its orthogonal projection, preserving the full dark compression. This yields the stated dimensions, bright weights and exact limiting states. The bridge input has weights 1/4 in each of two distinct half-flux cages and dark weight 1/2, giving 1/4+2(1/4)^2/2=5/16. Away from half flux the weight formula follows from Q†(QQ†)⁻¹Q; continuity at π gives the one-sided-in-flux comparison, and recentering the Fourier integral at φ/2 makes its nonconstant part odd, giving the thermodynamic limit at fixed interior phase. These arguments respect the order t→∞ before n→∞ and exclude endpoint rank resonances. Inspected RESULT.md §§1–4 and verify.py lines 10–108 without executing it; the code's finite numerical tests are not a proof of the rate or size quantifiers. Replay is python verify.py in the source directory with its requirements.txt.

## originality

PASS

Best of current evidence: coherent caging and the fixed-algebra technique are established, but the inspected comparisons do not give the specified periodic, selectively dephased model's bright stationary populations or its exact return jumps.

## value

PASS

The theorem separates coherent dark memory, which persists at every interior flux, from a sharp fragmentation of dissipative bright mixing only at π. The rank-two populations and the finite-size and thermodynamic return jumps give quantitative diagnostics even for unequal noise rates, not just an instance of coherent flat bands. The full stationary state also predicts returns from arbitrary inputs and makes the noncommuting limits operationally distinguishable without asserting a mixing rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
