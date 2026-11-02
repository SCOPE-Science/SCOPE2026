# Exact run-length activation laws and budget-optimal control batching in flat-top tent dynamics

## Finding

Let \(T:[-1,1]\to[-1,1]\) be the full tent map \(T(x)=1-2|x|\). At a selected time one may instead apply the flat-top limiter \(G(x)=\min\{T(x),1/2\}\), whose active plateau is \(I=(-1/4,1/4)\). Fix a horizon \(N\ge1\) and any prescribed set \(A\subseteq\{0,1,\ldots,N-1\}\) of limiter times. Start from \(x_0\) with normalized Lebesgue distribution on \([-1,1]\). Define first *genuine intervention* as the first \(n\in A\) for which \(G(x_n)\ne T(x_n)\). This is an entry into \(I\) at a controlled time; the event is not an assertion about eventual attraction after intervention.

**Exact schedule law.** If the maximal consecutive blocks of \(A\) have positive lengths \(\ell_1,\ldots,\ell_r\), the proportion \(S(A)\) of starting points experiencing no genuine intervention within the horizon is exactly
\[
S(A)=\prod_{j=1}^{r}\frac{\ell_j+2}{2^{\ell_j+1}},
\qquad S(\varnothing)=1.
\]
This holds for every finite binary control pattern, without periodicity assumptions.

**Optimal fixed-budget law.** Fix \(1\le k\le N\) and allow any schedule with exactly \(k\) controlled times. Then
\[
\min_{|A|=k}S(A)=\frac{k+2}{2^{k+1}},
\]
attained precisely by one consecutive block. Put \(r_* = \min\{k,N-k+1\}\), \(a=\lfloor k/r_*\rfloor\), and \(b=k-ar_*\). The sharp upper bound is
\[
\max_{|A|=k}S(A)=
\left(\frac{a+2}{2^{a+1}}\right)^{r_*-b}
\left(\frac{a+3}{2^{a+2}}\right)^b.
\]
It is attained precisely by schedules with \(r_*\) maximal consecutive blocks, of which \(b\) have length \(a+1\) and the others length \(a\). Thus, at a fixed number of opportunities, *batching controls maximizes the intervention probability*, whereas dispersing controls into as many balanced blocks as the horizon permits minimizes it. When \(N\ge 2k-1\), the ratio between the largest and smallest no-intervention probabilities is exactly \(2(3/2)^k/(k+2)\).

**Infinite-pattern consequence.** For every infinite binary pattern with infinitely many controlled times, almost every initially uniform point eventually experiences a genuine limiter intervention. No positive asymptotic frequency of control is needed.

## Assumptions and scope

Use the continuous plateau convention \(G(x)=1/2\) on \((-1/4,1/4)\) and \(G(x)=T(x)\) elsewhere. At \(x=\pm1/4\), the two branches agree. All conclusions concern normalized Lebesgue probability of initial conditions in \([-1,1]\), exact finite-horizon *first-activation* events, and arbitrary preassigned deterministic schedules, not adaptive scheduling. The underlying map is the \(u=1/2\) member of the flat-top tent family in Silva (2023). Exact boundary trajectories form a countable measure-zero set and cannot alter the probability formulas. The infinite-pattern consequence is about the first intervention only; no classification of subsequent orbits is claimed.

## Proof

1. **First interventions reduce to an uncontrolled orbit.** Prior to the first intervention, every executed map agrees with \(T\). Therefore no intervention through the horizon is equivalent to
\[
T^n(x_0)\notin I\quad\hbox{for each }n\in A.
\]
The equivalence includes trajectories which would deviate after a first intervention: they are excluded immediately, and no post-intervention behavior is used.

2. **Independent symbolic bits.** Outside the countable set of points reaching \(0\) under some iterate, let \(B_j(x_0)\) be \(L\) or \(R\) according to the sign of \(T^j(x_0)\). Every finite word of length \(m\) occurs on an interval of normalized Lebesgue measure \(2^{-m}\), because the two inverse branches of \(T\) are onto and have slope magnitude \(1/2\). Thus \((B_j)_{j\ge0}\) are independent fair binary symbols. For any \(z\in[-1,1]\) off the boundaries,
\[
z\in(-1/4,1/4)\quad\Longleftrightarrow\quad B_1(z)=R,\ B_2(z)=L.
\]
Indeed, \(B_1=R\) means \(T(z)>0\); then \(B_2=L\) means \(T(z)>1/2\), equivalent to \(|z|<1/4\). Consequently, a genuine limiter encounter at time \(n\) is the occurrence of the *nonoverlapping-with-itself* word \(RL\) in the two symbols \((B_{n+1},B_{n+2})\).

