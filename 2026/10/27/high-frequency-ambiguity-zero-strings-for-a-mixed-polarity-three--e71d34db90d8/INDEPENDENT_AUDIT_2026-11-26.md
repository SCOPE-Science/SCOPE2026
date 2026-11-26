# Independent mathematical audit

## correctness

PASS

For w=pi*nu the one-sided ambiguity integrals give exp(-u|T|)/(2u) and exp(-v|T|)/(2v), with u=a+iw and v=b-iw. Changing variables in the four-factor integral gives convolution in delay; splitting the two-kernel convolution at 0 and T and then applying (1/u)-partial_u gives the stated three-kernel expression. None of its denominators vanish on the real w axis for a>b>0. An independent algebra check writes the zero-equation right side R exactly as -(1+lambda*T)+(3*lambda*T/2)x+((3-lambda*T)/2)x^2-x^3/2 for x=lambda/u. Thus the first reciprocal-w correction is imaginary and the frozen second-order coefficient also agrees. The limiting equation is strictly convex with negative derivative at zero and a unique transverse positive crossing at T_*. With w=(pi*(n+1/2)+theta/2)/T the real Jacobian at infinite index is diagonal with entries F'(T_*) and exp(d*T_*). Analytic implicit continuation therefore produces real zeros; the imaginary correction gives theta=O(1/n), the real equation gives T-T_*=O(1/n^2), and the frequency and spacing laws follow. At fixed delay the complex derivative tends to -2i*T_*exp(d*T_*), and the ambiguity function is holomorphic near each real frequency by its exponential tails. For the boundary limit let h=d/lambda and y=d*T_*; h=y/(exp(y)-1) implies y tends to infinity, and y=log(1/h)+log(y+h) gives y/log(1/h) tending to 1 and then the log-log term with o(1) remainder. This verifies RESULT.md lines 49–129 for fixed rates, with a separate limit for T_* only. The inspected checker and its recorded nine roots are corroboration, not the asymptotic certificate.

## originality

PASS

The pass concerns the quantitative cofinite simple-zero string and limiting-delay law for the specified asymmetric three-factor family. It does not credit the qualitative observation that totally positive windows can have ambiguity zeros.

## value

PASS

The next mixed-polarity repeated convolution is a natural test against zero-free unequal two-factor and same-polarity families. It gives infinitely many genuine real nulls, not numerical near-cancellations, and explains where they concentrate and how that limiting delay escapes near equal rates. The quantitative location and simplicity answer a more precise question than the already known existence of zeros for some totally positive functions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
