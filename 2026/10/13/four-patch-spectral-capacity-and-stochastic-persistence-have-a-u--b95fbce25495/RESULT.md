# Four-patch spectral capacity and stochastic persistence have a unique ranking reversal
## Finding
The leading eigenvalue of a binary equal-quality habitat connectivity matrix need not rank finite-stochastic metapopulation persistence, even among networks with identical numbers of patches and links. The smallest connected undirected example has four patches and four links.

Define \(P\) as the paw graph with edges
\[
\{01,02,03,12\},
\]
and \(C_4\) as the cycle with edges
\[
\{01,12,23,03\}.
\]
Their adjacency spectral radii satisfy
\[
\rho(P)>2=\rho(C_4).
\]
Nonetheless, for independent patch extinction at rate \(1\) and colonization at rate \(\lambda\) per occupied adjacent neighbor, starting from full occupancy, the exact mean extinction times satisfy
\[
T_P(\lambda)>T_{C_4}(\lambda)\quad(0<\lambda<\alpha),
\]
\[
T_P(\lambda)=T_{C_4}(\lambda)\quad(\lambda=\alpha),
\]
\[
T_P(\lambda)<T_{C_4}(\lambda)\quad(\lambda>\alpha),
\]
where \(\alpha\) is the **unique** positive root of
\[
\begin{aligned}
F(\lambda)={}&648\lambda^9+3504\lambda^8+8486\lambda^7
 +10624\lambda^6+4144\lambda^5\\
&-7529\lambda^4-13801\lambda^3-10608\lambda^2
-4176\lambda-684,
\end{aligned}
\]
and is isolated exactly by
\[
1.079524<\alpha<1.079525.
\]
At the natural rate \(\lambda=2\),
\[
T_{C_4}(2)-T_P(2)=\frac{237101}{648778}>0.
\]
No strict spectral-versus-stochastic persistence ranking disagreement at matched vertex/link counts is possible for fewer than four vertices; among connected four-vertex networks the unique smaller link stratum where two graph types exist, the three-link tree stratum, has matching strict rankings at every positive colonization rate.

## Assumptions and scope
A landscape is a finite connected simple undirected graph with \(n\) labeled patches and \(m\) dispersal links. Species occupancy is Boolean at each patch. At every occupied vertex a local extinction occurs at rate \(1\); at an empty vertex the colonization rate is \(\lambda k\), where \(k\) is its number of occupied neighbors and \(\lambda>0\). All event clocks are independent given the present occupancy state, defining a finite continuous-time Markov chain.

The empty occupancy configuration is absorbing. At time zero all vertices are occupied. Let \(T_G(\lambda)\) be the expected hitting time of the empty configuration. This expectation is finite because each occupied patch can independently go extinct and no positive immigration is supplied externally. Let \(\rho(G)\) denote the largest adjacency eigenvalue. Only landscapes with equal patch number and equal edge number are compared.

The adjacency spectral radius is the relevant **binary, homogeneous** special case of a landscape connectivity spectral measure. The original metapopulation capacity of Hanski and Ovaskainen is a weighted, spatial matrix: our claim does not assert that the weighted quantity or its deterministic threshold universally predicts finite stochastic extinction times.

## Proof
**Absorption-time equations.** For each nonempty occupied set \(S\subseteq V(G)\), let \(t_S\) be its mean time until global extinction; set \(t_{\varnothing}=0\). If \(u\sim v\) denotes adjacency, the backward equation is
\[
\begin{aligned}
1={}&\sum_{v\in S}(t_S-t_{S\setminus\{v\}})\\
 &+\lambda\sum_{v\notin S}|\{u\in S:u\sim v\}|(t_S-t_{S\cup\{v\}}).
\end{aligned}
\]
For \(n=4\), this is a nonsingular \(15\times15\) linear system over \(\mathbb Q(\lambda)\). Nonsingularity for positive rates follows from transience of every nonempty state. Invariant partitions of these states under graph automorphisms yield equivalent systems of sizes \(11\) for \(P\), \(5\) for \(C_4\), \(7\) for the four-vertex star, and \(9\) for the four-vertex path. Cramer's rule and exact polynomial expansion give the rational formulas below; `verify_metapop_spectral_discordance.py` independently constructs the generator and verifies each polynomial cross-multiplication rather than trusting only numerical values.

