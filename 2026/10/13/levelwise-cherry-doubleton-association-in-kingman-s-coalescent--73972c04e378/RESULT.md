# Levelwise cherry–doubleton association in Kingman's coalescent

## Finding

Consider the standard, finite Kingman coalescent of \(n\ge2\) labeled leaves, with each unordered pair of extant ancestral lineages merging at rate one. Let \(C_n\) count cherries: internal merger nodes whose two incoming lineages are original singleton leaves. For each \(2\le k\le n\), let \(D_{n,k}\) be the number of lineages subtending **exactly two** original leaves at the stage with \(k\) extant lineages. Write \(T_{n,k}\) for the holding time at that stage and
\[
L_{n,2}=\sum_{k=2}^{n}D_{n,k}T_{n,k}.
\]
This is the total length of all branches ancestral to exactly two sampled leaves, stopping at the most recent common ancestor; in particular \(L_{2,2}=0\).

**Theorem.** For every integer \(n\ge5\) and \(2\le k\le n\),
\[
\operatorname{Cov}(C_n,D_{n,k})
=\frac{k(k-1)(n-k)(n-k-1)(n+k-6)}
 {3(n-1)(n-2)(n-3)(n-4)}.
\]
This is strictly positive for \(2\le k\le n-2\) and zero at \(k=n-1,n\). Consequently,
\[
\boxed{\operatorname{Cov}(C_n,L_{n,2})=\frac5{18}\qquad(n\ge5).}
\]
The remaining small-sample values are \(0\) for \(n=2,3\) and \(4/9\) for \(n=4\). Furthermore, \(\mathbb E L_{n,2}=1\) for every \(n\ge3\), and \(\mathbb E C_n=n/3\) for every \(n\ge3\).

Under an independent infinite-sites mutation process of rate \(\theta/2\) per unit branch length, the number \(\xi_{n,2}\) of mutations present in exactly two sampled leaves satisfies the immediate consequence
\[
\operatorname{Cov}(C_n,\xi_{n,2})=\frac{5\theta}{36}\qquad(n\ge5).
\]

## Assumptions and scope

The population genealogy is the *binary, exchangeable, constant-population* Kingman coalescent started from \(n\) distinct sample labels. Every currently available pair merges at rate one, independently of the partition history. No mutations are needed for the main theorem. The merger choices are independent of the successive exponential holding times, with
\[
\mathbb E T_{n,k}=\binom{k}{2}^{-1}=\frac{2}{k(k-1)}.
\]
The notation \((x)_{\underline r}\) denotes a falling factorial; \(\binom ab\) is zero unless \(0\le b\le a\), with the empty-composition convention stated in the proof. All claims concern exact finite-sample expectations; no asymptotic substitution or population-size approximation is used.

## Proof

**1. Cherries created from a fixed pair.** Fix two singleton lineages among \(m\ge3\) currently available lineages. Let \(p_m\) be the probability that they merge with each other before either merges with another lineage. At \(m=3\), \(p_3=1/3\). For \(m\ge4\), conditioning on the next pair gives
\[
p_m=\frac{2}{m(m-1)}+
\frac{(m-2)(m-3)}{m(m-1)}p_{m-1}
=\frac{2}{3(m-1)}.
\]
Induction proves the last equality. When a coalescent starts with \(m\) labeled singletons, linearity over its \(\binom m2\) possible cherry pairs gives expected cherry count \(m/3\) for \(m\ge3\), while the values for one and two singleton leaves are respectively zero and one.

**2. Uniform ordered block sizes at an ancestral level.** Stop the merger chain on reaching exactly \(k\) ancestral blocks, and then order the blocks uniformly at random. Denote their sizes by \((a_1,\ldots,a_k)\). This ordered size vector is uniform over all \(\binom{n-1}{k-1}\) compositions of \(n\) into \(k\) positive integers.

