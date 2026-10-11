# Independent mathematical audit

## correctness

PASS

Independent reduction gives trace \((2+\sigma-2r)/(1+\sigma)\), determinant \((1-r)/(1+\sigma)\), and discriminant \((\sigma^2-4r(1-r))/(1+\sigma)^2\). Below the repeated-root threshold the eigenvalues are conjugate with modulus \(\sqrt{(1-r)/(1+\sigma)}\), strictly decreasing. Above it the larger real root has positive derivative. Hence the unique minimum is at \(\sigma_*=2\sqrt{r(1-r)}\). Substitution into \(r=\sigma^2a^2/\beta\) gives the beta formula. Independent numerical monotonicity checks covered representative \(r\) values from 0.05 to 0.95.

## originality

PASS

The 2016/2018 source defines the ratio and convergence ceiling but explicitly treats ratio adaptation as outside its main strategy; Fercoq later makes spectral-radius minimization central but does not state the audited scalar closed form in the inspected material. No exact Resultary match was found.

## value

PASS

The formula gives an exact calibration of a free primal/dual ratio on the canonical one-singular-value model, and identifies the same underdamped/overdamped transition that later adaptive spectral methods try to locate numerically. It is a useful analytic benchmark rather than an arbitrary parameter sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
