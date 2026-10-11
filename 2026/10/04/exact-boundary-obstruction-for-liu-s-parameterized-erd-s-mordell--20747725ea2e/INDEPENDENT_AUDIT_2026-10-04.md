# Independent mathematical audit

## correctness

PASS

Writing s=sum r_i, T=sum R_i, D=sum r_i R_i-2 sum r_i r_j and E=s(T-2s), direct expansion of Liu's middle term gives the exact identities ((k+2)s/2)(M_k-2s)=E+(k-1)D and (k+2)s(T-M_k)=kE+2(1-k)D. Away from the equilateral center D>0, so with alpha=E/D the two sides reduce exactly to k>=1-alpha and, when alpha<2, k<=2/(2-alpha). For the normalized isosceles side-midpoint boundary family, half-angle parameter u gives alpha(u)=-(u⁴-12u³+4u-1)/(4u³), whose derivative is -(u⁴-8u+3)/(4u⁴). The relevant quartic has a unique minimizer u*=0.377539568391..., yielding alpha*=0.535565054837... and therefore the necessary window 0.464434945162939...<=k<=1.365714473426112.... Continuity transfers strict boundary failure outside this window to genuine interior points. Independent exact/symbolic checks reproduced the derivative and high-precision endpoints.

## originality

PASS

Liu's complete open primary article states Conjecture 6.3 exactly on 0.48<=k<=1.36 but does not reduce it to a one-dimensional defect ratio or derive the optimal isosceles boundary obstruction. A later open weighted Erdős-Mordell paper by Tran was read in full enough to compare its main weighted families; they are different coefficient systems and do not state this defect-ratio reduction. Resultary returns the assigned theorem as the exact hit and no prior source with the algebraic endpoints. Plausible later papers listed in the package metadata that were not fully accessible are retained as residual priority risks rather than treated as non-covering evidence.

## value

PASS

The theorem isolates an exact scalar invariant alpha=E/D governing both halves of a published parameter conjecture and computes a sharp algebraic obstruction from a canonical boundary family. Although it does not prove the conjectured interval, it gives a mathematically interpretable outer parameter envelope and a reusable reduction for any future sufficiency analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
