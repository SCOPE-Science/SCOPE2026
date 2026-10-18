# Minimal two-bath Kawasaki ring: exact local-order boundary and heat current

## Finding

For the four-site, zero-magnetization, ferromagnetic Ising ring under the two-reservoir Metropolis–Kawasaki process defined below, let \(q=e^{-4J/T_c}\) be the uphill acceptance at the three cold bonds and \(p=e^{-4J/T_h}\) the acceptance at the one hot bond, with Boltzmann's constant set to one. Assume \(J>0\), \(0<q\le p\le1\), \(0<T_c\le T_h\le\infty\). Write

\[
D=p(1+q)+3q+q^2.
\]

The stationary nearest-neighbor correlation at the hot bond and at its opposite bond is

\[
C_h=\frac{p(1-q)-q(1+q)}{D},
\]

whereas the two remaining cold bonds have

\[
C_c=\frac{q(1-q)-p(1+q)}{D}<0.
\]

In particular, positive alignment at the **heated** bond is possible exactly in the region

\[
q<\sqrt2-1,\qquad p>\frac{q(1+q)}{1-q}.
\]

Equality produces zero hot-bond correlation. For fixed \(q\), increasing \(p\) increases \(C_h\) strictly, since \(\partial_p C_h=4q/D^2>0\). Yet the energy inflow from the hot reservoir and the total steady-state entropy-production rate are

\[
\mathcal J_h=\frac{4Jq(p-q)}{D},\qquad
\dot S_{\rm tot}=\frac{q(p-q)\log(p/q)}{D}.
\]

Thus every strict thermal contrast \(p>q\) creates positive dissipation, while local ferromagnetic alignment requires a separate, sharp threshold. At \(p=q\), the process is equilibrium, has zero dissipation, and all four bonds have correlation \(-q/(2+q)\). The four-site ring is the smallest ordinary cycle with conserved spin-exchange dynamics for which a thermal contrast can affect transition rates: all two- and three-site fixed-magnetization Ising sectors have constant energy.

For the infinite-temperature hot bath \(p=1\), the entropy-production rate has exactly one maximum in \(0<q<1\), at \(q=0.130018772243409\ldots\). This maximum lies strictly inside the region \(C_h>0\). This is a finite-size correlation sign boundary, **not** a thermodynamic phase transition.

## Assumptions and scope

Label the four ring sites \(0,1,2,3\), with spins \(s_i\in\{-1,+1\}\), periodic indexing, and the constraint \(\sum_i s_i=0\). The energy is

\[
H(s)=-J\sum_{i=0}^3s_i s_{i+1},\qquad J>0.
\]

At each edge \((i,i+1)\), an independent rate-one Poisson clock attempts to exchange unequal neighboring spins. The exchange is accepted at rate \(1\) for a nonpositive energy change and at rate \(e^{-\Delta H/T_i}\) for a positive energy change. Edge \((0,1)\) has temperature \(T_h\); edges \((1,2),(2,3),(3,0)\) have temperature \(T_c\). The case \(T_h=\infty\) means accepting all attempted exchanges at the hot edge. The stated rates and entropy production use **one attempt per edge per unit time**, not a single attempt for the entire ring.

All stationary quantities refer to the unique stationary distribution at \(q>0\). No claim is made at zero cold temperature, where irreducibility can fail. The total entropy-production rate is in units of the Boltzmann constant per unit time.

## Proof

**Step 1: exact finite state reduction.** The six allowed configurations form three global-spin-reversal pairs:

\[
\begin{aligned}
A&=\{(++--),(--++)\},\\
B&=\{(+-+-),(-+-+)\},\\
C&=\{(+--+),(-++-)\}.
\end{aligned}
\]

The configurations in \(A\) and \(C\) have energy zero; those in \(B\) have energy \(4J\). Directly swapping adjacent unequal spins shows that, after aggregating by these pairs, the only transition rates are

