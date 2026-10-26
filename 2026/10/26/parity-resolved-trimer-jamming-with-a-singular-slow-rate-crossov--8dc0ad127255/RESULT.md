# Parity-resolved trimer jamming with a singular slow-rate crossover

## Finding
Consider irreversible random sequential adsorption of length-three segments on the integer lattice. A segment starting at an even site attempts at rate \(a>0\), and one starting at an odd site at rate \(b>0\); attempts require all three sites empty. There is an exact two-component linear ordinary differential equation for every vacant interval of length at least three and the two site-coverage fractions.

Let \(u_0,u_1\) solve, uniquely for \(t\ge0\),
\[
\begin{aligned}
 u_0'&=-b e^{-bt}u_1-a e^{-(a+b)t}u_0,\\
 u_1'&=-a e^{-at}u_0-b e^{-(a+b)t}u_1,\\
 u_0(0)&=u_1(0)=1.
\end{aligned}
\]
Set \(J_0(t)=\int_0^t a e^{-as}u_0(s)^2\,ds\) and \(J_1(t)=\int_0^t b e^{-bs}u_1(s)^2\,ds\). Then the probabilities \(C_0(t)\), \(C_1(t)\) that respectively an even site and an odd site are covered at time \(t\) are exactly
\[
C_0(t)=2J_0(t)+J_1(t),\qquad C_1(t)=J_0(t)+2J_1(t).
\]
The jammed fractions are their limits as \(t\to\infty\), and these expressions specify them at every positive rate pair.

For \(a>0\) fixed, put \(b=\varepsilon>0\). At any fixed \(s>0\), on the slow time \(t=s/\varepsilon\), the coverage has the explicit limit
\[
\begin{aligned}
\lim_{\varepsilon\downarrow0}C_0(s/\varepsilon)&=1-e^{-2}e^{-s},\\
\lim_{\varepsilon\downarrow0}C_1(s/\varepsilon)&=\tfrac12(1-e^{-2})+2e^{-2}(1-e^{-s}).
\end{aligned}
\]
In particular the limiting jammed densities as \(b\downarrow0\) through positive rates are \(1\) on even sites and \((1+3e^{-2})/2\) on odd sites. The mean coverage tends to \(\tfrac34(1+e^{-2})\). At the exactly zero odd-start rate, by contrast, the jammed densities are \(1-e^{-2}\) and \((1-e^{-2})/2\), with mean \(\tfrac34(1-e^{-2})\). The two orders of the limits \(b\downarrow0\) and \(t\to\infty\) differ by \(3e^{-2}/2\) in mean coverage.

## Assumptions and scope
The substrate is the full integer lattice \(\mathbb Z\), initially vacant, with a Poisson clock of rate \(r_i=a\) for even \(i\) and \(r_i=b\) for odd \(i\) attached to the triple \(\{i,i+1,i+2\}\). Every ringing clock deposits its three sites if and only if all three are vacant. Occupation is permanent; repeated failed clock rings do not change the configuration. In the zero-rate comparison, \(b=0\) means odd-start clocks are absent from the beginning. Time is ordinary continuous time; the slow-scale limit fixes \(s>0\) and sends \(\varepsilon\) to zero. The densities are single-site occupation probabilities, not probabilities that an entire infinite lattice is packed.

## Proof
**Vacant-interval hierarchy.** Let \(E_{i,n}(t)\) denote the probability that the \(n\) sites from \(i\) to \(i+n-1\) are all vacant. For \(n\ge3\), exactly \(n-2\) triples are wholly within this interval, and four other triples cross one boundary. First-event conditioning yields
\[
\begin{aligned}
E'_{i,n}={}&-\Bigl(\sum_{j=i}^{i+n-3}r_j\Bigr)E_{i,n}
-r_{i-1}E_{i-1,n+1}-r_{i-2}E_{i-2,n+2}\\
&-r_{i+n-2}E_{i,n+1}-r_{i+n-1}E_{i,n+2}.
\end{aligned}
\]
All initial values are one. There are no unlisted crossing triples because each depositing particle occupies exactly three consecutive sites.

**Exact closure.** Write \(\overline j\) for the parity of integer \(j\). Direct substitution into this hierarchy gives
\[
E_{i,n}(t)=\exp\Bigl[-t\sum_{j=i}^{i+n-3}r_j\Bigr]
 u_{\overline i}(t)u_{\overline {i+n-1}}(t),\qquad n\ge3.
\]
For a left extension by one site, the relative factor is \(e^{-r_{i-1}t}u_{1-\overline i}/u_{\overline i}\); for two, it is \(e^{-(a+b)t}\). The right extensions give the corresponding factors with the parity of the old right endpoint. These produce precisely the displayed two-component ODE. The linear hierarchy has at most four off-diagonal terms, each bounded by \(\max(a,b)\), and a nonnegative diagonal loss. Duhamel's formula and Grönwall's inequality therefore give uniqueness among bounded interval-probability families on each finite time interval. The candidate closure is bounded uniformly in interval length; hence it equals the physical probabilities. Positivity follows from this identity and the positive probability of no local attempted deposition on a finite interval.

