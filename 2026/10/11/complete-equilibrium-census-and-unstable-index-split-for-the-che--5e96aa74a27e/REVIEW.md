# Independent mathematical audit

## correctness

PASS

For the exact displayed 4D polynomial ODE, q=0 forces p=s=r=0. With q≠0 the first two equations force r²=50 and p=qr/5. Then s=-52p/21 and the third equation is exactly 35q²−52q−1995=0; its two real nonzero roots times two signs of r yield exactly four nonzero equilibria. The origin Jacobian is diag(5,-10,-19/5,21/20), unstable index 2. Independent SymPy reconstruction of the full Jacobian characteristic polynomial at both r-signs, reduced modulo the equilibrium quadratic, gives the asserted quartic. Independently recomputed Routh B and C agree after exact algebraic reduction; using -7<q_±<9 yields signs +,+,-,+,-, so each nonzero equilibrium has three strict right-half-plane eigenvalues. The Routh array is nondegenerate, hence hyperbolic; no finite enumeration is used for completeness.

## originality

PASS

Best-of-knowledge PASS for the exact five-point fixed-point census and local unstable-index split at the cited parameter vector. The full 2023 benchmark paper prints the same ODE and parameters, but computes only the origin spectrum; no four further equilibria or index-three classification is present. A different 2009 paper with a Chen-hyperchaotic title has materially different equations; the closest Resultary five-equilibrium article also concerns another ODE. The 2009 original article full text could not be read; this is an expressly retained priority risk, not proof of novelty.

## value

PASS

The five-point equilibrium skeleton is a natural invariant of an actively studied four-dimensional hyperchaotic Chen–Lee benchmark, and its exact classification fills a concrete gap left by a same-ODE source that studies only the origin. The four omitted hyperbolic fixed points have unstable dimension three, versus two at the origin, a qualitative distinction relevant to local stable/unstable manifold dimensions and interpretations of basins and self-excitation. This is a motivated exact finite classification of a real benchmark system, not a parameter-renaming exercise or finite numerical sample. It does not claim a general-parameter theorem or invalidate synchronization by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
