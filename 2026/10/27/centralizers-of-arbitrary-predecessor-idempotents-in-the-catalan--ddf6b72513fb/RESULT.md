# Centralizers of arbitrary predecessor idempotents in the Catalan monoid

## Finding

For every integer \(n\ge1\), write \(C_n\) for the monoid under composition of all weakly increasing, regressive maps \(f:[n]\to[n]\); thus \(f(i)\le i\) and \(f(i)\le f(i+1)\). Every idempotent is a predecessor projection
\[
e_S(i)=\max\{s\in S:s\le i\},\qquad S=\{s_1=1<\cdots<s_k\}\subseteq[n].
\]
Put \(s_{k+1}=n+1\), \(B_j=[s_j,s_{j+1}-1]\), and \(d_j=|B_j|=s_{j+1}-s_j\). For \(1\le a\le j\le k\), define
\[
w_j(a)=\begin{cases}
\operatorname{Cat}_{d_j}=\dfrac1{d_j+1}\binom{2d_j}{d_j},&a=j,\\[3pt]
\binom{d_j+d_a-2}{d_j-1},&a<j.
\end{cases}
\]
For any weakly increasing regressive map \(g:[k]\to[k]\), put \(v_j(g)=1\) if \(j<k\) and \(g(j)=g(j+1)\), and put \(v_j(g)=w_j(g(j))\) otherwise. Then the **whole element-centralizer of each idempotent**, not just its idempotent part, has cardinality
\[
\boxed{Z_n(S)=\#\{f\in C_n:fe_S=e_Sf\}
=\sum_{g\in C_k}\prod_{j=1}^{k}v_j(g).}
\]
The formula has the following quadratic-time transfer form. Initialize \(D_1(1)=1\), and for \(2\le j\le k\) and \(1\le b\le j\) set
\[
\boxed{D_j(b)=D_{j-1}(b)+\sum_{a=1}^{b-1}D_{j-1}(a)w_{j-1}(a),\qquad
Z_n(S)=\sum_{b=1}^{k}D_k(b)w_k(b).}
\]
Here out-of-range states are zero. Prefix sums evaluate every stage in linear time, so the total uses \(O(k^2)\) arithmetic operations.

The centralizer size depends on the **placement**, not merely the rank, of the fixed points: at \(n=6\), fixed sets \(S=\{1,2,6\}\) and \(T=\{1,5,6\}\) both have size three, but \(Z_6(S)=18\) and \(Z_6(T)=31\). As boundary checks, the constant map and the identity each commute with the whole monoid and yield \(\operatorname{Cat}_n\).

## Assumptions and scope

The degree \(n\) is any positive integer, and \([n]=\{1,\ldots,n\}\) has its usual total order. Products use ordinary function composition; the commutation equation is convention-independent. A regressive map satisfies \(f(i)\le i\). A map is weakly increasing if it is order-preserving. The centralizer includes **all** commuting transformations, whether or not they are idempotent, and the idempotent \(e_S\) is arbitrary. Arithmetic complexity counts integer arithmetic operations, not bit operations on large integers.

## Proof

**Idempotents.** Suppose \(e\in C_n\) is idempotent. Its image \(S\) is the fixed-point set, contains \(1\), and has \(e(i)\in S\cap[1,i]\). If \(s\in S\) and \(s\le i\), monotonicity gives \(s=e(s)\le e(i)\). Thus \(e(i)\) is the largest fixed point not exceeding \(i\), so \(e=e_S\). Conversely, each displayed \(e_S\) is weakly increasing, regressive, and idempotent.

**Restriction to the fixed set.** Fix \(e=e_S\) and \(f\in C_n\). If \(fe=ef\), then evaluating at \(s_j\) gives \(f(s_j)=e(f(s_j))\in S\). There is therefore a uniquely determined map \(g:[k]\to[k]\) with \(f(s_j)=s_{g(j)}\). Since \(f\) is increasing and regressive, \(g\) is increasing and \(g(j)\le j\). For every \(x\in B_j\), the commutation equation reads
\[
e(f(x))=f(e(x))=f(s_j)=s_{g(j)},
\]
so \(f(x)\in B_{g(j)}\). Conversely, if an increasing regressive \(f\) respects the fixed-set values and these block constraints, then this displayed identity holds for every \(x\), and hence \(fe=ef\).

