# Joint image-rank spectra of commuting idempotents in finite transformation monoids

## Finding
For every integer \(n\geq0\), let \(X_n\) be a labeled set of cardinality \(n\), and let \(T_n\) be the full transformation monoid of all maps \(X_n\to X_n\). For a map \(h\), put \(r(h)=|\operatorname{im}(h)|\). The complete joint rank enumerator for *ordered* pairs of commuting idempotents is
\[
F(z;u,v,w)=\sum_{n\geq0}\frac{z^n}{n!}
\sum_{\substack{e,f\in T_n\\e^2=e,\ f^2=f,\ ef=fe}}
u^{r(e)}v^{r(f)}w^{r(ef)}.
\]
As a formal power series in \(z\) with coefficients in \(\mathbb Q[u,v,w]\), it satisfies the universal identity
\[
\boxed{F(z;u,v,w)=\exp\left(wuvz\sum_{a,c,d\geq0}
\frac{u^av^cz^{a+c+d}}{a!c!d!}\big((a+1)(c+1)\big)^d\right).}
\]
In particular, for \(n\geq1\), the coefficient of \(u^rv^sw^t z^n/n!\) is positive **if and only if**
\[
1\leq t\leq\min(r,s),\qquad r+s-t\leq n.
\]
For \(n=0\), the only triple is \((r,s,t)=(0,0,0)\). Setting \(u=v=w=1\) gives the total numbers of ordered commuting idempotent pairs for \(n=0,1,\ldots,8\):
\[
1,\ 1,\ 7,\ 58,\ 601,\ 7616,\ 113989,\ 1963060,\ 38178193.
\]
The identity provides every joint rank coefficient and, by marginalization, the individual ranks and product-rank distribution.

## Assumptions and scope
Composition is ordinary function composition, and the order of multiplication is immaterial for the commuting pairs being counted. Each idempotent is a retraction onto its image. All maps are total self-maps of a finite labeled set; no order, metric, relation, or algebraic structure on the set is imposed. The empty labeled set has one empty map, which is treated as its identity. The identity is in the ring of formal power series over \(\mathbb Q[u,v,w]\); the final scaled coefficients are nonnegative integers. No asymptotic or uniqueness-of-publication statement is asserted.

## Proof
Let \(e,f\in T_n\) commute and be idempotent. Set \(p=ef=fe\). Then \(p^2=p\), and
\[
B:=\operatorname{im}(p)=\operatorname{im}(e)\cap\operatorname{im}(f).
\]
Indeed, every value of \(p\) belongs to both images. Conversely, any element fixed by both retractions is in the image of their composite; the intersection consists exactly of such fixed points.

For every \(b\in B\), the fiber \(P_b=p^{-1}(b)\) is invariant under both \(e\) and \(f\), since \(pe=p\) and \(pf=p\). Partition the fiber into four uniquely determined parts:
\[
\{b\},\quad A_b=(\operatorname{im}e\cap P_b)\setminus\{b\},\quad
C_b=(\operatorname{im}f\cap P_b)\setminus\{b\},\quad
D_b=P_b\setminus(\{b\}\cup A_b\cup C_b).
\]
The sets \(A_b,C_b\) are disjoint because the common image is exactly \(B\). For \(a\in A_b\), idempotence forces \(e(a)=a\), while \(f(a)=p(a)=b\). Similarly, for \(c\in C_b\), we have \(e(c)=b\), \(f(c)=c\), and both maps fix \(b\).

For any \(x\in D_b\), the images can be chosen independently:
\[
e(x)\in\{b\}\cup A_b,\qquad f(x)\in\{b\}\cup C_b.
\]
These conditions are necessary by fiber invariance and the definitions of the two image sets. Conversely, **every** such independent choice gives commuting idempotent retractions: each image point is fixed by its respective map, and each of the two composites sends all points in \(P_b\) to \(b\). Consequently, the rooted fiber data form a bijective encoding of the ordered pair \((e,f)\), with no overcounting.

