# Uniform commuting-tuple product fibers in abelian-group-colored partition monoids

## Finding

For every finite abelian group \(G\) of order \(g\ge1\), every pair of integers \(n,r\ge1\), and every prescribed colored ordered partition \(P\) of \([n]\) with \(m\) blocks, define
\[
\mathcal F_r(P)=\{(F_1,\ldots,F_r)\in\Sigma_n[G]^r:\ F_iF_j=F_jF_i\ (i,j\in[r]),\ F_1\cdots F_r=P\}.
\]
Writing \(b(F)\) for the number of blocks, the complete *joint block-count polynomial* is
\[
\boxed{\sum_{(F_i)\in\mathcal F_r(P)}\prod_{i=1}^r u_i^{b(F_i)}
=g^{r-1}\Big(\prod_{i=1}^r u_i\Big)
\Big(\sum_{\varnothing\ne S\subseteq[r]}g^{|S|-1}\prod_{i\in S}u_i\Big)^{m-1}.}
\]
In particular, the unweighted fiber size is
\[
\boxed{|\mathcal F_r(P)|=g^{r-1}\left(\frac{(g+1)^r-1}{g}\right)^{m-1}.}
\]
The quotient is an integer for positive integer \(g\). Thus this number depends only on \(g,r,m\), not the sizes of the blocks, their labels, or the isomorphism type of \(G\). For \(r=2\) it is \(g(g+2)^{m-1}\).

Summing all prescribed products, the exponential generating function recording *every factor's block count* is
\[
\boxed{\sum_{n\ge1}\frac{z^n}{n!}
\sum_{\substack{(F_1,\ldots,F_r)\in\Sigma_n[G]^r\\F_iF_j=F_jF_i\ \forall i,j}}
\prod_{i=1}^r u_i^{b(F_i)}
=\frac{g^r\left(\prod_i u_i\right)(e^z-1)}{1-\left(\prod_i(1+gu_i)-1\right)(e^z-1)}.}
\]
For all block weights equal to one, the exact number of tuples is
\[
\boxed{g^r\sum_{m=1}^n m!\,\left\{\begin{matrix}n\\m\end{matrix}\right\}\big((g+1)^r-1\big)^{m-1},}
\]
where the braces denote the Stirling number of the second kind.

## Assumptions and scope

An element of \(\Sigma_n[G]\), Hsiao's monoid of ordered \(G\)-partitions, is a list \(F=((B_1,a_1),\ldots,(B_k,a_k))\), where the \(B_i\) are nonempty, pairwise disjoint, and their union is \([n]\), and \(a_i\in G\). Its product with \(H=((C_1,c_1),\ldots,(C_l,c_l))\) is the row-major list of nonempty intersections \(B_i\cap C_j\), each labeled \(c_j a_i\). (For abelian \(G\), the order of the two colors is immaterial.) All products and commutations in the theorem are in this finite semigroup, not its semigroup algebra. Factors are ordered; the prescribed product has its actual sets and actual colors fixed. The theorem requires \(G\) abelian and finite; \(n\) and \(r\) are arbitrary positive integers.

## Proof

**Step 1 (uncolored compatibility).** Forget the colors. For two ordered partitions, the face-semigroup multiplication lists their nonempty intersections in row-major order, while the reverse product lists the same intersections in column-major order. These orders agree exactly when no pair of points is ordered strictly oppositely by the two partitions. In this case the strict comparison arising from either partition agrees whenever both distinguish a pair. For any family of pairwise commuting partitions, these consistent comparisons define a common weak total order: if \(x<y\) in one input and \(y<z\) in another, then in the first input \(x<z\) unless it also distinguishes \(y,z\), and if needed in the second input \(x<z\); any contrary ordering would be a forbidden inversion. Thus the ordered intersections of all input blocks form one ordered partition \(H=(D_1,\ldots,D_m)\), and each input is a merging of *consecutive* blocks of \(H\). Conversely every family obtained by merging consecutive blocks of a fixed \(H\) commutes, provided no consecutive blocks of \(H\) are merged by every input: the union of their cut sets separates every adjacency, hence the product is precisely \(H\).

Equivalently, at each of the \(m-1\) gaps between successive blocks of \(H\), record the nonempty set \(S\subseteq[r]\) of input partitions placing a cut there. Every independent choice of these nonempty sets produces a unique pairwise-commuting underlying tuple with product \(H\). Input \(i\) has \(1\) plus its total number of cuts across these gaps.

**Step 2 (abelian colors and fibers).** If two colored partitions have commuting uncolored projections, the intersection blocks of both products occur in the same order; their labels are \(a_i c_j\) and \(c_j a_i\), equal because \(G\) is abelian. Therefore colored commutation is equivalent to uncolored commutation. Conversely, colored equality of the two products obviously implies equality of their projections.

