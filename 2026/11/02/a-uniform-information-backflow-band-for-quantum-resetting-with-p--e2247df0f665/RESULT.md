# A uniform information-backflow band for quantum resetting with positive-rate memory

## Finding

Let \(\omega\ne0\) be the Bohr frequency of a two-level Hamiltonian, and let \(r>0\) be the rate of Poisson resetting to a uniformly sampled **earlier state of the same trajectory**. The ensemble-averaged dynamical channel is the uniform-memory model introduced by de Mauro, Kulkarni and Majumdar (2026). Define \(\lambda=r/|\omega|\). For every
\[
\boxed{\frac15\le\lambda\le\frac12},
\]
there exists one pair \((s,t)\) from the *fixed five-pair set*
\[
\mathcal T=\{(20,23),(14,16),(8,10),(7,10),(8,9)\}
\]
such that, for the two orthogonal equatorial pure states of the energy basis, their trace distance \(D\) satisfies
\[
\boxed{D(t/|\omega|)-D(s/|\omega|)>\frac1{400}.}
\]
Consequently the channel is not positive-divisible, hence not completely-positive-divisible, throughout that entire closed band, despite every actual reset having a **positive** Poisson intensity. The strictly positive lower bound is uniform in \(\lambda\), and the five possible measurements times are independent of the precise resetting rate. Neither sharpness of the band nor absence of revival at other rates is asserted.

## Assumptions and scope

Consider a time-independent, nondegenerate two-level Hamiltonian with energy difference \(|\omega|>0\). Between resets, the state evolves under this Hamiltonian. Each reset occurs from a classical Poisson clock of rate \(r>0\), and selects a time uniformly in the entire physical history preceding the reset, returning the state to the state realized at that selected time. The ensemble-averaged evolution acts linearly on any initial density matrix. Units are chosen so that \(\hbar=1\).

For energy eigenstates \(|0\rangle,|1\rangle\), take the input pair \(|\pm\rangle=(|0\rangle\pm|1\rangle)/\sqrt2\). The trace distance means \(D(\rho,\sigma)=\tfrac12\|\rho-\sigma\|_1\). No entanglement, measurement feedback, negative probability or time-dependent instantaneous reset intensity is assumed. The theorem concerns an ensemble channel and is not a statement about trace distances along individual random trajectories.

## Proof

**1. Reduction to a scalar coherence.** The published uniform-memory evolution equation in the energy basis is
\[
\partial_t f_\omega(t)=-(r+i\omega)f_\omega(t)+\frac r t\int_0^t f_\omega(u)\,du,
\qquad f_\omega(0)=1.
\]
Its unique regular solution is
\[
f_\omega(t)={}_1F_1\!\left(\frac{i\omega}{r+i\omega};1;-(r+i\omega)t\right).
\]
Diagonal density-matrix elements stay fixed, while each off-diagonal element is multiplied by \(f_\omega(t)\). Hence the trace distance of the specified pair is exactly \(D(t)=|f_\omega(t)|\). Changing the sign of \(\omega\) conjugates this function, so it suffices to set \(\omega=1\) and use dimensionless times.

**2. Exact local special-function bounds.** Fix a rational center \(q=k/10^6\) listed in `backflow_cover.csv`, with an associated time pair \((s,t)\) and rational bounds \(U,L\) also listed there. Put
\[
a_q=\frac{1+iq}{1+q^2},\qquad z_q(u)=-(q+i)u,
\]
and define the 130-term Kummer polynomial
\[
P_{q,u}=\sum_{n=0}^{129}\frac{(a_q)_n z_q(u)^n}{(n!)^2}.
\]
Each real and imaginary part of \(P_{q,u}\) is exactly rational. For every listed center, \(1/5\le q\le1/2\) and \(1\le u\le23\), so \(|z_q(u)|<26\) and \(|a_q+n|\le n+2\). Therefore the modulus of the 130th term is bounded by \(131\cdot26^{130}/130!\), and the ratio of successive term bounds beyond index 130 is at most \(26\cdot132/131^2<1/5\). The full tail is thus bounded by
\[
R_*:=\frac{5\cdot131\cdot26^{130}}{4\cdot130!}<10^{-30}.
\]
The independent exact-rational checker proves for each one of **786** rows that
\[
|P_{q,s}|^2<(U-R_*)^2,\qquad
|P_{q,t}|^2>(L+R_*)^2.
\]
The tail inequality then gives \(|f_q(s)|<U<L<|f_q(t)|\). This is finite arithmetic of rational integers, not numerical sampling or extrapolation. The complete rational centers, time pairs and rational comparison bounds appear in the accompanying CSV. The complete standalone verifier is supplied and uses only the Python standard library.

