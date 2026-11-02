# Exact coprime-matching multiplicities for two-prime-power divisor sets

## Finding

For distinct primes \(p,q\), integers \(a,b\geq1\), and an arbitrary set \(X\) of \(N=(a+1)(b+1)\) **distinct integers**, put \(n=p^a q^b\). Let \(M_n(X)\) be the number of bijections \(\phi:X\to D(n)\), where \(D(n)\) denotes the positive divisors of \(n\), for which \(\gcd(x,\phi(x))=1\) for every \(x\in X\).

Define the four disjoint divisibility-class sizes
\[
\begin{aligned}
T&=\#\{x\in X:pq\mid x\},\\
B&=\#\{x\in X:p\mid x,\ q\nmid x\},\\
C&=\#\{x\in X:q\mid x,\ p\nmid x\},\\
R&=N-T-B-C.
\end{aligned}
\]
For nonnegative integers \(u\), define the falling factorial with its zero extension
\[
F_u(k)=\begin{cases}u!/(u-k)!,&0\leq k\leq u,\\0,&\text{otherwise}.\end{cases}
\]
Then **the entire matching count** is
\[
\boxed{M_n(X)=\begin{cases}
0,&T\geq2,\\
F_b(B)F_a(C)R!,&T=1,\\
\bigl[F_b(B)F_a(C)+B F_b(B-1)F_a(C)+C F_a(C-1)F_b(B)\bigr](N-B-C)!,&T=0.
\end{cases}}
\]
The value is a nonnegative integer and the formulas have no restriction on the relative sizes of \(p,q,a,b\), the signs of members of \(X\), or any arithmetic-progression hypothesis.

An equivalent complete existence classification for arbitrary such \(X\) is: if \(T\geq2\), no matching exists; if \(T=1\), a matching exists precisely when \(B\leq b\) and \(C\leq a\); if \(T=0\), a matching exists precisely when \(B\leq b+1\), \(C\leq a+1\), and not simultaneously \(B=b+1\) and \(C=a+1\).

**Quantitative distinction beyond the one-prime existence data.** Take \(n=225=3^2 5^2\), so \(N=9\), and the two arithmetic progressions
\[
X=\{1,3,5,7,9,11,13,15,17\},\qquad
Y=\{1,5,9,13,17,21,25,29,33\}.
\]
Both contain exactly three multiples of \(3\) and two multiples of \(5\). However \(X\) contains the multiple \(15\) of both primes whereas \(Y\) contains none, so the formula gives
\[
\boxed{M_{225}(X)=480,\qquad M_{225}(Y)=288.}
\]
Thus the two individual prime-divisibility counts sufficient to decide **existence for arithmetic progressions** do not determine their **number** of coprime matchings. The intersection count matters.

## Assumptions and scope

The theorem applies to exactly two distinct prime factors, both with positive exponents, and to a set of \(N\) distinct integers. The divisors and the integers in \(X\) are treated as individually labelled by their distinct values; exchanging two different targets gives different bijections. A zero member of \(X\) is allowed and belongs to the doubly divisible class. The squarefree example \(a=b=1\) is included. The factorial \(0!\) equals \(1\). All inequalities in the support characterization concern nonnegative integer class counts arising from an actual \(X\).

## Proof

Every divisor of \(n\) has the unique form \(p^i q^j\) with \(0\leq i\leq a\) and \(0\leq j\leq b\). Thus the divisors form a rectangle with \(N\) cells. A member of class \(T\) is coprime only to the corner \(1=p^0q^0\). A member of class \(B\) may use precisely the \(b+1\) divisors \(1,q,\ldots,q^b\); a member of class \(C\) may use precisely the \(a+1\) divisors \(1,p,\ldots,p^a\). A member of class \(R\) may use any divisor. The two restricted lists intersect only at \(1\).

If \(T\geq2\), distinct members would each require the same divisor \(1\), so the permanent is zero. If \(T=1\), its unique member is forced to \(1\). The \(B\) individually distinguished members inject into the \(b\) targets \(q,\ldots,q^b\) in \(F_b(B)\) ways; independently the \(C\) members inject into the \(a\) targets \(p,\ldots,p^a\) in \(F_a(C)\) ways. The \(R\) unrestricted members biject to the \(R=N-1-B-C\) remaining divisors in \(R!\) ways. Multiplication gives the second case, with automatic zero whenever one injection is impossible.

