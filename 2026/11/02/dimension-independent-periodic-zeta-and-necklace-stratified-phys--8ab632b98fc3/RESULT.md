# Dimension-independent periodic zeta and necklace-stratified physical entropy in cyclic Cournot maps

## Finding
For every integer \(n\ge2\) a natural cyclic coordinate extension of a previously studied two-dimensional Cournot example has exactly one ergodic physical invariant probability for each binary necklace of length \(n\). A necklace with \(k\) high coordinates and \(d\) distinct cyclic shifts has basin fraction \(d/2^n\) and metric entropy \((k/n)\log 2\). Yet the number of points fixed by every \(m\)-th iterate is **exactly \(2^m\)**, independent of \(n\), and the uniform fixed-point measures tend to the unique maximal-entropy probability, not to the distribution of typical physical measures.

Writing \(N_n\) for the number of physical probabilities, and \(N_{n,k}\) for those of entropy \((k/n)\log2\),
\[
N_n=\frac1n\sum_{d\mid n}\varphi(d)2^{n/d},\qquad
N_{n,k}=\frac1n\sum_{d\mid\gcd(n,k)}\varphi(d)\binom{n/d}{k/d}.
\]
The full periodic-point and entropy formulas are
\[
\#\operatorname{Fix}(F_n^m)=2^m,\quad
\zeta_{F_n}(z)=\exp\!\left(\sum_{m\ge1}\frac{2^mz^m}{m}\right)=\frac1{1-2z},\quad
h_{\rm top}(F_n)=\log 2.
\]

## Assumptions and scope
Let \(I=[0,1]\), \(c=1/2\), and \(J=[1/2,1]\). Define the continuous piecewise-affine map
\[
g(t)=\begin{cases}
1/4+t/2,&0\le t\le1/2,\\
2t-1/2,&1/2\le t\le3/4,\\
5/2-2t,&3/4\le t\le1.
\end{cases}
\]
For every integer \(n\ge2\), the map \(F_n:I^n\to I^n\) is
\[F_n(x_1,\ldots,x_n)=(g(x_n),x_1,\ldots,x_{n-1}).\]
The source paper's Example 10.3 gives precisely \(g\) and the two-dimensional map \(F_2\), and its Open Problem 5 asks for higher-dimensional cyclic Cournot-map analysis. Here all links but one are identities; no assertion is made about arbitrary reaction functions.

Let \(\lambda\) be normalized one-dimensional Lebesgue probability on \(J\), and \(\delta_c\) the unit atom at \(c\). For a binary word \(s\in\{0,1\}^n\) write \(\rho_s=\bigotimes_{i=1}^n\rho_{s_i}\) with \(\rho_0=\delta_c\), \(\rho_1=\lambda\). Cyclic rotation of words is \(R\), its orbit (necklace) is \([s]\), the orbit length is \(d(s)\), and the number of ones is \(k(s)\). Define
\[\mu_{[s]}=\frac1{d(s)}\sum_{j=0}^{d(s)-1}\rho_{R^j s}.\]
A physical probability is an invariant probability whose empirical-time-average basin has positive \(n\)-dimensional Lebesgue measure. Entropy is Kolmogorov–Sinai entropy with natural logarithms. For each necklace, the basin has *normalized* Lebesgue mass \(d(s)/2^n\); all other basins have zero volume. The unique measure of maximal entropy is \(\lambda^{\otimes n}\).

## Proof
**1. Two one-dimensional statistical regimes.** On \([0,c)\), the first branch is a strict affine contraction toward \(c\): \(g^m(t)=c+2^{-m}(t-c)\). On \(J\), the map is the full two-branch tent map with slopes \(+2\) and \(-2\). Thus \(g_*\lambda=\lambda\), the tent map is exact/mixing for \(\lambda\), and a.e. point of \(J\) is generic for \(\lambda\). Its \(k\)-fold Cartesian product is mixing with respect to \(\lambda^{\otimes k}\). In particular \(F_n^n=(g,\ldots,g)\).