\[
A\xrightarrow{2q}B,\quad B\xrightarrow{2}A,
\qquad C\xrightarrow{p+q}B,\quad B\xrightarrow{2}C.
\]

Global reversal preserves all transition rates, and adjacent swaps connect all six configurations when \(p,q>0\); hence the stationary measure is unique and constant on each displayed pair. Denote the probability of **each individual** configuration in \(A,B,C\) by \(a,b,c\), respectively. Balancing flows between the three pairs gives

\[
b=qa,\qquad (p+q)c=2b,\qquad 2(a+b+c)=1.
\]

Therefore

\[
a=\frac{p+q}{2D},\qquad
b=\frac{q(p+q)}{2D},\qquad
c=\frac{q}{D}.
\]

These probabilities satisfy all six original master equations, not merely the aggregated equations; this follows from the spin-reversal symmetry and the explicit pair-to-pair edges, and is directly checked in the standalone verification program.

**Step 2: local correlations.** The hot edge \((0,1)\) and opposite edge \((2,3)\) have aligned spins exactly in pair \(A\), so their correlation is \(4a-1\). The other two edges have aligned spins exactly in pair \(C\), so their correlation is \(4c-1\). Substitution gives the stated rational formulas. Since \(p\ge q>0\),

\[
q(1-q)-p(1+q)\le -2q^2<0,
\]

so \(C_c<0\). Meanwhile \(C_h>0\) if and only if \(p(1-q)>q(1+q)\). With \(p\le1\), that inequality is attainable if and only if \(q^2+2q-1<0\), or \(q<\sqrt2-1\). Differentiation gives \(\partial_p C_h=4q/D^2\). Direct substitution at \(p=q\) gives the equilibrium correlation on all edges.

**Step 3: heat and dissipation.** The only hot-edge energy-increasing transitions are the two transitions from pair \(C\) into pair \(B\), each with rate \(p\), and their reverses from \(B\) to \(C\) each have rate one. The stationary net uphill event flux across the hot bond equals

\[
2cp-2b=\frac{q(p-q)}{D}.
\]

Each such event transports energy \(4J\) from the hot reservoir into the spin system, proving the formula for \(\mathcal J_h\). Stationarity makes the cold-reservoir heat flux equal to \(-\mathcal J_h\). Because \(\log(p/q)=4J(1/T_c-1/T_h)\), the reservoir entropy production is

\[
\mathcal J_h\left(\frac1{T_c}-\frac1{T_h}\right)
=\frac{q(p-q)\log(p/q)}{D}.
\]

This is strictly positive if \(p>q\), and zero at \(p=q\). The derivation includes the limiting case \(1/T_h=0\).

**Step 4: minimal size.** On a three-site cycle, any configuration with one spin differing from the other two has exactly two disagreeing edges, independent of the minority spin's position. Likewise, each fixed-magnetization two-site sector has constant energy. Thus all allowed Kawasaki moves on smaller ordinary cycles are energy-neutral and independent of thermal parameters. At four sites and zero magnetization, the pair \(B\) instead lies \(4J\) above pairs \(A,C\), allowing a genuine two-reservoir effect.

**Step 5: the unique infinite-hot-bath dissipation maximum.** Put \(p=1\) and \(F(q)=q(1-q)\log(1/q)/(1+4q+q^2)\). Define \(A(q)=q(1-q)/(1+4q+q^2)\). Then

\[
A'(q)=\frac{1-2q-5q^2}{(1+4q+q^2)^2}.
\]

For \(q\ge q_0=(\sqrt6-1)/5\), \(F'=A'\log(1/q)-A/q<0\). For \(0<q<q_0\), a stationary point obeys

\[
\log(1/q)=\frac{(1-q)(1+4q+q^2)}{1-2q-5q^2}.
\]

The left side decreases strictly from infinity; the right side increases strictly from one to infinity because its derivative is

