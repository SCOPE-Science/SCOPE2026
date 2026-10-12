# Sharp arithmetic morphism criterion and fiber-rigidity transition for finite quorum modal algebras

## Finding

For integers \(n\ge 1\) and \(1\le k\le n\), let \(\mathbf Q_{n,k}\) be the finite Boolean algebra \(\mathcal P([n])\) equipped with the monotone, generally non-normal unary operation
\[
  Q_{n,k}(S)=\begin{cases}[n],&|S|\ge k,\\ \varnothing,&|S|<k.\end{cases}
\]
The associated neighborhood frame has, at every world, precisely the neighborhoods containing at least \(k\) worlds. A homomorphism must preserve the Boolean operations and \(Q\).

**Complete classification.** For \(m,n\ge1\), \(1\le\ell\le m\), and \(1\le k\le n\), every homomorphism \(h:\mathbf Q_{m,\ell}\to\mathbf Q_{n,k}\) is the inverse-image map of a **surjection** \(f:[n]\twoheadrightarrow[m]\). Writing its positive fiber sizes in nondecreasing order as \(\lambda_1\le\cdots\le\lambda_m\), it is a homomorphism exactly when
\[
 \lambda_1+\cdots+\lambda_{\ell}\ \ge k
 \quad\text{and}\quad
 \lambda_{m-\ell+2}+\cdots+\lambda_m<k.
 \tag{1}
\]
The second sum is empty if \(\ell=1\). Consequently, if \(n<m\), no such homomorphism exists. If \(n\ge m\), write \(n=qm+r\) with \(0\le r<m\). Then one exists **if and only if**
\[
 (\ell-1)q+\min(\ell-1,r)
 < k \le
 \ell q+\max(0,\ell-(m-r)).
 \tag{2}
\]

The exact number of homomorphisms is the finite partition sum
\[
 \boxed{\displaystyle
 H(n,k;m,\ell)=n!m!
 \sum_{\substack{1\le\lambda_1\le\cdots\le\lambda_m,\;\sum_i\lambda_i=n\\
 \sum_{i=1}^{\ell}\lambda_i\ge k,\;
 \sum_{i=m-\ell+2}^{m}\lambda_i<k}}
 \frac{1}{\bigl(\prod_i\lambda_i!\bigr)
            \bigl(\prod_{s\ge1}\mu_s(\lambda)!\bigr)},
 }
 \tag{3}
\]
where \(\mu_s(\lambda)\) is the multiplicity of size \(s\) in the partition, and an impossible parameter range gives zero.

**Rigidity and the sharp boundary transition.** Every endomorphism of \(\mathbf Q_{n,k}\) is a permutation of its \(n\) atoms. In particular,
\[
 \operatorname{End}(\mathbf Q_{n,k})
 =\operatorname{Aut}(\mathbf Q_{n,k})\cong S_n,
 \qquad |\operatorname{End}(\mathbf Q_{n,k})|=n!,
\]
and the identity is its only idempotent endomorphism. More precisely, suppose \(n=qm\), \(m\ge3\), and \(2\le\ell\le m-1\). Homomorphisms exist exactly for
\[
 (\ell-1)q+1\le k\le\ell q.
\]
At either endpoint, **every** homomorphism has all its fibers of size \(q\), so its number is exactly \(n!/(q!)^m\). For each strictly interior integer quota, unequal fiber sizes are possible if and only if \(q\ge3\); the explicit profile \((q-1,q,\ldots,q,q+1)\) witnesses the failure of balanced-fiber rigidity. Thus \(q=3\) is the first block size permitting symmetry-breaking for an interior quota.

For instance, for maps from \(\mathbf Q_{3,2}\) into \(\mathbf Q_{9,k}\), the homomorphism numbers at \(k=4,5,6\) are exactly
\[
 1680,\quad11130,\quad1680.
\]
At \(k=5\) the permitted sorted profiles are \((3,3,3)\), \((2,3,4)\), and \((1,4,4)\); their contributions are \(1680\), \(7560\), and \(1890\), respectively. All homomorphisms are Boolean embeddings. There is also the complement-dual symmetry
\[
 H(n,k;m,\ell)=H(n,n-k+1;m,m-\ell+1).
 \tag{4}
\]

## Assumptions and scope

All underlying sets are finite and nonempty, all quotas are integers in the stated ranges, and the single additional algebra operation is exactly the global cardinality threshold. The operation is monotone but for interior quotas is generally not additive; the theorem is about **monotone neighborhood algebras**, not ordinary normal modal algebras. Homomorphisms preserve \(0,1\), complement, binary Boolean operations and the displayed unary operation, with no distinguished atom names required. Worlds and atoms are labeled for the counting formula. No assertion is made about other neighborhood modalities or weighted quotas not induced by integer fiber cardinalities.

## Proof

**Step 1: functions and extremal subset inequalities.** Every homomorphism of finite powerset Boolean algebras \(\mathcal P([m])\to\mathcal P([n])\) is uniquely \(h(S)=f^{-1}(S)\) for some \(f:[n]\to[m]\): the images of the \(m\) atoms partition \([n]\), and each element of \([n]\) belongs to precisely one atom image. The commutation equation \(h(Q_{m,\ell}(S))=Q_{n,k}(h(S))\) is, for **every** \(S\subseteq[m]\), exactly
\[
 |S|\ge\ell\quad\Longleftrightarrow\quad
 \sum_{j\in S}|f^{-1}(j)|\ge k.
 \tag{5}
\]
If \(f^{-1}(j)=\varnothing\), adjoining \(j\) to a subset of size \(\ell-1\) not containing it changes the left predicate and not the right, contradicting (5). Therefore \(f\) is surjective. Since the weights are positive, it suffices to check the largest possible weight among subsets of size \(\ell-1\) and the smallest among subsets of size \(\ell\). Sorting the weights yields exactly (1). Conversely (1) forces (5) for every smaller or larger subset by monotonicity.

