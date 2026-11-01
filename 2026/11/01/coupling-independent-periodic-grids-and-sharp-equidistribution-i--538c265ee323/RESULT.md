# Coupling-independent periodic grids and sharp equidistribution in triangular modular maps

## Finding

For arbitrary Borel triangular forcing, the integer-expanding modular three-coordinate system has exactly computable periodic point counts, independent of the forcing; its uniform periodic-point measures approximate normalized volume at an explicit exponential rate, without smoothness or boundedness-of-derivatives assumptions on the forcing.

For every integer \(n\ge1\), the total number of fixed points of the \(n\)-th iterate is
\[
P_n=(A^n-1)(C^n-1)(E^n-1).
\]
The number of geometrically distinct primitive orbits of least period \(n\) is
\[
O_n=\frac1n\sum_{d\mid n}\mu(n/d)(A^d-1)(C^d-1)(E^d-1),
\]
where \(\mu\) is the classical Möbius function. The Artin–Mazur dynamical zeta function is the following rational formal power series:
\[
\zeta_F(t)=\frac{(1-ACt)(1-AEt)(1-CEt)(1-t)}{(1-ACEt)(1-At)(1-Ct)(1-Et)}.
\]
Let \(\nu_n\) be uniform probability on \(\operatorname{Fix}(F^n)\), and \(m\) normalized Lebesgue measure on the state cube. For all real-valued observables \(h\) that are 1-Lipschitz with respect to the \(\ell^1\) metric,
\[
\left|\int h\,d\nu_n-\int h\,dm\right|\le\frac\beta2\left(\frac1{A^n-1}+\frac1{C^n-1}+\frac1{E^n-1}\right).
\]
Equivalently this bounds their \(1\)-Wasserstein distance for the \(\ell^1\) metric. When \(r=0\), the observable \(h(x,y,z)=z\) attains the single-coordinate discrepancy \(\beta/[2(E^n-1)]\), so an exponential rate faster than the slowest slope's inverse power is impossible uniformly over the forcing and shifts. Normalized Lebesgue measure is invariant under \(F\) as well.

## Assumptions and scope

