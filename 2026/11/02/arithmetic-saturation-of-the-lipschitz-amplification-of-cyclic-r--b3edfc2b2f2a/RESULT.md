# Arithmetic saturation of the Lipschitz amplification of cyclic running medians

## Finding
Let \(r\ge 1\) and \(n\ge 2r+1\) be integers, and let \(T_{n,r}:\mathbb R^n\to\mathbb R^n\) replace each coordinate by the median of the \(2r+1\) distinct coordinates in its centered cyclic window. For \(1\le p<\infty\), define
\[
L_p(n,r)=\sup_{x\ne y}\frac{\|T_{n,r}x-T_{n,r}y\|_p}{\|x-y\|_p}.
\]
Every such operator satisfies \(L_p(n,r)\le (2r+1)^{1/p}\). The following is a necessary and sufficient **arithmetic classification of equality**.

Write \(m=2r+1\). When \(n=m\), equality holds. When \(n>m\), put \(k=n-m\) and divide \(2r=qk+t\), with integers \(q\ge0\), \(0\le t<k\). Then
\[
\boxed{L_p(n,r)=m^{1/p}\ \Longleftrightarrow\ \exists\ a,b\in\mathbb Z:\ 0\le a\le t,\ 0\le b\le k-t,\ a(q+1)+bq=r.}
\]
The equivalence holds simultaneously for every finite \(p\); the equality is realized by an arbitrarily small perturbation of a single coordinate at an input with distinct entries. The complementary strict cases satisfy \(L_p(n,r)<m^{1/p}\).

Consequences with **exact** norms are:
\[
\begin{aligned}
&L_p(n,r)=m^{1/p}&&\text{if }n\text{ is odd or }n\ge4r+1,\\
&L_p(2r+2,r)=(r+1)^{1/p},&&r\ge1,\\
&L_p(10,3)=6^{1/p}.&&
\end{aligned}
\]
At the other endpoint, \(L_\infty(n,r)=1\) for all permitted parameters.

## Assumptions and scope
All inputs are real vectors; all norms are ordinary, unweighted \(\ell_p\) norms on the same \(n\) cyclic coordinates. Cyclic windows contain distinct sites, which is why \(n\ge2r+1\) is required. For odd length \(m\) the median is the uniquely determined middle order statistic even if data values tie. The global Lipschitz constant compares **two different input signals**, not merely the total variation of a single filtered signal. The theorem classifies precisely when the universal column-multiplicity bound is sharp; it does not claim a closed formula for every non-saturating pair \((n,r)\).

## Proof
**1. Local selectors give the exact reduction.** On each open chamber of \(\mathbb R^n\) where all input coordinates are distinct, the median in every window equals one of the input coordinates. Thus the map is linear there, with a selector matrix \(J\) having exactly one entry equal to \(1\) per row and all other entries zero. Let \(c_j\) be the number of rows selecting column \(j\). For \(1\le p<\infty\),
\[
\|Jh\|_p^p=\sum_{j=0}^{n-1}c_j|h_j|^p,
\qquad\|J\|_{p\to p}=(\max_jc_j)^{1/p}.
\]
The filter is a continuous, piecewise-linear map with finitely many chambers. Splitting any straight segment at its finitely many chamber transitions (or approximating a segment lying on ties) proves that the global Lipschitz constant is the largest norm of any chamber selector. Conversely a small coordinate perturbation entirely inside a maximizing chamber attains its local norm as a two-input quotient. A coordinate occurs in exactly \(m\) distinct cyclic windows, so \(c_j\le m\). Also every median is \(1\)-Lipschitz for \(\ell_\infty\), and a constant-input shift gives equality at \(p=\infty\).

**2. Saturation is a balancing problem.** By cyclic symmetry, fix selected coordinate \(0\). It is chosen by every one of the \(m\) windows containing \(0\) precisely when exactly \(r\) other values in each of those windows lie below \(x_0\), and exactly \(r\) lie above. Any assignment of these signs can be realized by distinct real data: set \(x_0=0\), put all designated lower values strictly below zero, and all upper values strictly above zero, with small distinct offsets. Thus \(\max_j c_j=m\) is equivalent to the existence of a binary coloring of vertices \(1,\ldots,n-1\) that has exactly \(r\) lower-colored vertices in every \(m\)-window containing vertex \(0\).

When \(n=m\), every window is the whole cycle, so choosing exactly \(r\) lower and \(r\) upper vertices works.