**Within a block.** Fix \(g(j)=a\). The value of \(f\) at the first point of \(B_j\) is \(s_a\). If \(a<j\), any weakly increasing sequence of \(d_j-1\) remaining entries in the target block \(B_a\), of size \(d_a\), is regressive on the source block, since every target entry is strictly below \(s_j\). Stars and bars therefore gives exactly \(\binom{d_j+d_a-2}{d_j-1}\) choices. If \(a=j\), the restriction to \(B_j\), after shifting the origin, is precisely a weakly increasing regressive transformation of a \(d_j\)-point chain, of which there are \(\operatorname{Cat}_{d_j}\). Thus an unconstrained block has \(w_j(a)\) choices.

**Between adjacent blocks.** If \(g(j)<g(j+1)\), the target blocks \(B_{g(j)}\) and \(B_{g(j+1)}\) are strictly ordered, so all independently chosen restrictions are automatically increasing across the boundary. If \(g(j)=g(j+1)=a\), the first value in the next block is \(f(s_{j+1})=s_a\), while every value in the preceding block is at least \(f(s_j)=s_a\). Monotonicity therefore forces the whole preceding block to be constantly \(s_a\); this produces one, rather than \(w_j(a)\), choice. There are no other compatibility constraints. Multiplication over the blocks and disjoint summation over admissible \(g\in C_k\) prove the first formula.

**Transfer recurrence.** Let \(D_j(b)\) be the weighted sum over prefixes \((g(1),\ldots,g(j))\) ending at \(g(j)=b\), with the block factors of stages \(1,\ldots,j-1\) accounted for. The first state is \(D_1(1)=1\). Given a previous value \(a\le b\), if \(a=b\) the previous block is forced constant (factor one), contributing \(D_{j-1}(b)\). If \(a<b\), the previous block is free (factor \(w_{j-1}(a)\)), contributing \(D_{j-1}(a)w_{j-1}(a)\). These are all possibilities. The final block always contributes \(w_k(b)\). This proves the recurrence and terminal evaluation. Successive prefix sums yield \(O(k^2)\) arithmetic operations.

**Rank does not determine the answer.** Substituting the block lengths \((1,4,1)\) for \(S=\{1,2,6\}\) gives \(Z_6(S)=18\). Substituting \((4,1,1)\) for \(T=\{1,5,6\}\) gives \(Z_6(T)=31\). These values may also be checked by complete enumeration of all \(132\) elements of \(C_6\). The proof above holds for every \(n\), independently of that finite check.

## Verification

The standalone \(verify.py\) uses the standard library only. It generates every Catalan transformation, constructs each idempotent by its fixed-point subset, checks commutation by direct composition, evaluates the weighted expression and the transfer recurrence independently, and compares all three. Exhaustive checks pass for every \(n=1,\ldots,9\), testing all \(2^{n-1}\) idempotents at each degree. The script also verifies the two stated rank-three examples. This finite verification corroborates but does not replace the general proof.

## Relationship to prior work

Margolis and Steinberg give the Catalan-monoid normal form and identify its monoid algebra with an incidence algebra. Their convention uses order-preserving extensive maps; reversing the finite chain identifies that monoid with the regressive convention used here. Their full paper proves representation-theoretic statements and does not give this element-centralizer enumeration. Santocanale describes idempotent monotone paths and explains classical idempotent-counting results. Its monoid of join-continuous maps is not identical to the Catalan submonoid, and its examined text does not contain the displayed commuting-element centralizer or weighted transfer formula. Older work counts idempotents and transformations with prescribed fixed-point sets, which is a different statistic from commuting with a prescribed idempotent. The result here counts all elements in each such centralizer and separates same-rank idempotents.

## Limitations

The finding concerns only finite **total**, order-preserving, regressive transformations, not all monotone maps, the non-expansive contraction monoid, partial Catalan monoids, or transformations that only share fixed points with \(e_S\). The weighted sum and recurrence do not directly give a closed formula for the histogram of centralizer sizes over all idempotents. We do not claim a complete classification of centralizer submonoids up to isomorphism or the absence of potentially unindexed equivalent older formulas. No independent audit or external validation has been performed.

## References

1. S. Margolis and B. Steinberg, *The algebra of the Catalan monoid as an incidence algebra: a simple proof*, arXiv:1806.06531v1 (first public posting 18 June 2018), §§1–3. https://arxiv.org/abs/1806.06531
2. L. Santocanale, *On discrete idempotent paths*, arXiv:1906.05590v1 (first public posting 13 June 2019), §§1–4. https://arxiv.org/abs/1906.05590
3. P. Higgins, *Combinatorial aspects of semigroups of order-preserving and decreasing functions*, in *Semigroups (Luino, 1992)* (1993), pp. 103–110. Cited for historical background, not assessed as a source-level noncoverage proof.
