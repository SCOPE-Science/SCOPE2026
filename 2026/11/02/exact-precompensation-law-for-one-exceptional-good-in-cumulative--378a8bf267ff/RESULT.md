# Exact precompensation law for one exceptional good in cumulative envy

## Finding

Two agents have **identical additive valuations** and receive an irrevocable allocation of a fixed, known sequence of goods. The values, in arrival order, are \(a\) copies of \(1\), one copy of \(H\), and \(b\) further copies of \(1\). Here \(a,b\) are arbitrary nonnegative integers and \(H\geq1\) is real. Each good must be assigned to exactly one agent at its arrival. Let \(z_t\) be the signed difference between their cumulative bundle values after round \(t\). Their cumulative maximum pairwise envy is \(E=\sum_{t=1}^{a+b+1}|z_t|\).

Set
\[
J_a=\{j\in\mathbb Z:-a\leq j\leq a,\ j\equiv a\pmod2\},\qquad
\delta_t(x)=\min_{0\leq k\leq t}|x-t+2k|\quad (x\geq0).
\]
The **exact optimum**, with the full future known but no reallocation or release-order choice, is
\[
\boxed{E^*(a,b,H)=\min_{j\in J_a}\left(\frac{a+j^2}{2}+|H-j|+\sum_{t=1}^{b}\delta_t(|H-j|)\right).}
\]
The formula gives a constructive finite procedure for *every* such sequence, including \(a=0\) or \(b=0\) and nonintegral \(H\).

There is a more explicit **midpoint-precompensation law** when \(H=m\) is a positive integer and \(a,b\geq m\). Define \(\epsilon\in\{0,1\}\) by \(\epsilon\equiv a+b-m\pmod2\). Then
\[
\boxed{E^*(a,b,m)=\frac{a+b+\epsilon}{2}+\frac{m^2}{4}
+\min_{\substack{0\leq j\leq m\\j\equiv a\pmod2}}\left(j-\frac m2\right)^2.}
\]
An optimal policy intentionally builds an imbalance of magnitude as close as the permitted parity lattice allows to \(m/2\), *against* the agent who will receive the large good. This may incur more early envy but lowers total envy after the exceptional arrival.

As a sharp asymptotic demonstration of foresight's value, put \(H=a=b=2h\), with integer \(h\geq1\). The exact optimum and the cost of **always allocating to a currently poorer agent** are respectively
\[
E^*=2h+2\left\lceil\frac{h^2}{2}\right\rceil,
\qquad E_{\rm greedy}=2h+2h^2,
\qquad \lim_{h\to\infty}\frac{E_{\rm greedy}}{E^*}=2.
\]
Thus, even when all but one good have the same value, myopic balance can asymptotically incur twice the cumulative envy of an optimal foresighted allocation. This statement is about the displayed family; no universal factor-two upper bound is asserted.

## Assumptions and scope

There are exactly two agents. They agree on every good's value; values are strictly positive, with unit scaling fixed as above. The whole order is known in advance, but an assigned good cannot subsequently move. Envy is the largest positive pairwise bundle-value difference after each prefix, not final envy, Nash welfare, or the number of envious agents. All integers \(a,b\geq0\) and all real \(H\geq1\) are covered by the first formula. The midpoint formula requires integer \(m\geq1\) and \(a,b\geq m\). The asymptotic claim concerns the explicit even-integer family only.

## Proof

**1. Reduce envy to a signed walk.** Since both valuations are identical, at every round exactly the poorer agent envies the richer (unless they tie). Therefore maximum pairwise envy equals \(|z_t|\), where each unit good changes \(z_t\) by \(+1\) or \(-1\), and the exceptional good changes it by \(+H\) or \(-H\). Relabel the agents if necessary so the exceptional change is \(+H\). After the first \(a\) unit goods the gap is \(-j\) for some \(j\in J_a\).

**2. Exact optimal cost of a unit prefix with prescribed endpoint.** Let \(z_0=0\) and let \(z_t-z_{t-1}\in\{-1,1\}\) for \(1\leq t\leq a\), with \(z_a=-j\). For each step,
\[
|z_t|\geq\frac{1+z_t^2-z_{t-1}^2}{2}.
\]
Indeed, if the step is upward, the right-hand side is \(z_t\); if downward, it is \(-z_t\). Summing telescopically gives \(\sum_{t=1}^{a}|z_t|\geq(a+j^2)/2\). Equality is attainable: perform \((a-|j|)/2\) cycles \(0,1,0\), then move monotonically from \(0\) to \(-j\) in \(|j|\) unit steps. All counts are nonnegative integers because \(j\in J_a\). The cost is exactly \((a+j^2)/2\).

**3. Exact optimal suffix, attained at every round simultaneously.** Immediately after the exceptional item, the gap is \(H-j\). Symmetry allows us to start the last \(b\) unit steps at \(x=|H-j|\geq0\). After exactly \(t\) unit steps, the possible gaps are \(x-t+2k\) with integer \(0\leq k\leq t\); hence the smallest possible absolute gap is \(\delta_t(x)\). A trajectory simultaneously attains these lower bounds at all \(t\): always move one unit toward zero, and once the gap enters \([0,1)\), alternate signs to obtain gaps with magnitudes \(x_0\) and \(1-x_0\), where \(x_0\) is the fractional remainder of the starting distance. If the gap reaches zero, alternate \(0,1,0\). Thus the minimum additional suffix cost is \(\sum_{t=1}^{b}\delta_t(x)\), without an incompatible choice across rounds. Adding the exceptional round and prefix cost and minimizing over \(J_a\) proves the first formula. The prescribed constructions concatenate to a valid allocation.

