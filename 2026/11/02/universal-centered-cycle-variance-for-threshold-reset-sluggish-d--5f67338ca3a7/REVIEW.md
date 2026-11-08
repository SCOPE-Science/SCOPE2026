# Independent mathematical audit

## correctness

PASS

The natural-scale diffusion is defined by Brownian generator d^2/dx^2 with physical clock integral |B_s|^alpha ds, alpha>=0, avoiding ambiguity at x=0. For a cycle from s=rho in (-1,1), the stopped Brownian Green kernel G(s,y) and weight |y|^alpha give E tau=(1-s^{alpha+2})/[(alpha+1)(alpha+2)] and theta=1-(1-s)/[2(1-s^{alpha+2})]. For centered reward A=int_0^tau(1_{X>0}-theta)dt, solve Dirichlet u''= -|x|^alpha(1_{x>0}-theta), u(s)=0. Ito stochastic integral and Green energy give E A^2=2int G(s,y)|u'(y)|^2 dy=3(1-s^2)/[4(alpha+2)^2(alpha+3)(2alpha+3)] for L=1. Brownian exit time controls all needed moments, so iid-cycle regenerative renewal-reward CLT yields V=E A^2/E tau. Brownian scaling multiplies CLT coefficient by L^{alpha+2} and cycle second moment by L^{2alpha+4}. For alpha=0 V=L^2/24 independent of rho; alpha>0 strict decrease follows monotonicity of (1-rho^2)/(1-rho^{alpha+2}) via positive conditional-integral average; endpoint values are one-sided limits. Independent quadrature for alpha 0,1,2 and rho .25,.6,.9 matched exact energy coefficients to numerical precision. No finite computation stands in for the regenerative CLT.

## originality

PASS

Qualified new exact centered stopped-cycle moment and CLT variance for boundary-triggered sluggish reset diffusion. Frimpong-Bresque-Roldán 2026 supplies the same model, occupation LLN and cycle duration; its accessible account discusses order-T^-1/2 fluctuations but no evaluated coefficient. Poisson-reset occupation CLTs concern a different protocol. Same-paper primary full text could not be retrieved, a significant risk of an explicit coefficient elsewhere.

## value

PASS

It is natural to ask not merely where the occupation fraction concentrates but its exact fluctuations; the universal 1-rho^2 single-cycle law and Brownian invariance versus strictly sluggish monotonicity are structural predictions with direct statistical meaning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
