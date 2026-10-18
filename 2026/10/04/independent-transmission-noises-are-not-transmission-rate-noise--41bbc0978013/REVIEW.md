# Independent mathematical audit

## correctness

PASS

For q=(1-alpha)sigma_beta SI, a scalar noisy beta enters both S,I with vector q(-1,1). Its covariance q^2[[1,-1],[-1,1]] differs from the paper's independent two-coordinate covariance q^2 I. The generator therefore differs by -partial_SI(q^2 f), and S+I receives quadratic-variation coefficient 0 vs 2q^2. Full source equations inspected; independent exact-fraction replay at S=1/2,I=1/4,alpha=0 gives q^2=1/3200. Restricted to q!=0; does not infer corrected numerical control trajectories.

## originality

PASS

Best-of-knowledge original source-specific covariance and Fokker--Planck interpretation correction; general Itô covariance identities and common-driver SIR modeling are acknowledged prior ingredients.

## value

PASS

A mismatch of the very diffusion tensor used in a stochastic epidemic forward-control PDE changes its rank, mixed derivative and total-transfer stochastic conservation; it materially changes interpretation and potential recomputation, beyond cosmetic signs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
