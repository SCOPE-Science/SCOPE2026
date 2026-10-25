# Independent mathematical audit

## correctness

PASS

Uniform barycentric Y~Dirichlet(1,...,1), at a vertex T=Y1~Beta(1,n-1). Reproducing endpoint moments yield kernel n(n+1)/4*[(n+2)(n+3)T²-4(n+2)T+2] and sign-change roots r±; exact norm follows integrating its negative interval. Independently evaluated n=3 norm 1+128sqrt(10)/135=3.9983077 and verified vertex moment matrix. Permutation averaging at centroid reduces degree-two symmetric polynomials to span{1,S=sum Yi²}; E S=2/(n+1), Var S=4(n-1)/[(n+1)²(n+2)(n+3)] give K_c=1-[(n+1)(n+2)(n+3)/(4n)](S-2/(n+1)), reproducing all quadratics. nY1→Exp(1), uniformly integrable vertex rescaled kernels -> gamma. Expressing Y_i=E_i/sum E_j and bivariate CLT for sample means E,E² gives sqrt(n)(nS-2)⇒N(0,4), K_c/sqrt(n)⇒N(0,1/4). Reproducing E[K_c²]=K_c(c)=O(n) yields UI and limit E|N(0,1/4)|=1/sqrt(2pi). Projection of indicator of negative kernel gives exact undershoot. Source check.py claims standard library but imports sympy; reproducibility caveat, not mathematical refutation.

## originality

PASS

Classical Jacobi/simplex polynomial machinery contains endpoint kernels; Melenk–Wurzer and Chernov treat trace stability for fixed low-dimensional simplices with polynomial degree increasing, not fixed degree two as dimension grows. Related published affine degree-one positivity-defect formula does not imply quadratic degree-two norm. Joint vertex n² versus centroid sqrt(n) asymptotics and sharp pointwise loss are not located as a prior exact theorem.

## value

PASS

A natural and previously unquantified stability/positivity contrast at geometrically canonical points under fixed polynomial degree and growing dimension, with explicit constants and exact Dirichlet-kernel proof, useful for interpreting multidimensional polynomial projection instability without claiming a global maximum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