For clarity, fix an ordered set partition with prescribed labeled blocks of sizes \(a_1,\ldots,a_k\). A block of size \(a\) can be internally merged in
\[
\prod_{j=2}^{a}\binom j2=\frac{a!(a-1)!}{2^{a-1}}
\]
possible chronological pair-choice histories. Interleaving the \(a_i-1\) internal mergers for different blocks gives \((n-k)!/\prod_i(a_i-1)!\) possibilities. Therefore the number of merger histories from \(n\) to \(k\) realizing these blocks is \((n-k)!\prod_i a_i!/2^{n-k}\), whereas the total number is
\[
\prod_{j=k+1}^{n}\binom j2
=\frac{n!(n-1)!}{2^{n-k}k!(k-1)!}.
\]
Allowing the final independent random ordering makes the probability of this particular ordered set partition
\[
\frac{\prod_i a_i!}{n!\binom{n-1}{k-1}}.
\]
There are \(n!/\prod_i a_i!\) ordered set partitions with any fixed ordered size vector, so its probability is exactly \(1/\binom{n-1}{k-1}\). The same counting factorization shows that, conditional on the partition, the internal merger history within each block is a uniform Kingman merger history on the leaves of that block; interleaving does not bias its internal cherry statistic.

Let \(B_{n,k}\) and \(D_{n,k}\) be the numbers of size-one and size-two blocks in this partition. For integers \(a,b\ge0\), the uniform-composition law gives
\[
\mathbb E[(B_{n,k})_{\underline a}(D_{n,k})_{\underline b}]
=(k)_{\underline{a+b}}
\frac{\binom{n-a-2b-1}{k-a-b-1}}{\binom{n-1}{k-1}}.
\]
When no parts remain to be assigned, the numerator is interpreted as one if no mass remains and zero otherwise; impossible selections also contribute zero. Only \((a,b)=(0,1),(1,1),(0,2),(2,1)\) will be needed below.

**3. Regression of the final number of cherries.** Given the entire partition at the \(k\)-lineage stage, each block of size at least three contributes its size divided by three to the conditional expected number of already formed cherries. A size-two block contributes one instead of \(2/3\), and a singleton contributes zero. Thus the expected number already formed is
\[
\frac{n-B_{n,k}+D_{n,k}}3.
\]
Any future cherry must involve two of the \(B_{n,k}\) currently singleton lineages. Part 1 applied to the future \(k\)-lineage coalescent gives the expected number \(B_{n,k}(B_{n,k}-1)/[3(k-1)]\). When \(k=2\) and \(n\ge3\), at most one lineage is an original singleton, so this expression remains zero. Hence, for \(n\ge3\),
\[
\mathbb E[C_n\mid\text{the partition at level }k]
=\frac{n-B_{n,k}+D_{n,k}}3
+\frac{B_{n,k}(B_{n,k}-1)}{3(k-1)}.
\]
At \(k=n\), the same formula confirms \(\mathbb E C_n=n/3\).

Multiplying this regression by \(D_{n,k}\), subtracting \((n/3)\mathbb E D_{n,k}\), and abbreviating \(B=B_{n,k}\), \(D=D_{n,k}\), yields
\[
\operatorname{Cov}(C_n,D)
=\frac13\left\{-\mathbb E[BD]
+\mathbb E[(D)_{\underline2}]+\mathbb ED
+\frac{\mathbb E[(B)_{\underline2}D]}{k-1}\right\}.
\]
The factorial-moment identity in Part 2 yields, for \(n\ge5\),
\[
\begin{aligned}
\mathbb ED&=\frac{k(k-1)(n-k)}{(n-1)(n-2)},\\
\mathbb E[BD]&=\frac{k(k-1)^2(k-2)(n-k)}{(n-1)(n-2)(n-3)},\\
\mathbb E[(D)_{\underline2}]&=
\frac{k(k-1)^2(k-2)(n-k)(n-k-1)}{(n-1)(n-2)(n-3)(n-4)},\\
\mathbb E[(B)_{\underline2}D]&=
\frac{k(k-1)^2(k-2)^2(k-3)(n-k)}{(n-1)(n-2)(n-3)(n-4)}.
\end{aligned}
\]
Substitution and cancellation prove the displayed levelwise covariance formula. In the allowed nonboundary range \(2\le k\le n-2\), every factor is positive. It is zero at the two remaining levels because \(D_{n,n-1}=1\) and \(D_{n,n}=0\) deterministically.

**4. Integrating over coalescent holding times.** Since the holding times are independent of the whole jump chain,
\[
\begin{aligned}
\operatorname{Cov}(C_n,L_{n,2})
&=\sum_{k=2}^{n-1}\frac{2}{k(k-1)}
\operatorname{Cov}(C_n,D_{n,k})\\
&=\frac{2}{3(n-1)(n-2)(n-3)(n-4)}
\sum_{k=2}^{n-1}(n-k)(n-k-1)(n+k-6).
\end{aligned}
\]
The elementary polynomial sum equals
\[
\sum_{k=2}^{n-1}(n-k)(n-k-1)(n+k-6)
=\frac5{12}(n-1)(n-2)(n-3)(n-4),
\]
which proves the constant \(5/18\). Similarly, summing \(\mathbb ED_{n,k}\mathbb ET_{n,k}\) gives \(\mathbb E L_{n,2}=1\) for \(n\ge3\).

