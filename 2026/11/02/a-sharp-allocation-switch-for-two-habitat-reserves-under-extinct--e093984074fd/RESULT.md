# A sharp allocation switch for two habitat reserves under extinction and rescue

## Finding

Let a fixed total area \(A>0\) be divided between two reserves of areas \(x\) and \(A-x\), with \(0<m<A/2\) and \(m\le x\le A-m\). Each occupied reserve goes locally extinct at rate \(\theta\) divided by its area, where \(\theta>0\). An occupied reserve recolonizes the other, when empty, at rate \(\beta\) times the recipient reserve's area, with \(\beta>0\). The completely empty state is absorbing, and both reserves are occupied initially.

For \(z=x(A-x)\), the exact expected time to total extinction is

\[
T(x)=\frac{1}{\theta}\left(A-\frac{z}{A}+\frac{\beta z^2}{A\theta}\right).
\]

Define \(z_-=m(A-m)\), \(z_+=A^2/4\), and the critical rescue coefficient

\[
\beta_c=\frac{\theta}{z_-+z_+}.
\]

The **complete global optimal allocation** over \([m,A-m]\) is:

1. For \(0<\beta<\beta_c\), only the two maximally unequal allocations \(x=m\) and \(x=A-m\) are optimal.
2. For \(\beta=\beta_c\), exactly the three allocations \(x=m\), \(x=A/2\), and \(x=A-m\) tie for the global maximum.
3. For \(\beta>\beta_c\), the unique optimum is the equal split \(x=A/2\).

The exact difference between the equal and maximally unequal allocations is

\[
T(A/2)-T(m)=\frac{z_+-z_-}{A\theta}
\left[\frac{\beta}{\theta}(z_++z_-)-1\right].
\]

Consequently the preferred allocation changes discontinuously at a single positive rescue threshold, not by a gradual interior movement of the optimizer. A further local feature is that both the equal and maximally unequal allocations are strict local maxima whenever

\[
\frac{\theta}{2z_+}<\beta<\frac{\theta}{2z_-};
\]

thus competing local optima coexist around the global switch.

## Assumptions and scope

The continuous-time Markov chain has occupancy states \(11,10,01,00\), with the digit 1 indicating an occupied reserve and \(00\) absorbing. An occupied patch of area \(s\) becomes empty at rate \(\theta/s\). An occupied source patch recolonizes an empty recipient of area \(s\) at rate \(\beta s\), independent of source area. Every possible event is represented by an independent exponential clock; simultaneous events have probability zero. There is no exogenous immigration, habitat loss, recovery delay, demographic size within an occupied patch, spatial distance effect, or correlated catastrophe. Every parameter \(A,\theta,\beta\) is strictly positive, and the minimum reserve size satisfies \(0<m<A/2\). The objective is the expected time to the first visit to \(00\), starting exactly in \(11\). At any feasible allocation the mean is finite.

This result concerns a deliberately elementary ecological benchmark, not a general recommendation for real conservation reserves. In particular, \(\theta/s\) and \(\beta s\) are modeling assumptions rather than universally observed area laws.

## Proof

Put \(y=A-x\), and abbreviate the extinction and rescue rates by

\[
u=\theta/x,\quad v=\theta/y,\quad c=\beta y,\quad d=\beta x.
\]

Let \(T_{ij}\) be the expected hitting time of state \(00\), starting in state \(ij\). First-step conditioning of the finite Markov chain gives

\[
\begin{aligned}
(u+c)T_{10}-cT_{11}&=1,\\
(v+d)T_{01}-dT_{11}&=1,\\
(u+v)T_{11}-vT_{10}-uT_{01}&=1.
\end{aligned}
\]

Here \(10\) loses its occupied first reserve at rate \(u\), and \(01\) loses its second reserve at rate \(v\); state \(11\) loses its first reserve at rate \(u\), entering \(01\), or its second at rate \(v\), entering \(10\). Since all extinction rates are positive, extinction is reached almost surely in finite mean time.

Eliminating \(T_{10}\) and \(T_{01}\) yields the exact rational identity

\[
T_{11}=\frac{(u+c)(v+d)+v(v+d)+u(u+c)}{uv(u+v+c+d)}.
\]

Substituting the four area-dependent rates and using \(z=xy\), \(x+y=A\), gives

\[
T_{11}=\frac{A}{\theta}-\frac{z}{A\theta}
+\frac{\beta z^2}{A\theta^2}=T(x).
\]

As \(x\) ranges over \([m,A-m]\), the product \(z=x(A-x)\) ranges over the entire interval \([z_-,z_+]\), with the lower endpoint attained exactly at \(x=m,A-m\) and the upper endpoint exactly at \(x=A/2\). The polynomial

\[
f(z)=\frac{A}{\theta}-\frac{z}{A\theta}
+\frac{\beta z^2}{A\theta^2}
\]

satisfies \(f''(z)=2\beta/(A\theta^2)>0\). A strictly convex function on a nondegenerate compact interval attains its maximum only at endpoints. Subtracting the endpoint values factorizes as

\[
f(z_+)-f(z_-)=\frac{z_+-z_-}{A\theta}
\left(\frac{\beta}{\theta}(z_++z_-)-1\right).
\]

Since \(z_+>z_->0\), the sign changes exactly at \(\beta_c=\theta/(z_-+z_+)\). This proves the complete three-regime classification and strictness away from the reported optimizers.