**Paw and cycle formulas.** Define
\[
\begin{aligned}
D_P(\lambda)={}&162\lambda^7+806\lambda^6+1857\lambda^5
 +2618\lambda^4\\
&+2412\lambda^3+1416\lambda^2+480\lambda+72,
\end{aligned}
\]
\[
\begin{aligned}
N_P(\lambda)={}&324\lambda^{10}+2556\lambda^9
 +9919\lambda^8+25760\lambda^7\\
&+48131\lambda^6+65654\lambda^5+65563\lambda^4\\
&+46968\lambda^3+22806\lambda^2+6696\lambda+900.
\end{aligned}
\]
Then
\[
T_P(\lambda)=\frac{N_P(\lambda)}{6D_P(\lambda)},
\qquad
T_{C_4}(\lambda)=
\frac{8\lambda^4+24\lambda^3+42\lambda^2+61\lambda+25}{4(5\lambda+3)}.
\]
Direct exact subtraction factors as
\[
T_{C_4}(\lambda)-T_P(\lambda)
=
\frac{\lambda^2 F(\lambda)}{12(5\lambda+3)D_P(\lambda)}.
\]
Every coefficient of \(D_P\) is positive. The descending coefficients of \(F\) exhibit exactly one sign change; thus Descartes' rule permits at most one positive root, and its constant term is negative while its leading term is positive. Therefore precisely one positive root exists. Direct integer evaluation at the rational endpoints \(1079524/10^6\) and \(1079525/10^6\) has opposite signs, proving the displayed isolating interval. The sign of the extinction-time difference follows for every positive rate. At \(\lambda=2\), the exact values are
\[
T_P(2)=\frac{1182381}{99812},
\qquad
T_{C_4}(2)=\frac{635}{52},
\]
so the stated positive difference follows.

**Spectral ranking.** The characteristic polynomial of \(C_4\) is \(x^2(x^2-4)\), so its adjacency spectral radius is \(2\). The characteristic polynomial of \(P\) is
\[
(x+1)(x^3-x^2-3x+1).
\]
The cubic is negative at \(x=2\) and positive at \(x=3\); its largest real root exceeds \(2\). Consequently the paw has the strictly greater adjacency spectral radius.

**The three-link comparison.** With four vertices and three links, the only connected graph types are the star and the path. The star has spectral radius \(\sqrt3\), while the path has spectral radius \(2\cos(\pi/5)<\sqrt3\). The corresponding exact extinction-time formulas are
\[
T_{\mathrm{star}}=
\frac{9\lambda^6+60\lambda^5+193\lambda^4+439\lambda^3+554\lambda^2+331\lambda+75}{6(\lambda+1)(3\lambda+2)(4\lambda+3)},
\]
\[
T_{\mathrm{path}}=
\frac{12\lambda^8+100\lambda^7+427\lambda^6+1280\lambda^5+2628\lambda^4+3527\lambda^3+2961\lambda^2+1424\lambda+300}{2(4\lambda^2+9\lambda+6)(12\lambda^3+31\lambda^2+32\lambda+12)}.
\]
Their difference factors as
\[
T_{\mathrm{star}}-T_{\mathrm{path}}
=
\frac{\lambda^2 B(\lambda)}{6(\lambda+1)(3\lambda+2)(4\lambda+3)(4\lambda^2+9\lambda+6)(12\lambda^3+31\lambda^2+32\lambda+12)},
\]
where
\[
\begin{aligned}
B(\lambda)={}&324\lambda^8+2595\lambda^7+8941\lambda^6+17676\lambda^5\\
&+22477\lambda^4+19319\lambda^3+11195\lambda^2+4032\lambda+684.
\end{aligned}
\]
Every coefficient in the numerator and denominator is positive. Thus the star has strictly longer persistence for every \(\lambda>0\), consistent with its larger spectral radius.

**Sharp minimality.** Enumerating all simple graphs on at most four vertices and identifying graphs modulo vertex permutation gives one connected isomorphism type in every nonempty fixed-\((n,m)\) class for \(n\le3\); for \(n=4\) it gives exactly two types at \(m=3\), exactly two at \(m=4\), and one each at \(m=5,6\). Because the three-link comparison cannot disagree, the four-link paw/cycle pair is simultaneously minimal in patch count and, at the first such patch count, dispersal-link count. This completes the proof.

