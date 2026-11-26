# Independent mathematical audit

## correctness

PASS

Direct product-basis calculation gives a shorter independent certificate. Put ψ_s=(|00⟩+s i|11⟩)/√2 for s=±1. In the specified MEMS, ψ₋ and ψ₊ have weights g+γ/2 and g−γ/2, and |01⟩ has weight 1−2g. After (I+i X⊗X)(R_y(π/2)⊗I)/√2 their respective images are |0⟩⊗|+y⟩, |1⟩⊗|+y⟩, and i|+x⟩⊗|−y⟩, with |±y⟩=(|0⟩±i|1⟩)/√2 and |+x⟩=(|0⟩+|1⟩)/√2. The remaining exp(iχ Y⊗Y) applies exp(±iχY) on the first qubit according to the second qubit's Y eigenvalue, preserving the product structure. Under T_B just the second factors conjugate; the three products remain orthonormal, since the first pair shares the same first-qubit unitary and the third has an orthogonal second factor. Thus the PT eigenvalues are g±γ/2, 1−2g and 0, proving both spectra including rank drops at the joins/endpoints. Squaring and summing the weights gives the stated purity ranges. Unitary conjugation then outputs the prescribed local copy of the MEMS. Below purity 1/3 the all-purity claim is trivial: a negative eigenvalue −a of the trace-one PT would force purity at least a²+(1+a)²/3>1/3, and two-qubit PPT implies separability.

## originality

PASS

Guan et al. already reported the exact family from a numerical inverse-MEMS search. The supported distinct content is the continuous analytic rank-three certificate with one fixed rotation and its common witness for both branches, not discovery of the gate family or rank-two existence.

## value

PASS

An exact construction closes the analytic gap left by the reported numerical second family. It certifies attainment at all purities over the full gate interval rather than at a grid of purity and gate parameters, and eliminates rotation search by giving a single explicit rotation and separable inverse images. The nontrivial rank-three scope is scientifically useful independently of the known rank-two existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