3. **Run factorization.** For a consecutive block of \(\ell\) controlled times, avoidance means no adjacent \(RL\) among \(\ell+1\) independent symbols. The admissible words are exactly \(L^jR^{\ell+1-j}\), \(j=0,\ldots,\ell+1\); hence the block survival probability is \(p_\ell=(\ell+2)/2^{\ell+1}\). Distinct control blocks are separated by at least one uncontrolled time. Their pairs of tested symbol coordinates are disjoint, so the block events are independent, proving the product.

4. **Budget extrema.** For any positive integers \(c,d\),
\[
p_cp_d-p_{c+d}=\frac{cd}{2^{c+d+2}}>0.
\]
Splitting a control block into two separated blocks strictly raises survival and merging decreases it. Exactly \(r\) blocks fit into \(N\) instants with \(k\) controls iff \(1\le r\le\min\{k,N-k+1\}\). Therefore one block minimizes survival and the maximum uses \(r_*\) blocks. For fixed \(r\), the denominator of \(\prod_jp_{\ell_j}\) is \(2^{k+r}\); if two lengths differ by at least two, moving one control from the longer to the shorter increases \((\ell_i+2)(\ell_j+2)\). Hence the unique maximizing length multiset is balanced as specified, proving both sharp bounds and equality descriptions.

5. **Infinite controls.** Among any first \(k\) selected control times, the product law and repeated merging imply \(S\le (3/4)^k\). The probability of never intervening is the decreasing limit as \(k\to\infty\), which is zero.

## Verification

The included standalone script `verify_tent.py` uses only the Python standard library. It exhaustively checks every binary schedule for each horizon \(1\le N\le8\) against direct exact-rational tent iterates at one representative of every branch cylinder, then checks the budget extrema for all \(k\le N\). Run `python verify_tent.py`. These finite checks test implementation and boundary conventions; the universal assertions follow from the preceding symbolic proof, not extrapolation.

For illustration, with \(N=6\) and \(k=3\), three consecutive controls have no-activation fraction \(5/16\); three isolated controls have fraction \(27/64\). The larger capture probability for consecutive controls is the complement of the smaller no-activation fraction.

## Relationship to prior work

The flat-top family, arbitrary binary iteration patterns, and qualitative local/Milnor attractors come from Silva, *Attractors in Pattern Iterations of Flat Top Tent Maps*, *Mathematics* **11** (2023), 2677. The proof here deliberately does not claim novelty for that model, full-shift coding, or generic binary-word avoidance. The stated new mathematical content is the exact **run-length factorization for genuine interventions in this dynamically controlled family**, its **global resource-constrained schedule optimization**, and the resulting **all-pattern almost-sure activation**. Silva's 2019 study analyzes existence of periodic nonautonomous attractors; Silva and Silva (2025) study kneading invariants and period incrementing. Those different objectives do not by themselves imply a first-intervention distribution or sharp finite-budget schedule ranking. Available text supports that comparison, while incomplete access to the later full text leaves a residual literature-priority risk.

## Limitations

The calculation is for the natural dyadic plateau parameter \(u=1/2\), not general limiter heights; the method exploits its two-symbol cylinder structure. It quantifies the initial time at which a limiter *actually changes the trajectory*, not whether a prescribed target periodic orbit is reached or remains attractive. It assumes a uniform initial ensemble and a deterministic, non-adaptive control schedule. Bounds for other initial measures, noisy tent maps, or different plateau widths are not asserted. The source comparison does not establish publication-level novelty conclusively, and an unindexed stronger general word-avoidance theorem could cover the symbolic optimization.

## References

1. L. Silva, *Attractors in Pattern Iterations of Flat Top Tent Maps*, *Mathematics* **11** (2023), 2677. DOI: 10.3390/math11122677. First verified public date: 2023-06-13.
2. L. Silva, *Periodic attractors of nonautonomous flat-topped tent systems*, *Discrete and Continuous Dynamical Systems B* **24** (2019), 1867–1874. DOI: 10.3934/dcdsb.2018243.
3. L. Silva and T. M. Silva, *Milnor attractors and period incrementing on pattern iterations of flat top tent maps*, *Topological Methods in Nonlinear Analysis* **65** (2025), 79–97. DOI: 10.12775/TMNA.2024.023.
4. C. Wagner and R. Stoop, *Renormalization approach to optimal limiter control in 1-D chaotic systems*, *Journal of Statistical Physics* **106** (2002), 97–106. DOI: 10.1023/A:1013120112236.
