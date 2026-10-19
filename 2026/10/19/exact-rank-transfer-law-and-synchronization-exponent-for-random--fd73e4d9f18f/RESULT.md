# Exact rank-transfer law and synchronization exponent for random finite-set retractions

## Finding

Let \(n\ge1\), let \([n]=\{1,\ldots,n\}\), and let \(\mathcal E_n\) be the set of all idempotent self-maps \(f:[n]\to[n]\), where \(f\circ f=f\). Give each member of \(\mathcal E_n\) equal weight. Write
\[
E_n=|\mathcal E_n|=\sum_{u=1}^{n}\binom{n}{u}u^{n-u}.
\]
For \(1\le r,v\le n\), define \(K_n(r,v)\) by the following explicit integer formula. Set
\[
H(m,c,k)=\sum_{j=0}^{k}(-1)^j\binom{k}{j}(c+k-j)^m,
\]
where \(m,c,k\) are nonnegative integers and the value \(0^0=1\) counts the unique empty assignment. For \(v\le r\), put
\[
\begin{aligned}
K_n(r,v)={}&\sum_{u=1}^n\;\sum_{\substack{\max(0,r+u-n)\le c\le\min(r,u)\\0\le v-c\le\min(r-c,u-c)}}
\binom rc\binom{n-r}{u-c}\,u^{n-r-u+c}\\
&\hspace{15mm}\cdot\binom{u-c}{v-c}\,H(r-c,c,v-c).
\end{aligned}
\]
Set \(K_n(r,v)=0\) for \(v>r\). This nonnegative integer is **exactly the number of idempotents \(f\) for which \(|f(A)|=v\), for any specified \(r\)-element subset \(A\subseteq[n]\)**. In particular, every row sums to \(E_n\), and \(K_n(r,v)>0\) precisely when \(1\le v\le r\).

Take independent uniformly chosen \(f_1,f_2,\ldots\in\mathcal E_n\), put \(g_0=\operatorname{id}_{[n]}\) and \(g_m=f_m\circ\cdots\circ f_1\), and let \(R_m=|g_m([n])|\). Then \((R_m)_{m\ge0}\) is a time-homogeneous Markov chain on \(\{1,\ldots,n\}\) with transition matrix \(K_n/E_n\). For every \(m\ge0\), the **exact number of ordered \(m\)-tuples** of retractions whose composite has rank \(v\) is
\[
\boxed{(K_n^m)_{n,v}.}
\]
All matrix powers are ordinary integer matrix powers; the formula includes \(m=0\).

For \(n\ge2\), let \(\tau=\min\{m\ge0:R_m=1\}\). The diagonal entries satisfy
\[
E_n=K_n(1,1)>K_n(2,2)>\cdots>K_n(n,n)=1.
\]
Consequently \(\tau\) is almost surely finite and, with
\[
\lambda_n=\frac{K_n(2,2)}{E_n}\in(0,1),
\]
its survival probability has the **sharp, fixed-\(n\) exponential rate**
\[
\boxed{\mathbb P(\tau>m)=\Theta_n(\lambda_n^m)\qquad(m\to\infty).}
\]
The exact mean is \(\mathbb E\tau=h_n\), where \(h_1=0\) and
\[
h_r=\frac{E_n+\sum_{v=1}^{r-1}K_n(r,v)h_v}{E_n-K_n(r,r)}\quad(2\le r\le n).
\]
For \(n=1\), every product has rank one and \(\tau=0\).

As an additional noncommutative consequence, the joint law of the first factor's rank, second factor's rank, and product rank is **not symmetric in the two factor ranks**. The first possible failure occurs at \(n=4\): there are \(48\) ordered pairs of ranks \((2,3)\) whose product has rank one, but only \(36\) ordered pairs of ranks \((3,2)\) with rank-one product.

## Assumptions and scope

The set \([n]\) is labeled. Every map in \(\mathcal E_n\) is a *total* self-map, not a partial transformation, and both the constant maps and the identity are included. Rank means cardinality of the image. Maps are composed right-to-left as functions: \((f\circ g)(x)=f(g(x))\). The random factors are independent and uniform over the entire finite set \(\mathcal E_n\), without restriction on individual ranks and without a commutativity assumption. No field or choice of coefficients is involved. The asymptotic statement fixes \(n\ge2\) and lets the number of factors tend to infinity; it is not uniform as \(n\to\infty\).

## Proof

**1. Idempotent images.** A total self-map \(f\) satisfies \(f\circ f=f\) if and only if it fixes every point of its image. Therefore a fixed nonempty subset \(B\subseteq[n]\) of size \(u\) is the image of precisely \(u^{n-u}\) idempotents: every point of \(B\) is fixed, and all other points choose any target in \(B\). Summing over \(B\) yields the stated formula for \(E_n\).

