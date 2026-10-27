# A dyadic one-bit law for online learning of order ideals on rooted spiders

## Finding

Let \(P=P(\ell_1,\ldots,\ell_m)\) be the finite rooted-spider poset formed by a unique minimum \(r\) and \(m\) mutually incomparable chains above it, the \(i\)-th chain containing \(\ell_i\ge1\) elements. Allow \(m=0\), when \(P\) consists just of \(r\). Let \(\mathcal I(P)\) be the class of indicators of **all** order ideals of \(P\), including the empty ideal, with queries at individual elements of \(P\). Write
\[
 b_i=\ell_i+1,\qquad a_i=\lfloor\log_2 b_i\rfloor,\qquad
 \varepsilon=\begin{cases}1,& b_i=2^{a_i+1}-1\text{ for every }i,\\0,&\text{otherwise.}\end{cases}
\]
The condition defining \(\varepsilon=1\) is understood to hold when \(m=0\). Then the exact Littlestone dimension is
\[
\boxed{\operatorname{Ldim}(\mathcal I(P))=\sum_{i=1}^m a_i+\varepsilon.}
\]
There are exactly \(1+\prod_{i=1}^m b_i\) ideals. In particular, the extra level is present **if and only if every arm has length one less than a Mersenne count**, equivalently \(\ell_i=2^{k_i}-2\) for some integer \(k_i\ge2\). For \(m=0\), the dimension is one. Thus two arms of length two give ten hypotheses and Littlestone dimension three, while one arm of length one and one of length two give seven hypotheses and dimension two. For any \(m\ge1\), \(m\) arms of length two have dimension \(m+1\), compared with dimension \(m\) for the product of their independent arm-threshold classes.

## Assumptions and scope

Order ideals are downward-closed subsets: \(v\in I\) and \(u\le v\) imply \(u\in I\). The Littlestone dimension is the maximum depth of a complete binary tree whose internal nodes are membership queries and whose every root-to-leaf labeling is realized by one hypothesis. Singleton hypothesis classes have dimension zero. This is binary realizable online prediction with no restriction on adaptive queries.

Each nonempty ideal is uniquely \(\{r\}\) together with a prefix of length \(t_i\in\{0,\ldots,\ell_i\}\) from each arm. The empty ideal is one additional, distinguishable hypothesis. The arm queries of depth \(j\in\{1,\ldots,\ell_i\}\) test \(t_i\ge j\); the root query tests whether the ideal is nonempty. No claim is made for more general rooted trees or posets with branching away from the root.

## Proof

**1. Product-threshold baseline.** Let \(B(b_1,\ldots,b_m)\) be the dimension of the class of all arm-prefix vectors, **without** the extra empty ideal, on the arm vertices. A chain with \(b\) possible prefixes has dimension \(f(b)=\lfloor\log_2 b\rfloor\). The upper bound follows from the number of hypotheses; recursively querying the median threshold gives a complete tree of depth \(f(b)\), proving the lower bound.

When concept classes are defined on disjoint query domains and all independent combinations of their concepts are allowed, their Littlestone dimensions add. For the lower bound, concatenate complete shattered trees for the factors, using one factor after the other. For the upper bound, induct on the number of combined hypotheses: any root query acts on one factor, and both resulting product classes retain the other factors; the Littlestone recurrence bounds the smaller child dimension by one less than that factor's current dimension. Consequently
\[
 B(b_1,\ldots,b_m)=\sum_i f(b_i).
\]
(The additive law is used only as a known elementary building block; the new assertion is the precise effect of adding the exceptional empty ideal.)

**2. Exact split recurrence for the augmented box.** Let \(H(b_1,\ldots,b_m)\) be the dimension after adding the one extra empty ideal to the product class. Put \(A=\sum_i f(b_i)\). Monotonicity of dimension under restriction of a concept class gives \(H\ge A\). If all \(b_i=1\), exactly two concepts remain, distinguished by the root query, so \(H=1\).

Otherwise, a root query leaves the empty ideal alone on one side and has depth contribution one. A query at arm \(i\) and depth \(1\le j<b_i\) has a positive branch which is a pure product with \(b_i-j\) choices in coordinate \(i\), and a negative branch which is the augmented product with \(j\) choices in that coordinate. Therefore, writing \(b_{-i}\) for the other coordinates,
\[
 H(b)=\max\Bigl\{1,\ \max_{i}\max_{1\le j<b_i}
 \bigl[1+\min\{B(b_{-i},b_i-j),\ H(b_{-i},j)\}\bigr]\Bigr\}.
\]
Every displayed branch is nonempty, and these are all nonconstant membership queries; hence this is an exact recurrence, not an upper-bound relaxation.

