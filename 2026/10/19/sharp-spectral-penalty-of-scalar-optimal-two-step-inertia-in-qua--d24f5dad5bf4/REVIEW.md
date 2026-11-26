# Independent mathematical audit

## correctness

PASS

The scalar polynomial is monic with p_q(1)=1−q. If all roots have modulus at most R<1, the reverse triangle inequalities give 1−q≥(1−R)³, and equality requires all three roots at t=1−(1−q)^{1/3}; coefficient matching gives the unique real parameters. Independently, with k=s/q and z=tu, the normalized polynomial equals (1−k)u³+k(u−1)³. For 0<k<1 put α=((1−k)/k)^{1/3}; its roots are 1/(1+αζ), with ζ ranging over the cube roots of unity. The conjugate pair governs the radius, with squared normalized modulus 1/(1−α+α²), uniquely maximized at α=1/2, k=8/9. The endpoint modes give normalized radii zero and one. The resulting envelope gives the stated strict cutoff for the entire finite-dimensional self-adjoint class, not for each spectrum individually; at or above it the maximizing mode obstructs convergence for suitable data. The cited Algorithm (17) reduces to the proximal step with B=C=0 and ρ=1. With η=2 and γ=1, β=4/7; the rational brackets give 0<θ<0.238<3/11 and −0.018<δ<−0.017. The two strict lower bounds on δ in Condition 3.2(iii) are below −0.018, and its remaining comparison has left side below −0.07 and right side above −0.036−0.018²/7. The required relaxation bound is 1<7/4. This verifies the strict sufficient regime for the example, whose modes 1/2 and 4/9 realize the two rates. Frozen support was inspected, not executed. The rate here is a companion spectral radius, not a pure exponential bound at the defective triple root.

## originality

PASS

Credit the exact frozen-parameter interior-mode penalty, its unique worst mode, and the resulting sharp stability boundary and admissible witness. Do not credit either the recurrence or the scalar monic-polynomial extremum as new: the former is already in the inertial proximal literature, and the latter follows directly from Arjevani–Shalev-Shwartz–Shamir, Lemma 6. The inspected prior work does not give the claimed envelope for this scalar-optimal proximal tuning.

## value

PASS

The result resolves a motivated failure mode in tuning two-step inertia for a quadratic: a mode strictly faster before acceleration becomes the slowest after using parameters optimal for the largest proximal eigenvalue. The exact universal worst mode and factor yield a sharp class-wide stability test and a counterexample inside the published sufficient convergence regime, beyond the prior scalar extremum or qualitative observation that spectral tuning can be sensitive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
