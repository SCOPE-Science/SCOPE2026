# A single cycle-length sign transition for branching-point covariance in uniform random mappings

## Finding

Let \(n\ge2\), and sample a function \(f:\{1,\ldots,n\}\to\{1,\ldots,n\}\) uniformly from all \(n^n\) functions. Regard \(f\) as a directed graph whose edges are \(v\to f(v)\), including loops. Let \(C_r\) count directed cycles with exactly \(r\) distinct vertices and let \(B_2\) count vertices with **indegree exactly two** (two preimages, including the vertex itself when appropriate). Put \(a=(n-1)/n\), \(P_n(r)=(n-r)(n^2-n+r^2-r)\), and \(c_{n,r}=(n)_{\underline r}/(r n^r)\), for \(1\le r\le n\). Then

\[
\operatorname{Cov}(C_r,B_2)
=\frac{c_{n,r}a^{n-r-2}}{2n^2}
\left(P_n(r)-n^2(n-1)a^r\right).
\]

For every \(n\ge4\), there is a unique integer \(t_n\), with \(2\le t_n<n\), such that

\[
\operatorname{Cov}(C_1,B_2)=0,\qquad
\operatorname{Cov}(C_r,B_2)>0\ (2\le r\le t_n),\qquad
\operatorname{Cov}(C_r,B_2)<0\ (t_n<r\le n).
\]

There are no other covariance zeros. For \(n=2\), the signs at cycle lengths \(1,2\) are zero and negative; for \(n=3\), the signs at lengths \(1,2,3\) are zero, zero, and negative. Furthermore,

\[
\lim_{n\to\infty}\frac{t_n}{n}=\rho=0.5847243864796\ldots,
\]

where \(\rho\) is the unique root in \((\sqrt2-1,1)\) of

\[
(1-\rho)(1+\rho^2)e^\rho=1.
\]

Thus the dependence of global cycles on local branching points changes from positive to negative at one cycle-length threshold, asymptotically about \(58.47\%\) of the vertex set. This statement concerns the ordinary uniform mapping, not fixed-indegree or conditioned-connectivity models.

## Assumptions and scope

The sampling space consists of all functions with independent, uniform images. Cycles are oriented functional-graph cycles, each counted once regardless of its starting vertex; length-one cycles are allowed. Indegree counts all incoming directed edges, including loops. Covariance is with respect to the unconditional uniform mapping distribution. No asymptotic condition is required for the exact formula. The threshold assertion holds for every integer \(n\ge4\); the two smaller values are stated separately.

## Proof

Fix any prescribed oriented cycle on a specified set of \(r\) distinct vertices, and write \(m=n-r\). Its \(r\) prescribed arrows occur with probability \(n^{-r}\). Conditional on these arrows, the \(m\) remaining image choices are independent and uniform. Each vertex on the prescribed cycle has indegree \(1+\operatorname{Bin}(m,1/n)\), while each vertex outside the cycle has indegree \(\operatorname{Bin}(m,1/n)\). Consequently,

\[
\mathbb E[B_2\mid\text{the prescribed cycle}]
=\frac{rm}{n}a^{m-1}
+\frac{m^2(m-1)}{2n^2}a^{m-2},
\]

where a term with a zero combinatorial coefficient is defined as zero when \(m=0\) or \(m=1\). The unconditioned expectation is \(\mathbb E B_2=\frac{n-1}{2}a^{n-2}\). There are \((n)_{\underline r}/r\) possible oriented \(r\)-cycles, and their event indicators sum to \(C_r\). By linearity, \(\mathbb E C_r=c_{n,r}>0\), and \(\mathbb E[C_rB_2]=c_{n,r}\mathbb E[B_2\mid\text{one prescribed cycle}]\). Subtracting the product of means and using the polynomial identity

\[
2rm(n-1)+m^2(m-1)=m(n^2-n+r^2-r)
\]

gives the exact covariance formula. Its expression remains valid at \(m=0,1\) as an algebraic identity (\(a>0\)).

All factors outside the parentheses in the covariance are positive. Define \(F_n(r)=P_n(r)/a^r\) and \(H_n=n^2(n-1)\); the sign equals that of \(F_n(r)-H_n\). Direct algebra gives

\[
P_n(r+1)-aP_n(r)
=\frac r n\big(n^2-n-(2n-1)r-r^2\big),
\qquad 1\le r<n.
\]

The quadratic in parentheses is strictly decreasing in \(r\), so the positive sequence \(F_n(1),\ldots,F_n(n-1)\), followed by \(F_n(n)=0\), first increases and then decreases (allowing one flat step). Moreover, \(F_n(1)=H_n\), while \(F_n(2)>H_n\) precisely when \(n>3\), because \(P_n(2)-aP_n(1)=n-3\). Therefore, for \(n\ge4\), this unimodal sequence begins at equality, rises strictly above \(H_n\), and ultimately reaches zero. It crosses the level at most once on the decreasing side.