For \(n=4\), the three-lineage stage contains exactly one doubleton. At the next merger, with probability \(1/3\) the two remaining singleton lineages merge: then \(C_4=2\) and \(D_{4,2}=2\). Otherwise, \(C_4=1\) and \(D_{4,2}=0\). Thus \(\operatorname{Cov}(C_4,D_{4,2})=4/9\), and \(\mathbb ET_{4,2}=1\). For \(n=2,3\), the cherry count is deterministic, giving zero covariance.

Finally, conditional on the genealogy, the infinite-sites doubleton mutation count has mean \((\theta/2)L_{n,2}\). Taking covariance with the genealogy-measurable \(C_n\) proves the stated mutation consequence.

## Verification

The accompanying standalone Python file `verify.py` uses exact rational arithmetic and performs three complementary checks. First, it verifies the uniform-composition factorial-moment calculation and every levelwise covariance identity for \(5\le n\le74\). Second, it computes the jump-chain law by an aggregated Markov recursion for \(3\le n\le15\), independently checking the nonasymptotic covariance and expected total two-descendant length. Third, it enumerates all \(59{,}602\) labeled Kingman merger histories for \(2\le n\le7\), calculating conditional holding-time averages without Monte Carlo error.

Run with `python3 verify.py`; no third-party Python modules are required. Exact checks cover finite values only. The proof above, not the finite checks, establishes all stated quantifiers.

## Relationship to prior work

Disanto and Wiehe (arXiv:1112.1295; 2011) obtain the generating function for cherry count in the ranked Kingman genealogy and for joint cherry–pitchfork counts. Their inspected preprint, particularly Sections 3.1–3.2, contains the marginal cherry expectation \(n/3\) but no merger-clock-weighted, size-two branch-length covariance. Birkner, Blath and Eldon (arXiv:1305.6043; 2013), building on Fu (1995), give moment formulas for the site-frequency spectrum and hence for the two-descendant branch-length marginal and its relations to other frequency classes. Their inspected full text, including Theorem 4.1 and Appendix S1, does not couple those lengths to the number of cherries. The levelwise composition calculation here supplies that missing topological–temporal mixed moment.

François and Mioland (2007) investigate Gaussian approximations for total cherry height and external lengths under a related phylogenetic model. Those quantities and approximation statements should not be conflated with the exact covariance here. An exhaustive historical-uniqueness claim is not made.

## Limitations

The formula depends on pairwise Kingman mergers at unit pair rate. Multiplying the rate of each pair by a positive constant rescales \(L_{n,2}\) and this covariance inversely. Multiple-merger genealogies, demographically time-inhomogeneous coalescents, correlated holding times, and mutation mechanisms departing from the independent infinite-sites Poisson model are not covered. This is an exact mixed second moment, not a full joint distribution or an independence statement. Historical literature coverage is incomplete, especially for older generating-function identities that might encode the same moment indirectly.

## References

1. F. Disanto and T. Wiehe, *Exact enumeration of cherries and pitchforks in ranked trees under the coalescent model*, arXiv:1112.1295 (first submitted 2011-12-06); Mathematical Biosciences 242 (2013), 195–200.
2. M. Birkner, J. Blath and B. Eldon, *Statistical properties of the site-frequency spectrum associated with Lambda-coalescents*, arXiv:1305.6043 (first submitted 2013-05-26); Genetics 195 (2013), 1037–1053.
3. Y. X. Fu, *Statistical properties of segregating sites*, Theoretical Population Biology 48 (1995), 172–197, doi:10.1006/tpbi.1995.1025.
4. O. François and C. Mioland, *Gaussian approximations for phylogenetic branch length statistics under stochastic models of biodiversity*, Mathematical Biosciences 209 (2007), 108–123, doi:10.1016/j.mbs.2007.01.005.
5. S. Janson and G. Kersting, *On the total external length of the Kingman coalescent*, Electronic Journal of Probability 16 (2011), 2203–2218, doi:10.1214/EJP.v16-955.