**2. Physical measures and exact basins.** A point not lying on a coordinate boundary \(x_i=c\) has a binary low/high word determined by whether \(x_i<c\) or \(x_i>c\). The first branch preserves low coordinates, while the tent branch preserves high coordinates; each application of \(F_n\) rotates this word. Along every \(n\)-th iterate, low coordinates converge to \(c\), and the high-coordinate Cartesian tent map is mixing. Consequently, for Lebesgue-a.e. point with word \(s\), the empirical averages along the subsequence of times divisible by \(n\) converge to \(\rho_s\); averages along times congruent to \(j\) modulo \(n\) converge to \(\rho_{R^j s}\). Averaging all phases gives \(\mu_{[s]}\). Each open pattern cell has volume \(2^{-n}\), and the different words in a necklace have disjoint interiors; therefore the full physical basin of \(\mu_{[s]}\), modulo null sets, is precisely the union of its \(d(s)\) pattern cells. The cells partition full volume. Different necklace measures are distinct: their restrictions to interiors of the corresponding coordinate faces differ. No other invariant probability can have a positive-volume empirical basin.

Every \(\rho_s\) is mixing under \(F_n^n\), because its positive-coordinate dynamics is a Cartesian product of full tent maps and its fixed coordinates are \(c\). The map \(F_n\) cyclically permutes these mixing components. Hence their averaged measure \(\mu_{[s]}\) is invariant and ergodic. The entropy identity \(h_{\mu}(F_n^n)=n h_{\mu}(F_n)\), the product entropy formula, and \(h_{\lambda}(g)=\log2\) give \(h_{\mu_{[s]}}(F_n)=(k(s)/n)\log2\). The mixed necklaces have a cyclic factor of period greater than one and are ergodic but not mixing; the all-high measure is mixing.

The action of cyclic rotations on \(\{0,1\}^n\) yields the two necklace formulas in the Finding by Burnside's lemma. If the initial state is distributed uniformly on the cube, its low/high word consists of independent fair binary variables. Thus the selected measure's entropy has the exact law \((\log2/n)K\), with \(K\) binomial of parameters \(n,1/2\). The mean entropy is \(\tfrac12\log2\) for every dimension, whereas the maximal entropy is \(\log2\); the entropy variance is \((\log2)^2/(4n)\).

**3. Periodic-point count.** Every periodic point lies in \(J^n\), since a coordinate strictly below \(c\) approaches \(c\) along the subsequence of iterations divisible by \(n\) and cannot be periodic. On \(J\), the inverse branches of \(g\) are
\[\phi_0(t)=1/4+t/2,\qquad \phi_1(t)=5/4-t/2.\]
The two full inverse branches of \(F_n|_{J^n}\) are
\[\Psi_b(y_1,\ldots,y_n)=(y_2,\ldots,y_n,\phi_b(y_1)),\qquad b\in\{0,1\}.\]
For every word \(w\in\{0,1\}^m\), its inverse-branch composition \(\Psi_w\) has a strict contraction power: after \(n\) repetitions, each coordinate has passed through exactly \(m\) affine inverse tent branches, and \(\operatorname{Lip}(\Psi_w^n)\le2^{-m}\) in the sup norm. Banach's theorem yields exactly one fixed point of \(\Psi_w\), which is fixed by \(F_n^m\). Conversely, a point fixed by \(F_n^m\) specifies a unique length-\(m\) branch itinerary, except potentially on a critical preimage. No periodic point meets the critical level \(3/4\), since its forward scalar itinerary would pass through \(1\) to the absorbing fixed point \(c\). Consequently the \(2^m\) words give exactly \(2^m\) *distinct* fixed points, proving the zeta identity.