**Step 2: balancing is optimal.** For a positive integer vector of length \(m\) and sum \(n\), transferring a unit from an entry exceeding another by at least two toward the smaller entry weakly decreases every sum of the \(p\) largest entries and weakly increases every sum of the \(p\) smallest entries. Repeating reaches the balanced vector with \(m-r\) entries equal to \(q\) and \(r\) equal to \(q+1\). Thus, if any vector satisfies (1), the balanced vector does. The largest \(\ell-1\) balanced entries sum to \((\ell-1)q+\min(\ell-1,r)\); the smallest \(\ell\) sum to \(\ell q+\max(0,\ell-(m-r))\). This proves both necessity and sufficiency of (2), including \(m=1\) and both endpoint quotas.

**Step 3: count functions exactly.** Fix a sorted permissible profile \(\lambda\). There are \(m!/\prod_s\mu_s(\lambda)!\) ways to assign its parts to the \(m\) labeled codomain elements, and for each ordered assignment there are \(n!/\prod_i\lambda_i!\) functions with those prescribed fibers. Summation proves (3). Every map is surjective, so its inverse-image homomorphism is injective and has image size \(2^m\).

**Step 4: endomorphism rigidity.** If \(m=n\), every surjective map of these finite sets is a permutation. Every permutation preserves cardinalities, and hence it preserves the threshold operation exactly when \(k=\ell\): take any set of the quota boundary size to rule out unequal quotas. This gives the automorphism group and the idempotent statement.

**Step 5: endpoint rigidity and symmetry-breaking.** For \(n=qm\) and any nonconstant sorted positive profile with average \(q\), the sum of its largest \(p\) entries is **strictly** greater than \(pq\) and the sum of its smallest \(p\) entries is strictly less than \(pq\), for every \(1\le p<m\). Indeed equality of a top partial sum to its overall average would force every entry to be \(q\): the top entries are each at least every remaining one; if they averaged \(q\), the remaining entries would also have to average \(q\), leaving no nonconstant arrangement. Applying this with \(p=\ell-1\) and \(p=\ell\) excludes all unequal profiles at the lower and upper quota endpoints, respectively. For a strictly interior \(k\), the profile with one \(q-1\), one \(q+1\), and the rest \(q\) has largest \(\ell-1\) sum \((\ell-1)q+1\) and smallest \(\ell\) sum \(\ell q-1\), so (1) holds. Such an interior integer exists exactly when \(q\ge3\). The example is a direct evaluation of (3).

**Step 6: dual quota.** Since inverse images commute with complements, preservation of \(Q_{n,k}\) is equivalent to preservation of its Boolean dual \(S\mapsto[n]\setminus Q_{n,k}([n]\setminus S)\), which equals \(Q_{n,n-k+1}\). Applying this simultaneously at both ends proves (4).

## Verification

The accompanying standalone \(\texttt{verify.py}\) enumerates every function \([n]\to[m]\) for \(1\le n,m\le6\), independently tests the modal-homomorphism equation on **all** codomain subsets and all quota pairs, and compares its result with (2), (3), the duality symmetry, and endomorphism rigidity. This means 82,200 concrete function tables and 441 parameter comparisons. It separately checks all 19,683 functions \([9]\to[3]\) for the three nontrivial sample quotas. The exact execution output is recorded in \(\texttt{VERIFICATION.md}\). These finite checks are corroboration only; the proof above establishes the unrestricted finite-parameter theorem.

## Relationship to prior work

Finite powerset duality and coalgebraic modal algebra are established in Bezhanishvili, Carai, and Morandi (2020/2022). Bezhanishvili, Bezhanishvili, and de Groot (2021/2022) give general duality for neighborhood algebras and, in particular, for monotone neighborhood frames; their definition of a neighborhood morphism is exactly the inverse-image preservation relation used here. That general semantic correspondence is not claimed as new. Uniform cardinality quotas are also elementary examples of weighted simple voting games. Published work on quorum constraints and integer representations studies their winning sets and weight representations, but the inspected material did not supply the joint fixed-total existence formula, homomorphism census, and endpoint-rigidity/interior-symmetry-breaking law stated here.

## Limitations

No independent audit has been carried out. The proof covers this one global cardinality-threshold operator and does not directly classify local, asymmetric, or arbitrary weighted neighborhood systems. A specialized voting-game result may encode part of the arithmetic conditions implicitly; the novelty of the full categorical/counting combination should be checked further before a priority claim. Exhaustive tests stop at the finite sizes specified above.

## References

1. G. Bezhanishvili, L. Carai, P. Morandi, *Duality for Powerset Coalgebras*, arXiv:2008.01849v1 (first public August 4, 2020); *Logical Methods in Computer Science* 18(1), 2022. https://arxiv.org/abs/2008.01849
2. G. Bezhanishvili, N. Bezhanishvili, J. de Groot, *A Coalgebraic Approach to Dualities for Neighborhood Frames*, arXiv:2106.01628v1 (June 3, 2021); *Logical Methods in Computer Science* 18(3), 2022. https://arxiv.org/abs/2106.01628
3. *Quorum Constraints and Filters in Boolean Lattices*, *Journal of Combinatorial Mathematics and Combinatorial Computing* 48 (2004), 115–137. https://combinatorialpress.com/jcmcc-articles/volume-048/quorum-constraints-and-filters-in-boolean-lattices/
4. *On Weights and Quotas for Weighted Majority Voting Games*, *Games* 12(4), article 91 (2021). https://www.mdpi.com/2073-4336/12/4/91