Now let \(T=0\). Partition matchings according to whether divisor \(1\) is assigned to a member of class \(R\), of class \(B\), or of class \(C\). In the first case the \(B\) members use the \(b\) nonunit \(q\)-powers and the \(C\) members use the \(a\) nonunit \(p\)-powers. Their injections contribute \(F_b(B)F_a(C)\); all remaining divisors (including \(1\)) are assigned to unrestricted members in \((N-B-C)!\) ways. In the second case, choose the \(B\) member assigned to \(1\) in \(B\) ways, inject the remaining \(B-1\) members into \(b\) nonunit \(q\)-powers and the \(C\) members into \(a\) nonunit \(p\)-powers, then permute the unrestricted members. This contributes \(B F_b(B-1)F_a(C)(N-B-C)!\). The third case contributes \(C F_a(C-1)F_b(B)(N-B-C)!\) by symmetry. These cases are disjoint and exhaustive. Summing proves the formula. Cases with no unrestricted members cause no overcount: because \(N=(a+1)(b+1)>a+b+1\), the relevant falling-factorial factors then vanish.

Every summand in the formula is nonnegative. For \(T=1\), positivity is equivalent to \(B\leq b\) and \(C\leq a\). For \(T=0\), positivity holds exactly if one of the three assignments of \(1\) is possible: either \(B\leq b,C\leq a\), or \(B\leq b+1,C\leq a\), or \(B\leq b,C\leq a+1\). This disjunction simplifies to the stated characterization. The evaluation at \(n=225\) follows by substitution: for \(X\), \((T,B,C,R)=(1,2,1,5)\), giving \(2\cdot2\cdot120=480\); for \(Y\), \((0,3,2,4)\), giving \(3\cdot2\cdot2\cdot24=288\). Both progressions satisfy the separate one-prime capacity inequalities.

## Verification

The accompanying standalone `verify_coprime_matchings.py` independently computes the full permanent by dynamic programming over subsets of divisors, with exact integers and exact gcd tests. It compares this count against the explicit formula for \(7776\) arithmetic-progressions across distinct prime pairs and exponent pairs. It also tests all \(846\) possible four-class occupancy profiles for a collection of small exponent pairs, constructing genuinely distinct integer representatives of each class. The run reports

`VERIFY_OK progression_cases=7776 occupancy_cases=846 positive=4281 zero=3495 exact_permanent_dp=yes`

No floating-point arithmetic is used. The verifier checks finite inputs only; the proof above establishes the theorem for arbitrary valid primes, exponents, and sets.

## Relationship to prior work

Max A. Alekseyev, *Coprime matchings of divisor sets* (arXiv:2610.37512v1, 27 October 2026), Theorem 1.1, determines whether a coprime matching exists when the target set is an arithmetic progression using one divisibility count for each prime. Its proof constructs some matchings; it does not evaluate the total number of them. Our result evaluates that number for every set, in the full two-prime-power family, and the \(225\) example shows concretely that the original one-prime counts cannot recover this multiplicity.

Nathan McNew and Carl Pomerance, *Matchable numbers* (arXiv:2604.05304, first posted 7 April 2026), study existence and density of matchable integers, not the evaluated two-prime-power permanent. Ashwin Sah and Mehtaab Sawhney, *Enumerating coprime permutations* (arXiv:2203.06268, 2022), count permutations on an interval asymptotically; their domain is not the divisor set \(D(p^a q^b)\). Generic permanent algorithms apply to every finite bipartite graph, but do not themselves provide the explicit constant-time expression in three divisibility-class counts.

## Limitations

The expression is restricted to integers with exactly two distinct prime factors, since three or more prime supports create additional overlaps between permitted divisor faces. It does not give a closed formula for arbitrary semiprime-support rank, nor a limiting distribution for random progressions. The exact finite formula and its proof are complete; priority with respect to earlier specialized permanent evaluations remains subject to independent literature review. All computational checks are finite corroborations, not proofs of the unrestricted assertion.

## References

1. M. A. Alekseyev, *Coprime matchings of divisor sets*, arXiv:2610.37512v1, 27 October 2026. https://arxiv.org/html/2610.37512v1
2. N. McNew and C. Pomerance, *Matchable numbers*, arXiv:2604.05304v1, 7 April 2026. https://arxiv.org/html/2604.05304v2
3. A. Sah and M. Sawhney, *Enumerating coprime permutations*, *Mathematika* 68 (2022), 1120–1134; arXiv:2203.06268. https://doi.org/10.1112/mtk.12159
4. C. Pomerance, *Coprime matchings*, *Integers* 22 (2022), A2; arXiv:2111.07157. https://arxiv.org/abs/2111.07157