**2. The transfer count.** Fix a subset \(A\subseteq[n]\) of size \(r\), and partition the idempotents \(f\) according to their image \(B\), with \(|B|=u\) and \(c=|A\cap B|\). There are
\[\binom rc\binom{n-r}{u-c}\]
choices of \(B\), and \(c\) necessarily lies between \(\max(0,r+u-n)\) and \(\min(r,u)\). Since \(f\) fixes \(B\), the set \(f(A)\) includes every one of the \(c\) points of \(A\cap B\). If \(|f(A)|=v\), precisely \(k=v-c\) additional image points must come from \(B\setminus A\); choose those with \(\binom{u-c}{k}\) possibilities. The \(r-c\) points of \(A\setminus B\) can map to those \(c+k\) specified target points, but must hit all \(k\) additional points. Inclusion-exclusion gives exactly \(H(r-c,c,k)\) assignments. Finally, the \(n-r-u+c\) points outside \(A\cup B\) each have \(u\) unconstrained choices of image in \(B\). Multiplying, then summing over the disjoint possibilities \((u,c)\), proves the formula for \(K_n(r,v)\). This argument is a bijective count and works even when \(c=0\) or some sets are empty, with the stipulated empty-assignment convention.

The rank of \(f(A)\) can never exceed \(r\) and cannot be zero. Conversely, for each \(1\le v\le r\), choose \(B\subseteq A\) of size \(v\) and make an idempotent fixing \(B\) and mapping every point of \(A\setminus B\) into \(B\); hence \(K_n(r,v)>0\). Summing \(K_n(r,v)\) over \(v\) counts every member of \(\mathcal E_n\) exactly once and gives the row sum \(E_n\).

**3. Exact products.** For any map \(g\) with image \(A\), the image of \(f\circ g\) equals \(f(A)\). Conditional on an arbitrary past composite \(g_m\) of rank \(r\), there are therefore exactly \(K_n(r,v)\) choices of the next idempotent \(f_{m+1}\) that yield rank \(v\). The count depends only on \(r\): the fixed subset \(A\) does not occur in the formula. Independence and uniformity give the Markov transition matrix \(K_n/E_n\). Starting at rank \(n\) and multiplying the count matrices shows inductively that the number of ordered \(m\)-tuples ending with rank \(v\) is \((K_n^m)_{n,v}\), with the zeroth power counting the empty tuple.

For clarity, an ordered pair whose first factor has rank \(r\), second factor has rank \(u\), and composite has rank \(v\) is counted by
\[
\binom nr r^{n-r}\sum_{\substack{\max(0,r+u-n)\le c\le\min(r,u)\\0\le v-c\le\min(r-c,u-c)}}\binom rc\binom{n-r}{u-c}u^{n-r-u+c}\binom{u-c}{v-c}H(r-c,c,v-c).
\]
Indeed, choose the first image and first retraction, and then count second retractions of specified rank on that image. The displayed expression is integer-valued despite its inclusion-exclusion presentation. Formula evaluation at \(n=4\) gives \(48\) for rank triple \((2,3,1)\), \(36\) for \((3,2,1)\), and the complementary rank-two counts \(240\) and \(252\), respectively. For \(n\le3\), any unequal positive rank pair contains rank one or the full rank \(n\); a rank-one factor gives rank-one product, and a full-rank idempotent is the identity. Thus the two factor-rank orders have identical product-rank distributions for \(n\le3\), proving the minimality of \(n=4\).

**4. Strict eigenvalue ordering.** For a fixed \(r\)-element set \(A_r\), \(K_n(r,r)\) counts idempotents whose restrictions to \(A_r\) are injective. Choose a nested chain of sets \(A_1\subset\cdots\subset A_n=[n]\). Injectivity on \(A_{r+1}\) implies injectivity on \(A_r\), so the diagonal count is weakly decreasing. The containment is strict for every \(1\le r<n\): let \(x\) be the new point of \(A_{r+1}\), fix every point of \(A_r\), send \(x\) to one point of \(A_r\), and send all remaining points into \(A_r\). This is an idempotent injective on \(A_r\) but not on \(A_{r+1}\). Also \(K_n(1,1)=E_n\), whereas \(K_n(n,n)=1\) because a bijective idempotent is the identity. Thus all diagonal inequalities are strict.

