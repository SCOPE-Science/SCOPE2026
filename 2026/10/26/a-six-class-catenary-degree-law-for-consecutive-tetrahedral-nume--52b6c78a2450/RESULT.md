# A six-class catenary degree law for consecutive tetrahedral numerical semigroups

## Finding
For every integer \(n\ge4\), define \(t_j=\binom{j+2}{3}=j(j+1)(j+2)/6\) and the numerical semigroup
\[
S_n=\langle t_n,t_{n+1},t_{n+2},t_{n+3}\rangle.
\]
Its ordinary (not monotone) catenary degree is
\[
\boxed{\mathsf c(S_n)=
\begin{cases}
n+5,&n\equiv3,5\pmod6,\\
n+4,&n\equiv0\pmod6,\\
n+3,&n\equiv1,2,4\pmod6.
\end{cases}}
\]
The three-branch law is exact for all \(n\ge4\); it does not assert an unproved classification of all individual elementwise catenary degrees.

## Assumptions and scope
Write \(g_i=t_{n+i-1}\), for \(1\le i\le4\). The four generators are distinct and constitute a minimal generating system for \(n\ge4\), by Proposition 32 of Robles-Pérez and Rosales [1]. A factorization of \(s\in S_n\) is \(z=(z_1,z_2,z_3,z_4)\in\mathbb N^4\) with \(s=\sum_i z_i g_i\). For \(z,z'\), define \(z\wedge z'\) coordinatewise by minima, \(|z|=\sum_i z_i\), and
\[
d(z,z')=\max\{|z-z\wedge z'|,|z'-z\wedge z'|\}.
\]
A \(C\)-chain between two factorizations consists of factorization steps each of distance at most \(C\). The catenary degree \(\mathsf c(S_n)\) is the least \(C\) for which every pair of factorizations of every \(s\in S_n\) admits such a chain. We use the **complete minimal presentations** explicitly supplied in Proposition 33 of [1], and verify their arithmetic and applicability for the present generator ordering.

## Proof
Let \(e_1,\ldots,e_4\) denote the standard basis of \(\mathbb N^4\). A relation \(a\leftrightarrow b\) in a semigroup presentation transforms any factorization \(a+v\) to \(b+v\); its distance is \(d(a,b)\), independently of the common added vector \(v\). Any two factorizations of an element are joined by presentation moves. Consequently, the maximum of the lengths of both sides of all relations bounds \(\mathsf c(S_n)\) from above.

For transparency, the six complete presentations from [1, Proposition 33] are reproduced as identities of exponent vectors. In each row the three pairs separated by semicolons generate the entire factorization congruence:

| \(n\bmod6\) | Three presentation relations \(a\leftrightarrow b\) |
|---|---|
| 0 | \(\tfrac{n+2}{2}e_4\leftrightarrow2e_3+\tfrac{n+4}{2}e_2\); \((n+1)e_3\leftrightarrow(n+4)e_2\); \(\tfrac n3e_2\leftrightarrow\tfrac{n+3}3e_1\) |
| 1 | \(\tfrac{n+2}3e_4\leftrightarrow\tfrac{n+5}3e_3\); \(\tfrac{n+1}2e_3\leftrightarrow2e_2+\tfrac{n+3}2e_1\); \(ne_2\leftrightarrow(n+3)e_1\) |
| 2 | \(\tfrac{n+2}2e_4\leftrightarrow2e_3+\tfrac{n+4}2e_2\); \(\tfrac{n+1}3e_3\leftrightarrow\tfrac{n+4}3e_2\); \(ne_2\leftrightarrow(n+3)e_1\) |
| 3 | \((n+2)e_4\leftrightarrow(n+5)e_3\); \(\tfrac{n+1}2e_3\leftrightarrow2e_2+\tfrac{n+3}2e_1\); \(\tfrac n3e_2\leftrightarrow\tfrac{n+3}3e_1\) |
| 4 | \((n+3)e_1\leftrightarrow ne_2\); \(\tfrac{n+4}2e_2\leftrightarrow\tfrac{n-1}3e_3+\tfrac{n+2}6e_4\); \(\tfrac{n+5}3e_3\leftrightarrow\tfrac{n+2}3e_4\) |
| 5 | \(\tfrac{n+3}2e_1\leftrightarrow\tfrac{n-2}3e_2+\tfrac{n+1}6e_3\); \(\tfrac{n+4}3e_2\leftrightarrow\tfrac{n+1}3e_3\); \((n+5)e_3\leftrightarrow(n+2)e_4\) |

All coefficients are nonnegative integers in their indicated congruence classes for \(n\ge4\); directly substituting \(g_i=t_{n+i-1}\) verifies equality of weights on each side. Taking the largest side length in each row gives, respectively, \(n+4,n+3,n+3,n+5,n+3,n+5\), proving the claimed upper bounds.

