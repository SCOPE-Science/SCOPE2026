# Sharp stationary second-moment threshold for geometric-emigration branching

## Finding
For the geometric-emigration branching chain specified below, with a unique invariant distribution \(\pi_p\) for \(2/3<p<1\), the second stationary moment is finite **if and only if** \(p>4/5\). In that regime,
\[
\mathbb E_{\pi_p}[V^2]=\frac{6p(1-p)}{(4p-3)(5p-4)},\qquad
\operatorname{Var}_{\pi_p}(V)=\frac{2(1-p)(2p-1)(11p-8)}{(4p-3)^2(5p-4)}.
\]
Both quantities diverge as \(p\downarrow4/5\); more precisely,
\[
\lim_{p\downarrow4/5}(p-4/5)\mathbb E_{\pi_p}[V^2]=
\lim_{p\downarrow4/5}(p-4/5)\operatorname{Var}_{\pi_p}(V)=\frac{24}{25}.
\]
The first-moment boundary \(p=3/4\) and the stationary mean above it are prior results; their rederivation here is an intermediate step, not part of the novelty claim.

## Assumptions and scope
Fix \(p\in(2/3,1)\), put \(q=1-p\), and let \(K_n\) and \(X_{n,j}\) be mutually independent, with
\[
\Pr(K_n=k)=qp^k\quad(k=0,1,\ldots),\qquad
\Pr(X_{n,j}=k)=2^{-(k+1)}\quad(k=0,1,\ldots).
\]
Define a time-homogeneous chain on \(\mathbb Z_{\ge0}\) by
\[
V_{n+1}=\mathbf 1_{\{K_n\le V_n\}}\left(1+\sum_{j=1}^{V_n+1-K_n}X_{n,j}\right).
\]
An empty sum is zero. Here \(K_n\) removes potential parents and, if it exceeds the current population, causes a reset to zero; surviving parents produce geometric numbers of children with mean one, plus one designated individual. This is the geometric-emigration chain introduced in Carper (2026), not an arbitrary branching chain. The claims concern the invariant **one-time** distribution, not excursion sums or general offspring laws.

## Proof
**1. Existence and moment integrability.** Let \(a=p/q\), and write \(P\) for the transition operator. Directly summing over \(K_n\), using that the geometric offspring law has mean one, gives
\[
(Px)(x)-x=(2-a)+(a-1)p^{x+1}.
\]
The chain is irreducible: from any state it can reset to zero, and from zero every nonnegative state is accessible with positive probability. It is aperiodic because it has a positive self-loop at zero. For \(a>2\) the displayed drift is eventually strictly negative, yielding positive recurrence by the usual Foster criterion, hence a unique invariant probability \(\pi_p\).

The geometric offspring law has factorial moments \(\mathbb E(X)_j=j!\), and the sum of \(\ell\) such offspring has raw moments
\[
\mathbb E Z=\ell,\quad \mathbb E Z^2=\ell^2+2\ell,\quad
\mathbb E Z^3=\ell^3+6\ell^2+6\ell.
\]
Summation over the geometric emigration variable gives, as \(x\to\infty\),
\[
P(x^2)(x)-x^2=2(3-a)x+O_p(1),\qquad
P(x^3)(x)-x^3=3(4-a)x^2+O_p(x+1).
\]
Each error is bounded in the stated order because the truncated geometric sums are polynomials in \(x\) plus exponentially decaying terms. Thus the quadratic test function gives \(\mathbb E_{\pi_p}V<\infty\) when \(a>3\); the cubic test function gives \(\mathbb E_{\pi_p}V^2<\infty\) when \(a>4\).

For completeness, the version of the drift lemma used here does not presuppose integrability of the test function. If a recurrent chain with invariant \(\pi\) satisfies \(Pf-f\le C-cw\) pointwise, with \(f,w\ge0\), \(Pf(x)<\infty\) at each state and \(c>0\), put \(f_R=\min\{f,R\}\). At states where \(f\ge R\), \(Pf_R-f_R\le0\); at other states \(Pf_R-f_R\le Pf-f\le C-cw\). Integrating the bounded drift \(Pf_R-f_R\) under \(\pi\) yields \(c\int_{\{f<R\}}w\,d\pi\le C\), and monotone convergence yields \(\pi w<\infty\). The finite exceptional states in the preceding asymptotic drift inequalities are absorbed into \(C\).

**2. Exact invariant transform.** The geometric offspring probability-generating function is \(F(t)=1/(2-t)\). For each state \(x\ge0\) and \(0\le t\le1\),
\[
\mathbb E[t^{V_{n+1}}\mid V_n=x]
=p^{x+1}+tq\sum_{k=0}^x p^kF(t)^{x+1-k}.
\]
Let \(\Phi(t)=\mathbb E_{\pi_p}t^V\) and \(B=p\Phi(p)=\pi_p(0)\). Set \(g(h)=\Phi(1-h)\), where \(0<h<q/p\). A geometric-series sum and stationarity give the exact functional equation
\[
(1-ah)g(h)=\frac{1-h}{1+h}g\!\left(\frac{h}{1+h}\right)+(1-a)Bh.\tag{1}
\]
The equality is exact, not a formal Taylor approximation.

