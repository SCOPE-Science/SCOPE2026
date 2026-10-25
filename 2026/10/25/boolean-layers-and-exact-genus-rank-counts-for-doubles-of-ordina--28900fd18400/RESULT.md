# Boolean layers and exact genus–rank counts for doubles of ordinary numerical semigroups

## Finding
Let \(m\ge2\) be an integer and let \(O_m=\{0\}\cup\{n\in\mathbb N_0:n\ge m\}\). A numerical semigroup \(S\subseteq\mathbb N_0\) lies in the fixed-quotient fiber
\[
\mathcal F_m=\{S:S/2=O_m\},\qquad S/2=\{n\in\mathbb N_0:2n\in S\},
\]
if and only if it has the following **unique normal form**. Choose an odd integer \(b\ge m\) and an arbitrary set
\[
B\subseteq\{b+2,b+4,\ldots,b+2m-2\}.
\]
Then
\[
\boxed{S=S_{m,b,B}=\{0\}\cup\{2n:n\ge m\}\cup\{b\}\cup B\cup\{b+2m+2j:j\ge0\}.}
\]
No compatibility conditions on \(B\) are required. For a fixed least odd element \(b\), the fiber forms a Boolean interval of dimension \(m-1\), ordered by inclusion of \(B\).

Define the **relative rank** \(r_m(S)\) as the smallest cardinality of a finite set \(A\subset S\setminus2O_m\) such that \(S=\langle A\rangle+2O_m\), where the right side means the Minkowski sum of additive submonoids. The unique minimal relative generating set is
\[
\boxed{A=\{b\}\cup B,\qquad r_m(S)=1+|B|.}
\]
Write \(g(S)=|\mathbb N_0\setminus S|\) for the genus and \(b_0=m\) for odd \(m\), \(b_0=m+1\) for even \(m\). Put
\[
g_0=m-1+\frac{b_0-1}{2}.
\]
For integers \(g\ge0\) and \(r\ge1\), the **complete joint genus–relative-rank census** is
\[
\boxed{\#\{S\in\mathcal F_m:g(S)=g,\ r_m(S)=r\}=
\begin{cases}
\binom{m-1}{r-1},&1\le r\le m\text{ and }g\ge g_0+m-r,\\
0,&\text{otherwise}.
\end{cases}}
\]
Equivalently, the bivariate formal series is
\[
\boxed{\sum_{S\in\mathcal F_m}z^{g(S)}w^{r_m(S)}
=\frac{z^{g_0}w(z+w)^{m-1}}{1-z}.}
\]
In particular, the minimum genus \(g_0\) is attained by exactly one member; the numerical value of this minimum also follows from the earlier general theorem of Strazzanti (2015) and is **not** claimed as independently new. The number of members of genus \(g\) stabilizes **exactly** at \(2^{m-1}\) for every \(g\ge g_0+m-1\). At those genera the relative-rank counts are the binomial row \(\binom{m-1}{r-1}\) for \(1\le r\le m\).

For completeness, the Frobenius number can also be recovered exactly. With \(J=\{j\in\{1,\ldots,m-1\}:b+2j\notin B\}\),
\[
\boxed{F(S)=\max\big(\{2m-2,b-2\}\cup\{b+2j:j\in J\}\big).}
\]
The fiber has a unique inclusion-maximal member, namely \(S_{m,b_0,B_0}\), where \(B_0\) consists of all \(m-1\) allowable intermediate odd integers.

## Assumptions and scope
All integers are ordinary nonnegative integers. A numerical semigroup is a cofinite additive submonoid of \(\mathbb N_0\). The parameter is any fixed integer \(m\ge2\). The quotient is by exactly \(2\); it is *not* the multiplicative product of numerical-semigroup ideals. The invariant \(r_m\) is the relative generator rank within the fixed quotient fiber, not the quotient rank obtained by varying the divisor or the ordinary embedding dimension.

For the formal bivariate series, \(z\) and \(w\) are indeterminates. Since the coefficient of every fixed power of \(z\) is finite, the displayed identity is well-defined as an element of \(\mathbb Z[w][[z]]\). No assertion is made about larger quotient divisors or arbitrary target numerical semigroups.

