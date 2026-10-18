# Independent mathematical audit

## correctness

PASS

For fixed h,c>0 and variable b, f_b(x,y)=1/2(h-b^2/c)x^2+bxy-1/2 c y^2 has follower Hessian -c and leader Schur complement h>0, so unique strict minimax (0,0). Substitution of the exact source FR correction and ridge error e=y-(b/c)x gives e^+=q e and x^+=p x-eta_x b e, p=1-eta_x h, q=1-eta_y c. Explicit upper-triangular matrix powers yield divided difference (p^t-q^t)/(p-q), or Jordan t r^(t-1) when p=q=r. Fixed |p|,|q|<1 gives asymptotic convergence for each b. At matched steps and z0=(0,1), x1=-(1-r)b/h, y1=r-(1-r)b^2/(hc), so squared Euclidean gain grows like (1-r)^2 b^4/(h^2 c^2) while both eigenvalues fixed r. The original paper example -3x^2+4xy-y^2 has h=c=2, b=4 and is resonant for equal steps. Independent matrix-column computations checked exact gain and repeated eigenvalue across b=1,4,13,40,100. Linear scaling makes transient equally possible arbitrarily close to minimax.

## originality

PASS

PASS best of knowledge for explicit nonnormal transient unboundedness at a fixed FR spectrum and identifying resonance of the original paper example; the source itself already proves the general triangular Jacobian and real eigenvalues. New conclusion is an explicit quantitative family, not a claim to the triangular identity.

## value

PASS

The explicit counterexample addresses a specific interpretive gap in a standard minimax optimizer: strictly real locally stable eigenvalues do not protect Euclidean optimization iterates against arbitrarily large finite transients. It is not just the generic Jordan phenomenon because the parameter family preserves follower curvature, Schur complement, learning rates, strict local minimax, and spectrum while varying only game coupling; the defining paper’s own toy model is resonant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
