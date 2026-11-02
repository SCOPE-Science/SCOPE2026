# A first-return law makes Crank–Nicolson positivity one-interval on finite irreducible Markov chains

## Finding
Let \(Q\) be the row generator of any finite, irreducible, continuous-time Markov chain on \(n\ge2\) states: \(q_{ij}\ge0\) for \(i\ne j\), \(Q\mathbf 1=0\). No reversibility is assumed. For \(s\ge0\), write
\[
R_s=(I-sQ)^{-1},\qquad C_h=(I-hQ/2)^{-1}(I+hQ/2)=2R_{h/2}-I.
\]
For each state \(i\), put \(a_i=-q_{ii}>0\), and let \(T_i\) denote the **time to first return to state \(i\) after leaving it**: its initial state is selected with probabilities \(q_{ij}/a_i\), \(j\ne i\), and the chain subsequently follows \(Q\) until hitting \(i\). Then for every \(s>0\),
\[
\boxed{(R_s)_{ii}=\frac{1}{1+a_i\,\mathbb E[s(1-e^{-T_i/s})]}.}\tag{1}
\]
Every diagonal \((R_s)_{ii}\) is strictly decreasing on \((0,\infty)\) from \(1\) to the stationary probability \(\pi_i\), even when \(Q\) is nonreversible and has nonreal eigenvalues.

Consequently the Crank–Nicolson end step is entrywise nonnegative precisely when
\[
\boxed{a_i\,\mathbb E\!\left[\frac h2(1-e^{-2T_i/h})\right]\le1\quad\text{for every state }i.}\tag{2}
\]
For each \(i\) with \(\pi_i<1/2\), the equality in (2) has a unique finite positive root \(h_i\). States with \(\pi_i\ge1/2\) never obstruct finite-step positivity. Hence, writing
\[
h_*=\min_{i:\,\pi_i<1/2} h_i\quad(\min\varnothing:=\infty),
\]
we have the **universal no-reentrance law**
\[
\boxed{C_h\ge0\ \Longleftrightarrow\ 0\le h\le h_*.}\tag{3}
\]
The single-interval conclusion holds for **all** finite irreducible Markov generators, not only reversible ones.

For the nonreversible directed \(n\)-cycle with equal forward transition rate \(a>0\), \(n\ge3\), define \(r_n\in(1/2,1)\) as the unique solution of
\[
\sum_{j=1}^{n-1}r_n^j=1.
\]
Then the exact sharp threshold is
\[
\boxed{h_*^{(n)}=\frac{2r_n}{a(1-r_n)},\qquad h_*^{(3)}=\frac{1+\sqrt5}{a}.}\tag{4}
\]
These thresholds decrease strictly with \(n\) and converge to \(2/a\) from above. The directed two-cycle is the balanced two-state case and has no finite positivity threshold.

## Assumptions and scope
All matrices and transition rates are real. The chain is finite, irreducible, and homogeneous in continuous time. The row convention means a probability row vector evolves by right multiplication with \(e^{tQ}\). For \(n\ge2\), irreducibility implies \(a_i>0\), finite almost-sure hitting times, and a unique strictly positive stationary law \(\pi\). The return variable \(T_i\) excludes the initial exponential holding time; its distribution is the mixture of hitting-time laws starting from the possible immediate destination states after departure from \(i\).

Positivity means entrywise nonnegativity of the complete end-step matrix, not internal-stage positivity. The formulas use exact arithmetic. The time-step variable \(h\) has units of time, and \(s=h/2\) is the backward-Euler resolvent parameter.

