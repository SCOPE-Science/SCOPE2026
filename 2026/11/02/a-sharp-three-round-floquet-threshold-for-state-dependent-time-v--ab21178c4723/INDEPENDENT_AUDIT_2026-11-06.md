# Independent mathematical audit

## correctness

PASS

For the explicitly stated APG2 scalar update, beta=1/(1+|x-z|) and inactive projection near zero give derivative M_t=[[0,t],[-1,2t]] for t=1-a. At 3-round cadence T_s=M_s M_(4/5)^2, trace (48s-32)/25, det 16s/25. Exact Schur inequalities are (25-16s)/25>0, (57-32s)/25>0 and (64s-7)/25>0. The last gives s>7/64; at s=7/64 eigenvalues -1,-7/100. For 0<s<7/64, hyperbolic saddle; det[(1,1),T_s(1,1)]=(4s-12)/25 nonzero gives legal-initialization transversality to local stable manifold, hence neighborhood exit. PG 3-round product 16s/25 contracts. Independent SymPy matrix products/eigenvalues at s=1/10,7/64,1/2 confirmed these identities. Stability at equality beyond absence of exponential attraction intentionally not classified.

## originality

PASS

Classical Jury/Schur/Floquet criteria are acknowledged. The source time-varying APG2 paper states tracking objective-gap bounds under bounded variation, not a common-minimizer exact three-round instability threshold in accessible text; specific comparison with full algorithm source remains limited by full-text access.

## value

PASS

A strongly convex common-minimizer periodic schedule that destabilizes acceleration but not basic PG exposes a mechanism-specific robustness limit, with exact threshold and initialized dynamics; not a broad claim about all acceleration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
