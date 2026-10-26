# Complete product-rank spectrum and asymmetric limits for partial idempotents

## Finding

Let \(P_n\) be the semigroup of all partial self-maps of \(X_n=\{1,\ldots,n\}\), with composition \(e\circ f\) applying \(f\) first. Let \(N_n(r,s,t)\) count **ordered** pairs of idempotents \(e,f\in P_n\) with \(\lvert\operatorname{im}e\rvert=r\), \(\lvert\operatorname{im}f\rvert=s\), and \(\lvert\operatorname{im}(e\circ f)\rvert=t\). For all integers \(n\ge0\) and \(0\le r,s\le n\), the complete distribution is

\[
\begin{aligned}
N_n(r,s,t)&=\binom nr(s+1)^{n-s}
\sum_{h=\max(0,r+s-n)}^{\min(r,s,t)}
\binom rh\binom{n-r}{s-h}(r+1)^{n-r-s+h}\binom{r-h}{t-h}\\
&\qquad\qquad\times\sum_{j=0}^{t-h}(-1)^{t-h-j}\binom{t-h}{j}(h+j+1)^{s-h}.
\end{aligned}
\]

Here \(N_n(r,s,t)=0\) outside \(0\le t\le\min(r,s)\), an empty sum is zero, and \(0^0=1\) when encountered as a counting convention. A second, independent coefficient description is

\[
N_n(r,s,t)=\binom nr\binom rt(s+1)^{n-s}
[u^s]\sum_{j=0}^{t}(-1)^{t-j}\binom tj(1+u)^j
\bigl(r+1+(j+1)u\bigr)^{n-r}.
\]

Every feasible rank triple occurs: \(N_n(r,s,t)>0\) exactly when \(\max(0,r+s-n)\le t\le\min(r,s)\). This support statement is a consequence of the enumeration, not asserted as an independently novel theorem.

There is also a nontrivial law of large numbers for the *same* rank statistic. If \(r_n/n\to a\in(0,1)\) and \(s_n/n\to b\in(0,1)\), and \(e_n,f_n\) are independent uniformly chosen idempotents of their respective ranks, then

\[
\frac{\lvert\operatorname{im}(e_n\circ f_n)\rvert}{n}
\ \xrightarrow{\ \mathrm P\ }\
\Phi(a,b)=a\left[1-(1-b)\exp\!\left(-\frac{b(1-a)}a\right)\right].
\]

Composition order matters, including at macroscopic scale: \(\Phi(1/5,3/5)=0.1927425637\ldots\), but \(\Phi(3/5,1/5)=0.1799168069\ldots\).

## Assumptions and scope

Partial self-maps may be undefined at any point, including everywhere. An idempotent satisfies \(e\circ e=e\), fixes every point of its image, and takes each other point either to an image point or to the undefined state. The empty map is the unique rank-zero idempotent. Maps and points are labeled; pairs are ordered, and no commutativity or common-domain condition is imposed. The finite-field, inverse-monoid, and total-transformation settings are not being identified with this semigroup. This applies for all \(n\ge0\), including \(N_0(0,0,0)=1\).

## Proof

**1. Identity for the product image.** Write \(E=\operatorname{im}e\) and \(F=\operatorname{im}f\). Since \(f\) is idempotent, \(f\) fixes its image pointwise and is onto \(F\) from its domain. Thus

\[
\operatorname{im}(e\circ f)=e\bigl(F\cap\operatorname{dom}e\bigr).
\]

For fixed \(F\) of size \(s\), the number of idempotent \(f\) with image exactly \(F\) is \((s+1)^{n-s}\), since each outside point chooses an undefined value or one of the \(s\) fixed image points. In particular, the product-image rank depends only on \(F\), not on the other choices defining \(f\).

**2. Exact occupancy count.** Choose \(E\subseteq X_n\) of size \(r\), then choose \(F\subseteq X_n\) of size \(s\) with \(h=|E\cap F|\). There are \(\binom nr\binom rh\binom{n-r}{s-h}\) choices. The \(h\) shared image points already lie in the product image. Among the remaining \(m=s-h\) points of \(F\setminus E\), precisely \(d=t-h\) *distinct additional* roots in \(E\setminus F\) must be hit. Choose the additional roots in \(\binom{r-h}{d}\) ways. For each of the \(m\) marked points, the allowed values are undefined, any of the \(h\) shared roots, or any of these \(d\) additional roots. Requiring each additional root to be hit, inclusion–exclusion gives

\[
\sum_{j=0}^{d}(-1)^{d-j}\binom dj(h+j+1)^m.
\]

The remaining \(n-r-m\) points outside \(E\cup F\) freely take any of \(r+1\) values, giving \((r+1)^{n-r-m}\). Multiply by the choices for \(f\) and sum over the possible intersections \(h\). This proves the first formula. No surjectivity requirement was omitted: each image root is already fixed by \(e\).