Fix a real width \(\beta>0\), positive integers \(A,C,E\ge2\), a real constant \(r\), and arbitrary finite-valued Borel functions \(\Phi:[0,\beta)^2\to\mathbb R\) and \(\Psi:[0,\beta)\to\mathbb R\). For \(u\in\mathbb R\), define the canonical remainder \([u]_\beta=u-\beta\lfloor u/\beta\rfloor\in[0,\beta)\). Define a deterministic Borel map of the half-open cube \(X=[0,\beta)^3\) into itself by
\[
F(x,y,z)=\bigl([Ax+\Phi(y,z)]_\beta,\ [Cy+\Psi(z)]_\beta,\ [Ez+r]_\beta\bigr).
\]
No continuity or periodic boundary compatibility of \(\Phi\) or \(\Psi\) is assumed. The cube is treated as a canonical domain with its ordinary Euclidean coordinates, and the \(\ell^1\) distance means \(|x-x'|+|y-y'|+|z-z'|\), not the wrapped torus metric. All fixed points are distinct coordinate triples in this domain. The polynomial subfamily \(\Phi(y,z)=b y^\gamma\), \(\Psi(z)=d z^\gamma\) with real \(b,d\), positive integer \(\gamma\), and **fixed** \(r\) specializes equation (1) of Zhang, Dong, Zhang and Ding (2023); their random-in-time disturbance is deliberately not part of this deterministic theorem.

## Proof

**1. Modular iterate reduction.** Let \(D\in\mathbb Z_{\ge2}\), \(\beta>0\), and \(K\in\mathbb R\). The congruence
\[
[D^n u+K]_\beta=u,\qquad 0\le u<\beta,
\]
is equivalent to \((D^n-1)u+K\in\beta\mathbb Z\). It therefore has exactly \(D^n-1\) solutions in the half-open interval, and those solutions are a translate modulo \(\beta\) of the equally spaced grid \(\{j\beta/(D^n-1):0\le j<D^n-1\}\). Integer \(D\) is essential here: it ensures that repeated reduction modulo \(\beta\) does not change the final expression \([D^n u+K]_\beta\).

**2. Triangular periodic-point census.** The last coordinate evolves independently as \(z\mapsto[Ez+r]_\beta\). By Step 1, exactly \(E^n-1\) initial \(z\)-values return after \(n\) steps. Fix one such complete \(z\)-itinerary. The first \(n\) iterates of the second coordinate reduce to
\[
[y_n]_\beta=[C^n y_0+K_y(z_0,\ldots,z_{n-1})]_\beta,
\]
where \(K_y\) is a finite weighted sum of the values \(\Psi(z_j)\), independent of \(y_0\). Again Step 1 yields exactly \(C^n-1\) possible \(y_0\), each generating its own full \(y\)-itinerary. Fix each such pair of itineraries. The first coordinate similarly satisfies \(x_n=[A^n x_0+K_x]_\beta\) for a constant depending only on these itineraries. It admits exactly \(A^n-1\) initial \(x_0\). No solutions are omitted or counted twice, proving \(P_n\). Since the finite fixed set of \(F^n\) partitions into orbits of periods dividing \(n\), Möbius inversion yields \(O_n\).

**3. Exact zeta function.** Expand the product:
\[
P_n=(ACE)^n-(AC)^n-(AE)^n-(CE)^n+A^n+C^n+E^n-1.
\]
Insert this into the defining formal identity \(\log\zeta_F(t)=\sum_{n\ge1}P_n t^n/n\) and use \(-\log(1-kt)=\sum_{n\ge1}k^n t^n/n\). This yields the displayed rational function, with constant coefficient \(1\).

**4. Volume invariance.** For each positive integer \(D\), each real \(v\), and every integrable function \(g\) on \([0,\beta)\),
\[
\int_0^\beta g([Du+v]_\beta)\,du=\int_0^\beta g(u)\,du.
\]
Integrate an arbitrary bounded measurable test function of \(F(x,y,z)\) successively in \(x\), then \(y\), then \(z\). The triangular dependence makes each step a translated integer-multiplication map, so the integral is unchanged. Thus normalized Lebesgue measure \(m\) is \(F\)-invariant. No assertion of unique invariance or mixing is needed.

**5. Uniform quantitative distribution.** An equally spaced \(N\)-point grid on \([0,\beta)\) with arbitrary offset is of the form \(u_j=\beta(j+\theta)/N\), where \(0\le j<N\) and \(0\le\theta<1\). For a 1-Lipschitz function \(g\), pair each \(u_j\) with the cell \([j\beta/N,(j+1)\beta/N)\). The average absolute cellwise distance is
\[
\frac\beta{2N}\bigl(\theta^2+(1-\theta)^2\bigr)\le\frac\beta{2N}.
\]
Consequently the difference between uniform-grid averaging and normalized interval integration is bounded by \(\beta/(2N)\). In the finite set constructed in Step 2, conditional on every downstream pair \((y,z)\), the \(x\)-coordinates form an offset grid of size \(A^n-1\). Replace its average by normalized \(x\)-integration, incurring at most \(\beta/[2(A^n-1)]\). Conditional on each \(z\), the remaining \(y\)-coordinates form an offset grid of size \(C^n-1\); after the first replacement the integrand remains 1-Lipschitz in \(y\). Replace this average by normalized \(y\)-integration, then replace the final \(z\)-grid by normalized \(z\)-integration. The triangle inequality gives the displayed three-term bound, independently of all forcing values and their regularity. It also implies \(\nu_n\) converges weakly to \(m\).

**6. Sharp exponent.** Set \(r=0\). The \(z\)-coordinates of all \(F^n\)-fixed points, counting their equal multiplicities, are exactly \(z_j=j\beta/(E^n-1)\), for \(j=0,\ldots,E^n-2\). Their average is \(\beta/2-\beta/[2(E^n-1)]\), whereas \(m\) has \(z\)-mean \(\beta/2\). The 1-Lipschitz test \(h(x,y,z)=z\) thus produces equality in the individual \(E\)-coordinate bound. In particular, if \(E\le A,C\), the upper and lower bounds have the same exponential order \(E^{-n}\), uniformly over the entire forcing class; no strictly faster uniform exponential convergence assertion is possible.

## Verification

The standalone file `verify_periodic_grid.py` uses exact rational arithmetic and no external packages. It constructs all fixed-point grids by successive congruence solving for the polynomial forcing \(\Phi(y,z)=b y^\gamma\), \(\Psi(z)=d z^\gamma\), checks distinctness and exact return under direct map iteration, and tests the mean-discrepancy inequality at periods \(1,2,3\). Three nontrivial parameter choices, including moduli \(1\), \(5/3\), and \(7/4\), give fixed point counts \(2\), \(72\), and \(1274\) at these periods. The zero-shift last coordinate also realizes the sharp single-coordinate discrepancy at period \(3\). A further explicitly discontinuous, piecewise-constant Borel forcing example with three identical slopes \(2\) has counts \(1,27,343\) at periods \(1,2,3\), each checked by direct iteration. These computations do not replace the all-period, arbitrary-Borel-function proof.

## Relationship to prior work

Zhang, Dong, Zhang and Ding introduced the polynomial triangular modular construction and analyzed its Lyapunov spectrum and application to encryption (2023, equation (1)). The deterministic fixed-disturbance integer-expansion subfamily considered here is not their randomly disturbed implementation. Their investigated dynamical properties do not state the exact all-period point census, the coupling-invariant rational dynamical zeta function, or a forcing-independent sharp quantitative periodic-point equidistribution inequality.

The general Möbius inversion between fixed points and primitive orbits is classical, as discussed by Puri and Ward (2001); that identity alone does not determine the product formula for the nonlinear triangular family. Chothi, Everest and Ward (1997) established broad periodic-point asymptotics and Haar equidistribution for algebraic-group systems, which includes uncoupled integer circle multiplications. Those results do not directly encompass arbitrary Borel triangular forcing, or yield the stated all-parameter uniform finite-time Wasserstein estimate. Work on smooth random partially expanding skew products and on expanding Thurston maps similarly has different structural hypotheses. The present contribution is the forcing-insensitive *exact* finite-level structure, notably with neither smoothness nor continuous torus descent of the nonlinear forcing required.

## Limitations

The integer slopes are indispensable to the congruence argument; the theorem does not cover the general nonintegral parameter values studied in the source article. The disturbance \(r\) is fixed, not independently sampled at every iteration. The zeta function is a periodic-point formal series and is not a security metric. No claims are made about randomness tests, cryptographic security, uniqueness of invariant measures, mixing, or the topological entropy of a discontinuous map. The three-term Wasserstein bound has a sharp *exponential order* when the last-coordinate slope is smallest, but the optimal prefactor for the full three-coordinate error is not determined. Possible unpublished or unindexed extensions of the standard skew-product argument remain a publication-priority uncertainty.

## References

1. Y. Zhang, W. Dong, J. Zhang and Q. Ding, “An Image Encryption Transmission Scheme Based on a Polynomial Chaotic Map,” *Entropy* **25** (2023), 1005, first published 2023-06-29. DOI: `10.3390/e25071005`. Open access: https://pmc.ncbi.nlm.nih.gov/articles/PMC10377869/ .
2. Y. Puri and T. Ward, “Arithmetic and growth of periodic orbits,” *Journal of Integer Sequences* **4** (2001), article 01.2.1; https://eprints.whiterose.ac.uk/id/eprint/149677/ .
3. V. Chothi, G. Everest and T. Ward, “S-integer dynamical systems: periodic points,” *J. Reine Angew. Math.* **489** (1997), 99–132. DOI: `10.1515/crll.1997.489.99`.
4. Z. Li, “Periodic Points and the Measure of Maximal Entropy of an Expanding Thurston Map,” arXiv:1311.6906 (2013). That article concerns expanding sphere maps, not arbitrary triangular modular forcing.
