# Independent mathematical audit

## correctness

PASS

For N(x)=max(alpha^-1|x1|,Euclidean(x)), skew parallelogram decomposition gives S_lambda(tau)^2 >= (1+tau^2)(1+alpha^2)/2. Since 1+alpha^2<2, equality must use one flat-side center (alpha,0) and one circular-arc (a,b) with |a|<=alpha^2. Equality of both output branches imposes tau(sqrt(1-a^2)+(beta/alpha)a)>=beta. Strict concavity gives maximum at a*=min(beta,alpha^2); its value yields sharp onset tau_c=sqrt(1+alpha^2)-alpha when alpha^2<=(sqrt5-1)/2 and alpha beta otherwise. For tau_c<=tau<=beta, a continuous cone-boundary witness exists and second cone inequality follows from (b-kappa a)(b+kappa a)=1-a^2/alpha^2>=beta^2; for tau>=beta choose x=(0,1),y=(alpha,0). Compactness makes every tau<tau_c strict. Independent algebra checked switch continuity and both optimizer branches at alpha=.2,.65,.9, and the exact rational threshold witness in the frozen verifier.

## originality

PASS

Best-of-knowledge PASS for exact minimum saturation onset, not for previously known sufficient range tau>=beta. Xu--Liu introduce this infimal skew constant and display equality above beta for a fixed witness; the new cone contact optimization yields strictly smaller tau_c and a golden-ratio branch switch. Chen et al study a supremal skew generalized Jordan quotient and cannot directly imply this infimal equality onset. The highly relevant Xu--Liu full primary Example 3.5 could not be accessed despite OA avenues and authorized institutional retrieval returning VPN disconnected; no whole-text exclusion is asserted and this is a substantial named priority risk, not itself grounds for false FAIL.

## value

PASS

The exact phase boundary for equality in a natural published lower-envelope inequality is a mathematically motivated invariant, not a parameter-picked toy example. It sharpens the source sufficient threshold for every lambda>1, classifies the geometry of equality witnesses and exhibits a real golden-ratio optimizer transition. Determining full subthreshold constant is outside scope; exact onset itself is useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
