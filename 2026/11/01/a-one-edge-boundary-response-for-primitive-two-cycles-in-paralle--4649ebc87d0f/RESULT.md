# A one-edge boundary response for primitive two-cycles in parallel chip-firing

## Finding
Let \(F_n=K_1\vee P_n\) be the labelled fan graph, formed by joining a hub to every vertex of a path of length \(n-1\), and let \(W_n=K_1\vee C_n\) be the wheel obtained by adding the edge between the path endpoints. Under ordinary synchronous, degree-threshold parallel chip-firing with nonnegative integer chip heights, let \(f_n\) and \(w_n\) count distinct **primitive two-cycle orbits** on these graphs, respectively, with temporal phase rotations identified but no spatial relabelling. For every integer \(n\ge2\), the fan counts have the exact rational generating function
\[
\boxed{\sum_{n\ge2}f_n t^n=\frac{t^2(6-16t^2-7t^3-t^4)}{(1+t)(1-3t-t^2)^2}.}
\]
In particular, \(f_2=6\), \(f_3=30\), \(f_4=128\), \(f_5=525\), \(f_6=2064\), \(f_7=7915\), and \(f_8=29760\). For every \(n\ge3\), opening this single rim edge strictly decreases the two-cycle orbit population, yet the exponential growth constant remains \(\lambda=(3+\sqrt{13})/2\). More precisely,
\[
\boxed{\frac{f_n}{w_n}=1-\frac{2}{\sqrt{13}}+O(n^{-1})\quad(n\to\infty).}
\]
Thus deleting one edge removes an asymptotic fraction \(2/\sqrt{13}\) of the primitive two-cycle orbits. This is an exact global boundary-response law, not an assertion about other periods or transient behavior.

## Assumptions and scope
All graph vertices are labelled. The fan has vertex set \(\{0,1,\ldots,n\}\), path edges \(\{i,i+1\}\) for \(1\le i<n\), and hub edges \(\{0,i\}\) for \(1\le i\le n\). The wheel is defined for \(n\ge3\) by also adding \(\{1,n\}\). The fan case \(n=2\) is the triangle and is included only as the first coefficient. Every vertex with at least its degree in chips sends one chip to each neighbor at each simultaneous update. A primitive two-cycle is a pair of distinct nonnegative integer configurations \(c_0,c_1\) satisfying \(U(c_0)=c_1\) and \(U(c_1)=c_0\). One orbit counts once, regardless of the two possible time origins. Heights are unrestricted in the definition; the proof shows all relevant heights lie below twice their vertex degrees.

## Proof
**1. Exact cut-weight characterization.** For a connected loopless graph \(G\), let \(L_G\) be its Laplacian and let \(s_j(v)\in\{0,1\}\) be the indicator that vertex \(v\) fires in state \(c_j\). The update is \(c_{j+1}=c_j-L_Gs_j\). A two-step return implies \(L_G(s_0+s_1)=0\). Connectedness forces \(s_0+s_1\) to be constant on vertices. Constants zero and two describe fixed states (nobody fires or everybody fires), not primitive two-cycles. Hence a primitive two-cycle has \(s_1=\mathbf1-s_0\). Fix the firing cut \(S=\{v:s_0(v)=1\}\), and put \(k_v=|\{u\sim v:s_0(u)\ne s_0(v)\}|\). During the first update a firing vertex loses exactly \(k_v\) chips and a waiting vertex gains exactly \(k_v\). Both phase requirements hold precisely for
\[
\begin{cases}
 d_v\le c_0(v)\le d_v+k_v-1,&v\in S,\\
 d_v-k_v\le c_0(v)\le d_v-1,&v\notin S.
\end{cases}
\]
Each interval contains \(k_v\) integers (zero if \(k_v=0\)); all its entries are nonnegative. These local choices are independent. Conversely, they produce complementary firing phases and exact two-step return, because every vertex fires once across the two updates. Thus there are precisely \(\prod_v k_v\) primitive periodic states having firing cut \(S\), and the number of primitive two-cycle orbits is
\[
\frac12\sum_{S\subseteq V(G)}\prod_{v\in V(G)}k_v(S).
\]
No infinite search or presumed period classification is involved.

**2. Canonical fan phase.** Each primitive two-cycle has exactly one time phase in which the hub waits. In that phase let \(b_i\in\{0,1\}\) indicate whether rim vertex \(i\) fires, and set \(s=\sum_{i=1}^n b_i\). The hub has \(s\) cut neighbors; rim vertex \(i\) has
\[
q_i=b_i+\sum_{\substack{j\in\{i-1,i+1\}\\1\le j\le n}}\mathbf1_{b_j\ne b_i}.
\]
Therefore the exact number of orbits with rim word \((b_1,\ldots,b_n)\) is \(s\prod_i q_i\). In particular, \(f_n=\sum_{b\in\{0,1\}^n}(\sum_i b_i)\prod_iq_i\). The distinguished waiting phase makes this an orbit count without an extra factor of two.

