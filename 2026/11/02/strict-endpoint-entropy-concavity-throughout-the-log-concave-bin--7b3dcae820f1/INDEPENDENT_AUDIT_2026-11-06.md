# Independent mathematical audit

## correctness

PASS

X_alpha log density has Hessian -1/(1-alpha)+alpha sech^2(sqrt(alpha)x/(1-alpha))/(1-alpha)^2, log-concave exactly alpha<=1/2. U_alpha is unit variance symmetric Gaussian location mixture with score rho=-2u/S+c tanh(cu), S=2-alpha, c=sqrt(2alpha)/S. Integration by parts gives B=E rho'''=c^4 e^{-v/2}(4 E sech Z -6 E sech^3 Z), v=alpha/S<=1/3. Under positive sech tilt, E_w Z^2 < v and sech^2 z>=1-z^2 strictly off zero, so E sech^3/E sech>1-v>=2/3 and B<0 throughout range. Fourth cumulant kappa4(U)=-alpha^2/2; applying known smooth endpoint identity F''=-A/2-kappa4 B/12, A=E(1+rho')^2>=0, proves F''(0+)=F''(1-)<0. Dominated small-alpha scaling A/alpha^4->1/8, B/alpha^2->-1/2 gives -1/12 coefficient. Independently evaluated selected Gaussian-Hermite quadrature integrals/signs; finite numerics do not substitute for analytic proof. The endpoint identity is cited prior work, not re-proved from paper here due full-text access limits.

## originality

PASS

The general endpoint-curvature identity belongs to Abu-Ajamieh (2026), rather than this finding. Its technically relevant full text was not accessible; lawful OA/preprint routes failed and Oxford VPN disconnected, so potential already-proved Gaussian-location example remains a substantive originality risk. Eskenazis–Gavalakis scale mixtures have nonnegative fourth cumulant and cannot include this negative-cumulant displaced-mean mixture; Luo's asymmetric log-concave counterexample does not cover the even family. A bounded search does not certify priority.

## value

PASS

Determines sign and sharp fourth-order onset of entropy endpoint curvature for the complete natural log-concave range of a two-location Gaussian family, a concrete unresolved parameter class in a broad entropy-concavity question; not merely a Gaussian perturbation calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