## Proof
**1. Forced parity and the first odd element.** The equation \(S/2=O_m\) is equivalent to
\[
S\cap2\mathbb N_0=2O_m=\{0\}\cup\{2m,2m+2,\ldots\}.
\]
Because \(S\) is cofinite, it contains an odd positive integer. Let \(b\) be its least such integer. The additive closure condition yields \(2b\in S\), and the fixed even part forces \(2b\ge2m\), hence \(b\ge m\). Adding the allowed even integers \(2m+2j\) to \(b\) shows that \(b+2m+2j\in S\) for every \(j\ge0\). There are exactly \(m-1\) odd integers strictly between \(b\) and \(b+2m\), so all freedom is contained in the subset \(B=S\cap\{b+2,\ldots,b+2m-2\}\). This proves uniqueness and necessity of the proposed normal form.

**2. Converse: no omitted condition.** Given any allowed \((b,B)\), the proposed set contains zero, all even numbers at least \(2m\), and all odd numbers at least \(b+2m\), hence is cofinite. Sums of two positive even elements are allowed even elements. Any sum of a positive even element with an odd element is at least \(2m+b\) and therefore belongs to the odd tail. A sum of two odd elements is even and at least \(2b\ge2m\), so it is allowed as well. Thus the set is an additive monoid with exactly the even part \(2O_m\), establishing sufficiency. The distinct \((b,B)\) are distinguished by the least positive odd element and the intermediate odd membership pattern.

**3. Relative minimal generators.** Let \(A=\{b\}\cup B\). The normal form shows \(S=\langle A\rangle+2O_m\): every odd element not in \(A\) is \(b+2m+2j\) for some \(j\ge0\), hence belongs to \(b+2O_m\); all even elements already belong to \(2O_m\). Conversely, the closure proved in step 2 gives the inclusion in the other direction. Every \(a\in A\) lies in \([b,b+2m)\). It cannot be obtained from other elements of \(A\) and \(2O_m\): adding a positive member of \(2O_m\) increases an odd summand by at least \(2m\); any expression using three or more odd summands is at least \(3b\ge b+2m\); an expression with two odd summands is even. Consequently, \(A\) is indispensable. Any relative generating system must contain each element of \(A\), giving uniqueness and \(r_m(S)=1+|B|\).

**4. Genus and exact series.** The forbidden positive evens are exactly \(2,4,\ldots,2m-2\), contributing \(m-1\) gaps. The positive odds below \(b\) contribute \((b-1)/2\) gaps. Of the \(m-1\) intermediate odd positions, exactly \(m-1-|B|\) are gaps, and the odd tail has none. Therefore
\[
g(S)=2m-2+\frac{b-1}{2}-|B|.
\]
Write \(b=b_0+2h\), where \(h\ge0\), and \(r=1+|B|\). Substitution gives the exact identity \(g(S)=g_0+m-r+h\). For any fixed \(r\in\{1,\ldots,m\}\) and \(g\), the value of \(h\) is forced, and is admissible precisely when \(g\ge g_0+m-r\). There are exactly \(\binom{m-1}{r-1}\) subsets \(B\) of that cardinality. This proves the joint counting formula.

Summing over all \(h\ge0\) and all subsets \(B\) gives
\[
\sum_{h\ge0}z^h\sum_{r=1}^{m}\binom{m-1}{r-1}z^{g_0+m-r}w^r
=\frac{z^{g_0}w(z+w)^{m-1}}{1-z}.
\]
The single choice at \(g=g_0\) is \(b=b_0\) and \(B=B_0\). If \(g\ge g_0+m-1\), every rank condition is admissible, and summing the binomial row gives \(2^{m-1}\). For smaller \(g\), the rank-one term is absent, making this the sharp stabilization threshold.

**5. Frobenius number, order, and maximal member.** The gap list in step 4 is exhaustive. The last excluded even is \(2m-2\); the last odd below \(b\) is \(b-2\); and the remaining odd gaps are precisely \(b+2j\) for \(j\in J\). Their maximum is the stated Frobenius number. For a fixed \(b\), all semigroups have the same forced even and odd-tail parts, so inclusion is exactly inclusion of their \(B\)-subsets, a Boolean lattice of rank \(m-1\). The semigroup with \(b=b_0\) and full \(B_0\) contains every odd \(n\ge b_0\) and every allowed even number; all other fiber elements are subsets of it. Thus it is the unique maximum.