**3. Extension from centers to a continuum.** Couple two Poisson resetting clocks of rates \(r\) and \(q\) using common events of rate \(\min(r,q)\) and independent excess events of rate \(|r-q|\). Use the same uniform random draws for the remembered past times at common events. Until the first excess event the full trajectories agree. Writing their coherence factors as expectations of unit-modulus phase variables therefore gives, at dimensionless time \(u\),
\[
|f_r(u)-f_q(u)|\le2(1-e^{-|r-q|u})\le2u|r-q|,
\]
and the same Lipschitz estimate holds for their moduli. Let \(g_q=L-U>0\). Every \(r\) in
\[
J_q=\left[q-\frac{g_q}{4(s+t)},\quad q+\frac{g_q}{4(s+t)}\right]
\]
therefore satisfies
\[
|f_r(t)|-|f_r(s)|>g_q-2(s+t)|r-q|\ge\frac{g_q}{2}.
\]
The verifier checks, with exact fractions and ordered intervals, that the union of all 786 intervals \(J_q\) contains the entire interval \([1/5,1/2]\). It also checks that \(g_q/2>1/400\) for every row. This proves the uniform strict bound for every real rate in the band, not only the rational centers.

**4. Operational nondivisibility.** The differences of the two output density matrices have eigenvalues \(\pm|f_r(u)|\), giving the stated trace distance. A positive trace-preserving intermediate channel cannot increase trace distance of two states. The strict increase at one of the five time pairs therefore rules out P-divisibility, and a fortiori CP-divisibility, for each allowed rate. The usual trace-distance information-backflow measure is at least \(1/400\) over the observation interval chosen for that rate.

## Verification

Run `python3 verify_memory_backflow.py` with `backflow_cover.csv` in the same directory. It checks every individual Kummer Taylor inequality using exact `fractions.Fraction` arithmetic, proves the uniform remainder bound by integer inequalities, reconstructs the continuum covering without floating-point comparisons, and checks the uniform positive lower bound. In the tested package, all **786** certificate rows passed, with coverage extending to \(0.500012808824\ldots\), beyond the required endpoint \(1/2\). The Python proof is fully finite; the infinite-time dynamical definition and reduction to the published Kummer function use the analytical arguments above.

## Relationship to prior work

De Mauro, Kulkarni and Majumdar (2026), arXiv:2608.02297, introduced and solved exactly the uniform-memory quantum-reset protocol. The master equation, Kummer representation and algebraic large-time coherence decay are prior results and are **not** claimed here. Their two-level analysis reports decaying polarization oscillations and does not establish a strictly increasing trace distance or a continuum resetting-rate band with a uniform positive backflow bound.

Carollo and Wald (2026), arXiv:2601.13367, analyze discrete-time resets to a **fixed** reference state. Under genuine nonnegative reset probabilities they show nonincreasing trace distance in that setting; their revivals require quantum-effective negative reset probabilities. The theorem here concerns a different operation: every reset has positive probability, but its destination is a previously visited state. The contrast clarifies why classical positivity of reset events does not by itself preclude operational information backflow when the reset destination carries memory. General trace-distance backflow and divisibility criteria are standard, including the work of Breuer, Laine and Piilo (2009).

## Limitations

The certified interval \([1/5,1/2]\) is a sufficient region, **not** an exact threshold or maximal revival region. This theorem proves an existence statement for one of five specified pairs of observation times, not monotonicity or a complete sequence of local extrema. The source paper already provides the general scalar coherence formula, so the contribution is the **new continuum nonmonotonicity inequality and its exact rational certificate**, not a new master equation. The result applies to a single two-level energy gap, with uniform sampling of the complete prior history and ideal Poisson events. Independent scientific review and independent priority validation have not been performed.

## References

1. G. de Mauro, M. Kulkarni and S. N. Majumdar, *Quantum resetting with memory* (submitted August 3, 2026), https://arxiv.org/abs/2608.02297 ; especially the uniform-memory equation and two-level section.
2. F. Carollo and S. Wald, *Stochastic resetting induces quantum non-Markovianity* (submitted January 19, 2026), https://arxiv.org/abs/2601.13367 ; especially the trace-distance contraction and effective-negative-reset comparison.
3. H.-P. Breuer, E.-M. Laine and J. Piilo, *Measure for the Degree of Non-Markovian Behavior of Quantum Processes in Open Systems* (2009), DOI:10.1103/PhysRevLett.103.210401.
4. NIST Digital Library of Mathematical Functions, confluent hypergeometric \({}_1F_1\) series, https://dlmf.nist.gov/13.2 .
