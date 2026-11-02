# Finite-population parity law for coordinate-wise median facility location in the Chebyshev plane

## Finding

For every integer \(n\ge 2\), let \(X=(a_1,\ldots,a_n)\in(\mathbb R^2)^n\) be any profile of \(n\) possibly coincident agents, with distance \(d_\infty(a,b)=\max\{|a_1-b_1|,|a_2-b_2|\}\). Let \(C(X)\) be its coordinate-wise median, breaking even-size median ties by the **lower** order statistic in each coordinate. Define \(S_X(z)=\sum_i d_\infty(a_i,z)\) and \(O(X)=\min_z S_X(z)\). Then the exact uniform ratio at each fixed population size is

\[
\sup_{X:O(X)>0}\frac{S_X(C(X))}{O(X)}=
\begin{cases}
2,& n\text{ even},\\
\dfrac{2n}{n+1},& n\text{ odd}.
\end{cases}
\]

The supremum is attained for every \(n\), even when all reports belong to the three-point set \(\{(-1,-1),(-1,1),(0,0)\}\). Thus odd populations enjoy a strictly better factor than the uniform sharp bound \(2\), whereas the factor \(2\) remains attained at each even population size.

## Assumptions and scope

One unconstrained facility is placed anywhere in the real plane; every agent's disutility is Chebyshev distance to the facility; social cost is the **sum**, not the maximum, of agents' disutilities. Agents have equal unit weight. Reports may coincide. The comparison optimum ranges over all real facility locations. The median is coordinate-wise and lower-tie-broken for even \(n\). All statements quantify over every finite profile of the stated cardinality; zero-optimum profiles have zero median cost and are excluded only from the quotient.

## Proof

**Optimal cost formula and existence.** Write \(a_i=(x_i,y_i)\), \(u_i=x_i+y_i\), and \(v_i=x_i-y_i\). The identity
\[
\max\{|s|,|t|\}=\tfrac12\bigl(|s+t|+|s-t|\bigr)
\]
shows that, with the invertible coordinates \(U=z_1+z_2\), \(V=z_1-z_2\),
\[
S_X(z)=\tfrac12\sum_i\bigl(|u_i-U|+|v_i-V|\bigr).
\]
Consequently, an optimum exists and is obtained by independently taking medians of \((u_i)\) and \((v_i)\), then using \(z=((U+V)/2,(U-V)/2)\).

**Even-population upper bound.** For any \(z\), \(\|w\|_\infty\le\|w\|_1\le2\|w\|_\infty\), and the coordinate-wise median minimizes \(\sum_i\|a_i-z\|_1\). Hence
\[
 S_X(C(X))\le\sum_i\|a_i-C(X)\|_1
 \le\sum_i\|a_i-z\|_1\le2S_X(z).
\]
This proves the factor \(2\) (in fact for all population sizes).

**Odd-population sharp upper bound.** Write \(n=2k+1\), \(k\ge1\), and \(R=n/(k+1)=2n/(n+1)\). Translate all reports so that their coordinate-wise median is the origin. Each coordinate then has **at most \(k\) strictly positive reports**, regardless of repeated or zero coordinates. To show \(\sum_i\|a_i\|_\infty\le R\sum_i\|a_i-z\|_\infty\) for every candidate location \(z\), the case \(z=0\) is immediate. Otherwise reflect and interchange coordinates, preserving the median and all Chebyshev distances, and scale by a positive constant so that \(z=(1,t)\) with \(0\le t\le1\).

For one report \(a=(x,y)\), put \(r=\max\{|x-1|,|y-t|\}\), \(s=\max\{|x|,|y|\}\), and \(f=Rr-s\). Set \(c=R-1+t\), \(A=R+(2-R)t\), and \(B=2t\); these last two quantities are nonnegative. The following pointwise inequality holds:
\[
 f\ge c-A\mathbf1_{\{x>0\}}-B\mathbf1_{\{y>0\}}.\tag{*}
\]
Indeed, split into four sign regions (zero belongs to the nonpositive region):

* When \(x>0,y>0\), the right side is \(-1+(R-3)t\le-1\); the triangle inequality \(s\le r+1\) implies \(f\ge-1+(R-1)r\ge-1\).
* When \(x>0,y\le0\), the right side is \(-1+(R-1)t\); \(r\ge t\) and \(s\le r+1\) imply the inequality.
* When \(x\le0,y>0\), the right side is \(R-1-t\); \(r\ge1\) and \(s\le r+t\) imply \(f\ge(R-1)r-t\ge R-1-t\).
* When \(x\le0,y\le0\), the right side is \(R-1+t\); \(r\ge1\) and \(s\le r-t\) imply \(f\ge(R-1)r+t\ge R-1+t\).

