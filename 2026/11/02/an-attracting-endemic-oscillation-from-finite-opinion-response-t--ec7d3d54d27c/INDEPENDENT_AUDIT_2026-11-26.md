# Independent mathematical audit

## correctness

PASS

For L=log(3) and a=3/16 the given point balances the prevalence equation and has opinion argument -L/2 with tanh=-1/2. The Jacobian has rows (-a,a) and (-9/(32*tau),H/tau); 0<H<9/32 is certified by the rational L enclosure. Its determinant is a(9/32-H)/tau>0 for every tau>0. The trace vanishes at tau_H=H/a, decreases through zero, and gives the displayed stability sides and omega^2. Independently expanded the prevalence jet -aU+aV-(3/8)U^2-(3/4)U^2 V in centered coordinates and the opinion-argument increment h=-3U/8+(L+3/8)V+(3/4)UV-(9/8)V^2+(3/4)V^3. Using the tanh addition law gives -1/2+3h/4+3h^2/8-h^3/16 through cubic order. Substitute U=X, V=X-omega Y/a, transform the second component by a(F-G)/omega, and extract derivatives as i!j! times the coefficients of X^iY^j. Reducing the Lyapunov expression algebraically by omega^2=9(4-3L)/(32(24L-23)) reproduces the frozen rational function exactly. The log atanh series with a geometric tail yields 1.0986<L<1.0987, where the frozen centered quartic bound is >1700 and the denominator is negative; ell_1 is strictly negative. The planar Hopf theorem applies with real-part derivative -H/(2*tau_H^2), giving an attracting local cycle for every sufficiently close tau below tau_H, with frequency limit in physical time and the stated interior by proximity to (1/2,-1/2).

## originality

PASS

The supported distinct finding is an exact nondegenerate supercritical Hopf in the original homogeneous two-state NOD-SIS equations, not the introduction of endemic oscillations or behavioral Hopf bifurcations generally.

## value

PASS

The calculation answers a concrete dynamical question left open for the source model: two homogeneous unforced state variables suffice for an attracting endemic oscillation, with both criticality and parameter side certified analytically. Finding a pair of imaginary eigenvalues alone would not give that conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