## Verification
The standalone `verify_metapop_spectral_discordance.py` is self-contained, uses only Python's standard library, and prints `VERIFY_OK` on success. Run:

`python3 verify_metapop_spectral_discordance.py`

For each graph it constructs the exact continuous-time generator, proves that the automorphism orbit partition is a strong lumping by checking rates from every representative state, evaluates the relevant polynomial determinant with exact integer-coefficient subset dynamic programming, and checks the closed absorption-time formula by symbolic polynomial identity. It independently solves the full uncompressed fifteen-state system with rational Gaussian elimination at three positive rates. It also checks the two difference factorizations, characteristic polynomials, positive-coefficient arguments, rational root bracket, example value, and connected graph isomorphism census.

The symbolic determinant identity, not finite numerical sampling, verifies the closed rational functions for **all** \(\lambda>0\). The final sign argument uses an exact polynomial with one Descartes sign change, not a plotted curve.

## Relationship to prior work
Hanski and Ovaskainen (2000) introduced the metapopulation capacity of a fragmented landscape as the leading eigenvalue of a spatially weighted matrix, motivating an ecological landscape-capacity proxy. Their deterministic occupancy-equation threshold does not assert a universal comparison with the **fully finite** continuous-time stochastic mean extinction time under the binary neighboring-patch model.

Frank (2005) explicitly showed that introducing stochasticity can alter ecological persistence rankings across heterogeneous landscapes. Therefore neither the **possibility of rank disagreement in general** nor a claim that spectral scores are universally trustworthy is new. Her published abstract does not specify the four-patch paw/cycle equal-budget first example or its exact one-parameter rate crossing; inspection of the article body was not obtained.

Van de Bovenkamp and Van Mieghem (2015) derived exact SIS survival times for complete and star graphs and discussed the difficulty of cross-topology comparisons. Holme and Tupikina (2018), inspected in full, already computed exact SIS extinction-time functions for all connected three-to-eight-vertex graphs and compared numerous same-graph initial configurations. They did **not** publish the per-graph full rational functions or a theorem comparing **the spectral-capacity ranking across two different graphs of equal order and size** with the specific unique paw/cycle crossover and graph-order sharpness. The computation of raw small-graph absorption times is accordingly prior coverage, not itself a novelty assertion here.

The new assertion is the proved sharp minimal mismatch and its unique exact crossover, with a closed algebraic certificate under matched patch/link budgets. This is a special-purpose finite result, not a universal spectral ordering theorem.

## Limitations
This theorem assumes homogeneous patch quality, undirected binary links, local extinction rate one, per-neighbor colonization, Markovian independent clocks, and initially full occupancy. Other initial sets, unequal habitats, directed or weighted dispersal, correlated extinctions, immigration, and nonlinear colonization are outside its scope. The original spatially weighted metapopulation-capacity formulation need not literally reduce to a binary graph without extra equal-quality/connectivity assumptions.

The original work on ecological stochasticity already establishes qualitative ranking changes, and later studies compute SIS lifetimes for all small graphs; the claim does **not** seek priority for either broad fact. An article not available in complete readable form could still contain this particular four-patch comparison or an equivalent threshold without indexing. There is no independent audit of the result.

## References
1. I. Hanski and O. Ovaskainen, “The metapopulation capacity of a fragmented landscape,” *Nature* 404, 755–758 (2000), DOI: 10.1038/35008063. First published 13 April 2000.
2. O. Ovaskainen and I. Hanski, “Spatially structured metapopulation models: global and local assessment of metapopulation capacity,” *Theoretical Population Biology* 60, 281–302 (2001), DOI: 10.1006/tpbi.2001.1548.
3. K. Frank, “Metapopulation persistence in heterogeneous landscapes: lessons about the effect of stochasticity,” *The American Naturalist* 165, 374–388 (2005), DOI: 10.1086/428293. First published online 3 February 2005.
4. R. van de Bovenkamp and P. Van Mieghem, “Survival time of the susceptible-infected-susceptible infection process on a graph,” *Physical Review E* 92, 032806 (2015), DOI: 10.1103/PhysRevE.92.032806.
5. P. Holme and L. Tupikina, “Epidemic extinction in networks: insights from the 12,110 smallest graphs,” *New Journal of Physics* 20, 113042 (2018), DOI: 10.1088/1367-2630/aaf016; preprint arXiv:1802.08849 first posted 24 February 2018.
