# Independent mathematical audit

## correctness

PASS

Normalize the nonzero center b by simultaneous rotation, which preserves each circle maximum and the modulus of the derivative. For the normalized symbol phi use (phi-t)/(1-t phi)=zh(z), with |h(0)|=c. Schwarz–Pick on h gives |zh|<=u_c(r); the inverse disk automorphism has maximal modulus at the positive real point on each modulus circle, and |1-zbar phi|>=1-r|phi|. The symbol using h_c(z)=(c+z)/(1+cz), with h_1=1, makes all of these inequalities exact for every positive real r and rotates back to center b. Both u_c and E as a function of u are nondecreasing, so an upper bound, not just equality, on the normalized derivative gives the stated constrained optimum. The profile is at most 1+tr; its limit at r=1 is 2(1+t)(1+c)/[(1+t)(1+c)+2(1-t)], strictly below 1+t for t>0 and c<1. Thus an extremizing sequence at the universal bound requires c=1. The resulting Möbius map phi=(t+tau z)/(1+t tau z) extends continuously across the circle. A subsequential boundary limit zeta of the extremizing sequence must be a fixed point, and comparison with (1-r^2)/(1-r|phi|) gives a limiting deficit ratio at most (1-t)/(1+t). The automorphism identity gives the ratio (1-t^2)/|1+t tau zeta|^2, forcing tau zeta=1 and then zeta=tau=1. Conversely the aligned map gives 1+tr on its distinguished radius. At t=0, Schwarz's lemma and evaluation at 0 give radius 1 for every such symbol. The Finding uses the correct supremum over r<1; the term ‘maximum’ in the limitations should not be read as attainment in the open interval (e.g. c=1, t>0). A separate bounded replay, python3 /workspace/branches/bb7b8615-8deb-411b-9e00-d27255140560/reproduce_jet_envelope.py --steps 25, passed 81900 exact-rational and 178750 complex sample checks; the universal argument does not rely on sampling.

## originality

PASS

Distinct to the best of the inspected evidence for the sharp simultaneous Berezin profile at fixed modulus of the center and bounded normalized derivative, and for the nonzero-center equality characterization. The transform formula, the universal 1+t bound, the origin-fixing endpoint, and the Schur/Schwarz–Pick reductions are not new.

## value

PASS

The first derivative refines a natural operator-radius bound. Rather than just transplanting a single disk-map inequality, the result supplies one extremizing operator for a whole radial profile and identifies exactly when the universal operator bound can be approached at the boundary without assuming boundary regularity. That phase-sensitive global equality conclusion and the sharp constrained profile are useful even though the initial Schur step is standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