Sum (*) over the \(2k+1\) agents. The two indicator sums are separately at most \(k\). Therefore,
\[
\sum_i\bigl(R\|a_i-z\|_\infty-\|a_i\|_\infty\bigr)
 \ge (2k+1)c-k(A+B)
 =\frac{t}{k+1}\ge0.
\]
Since this holds for every \(z\), it holds for an optimal facility. This proves the odd-size upper bound, without any compactness assumption on the reports beyond finiteness.

**Matching examples.** If \(n=2k+1\), take \(k\) agents at \((-1,-1)\), one at \((-1,1)\), and \(k\) at \((0,0)\). The unique coordinate-wise median is \((-1,0)\); its total cost is \(2k+1\), while the facility at \((0,0)\) costs \(k+1\). The upper bound forces this facility to be optimal, and the attained ratio is \((2k+1)/(k+1)\). If \(n=2k\), instead use \(k-1\) agents at \((-1,-1)\), one at \((-1,1)\), and \(k\) at \((0,0)\). The lower coordinate-wise median is again \((-1,0)\), with cost \(2k\), while the origin has cost \(k\). The preceding even upper bound forces the optimum to equal \(k\), giving factor \(2\). These constructions cover \(k=1\), too.

## Verification

The standalone script `verify.py` reconstructs \(O(X)\) independently from the 45-degree rotation formula, exhaustively enumerates unordered profiles on the nine-point grid \(\{-1,0,1\}^2\) for \(2\le n\le10\), checks sharpness witnesses at each size, tests 7,500 seeded random integer-coordinate profiles with up to 30 agents, and checks the pointwise inequality (*) on 38,808 rational test cases. Every finite test uses exact integer or rational arithmetic and has passed. These finite tests illustrate and regression-check the argument; the displayed proof covers all real profiles and all sizes.

To reproduce: `python verify.py` (Python standard library only).

## Relationship to prior work

Hastings, *Strategic Facility Location with p-Norm Social Costs* (first publicly posted June 10, 2026, arXiv:2606.12187), establishes the sharp **population-uniform** factor \(2\) in the planar Chebyshev-distance/utilitarian-cost case (the setting \(p=1\) and \(q=\infty\)). Its lower-bound analysis explicitly takes a limit in population size; its reduction also duplicates odd profiles when analyzing the upper bound. Neither an asymptotic factor \(2\) nor the duplication reduction determines the sharp constant for an independently fixed **odd** population. The present statement identifies all finite-population constants and their attaining profiles.

Goel and Hann-Caruthers, *Optimality of the coordinate-wise median mechanism for strategyproof facility location in two dimensions* (arXiv:2007.00903; *Social Choice and Welfare*, 2023), considers **Euclidean** individual distances, so its finite-odd formula addresses a different metric. Lin, *Optimality and Impossibility in Multidimensional Strategyproof Facility Location* (first posted October 27, 2026, arXiv:2610.36613), additionally studies Chebyshev-distance optimization and describes the uniform factor \(2\); the inspected text does not identify the finite-odd Chebyshev constant. This latter paper postdates the October 25 research anchor and is treated only as contemporaneous comparison, not as the initiating source.

## Limitations

The exact odd improvement relies on two-dimensional Chebyshev distance and **equal-weight, utilitarian** social cost. It does not establish corresponding finite-size constants for higher dimensions, other \(\ell_q\) metrics, unequal weights, multiple facilities, or social-cost norms other than the sum. The result evaluates the coordinate-wise median, not optimality among all strategyproof mechanisms. Literature searches and inspected sources do not establish absolute priority; related or unindexed results may exist. Independent external verification has not occurred.

## References

1. J. Hastings, *Strategic Facility Location with p-Norm Social Costs*, arXiv:2606.12187, first posted 2026-06-10, https://arxiv.org/abs/2606.12187 .
2. S. Goel and W. Hann-Caruthers, *Optimality of the coordinate-wise median mechanism for strategyproof facility location in two dimensions*, arXiv:2007.00903, https://arxiv.org/abs/2007.00903 .
3. J. Lin, *Optimality and Impossibility in Multidimensional Strategyproof Facility Location*, arXiv:2610.36613, first posted 2026-10-27, https://arxiv.org/abs/2610.36613 .
