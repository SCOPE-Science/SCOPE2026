# A sharp premium-price threshold for minimax hitting times on symmetric stars

## Finding

Let \(k\ge3\) be an integer. Consider the star with center \(0\) and leaves \(1,\ldots,k\). Its continuous-time Markov generator has rate \(r_i>0\) in **both** directions along edge \(\{0,i\}\). Independently choose all \(r_i\), subject to \(\sum_{i=1}^k p_i r_i\le B\), where \(p_i>0\) and \(B>0\). Minimize the largest ordered-pair mean first-hitting time
\[
T(r)=\max_{s\ne t}\mathbb E_s\tau_t.
\]
Put \(p=\max_i p_i\), \(P=\sum_i p_i-p>0\). There is exactly one optimal rate vector, and its optimum value is
\[
\boxed{T_*=\frac{(k+1)(p+P)-(\sqrt p-\sqrt{kP})_+^2}{B}},
\qquad (u)_+=\max\{u,0\}.
\]
More precisely:

* If \(p\le kP\), the unique optimum is the **uniform rate vector**
  \[
  r_i^*=\frac B{p+P}\quad(1\le i\le k),\qquad
  T_*=\frac{(k+1)(p+P)}B.
  \]
* If \(p>kP\), the maximum-priced leaf \(h\) is unique. Set \(t=\sqrt{p/(kP)}>1\). Then the unique optimum is
  \[
  r_h^*=\frac B{p+Pt},\qquad
  r_i^*=\frac B{P+p/t}\quad(i\ne h),
  \]
  and
  \[
  T_*=\frac{kp+P+2\sqrt{kpP}}B.
  \]

In particular, the advantage over the unique equal-rate allocation is exactly
\[
\boxed{T_{\rm equal}-T_*=\frac{(\sqrt p-\sqrt{kP})_+^2}{B}}.
\]
Thus the price threshold depends only on the largest individual price and the sum of all others: arbitrary smaller-price heterogeneity does not change the form of the optimizer. For example, with \(k=3\), \(B=1\), and prices \((54,1,1)\), the premium edge receives rate \(1/60\), the other two rates are \(1/20\), and \(T_*=200\), compared with \(T_{\rm equal}=224\).

## Assumptions and scope

The chain is time-homogeneous, irreducible, and reversible with uniform stationary mass on its \(k+1\) states. The generator satisfies \(Q_{0i}=Q_{i0}=r_i\), \(Q_{ii}=-r_i\) for leaves and \(Q_{00}=-\sum_i r_i\); all other off-diagonal entries vanish. The first-hitting time \(\tau_t=\inf\{u\ge0:X_u=t\}\) includes zero when the start is already the target, but only distinct ordered pairs enter the maximum. No other transitions or self-loop controls are allowed. All prices, budgets and rates have the stated strict sign conditions.

## Proof

**1. Exact hitting-time identity.** Write \(H_{st}=\mathbb E_s\tau_t\). For a leaf \(i\), \(H_{i0}=1/r_i\). For a fixed target leaf \(j\), the first-step equations at the center and other leaves are
\[
H_{0j}=\frac1{\sum_i r_i}+\sum_{\ell\ne j}\frac{r_\ell}{\sum_i r_i}H_{\ell j},
\qquad H_{\ell j}=\frac1{r_\ell}+H_{0j}.
\]
Substitution yields \(r_jH_{0j}=1+(k-1)=k\), hence
\[
H_{0j}=\frac{k}{r_j},\qquad
H_{ij}=\frac1{r_i}+\frac{k}{r_j}\quad(i\ne j\text{ leaves}).
\]
For \(x_i=1/r_i>0\), arrange the waiting times decreasingly as \(x_{(1)}\ge x_{(2)}\ge\cdots\ge x_{(k)}\). Since \(k\ge2\), maximizing over ordered distinct leaves, and then comparing center-involving pairs, gives exactly
\[
\boxed{T(r)=kx_{(1)}+x_{(2)}}.
\]
The budget is equivalently \(\sum_i p_i/x_i\le B\). The equal-rate feasible vector gives a finite comparison value \(M\). Every feasible rate vector with \(T(r)\le M\) has \(r_i\ge k/M\), because \(H_{0i}=k/r_i\), and also \(r_i\le B/p_i\). Thus the relevant sublevel set is compact and a global minimizer exists. At an optimum the budget is saturated: if the inequality were strict, a common decrease of every waiting time would improve the objective while remaining feasible.

**2. All but at most one waiting time coincide.** Suppose some \(x_i<x_{(2)}\) at an optimum. Replace it by \(x_{(2)}\). Neither of the two largest order statistics changes, so \(T\) is unchanged, but the positive term \(p_i/x_i\) in the budget falls strictly. A small common decrease of all waiting times restores budget equality while strictly decreasing \(T\), a contradiction. Therefore every waiting time other than a possible single strictly largest one equals the common level \(x>0\). This also covers ties for the largest level, when all waiting times must coincide.

