# Independent mathematical audit

## correctness

PASS

The circulant eigenspaces are Fourier characters. The actual RESULT.md expresses each eigenvalue as an infinite positive Gaussian theta periodization P minus the omitted symmetric Gaussian tail E. Poisson summation gives P>=sqrt(pi n/c) exp(-pi^2 n/(4c)); E=O(exp(-cn/4)) for all frequencies, proving positivity when c>pi. For c<pi choose the largest even index <=floor(n/2): exact even tail has positive scaled limit tanh(c/2), while the paired odd tail has positive first scaled derivative pi*delta exp(-c/2)(1-exp(-c))/(1+exp(-c))^2, delta=1 or 3. Exponential-rate comparison suppresses P and yields negative eigenvalue and sharp asymptotics. Positivity of a Schur multiplier is equivalent to positive semidefiniteness of its symbol (apply to the all-ones rank-one matrix); proof addresses all n sufficiently large separately for both parities. Independent mpmath Fourier/periodization calculations checked signed modes and both leading constants, not the all-n theorem.

## originality

PASS

Sharp finite-sample moving-parameter threshold c=pi and parity-resolved negative eigenvalue constants are not the fixed physical-scale continuous-circle nonpositive-definiteness shown by Da Costa et al., nor the sufficient positive-embedding results for periodized stationary kernels. Classical Fourier/Poisson identities are acknowledged. Priority remains best-of-knowledge because Wood 1995 and potential aliasing/circulant covariance literature might contain equivalent asymptotics.

## value

PASS

The positive-definiteness of a geodesic Gaussian Gram matrix is exactly the admissibility of a kernel/covariance and complete positivity of the associated Schur map; the sharp n-dependent bandwidth boundary and parity magnitudes answer a natural nontrivial finite-sampling question. This is not a routine restatement of continuous-circle nonpositivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
