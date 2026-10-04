# Sharp unanimity envelope for pairwise-independent Bernoulli trials
## Finding
Let \(n\ge 2\), and let \(X_1,\ldots,X_n\) be Bernoulli random variables with common success probability \(p\) that are pairwise independent. Define
\[
U_n(p)=\sup \Pr(X_1=\cdots=X_n),\qquad q=\min(p,1-p).
\]
Then \(U_n(p)=1\) when \(q=0\). For \(0<q\le 1/2\), the sharp value is as follows.

If \(n\) is even and
\[
q\ge \frac{n-2}{2(n-1)},
\]
then
\[
U_n(p)=\frac1n+4\left(1-\frac1n\right)\left(p-\frac12\right)^2.
\]
In every other case, put \(r=\lceil (n-1)q\rceil\). Then
\[
U_n(p)=\frac{n(n-1)q^2-2nrq+r(r+1)}{r(r+1)}.
\]
The formulas agree at the even-case transition points. In particular,
\[
U_n(1/2)=
\begin{cases}
1/(n+1),& n\text{ odd},\\
1/n,& n\text{ even}.
\end{cases}
\]
Thus the fair case has an exact parity effect. For even \(n\), a nontrivial central interval is genuinely two-ended: an extremizer places mass on both unanimous outcomes and on the midpoint success count.

## Assumptions and scope
Only identical Bernoulli marginals and pairwise independence are assumed; joint exchangeability is not assumed. The event of interest and all pairwise-moment constraints are permutation invariant, so averaging any feasible law over coordinate permutations preserves feasibility and the unanimity probability. It is therefore enough to optimize over exchangeable laws.

Write
\[
K=\sum_{i=1}^n X_i.
\]
For an exchangeable feasible law, pairwise independence is equivalent to
\[
\mathbb E K=np,\qquad \mathbb E[K(K-1)]=n(n-1)p^2.
\]
Conversely, any probability law on \(\{0,1,\ldots,n\}\) satisfying these two moment equations yields a feasible exchangeable Bernoulli law by conditioning uniformly on binary strings with the specified value of \(K\).

## Proof
By complementing every bit, it is enough for the first branch argument to treat \(0<p\le 1/2\); afterward replace \(p\) by \(q\).

For the outer branch define \(r=\lceil(n-1)p\rceil\) and the quadratic
\[
H_r(k)=\frac{(k-r)(k-r-1)}{r(r+1)}.
\]
For every integer \(k\in\{0,1,\ldots,n\}\), the product of the two consecutive integer factors in the numerator is nonnegative. Also \(H_r(0)=1\). On the outer branch one has \(r\le (n-1)/2\), hence
\[
H_r(n)=\frac{(n-r)(n-r-1)}{r(r+1)}\ge 1.
\]
Therefore
\[
\mathbf 1_{\{0,n\}}(k)\le H_r(k)
\]
for every allowed integer \(k\). Taking expectations and using the two factorial moments gives
\[
\Pr(K\in\{0,n\})
\le
\frac{n(n-1)p^2-2nrp+r(r+1)}{r(r+1)}.
\]
This is attained by a law supported on \(\{0,r,r+1\}\) with weights
\[
a_0=\frac{n(n-1)p^2-2nrp+r(r+1)}{r(r+1)},
\]
\[
a_r=\frac{np\,[r-(n-1)p]}{r},\qquad
a_{r+1}=\frac{np\,[(n-1)p-r+1]}{r+1}.
\]
The definition of \(r\) makes all three weights nonnegative. Direct substitution shows that they sum to \(1\) and have factorial moments \(np\) and \(n(n-1)p^2\). The resulting exchangeable binary law is therefore pairwise independent and has unanimity probability \(a_0\). Complementation supplies the symmetric construction for \(p>1/2\).

