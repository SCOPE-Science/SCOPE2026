# Independent mathematical audit

## correctness

PASS

From L∞ Poisson representation, u(0)=∇u(0)=0 removes Fourier modes 0,1. The derivative kernel is K_r(t)=(1-r²)sin(t)/(1-2r cos t+r²)². After odd symmetrization ψ, its first sine moment is zero. For H_r(x)=(1-r²)/(1-2rx+r²)² strictly increasing, subtracting H_r(0) and taking the L∞ bound yields |u_y(r,0)|≤(2/π)[∫_0^1 H_r(x) dx−∫_{−1}^0 H_r(x) dx]=8r/[π(1−r⁴)]. The trace −sgn(sin 2t) has zero constant/first Fourier modes and saturates the bound at every 0<r<1; its Poisson integral is u*(z)=(2/π)Arg[(1−z²)/(1+z²)] with |u*|<1 in the disk. For F=z+i(M−1)u, J=1+(M−1)u_y, so a positive-real-axis fold forces r≥r_M, unique from 8(M−1)r=π(1−r⁴); u* attains. Comparison with r_0(M)=M−√(M²−1) factors into (ρ−1)[πρ³+πρ²+(π+4)ρ+π−4]=0. The cubic is strictly increasing, has unique root ρ*∈(0,1), and strict comparison occurs exactly for M>(1+ρ*²)/(2ρ*)=4.4487630197851664... . Independent SymPy simplifications checked kernel/integral/factorization and independently recomputed 60-digit threshold, with numerical quadrature at r=0.1,0.5,0.9. These checks corroborate, not replace, the all-r analytic argument.

## originality

PASS

Best-of-knowledge PASS after searching Resultary and relevant published records, and directly inspecting seven highly relevant full mathematical texts. Borovikov explicitly gives u* and its fold equation; independently published exact centered univalence classification covers the same fixed u*, but neither establishes the sharp inequality for every zero-first-jet bounded real harmonic perturbation or its extremality over this whole shear class. Svetlik's highly relevant same-first-jet theorem gives a sharp value bound but not a sharp derivative; general gradient and higher-order mapping lemmas use different conditions. No examined prior result implies the complete derivative optimality and exact class threshold. This does not claim that unsuccessful keyword searches prove novelty.

## value

PASS

The natural class consists of all real bounded harmonic perturbations with vanishing first jet, the exact normalization required by the recent harmonic Landau counterexample. The sharp transverse derivative is an independently useful natural extremal invariant of this whole class, not merely the small numerical improvement from Borovikov's sufficient threshold. It proves a structural optimization boundary for earliest positive-real-axis Jacobian folding and identifies a common extremal for all radii and a unique exact parameter transition. Future efforts to improve the Landau bound using real-axis vertical shears need this exact optimal constant to distinguish this mechanism from nonreal or non-shear alternatives. No claim of solving the universal Landau problem, global injectivity of every arbitrary shear, or downstream landmark theorem is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
