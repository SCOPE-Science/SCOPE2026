# Independent mathematical audit

## correctness

PASS

Read Cui et al. original primary full PDF equation (3.2): all four diagonal entries are z=λ+a e^(−λθ). Exact determinant expansion of the printed 4×4 matrix gives F(z)=z⁴+3z²−z+1, and expansion in delayed powers matches paper (3.3). For a=1/4, F(λ+1/4)=λ⁴+λ³+(27/8)λ²+(9/16)λ+241/256 has positive Hurwitz determinants 1,45/16,41/64 and 241·41/(256·64). The four simple roots of F have real parts ±r where r² is the unique positive zero of 64q³+96q²+20q−1, with r≈0.20372326785<1/4. Write their positive imaginary parts y1≈0.560667728 and y2≈1.663928496, s=√(1/16−r²)≈0.14490283, α=acos(4r)≈0.61825. Exhaustive phase equations produce frequencies y1+s,y2+s,y2−s,y1−s and their least nonnegative delay representatives 0.87624353,1.39501178,2.47516838,13.62532935 respectively. No later branch wraps give an earlier delay. Implicit differentiation yields Re λ′=ω*s/[(1−rθ)²+(sθ)²]≈0.1479657>0 at first crossing. Spectral continuity and the fixed disks |λ−z_j|≤1/4 in Re λ≥0 prevent unstable roots from arriving at infinity. Max crossing frequency 1.8088313<2.0083. The computations support the exact finite-branch algebra, not nonlinear Hopf claims.

## originality

PASS

Original primary Cui et al. article prints a different crossing frequency φ0=2.0083 and θ0≈0.8, and does not display the scalar-shift factorization or corrected exhaustive frequency set. Nearest four-neuron predecessor uses unequal delayed diagonals; published Resultary matches concern different equations.

## value

PASS

The exact scalar shift splits a four-dimensional characteristic equation into four simple scalar delay branches, supplies all crossing frequencies and replaces an impossible published numerical Hopf benchmark with an exact linear stability margin. Structural diagnosis and a meaningful correction are independently useful, not mere decimal adjustment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