Put \(a=|A_b|\), \(c=|C_b|\), \(d=|D_b|\). On a fixed labeled block of size \(m=1+a+c+d\), the distinguished root \(b\) has \(m\) choices, the three remaining disjoint subsets have \((m-1)!/(a!c!d!)\) allocations, and the \(d\) free points have \(((a+1)(c+1))^d\) independent pairs of images. Each such block contributes ranks \((a+1,c+1,1)\), so its weighted exponential generating function is
\[
H(z;u,v,w)=wuvz\sum_{a,c,d\geq0}
\frac{u^av^cz^{a+c+d}}{a!c!d!}\big((a+1)(c+1)\big)^d.
\]
The partition into nonempty product fibers \(P_b\) is canonical and unordered; the labeled exponential formula thus gives \(F=\exp(H)\), proving the displayed identity.

Finally, for a nonempty set, the product image has size \(t=|B|\geq1\). Since \(\operatorname{im}(e)\) and \(\operatorname{im}(f)\) meet exactly in \(B\), inclusion-exclusion gives \(r+s-t\leq n\) and \(t\leq\min(r,s)\). Conversely, whenever these inequalities hold, choose \(t\) root points, \(r-t\) additional points fixed only by \(e\), \(s-t\) fixed only by \(f\), and assign the remaining \(n-r-s+t\) points to a root block. Mapping each surplus point to its block root under both maps constructs an admissible pair. All and only the specified rank triples therefore occur. The empty-set case follows directly.

## Verification
Run `python3 verify_joint_ranks.py` using standard Python 3. The checker enumerates every total map on each labeled set for \(0\leq n\leq6\), filters idempotents, tests commutation by direct composition, and computes the full triple-rank histogram. A separate labeled-block recurrence using the smallest label and binomial convolution computes the coefficients of the asserted exponential formula. The two complete histograms agree in each tested dimension. For \(1\leq n\leq8\), the checker also tests the exact nonzero support and symmetry in the first two ranks. Its deterministic output is included in `verify_joint_ranks.out`. These finite computations support but do not replace the general bijective proof.

## Relationship to prior work
Dolinka and East (2014 preprint) enumerate individual idempotents of finite transformation monoids preserving a uniform partition and record the classical one-map formula \(\binom{n}{k}k^{n-k}\) for the full transformation monoid (their Proposition 2.1). The present result concerns a **joint three-rank distribution** of ordered *commuting pairs* of unrestricted retractions, not a one-map rank distribution.

Fleischer and Jack (first public preprint 2018) give decision algorithms for properties of generated transformation semigroups, including whether all idempotents commute (Corollary 5.2). That yes/no decision result neither gives nor logically implies the present exact coefficient formula.

Konieczny (2002) determines Green relations and regular elements of centralizers of idempotents in partial transformation semigroups. Its publicly available abstract was inspected, but the full paper was not obtainable for a decisive theorem-by-theorem comparison. An implicit or explicit related counting identity cannot be excluded. The claimed contribution is the complete joint rank enumeration and canonical product-fiber encoding, subject to that priority risk.

## Limitations
The theorem is restricted to **pairs** of commuting idempotent *total transformations*. It does not enumerate triples, arbitrary commuting transformations, or partial transformations. The self-contained proof establishes the formula for all finite \(n\); the attached exhaustive computation stops at \(n=6\). Historical-priority and equivalent-formulation uncertainty remains for uninspected full texts and nonindexed literature, especially Konieczny (2002). No independent audit of this finding has been performed.

## References
1. I. Dolinka and J. East, *Idempotent generation in the endomorphism monoid of a uniform partition*, arXiv:1407.3312 (first public 2014-07-11), especially Proposition 2.1. https://arxiv.org/html/1407.3312v2
2. L. Fleischer and T. Jack, *On the Complexity of Properties of Transformation Semigroups*, arXiv:1811.00060 (first public 2018-10-31), especially Section 5 and Corollary 5.2. https://arxiv.org/abs/1811.00060
3. J. Konieczny, *Semigroups of transformations commuting with idempotents*, Algebra Colloquium 9 (2002), 121–134; abstract available at https://www.researchgate.net/publication/266434306_Semigroups_of_transformations_commuting_with_idempotents
