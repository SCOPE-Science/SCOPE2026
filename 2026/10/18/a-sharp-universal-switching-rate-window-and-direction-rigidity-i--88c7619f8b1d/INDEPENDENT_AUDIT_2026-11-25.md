# Independent mathematical audit

## correctness

PASS

Eliminate the OFF masses with (s+3)q=(1/2)1+sp. The remaining equation is stationarity of an effective three-state chain with rates r_ij=w_j/w_i+t, where h=3s/(s+3), t=h/3, and the ON probability mass is 1/2. Its effective bond current equals the physical current including the OFF contribution. Independently, the triangle tree formula gives the cycle-product difference t(1-t)V/e_3 divided by twice the sum of the rooted tree weights, with V the stated oriented Vandermonde. On the zero-sum subspace, adding the uniform rates shifts the two negative generator eigenvalues by -h; the tree weight sum is h^2+h(e_1e_2/e_3-3)+e_1 U/e_3, from the trace and the pair principal minors, with U=sum w_i^2. Substitution gives the claimed A,B,C, sign and normalization. The exact symbolic stationary check independently agreed, including J=1/658 for (w_0,w_1,w_2,s)=(1,2,3,1). Positivity follows from the coefficient expansions, and differentiation reduces the magnitude maximizer to C-As^2=0. Since 0<e_2<U for distinct positive weights, the window is strict; near-equal weights and a dominant weight approach the respective endpoints. Any repeated weight gives zero current. Conservation makes bond currents equal; three oriented bonds contribute to the displacement rate, so the velocity is 3J. The frozen Python checker was read, not executed.

## originality

PASS

The model, generic stationary solution methods, reversal-degree bounds, and some restricted-family transport behavior are known. The distinct supported claim is the arbitrary positive weight-ratio/unit-OFF specialization with its factored current, absence of direction reversal and sharp exact rate window, not a new generic triangle rational form.

## value

PASS

The exact factorization separates the direction from the time-scale dependence in a standard microscopic ratchet. It supplies a sharp range valid for every detailed-balance weight profile in the stipulated normalization and a computable attainable maximum for any such profile. This gives quantitative information beyond a generic upper bound on reversal count, without extrapolating to general ratchet dynamics or entropy-production optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
