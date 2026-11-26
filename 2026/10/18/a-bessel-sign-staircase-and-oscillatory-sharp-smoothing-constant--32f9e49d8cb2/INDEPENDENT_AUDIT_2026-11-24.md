# Independent mathematical audit

## correctness

PASS

This PASS is for the corrected files in repairs/1, not for the original extremizer classification. At any t in (0,tau_1) the real sign input is negative only at zero. Taking f=-1 on the positive squares and +1 elsewhere yields an extremizer not of the stated translated/signed form: viewed from successive square sites, the translated f converges locally to the sign kernel, so summability gives extremizing output values in the limit; no site attains the convolution norm. Also, over complex scalars the allowed global factor is any unit phase, not only a sign. The repair states fixed-output-site equality, where equality in the triangle inequality gives exactly the unit-phase sign pattern and freedom at zero entries. For the main claim, H=Delta G has zero sum and ℓ1 size equal to both endpoint operator norms (point mass and sign input). The Riccati equation orders adjacent log derivatives by the strictly positive derivative of their difference at any common value. At L_m=1 the derivative equals (m^2-x)/x^2; a first crossing below m^2 cannot occur, and at equality the second derivative is strictly negative, contrary to positivity on its left. Small x starts above and large x ends below for m>=1, and every later zero crosses downward. L_0<1 by the positive integral for I_0-I_1. This proves the negative central block and exactly the ordered switches. Telescoping that block gives 4(G(m)-G(m+1)); consecutive nonnegative-index differences differ by H, giving the unique maximizer and adjacent tie. In the scaling h=x^(-1/2), u=mh, expanding the Fourier multiplier with Gaussian domination gives H/h^3=phi(u)[u^2-1+h^2(He_4/12+He_6/24)+O(h^4)]. The crossing localizes at u=1 and the correction there is 1/2; with u^2=m^2/x the root is x=m^2+1/2+O(m^-2). For the first difference about the midpoint, the h^2 relative correction at v=1 is (He_3(1)+He_5(1))/24=1/6. The leading profile v phi(v) has quadratic coefficient -phi(1) there. Mis-rounding occurs only within O(1) in x of x=j^2 and affects the squared phase distance by O(x^-1/2). Thus multiplying the optimized first difference by four and setting x=2t gives the stated coefficient 1/12-rho^2/2 and the exact accumulation interval [-1/24,1/12]. The repair makes these remainder and boundary arguments explicit and corrects the verification description: check.py uses Fourier quadrature, not a positive Bessel series. Frozen verification and script were inspected, not executed; the reported 134 finite assertions are not a proof or a required certificate.

## originality

PASS

PASS applies only to the repaired quantitative asymptotic claim: the constant shift with error bound for the switch times and the uniform phase-dependent second-order endpoint norm, including its interval of limit points. The original attribution of novelty to the exact all-time formula and staircase does not pass: the distinct indexed gradient theorem gives exactly their root equation and maximizing-index law, and telescoping transfers the sharp norm. The repair treats those results as inputs or rederived auxiliaries. Existing gradient brackets do not give the shift or optimized second-order coefficient. This is a bounded statement-coverage decision, not a claim of historical priority.

## value

PASS

Even after discarding novelty credit for the exact staircase, the sharp uniform second-order asymptotic resolves a natural continuum-versus-lattice question: the correction is a phase effect with a nontrivial interval of subsequential limits, not a constant. It quantifies the best endpoint time-derivative amplification and the discrepancy between continuum rounding and actual switching, rather than just adding an arbitrary parameter or tightening an unmotivated bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
