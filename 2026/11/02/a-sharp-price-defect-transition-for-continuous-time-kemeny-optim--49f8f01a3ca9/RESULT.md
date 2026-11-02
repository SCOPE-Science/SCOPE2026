# A sharp price-defect transition for continuous-time Kemeny optimization on directed cycles

## Finding

For every integer \(n\ge3\), put \(k=n-1\). Consider the continuous-time Markov chain that jumps only clockwise on a directed \(n\)-cycle with rates \(r_1,\ldots,r_n>0\), under the resource constraint
\[
\sum_{i=1}^{k}r_i+q r_n\le B,\qquad B>0,\quad q>0.
\]
Its continuous-time Kemeny constant is the expected first hitting time of an independent stationary-distributed target, with hitting time zero if the starting state already equals the target. The exact threshold for the unique globally optimal positive rate vector to exist is
\[
q_c=\frac{k(k+1)}2=\frac{n(n-1)}2.
\]
For \(0<q<q_c\), set
\[
u_* =\frac1k\left(\sqrt{\frac{(k+1)(k^2-q)}{(k-1)q}}-1\right),\qquad
x_* =\frac{B}{k+qu_*},\qquad y_*=u_*x_*.
\]
Then the **unique** global minimizer, without any prior symmetry restriction, is
\[
(r_1,\ldots,r_n)=(x_*,\ldots,x_*,y_*),
\]
with optimum
\[
K_* = \frac{k(k+qu_*)((k-1)u_*+2)}{2B(ku_*+1)}.
\]
For \(q\ge q_c\), there is **no minimizer with strictly positive rates**. The exact infimum is \(k^2/B\), approached by ordinary rates tending to \(B/k\) and the expensive exceptional rate tending to zero. At \(q=1\), the unique minimizer is uniform, with all rates equal to \(B/n\) and \(K_*=n(n-1)/(2B)\).

## Assumptions and scope

The state space is \(\{1,\ldots,n\}\), indices read modulo \(n\). The generator \(Q\) has \(Q_{i,i+1}=r_i\) and \(Q_{ii}=-r_i\), all other off-diagonal entries zero. Every rate is strictly positive, ensuring an irreducible continuous-time process. The stationary distribution of this process is optimized along with its rates; it is not fixed externally. Price \(q\) applies to a distinguished directed transition only. The objective is the *continuous-time* stationary-target expected hitting time, not discrete jump count, spectral gap, or mixing distance.

Define \(\tau_j=\inf\{t\ge0:X_t=j\}\) and
\[
K(r)=\sum_{j=1}^n\pi_j\mathbb E_i[\tau_j],
\]
where \(\pi\) is stationary. This quantity is independent of the initial state \(i\), as derived below. The boundary rate \(r_n=0\) is excluded, and no Kemeny value is assigned to the resulting reducible generator.

## Proof

**1. Exact objective.** Write \(t_i=1/r_i\) and \(T=\sum_i t_i\). Since stationary flux is constant around a directed cycle, \(\pi_i=t_i/T\). Clockwise movement is obligatory, so for \(i\ne j\), \(\mathbb E_i\tau_j\) is the sum of holding-time means \(t_a\) on the unique clockwise arc from \(i\) up to but not including \(j\). For each unordered pair of distinct edges, exactly one of their two possible cyclic orders contributes to the stationary-target sum. Consequently, for every starting state,
\[
K(r)=\frac{\sum_{1\le a<b\le n}t_at_b}{\sum_{a=1}^n t_a}
=\frac{T^2-\sum_{a=1}^n t_a^2}{2T}. \tag{1}
\]
This identity also follows directly by summing the clockwise arcs and their target probabilities. Uniform scaling \(r\mapsto c r\) sends \(K\mapsto K/c\); therefore any positive-rate minimizer exhausts its budget.

**2. Unrestricted ordinary-rate symmetrization.** Fix two ordinary rates \(a_1,a_2>0\) with sum \(s=a_1+a_2\), and hold the other \(n-2\) rates fixed. Let \(v=1/a_1+1/a_2\); let \(R>0\) and \(H>0\) be the sum and sum of squares of the other reciprocal rates. As \(1/(a_1a_2)=v/s\), identity (1) becomes
\[
K(v)=\frac{R^2-H+2(R+1/s)v}{2(R+v)},\qquad
\frac{dK}{dv}=\frac{R^2+H+2R/s}{2(R+v)^2}>0. \tag{2}
\]
The arithmetic–harmonic mean inequality gives \(v\ge4/s\), with equality exactly when \(a_1=a_2=s/2\). Hence averaging any unequal pair of equally priced ordinary rates strictly decreases \(K\) while leaving cost unchanged. Repeated pairwise averaging converges to equality for all \(k\) ordinary rates; continuity on positive rates implies that the fully symmetrized vector is no worse. Thus every global minimizer, and the global infimum, may be analyzed with
\[
r_1=\cdots=r_k=x>0,\qquad r_n=y>0.
\]
For strict uniqueness, any nonuniform ordinary-rate vector cannot be optimal because one averaging step strictly improves it.