There is no further integer equality: if \(r\ge3\) and \(F_n(r)=H_n\), then the integer \(P_n(r)\) would equal \((n-1)^{r+1}/n^{r-2}\), impossible because \(n\) and \(n-1\) are coprime. The case \(r=2\) is nonzero for \(n\ge4\) by the preceding difference. Hence the asserted unique integer threshold and strictly signed intervals exist. Direct substitution handles \(n=2,3\).

For a fixed real \(x\in(0,1)\), set \(r=\lfloor nx\rfloor\). Then

\[
\frac{F_n(r)}{n^3}\longrightarrow (1-x)(1+x^2)e^x,
\qquad
\frac{H_n}{n^3}\longrightarrow1.
\]

The derivative of \(h(x)=(1-x)(1+x^2)e^x\) is \(h'(x)=e^x x(1-2x-x^2)\), so \(h\) strictly increases on \((0,\sqrt2-1)\) and strictly decreases on \((\sqrt2-1,1)\). Since \(h(0)=1\) and \(h(1)=0\), exactly one positive level-one root \(\rho\) exists. The exact finite unimodality and pointwise limit imply that, for any \(\epsilon>0\), all sufficiently large \(n\) have \(t_n/n\in(\rho-\epsilon,\rho+\epsilon)\): pick comparison fractions on the two sides of \(\rho\), apply the respective signs and the single-crossing property. This proves the limit.

## Verification

The accompanying `verify.py` uses only the Python standard library. It independently enumerates every mapping for \(2\le n\le6\), exactly \(50{,}068\) mappings, and compares the resulting cycle–branching covariance and mixed expectations with the theorem using exact rational arithmetic. It additionally checks the covariance sign classification through \(n=150\) and the discrete difference identity for every indicated parameter through that range. A direct run reported `PASS 50068 mappings enumerated; 11828 exact checks`. These checks are finite reproducibility evidence, not an infinite proof; the preceding algebra provides that proof.

## Relationship to prior work

Arney and Bender's 1982 study, *Random mappings with constraints on coalescence and number of origins*, defines indegree-count parameters and studies constrained random-mapping distributions. Flajolet and Odlyzko's 1990 *Random Mapping Statistics* develops generating-function formulas for marginal random-mapping statistics, including indegree-related counts. Hansen and Jaworski's *Random mappings with exchangeable in-degrees* (first published 4 September 2007) introduces a broader fixed-exchangeable-indegree framework and describes cyclic-point, component, and component-size distributions. Their 2008 *Local properties of random mappings with exchangeable in-degrees* gives exact local predecessor/successor distributions; the full text was inspected, including its definitions and results section. Those statements do not assert the specific unconditional covariance of a cycle-length count with the number of exactly-two-preimage vertices, its discrete sign classification, or its asymptotic threshold.

These are comparisons of stated statistical quantities rather than claims that broad generating-function or random-mapping methods cannot derive the result. The inaccessible full 1992 Berg–Jaworski chapter *Probability distributions related to the local structure of a random mapping* is a specific residual historical-priority risk, as is any unindexed earlier mixed-moment identity.

## Limitations

The theorem concerns only the uniform independent-image random mapping and exact indegree two; other indegree values or nonuniform maps may behave differently. Covariance zero at a fixed-point count does not assert independence. The asymptotic threshold is a limit of exact finite thresholds, not an exact finite closed form for \(t_n\). Although several older methods could imply the identity after additional algebra, priority has not been independently established, and no independent audit has been performed.

## References

1. J. Arney and E. A. Bender, *Random mappings with constraints on coalescence and number of origins*, Pacific Journal of Mathematics 103 (1982), 269–294. https://msp.org/pjm/1982/103-2/pjm-v103-n2-p03-p.pdf
2. P. Flajolet and A. M. Odlyzko, *Random Mapping Statistics*, in Advances in Cryptology — EUROCRYPT proceedings, LNCS 434 (1990), 329–354. https://scispace.com/pdf/random-mapping-statistics-yjuqfvoh87.pdf
3. J. C. Hansen and J. Jaworski, *Random mappings with exchangeable in-degrees*, Random Structures & Algorithms 33 (2008), 105–126. First published 4 September 2007. https://doi.org/10.1002/rsa.20187
4. J. C. Hansen and J. Jaworski, *Local properties of random mappings with exchangeable in-degrees*, Advances in Applied Probability 40 (2008), 183–205. https://doi.org/10.1239/aap/1208358892
5. S. Berg and J. Jaworski, *Probability distributions related to the local structure of a random mapping*, in Random Graphs, vol. 2 (1992), 1–22. Full text not available for comparison.
