# Sharp unique-maximum probability under fixed Bernoulli marginals and union probability

## Finding
For any integer \(d\ge2\), let \(A_1,\ldots,A_d\) be events with \(\Pr(A_i)=p_i\in[0,1]\). Their union probability is prescribed as \(q=\Pr(\cup_i A_i)\). Let \(N=\sum_{i=1}^{d}\mathbf1_{A_i}\), \(S=\sum_i p_i\), and \(y=S-q\). Define
\[
s_*:=\min\left\{s\in[0,q]: \sum_{i=1}^d\min\{p_i,s\}-s\ge y\right\}.
\]
The exact range over **all couplings with these data** is
\[
\boxed{\max\{0,2q-S\}\ \le\ \Pr(N=1)\ \le\ q-s_* .}
\]
Both endpoints are attained by probability laws on subsets of \(\{1,\ldots,d\}\), and all intermediate values are attained. A sort-and-scan implementation finds \(s_*\) in \(O(d\log d)\) arithmetic operations by checking the breakpoints \(0,p_1,\ldots,p_d,q\). Thus the probability that a Bernoulli maximum of value \(1\) is attained at a unique coordinate has a completely explicit sharp envelope.

The upper endpoint genuinely detects heterogeneity beyond the union and the marginal sum: at \(d=3\), \(q=19/20\) and \(S=19/10\), the marginal vectors \((9/10,9/10,1/10)\) and \((19/30,19/30,19/30)\) yield upper bounds \(1/10\) and \(19/40\), respectively. Both lower bounds are zero.

## Assumptions and scope
Here \(d\ge2\) is an integer; probabilities satisfy \(0\le p_i\le1\) and the familiar necessary and sufficient feasibility conditions
\[
\max_i p_i\le q\le\min\left\{1,\sum_i p_i\right\}.
\]
No independence, equal-marginal, regularity, or exchangeability assumption is made. All probability laws can be finitely supported. If \(q=0\), all marginals vanish and both endpoints are zero. If \(y=0\), the events may be disjoint and \(s_*=0\), giving the singleton probability \(q\).

## Proof
**1. An integer-slice convex-hull lemma.** For integers \(0\le a\le b\le d\),
\[
\operatorname{conv}\{\mathbf1_B:B\subseteq\{1,\ldots,d\},\ a\le |B|\le b\}
=\{x\in[0,1]^d:a\le\sum_i x_i\le b\}.
\]
Indeed, any vertex of the right-hand polytope is integral. If at least two coordinates are fractional, a small positive/negative exchange of those coordinates preserves their sum and constraints, contradicting extremality. If exactly one is fractional, either the sum constraints are slack, allowing a one-coordinate perturbation, or an integer endpoint \(a\) or \(b\) is tight, forcing the remaining coordinate to be integral as well. This covers equality and degenerate cases. The asserted convex hull follows.

**2. Lower bound and attainment.** On every nonzero outcome \(N\ge1\), and with \(U=\Pr(N=1)\),
\[
S=\mathbb E N\ge U+2(q-U)=2q-U.
\]
Hence \(U\ge\max\{0,2q-S\}\). For \(q>0\), the vector \((p_1/q,\ldots,p_d/q)\) lies in \([0,1]^d\) and has sum \(S/q\ge1\). If \(S\le2q\), the convex-hull lemma with \(1\le|B|\le2\) produces a conditional distribution of nonempty subsets with these inclusion marginals and support only on singleton and two-element sets. It has \(U=2q-S\). If \(S\ge2q\), use the lemma with \(2\le|B|\le d\), giving \(U=0\). Put probability \(1-q\) on the empty set in both cases. This yields all required marginals and exactly the prescribed union probability.

**3. Upper bound.** Write \(s=\Pr(N\ge2)=q-U\), and for each coordinate let \(z_i=\Pr(A_i\cap\{N\ge2\})\). Then
\[
0\le z_i\le\min\{p_i,s\},\qquad \sum_i z_i=S-U=S-q+s=y+s.
\]
Consequently \(\sum_i\min\{p_i,s\}-s\ge y\), so \(s\ge s_*\) and \(U\le q-s_*\). The defining set for \(s_*\) is nonempty because at \(s=q\) its left side is \(S-q=y\), since every \(p_i\le q\). Continuity ensures a minimum; when \(y>0\), continuity and the zero value at \(s=0\) give equality at \(s=s_*\).

**4. Upper-bound attainment and the key inequality.** One always has \(s_*\le y\): this is automatic if \(y\ge q\). If \(0<y<q\) and \(p_{\max}<y\), then \(\sum_i\min(p_i,y)-y=S-y=q>y\). If \(p_{\max}\ge y\), the other marginals total at least \(y\) because \(\sum_{i\ne\max}p_i=y+q-p_{\max}\ge y\). Therefore \(\sum_{i\ne\max}\min(p_i,y)\ge y\), and after including the largest coordinate, \(\sum_i\min(p_i,y)-y\ge y\). In either case \(s=y\) is feasible, proving \(s_*\le y\).