\[
\frac{5q^4+4q^3+18q^2+4q+5}{(1-2q-5q^2)^2}>0.
\]

There is exactly one stationary point, necessarily the global maximum since \(F\) vanishes at both endpoints. Its indicated decimal value is a numerical approximation of that uniquely characterized root. Finally \(q_0<1/3<\sqrt2-1\), placing the maximum in the strictly positive hot-correlation region.

## Verification

Running `python check.py` with SymPy constructs the full six-state generator independently from the Hamiltonian and Metropolis rule. It confirms the six stationary master equations symbolically, the four pair-correlation identities, the heat flux, the equilibrium reduction and the derivative identities. It separately solves the full six-state rational stationary system for 18 pairs of bath parameters and evaluates Schnakenberg entropy production against the thermodynamic formula. The same program checks the energy degeneracy for smaller cycles and the monotonicity identity used for the unique dissipation maximum. All implemented checks passed. The infinite-parameter statements are proved algebraically above, not inferred from numerical tests.

## Relationship to prior work

Borchers, Pleimling and Zia introduced the spatially partitioned two-temperature Kawasaki–Ising ring and demonstrated the qualitative freezing-by-heating phenomenon, mainly by simulations. Their paper treats the infinitely hot window and does not state the finite-hot-temperature, four-site stationary formulas or the local correlation sign curve above. Borchers' 2015 thesis includes a small-system analysis, specifically a six-site, two-hot-bond example, which is closer to this work than the published paper's large-system plots. That analysis is acknowledged rather than portrayed as absent: it does not supply the distinct four-site, one-hot-bond, two-temperature rational sign and entropy formulas established here.

The exact alternating-temperature Ising results of Schmittmann and Schmüser concern **spin-flip Glauber dynamics**, not conserved Kawasaki exchange. Renklioglu and Yalabik study a **two-dimensional** anisotropic Kawasaki Ising lattice. These results do not directly imply the present finite-ring invariant. The present derivation is elementary finite-state analysis and is not represented as a general solution of the two-temperature Ising model.

## Limitations

The effect proved is a sharp **finite-size** sign change, not a singular phase transition in a thermodynamic limit. The geometry is restricted to the four-site half-filled periodic ring, a single hot bond, and otherwise homogeneous Metropolis exchange rates. For larger rings or different magnetizations, the displayed rational formulas need not hold. Infinite cold-bath inverse temperature is excluded from the theorem. The assertion of originality is limited to the specific primary literature and research-record comparisons documented alongside this result; differently indexed prior calculations may exist. The work has not received independent scientific validation.

## References

1. N. Borchers, M. Pleimling and R. K. P. Zia, *Non-equilibrium statistical mechanics of a two-temperature Ising ring with conserved dynamics*, Phys. Rev. E 90, 062113 (2014), arXiv:1411.6180 (first public version 22 November 2014), https://arxiv.org/abs/1411.6180. DOI:10.1103/PhysRevE.90.062113.
2. N. J. Borchers, *Non-equilibrium Statistical Mechanics of a Two-temperature Ising Ring With Conserved Dynamics*, doctoral dissertation, Virginia Tech, 30 April 2015; particularly Chapter 4, Section 4.4, pp. 52–58, accessible at https://scispace.com/pdf/nonequilibrium-statistical-mechanics-of-a-two-temperature-2lcb77q8tr.pdf.
3. B. Schmittmann and F. Schmüser, *Stationary correlations for a far-from-equilibrium spin chain*, Phys. Rev. E 66, 046130 (2002), arXiv:cond-mat/0212616, https://arxiv.org/abs/cond-mat/0212616.
4. B. Renklioglu and M. C. Yalabik, *Non-equilibrium phase transitions in the two-temperature Ising model with Kawasaki dynamics*, Eur. Phys. J. B 85, 398 (2012), DOI:10.1140/epjb/e2012-30726-5.