**3. Location of a possible exceptional edge.** If a unique larger waiting time \(tx\), \(t>1\), is assigned to leaf \(h\) while \(p_h<p_j\) for some other leaf \(j\), exchanging these two waiting times leaves \(T\) unchanged and strictly reduces the budget expenditure:
\[
\frac{p_h}{x}+\frac{p_j}{tx}
-\left(\frac{p_h}{tx}+\frac{p_j}{x}\right)
=\frac{(p_h-p_j)(1-1/t)}x<0.
\]
Here the left-hand cost corresponds to placing the larger waiting time at \(j\), whereas the parenthesized cost places it at \(h\); thus, for an initially cheaper \(h\), reassigning the larger waiting time to the more expensive \(j\) decreases cost. The resulting slack again permits a strict common improvement. Hence any exceptional leaf must carry maximal price \(p\).

**4. Scalar optimization and uniqueness.** Let \(P>0\) sum the prices on the other leaves. With a maximal-price exceptional leaf and ratio \(t\ge1\), budget saturation forces
\[
x=\frac{P+p/t}{B},\qquad
T(t)=(kt+1)x
=\frac{kp+P+kPt+p/t}{B}.
\]
The first two terms are independent of \(t\), while the remaining terms are strictly convex for \(t>0\):
\[
T'(t)=\frac{kP-p/t^2}{B},\qquad
T''(t)=\frac{2p}{Bt^3}>0.
\]
Thus the unique minimizer over \(t\ge1\) is \(t_*=\max\{1,\sqrt{p/(kP)}\}\). For \(p\le kP\), the minimizer is \(t=1\), which is the same equal-rate vector regardless of which maximally priced leaf was provisionally selected. For \(p>kP\), the maximizing price must be unique, because a second price \(p\) would imply \(P\ge p\), contradicting \(p>kP\). The unique exceptional index and the strict scalar minimizer yield uniqueness among **all** independently chosen positive rate vectors.

Finally, substitution of \(t_*\) gives the piecewise formulas. Subtracting the premium-regime value from the equal-rate value gives \((\sqrt p-\sqrt{kP})^2/B\), proving the unified positive-part formula, including equality at the threshold. Every optimizer is strictly positive and spends exactly \(B\).

## Verification

The standalone Python 3 program `verify.py` performs independent Gaussian elimination over rational numbers on finite symmetric-star generators and compares every ordered hitting time with the formula above. It also checks budgets, claimed objectives, and deterministic competing allocations over several sizes, prices, and both threshold regimes. Executing `python3 verify.py` yields `VERIFY_OK 249020 checks`. These finite calculations are supplemental; the proof above is exact and applies to all positive real inputs and all integers \(k\ge3\).

## Relationship to prior work

Aldous and Fill's 1999/2002 notes establish broad hitting-time identities and earlier unweighted extremal results for star trees, but do not provide this arbitrary-positive-price rate-allocation threshold. Sun, Boyd, Xiao, and Diaconis (electronically published November 2, 2006) analyze a symmetric continuous-time chain with a linear conductance budget, but optimize the **spectral gap** rather than the worst ordered hitting time. Zeng (2021) studies **average** hitting time over weighted trees when an edge-weight multiset is fixed; this has neither the objective nor the decision variables used here. Berman's 1964 PERT allocation framework is a broad predecessor for resource-cost optimization; its accessible abstract does not resolve this exact stochastic-star theorem, but its inaccessible full text leaves an explicit priority uncertainty. The present claim concerns the stated sharp price-dominance threshold and complete unique optimizer, not the general existence of hitting-time formulas or convex resource-allocation methods.

## Limitations

This theorem is restricted to symmetric rates on a fixed star, positive linear rate prices, and worst **mean first-hitting times between states**. It does not optimize cover times, stationary-random-target times, commute times, spectral gaps, asymmetric generators, or general trees. Historical priority beyond the inspected literature remains uncertain; the accessible comparisons do not establish universal novelty.

## References

1. D. Aldous and J. A. Fill, *Reversible Markov Chains and Random Walks on Graphs*, unfinished monograph (1999–2002), Chapters 2.2, 3.7 and 5.3. https://www.stat.berkeley.edu/users/aldous/RWG/Book_Ralph/book.html
2. J. Sun, S. Boyd, L. Xiao and P. Diaconis, “The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem,” *SIAM Review* **48** (2006), 681–699. First public electronic date: November 2, 2006. https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf
3. J. Zeng, “On average hitting time and Kemeny's constant for weighted trees,” arXiv:2109.09249 (September 19, 2021). https://arxiv.org/abs/2109.09249
4. E. B. Berman, “Resource Allocation in a PERT Network Under Continuous Activity Time-Cost Functions,” *Management Science* **10** (1964), 734–745. https://doi.org/10.1287/mnsc.10.4.734
