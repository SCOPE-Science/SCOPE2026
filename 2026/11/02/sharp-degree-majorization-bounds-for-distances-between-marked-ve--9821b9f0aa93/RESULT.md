# Sharp degree-majorization bounds for distances between marked vertices in random labeled trees

## Finding

For every integer \(n\ge3\), fix distinct labeled vertices \(u,v\) in \([n]\) and a positive integer degree vector \(\boldsymbol d=(d_i)_{i\in[n]}\) satisfying \(\sum_i d_i=2(n-1)\). Draw a labeled tree uniformly from the trees with these *exact assigned degrees*, and let \(D\) be the graph distance between \(u\) and \(v\). Write \(N=n-2\), and let \(\boldsymbol b=(d_w-1)_{w\notin\{u,v\}}\), with elementary symmetric functions \(e_k(\boldsymbol b)\) and \(e_0=1\). The exact complete survival law is

\[
\Pr_{\boldsymbol d}(D>k)=\frac{k!e_k(\boldsymbol b)}{(N)_{\underline{k}}}\qquad(0\le k\le N).
\]

In particular, the degrees of the two marked vertices enter the law only through their sum. Fix their degrees, and thus the total unmarked excess \(s=\sum_{w\ne u,v}(d_w-1)=n-d_u-d_v\). For two admissible degree profiles with the same marked degrees, if \(\boldsymbol b\) majorizes \(\boldsymbol b'\) (so that \(\boldsymbol b\) is more concentrated), then

\[
D_{\boldsymbol b}\le_{\mathrm{st}}D_{\boldsymbol b'}.
\]

When the sorted profiles differ, necessarily \(s\ge2\) and \(N\ge2\); the ordering is nontrivial and strict at the threshold \(D>2\). For *all* admissible profiles with the fixed marked degrees, the least distance law is obtained when \(\boldsymbol b=(s,0,\ldots,0)\), and the greatest when \(\boldsymbol b\) consists of \(s\) ones and \(N-s\) zeros. Their survival functions and sharp mean bounds are

\[
\begin{aligned}
\Pr_{\min}(D>1)&=s/N,&\Pr_{\min}(D>k)&=0\quad(k\ge2),\\
\Pr_{\max}(D>k)&=\frac{(s)_{\underline{k}}}{(N)_{\underline{k}}}\quad(0\le k\le N),\\
1+\frac{s}{N}&\le\mathbb E_{\boldsymbol d}[D]\le\frac{N+1}{N-s+1}=\frac{n-1}{d_u+d_v-1}.
\end{aligned}
\]

For \(s\ge2\), the extremizing nonmarked degree multisets are unique, up to permutation. For \(s\le1\), all admissible unmarked profiles have the same law. These conclusions include every feasible boundary degree vector and every integer tail threshold.

## Assumptions and scope

Every vertex label is distinguished, including the two endpoints, and the full degree vector is prescribed label by label; this differs from merely prescribing the multiset of degrees. Every degree is at least one. Feasibility is exactly \(1\le d_u,d_v\) and \(d_u+d_v\le n\) together with the stated total degree condition. Any nonnegative integer unmarked excess profile summing to \(s\) is realizable by at least one labeled tree by the Prüfer correspondence. The stochastic-order comparison keeps \(d_u\) and \(d_v\) separately fixed. The two-vertex case \(n=2\) is deterministic with \(D=1\) and is excluded only to avoid the zero falling-factorial denominator.

The falling factorial \((N)_{\underline k}=N(N-1)\cdots(N-k+1)\), and \(e_k\) is the sum of products over all size-\(k\) subsets of unmarked indices; \(e_k=0\) outside feasible indices. Majorization means that after sorting entries decreasingly, each initial partial sum of the first vector is at least that of the second, with equal total sums. Stochastic order is defined by domination of all upper-tail probabilities.

## Proof

**1. Weighted labeled-tree and rooted-forest identities.** Introduce indeterminates \(x_1,\ldots,x_n\), let \(X=\sum_i x_i\), and give edge \(\{i,j\}\) weight \(x_ix_j\). The multivariate Cayley identity is

\[
\sum_{T\text{ labeled tree}}\prod_{\{i,j\}\in E(T)}x_ix_j
=\left(\prod_{i=1}^n x_i\right)X^{n-2}.
\]

Consequently the coefficient of the prescribed degree monomial \(\prod_i x_i^{d_i}\) equals \(N!/\prod_i(d_i-1)!\), the familiar Prüfer degree count.

For a fixed nonempty root set \(P\) of vertices, write \(X_P=\sum_{i\in P}x_i\). The sum over all spanning forests whose components each contain exactly one vertex of \(P\), weighted by the same edge weights, is

\[
\left(\prod_{i\notin P}x_i\right) X_P X^{n-|P|-1}
\]

when the complement is nonempty. To verify it, orient each forest edge toward its unique root. Factoring the weight \(x_i\) for each nonroot child leaves the determinant of the directed reduced Laplacian \(L=X I-\boldsymbol1\boldsymbol x_{[n]\setminus P}^{\mathsf T}\), which is \(X^{n-|P|-1}X_P\) by the rank-one determinant lemma. If the complement is empty, the only forest is edgeless.

**2. Enumeration of the marked path.** Fix \(0\le k\le N-1\), and a particular ordered list \(w_1,\ldots,w_k\) of distinct unmarked vertices. Require the \(u\)-to-\(v\) path to be precisely \(u,w_1,\ldots,w_k,v\). Removing its \(k+1\) edges leaves a forest rooted at those path vertices. By the previous identity, the edge-weight polynomial for trees having this particular path is

\[
\left(\prod_{i=1}^n x_i\right)
\left(\prod_{j=1}^k x_{w_j}\right)X_P X^{N-k-1}.
\]

With \(A=(d_u-1)+(d_v-1)\), coefficient extraction relative to the full fixed-degree tree count gives

\[
\Pr(\text{this ordered path}\mid\boldsymbol d)
=\frac{\left(\prod_{j=1}^k b_{w_j}\right)
\left(A+\sum_{j=1}^k b_{w_j}-k\right)}{(N)_{\underline{k+1}}}.
\]

This expression remains valid when any specified internal vertex has excess zero, as then the path is impossible. Summing over ordered internal lists and writing \(s=\sum b_w=N-A\) yields

\[
\begin{aligned}
\Pr(D=k+1\mid\boldsymbol d)
&=\frac{k!}{(N)_{\underline{k+1}}}
\left[(A-k)e_k(\boldsymbol b)
+\sum_w b_w^2e_{k-1}(\boldsymbol b_{\widehat w})\right]\\
&=\frac{k!e_k(\boldsymbol b)}{(N)_{\underline k}}
-\frac{(k+1)!e_{k+1}(\boldsymbol b)}{(N)_{\underline{k+1}}}.
\end{aligned}
\]

Here the second equality uses the elementary identity

\[
\sum_w b_w^2 e_{k-1}(\boldsymbol b_{\widehat w})
=s e_k(\boldsymbol b)-(k+1)e_{k+1}(\boldsymbol b).
\]

For the remaining terminal path length \(N+1\), every vertex is on the path; direct enumeration gives \(\Pr(D=N+1)=e_N(\boldsymbol b)\), as is also forced by normalization. Telescoping the displayed mass formula now proves the survival law for every \(0\le k\le N\).

**3. Majorization.** It suffices to analyze a nontrivial integer balancing transfer, replacing two excess entries \(x,y\) with \(x-1,y+1\), where \(x\ge y+2\). Let \(\boldsymbol c\) denote the other \(N-2\) excess entries. Expansion in the two changed coordinates proves for every \(k\)

\[
e_k(x-1,y+1,\boldsymbol c)-e_k(x,y,\boldsymbol c)
=(x-y-1)e_{k-2}(\boldsymbol c)\ge0.
\]

The right side is strictly positive when \(k=2\). Any integer majorization relation factors into such balancing transfers and permutations, so the complete survival law gives stochastic domination, strictly at threshold two for genuinely different sorted profiles.

**4. Extremizers.** Since \(s\le N\), the vector \((s,0,\ldots,0)\) majorizes every admissible unmarked excess profile, and every such profile majorizes the vector with \(s\) ones and the remaining zeros. The two extremal survival formulas follow by evaluating \(e_k\). The mean is the sum of survival probabilities over \(k\ge0\). At the upper endpoint,

\[
\sum_{k=0}^s\frac{(s)_{\underline k}}{(N)_{\underline k}}
=\frac1{\binom{N}{N-s}}\sum_{k=0}^s\binom{N-k}{N-s}
=\frac{N+1}{N-s+1},
\]

using the hockey-stick identity. Uniqueness follows because \(e_2=\big(s^2-\sum b_w^2\big)/2\) is minimized only when all excess is on one vertex and maximized only when the nonnegative integer excess entries are all zero or one. This completes the proof.

## Verification

The self-contained `verify.py` checks exact rational survival probabilities against every Prüfer word on \(2\le n\le8\), grouped by the complete labeled degree vector; it also checks the balancing-transfer identity for all unmarked nonnegative integer profiles with \(2\le N\le8\), and exact stochastic extremizers and mean bounds for all profiles with \(1\le N\le9\). The program uses only Python's standard library, exact integers, and exact rational arithmetic. It completed 1,991,963 assertions. This finite exercise checks indexing, normalization, boundary cases, and coefficients; the infinite claims follow from the algebraic proof above rather than the finite tests.

As a nontrivial same-endpoint-degree example, take \(n=8\), \(d_u=d_v=2\), and compare \(\boldsymbol b=(3,1,0,0,0,0)\) to \(\boldsymbol b'=(2,2,0,0,0,0)\). Both have \(\Pr(D>1)=2/3\), but their probabilities of \(D>2\) are respectively \(1/5\) and \(4/15\). This is a balancing transfer between two already-positive excess degrees, not merely moving excess onto a formerly zero-degree position.

To reproduce, run `python3 verify.py` in the same directory as this document.

## Relationship to prior work

The multivariate Cayley identity, Prüfer degree enumeration, rooted-forest matrix-tree determinant, majorization's balancing-transfer principle, and properties of elementary symmetric polynomials are established tools and are not claimed as new. Broutin–Marckert's prescribed-degree tree work (2011) studies Brownian continuum-tree limits under degree-profile hypotheses. Addario-Berry, Donderwinkel, Maazoun and Martin (2021) give a Foata–Fuchs framework, unconditional typical-distance laws, and a stochastic comparison under a type-splitting relation for a root-to-uniform-leaf distance. Addario-Berry–Donderwinkel (2022) study height bounds under degree-profile constraints and majorization. The statement here instead fixes two *specific distinct labels* and their individual degrees, gives an exact finite-sample law under a fully labeled degree vector, and orders it under all same-sum transfers among *unmarked* excess degrees, including transfers between positive coordinates. The resulting simultaneous sharp full distribution bounds and equality cases are the assessed contribution.

Meir and Moon's early work on distances in random trees, and Dahl's work on majorization of deterministic distance vectors in a fixed tree, are further historical comparators. Full texts of some early potential comparators were not available for inspection; the novelty conclusion is qualified accordingly.

## Limitations

No independence or external certification is asserted. The theorem concerns the uniform measure on labeled trees with one fixed degree assigned to each label; it does not automatically extend to weighted tree laws, random recursive trees, plane ordered trees, or distributions conditioned only on an unordered degree multiset. The ordering keeps both endpoint degrees fixed, and profiles with incomparable majorization order are not classified against one another. The equality cases for the least and greatest laws are up to permutation of unmarked labels. The proofs of completeness and uniqueness are internal exact mathematical arguments; tests at finite sizes cannot independently establish them. Historical priority could depend on uninspected older results or implicit consequences of broader tree bijections.

## References

1. N. Broutin and J.-F. Marckert, *Asymptotics of trees with a prescribed degree sequence and applications*, arXiv:1110.5203, first public 24 October 2011. https://arxiv.org/abs/1110.5203
2. L. Addario-Berry, S. Donderwinkel, M. Maazoun and J. B. Martin, *The Foata–Fuchs proof of Cayley's formula, and its probabilistic uses*, arXiv:2107.09726, first public 20 July 2021. https://arxiv.org/abs/2107.09726
3. L. Addario-Berry and S. Donderwinkel, *Random trees have height \(O(\sqrt n)\)*, arXiv:2201.11773, first public 27 January 2022. https://arxiv.org/abs/2201.11773
4. A. Meir and J. W. Moon, *The distance between points in random trees*, 1970, DOI:10.1016/S0021-9800(70)80012-6. Full text not inspected.
5. G. Dahl, *Majorization and distances in trees*, *Networks* 50 (2007), 251–257, DOI:10.1002/net.20202. Abstract inspected only.