**3. Induction and the dyadic equality case.** Induct on \(\sum_i b_i\), with the all-ones case handled above. For a split in coordinate \(i\), let \(a=f(b_i)\ge1\) and \(A_{-i}=\sum_{h\ne i} f(b_h)\). By induction the positive child has dimension \(A_{-i}+f(b_i-j)\), and the negative child has dimension
\[
 A_{-i}+f(j)+\delta_j,
\]
where \(\delta_j\in\{0,1\}\) is one precisely when \(j=2^{f(j)+1}-1\) **and** every other coordinate \(b_h\) has the analogous Mersenne form.

Since \(j<b_i<2^{a+1}\), both \(f(b_i-j)\le a\) and \(f(j)+\delta_j\le a\). For the second inequality, the only possible obstruction would be \(f(j)=a\) and \(\delta_j=1\), which would force \(j=2^{a+1}-1\ge b_i\), impossible. Thus every split contributes at most \(A+1\), so \(H\le A+1\).

A split achieves \(A+1\) **only if** both children have dimension at least \(A\). The positive child then forces \(b_i-j\ge2^a\), giving \(j\le b_i-2^a\le2^a-1\). The negative child must therefore have \(f(j)=a-1\) and \(\delta_j=1\). The latter forces \(j=2^a-1\) and the Mersenne condition on all the other coordinates. Combining with \(b_i-j\ge2^a\) and \(b_i<2^{a+1}\) forces \(b_i=2^{a+1}-1\). Hence an extra level is possible only when **all** coordinates have the stated form.

Conversely, suppose all \(b_i\) have Mersenne form and at least one exceeds one. Choose such a coordinate with \(a=f(b_i)\), and query it at \(j=2^a-1\). The positive child has \(b_i-j=2^a\) choices and dimension \(A_{-i}+a=A\). The negative child has \(j=2^a-1\) choices and remains an augmented all-Mersenne product; by induction its dimension is \(A_{-i}+(a-1)+1=A\). Thus the query roots a complete shattered tree of depth \(A+1\). Together with the baseline \(H\ge A\), the induction proves the theorem for every finite number of arms and all allowed lengths.

## Verification

The self-contained verifier `verify_spider_ideals.py` independently enumerates all downward-closed subsets of each tested rooted spider and computes the exact Littlestone recurrence over subsets of the resulting hypothesis class. It compares against the closed formula and the independent ideal count. Running `python3 verify_spider_ideals.py` produces `verify_spider_ideals_output.txt`, ending in `ALL_FORMULA_CHECKS_PASS`. The recorded run checks 183 nondecreasing arm vectors with up to five arms, lengths at most eight, and total vertices at most thirteen, including the empty-arm case. The all-parameter conclusion depends on the preceding proof, not on this finite enumeration.

## Relationship to prior work

Ghazi, Golowich, Kumar and Manurangsi analyze general closure bounds for Littlestone dimension (arXiv:2007.03668, first public July 7, 2020); their aggregation inequalities do not supply an exact order-ideal classification or this Mersenne equality condition. Hanneke, Moran and Waknine prove additive Littlestone behavior for direct sums of learning problems (PMLR 247, 2024, Proposition 2); the independent-arm baseline is consistent with that general phenomenon, but additivity does not determine the effect of the extra empty ideal. Frank a Campo develops enumeration methods for finite-poset downsets (arXiv:2206.10293, first public June 21, 2022); the ideal count is elementary here, whereas the new quantity is adaptive shattering depth. The three full texts were examined for their actual statements and relevant sections. Available literature comparisons do not establish absolute publication priority.

## Limitations

The exact formula applies to membership classes of ideals of a single minimum joined to disjoint chains. It does not classify arbitrary rooted-tree ideals, arbitrary intersections of concept classes, noisy online learning, or improper prediction. The 183 finite checks are supplementary and cannot certify the unrestricted theorem by themselves. Historical publication priority may require wider specialist review.

## References

1. B. Ghazi, N. Golowich, R. Kumar and P. Manurangsi, *Near-tight closure bounds for Littlestone and threshold dimensions*, arXiv:2007.03668 (July 7, 2020); Proceedings of Machine Learning Research 132 (2021), 686–696. https://arxiv.org/abs/2007.03668 ; https://proceedings.mlr.press/v132/ghazi21a.html
2. F. a Campo, *A Flexible Approach for the Enumeration of Down-Sets and its Application on Dedekind Numbers*, arXiv:2206.10293 (June 21, 2022). https://arxiv.org/abs/2206.10293
3. S. Hanneke, S. Moran and T. Waknine, *Open problem: Direct Sums in Learning Theory*, Proceedings of Machine Learning Research 247 (2024), 5325–5329, Proposition 2. https://proceedings.mlr.press/v247/hanneke24c.html
