# Independent mathematical audit

## correctness

PASS

The positive Dirichlet Laplacian has an explicitly reconstructible Green diagonal \(G_m(t)=(1-r^{2m})/\sqrt{t(t+4)}\), with \(t=(1-r)^2/r\). The resolvent Cauchy–Schwarz bound yields \(K_m\le\sup_t2\sqrt t G_m(t)\); at the unique maximum of this function, differentiating \(G_m\) gives \(\|Dg_t\|_2^2=t\|g_t\|_2^2\), so the upper bound is attained and equality vectors are exactly multiples of \(g_t\). The logarithmic derivative is a product of strictly decreasing positive terms, giving unique \(r_m\) and strict site monotonicity. With \(a_m=-m\log r_m\), the critical equation is \(e^{2a_m}-1=4m\coth(a_m/(2m))\); it gives \(a_m=\log m-\frac12\log\log m+\frac12\log8+o(1)\). Expanding \(K_m=(1-e^{-2a_m})\operatorname{sech}(a_m/(2m))\) yields the stated logarithmic deficit. The actual check_halfline.py uses monotone root finding, finite extremizers and random checks; its code was inspected, not used as an infinite proof.

## originality

PASS

Ilyin–Laptev–Zelik give the whole-lattice sharp constant one and the Green-resolvent optimization method; neither that constant nor its nonattainment controls a fixed site at finite distance from a Dirichlet boundary. The known half-line Jacobi resolvent supplies the kernel but not the optimization, unique all-site extremizers, or logarithmic boundary-layer asymptotic. No checked primary text supplies the exact \(K_m\) profile or the coefficient \(1/8\) and three-term expansion, though the prior-results search service was unavailable.

## value

PASS

Optimal interpolation constants at specified distances from a Dirichlet boundary and their distinct logarithmic approach to the whole-lattice constant are natural analytic invariants. The complete equality cases and sharp leading/three-term deficit are useful boundary-layer information not supplied by the general resolvent method alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