**5. Synchronization and its rate.** Rank is nonincreasing, and rank one is absorbing. For each transient state \(r\ge2\), the probability of moving to rank one in one step is at least \(n/E_n>0\), because every constant map is idempotent. Thus absorption occurs almost surely with finite mean. Restrict the transition matrix to transient states \(2,\ldots,n\). Its triangular diagonal consists of the distinct numbers \(K_n(r,r)/E_n\), whose unique maximal member is \(\lambda_n\). All remaining eigenvalues have strictly smaller modulus, so its matrix powers have norm \(O_n(\lambda_n^m)\) (the dominant eigenvalue is simple). This yields the upper bound for \(\mathbb P(\tau>m)\). For \(n=2\), remaining at rank two for all \(m\) steps has probability exactly \(\lambda_n^m\). For \(n>2\), the first factor can have rank two with positive probability; after that, choosing only idempotents injective on the current two-point image for \(m-1\) steps has probability \(\lambda_n^{m-1}\). This gives the matching positive-constant lower bound. Lastly, first-step conditioning yields \(h_r=1+E_n^{-1}\sum_{v=1}^rK_n(r,v)h_v\), and solving for \(h_r\) gives the stated finite recursion.

## Verification

Run `python3 rank_kernel_checker.py` from a directory containing the supplied standalone checker. It computes the integer formula independently from an exhaustive enumeration of actual finite-set self-maps satisfying the idempotence equation. For each \(1\le n\le6\), every row and coefficient of the transfer kernel agrees with enumeration, and its row sums agree with the independently counted idempotents. For \(1\le n\le4\), two-step product counts are separately exhaustively enumerated and agree with matrix powers. The checker also verifies the two unequal rank-order multiplicities \(48\) and \(36\) at \(n=4\), the strict diagonal ordering, expected-hitting-time recursions, and additional exact-arithmetic formula identities at \(n=7,9,12\). The final output is `ALL_EXACT_CHECKS_PASSED`. These finite checks corroborate but do not replace the bijective proof for all \(n\) and all product lengths.

For \(n=4\), the exact count transfer matrix, indexed by ranks \(1,2,3,4\), is
\[
K_4=\begin{pmatrix}
41&0&0&0\\16&25&0&0\\7&27&7&0\\4&24&12&1
\end{pmatrix}.
\]
Consequently there are \(41\) individual idempotents, and the two-factor product-rank counts, from ranks one through four, are \((636,948,96,1)\), summing to \(41^2=1681\). Its synchronization exponent is \(\lambda_4=25/41\), and the exact mean synchronization time is \(19229/5440\).

## Relationship to prior work

Araújo, Bentz and Cameron (2019) study strongly factorizable transformation semigroups and the interaction of idempotents with permutation groups; their theorems concern generation and factorization properties for maps of specified ranks. Sarkar and Singh (2021) classify unit-regularity and semi-balanced conditions in transformation semigroups. Bugay (2024) examines quasi-idempotents, Green-class structures and quasi-idempotent generating ranks; in particular, its rank-preservation criterion for products is qualitative. These are relevant structural inputs and comparisons, but none of the inspected statements determines the complete random-idempotent rank-transfer matrix, the arbitrary-product rank polynomial or the sharp fixed-size synchronization exponent proved above. Classic work on products of idempotents establishes generation and factorization properties, while work on compositions of unrestricted random functions uses a different distribution of factors. Those results are not being claimed anew. The possibility of an equivalent exact transfer law in older probability, transformation-semigroup or automata literature has not been eliminated.

## Limitations

The theorem tracks only the image cardinality of the composed map, not its full kernel partition, conjugacy class or individual output-map multiplicities. The independence and uniformity of the idempotent factors are essential for the stated stochastic law, although the deterministic transition counts are unconditional. The asymptotic exponent is for each fixed finite \(n\); no uniform \(n\to\infty\) limit law is asserted. The enumeration code verifies only finite instances and does not constitute an infinite proof. Originality remains subject to independent literature assessment, especially alternative formulations of random transformation products through occupancy or Green-relation methods.

## References

1. J. Araújo, W. Bentz and P. J. Cameron, *Primitive Permutation Groups and Strongly Factorizable Transformation Semigroups*, initial arXiv posting 2019-10-18, https://arxiv.org/abs/1910.08335 ; see introduction and Section 3.
2. M. Sarkar and S. N. Singh, *Unit-regular and semi-balanced elements in various semigroups of transformations*, initial arXiv posting 2021-06-15, https://arxiv.org/abs/2106.08063 ; see Sections 1 and 3.
3. L. Bugay, *Quasi-idempotents in certain transformation semigroups*, *Algebra and Discrete Mathematics* 37 (2024), 181–190, https://doi.org/10.12958/adm2223 ; see Section 2, Proposition 3 and Theorem 4.
4. A. Dalal and E. Schmutz, *Compositions of Random Functions on a Finite Set*, *Electronic Journal of Combinatorics* 9 (2002), R26, https://doi.org/10.37236/1642 ; comparison concerns unconstrained random self-maps rather than idempotent factors.