For \(y>0\) set \(s=s_*\), \(z_i=\min(p_i,s)\), and \(t_i=p_i-z_i=(p_i-s)_+\). Equality in the defining equation gives
\[
\sum_i z_i=y+s\ge2s,\qquad \sum_i t_i=q-s,\qquad 0\le z_i\le s.
\]
By the integer-slice lemma with \(2\le|B|\le d\), the normalized vector \((z_i/s)_i\) is the vector of inclusion probabilities of a random subset of cardinality at least two. Give this law total mass \(s\), give singleton subset \(\{i\}\) mass \(t_i\), and give the empty set mass \(1-q\). The result has marginals \(p_i\), union probability \(q\), and \(U=q-s_*\). The case \(y=0\) is achieved by disjoint singleton events with probabilities \(p_i\).

**5. Every intermediate value.** Convexly mix the lower- and upper-extremal joint laws. Each mixture retains every \(p_i\) and \(q\); its singleton probability interpolates linearly between the endpoints. This concludes the proof.

## Verification
The independent exact-rational verifier `verify_bounds.py` enumerates all feasible three-coordinate instances on the grid \(\{0,1/4,1/2,3/4,1\}\), and computes extrema by enumerating full-rank basic feasible solutions of the joint-law linear program over all eight binary outcomes. It matches the claimed formula on 190 feasible grid cases and recomputes the two heterogeneity examples using exact fractions. An additional random numerical linear-program comparison covering 600 instances of dimensions two through seven was performed during analysis; no random-comparison code is required for reproducibility of the embedded rational certificate. These finite tests are not used to infer the general case; the convex-hull argument above proves all dimensions.

To reproduce the packaged exact check, run `python3 verify_bounds.py` with a standard Python 3 interpreter in the same directory. The recorded output is in `CHECK_OUTPUT.txt`.

## Relationship to prior work
Ansari's *Couplings with prescribed maxima* (2026), Theorem 1, identifies which maximum distributions are attainable with fixed margins; for Bernoulli marginals it yields the feasibility conditions above, but not the sharp range of probability of an **isolated** maximizer. Bartl, Kupper, Lux and Papapantoleon (2018 preprint; 2022 journal), Corollary 2.5, establish a much broader optimal-transport **duality** for arbitrary bounded upper-semicontinuous payoffs subject to a prescribed maximum. That variational theorem encompasses the finite optimization problem abstractly, but does not supply the stated explicit order-statistic-of-marginals / water-filling envelope or its finite-support extremizers. The claimed contribution is the closed-form solution of this particular dual optimization, not the existence of a dual.

Prékopa (1990) and Boros–Prékopa (1989) develop sharp event-count bounds using binomial-moment information and linear programs. In contrast, the present constraints specify each labeled marginal separately **and** the union probability; the explicit heterogeneity example shows why reducing these data to a first moment loses information. Pinelis (2021) studies exactly-one bounds in a different class with symmetric event probabilities and pairwise-independence information; neither of those assumptions is imposed here.

## Limitations
The formula is finite-dimensional and applies to Bernoulli maxima, not arbitrary real-valued maxima or general unique-argmax distributions. Exact historical priority of this explicit specialization has not been independently established; a formula may be implicit in broader event-bound or optimal-transport literature. The algorithm assumes exact real arithmetic on the input probabilities; bit complexity is not asserted. No independent mathematical audit has been performed.

## References
- J. Ansari, *Couplings with prescribed maxima: A short proof of the quasi-copula characterization*, arXiv:2610.30642v1 (first public 22 October 2026), https://arxiv.org/abs/2610.30642.
- D. Bartl, M. Kupper, T. Lux and A. Papapantoleon, *Marginal and dependence uncertainty: bounds, optimal transport, and sharpness*, arXiv:1709.00641v2, https://arxiv.org/abs/1709.00641; SIAM Journal on Control and Optimization **60** (2022), 410–434.
- A. Prékopa, *Sharp Bounds on Probabilities Using Linear Programming*, Operations Research **38** (1990), 227–239, https://doi.org/10.1287/opre.38.2.227.
- E. Boros and A. Prékopa, *Closed Form Two-Sided Bounds for Probabilities that At Least r and Exactly r Out of n Events Occur*, Mathematics of Operations Research **14** (1989), 317–342, https://doi.org/10.1287/moor.14.2.317.
- I. Pinelis, *Exact lower bound on an "exactly one" probability*, arXiv:2102.05170v1, https://arxiv.org/abs/2102.05170.
