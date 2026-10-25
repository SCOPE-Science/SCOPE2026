# The sharp two-leader coherence transition on unweighted wheels

## Finding
Let \(W_n=K_1\vee C_n\) be the unit-conductance wheel with one hub and \(n\ge3\) rim vertices. Choose exactly two *noise-free* leader vertices; independent unit-intensity white noise perturbs every other vertex under continuous-time Laplacian consensus. The optimal leader sets minimizing total steady-state follower variance are **exactly**:

- For \(n=3\), every one of the six two-vertex sets (the wheel is \(K_4\)).
- For \(4\le n\le6\), two rim vertices at maximum cyclic distance \(\lfloor n/2\rfloor\); the number of optimal sets is \(n/2\) when \(n\) is even and \(n\) when \(n\) is odd.
- For every \(n\ge7\), the hub together with any one rim vertex; exactly \(n\) sets.

All inequalities underlying this classification are strict outside the \(n=3\) tie. In particular, the first graph for which the hub is indispensable in an optimal two-leader set is the wheel with seven rim vertices (eight vertices total).

An exact, closed formula for the minimum and for every two-rim-leader alternative is given below. This is a network-wide leader-placement result, not an assertion about two edge failures.

## Assumptions and scope
All spokes and rim edges have unit conductance. Each leader is pinned perfectly to a common reference signal; followers obey \(dX_F=-L_{FF}X_F\,dt+dB_F\), where \(L\) is the wheel's combinatorial Laplacian, \(F\) is the complement of the two-leader set, and \(B_F\) has independent standard Brownian coordinates. The total stationary variance equals \(\operatorname{tr}(L_{FF}^{-1})/2\). We minimize the equivalent normalized objective \(J(S)=\operatorname{tr}(L_{FF}^{-1})\). Each grounded principal Laplacian is positive definite.

Put
\[
q=\frac{3-\sqrt5}{2},\qquad
\phi(t)=\frac{tq^t}{1-q^t}\quad(t>0),
\]
and, for \(1\le d\le\lfloor n/2\rfloor\),
\[
g_n=\frac{1+q^n}{\sqrt5(1-q^n)},\qquad
s_n(d)=\frac{(1-q^d)(1-q^{n-d})}{\sqrt5(1-q^n)}.
\]
Every hub--rim leader set has normalized objective
\[
H_n=\frac{n}{\sqrt5}\frac{1+q^{2n}}{1-q^{2n}}-\frac35.
\]
Every pair of rim leaders at cyclic separation \(d\) has normalized objective
\[
R_n(d)=(2n+1)g_n-2-\frac{n+1}{2}s_n(d)-\frac35+
\frac{\phi(d)+\phi(n-d)-\phi(n)}{\sqrt5}.
\]
For \(n\ge4\) the minimum is \(R_n(\lfloor n/2\rfloor)\) when \(n\le6\), and \(H_n\) when \(n\ge7\). At \(n=3\), both values equal \(3/4\). Divide these expressions by two for total unit-noise stationary variance.

## Proof
**1. Grounding and resistance identity.** Let \(r(u,v)\) be effective resistance in the original wheel, and \(r(v,\{a,b\})\) resistance to the electrically shorted pair \(a,b\). The grounding identity gives \(J(\{a,b\})=\sum_v r(v,\{a,b\})\). Minimizing the dissipated energy over the two fractions of a unit current sent from \(v\) to \(a\) and \(b\) yields
\[
r(v,\{a,b\})=\frac{r(v,a)+r(v,b)}2-\frac{r(a,b)}4-
\frac{(r(v,a)-r(v,b))^2}{4r(a,b)}.
\]
Indeed the energy when fraction \(\theta\) is sent to \(a\) equals \(r(v,b)+\theta[r(v,a)-r(v,b)-r(a,b)]+\theta^2r(a,b)\); its minimum gives the identity. Leaders themselves contribute zero.

**2. Exact wheel Green function.** Grounding the hub leaves the rim matrix \(T=3I-A(C_n)\), whose inverse \(G\) has entries \(G_{ij}=g_{|i-j|}\), with cyclic distance and
\[
g_d=\frac{q^d+q^{n-d}}{\sqrt5(1-q^n)}\quad (0\le d\le n).
\]
This follows by solving the second-order difference recurrence \(3g_d-g_{d-1}-g_{d+1}=\mathbf1_{\{d=0\}}\) periodically. The resistance between rim vertices at separation \(d\) is \(2(g_0-g_d)=2s_n(d)\); a rim-to-hub resistance is \(g_0\). Since \(T\mathbf1=\mathbf1\), the sum of resistances from one rim vertex to every wheel vertex is \((2n+1)g_0-2\). For a difference between two rim vertices, the corresponding Laplacian-pseudoinverse column difference equals the rim Green-column difference and vanishes at the hub. Thus
\[
\sum_v[r(v,a)-r(v,b)]^2=8[(T^{-2})_{00}-(T^{-2})_{0d}].
\]
Writing \(T(a)=aI-A(C_n)\) and differentiating at \(a=3\) gives \(T^{-2}=-\partial_a T(a)^{-1}\). Consequently the ratio appearing after inserting these identities into step 1 is
\[
\frac{(T^{-2})_{00}-(T^{-2})_{0d}}{g_0-g_d}=
-\left.\partial_a\log(g_0(a)-g_d(a))\right|_{a=3}=
\frac35-\frac{\phi(d)+\phi(n-d)-\phi(n)}{\sqrt5}.
\]
The stated exact expression for \(R_n(d)\) follows.

