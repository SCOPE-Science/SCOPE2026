# Independent mathematical audit

## correctness

PASS

Reconstructed SPD drift Q=[[a+d,-d],[-d,b+d]] for positive a,b and d>=0; its stationary Gaussian covariance exists, is unique, and solves QC+CQ=diag(A,B). Eliminating three covariance entries gives V(d)=(a+b+4d)[A(b+d)+B(a+d)]/[2(a+b+2d)(ab+(a+b)d)], with V(0)=A/(2a)+B/(2b) and V(infinity)=(A+B)/(a+b). For 0<a<b, derivative sign is BU(d)-AW(d), where U and W are the stated positive quadratics. Independent symbolic polynomial differentiation confirmed both the exact V derivative denominator and R=U/W derivative 4(b-a)(a+b)(a+b+2d)[ab+(a+b)d]/W^2>0 for all finite d>=0. R endpoints are (a/b)^2 and (3a+b)/(a+3b). These imply increasing/decreasing/single-global-minimum cases exactly according to A/B and endpoint equality, including strict monotonicity on finite d and no false finite boundary optimum. a=b decouples the sum. Exact witness a=1,b=2,A=1/2,B=1,d*=1 gives 49/100 against 1/2 endpoints.

## originality

PASS

The exact one-valley necessary/sufficient *noise-intensity ratio* phase diagram for stationary regional-sum fluctuations in a heterogeneous symmetric-coupling two-patch OU model was not located in compared ecological/OU prior work. The Lyapunov method and qualitative nonmonotone spatial insurance are standard, credited; the original aspect is the monotone rational threshold and global no-other-extrema classification. O’Regan et al. 2017 studies additive/multiplicative noise and heterogeneity in two-patch ecological systems, a significant plausible comparison; its full mathematical sections were not exhaustively read.

## value

PASS

Regional fluctuation variance is a natural ecological spatial-insurance observable. The result separates exact noise/return-rate heterogeneity regimes in which dispersal helps or hurts and exhibits a mathematically unique interior optimum, rather than merely a numerical optimal d. The independent Gaussian-input, linearized domain is narrow but a standard calibration model; no broader extinction or nonlinear persistence claim is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