**4. Equidistribution and maximal entropy.** Let \(u_m\) be the normalized uniform atomic probability on \(\operatorname{Fix}(F_n^m)\). A uniformly chosen length-\(m\) inverse word has fixed point \(p_w\) and maps any predetermined \(z\in J^n\) to \(\Psi_w(z)\). As \(m\to\infty\), the distance between these two points is uniformly bounded by the diameter of \(J^n\) times \(2^{-\lfloor m/n\rfloor}\). The random inverse-branch Markov operator \(\frac12(\Psi_0)_*+\frac12(\Psi_1)_*\) preserves \(\lambda^{\otimes n}\): replacing a uniform \(J\) coordinate by an equiprobable inverse tent branch again gives a uniform \(J\) coordinate, independent of the other coordinates. Every \(n\) random inverse steps contract the sup norm by at least \(1/2\), hence this stationary probability is unique and the pushforward of any point mass tends to it. Therefore \(u_m\Rightarrow\lambda^{\otimes n}\).

Finally, the tent subsystem has \(h_{\rm top}(g)=\log2\); the lower attracting branch adds no topological entropy. By the product rule and \(F_n^n=g^{\times n}\), \(h_{\rm top}(F_n)=\log2\). The full-branch tent map has unique measure of maximal entropy \(\lambda\); its \(n\)-fold product has unique maximal-entropy probability \(\lambda^{\otimes n}\) (equivalently, the independent fair Bernoulli inverse-branch process). Any \(F_n\)-invariant measure of entropy \(\log2\) would be a maximal-entropy measure for \(F_n^n\), forcing that same product. Thus \(\lambda^{\otimes n}\) is the unique maximal-entropy measure for \(F_n\).

## Verification
Run `python3 verify_cyclic_cournot.py` with Python 3 and NumPy. It checks, for dimensions \(2\le n\le8\), Burnside necklace counts, basin mass partitions, binomial entropy means, and for \(1\le m\le6\) constructs every inverse-word fixed point and tests its exact-period-dividing-\(m\) identity numerically. The infinite-dimensional-in-\(n\) classification is proved above, not inferred from this bounded test.

## Relationship to prior work
García Guirao, *Connected omega-limit sets of Cournot maps* (arXiv:2610.27229, first posted 2026-10-19), Example 10.3, supplies the explicit one-dimensional map \(g\) and establishes the positive-area L-shaped omega-limit sets for \(n=2\). Its Open Problem 5 requests extensions of the omega-limit theory to higher-dimensional cyclic coordinate maps. Neither its stated examples nor the inspected arguments give the all-dimensional necklace-indexed physical probabilities, their exact metric entropies and basin masses, or a dimension-independent periodic zeta and fixed-point equidistribution. Earlier Linero-Bas–Muñoz-Guillermo (2021) studies omega-limit geometry in dimension two, rather than this all-dimensional statistical and periodic-point theorem. The statement is limited to the very explicit cyclic map above and does not solve the full generality of the open problem.

## Limitations
The result determines positive-volume basins only up to Lebesgue-null exceptional sets; exotic invariant probabilities and atypical orbits can exist on the tent repeller. The normalized Lebesgue product on \(J^n\) is the *unique maximal-entropy* measure, not the only invariant measure. Equidistribution of all fixed points is an asymptotic weak-convergence assertion. This special family has identity reaction functions at all but one link; no classification is claimed for arbitrary multidimensional Cournot maps. Historical priority beyond the inspected sources remains provisional. Numerics do not replace the exact inverse-branch proof.

## References
1. J. L. García Guirao, *Connected omega-limit sets of Cournot maps: periodic orbits, realization and almost every point*, arXiv:2610.27229 (2026), especially Example 10.3 and Open Problem 5.
2. A. Linero-Bas and M. Muñoz-Guillermo, *A Full Description of Omega-Limit Sets of Cournot Maps Having Non-Empty Interior and Some Economic Applications*, Mathematics 9 (2021), 452, DOI:10.3390/math9040452.
3. Standard full-tent-map facts: its normalized Lebesgue invariant probability is exact and has entropy \(\log2\), with two independent inverse branches.