**3. Strict separation monotonicity.** On \(0<d<n/2\), the function \(q^d+q^{n-d}\) strictly decreases, so \(s_n(d)\) strictly increases. Also \(\phi(t)=t/(e^{ct}-1)\), where \(c=-\log q>0\), is strictly convex. Explicitly the numerator of its second derivative after factoring positive terms is \((x-2)e^x+x+2\) for \(x=ct>0\). This function and its first derivative vanish at zero, while its second derivative is \(xe^x>0\); hence it is positive. Therefore \(\phi(d)+\phi(n-d)\) strictly decreases for \(d<n/2\). Both separation-dependent terms of \(R_n(d)\) strictly decrease, proving that the best pair of rim leaders is at maximum cyclic separation, with no other rim-pair ties.

**4. Hub comparison.** Grounding the hub and one rim vertex leaves the tridiagonal Dirichlet matrix \(T_{n-1}=3I-A(P_{n-1})\). Its determinant at variable diagonal \(a\) is \((\rho^n-\rho^{-n})/(\rho-\rho^{-1})\), where \(\rho=(a+\sqrt{a^2-4})/2\). Differentiating its log determinant at \(a=3\) proves the formula for \(H_n\).

Exact rational substitutions for \(n=3,4,5,6,7,8\) produce the ordered pairs \((R_n(\lfloor n/2\rfloor),H_n)\):
\[
(3/4,3/4),\ (31/30,25/21),\ (67/44,18/11),\ (2,25/12),\
(31/12,954/377),\ (221/70,2939/987).
\]
These establish the claimed boundary up to \(n=8\). For all \(n\ge8\), since \(g_n>1/\sqrt5\), \(s_n(d)<1/\sqrt5\), and \(\phi(t)>0\), subtraction gives the uniform bound
\[
R_n(d)-H_n>
\frac{n+1}{2\sqrt5}-2-\frac{\phi(n)+\phi(2n)}{\sqrt5}=:\delta_n.
\]
The function \(\phi(t)\) is strictly decreasing for positive \(t\), so \(\delta_n\) strictly increases with \(n\). At \(n=8\), exact radical simplification gives
\[
\delta_8=\frac{33\sqrt5}{10}-\frac{36362}{4935}>0.
\]
This proves the hub--rim choice is uniquely optimal in type for every \(n\ge8\), with \(n=7\) already handled exactly. Rotational symmetry and the strict inequalities give all stated equality cases and counts. \(\square\)

## Verification
The included `verify.py` independently builds exact rational grounded wheel Laplacians for each rim size from \(3\) through \(11\), checks every inequivalent two-rim leader separation and each hub--rim case against the radical formulas, establishes their ordering, and validates the exact small-size comparison table and the positive uniform lower bound at \(n=8\). It uses SymPy only. Run `python verify.py` with the version requirement in `requirements.txt`. The infinite-family monotonicity and hub threshold use the analytic arguments above, not a finite test.

## Relationship to prior work
Fitch and Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569 (first posted 2014-07-07), develop joint-centrality formulas and solve cycle and path cases. Their two-leader cycle corollary and appendix concern a vertex-transitive cycle, rather than a wheel with a hub of unequal degree. Patterson, McGlohon and Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595 (2014), give algorithms for paths and rings. Patterson, Yi and Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873 (2017), provide general resistance formulas and exact results for paths, cycles and particular trees. Those formulas motivate and are consistent with the grounding calculation here; none of their inspected specialized results determines the sharp wheel-specific hub/rim change at seven rim vertices or proves strict placement optimality for every wheel size. Broad resistance formulas alone do not supply the requisite wheel inequalities.

## Limitations
Only unit-weight undirected wheels, exactly two noise-free leaders and independent equal-intensity follower disturbances are covered. The classification does not assert the same choices for finite-gain/noisy leaders, heterogeneous weights, different noise covariance, more than two leaders or other graph families. General formulas and specialized historical literature may contain equivalent implications not detected by the consulted sources. The proof and verification here are not an independent external mathematical audit.

## References
1. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, first public arXiv submission 2014-07-07. https://arxiv.org/abs/1407.1569
2. S. Patterson, N. McGlohon and K. Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595, first public arXiv submission 2014-12-20. https://arxiv.org/abs/1412.6595
3. S. Patterson, Y. Yi and Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873, first public arXiv submission 2017-08-23. https://arxiv.org/abs/1708.06873