It remains to handle the central branch, which occurs only for even \(n\). Write \(n=2m\). Use
\[
H_c(k)=\frac{(k-m)^2}{m^2}.
\]
This polynomial equals \(1\) at \(k=0\) and \(k=n\), and is nonnegative at every interior count, so it majorizes the unanimity indicator. Since pairwise independence gives \(\operatorname{Var}(K)=np(1-p)\),
\[
\mathbb E H_c(K)
=\frac{np(1-p)+(np-m)^2}{m^2}
=\frac1n+4\left(1-\frac1n\right)\left(p-\frac12\right)^2.
\]
For
\[
\frac{m-1}{2m-1}\le p\le \frac{m}{2m-1},
\]
equality is attained by a law on \(\{0,m,n\}\) with weights
\[
a_0=\frac{(1-p)[m-(2m-1)p]}{m},
\]
\[
a_m=\frac{2(2m-1)p(1-p)}{m},
\]
\[
a_n=\frac{p[(2m-1)p-m+1]}{m}.
\]
These weights are nonnegative exactly on the displayed interval, sum to \(1\), and have the required two factorial moments. This interval is equivalent to \(q\ge (n-2)/(2(n-1))\), proving the central branch and completing the sharpness argument.

## Verification
The proof is symbolic and does not depend on computation. As an independent finite check of the algebra and branch boundaries, the accompanying script `verify_unanimity.py` enumerates every three-support vertex of the success-count moment polytope using exact rational arithmetic for \(693\) parameter cases with \(2\le n\le 12\). It checks that the displayed formula equals the vertex optimum, that the proposed extremal weights are nonnegative, and that their first two factorial moments are exact. The run terminates with `CHECK_OK`.

## Relationship to prior work
Peled, Yadin, and Yehudayoff reduce the identical-marginal bounded-independence problem for the single endpoint \(K=n\) to a discrete moment problem and develop polynomial bounds for that objective. Benjamini, Gurel-Gurevich, and Peled give a broader linear-programming and polynomial-sandwich framework for Boolean functions under bounded independence. Those frameworks motivate the present reduction, but the targeted inspection did not locate the two-endpoint unanimity envelope above or its even-versus-odd phase structure.

Kwerel's classical work gives sharp bounds for individual exact-count probabilities and other aggregated event probabilities from low-order occurrence sums. More recent exact work on pairwise-independent bits again treats the single endpoint \(K=n\). Separate single-endpoint maxima do not by themselves imply the sharp maximum of \(\Pr(K=0)+\Pr(K=n)\): in the even central interval the optimizer simultaneously uses both endpoints, and its quadratic majorant is centered at \(n/2\).

## Limitations
The result is restricted to common Bernoulli marginals and pairwise independence. It does not treat heterogeneous success probabilities, higher-order independence, minima of unanimity probability, restrictions on the underlying sample-space size, or other two-tail events. The literature comparison used targeted semantic searches and direct inspection of the most relevant accessible sources; an older result stated in different terminology could have been missed. The novelty conclusion should therefore be read as a documented search result rather than a publication-level guarantee of priority.

## References
1. R. Peled, A. Yadin, and A. Yehudayoff, “The maximal probability that \(k\)-wise independent bits are all 1,” *Random Structures & Algorithms* 38 (2011), 502–525. DOI: 10.1002/rsa.20329. First public preprint: arXiv:0801.0059, 2007-12-31.
2. I. Benjamini, O. Gurel-Gurevich, and R. Peled, “On \(k\)-wise independent distributions and Boolean functions,” arXiv:1201.3261, 2012.
3. S. M. Kwerel, “Most stringent bounds on aggregated probabilities of partially specified dependent probability systems,” *Journal of the American Statistical Association* 70 (1975), 472–479. DOI: 10.1080/01621459.1975.10479893.
4. D. Berend, P. A. Ernst, A. Kontorovich, and R. Kumar, “Exact expressions for the maximal probability that all \(k\)-wise independent bits are 1,” arXiv:2407.18688, 2024.
