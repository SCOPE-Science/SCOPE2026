# Independent mathematical audit

## correctness

PASS

Eliminating y gives x_(j+1)x_(j-1)=lambda*x_j^2/(1+x_j). Its positive lift y_j=x_(j+1)(1+x_j)/x_j is unique and preserves least period. After taking logs, the centered energy identity bounds the cyclic difference energy strictly above by the centered squared norm, since g'(u)=-exp(u)/(1+exp(u)) lies strictly between -1 and 0. The first nonzero Fourier eigenvalue of the cyclic difference energy is 4sin^2(pi/q)>=1 for 2<=q<=6, including equality at six, so only constants remain and they give (lambda-1,lambda). At lambda=5 the palindromic ansatz enforces all scalar equations except the midpoint, whose residual Z(1+W)-5W equals -ZR/[Y(1+Z)] in the source notation. Independent rational recalculation gives R(41/4)=49241/13254 and R(19)=-19/882. Continuity supplies a positive root with X>41/4, so the lift is not the fixed point with x=4; primality of seven proves least period seven. This is a sign certificate plus an analytic exclusion, not a numerical orbit claim. Frozen check.py was inspected, not executed.

## originality

PASS

The May model, its equilibrium and the exclusion of a positive two-cycle are not new. In the sources checked, the universal exclusion through period six together with a rigorous positive primitive period-seven witness for this precise autonomous k=1 map is distinct. The nearby period-six and period-seven references do not establish this sharp gap under the stated hypotheses.

## value

PASS

This establishes a uniform, attained cutoff for the first possible nonstationary positive orbit in a standard nonlinear model. The spectral bound controls finite-amplitude orbits even at the strict period-six boundary, and the parameter-explicit seven-cycle makes the bound sharp rather than just a necessary estimate or a numerical sighting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
