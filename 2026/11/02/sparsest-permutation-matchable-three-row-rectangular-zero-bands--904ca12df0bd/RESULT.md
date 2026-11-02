# Sparsest permutation-matchable three-row rectangular zero bands

## Finding
For every integer \(q\ge1\), the smallest number of nonzero idempotents in a regular rectangular zero band with three labeled row classes and \(q\) labeled column classes **admitting a permutation matching** is
\[
m(q)=\begin{cases}q,&q\equiv0\pmod3,\\q+2,&q\equiv1,2\pmod3.\end{cases}
\]
Here “permutation matching” means a permutation of the nonzero regular class carrying each element to an inverse in the semigroup sense. Let \(N(q)\) be the number of admissible **labeled** structure supports attaining this minimum. Writing \(q=3k+r\), \(0\le r<3\), one has
\[
N(q)=\begin{cases}
\dfrac{q!}{(k!)^3},&r=0,\\[4pt]
\dfrac{q(3k)!}{(k!)^3}+\dfrac{3q(q-1)(3k-1)!}{(k-1)!(k!)^2},&r=1,\ k\ge1,\\[4pt]
1,&q=1,\\[4pt]
\dfrac{3q(q-1)(3k)!}{(k!)^3},&r=2.
\end{cases}
\]
There is a complete structural characterization of all minimizers, given in the proof.

## Assumptions and scope
Fix \(q\ge1\). Let \(R\) be a \(3\times q\) binary matrix, with row labels \(\{1,2,3\}\) and column labels \(\{1,\ldots,q\}\). Define \(B_R=\{0\}\cup(\{1,2,3\}\times\{1,\ldots,q\})\), with zero absorbing and
\[
(i,j)(h,\ell)=\begin{cases}(i,\ell),&R_{hj}=1,\\0,&R_{hj}=0.\end{cases}
\]
The nonzero element \((i,j)\) is idempotent if and only if \(R_{ij}=1\). We require the nonzero class to be regular; the balanced condition below implies that \(R\) has neither an all-zero row nor an all-zero column. The enumeration is of binary matrices in the given labeled coordinates, **not** semigroup isomorphism classes.

By the balanced-weighting permutation-matching theorem of Higgins [1], the nonzero regular \(\mathcal D\)-class has a permutation matching if and only if its support admits a nonnegative weighting with equal row sums and equal column sums. Equivalently, for every subset \(X\subseteq\{1,2,3\}\),
\[
q|X|\le3|\Gamma(X)|,
\]
where \(\Gamma(X)\) is the set of columns meeting at least one row in \(X\). This is the only external implication used in the counting proof.

## Proof
Put \(q=3k+r\) with \(r\in\{0,1,2\}\). Each nonzero column has a support among the seven nonempty subsets of \(\{1,2,3\}\). Let \(a_i\) be the number of columns supported **only** at row \(i\), and \(d_i\) the number of columns containing row \(i\). The weighted Hall conditions for the three singleton subsets \(\{i\}\) and three two-row subsets \(\{1,2,3\}\setminus\{i\}\) are exactly
\[
d_i\ge\lceil q/3\rceil,\qquad a_i\le\lfloor q/3\rfloor=k\quad(i=1,2,3).
\]
The empty and full row subsets contribute only trivial conditions because all columns are nonempty. Thus these six inequalities completely characterize matching-admissibility among nonzero-column supports.

Let \(e=\sum_i d_i\) count all nonzero entries. Since every column is nonempty, \(e\ge q\). If \(r=0\), equality is attained only by singleton columns; the row-degree conditions force exactly \(k\) columns of each singleton type. They satisfy all six inequalities, giving \(m(q)=q\) and \(N(q)=q!/(k!)^3\).

Suppose \(r=1\). The three degree inequalities give \(e\ge3(k+1)=q+2\). Equality forces \(d_1=d_2=d_3=k+1\), and since \(e-q=2\), either (A) one column contains all three rows and all others are singletons, or (B) precisely two columns have support size two and all other columns are singletons. In case (A), there are \(k\) singleton columns of each row. There are \(q(3k)!/(k!)^3\) labeled matrices. In case (B), the two double supports cannot coincide: otherwise the omitted row would have \(k+1\) singletons, contradicting \(a_i\le k\). Thus the two double columns have distinct supports and share exactly one row. Their shared row has \(k-1\) singleton columns and the other two rows have \(k\) each. Such matrices exist only for \(k\ge1\) and number
\[
3q(q-1)\frac{(3k-1)!}{(k-1)!(k!)^2}.
\]
All meet the six inequalities, so they exhaust and attain the minimum. For \(q=1\), only (A) occurs.

Suppose \(r=2\). The row degrees initially give \(e\ge3(k+1)=q+1\). If equality held, there would be exactly one double-support column and all remaining columns singletons. The row missing from this double support would then have \(k+1\) singleton columns, violating \(a_i\le k\). Thus \(e\ge q+2\). At equality, either there is one triple-support column or there are two double-support columns. The first case is impossible: it leaves \(3k+1\) singleton columns but their total permitted count is at most \(3k\). For the second case, the same bound forces exactly \(k\) singleton columns for each row. The two double columns must have distinct two-element supports (identical double supports would yield degree \(k\) at the excluded row). Hence the two double supports meet in one row, giving row degrees \(k+2,k+1,k+1\); all Hall inequalities hold. Choose their shared row in three ways, their ordered labeled columns in \(q(q-1)\) ways, and distribute singleton labels in \((3k)!/(k!)^3\) ways. This yields the formula for \(N(q)\) and shows attainability of \(m(q)=q+2\).

The above alternatives are mutually exclusive and exhaust all equality cases. Every asserted count follows by labeled multinomial enumeration; no division by automorphism groups is used.

## Verification
The included standalone program `verify.py` independently enumerates all seven nonempty column-support types as multisets and assigns each multiset its full multinomial number of labeled column placements. It implements the seven weighted Hall inequalities directly for every \(q\) from \(1\) through \(10\) and compares both minimal edge count and full minimizing labeled count with the formulas. The run printed `ALL_CHECKS_PASSED`; the recorded counts were \(1,6,6,96,360,90,4410,15120,1680,168000\). These finite computations corroborate, but do not replace, the arbitrary-\(q\) proof.

## Relationship to prior work
Higgins [1], publicly posted October 1, 2026, proves the balanced-weighting criterion for permutation matchings and applies it to order-preserving maps. That criterion is used as an established theorem; neither its proof nor the existence of balanced weightings is claimed new. Higgins [2] investigates matching involutions of finite transformation semigroups rather than the extremal number and labeled classification of idempotents in three-row rectangular zero bands. The present result gives the exact first nontrivial fixed-row sparsity threshold, all its equality structures, and every labeled multiplicity as \(q\) varies.

## Limitations
The classification concerns only three-row binary Rees matrices, although its column count is arbitrary. It does not enumerate isomorphism classes, nonbinary sandwich matrices, or general rectangular shapes. Older unindexed incidence-matrix enumerations could contain an equivalent result; no absolute claim of historical priority is made. The computational check covers finite \(q\), while the symbolic proof supplies the unrestricted theorem.

## References
[1] P. M. Higgins, *Balanced weightings and permutation matchings applied to the monoid of order-preserving mappings*, arXiv:2610.01912 (posted 2026-10-01), https://arxiv.org/abs/2610.01912 .

[2] P. M. Higgins, *Permutation matchings in finite semigroups*, Semigroup Forum (2024), DOI:10.1007/s00233-024-10430-0 .