**Coverage.** A three-site interval beginning at an even site is vacant with probability \(e^{-at}u_0(t)^2\), and one beginning at an odd site has probability \(e^{-bt}u_1(t)^2\). Thus the successful deposition rates per starting position are \(J_0'(t)\) and \(J_1'(t)\). An even-start trimer occupies two even sites and one odd site; an odd-start trimer occupies one even and two odd sites. There are equally many starting positions of each parity per unit cell of length two, giving the two coverage identities. Since occupation is monotone and bounded, the jammed limits exist.

**Separated time scales.** Divide all rates by \(a\) if desired; for the limit, keep \(a>0\) fixed. On each fixed time interval, as \(b=\varepsilon\downarrow0\) the equations converge to \(u_0'=u_1'=-a e^{-at}u_0\), with solution \(u_0=u_1=\exp[-(1-e^{-at})]\). Therefore
\[
J_0(\infty)\longrightarrow\int_0^\infty a e^{-at}\exp[-2(1-e^{-at})]\,dt=\frac{1-e^{-2}}2.
\]
This limit follows by dominated convergence because the integrand is bounded by \(ae^{-at}\). More precisely, the same limit holds at upper time \(s/\varepsilon\) for every fixed \(s>0\).

For \(u_1\), its derivative after a large fixed time \(T\) has absolute integral bounded by \(\int_T^\infty(ae^{-at}+\varepsilon e^{-(a+\varepsilon)t})\,dt\), uniformly tending to zero with \(T\to\infty\) and \(\varepsilon\downarrow0\). Together with fixed-time convergence, this proves \(u_1(s/\varepsilon)\to e^{-1}\) for every \(s>0\). Substitute \(v=\varepsilon t\) in the odd-start deposition integral, apply dominated convergence on \([0,s]\), and obtain
\[
J_1(s/\varepsilon)=\int_0^s e^{-v}u_1(v/\varepsilon)^2\,dv\longrightarrow e^{-2}(1-e^{-s}).
\]
The same argument on \([0,\infty)\), dominated by \(e^{-v}\), yields \(J_1(\infty)\to e^{-2}\). Combining the limits proves the claimed time-dependent and jammed densities. At exactly \(\varepsilon=0\), \(J_1\equiv0\) and \(J_0(\infty)=(1-e^{-2})/2\). The jump of \(3e^{-2}/2\) follows.

There is also a geometric interpretation: the fast even-start triples are ordinary dimer arrivals on the compressed lattice of even sites; the remaining even vertices are isolated vacancies of this greedy matching. Each such vacancy has two vacant odd neighbors, and the resulting slow odd-start triples are disjoint. They fill independently at slow rate, accounting for the exponential crossover and three added occupied sites per fast-stage defect.

## Verification
Two independently coded finite-ring checks complement the proof. `trimer_verify.py` compares the ODE predictions with an exact rational first-successful-arrival recursion for rings of lengths 6 through 18 and with random exponential-priority packing on 300-site rings. It also tests the rate-separation limit at five positive slow times. It completed 134 coded conditions. `trimer_transient.py` independently simulates finite-time vacancy probabilities on 100-site rings for nine parameter-time pairs, comparing both parity classes with the vacant-interval ODE (18 inequalities passed). Run with Python 3 and NumPy/SciPy installed, using `python trimer_verify.py` and `python trimer_transient.py` in the directory containing these files. Finite computations test small and large finite systems; they are not a substitute for the infinite-lattice proof.

## Relationship to prior work
Classical uniform one-dimensional \(k\)-mer adsorption gives the \(k=3\) reference jamming coverage \(0.82365296\ldots\), also recorded in the full text of Lebovka et al. (2011). Their paper treats orientation anisotropy on two-dimensional square lattices, not parity-dependent starting-position rates on the infinite one-dimensional trimer lattice. de Oliveira and Tomé (1994) study inhomogeneous adsorption on bipartite lattices and report exact sublattice coverage formulas for a linear chain. The precise exclusion footprint and full implications of that closely related paper could not be determined from the accessible abstract; its full text was not available. Consequently priority and possible broader coverage remain uncertain. The evaluated claim here is restricted to occupied length-three segments, the explicit two-component closure, and its singular limit; it does not purport to originate empty-interval methods or the uniform trimer formula.

## Limitations
All formulas concern irreversible homogeneous-within-parity length-three segments and two alternating positive rates, except for the explicitly stated zero-rate boundary. No strict monotonicity or optimality theorem in the rate ratio is asserted. The slow-time formula is for fixed positive \(s\) only, not a uniform approximation down to \(s=0\). The result does not classify spatial correlation functions beyond contiguous empty intervals, random substrates, other segment lengths, or finite-size correction coefficients. The full text of the closely related 1994 bipartite-adsorption source was inaccessible, so historical originality is not independently established.

## References
1. J. W. Evans, *Random and cooperative sequential adsorption*, Reviews of Modern Physics **65**, 1281 (1993), DOI: 10.1103/RevModPhys.65.1281.
2. M. J. de Oliveira and T. Tomé, *Inhomogeneous random sequential adsorption on bipartite lattices*, Physical Review E **50**, 4523 (1994), DOI: 10.1103/PhysRevE.50.4523.
3. N. I. Lebovka, N. N. Karmazina, Y. Y. Tarasevich and V. V. Laptev, *Random sequential adsorption of partially oriented linear k-mers on square lattice*, arXiv:1109.3271v1 (publicly posted 2011-09-15); later Physical Review E **84**, 061603 (2011).
