# Independent mathematical audit

## correctness

PASS

Conditional on the renewal age A, the OU mean is zero and the variance is (D/κ)(1−exp(−aA)), a=2κ. Write H(s)=∑_{k=0}^{m−1}r^k/(s+a+r)^{k+1} for the shifted survival transform. Summing over the last renewal gives the independently reconstructed age transform H(s)/[1−(r/(s+r))^m], initially for Re s>0. Its residue at zero is (r/m)H(0). The nonreal leading roots are s=r(z−1), z=exp(2πi/m) and its conjugate. The first root's residue is (rz/m)H(s); cancellation would require (a+rz)^m=r^m. For m≥4, |a+rz|>r. For m=3, equality of moduli is possible only at a=r, but then (a+rz)^3=−r^3. For m≥4 the pair has real part at least −r and strictly beats −(a+r); for m=3 it beats that real exponent exactly at r<2a. At r≥2a the cubic-pole coefficient in the age transform is r²a³/(a³+r³), so the negative variance deviation is led by (D/κ) times its negative inverse-Laplace contribution, including equality where the t² factor dominates the sinusoid. The nonzero leading sinusoid in the complementary phase gives opposite signs along successive extrema. Shapes 1 and 2 have only real poles, even if they coincide; the last nonzero exponential-polynomial mode fixes the eventual sign. Exponential-polynomial analyticity and V(0)<V∞ exclude accumulating zeros at finite times in every eventually one-sided case. These checks prove the dichotomy and constants without relying on the bundled finite tests.

## originality

PASS

The distinct result supported by the comparison is the full harmonic Erlang crossing classification and leading asymptotics, not the general renewal transform or the Poisson harmonic model. The closest explicit catalogue crossing result uses a different motion/rest process and has a different boundary; primary antecedents do not determine this classification without the mode and noncancellation analysis.

## value

PASS

The integer clock shape controls whether a natural transient observable crosses its own equilibrium infinitely often, despite monotone variance growth within each excursion. The exact threshold, exceptional equality case, and oscillation frequency and damping distinguish relaxation mechanisms that the equilibrium moment alone cannot diagnose.

The dated certificate retains the supplied scientific assessment, sources and limitations.
