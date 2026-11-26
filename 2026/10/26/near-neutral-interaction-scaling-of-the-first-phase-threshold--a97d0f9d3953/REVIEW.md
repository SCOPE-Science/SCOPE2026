# Independent mathematical audit

## correctness

PASS

Reconstructed the first-root threshold. For z≥1/a the expression is positive, so all z>1 roots come from solving z^β=((1+a)z−2a)/(1−az) on 1<z<1/a. This gives a continuous exponent with endpoint value (1+2a)/(1−a) at z=1 and divergence at z=1/a. With δ=1−a and z=1+δs, the scaled exponent is Gδ(s) as claimed; its right derivative at s=0 is −a(1+2a)/2, so its minimum is interior. Along δ→0, Gδ(s)→3 when s→0 by the uniform first-order logarithm expansions, and Gδ(s)→∞ when s→1 within the varying domain, using δ/log(1+δs)≥1/s. The trial value at s=2/5 tends to (5/2)log 3<3, so minimizing sequences stay in a common interior compact set, where convergence is uniform. For f(s)=log((1+2s)/(1−s)), the derivative of sf′−f is sf″, with sign changing from negative to positive at 1/4; sf′−f starts at zero and tends to +∞. Thus the unique interior zero yields the unique minimizer. Independent bisection gives s≈0.37720062726944 and f′(s)≈2.745643576732724. Frozen verify.py was inspected, not run; its bisection only checks the decimal, while the argument above checks the limit. The onset is for stationary roots, not a dynamical or trajectory threshold.

## originality

PASS

Credit the limiting variational problem and constant to the known three-state mean-field Potts spinodal under rescaling. The supported distinct claim is convergence of the finite-interaction Costa–Jordan urn threshold to that constant, not a new spinodal or a new phase diagram. The inspected sources and catalogue comparisons do not state or already supply that convergence.

## value

PASS

The sharp coefficient quantifies the divergence of the first nontrivial stationary branch where published urn bounds leave a finite leading-order gap. The identification with the Potts spinodal gives a meaningful comparison between stationary thresholds of the two models; merely recomputing the Potts constant would not supply this value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