## Verification
The included self-contained Python 3 verifier, `verify.py`, implements numerical-semigroup closure by dynamic programming independently of the normal-form membership function. It checked 2,794 parameter triples with \(2\le m\le8\), eleven admissible choices of the smallest odd element for each \(m\), and every Boolean intermediate subset. For every triple it compared all memberships through at least \(300\), the gap count, and the relative generating set. In addition, it independently enumerated finite-cofinite odd-membership masks in a bounded window for \(m=2,3,4,5\), and checked the complete genus–rank formula for those \(m\) across fifteen consecutive genera (also \(m=6,7,8\)). Results were `PARAMETER_CASES_OK 2794`, `BRUTE_FIBER_SLICE_OK` for \(m=2,3,4,5\), `JOINT_CENSUS_OK`, and `VERIFY_OK`.

Run from the directory containing the included files:

```shell
python3 verify.py
```

All infinite-parameter conclusions follow from steps 1–5. Bounded computation is a supplementary check, not an infinite proof or an exhaustive search of the literature.

## Relationship to prior work
Ojeda and Rosales, *On Numerical Semigroups with Fixed Quotient*, arXiv:2605.14775v1 (first posted 14 May 2026), prove the general generating-set description of a fixed quotient fiber, introduce its relative rank, and classify rank-one elements. Their general theorem and the earlier 2024 study of multiples provide the terminology and broad structural framework. The present specialization to quotient \(2\) over the ordinary semigroups \(O_m\) computes the **entire** fiber at all relative ranks as Boolean layers and determines a closed bivariate genus–rank counting function, an exact stabilization threshold, and the full parametrization. The general generating-set criterion does not itself state these enumerative formulas. Its rank-one results account for the \(r=1\) stratum; this known stratum is not independently claimed as new.

Ojeda and Rosales, *The multiples of a numerical semigroup*, arXiv:2402.04413v1 (2024), establish maximal-member and rooted-tree descriptions and general structural and rank properties, but do not state this Boolean normal form or its genus–rank distribution. Strazzanti, *Minimal genus of a multiple and Frobenius number of a quotient of a numerical semigroup* (2015), already gives the minimum genus across general doubles, so the value \(g_0\) is prior knowledge; our result adds the uniqueness statement and, principally, all-genus counts refined by relative rank. Work on genus distributions under quotients studies invariants of individual input semigroups rather than counting this full fiber. These comparisons are not a guarantee of historical priority: an equivalent enumeration may have appeared under different terminology.

## Limitations
The classification relies on both the ordinary gap pattern and the parity simplification for divisor two. It does not extend without further constraints to nonordinary targets or divisors greater than two. The relative-rank distribution is not a classification by ordinary embedding dimension, and the formula gives counts of numerical semigroups as subsets of \(\mathbb N_0\), not isomorphism classes of associated semigroup rings. Literature searches and inspection cannot rule out an older unindexed equivalent result. No independent mathematical audit has been conducted.

## References
1. I. Ojeda and J. C. Rosales, *On Numerical Semigroups with Fixed Quotient*, arXiv:2605.14775v1, 14 May 2026, https://arxiv.org/abs/2605.14775 .
2. I. Ojeda and J. C. Rosales, *The multiples of a numerical semigroup*, Turkish Journal of Mathematics 48 (2024), 1055–1066; arXiv:2402.04413v1, https://arxiv.org/abs/2402.04413 .
3. A. Adeniran et al., *On the genus of a quotient of a numerical semigroup*, Semigroup Forum 98 (2019), 690–700, https://doi.org/10.1007/s00233-018-9989-3 .
4. F. Strazzanti, *Minimal genus of a multiple and Frobenius number of a quotient of a numerical semigroup*, International Journal of Algebra and Computation 25 (2015), 1043–1053, https://doi.org/10.1142/S0218196715500290 .
