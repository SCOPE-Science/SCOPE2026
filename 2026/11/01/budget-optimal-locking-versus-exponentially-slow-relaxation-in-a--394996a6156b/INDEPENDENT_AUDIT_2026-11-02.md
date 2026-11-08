# Independent mathematical audit

## correctness

PASS

Direct subtraction of phase equations enforces sin(u)=sin(v); the complementary v=pi-u branch has weighted Laplacian trace -2b<0, forbidding attraction (including branch crossings). Symmetric branch phases (-phi,0,phi) obey omega=a[sin phi+q sin(2phi)], q=2^p, a=3K/[2(q+2)]. Positive nonneutral decay rates are 3a cos phi and a(cos phi+2q cos 2phi). Strict h_q concavity on (0,pi/2), explicit fold cos phi*=(sqrt(1+32q^2)-1)/(8q), and positive-derivative side prove exactly one stable lock iff K> Klock=2omega(q+2)/[3 sin phi*(1+2q cos phi*)]. Its envelope derivative sin(phi*)(4cos(phi*)-1)/(q+2)^2 is positive q>=1, hence strictly decreasing Klock. Expansion gives Klock=(2omega/3)[1+(2-1/sqrt(2))/q+O(q^-2)]. For fixed K>2omega/3 the vanishing slow eigenvalue is 9K cos(phi_infty)/(2q)+O(q^-2), other rate tends positive; gap vanishes also at the lower onset fold for budgets within the crossover window, yielding an interior positive maximum. Independently checked numeric q=1 Klock/omega=1.1362522107, q=2 0.9747247402 and high-q approach. The inspected verify.py explicitly tests eigenvectors and 400 stationary spectra; finite sampling not used for uniqueness proof.

## originality

PASS

Pando et al. arXiv:2603.29648v2 use the exact same proportional detuning power allocation under a budget but study large random-frequency ensembles and approximate strong-lock behavior; inspected primary full HTML does not establish the exact three-frequency fold or two-mode spectral relaxation tradeoff. Zhao–Zhou concern isosceles triangles without detuning; Xin–Kikkawa–Liu use uniform coupling. Best-of-knowledge the exact N=3 power-law design result is not implied.

## value

PASS

The same fixed coupling budget creates opposing objectives even at the smallest heterogeneous oscillator motif: exact sharp onset improves monotonically while spectral convergence becomes exponentially slow, forcing a finite rate-optimal allocation exponent for every budget in a natural crossover interval. Precise rates and normalization could guide motif-scale design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