For the local-maxima assertion, \(f'(z)=(2\beta z-\theta)/(A\theta^2)\). The boundary allocations are strict one-sided local maxima when \(f'(z_-)<0\), equivalently \(\beta<\theta/(2z_-)\). The central allocation, at the maximum of \(z(x)\), is a strict local maximum when \(f'(z_+)>0\), equivalently \(\beta>\theta/(2z_+)\). These inequalities overlap because \(z_-<z_+\), proving the stated local-optimum coexistence. All conclusions follow analytically for every admissible real parameter tuple.

## Verification

The included standalone `VERIFY.py` uses only the Python standard library and performs exact-rational Gaussian elimination on the independently written transient-state generator; it compares the resulting absorption time against the closed formula at many exact parameter values. It checks endpoint symmetry, strict optimum classifications on parameter grids, the threshold, and the difference identity. Run `python VERIFY.py` from the package directory. A complete run prints `VERIFY_OK assertions=73158`.

For example, take \(A=4\), \(m=1\), \(\theta=1\). Then \(z_-=3\), \(z_+=4\), and \(\beta_c=1/7\). At \(\beta=1/8\), the asymmetric allocation gives \(T(1)=113/32>7/2=T(2)\); at \(\beta=1/7\), both give \(25/7\); at \(\beta=1/6\), the equal split gives \(11/3>29/8=T(1)\). These are exact finite examples; they are not used to infer the universal result, which follows from the proof.

## Relationship to prior work

Etienne and Heesterbeek (2000) study reserve size and number under fixed total area, using extinction time and a patch-dynamic framework. Their published abstract explicitly formulates varying the number and common circular reserve size, rather than fixing two reserves and optimizing a continuously unequal division. Hernández-Suárez, Marquet and Velasco-Hernández (1999), whose full article was inspected, provide an extinction-time treatment of identical-patch stochastic occupancy models, not the present heterogeneous two-area optimization. Day and Possingham (1995) already give a heterogeneous-patch binary-state transition-matrix framework, using discrete extinction and colonization phases; their full publicly indexed text considers area heterogeneity and compares sample landscapes, but does not establish the stated continuous-time, two-area global switching threshold. Etienne (2000) considers heterogeneous patch sizes and rescue in a Levins model, another related but distinct mean-field framework. Ovaskainen (2002) studies the conservation trade-off in the number and size of patches. Frank and Wissel (2002) develop a metapopulation-lifetime approximation for heterogeneous landscapes, a related but different optimization framework.

An existing fixed-rate two-patch result optimizes directional recolonization rates under a fixed colonization budget while holding both extinction rates fixed. Here the extinction rates and recolonization rates change *jointly* with the area allocation. That fixed-extinction optimizer does not imply the present global comparison: in the low-rescue regime the optimum is deliberately unequal even though rescue-only allocation would favor symmetry. The new contribution assessed here is the explicit exact area-coupled extinction time and complete switching classification, not finite-state Markov hitting-time methodology itself.

## Limitations

This is a mathematical statement within the stated four-state continuous-time model. Different extinction-area exponents, dispersal-distance effects, unequal propagule production, environmental correlation, different starting occupancy, reserve acquisition cost, or demographic heterogeneity may change the optimum. No empirical calibration is made. Exact historical priority remains uncertain because the full texts of several plausibly related reserve-design and heterogeneous-lifetime papers were unavailable; the fact that their accessible descriptions do not state the same optimization is not a proof of novelty. No independent audit has been performed.

## References

1. R. S. Etienne and J. A. P. Heesterbeek, “On optimal size and number of reserves for metapopulation persistence,” *Journal of Theoretical Biology* 203 (2000), 33–50. DOI: 10.1006/jtbi.1999.1060. https://pubmed.ncbi.nlm.nih.gov/10677275/
2. C. M. Hernández-Suárez, P. A. Marquet and J. X. Velasco-Hernández, “Threshold parameters and metapopulation persistence,” *Bulletin of Mathematical Biology* 61 (1999), 341–353. DOI: 10.1006/bulm.1998.0084. Full text: https://marquet.cl/wp-content/uploads/2016/10/45_hernandez_suarez_et_al_1999.pdf
3. O. Ovaskainen, “Long-term persistence of species and the SLOSS problem,” *Journal of Theoretical Biology* 218 (2002), 419–433. https://pubmed.ncbi.nlm.nih.gov/12384046/
4. K. Frank and C. Wissel, “A formula for the mean lifetime of metapopulations in heterogeneous landscapes,” *American Naturalist* 159 (2002), 530–552. DOI: 10.1086/338991. https://pubmed.ncbi.nlm.nih.gov/18707435/
5. R. S. Etienne and J. A. P. Heesterbeek, “Rules of thumb for conservation of metapopulations based on a stochastic winking-patch model,” *American Naturalist* 158 (2001), 389–407. DOI: 10.1086/321986. https://pubmed.ncbi.nlm.nih.gov/18707335/
6. J. R. Day and H. P. Possingham, “A stochastic metapopulation model with variability in patch size and position,” *Theoretical Population Biology* 48 (1995), 333–360. DOI: 10.1006/tpbi.1995.1034. Author-uploaded public text: https://www.researchgate.net/publication/256906366_A_Stochastic_Metapopulation_Model_with_Variability_in_Patch_Size_and_Position
7. R. S. Etienne, “Local populations of different sizes, mechanistic rescue effect and patch preference in the Levins metapopulation model,” *Bulletin of Mathematical Biology* 62 (2000), 943–958. DOI: 10.1006/bulm.2000.0186. https://pubmed.ncbi.nlm.nih.gov/11016091/
