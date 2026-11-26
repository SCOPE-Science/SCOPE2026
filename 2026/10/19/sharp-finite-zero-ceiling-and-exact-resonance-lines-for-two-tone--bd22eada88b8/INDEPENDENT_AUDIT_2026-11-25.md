# Independent mathematical audit

## correctness

PASS

Gaussian integration of the generating function sends its parameter z to −iz under the stated Fourier convention. Consequently the nonzero overall phase can be discarded locally and the amplitude is e^(2πidt)A+e^(−2πidt)B with A,B real. Unless both vanish, cancellation requires A=±B and one of the two stated time slices; simultaneous vanishings give exactly the root-gap midpoint lines. Each branch, after multiplication by a positive analytic factor, is an exponential times a degree-n polynomial plus a degree-n polynomial. The (n+1)st derivative kills the second and leaves a nonzero Gaussian-free exponential times a degree-n polynomial (leading coefficient multiplied by (4πd)^(n+1)). Multiplicity-aware Rolle applied to any finite set of roots gives at most 2n+1 per branch; parity forces the even branch down to 2n including any origin multiplicity. For large d the translated branches converge in C¹ near each simple shifted Hermite root to a nonzero multiple of the unshifted window, giving one simple root per neighborhood. The odd branch also has the origin root, simple when h_n'(d)≠0, which holds eventually. At a simple branch zero the time derivative points in the complementary real direction and is proportional to the nonzero surviving shifted-window value, so the real STFT Jacobian has rank two. The degree-zero case has just the odd-branch origin and no resonance. The n=2,3 roots have the stated scaling. Source verification and its 95 reported integral, resonance and count checks were inspected, not rerun; finite grid sign changes were not used to prove the multiplicity bound. Nondegeneracy here refers to a simple zero of the complex STFT as a real map, not a nonzero gradient of its squared modulus.

## originality

PASS

The supported distinct claim is the joint sharp canonical-Hermite all-order scalar-multiplicity bound plus the exact line-resonance classification, not the Gaussian or first-order subcases or the underlying exponential-polynomial root bound. None of the inspected matching statements gives that combination or a stronger result covering it.

## value

PASS

For a minimal deterministic interference model, the theorem gives both a sharp quantitative limit on isolated zeros and a precise exceptional set where the geometry changes to entire zero lines. The exact count at large gaps and the root-gap formula at resonances are useful distinctly from the elementary branch decomposition, and avoid transferring random-field isolation or Gaussian-window intuition to arbitrary Hermite windows. No exact count at every nonresonant gap is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
