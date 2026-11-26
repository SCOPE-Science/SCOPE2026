# Independent mathematical audit

## correctness

PASS

The 2N+1 nodal values are free real coordinates by discrete Fourier inversion. The mass is the grid weight times their sum, and integrating against x gives the same weight times the nodal dot product with q_{N,j}, using ∫x sin(kx)dx=2π(−1)^{k+1}/k. At positive mass the normalized feasible set is the convex hull of the antisymmetric q_{N,j}; strictly positive weights exclude its endpoints and realize any interior mean by mixing uniform and extremal-node weights. The hull is nondegenerate since the sampled degree-N sine polynomial with these coefficients is not identically zero. Physical positive-mass means are strictly between −π and π, and smooth periodic bumps supported near one endpoint approach that endpoint’s mean. Thus the universal condition is B_N≥π; below it even nonnegative nodes can fail. Independently verified all 1,953 pairs of signed finite inequalities for 1≤N≤62 with rational interval arithmetic (smallest gap 0.0002667123586728 at (62,61)); replay `python /workspace/reproductions/1.py`. The new check uses the atan(1/2)+atan(1/3) identity and Taylor plus Lipschitz bounds, and does not execute the frozen script. For j=N−1 the step h=(3π/2)/(N+1/2) turns the nodal sum into twice a midpoint sum for sinc; the uncovered half-interval costs at most h and the full-interval error at most N*h³/36 because |sinc''|≤1/3. The independent exact check gives positive margin 0.0002211068588182 for the N=63 inequality, and the bound only decreases thereafter. The large-N maximum is also checked: fixed r=N−j gives the sinc integral at (2r+1)π/2 by Riemann sums, with r=0,2 strictly between 0 and π; twice integrating the sine-integral tail by parts bounds the absolute deviation from π by 4/t² for each fixed r≥3. The Abel tail bound works for the absolute value as needed: the infinite sawtooth value π−δ is nonnegative for δ=(2r+1)π/(2N+1) in (0,π], and the absolute truncation error is bounded by 2/((N+1)sin(δ/2))<4/(2r+1). Hence r≥30 are uniformly below the r=1 limiting value even in absolute value. The finitely many remaining fixed indices admit the stated comparisons, and r=1 attains the limit. All infinite claims use these analytic estimates, not enumeration.

## originality

PASS

The matching nodal Fourier method and its strict feasibility hypothesis are prior work, as are the sawtooth series and Gibbs mechanism. The exact universal raw-(1,x) cutoff on the matching 2N+1 grid and the complete moment-cone feasibility classification are distinct on the material checked. The precise sampled asymptotic is evaluated here, but the priority of that sampled value in all Gibbs literature is not claimed.

## value

PASS

The exact degree resolves a concrete strict-feasibility hypothesis in a published nodal projection framework for the natural mass/raw-first-moment pair. It separates resolutions at which positive-mass smooth data can be infeasible from those at which strict feasibility is guaranteed for every admissible input. The cone endpoints give a per-datum diagnostic, while the asymptotic explains why increasing resolution eventually works but is not itself the cutoff proof. This is a benchmark for the specified grid and moments, not a runtime theorem or a guarantee of between-node positivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
