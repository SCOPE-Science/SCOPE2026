# Independent mathematical audit

## correctness

PASS

For N>=7, t>0 and rho>=0 the DFT of K=e^{t cos(theta)+rho t cos(2theta)} equals N e^{(1+rho)t} times the continuous-time cyclic random walk mass with jumps ±1,±2, ensuring positive eigenvalues. Symmetric radial decreasing arc functions form a convolution cone; Euler approximation proves weak spectral ordering for rho<=1. For rho<1, factor off a positive-time strictly decreasing nearest-neighbor heat kernel to prove strict inequalities. For rho>1, the one-jump expansions p_t(2)-p_t(1)=(rho-1)t/2+O(t²)>0. For large t, strict convexity of x+rho(2x²−1) on frequencies x in [-d_N,c_N] makes k=1 or antipodal endpoint dominant; equality is handled by the combined leading coefficient, yielding sharp rho*=1/[2(d_N-c_N)], parity asymptotics N²/(4π²) even and N²/(3π²) odd. Independently recomputed exact arc-convolution differences for small cycles and sample high-precision spectral/endpoint signs at N=7,8,9,10,13,17,29. These checks support but do not replace the analytic proof.

## originality

PASS

Generalized von Mises spatial bimodality and ordinary nearest-neighbor cyclic heat kernels are established, but neither identifies the two sharp thresholds for the sampled two-harmonic Fourier eigenvalue sequence. Spatial density modality starts changing already at rho>1/4, unlike the Fourier eigenvalue ordering threshold rho=1. Comparing asymptotic Fourier exponents adds a second parity-dependent threshold beyond classical unimodal-convolution closure.

## value

PASS

Complete all-time and eventual sharp order regions, including a nontrivial mode-order healing window 1<rho<rho*(N), describe natural spectra of a common positive definite sampled circular kernel. They distinguish two concepts often conflated: spatial bimodality and Fourier-mode ordering, and give exact parity-sensitive parameter boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
