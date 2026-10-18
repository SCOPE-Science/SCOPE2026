# Scientific review: dihedral positive-type optimizer faces

## Correctness — PASS
For all \(n\ge3\), the irreducible representation matrices (including reducible endpoint blocks) give an exact necessary-and-sufficient Fourier-positivity criterion. The support-preserving group automorphism permits symmetrization without reducing the optimum. The two-positive-contact dual certificate proves the unique symmetric optimum whenever \(3\nmid n\); a factorized polynomial and endpoint constraints prove the complete optimal segment otherwise. Saturated full Fourier blocks force \(\operatorname{Im}f(r)=0\) and \(f(s)=f(sr)\) for **every** optimum, not just an averaged one. The standalone checker ran successfully for every order from 3 through 120, including 120 interval witnesses and independent two-variable LP vertex checks. Numerical experiments are corroboration, not the infinite proof.

## Originality — PASS, subject to residual risk
Bachoc–Pêcher–Thiéry (arXiv:1103.0444, especially Sections 2–3) already give the scalar theta values for cycle powers; the dihedral Cayley graph is a cycle square, so no new scalar maximum is claimed. The new statement determines all noncommutative complex **group-positive-type** equality cases, and shows the precise uniqueness/interval bifurcation and the forced disappearance of complex and reflection-asymmetric parameters. The inspected 2011 primary text constructs a real translation-symmetric optimum and proves the numerical value, but does not classify this complex nonabelian equality face. Nearby results on cyclic five-point Turán supports or dihedral harmonic ranks do not logically imply it. A hidden equality-face theorem in earlier graph semidefinite-program work remains a genuine possibility.

## Mathematical value — PASS
Determining a theta value and determining all positive-type optimal kernels are different problems. The theorem solves the latter for a natural, nonabelian, five-element support class, identifies when optimization uniquely reconstructs a positive-type function, and gives a precise arithmetic transition to a one-parameter family. The noncommutative Fourier rigidity argument is needed to rule out asymmetric and complex solutions that scalar symmetrization does not exclude.

## Scope of verification
No assertion is made about non-group-invariant theta SDP matrices or a general classification of dihedral neighborhoods. The statements are self-contained apart from the standard Fourier positivity criterion; the attached checker confirms only finitely many instances. Independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
