# Independent mathematical audit

## correctness

PASS

The source Gram identity gives \(\|y_n\|^2=n^{-2}\sum_{i,j}\rho_i\rho_j e^{-\delta^2(H_{i-1}-H_{j-1})^2}\). Since \(\rho_n\to e^{-\delta^2\pi^2/6}\), Cesàro convergence removes the radial factors at vanishing averaged error. Away from the first \(\varepsilon n\) indices, the harmonic-number expansion is uniform and turns the remaining bounded kernel into a Riemann sum for the double integral over \([0,1]^2\); the discarded strips have normalized mass at most \(2\varepsilon\). Symmetry and the substitution \(s=rt\) reduce the double integral to \(\int_0^1e^{-\delta^2(\log r)^2}dr\), and \(u=-\log r\) gives the stated erfc form. This proves the exact positive norm limit without asserting vector norm convergence.

## originality

PASS

Bauschke and Tung construct exactly this firmly nonexpansive harmonic orbit and prove weak convergence of its Cesàro means together with a positive lower norm bound, but the inspected harmonic-example section does not evaluate the double Gram average or state a norm limit. The audited result adds the asymptotic Riemann-sum evaluation and closed Gaussian integral. Resultary searches for the harmonic firmly nonexpansive Cesàro example and an exact norm limit returned no prior matching finding.

## value

PASS

The source is a sharp current counterexample, and identifying its unique positive Cesàro norm limit materially refines the qualitative failure of strong convergence. The closed form exposes the exact asymptotic size of the obstruction rather than merely another lower estimate. That is a natural invariant of the canonical construction and a reusable benchmark for nonlinear mean-ergodic behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
