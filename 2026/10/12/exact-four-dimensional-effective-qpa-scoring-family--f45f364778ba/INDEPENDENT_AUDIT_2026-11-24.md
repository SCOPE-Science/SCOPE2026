# Independent mathematical audit

## correctness

PASS

The actual scorer is specified by Eqs. (1)–(10) of arXiv:2605.25365v1; Eq. (7) alone is the entangling unitary. Starting from the encoded product state, apply CNOT(0→1), I⊗RY(t), and CNOT(1→0) in that order. This gives the four displayed real amplitudes. The two X rotations and the parity projector give the stated expectation: mixed ZY and YZ terms vanish on a real state, while YY supplies the two trigonometric terms with the minus sign. The encoder factors through the stated four coordinates, and the linear section θ_s=0, γ_d=ω_d/2, γ_s=ω_s/2 lifts the witness. Independent replay `python3 /workspace/reproductions/rank_certificate.py` multiplies the gate matrices and differentiates the projected amplitudes; it gives the displayed four-by-four Jacobian and positive determinant (222+174√2+180√3+129√6)/1024. Thus evaluations at the four real inputs already have rank four, so the local functional rank is four at the witness, and cannot exceed four anywhere. This is a maximal rank, not uniform pointwise rank (for instance the entangling-angle derivative vanishes when β=0), and not the rank of a single scalar evaluation. Inspected VERIFICATION.md and artifacts/verify.py without running the bundled script.

## originality

PASS

The circuit, definition and upper-bound reparameterization are prior. The distinct supported part is attaining that bound with an exact, nonzero Jacobian minor for the same score family.

## value

PASS

A four-coordinate circuit decomposition alone cannot tell whether the parity measurement hides further parameter dependencies. Exact maximal score rank settles the source's explicit unresolved interval and tells users of this scorer that all four effective coordinates are locally identifiable from suitable inputs, but only four. This is a concrete capacity statement for the measured family, not evidence for a training or generalization advantage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