We next prove they cannot be improved. Two elementary observations make the lower bounds rigorous. First, if for a factorization \(z=C e_i\) **no presentation side is supported on \(e_i\) with coefficient at most \(C-1\)**, then \((C-1)e_i\) is the unique factorization of its weight. Indeed, if there were a second one, completeness of the presentation would give a first move out of \((C-1)e_i\), impossible by the stated condition. If a factorization \(w\ne z\) of the weight of \(z\) had \(w_i>0\), subtracting \(e_i\) from both factorizations would contradict uniqueness. Hence \(z\) shares no positive coordinate with any distinct factorization of its weight. Each step starting at \(z\) must therefore have distance at least \(|z|=C\).

For \(n\equiv1,2,4\pmod6\), take \(z=(n+3)e_1\). Inspection of the appropriate presentation row shows no side supported only on \(e_1\) of smaller positive size. The other factorization \(ne_2\) exists, so \(\mathsf c(S_n)\ge n+3\).

For \(n\equiv3,5\pmod6\), take \(z=(n+2)e_4\). There is no presentation side supported only on \(e_4\) of size less than \(n+2\). Thus any other factorization \(w\) has \(w_4=0\). But the common weight is \((n+5)g_3\), and \(g_1<g_2<g_3\), so \(|w|g_3\ge(n+5)g_3\), whence \(|w|\ge n+5\). Its distance from \(z\) is therefore at least \(n+5\). The alternative factorization \((n+5)e_3\) exists, and \(\mathsf c(S_n)\ge n+5\).

For \(n\equiv0\pmod6\), set \(z=(n+1)e_3\) and \(w=(n+4)e_2\). In this fiber every factorization has fourth coordinate zero. To establish the latter fact without assuming a finite experiment, start with \(w\) and apply the complete presentation in the first row. The third relation changes only coordinates \(1,2\). The second relation exchanges \(w\) with \(z\), because it consumes all \(n+4\) units of \(e_2\) or all \(n+1\) units of \(e_3\). The first relation cannot be used: its \(e_4\) side is absent, while its other side needs *both* positive \(e_2\) and positive \(e_3\), which are never simultaneously available in the reached states. This set of states is closed under every relation, so presentation completeness implies it contains all factorizations of the common weight. Moreover, no presentation side supported only on \(e_3\) has fewer than \(n+1\) copies of \(e_3\). By the uniqueness argument above, \(z\) is disjoint from every other factorization. These others use only \(g_1,g_2\), with \(g_1<g_2\), and their common weight is \((n+4)g_2\). Therefore each has length at least \(n+4\), and every chain leaving \(z\) contains a step of distance at least \(n+4\).

The lower bounds match all six upper bounds, proving the formula for every \(n\ge4\).

## Verification
The standalone `verify.py` checks the six presentation identities, upper-bound relation lengths, and exact factorization fibers at every distinct presentation (Betti) weight for each of the 30 integers \(4\le n\le33\). It computes the exact least-bottleneck spanning-tree threshold of the complete factorization-distance graph, independently of the presentation upper bound. Across these 30 semigroups there are 88 distinct critical fibers; the maximum observed cardinality is 22. The program also verifies the four generators have greatest common divisor one. Run `python3 verify.py` with Python 3; no third-party packages are required. These finite checks test the argument but do not establish the theorem for unbounded \(n\).

## Relationship to prior work
Robles-Pérez and Rosales [1, Proposition 33 and Corollary 34] established the complete presentations and Betti elements of these **same tetrahedral semigroups**; those results are essential premises, not independent contributions of this note. Their treatment gives Frobenius, Apéry, and presentation data but does not state the exact catenary-degree law above. Chomicz [2] studied catenary degrees of four consecutive **square and triangular** semigroups, not tetrahedral ones. Süer and Sezgin [3] studied **three-generated** telescopic families. The contribution here is specifically the three-branch, six-class closed catenary formula, with a proof that the longest presentation trade is an unavoidable bottleneck in each class. The fact that the formula can be derived from [1] by an additional fiber analysis limits claims of conceptual independence.

## Limitations
This is the ordinary catenary degree for four *consecutive tetrahedral* generators and \(n\ge4\), not a result for nonconsecutive tuples, monotone/equal catenary degree, or every elementwise catenary degree. The presentation-completeness input is a previously published theorem [1]. Computational checks stop at \(n=33\). Mathematical priority remains subject to discovery of equivalent earlier consequences of general numerical-semigroup methods; no independent verification is claimed.

## References
[1] A. M. Robles-Pérez and J. C. Rosales, “The Frobenius number for sequences of triangular and tetrahedral numbers,” arXiv:1706.04378, first public 2017-06-14; especially Propositions 32–33 and Corollary 34. https://arxiv.org/abs/1706.04378

[2] K. Chomicz, “On numerical semigroups with embedding dimension four,” arXiv:2604.25653, first public 2026-04-28, sections on catenary degrees of four consecutive squares and triangular numbers. https://arxiv.org/abs/2604.25653

[3] M. Süer and M. Ş. Sezgin, “Betti elements and catenary degree of telescopic numerical semigroup families,” arXiv:2011.09548, first public 2020-11-18. https://arxiv.org/abs/2011.09548
