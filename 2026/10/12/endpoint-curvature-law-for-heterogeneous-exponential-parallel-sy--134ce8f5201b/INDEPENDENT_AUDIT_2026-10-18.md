# Independent mathematical audit

## correctness

PASS

The exact cdfs (1-e^{-lambda1*x})(1-e^{-lambda2*x}) with equal hazard sums S expand at zero with quadratic and cubic terms. Setting Q=Ax+Bx² gives A²=lambda1 lambda2/(theta1 theta2)>1 and B=S A(A-1)/4, hence Q''(0+)>0. At infinity the second survival exponential of X has relative order e^{-(lambda2-lambda1)x}, while the Y second-rate exponential after scaling c=lambda1/theta1 is of strictly higher exponent by the positive identity c(theta2-theta1)-(lambda2-lambda1)=S(c-1). Thus Q=cx-(1/theta1)e^{-alpha x}+o(e^{-alpha x}); implicit density and density-derivative equations justify first and second derivative expansions, not uncontrolled differentiation of big-O. Independent 65-digit mpmath inversion confirmed Q''(.001)=0.184816889953>0, Q''(10) approximately -3.0264e-5, and scaled tail constants near (-2/3,+2/3,-2/3). The theorem proves at least one inflection, NOT uniqueness or multi-component generalizations.

## originality

PASS

PASS best-of-knowledge: Arab–Hadjikyriakou–Oliveira provide numerical curvature signs for the exact (2,3) versus (1.5,3.5) example and a zeroth-order tail straight-line limit. Their full author-posted primary text, especially the final part of Theorem 3.4, explicitly notes inverse-cdf derivatives lack a simple closed expression. The audited first correction with its signed curvature derivative and origin coefficient adds theorem-level analytic asymptotics, not merely numerical non-comparability. Broader 2020 non-comparability criteria are distinct. An equivalent expansion in general reliability literature remains possible.

## value

PASS

PASS: The full paper identifies a visually almost-linear transform whose curvature reverses unexpectedly; analytic endpoint signs and a sharp exponential correction explain the observed phenomenon and give a reusable asymptotic diagnostic in the natural majorization family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
