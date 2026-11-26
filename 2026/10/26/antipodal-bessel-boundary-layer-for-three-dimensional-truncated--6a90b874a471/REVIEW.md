# Independent mathematical audit

## correctness

PASS

The Legendre generating function and its derivative give the full Poisson kernel in the stated normalization. With q=cos(z/N)+i sin(z/N)cos(φ), parity and the Laplace integral express each omitted term as the integral of (2n+1)(−rq)^n. Because |q|≤1 and r<1, the sum can be taken inside the integral. The tail divided by (−r)^(N+1) is the average of q^(N+1) times [(2N+3)/(1+rq)−2rq/(1+rq)^2]. For fixed z, q^(N+1) tends uniformly to exp(iz cos(φ)), while the bracket divided by N tends uniformly to one. The normalized integral is therefore J₀(z). With δ=1−r_N(c), Nδ²→0 and N²r_N(c)^(N+1)/log N→e^(−c); the full kernel is δ/4·(1+o(1)) since the denominator tends to 8. Subtracting the tail yields the stated sign and prefactor for both parities. The series for J₀(4) has partial sum −1/3 at k=4, followed by a negative alternating remainder of decreasing magnitudes. Negativity for each fixed c below the respective threshold implies R_N<r_N(c), and taking c upward yields the liminf with the stated inequality direction. At r=1−β log N/N, the full-kernel to Nr^(N+1) ratio is O(log N·N^(β−2)), proving strict negativity at z=4 along even N for 0<β<2. These are obstructions only. The frozen numerical script was read, not run; the rational alternating-sum bound is in the proof, not the numerical script.

## originality

PASS

The supported distinctive part is the fixed-angle antipodal-window law for the finite sum and its genuinely off-antipode even-degree obstruction. Reusken already treats the same projected kernel, proves the leading odd obstruction, and gives the exact odd t=−1 identity; that identity yields the odd z=0 second-order comparison by substitution. The comparison clause deserves no separate priority credit. Classical polynomial/Bessel limits are prior input, not the finite-sum law.

## value

PASS

The sign of the projected kernel controls a maximum-principle property. The angular scale is not an arbitrary evaluation slice: at fixed z near the antipode the first oscillatory tail can compete with the small smooth Poisson term, and the negative Bessel lobe provides an even-degree obstruction in the regime left untreated by the prior odd proof. The profile explains this mechanism and determines a second-order obstruction without overclaiming the global positivity radius.

The dated certificate retains the supplied scientific assessment, sources and limitations.