**3. Independent coefficient formula and exact support.** Alternatively, choose \(E\) and then the \(t\) roots of \(E\) that the selected set \(F\) touches through \(e\). For any set of \(j\) allowed roots, an image root is either selected into \(F\) or not, contributing \((1+u)^j\). For each of the \(n-r\) other points, the alternatives are \(r+1\) unselected states or \(j+1\) selected states, contributing \(r+1+(j+1)u\). Inclusion–exclusion forces every one of the \(t\) chosen roots to be touched; taking \([u^s]\) gives the second formula. For the support lower bound, at least \(r+s-n\) elements of \(E\) must belong to \(F\) and are fixed by \(e\), while the product image lies in both \(E\) and an image of a set of size \(s\). To realize each admissible \(t\), take \(e\) and \(f\) as partial identities on two subsets of cardinalities \(r,s\) intersecting in exactly \(t\).

**4. Random limit.** Conditional on uniformly chosen root sets \(E,F\), the intersection \(H=|E\cap F|\) is hypergeometric and \(H/n\to ab\) in probability. Given \(H=h\), the \(s-h\) points of \(F\setminus E\) choose independently and uniformly one of \(r+1\) options (undefined or one of the \(r\) roots). The product rank equals \(h+W\), where \(W\) counts roots of \(E\setminus F\) hit at least once. Therefore

\[
\mathbb E[W\mid H=h]
=(r-h)\left[1-\left(1-\frac1{r+1}\right)^{s-h}\right].
\]

Changing one of the \(s-h\) independent choices alters \(W\) by at most one, so bounded-differences concentration gives \((W-\mathbb E[W\mid H])/n\to0\) in probability, uniformly for \(0\le h\le\min(r,s)\). Since \(r/n\to a>0\), the last conditional expectation divided by \(n\) converges in probability to \(a(1-b)[1-\exp(-b(1-a)/a)]\); adding \(H/n\to ab\) yields \(\Phi(a,b)\). The two displayed values establish a strict macroscopic order effect, not merely a finite-size artifact.

## Verification

Run `python3 partial_idempotent_product_rank_checker.py` in the same directory. It directly constructs all partial maps on \(n=0,1,2,3,4,5\), filters by idempotence, explicitly composes every ordered pair, and checks every triple against the two formulas. This exhausts 299755 ordered pairs; the rank-polynomial identity is independently compared through \(n=14\) for 5440 parameter triples. The expected final line is `ALL_PARTIAL_IDEMPOTENT_PRODUCT_RANK_CHECKS_PASSED block_formula_checks=5440`. The same checker verifies the nonsymmetric finite example \(n=5,r=2,s=4\): respective product-rank histograms are \((0,800,5950)\) and \((0,1080,5670)\) when the factor ranks are swapped. Finite computations check instances but cannot prove the all-size identities or probability limit.

## Relationship to prior work

Luangchaisri and Changphas (2021, DOI below) study **existence and types of skew pairs of idempotents** in the full partial-transformation semigroup and explicitly describe product-image domains; the full accessible article, including its main theorems and conclusion, does not provide the complete joint three-rank enumeration or the random-rank law above. Classical fixed-image-root counting is known (for example, the total-map count in the 2018 Semigroup Forum paper below). The present result uses that counting as an ingredient but addresses **ordered products of arbitrary, not necessarily commuting, partial idempotents**, which are not counted by one-factor idempotent formulas. A previously recorded theorem for **commuting total transformations** concerns a more restrictive semigroup and commutation condition, and its joint-rank EGF does not imply this noncommuting partial-map distribution. Classical random mapping occupancy results are background, not claimed new.

## Limitations

Novelty is assessed against the inspected sources and actual mathematical-query searches, not as a uniqueness theorem. Full texts of some older specialist papers on transformation semigroup idempotents and products were not accessible; an implicit or differently indexed equivalent formula could exist. The macroscopic limit assumes both fixed-rank densities converge to interior values \((0,1)\); boundary-density scaling, joint fluctuations, and limiting covariance of the two composition orders are not established. The theorem counts all ordered pairs, not specifically skew pairs satisfying an extra idempotence-of-product condition. Direct computations are restricted to stated finite ranges.

## References

1. P. Luangchaisri and T. Changphas, "Skew Pairs of Idempotents in Partial Transformation Semigroups," *Mathematics* 10 (2022), article 2, publicly released 2021-12-21, DOI: 10.3390/math10010002, https://www.mdpi.com/2227-7390/10/1/2.
2. I. Dolinka and J. East, "Idempotent generation in the endomorphism monoid of a uniform partition," preprint arXiv:1407.3312 (2014), https://arxiv.org/abs/1407.3312.
3. "Random ubiquitous transformation semigroups," *Semigroup Forum* (2019), DOI: 10.1007/s00233-018-09992-7, https://link.springer.com/article/10.1007/s00233-018-09992-7.
4. T. S. Blyth and M. H. Almeida Santos, "Skew pairs of idempotents in transformation semigroups," *Acta Mathematica Sinica* 22 (2006), 1705–1714; inspected at abstract level only.
