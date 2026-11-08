# Independent mathematical audit

## correctness

PASS

For fixed n>=2 Vandermonde^theta density on [0,1]^n, theta>=0, and q>0, each Lagrange absolute product |ell_i(t)| <= prod_{j!=i}|X_i-X_j|^-1. Raising to q, discarding bounded non-i Vandermonde factors, and integrating each |u-v|^(theta-q) shows E Lambda^q<infty if theta-q>-1. Conversely choose two labeled nodes with gap d tending to zero inside a fixed compact interval away from t0 while every other node lies in separated compact subintervals; the integrand lower bounds c d^(theta-q), so E Lambda^q diverges when q>=theta+1, including equality. For n=2, gap d has weight 2d^theta(1-d)/Z and midpoint is conditionally uniform; Lambda=2 max(u,1-u)/d. Exact split integration at d=1/t and 2/(t+1) gives P(Lambda>t)=2(2/(1+t))^(theta+1)-t^-(theta+1), t>=1, with mean 1+3/theta (theta>0) and second moment (theta^2+5theta+8)/[theta(theta-1)] (theta>1). Noiseless interpolant of C^{n-1} f remains uniformly bounded via Newton divided differences. Conditional Gaussian noise has q-moment constant times (sum ell_i(t0)^2)^(q/2), so same threshold by upper Lambda and lower collision bound; adding bounded deterministic offset cannot alter integrability. Independently integrated exact two-node tail for theta=0,1,2,3 and moments for theta=2,3,4. The infinite fixed-n statement rests on integrability bounds, not simulation.

## originality

PASS

Belhadji–Bardenet–Chainais (2020) analyze kernel continuous volume sampling and explicitly identify studying Lebesgue constants for stability as a future direction in their conclusion, without solving the current all-n random polynomial operator-norm moment spectrum. Their 2023/24 DPP signal reconstruction work concerns average L2 reconstruction and estimators not identical to full-degree noisy Lagrange interpolation, nor exact two-node distribution. Chkifa–Dolbeault address a different randomized oversampling and interpolation design. Deterministic Leja growth results are different. The assessed sharp finite-n repulsion collision threshold and pointwise Gaussian noise moment boundary are new to the inspected literature, with the clear risk that separate inverse-Vandermonde moment theory already contains equivalent statements.

## value

PASS

Random interpolation stability and noise amplification are natural operator-norm/pointwise moment questions; collision exponent theta makes a sharp universal cutoff q<theta+1 independent of fixed n. The threshold separates infinite-mean amplification for iid nodes (theta=0) from finite quadratic amplification for polynomial projection DPPs (theta=2), and the explicit two-node tail gives an exact baseline for random-node designs. The claim addresses a literature-identified gap and is more informative than finite Monte Carlo statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
