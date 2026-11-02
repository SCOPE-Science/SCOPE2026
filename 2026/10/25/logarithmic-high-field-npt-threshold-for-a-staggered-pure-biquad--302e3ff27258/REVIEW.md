# Independent mathematical audit

## correctness

PASS

For two spin-1 particles (S1·S2)^2=I+3P0 (singlet projector), so remove scalar -JI to obtain H'=hD-3JP0. On total magnetization zero, in basis (|1,-1>,|0,0>,|-1,1>) the dimensionless A_epsilon has diagonal (2,0,-2)-epsilon and alternating off-diagonal signs; remaining product states retain diagonal weights 1,e^{±x}, x=h/T. Partial transpose gives exactly three 2x2 positivity inequalities |G_ac|<=1, |G_ab|<=e^-x, |G_bc|<=e^x where G=exp(-xA_epsilon). The smallest eigenvector near epsilon=J/h=0 has components (epsilon/4,-epsilon/2,1)+O(epsilon^2), eigenvalue -2-epsilon+O(epsilon^2). In x=(1/2)log(4/epsilon)+O(1), epsilon*x->0 and G_ac=(epsilon/4)e^{2x}(1+o(1)), while G_ab=O(epsilon), G_bc=O(1); first block thus crosses at x*=0.5 log(4/epsilon)+o(1), other blocks remain PPT there. First-order Duhamel bounds for smaller x exclude an earlier crossing for these other blocks, so the supremum NPT temperature is T_NPT=2h/(log(4h/J)+o(1)), not a statement about PPT separability. Independently diagonalized 3x3 A and brent-bracketed all three block inequalities at epsilon=1e-2,1e-3,1e-4, obtaining first roots 2.978270256...,4.144701322...,5.298027449... and later roots for the other blocks; gap to 0.5 log(4/epsilon) decreases. Fixed epsilon tests cannot prove asymptotics. Inspected RESULT.md 2a68b3..., verify_threshold.py cca14c..., status files.

## originality

PASS

Closest known exact pure-biquadratic two-qutrit thermal threshold in Resultary uses a UNIFORM field B(S1z+S2z); this field conserves total spin projection and has field-independent positive-temperature threshold. The staggered field h(S1z-S2z) breaks that symmetry, mixes the singlet with m=0 basis states, and creates an h/log h threshold. Other inspected spin-dimer works use bilinear XXZ exchange, DM or single-ion anisotropy. No exact same-Hamiltonian high-field NPT coefficient or first-block proof identified; nonlinear-coupling historical text remains only partly accessible.

## value

PASS

A sharp asymptotic entanglement transition for a canonical spin-1 two-site Hamiltonian identifies a nontrivial logarithmic field scale and responsible partial-transpose block, contrasting strikingly with the uniform-field model. The exact coefficient 2 and logarithm constant 4 are not merely a dimension or unit renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