**3. Scalar optimization.** Exhausting the budget and setting \(u=y/x>0\) gives
\[
x=\frac{B}{k+qu},\qquad y=ux,
\]
and identity (1) reduces exactly to
\[
F(u)=\frac{k(k+qu)((k-1)u+2)}{2B(ku+1)}. \tag{3}
\]
Differentiating, a strictly positive denominator and prefactor show
\[
\operatorname{sgn} F'(u)=\operatorname{sgn}\left(
q[k(k-1)u^2+2(k-1)u+2]-k(k+1)
\right). \tag{4}
\]
The expression in parentheses has strictly positive derivative in \(u>0\), equals \(2q-k(k+1)\) at \(u=0\), and tends to positive infinity. Thus for \(q<k(k+1)/2\), there is exactly one critical point \(u_*>0\), and it is the unique global minimum. Solving the quadratic in (4) yields precisely the displayed radical. Since \(F(u)\to\infty\) as \(u\to\infty\), no other boundary competes. The strict ordinary-rate averaging from step 2 establishes uniqueness over all feasible positive rate vectors, not merely within the symmetric ansatz.

For \(q\ge k(k+1)/2\), (4) is strictly positive for every \(u>0\), so the infimum lies at the excluded boundary \(u\downarrow0\). Taking this limit in (3) yields \(k^2/B\). The same strict pairwise averaging and scalar monotonicity show that every strictly positive feasible vector has larger objective. In particular this includes equality at the threshold. Finally, inserting \(q=1\) into the radical gives \(u_*=1\), proving the uniform-rate specialization. \(\square\)

## Verification

The standalone standard-library Python program `verify.py` tests equation (1) against direct exact-rational first-hit-time summation for every starting state on many random finite cycles; tests strict pairwise improvement with rational arithmetic; and checks the scalar critical-point formula, costs, sampled global comparisons, and the nonattainment boundary. It was executed successfully and reported `PASS 12516 exact-rational and floating checks`. Algebraic differentiation and the quadratic-root substitution were also independently simplified symbolically during derivation. All universal claims are established by the proof, not by the finite checks.

To reproduce, save `verify.py` in the same directory as this file and run `python verify.py` using a standard Python 3 interpreter. No external packages are required.

## Relationship to prior work

Kemeny constants and their relation to stationary-weighted hitting times, perturbations and directed graph cycles are developed by Catral–Kirkland–Neumann–Sze. Their constant-value cycle theorem concerns particular discrete-time digraph structures, rather than optimizing nonuniform continuous-time holding rates under linear prices. Kirkland's directed-graph extremal Kemeny study optimizes over **discrete-time stochastic transition matrices** with graph support constraints, not continuous-time rate budgets. Patel–Agharkar–Bullo provide weighted Kemeny optimization formulations chiefly for **reversible discrete-time chains**, different from a one-way nonreversible continuous-time generator with a freely varying invariant law. Earlier directed-cycle shortcut calculations also express the zero-shortcut continuous-time Kemeny functional as the ratio of the second elementary symmetric polynomial in holding times to their sum. Identity (1), therefore, is background rather than a novelty claim. The contribution is the unrestricted price-budget minimizer, its explicit threshold, and the strict existence/nonattainment dichotomy; general frameworks and identity (1) are not claimed as new.

## Limitations

The theorem addresses one exceptional price and a strictly one-directional cycle; it does not solve multiple distinct prices, added reverse edges, prescribed stationary distributions, spectral-gap optimization, or transient mixing. The above infimum at high exceptional price is not a claim about a reducible chain at zero rate. Novelty has been checked against inspected source material and semantic search results, but cannot exclude an unlocated equivalent specialized treatment; an independent scholarly audit has not been performed.

## References

1. M. Catral, S. J. Kirkland, M. Neumann and N.-S. Sze, *The Kemeny Constant for Finite Homogeneous Ergodic Markov Chains*, Journal of Scientific Computing 45 (2010), 151–166. Lawful open-access manuscript: https://www.polyu.edu.hk/ama/profile/sze/PDF/kemeny.pdf ; repository public-deposit record dated 2010-10-13: https://mural.maynoothuniversity.ie/id/eprint/2185/ .
2. S. Kirkland, *Fastest Expected Time to Mixing for a Markov Chain on a Directed Graph*, accessible manuscript: https://www.hamilton.ie/skirkland/min_kemeny_final.pdf .
3. R. Patel, P. Agharkar and F. Bullo, *Robotic Surveillance and Markov Chains With Minimal Weighted Kemeny Constant*, accessible manuscript: https://motion.me.ucsb.edu/pdf/2014b-pab.pdf .