**3. Transfer matrix with open boundaries.** Index adjacent bits by \((0,0),(0,1),(1,0),(1,1)\). Let
\[
T(z)=\begin{pmatrix}0&1&0&0\\0&0&3z&2z\\1&2&0&0\\0&0&2z&z\end{pmatrix},\quad
E(z)=(0,1,2z,z),\quad
R(z)=(0,2z,1,z)^\mathsf T.
\]
A transition \((a,b)\to(b,c)\) has weight \(z^b[b+\mathbf1_{a\ne b}+\mathbf1_{b\ne c}]\); \(E(z)\) and \(R(z)\) supply the endpoint factors. Consequently
\[
P_n(z)=E(z)T(z)^{n-2}R(z)=\sum_b z^{\sum_i b_i}\prod_iq_i,
\qquad f_n=\left.z\frac{d}{dz}P_n(z)\right|_{z=1}.
\]
Direct inversion of the explicitly displayed four-by-four matrix gives
\[
\sum_{n\ge2}P_n(z)t^n=
\frac{t^2z(t^3z^2+2t^2z^2+5t^2z+8tz+3t+z+4)}{1-tz-6t^2z-(3z+2z^2)t^3-z^2t^4}.
\]
Differentiating with respect to \(z\) and substituting \(z=1\) gives the stated exact fan generating function. This identity is valid as a formal power series and therefore proves all coefficients, including arbitrary \(n\).

**4. Recompute the wheel comparison.** The same local interior transition, now with periodic rather than open rim boundaries, yields \(\operatorname{tr}T(z)^n\) for the weighted rim colorings. Differentiation supplies the hub cut count. Using \(-\log\det(I-tT(z))=\sum_{n\ge1}\operatorname{tr}(T(z)^n)t^n/n\), direct determinant evaluation gives
\[
\sum_{n\ge1}\frac{w_n}{n}t^n
=\left.-z\frac{\partial}{\partial z}\log\det(I-tT(z))\right|_{z=1}
=\frac{t(1+5t+2t^2)}{(1+t)(1-3t-t^2)}.
\]
The formal coefficients below \(n=3\) are not used as wheel-graph claims.

**5. Strict loss and limiting ratio.** Adding an edge can only increase cut-neighbor counts \(k_v(S)\) for each fixed cut \(S\), so the cut-weight characterization proves \(f_n\le w_n\). Strictness follows, for example, from the hub-waiting word with \(b_1=\cdots=b_{n-1}=1\) and \(b_n=0\): all its fan cut counts are positive, and the added closing edge strictly increases two of them. Let \(\rho=(\sqrt{13}-3)/2\); the dominant real pole \(t=\rho\) is double in the fan generating function and simple in the normalized wheel generating function. Their leading singular coefficients are respectively
\[
B_F=\frac{28-5\sqrt{13}}{39},\qquad
B_W=\frac23-\frac{\sqrt{13}}{39},
\]
so \(f_n=B_F n\rho^{-n}(1+O(n^{-1}))\) and \(w_n=B_W n\rho^{-n}(1+o(1))\). The other poles, at \(-1\) and \(-(3+\sqrt{13})/2\), contribute exponentially smaller terms relative to \(n\rho^{-n}\). Algebra gives \(B_F/B_W=1-2/\sqrt{13}\), establishing the asymptotic formula.

## Verification
The standalone program `fan_direct_check.cpp` independently builds each graph and simulates every nonnegative configuration in the necessary box \(0\le c(v)<2d_v\) for \(2\le n\le8\). It checks whether the state returns after two updates without returning after one, then divides the primitive-state count by two. The output `DIRECT_CHECK.txt` contains the exact counts. The separate `fan_transfer_check.py` constructs the transfer matrix symbolically, checks the rational identities, compares its first fourteen coefficients with a direct binary-word sum, and independently reconstructs the wheel comparison. Its output is `SYMBOLIC_CHECK.txt`. These finite computations check implementation and algebra; the proof for all \(n\) is Steps 1–5.

## Relationship to prior work
Jiang's paper *On the Period Lengths of the Parallel Chip-Firing Game* (arXiv:1003.0943, first submitted 2010-03-04) establishes equal firing counts in periodic configurations and general confinement principles, and classifies possible periods for complete multipartite graph families. It does not give the fan's primitive-two orbit population. Levine's *Parallel Chip-Firing on the Complete Graph* (arXiv:0811.2800, first submitted 2008-11-17) treats a complete-graph dynamical model and rotation numbers, not this open-boundary orbit census. Selig's *Combinatorial Aspects of Sandpile Models on Wheel and Fan Graphs* (arXiv:2202.06487) studies the different sink-based Abelian/stochastic sandpile model with grain addition and stabilization; its fan recurrent-configuration enumeration is not an enumeration of primitive two-cycles under synchronous conservative updates. The wheel comparison is recalculated directly in Step 4, and an exact wheel census by itself does not determine the effect of removing the closing edge. The novel claim assessed here is the open-boundary generating function and nonzero limiting one-edge response, not the general equal-firing lemma or the transfer-matrix method.

## Limitations
Only primitive period-two orbits are counted; the theorem does not classify all recurrence, period lengths, transients, chip-total-conditioned distributions, or graph automorphism orbits. No assertion is made that the general cut-weight formula or the underlying transfer-matrix technique is new. Historical equivalence beyond the sources inspected remains possible; a 1992 article on parallel chip-firing was not fully accessible. There is no independent external audit, and finite testing does not replace the symbolic proof.

## References
- T.-Y. Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, arXiv:1003.0943, originally submitted March 4, 2010, https://arxiv.org/abs/1003.0943.
- L. Levine, *Parallel Chip-Firing on the Complete Graph: Devil's Staircase and Poincaré Rotation Number*, arXiv:0811.2800, originally submitted November 17, 2008, https://arxiv.org/abs/0811.2800.
- T. Selig, *Combinatorial Aspects of Sandpile Models on Wheel and Fan Graphs*, arXiv:2202.06487, originally submitted February 14, 2022, https://arxiv.org/abs/2202.06487.
- J. Bitar and E. Goles, *Parallel Chip-Firing Games on Graphs*, Theoretical Computer Science 92 (1992), 291–300 (relevant historical general background; full text not inspected).