## Proof
**Step 1: renewal identity without detailed balance.** Fix \(i\), abbreviate \(a=a_i\), and let \(H\sim\operatorname{Exp}(a)\) be the holding time in state \(i\). By the strong Markov property, successive visits to \(i\) create independent cycles consisting of \(H\) followed by the excursion \(T_i\). Let \(p_{ii}(t)=(e^{tQ})_{ii}\), \(\lambda>0\), and \(\varphi_i(\lambda)=\mathbb E[e^{-\lambda T_i}]\). The discounted expected occupation in the first holding period is
\[
\mathbb E\left[\int_0^H e^{-\lambda t}\,dt\right]=\frac1{a+\lambda}.
\]
The Laplace transform of the cycle length is
\[
\mathbb E[e^{-\lambda(H+T_i)}]=\frac{a}{a+\lambda}\varphi_i(\lambda).
\]
Summing the renewal geometric series gives the exact occupation transform
\[
\int_0^\infty e^{-\lambda t}p_{ii}(t)\,dt
=\frac{1/(a+\lambda)}{1-a\varphi_i(\lambda)/(a+\lambda)}
=\frac1{\lambda+a(1-\varphi_i(\lambda))}.
\]
The resolvent is \(R_s=\frac1s\int_0^\infty e^{-t/s}e^{tQ}\,dt\). Set \(\lambda=1/s\) to obtain (1), with no spectral or reversibility assumption. This representation is also computable without simulating excursions: if \(S\) is the set of states other than \(i\), the ordinary killed-chain hitting-time equations give
\[
\varphi_i(\lambda)=\frac{1}{a_i}\,q_{iS}(\lambda I-Q_{SS})^{-1}q_{Si}.
\]
The subgenerator \(Q_{SS}\) is transient by irreducibility, so this inverse exists for every \(\lambda>0\).

**Step 2: strict monotonicity.** For every deterministic \(t>0\),
\[
s(1-e^{-t/s})=\int_0^t e^{-u/s}\,du.
\]
For each \(u>0\), the integrand is strictly increasing with \(s>0\). Since \(T_i>0\) almost surely (an excursion starts away from \(i\)) and has finite mean, Tonelli's theorem shows
\[
G_i(s):=\mathbb E[s(1-e^{-T_i/s})]
=\int_0^\infty e^{-u/s}\Pr(T_i>u)\,du
\]
is continuous and strictly increasing. Dominated convergence yields \(G_i(s)\to0\) as \(s\downarrow0\) and \(G_i(s)\to\mathbb E T_i\) as \(s\to\infty\). By (1), the diagonal resolvent strictly decreases from \(1\) to \((1+a_i\mathbb ET_i)^{-1}\). The latter is \(\pi_i\), by the regenerative occupation fraction (mean holding time divided by mean complete cycle length). This proves the unconditional monotonicity assertion.

**Step 3: positivity and sharp boundary.** For every \(s\ge0\), \(I-sQ\) is a nonsingular \(M\)-matrix, so \(R_s\ge0\). Since \(Q\mathbf1=0\), \(R_s\mathbf1=\mathbf1\). Algebraically, \(C_h=2R_{h/2}-I\). Thus \(C_h\mathbf1=\mathbf1\), all its off-diagonal entries are nonnegative, and \((C_h)_{ii}=2(R_{h/2})_{ii}-1\). Inserting (1) proves (2). Strict monotonicity of each diagonal proves that a state with \(\pi_i<1/2\) crosses the level \(1/2\) exactly once, while a state with \(\pi_i\ge1/2\) never crosses it at a finite step. Intersecting all statewise intervals proves (3), including both endpoints. For \(n\ge3\), at least one \(\pi_i<1/2\), hence the boundary is finite; for \(n=2\), the balanced stationary law yields an infinite boundary, as already known from direct inversion.

**Step 4: exact directed-cycle classification.** On a unidirectional \(n\)-cycle let \(P\) be its cyclic permutation matrix, so \(Q=a(P-I)\), \(P^n=I\). Put \(r=as/(1+as)\in[0,1)\). The finite geometric identity yields
\[
R_s=\frac{1}{1+as}\frac{I+rP+\cdots+r^{n-1}P^{n-1}}{1-r^n}
\]
and, for every state,
\[
(R_s)_{ii}=\frac{1-r}{1-r^n}
=\frac1{1+r+\cdots+r^{n-1}}.
\]
The diagonal condition \((R_s)_{ii}\ge1/2\) is equivalent to \(\sum_{j=1}^{n-1}r^j\le1\), proving (4). For \(n\ge3\) the polynomial sum is strictly increasing from \(0\) at \(r=0\) to \(n-1>1\) at \(r=1\), giving exactly one root. At \(r=1/2\), the sum is strictly below \(1\), so \(r_n>1/2\). At fixed \(r>0\), the sum strictly increases with \(n\); therefore \(r_n\) and \(h_*^{(n)}\) strictly decrease. The infinite geometric series \(\sum_{j\ge1}r^j=r/(1-r)\) has root \(r=1/2\), so \(r_n\downarrow1/2\) and \(h_*^{(n)}\downarrow2/a\). For \(n=3\), solving \(r+r^2=1\) gives \(r_3=(\sqrt5-1)/2\), hence \(h_*^{(3)}=(1+\sqrt5)/a\). For \(n=2\), \(1+r\le2\) for every \(r<1\), so positivity holds for all finite steps.