**3. Arithmetic classification when \(n>m\).** Put \(k=n-m\). The \(m\) windows containing vertex \(0\), written in order of their starting indices, start at \(-m+1,-m+2,\ldots,0\), modulo \(n\). Comparing two consecutive window counts removes a vertex \(s\in\{-m+1,\ldots,-1\}\) and inserts vertex \(s+m\). Their lower/upper indicators must agree. Since \(n=m+k\), these are precisely the constraints
\[
\chi_j=\chi_{j+k}\qquad(1\le j\le m-1),
\]
where \(\chi_i\in\{0,1\}\) denotes the indicator that \(x_i<x_0\). All such equalities are equivalent to \(\chi\) being constant on each of the \(k\) residue-class chains
\[
\{a,a+k,a+2k,\ldots\}\cap\{1,\ldots,n-1\},\qquad 1\le a\le k.
\]
The first window has, apart from vertex \(0\), the sites \(k+1,\ldots,n-1\). Its intersection with chain \(a\) contains
\[
w_a=\left\lfloor\frac{n-1-a}{k}\right\rfloor
=\begin{cases}q+1,&1\le a\le t,\\q,&t<a\le k,\end{cases}
\]
where \(2r=qk+t\). Consequently exactly \(r\) lower entries in the first window are possible if and only if one selects \(a\) of the \(t\) chains of weight \(q+1\) and \(b\) of the \(k-t\) chains of weight \(q\), giving \(a(q+1)+bq=r\). Once the first window is balanced, the chain equalities make all subsequent windows balanced. This proves both directions of the boxed criterion.

**4. Exact consequences.** If \(n>m\) is odd, then \(k\) is even. In the division \(2r=qk+t\), \(t\) is even, so choosing \(a=t/2\), \(b=(k-t)/2\) meets the criterion. If \(k\ge2r\), the weights \(w_a\) consist of \(2r\) ones and any remaining zeros, so choose \(r\) ones. This covers \(n\ge4r+1\). If \(n=m+1\), the \(m\) windows containing vertex \(0\) each omit exactly one of the other \(m\) vertices. With \(u\) lower-valued other vertices, the window is balanced exactly when the omitted value is upper and \(u=r\), or omitted lower and \(u=r+1\). In either case exactly \(r+1\) windows are balanced, and all other \(u\) give none. Hence the maximal selector-column count is \(r+1\), proving the second line of the exact norms.

For \((n,r)=(10,3)\), \(k=3\), \(q=2\), \(t=0\), so all three weights are \(2\). No subset sums to \(r=3\); thus at most six of the seven relevant windows can select one coordinate. Taking vertex \(0\) as zero, vertices \(1,3,4,6,7\) below zero and \(2,5,8,9\) above zero (with pairwise distinct magnitudes) balances the first six windows, centered at \(7,8,9,0,1,2\). Therefore the maximal multiplicity is six, and \(L_p(10,3)=6^{1/p}\).

## Verification
Run `python3 check_median.py` with Python 3 (standard library only). It independently enumerates all binary lower/upper assignments for 60 parameter pairs with \(n\le17\), compares the observed maximal selector multiplicity to the arithmetic criterion, tests the exact \(n=m+1\) and exceptional \((10,3)\) formulas, and checks the arithmetical consequences over 100 window widths. These finite computations are corroboration; Steps 1–4 prove the quantified theorem for every admissible \(n,r\) and all \(p\).

## Relationship to prior work
Arias-Castro and Donoho (first public preprint 2006) analyze the denoising risk and edge behavior of moving medians; those probabilistic mean-square rates do not supply the sharp two-input \(\ell_p\) Lipschitz saturation criterion. Suomela (2014) proves sorting-complexity equivalences for sliding medians; the sorting reduction is not a claim about the operator's perturbation norm. Median/stack-filter and variation-diminishing literature motivates attention to deterministic robustness, but one-signal total-variation descent, when available, does not imply a two-input \(\ell_p\) bound. A closely related previously recorded result for an endpoint-preserving path median concerns a **two-input weighted edge-variation seminorm**, not the cyclic coordinatewise \(\ell_p\) Lipschitz constant or its arithmetic saturation. The present result specifies those distinctions rather than claiming a general theory of nonlinear filters.

## Limitations
The general strict-side value \(L_p(n,r)\) is not determined here when the arithmetic criterion fails, except for the specified exact cases. The result does not treat even window widths, ties resolved by rules other than the usual odd median, noncyclic boundary conditions, unequal coordinate costs, iterative compositions, stochastic errors, or multidimensional image windows. Older stack-filter literature might encode an equivalent combinatorial saturation statement under different terminology; priority is therefore qualified rather than asserted absolutely. Independent external scientific audit has not been performed.

## References
1. E. Arias-Castro and D. L. Donoho, *Does median filtering truly preserve edges better than linear filtering?*, arXiv:math/0612422, first posted 2006-12-14; Annals of Statistics 37 (2009), 1172–1206. https://arxiv.org/abs/math/0612422
2. J. Suomela, *Median Filtering is Equivalent to Sorting*, arXiv:1406.1717, first posted 2014-06-06. https://arxiv.org/abs/1406.1717
3. W. Ye and Z. Liao, *Generalized Correlativity of Median Filtering Operator on Signals*, Open Journal of Discrete Mathematics 2 (2012), 83–87, DOI: 10.4236/ojdm.2012.23015.