**4. Integer midpoint law.** For a nonnegative integer starting gap \(r\), include the current-round gap and the next \(b\) unit-round gaps in \(T_b(r)=r+\sum_{t=1}^{b}\delta_t(r)\). Explicitly,
\[
T_b(r)=\begin{cases}
\frac{r(r+1)}2+\left\lceil\frac{b-r}{2}\right\rceil,&0\leq r\leq b,\\
(b+1)r-\frac{b(b+1)}2,&r\geq b.
\end{cases}
\]
These formulas agree at \(r=b\), and their successive integer differences are nonnegative; therefore \(T_b(r)\) is nondecreasing on nonnegative integers.

In the minimum from step 3 with \(H=m\), a negative \(j\) can be reflected to \(-j\), leaving the prefix cost unchanged and weakly decreasing \(|m-j|\). Any \(j>m\) can be reduced in steps of two, retaining its parity and strictly lowering its squared prefix cost while never increasing the exceptional-round/suffix cost; the potential last step from \(m+1\) to \(m-1\) keeps \(|m-j|\) unchanged. Thus an optimum has \(0\leq j\leq m\). The parity-compatible set is nonempty because \(a\geq m\geq1\).

Now \(r=m-j\) satisfies \(0\leq r\leq m\leq b\). Write \(\epsilon\equiv b-r\pmod2\); because \(j\equiv a\pmod2\), \(\epsilon\equiv a+b-m\pmod2\) is independent of \(j\). The cost simplifies to
\[
\frac{a+j^2}{2}+T_b(m-j)
=\frac{a+b+\epsilon}{2}+\frac{j^2+(m-j)^2}{2}
=\frac{a+b+\epsilon}{2}+\frac{m^2}{4}
+\left(j-\frac m2\right)^2.
\]
Selecting the nearest parity-compatible integer to \(m/2\) proves the midpoint formula.

**5. Sharp asymptotic greedy separation.** With \(a=b=m=2h\), the midpoint lattice consists of even integers. Writing \(j=2r\), minimizing \((j-h)^2\) is equivalent to minimizing \(r^2+(h-r)^2\); the minimum of \(r^2+(h-r)^2\) is \(\lceil h^2/2\rceil\), so its contribution to the cost is \(2\lceil h^2/2\rceil\). Thus \(E^*=2h+2\lceil h^2/2\rceil\). A current-poorest assignment balances the first \(2h\) unit goods at every even prefix, so the gap before the heavy good is zero; afterward, the gap takes values \(2h,2h-1,\ldots,0\). Its prefix cost is \(h\), giving \(E_{\rm greedy}=h+\sum_{r=0}^{2h}r=2h+2h^2\). Their quotient tends to \(2\), as claimed.

## Verification

The standalone file `verify.py` independently performs exact-rational shortest-path optimization over all reachable signed gaps, and compares it to the structural formula for \(891\) combinations of \((a,b,H)\). It additionally checks \(480\) integer-midpoint cases and \(60\) even-integer asymptotic-family identities, with direct dynamic checks for small members. Run `python3 verify.py`. The expected output is `VERIFY_OK direct_dynamic_checks=891 integer_midpoint_checks=480 symmetric_witnesses=60`. These tests corroborate the identities over finite domains; the preceding argument proves the unbounded quantified assertions.

## Relationship to prior work

Goldberg, Robinson, and Teh introduced cumulative maximum envy for temporally allocated goods and gave a general pseudopolynomial algorithm for fixed agent count together with hardness and approximation results. The contribution here is not the general dynamic program: it is the single-exception closed formula, the integral midpoint precompensation law, and a concrete asymptotic factor-two loss of the prefix-greedy rule when the release order is fixed. Their \(3/2\)-approximation for two agents concerns a *different model* where the planner can choose the release order. Earlier temporal fairness work studies prefixwise EF1-type feasibility rather than the minimum area under the envy curve. Closely related results for unit/two-unit fixed orders and for freely chosen release order of one exceptional good are not equivalent to the claimed fixed-order formula with arbitrary \(H\). Full-text comparison with the primary 2026 manuscript was limited by access; this remains a priority risk, not a mathematical lemma.

## Limitations

This is a two-agent, identical-value, one-exceptional-item theorem. It does not cover arbitrary numbers or types of exceptional goods, heterogeneous values, uncertain future arrival, or a general approximation guarantee for the myopic policy. The computational checks are finite and do not themselves prove any infinite statement. The primary 2026 paper's abstract and introductory sections were accessible, but the complete manuscript and appendices could not be examined in this examination; possible overlap in uninspected sections is not excluded. Independent external review has not occurred.

## References

1. P. W. Goldberg, I. Robinson, and N. Teh, *Minimizing Cumulative Envy in Allocating a Sequence of Items*, arXiv:2610.09843 (public preprint October 7, 2026). https://arxiv.org/abs/2610.09843
2. *19th International Symposium on Algorithmic Game Theory* program, University of Augsburg, listing the same work as a September 16, 2026 paper presentation. https://www.uni-augsburg.de/de/fakultaet/fai/conferences/sagt-2026/
3. E. Elkind, A. Lam, M. Latifian, T. Y. Neoh, and N. Teh, *Temporal Fair Division of Indivisible Items*, arXiv:2410.14593 (2024). https://arxiv.org/abs/2410.14593