Fix the target \(P=((D_1,c_1),\ldots,(D_m,c_m))\) and one sequence of cut sets. On the first output block, choose labels for the \(r\) initial input blocks whose product equals \(c_1\); there are \(g^{r-1}\) solutions. At the next gap, suppose the set of factors starting a new block is \(S\) of size \(s\ge1\). The \(r-s\) continuing labels are already fixed. The product label required on the following output block determines one of the \(s\) new labels uniquely from the remaining \(s-1\), allowing exactly \(g^{s-1}\) assignments. Repeating independently over all gaps proves both the stated color multiplicities and, after recording the new block for each factor \(i\in S\), the product formula for the joint block-count polynomial. The proof uses only the size and abelian law of \(G\), not its group decomposition.

**Step 3 (all-product enumeration).** Exactly \(g^m m!\left\{\begin{smallmatrix}n\\m\end{smallmatrix}\right\}\) colored ordered partitions of \([n]\) have \(m\) blocks. Each has the same polynomial fiber. Use \(\sum_{n\ge m}m!\left\{\begin{smallmatrix}n\\m\end{smallmatrix}\right\}z^n/n!=(e^z-1)^m\) and sum the geometric series over \(m\ge1\). Since
\[
g\sum_{\varnothing\ne S\subseteq[r]}g^{|S|-1}\prod_{i\in S}u_i
=\prod_{i=1}^r(1+gu_i)-1,
\]
the claimed rational expression in \(e^z\) follows as a formal power-series identity.

## Verification

The included standard-library Python file `verify_colored_partitions.py` directly generates and multiplies ordinary colored ordered partitions. For cyclic groups of orders \(1,2,3\), it checks the *entire joint block-count polynomial over each prescribed product* for every pairwise-commuting pair through \(n=3\), and for triples through \(n=2\). It separately checks pairs over both the cyclic group of order four and the noncyclic Klein four-group at \(n=2\), and compares each total with the Stirling formula. All checked cases passed (`VERIFY_OK`). These computations corroborate, but are not prerequisites for, the arbitrary-\(n,r,G\) proof.

## Relationship to prior work

Hsiao, *A semigroup approach to wreath-product extensions of Solomon's descent algebras* (2007 preprint), §2.1 and Proposition 2, defines precisely this colored ordered-partition monoid and supplies a general multiplication/type-factorization matrix rule; that structure is prior work, not new here. Brown, *Semigroups, Rings, and Markov Chains* (2000), treats the uncolored braid-arrangement face monoid. Commutativity of compatible faces and common-refinement descriptions are classical antecedents, not claimed as original. Bastidas–Brauner–Saliola, *Left Regular Bands of Groups and the Mantaci–Reutenauer algebra* (2023 preprint), and Steinberg, *Topology and monoid representations II* (2024 preprint), study representation-theoretic structure of the colored monoid. The uncolored \(g=1,r=2\) total \(1,7,73,1015,\ldots\) is independently tabulated as OEIS A050352 (including its Stirling transform), and is **not** new. The contribution assessed here is the full elementwise prescribed-product fiber, simultaneous all-arity commuting condition, and joint block-count refinement, not its known uncolored specialization.

## Limitations

The construction is specific to the ordered-block intersection semigroup and finite **abelian** color groups. For nonabelian \(G\), equality of colored products imposes additional group commutation constraints and the formula generally fails already for \(n=1\). It does not describe arbitrary noncommuting product factorizations, ideals, representation modules, or semigroup-algebra primitive idempotents. Independent literature validation remains unperformed; an equivalent obscure formula could exist. The finite checks are not an infinite proof.

## References

1. S. K. Hsiao, *A semigroup approach to wreath-product extensions of Solomon's descent algebras*, arXiv:0710.2081 (first posted 10 October 2007), §2.1 and Proposition 2; https://arxiv.org/abs/0710.2081.
2. K. S. Brown, *Semigroups, Rings, and Markov Chains*, arXiv:math/0006145 (2000); https://arxiv.org/abs/math/0006145.
3. J. Bastidas, S. Brauner, F. Saliola, *Left Regular Bands of Groups and the Mantaci–Reutenauer algebra*, arXiv:2306.14985 (2023); https://arxiv.org/abs/2306.14985.
4. B. Steinberg, *Topology and monoid representations II: left regular bands of groups and Hsiao's monoid of ordered G-partitions*, arXiv:2404.03475 (2024); https://arxiv.org/abs/2404.03475.
5. OEIS A050352, prior numerical sequence and Stirling sum; https://oeis.org/A050352.