**3. First-moment boundary.** If \(m=\mathbb E_{\pi_p}V<\infty\), then \(g(h)=1-mh+o(h)\), \(g'(h)=-m+o(1)\), and
\[
g(h)-g(h/(1+h))=-mh^2+o(h^2).
\]
Subtract the right-hand \(g\)-term from (1), collecting the difference using \(w(h)=(1-h)/(1+h)\):
\[
[(1-ah)-w(h)]g(h)+w(h)[g(h)-g(h/(1+h))]=(1-a)Bh.\tag{2}
\]
Comparison of coefficients of \(h\) and \(h^2\) gives
\[
B=\frac{a-2}{a-1},\qquad (a-3)m=2.\tag{3}
\]
Since \(m\ge0\), a finite first moment is impossible for \(a\le3\). For \(a>3\), the drift argument establishes finiteness and (3) gives \(m=2/(a-3)=2(1-p)/(4p-3)\). This restates the known first-moment result for orientation.

**4. Second-moment boundary and evaluation.** Suppose \(\mathbb E_{\pi_p}V^2<\infty\), so \(a>3\) by step 3. Write \(f=\mathbb E_{\pi_p}[V(V-1)]\). Second-moment integrability gives the one-sided expansions
\[
g(h)=1-mh+\frac f2h^2+o(h^2),\quad
g'(h)=-m+fh+o(h),
\]
\[
g(h)-g(h/(1+h))=-mh^2+(m+f)h^3+o(h^3).
\]
The coefficient of \(h^3\) in (2) yields
\[
(a-4)f=4+10m.\tag{4}
\]
Its right-hand side is strictly positive; hence for \(3<a\le4\), a finite second moment is impossible. The case \(a\le3\) was already excluded because a finite second moment implies a finite first moment. Conversely, for \(a>4\) the cubic Foster test establishes \(f<\infty\), so (3) and (4) are valid and give
\[
\mathbb E_{\pi_p}V^2=m+f
=\frac{6p(1-p)}{(4p-3)(5p-4)}.
\]
Subtracting \(m^2\) yields the displayed variance formula. The identities \(a>4\iff p>4/5\) and \(a>3\iff p>3/4\) prove the sharp threshold assertions. Multiplying the two rational formulas by \(p-4/5\) and taking the right limit gives \(24/25\) in both cases. This completes the proof.

## Verification
The supplementary standard-library Python program `check_moments.py` evaluates **773** independent exact-rational equalities for conditional first, second and third moments, the conditional generating function, and the stated stationary-moment algebra. It is invoked by `python3 check_moments.py` and its recorded successful output is `check_output.txt`. These computations guard against algebraic errors in the finite-state recurrences; they do not establish the invariant measure, moment finiteness, sharpness or uniqueness. All infinite claims follow from the drift argument and the exact transform in the proof.

## Relationship to prior work
Carper's arXiv:2609.06311 introduces exactly this process, proves recurrence properties, and computes the stationary mass at zero and stationary mean. The present claim concerns a higher moment **not stated in those inspected results**: the exact finite-variance boundary \(p=4/5\), a closed stationary second-moment formula, and its pole. It is not presented as a new recurrence theorem or as a new stationary-mean formula. Kosygina and Peterson's arXiv:1504.06280 develops broader excited-walk branching methods and excursion tail theory, but the inspected results do not give this chain's exact one-time stationary variance. The general branching-with-migration literature may yield moment criteria indirectly; a direct prior formula or a stronger implication has not been established from the compared material. This is a qualified originality claim, not an assertion of exhaustive historical priority.

## Limitations
The theorem assumes independent geometric emigration and geometric offspring exactly as defined, and applies to \(2/3<p<1\). It does not furnish the full invariant probability mass function, tail equivalences, higher moments, uniform convergence rates, or excursion-area variance. The moment formulas are same-work analytical deductions; they have not been independently certified. The exact moment threshold may be implied by broader earlier migration-process theorems not isolated here.

## References
1. Patrick Carper, *A Branching Process with Geometric Emigration and the "Have Your Cookie and Eat It" Random Walk*, arXiv:2609.06311v1 (first public 2026-09-05), https://arxiv.org/abs/2609.06311.
2. Elena Kosygina and Jonathon Peterson, *Excited random walks with Markovian cookie stacks*, arXiv:1504.06280 (2015), https://arxiv.org/abs/1504.06280.
3. Thierry E. Huillet, *On the Balance between Emigration and Immigration as Random Walks on Non-Negative Integers*, Mathematics 12(20), 3198 (2024), https://doi.org/10.3390/math12203198. This reference examines distinct migration mechanisms and does not supply the current recurrence.