## Verification
The accompanying standalone `verify.py` uses only the Python standard library. It inverts small resolvents over exact fractions, computes the first-return Laplace transform independently by solving the killed-generator hitting-time equations, and checks identity (1), strict diagonal decrease, stochasticity, and the equivalence of nonnegativity with the diagonal test. It treats nine irreducible directed test generators, including nonreversible cycles and nonuniform directed graphs, at six positive rational values of \(s\). Separate exact rational bisection brackets check the polynomial boundaries for thirteen cycle lengths. Running `python verify.py` prints:

`VERIFY_OK: exact_first_return_checks=222; directed_generators=9; cycle_boundaries=13`

Finite tests are cross-checks only. The statements for arbitrary chain size, timestep, and real rates follow analytically from the regenerative proof and geometric matrix identity.

## Relationship to prior work
The classical resolvent/Cayley identity and the fact that an inverse \(M\)-matrix is nonnegative are established tools; they are not claimed as novel here. Fallat and Tsatsomeros (2002) study Cayley transforms of matrix positivity classes. Higueras and Roldán (first public preprint January 3, 2023) provide sharp Crank–Nicolson positivity thresholds for a symmetric tridiagonal heat-equation discretization, not arbitrary nonreversible Markov chains.

The published study *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains* establishes the full diagonal resolvent criterion, strict monotonicity, and an interval threshold **under reversibility**, along with irreducible-chain eventual obstructions and two-state classification. Its statement explicitly leaves open the behavior of positivity windows for nonreversible generators after an initial loss. The present theorem supplies a new return-time proof of strict monotonicity that does not use reversibility; it therefore strengthens that published single-interval theorem to all finite irreducible chains. The cycle thresholds supply exact genuinely nonreversible examples. The earlier reversible and eventual-obstruction cases are logically covered by its already published conclusions and are not presented as independent discoveries.

Classical first-return/renewal transforms are also prior probabilistic knowledge. The contribution assessed here is the resulting universal fixed-generator numerical-positivity law, rather than rediscovery of renewal theory or the Cayley identity. Horváth's analyses of Runge–Kutta positivity radii concern method-wide sufficient or class-wise sharp criteria, which do not directly imply the fixed-generator no-reentrance result.

## Limitations
The result concerns finite irreducible homogeneous Markov chains. Reducible chains, nonlinear Markovian evolutions, rounding errors near an exact-zero transition entry, and positivity of intermediate Runge–Kutta stages are not classified. The return-time distribution can be challenging to evaluate explicitly on large directed graphs; formula (2) is a sharp implicit criterion, not a general constant-cost algorithm. The directed-cycle closed form assumes identical rates on all cycle edges. A specialized earlier source may independently contain the same renewal-to-Crank–Nicolson implication under different terminology; publication priority has not been independently certified.

## References
1. I. Higueras and T. Roldán, *A new insight on positivity and contractivity of the Crank–Nicolson scheme for the heat equation*, arXiv:2301.01066v1, first submitted 2023-01-03. https://arxiv.org/abs/2301.01066
2. S. M. Fallat and M. J. Tsatsomeros, *On the Cayley Transform of Positivity Classes of Matrices*, Electronic Journal of Linear Algebra **9** (2002), 190–196, DOI:10.13001/1081-3810.1086. https://journals.uwyo.edu/index.php/ela/article/download/173/173
3. Z. Horváth, *Positivity of Runge–Kutta and Diagonally Split Runge–Kutta Methods*, Applied Numerical Mathematics **28** (1998), 309–326, DOI:10.1016/S0168-9274(98)00050-6.
4. *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains*, published mathematical finding, October 2026. https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-a-resolvent-return-law-for-crank-nicolson-positivity-on-reversib--d475df91cd2a/RESULT.md
