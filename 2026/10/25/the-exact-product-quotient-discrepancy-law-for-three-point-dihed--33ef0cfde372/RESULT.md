# The exact product--quotient discrepancy law for three-point dihedral subsets

## Finding

Let \(D_n=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle\), of order \(2n\), with \(n\ge3\). For each three-element subset \(A\subset D_n\), set \(\Delta(A)=|AA|-|AA^{-1}|\), where \(AA=\{xy:x,y\in A\}\) and \(AA^{-1}=\{xy^{-1}:x,y\in A\}\). Write \(C=\binom n3\), \(t=\gcd(n,2)\), and
\[
 B=\frac{n(n-t)}2-\frac{2n}{3}\mathbf 1_{3\mid n}.
\]
Here \(B\) is always an integer. The **complete** possible discrepancy values are \(-1,0,1,3\), with the following exact counts, organized by the number \(j\) of rotations in \(A\). Entries not displayed in a given row are zero.

| Regime | \(j\) | \(\#(\Delta=-1)\) | \(\#(\Delta=0)\) | \(\#(\Delta=1)\) | \(\#(\Delta=3)\) |
|---|---:|---:|---:|---:|---:|
| all \(n\) | 0 | 0 | \(C\) | 0 | 0 |
| all \(n\) | 3 | \(C-B\) | \(B\) | 0 | 0 |
| odd \(n\) | 1 | 0 | \(n(n-1)/2\) | \(n(n-1)\) | \(n(n-1)(n-3)/2\) |
| odd \(n\) | 2 | 0 | \(n(n-1)/2\) | \(n(n-1)\) | \(n(n-1)(n-3)/2\) |
| \(n\equiv2\pmod4\) | 1 | 0 | \(n(n-1)\) | \(n(n-2)\) | \(n(n-2)(n-3)/2\) |
| \(n\equiv0\pmod4\) | 1 | 0 | \(n^2\) | \(n(n-4)\) | \(n(n^2-5n+8)/2\) |
| even \(n\) | 2 | 0 | \(n^2/2\) | \(2n(n-2)\) | \(n(n-2)(n-4)/2\) |

Thus, under the uniform distribution on \(\binom{D_n}{3}\),
\[
 \lim_{n\to\infty}\Pr(\Delta>0)=\frac34,\qquad
 \lim_{n\to\infty}\Pr(\Delta=0)=\frac18,\qquad
 \lim_{n\to\infty}\Pr(\Delta<0)=\frac18.
\]
The exact table is stronger than a mere comparison of the numbers of product-dominant and quotient-dominant sets: it distinguishes the four actual discrepancy sizes and every rotation/reflection composition.

## Assumptions and scope

All products and quotients are **sets** of distinct group elements, not multisets. In particular \(AA^{-1}\) uses inverses only on the *second* factor, and product order matters. The three elements of \(A\) are distinct and unordered. The parameter \(n\) is arbitrary integer at least \(3\); no primality or large-\(n\) hypothesis is imposed. A rotation is an element \(r^a\); a reflection is an element \(r^b s\), with exponents in \(\mathbb Z/n\mathbb Z\).

## Proof

Represent \(r^a s^\varepsilon\) by \((a,\varepsilon)\), with product
\[
 (a,\varepsilon)(b,\delta)
 =(a+(-1)^\varepsilon b,\varepsilon+\delta\pmod2).
\]
A reflection is its own inverse; a rotation \(r^a\) has inverse \(r^{-a}\).

**Three reflections.** Since each reflection is an involution, \(xy^{-1}=xy\) for all choices of right-hand factor in \(A\). Hence \(AA^{-1}=AA\), giving exactly \(C\) balanced subsets.

**Three rotations.** Translate exponents so that their unordered set is \(\{0,u,v\}\) in the cyclic additive group. The six formal unordered sums are \(0,u,v,2u,u+v,2v\); the seven formal differences are \(0,\pm u,\pm v,\pm(u-v)\). Equalities among formal sums arise precisely from a three-term arithmetic progression \(2a=b+c\) among the three distinct elements, or from two distinct elements separated by the unique element of order two. The latter coincidence also identifies one opposing pair of formal differences and hence leaves the discrepancy unchanged. If there is no arithmetic progression, the difference set therefore has exactly one more element than the sumset. If there is a progression, the triple is centrally symmetric, and translating it to \(\{-d,0,d\}\) shows the sum and difference sets have equal sizes. This classification remains valid when an order-two separation is present, because the additional sum and difference collisions occur in parallel. Thus \(\Delta=0\) precisely for arithmetic-progression triples and \(\Delta=-1\) otherwise.

Count progressions by choosing their center \(a\) and nonzero step \(d\), excluding \(2d=0\); there are \(n(n-t)\) such ordered choices, where \(t=\gcd(n,2)\). A typical three-element progression has two presentations (reversing \(d\)), but a coset of the unique order-three subgroup, when \(3\mid n\), has six presentations. There are \(n/3\) such cosets; correcting for their four extra presentations yields \(B=n(n-t)/2-2n/3\,\mathbf1_{3\mid n}\), as claimed.

**One rotation and two reflections.** Write \(A=\{r^a,r^b s,r^c s\}\), \(b\ne c\), and introduce \(d=b-c\ne0\), \(t=2a\) in the cyclic group. After separate translations of rotation and reflection exponents, the rotation components of \(AA\) and \(AA^{-1}\) are respectively \(\{0,d,-d,t\}\) and \(\{0,d,-d\}\); their reflection components are \(\{0,d,t,t+d\}\) and \(\{t,t+d\}\). Consequently
\[
\Delta=\mathbf1_{\{t\notin\{0,d,-d\}\}}
     +|\{0,d,t,t+d\}|-2.
\]
When \(2d\ne0\), this equals \(0\) if \(t=0\), \(1\) if \(t=d\) or \(-d\), and \(3\) otherwise. When \(2d=0\), it equals \(0\) for \(t\in\{0,d\}\) and \(3\) otherwise.

**Two rotations and one reflection.** Write \(A=\{r^a,r^b,r^c s\}\), \(a\ne b\), let \(d=a-b\ne0\), \(t=2a\). The rotation components of \(AA\) and \(AA^{-1}\) translate to \(\{0,t,t-d,t-2d\}\) and \(\{0,d,-d\}\), while their reflection components translate to \(\{0,d,t,t-d\}\) and \(\{t,t-d\}\). Therefore
\[
\Delta=|\{0,t,t-d,t-2d\}|-|\{0,d,-d\}|
       +|\{0,d,t,t-d\}|-2.
\]
When \(2d\ne0\), this is \(0\) for \(t=d\), \(1\) for \(t=0\) or \(2d\), and \(3\) otherwise. When \(2d=0\), it is \(0\) for \(t=0\) or \(d\), and \(3\) otherwise.

**Counting the mixed types.** For odd \(n\), the map \(a\mapsto2a\) is a bijection, and all nonzero \(d\) have \(2d\ne0\). Thus for each \(d\), the numbers of \(a\) giving \(\Delta=0,1,3\) are respectively \(1,2,n-3\), for either mixed type. There are \(n\) choices of the remaining reflection position and each unordered same-type pair is represented twice: multiply by \(n(n-1)/2\).

For even \(n\), \(t=2a\) runs through the even residue classes, each twice. There are \(n/2\) odd nonzero \(d\) and \(n/2-1\) even nonzero \(d\). The single involution \(d=n/2\) is odd precisely when \(n\equiv2\pmod4\). For the one-rotation case, the per-\(d\) count vectors \((\#\Delta_0,\#\Delta_1,\#\Delta_3)\), counted over \(a\), are:

| \(d\) type | Vector |
|---|---|
| odd | \((2,0,n-2)\) |
| even, not involution | \((2,4,n-6)\) |
| even involution | \((4,0,n-4)\) |

For the two-rotation case the corresponding vectors are:

| \(d\) type | Vector |
|---|---|
| odd, not involution | \((0,4,n-4)\) |
| odd involution | \((2,0,n-2)\) |
| even, not involution | \((2,4,n-6)\) |
| even involution | \((4,0,n-4)\) |

These vectors apply only to types possible at the given \(n\): in particular the even-non-involution row requires \(n\ge6\). Multiply the sum of vectors over all nonzero \(d\) by \(n/2\), for the remaining reflection translation and unordered same-type pair. This gives exactly the displayed even-\(n\) formulas, including both congruence classes modulo four. Every formula sums to \(n\binom n2\) in each mixed row; the four rows together sum to \(\binom{2n}{3}\).

Finally, the mixed rows contribute \(n^3+O(n^2)\) positive-discrepancy subsets; the all-rotations row contributes \(n^3/6+O(n^2)\) negative-discrepancy subsets; the all-reflections row contributes \(n^3/6+O(n^2)\) balanced subsets, while remaining balance counts are \(O(n^2)\). Since \(\binom{2n}{3}=4n^3/3+O(n^2)\), division gives the three limits. This proves the theorem.

## Verification

The accompanying independent standard-library program `dihedral_three_verifier.py` enumerates all unordered three-element subsets of \(D_n\), directly forms both group product sets, and compares the complete discrepancy-frequency table with the closed formulas for every integer \(3\le n\le36\). The command `python dihedral_three_verifier.py` printed `VERIFY_OK n=3..36`. These exhaustive **finite** checks verify arithmetic and normalization only; the proof above, not finite testing, establishes the theorem for unbounded \(n\).

## Relationship to prior work

Amit and collaborators, *Product and Quotient Set Dominance in Finite Groups* (arXiv:2610.12912, first version 2026-10-09), investigate product/quotient dominance for random group subsets, including dihedral groups. Their probabilistic framework motivates resolving a fixed-small-cardinality distribution at exact discrepancy levels. Ascoli and collaborators, *Sum and Difference Sets in Generalized Dihedral Groups* (arXiv:2210.00669, 2022), Appendix A, Lemma 2.2, prove a comparison between the number of product-dominant and quotient-dominant three-subsets and discuss rotation/reflection cases; they do not state this complete four-valued discrepancy table or its asymptotic mass decomposition. Earlier work by Haviland and collaborators, *More Sums Than Differences Sets in Finite Non-Abelian Groups* (2020 slides), addresses broader dominance and expectations. Mandal and Neetu, *Exact and Asymptotic Counts of MSTD, MDTS, and Balanced Sets in Dicyclic Groups* (arXiv:2602.09073, 2026), give formulas for the distinct dicyclic family. These comparisons are by mathematical statement, not by title alone. Existing formulas may imply pieces of the table after supplementary derivation; the claimed contribution is the full discrepancy classification and all-\(n\) table together.

## Limitations

This is an exact theorem only for cardinality-three subsets of ordinary cyclic dihedral groups; no analogous claim is made for larger subsets, generalized dihedral kernels, or dicyclic groups. The asymptotic concerns a uniformly sampled three-subset, not a random subset of unrestricted size. As with any literature search, unindexed or inaccessible previous treatments may contain equivalent classifications. Review of scientific originality is not independent.

## References

1. Yuval Amit and collaborators, *Product and Quotient Set Dominance in Finite Groups*, arXiv:2610.12912 (v1, 2026-10-09), https://arxiv.org/abs/2610.12912.
2. Ruben Ascoli and collaborators, *Sum and Difference Sets in Generalized Dihedral Groups*, arXiv:2210.00669 (2022), https://arxiv.org/abs/2210.00669.
3. John Haviland and collaborators, *More Sums Than Differences Sets in Finite Non-Abelian Groups*, conference slides (2020), https://jackhaviland.com/math/slides/mstd_finite_nonabelian.pdf.
4. Sagar Mandal and Neetu, *Exact and Asymptotic Counts of MSTD, MDTS, and Balanced Sets in Dicyclic Groups*, arXiv:2602.09073 (2026), https://arxiv.org/abs/2602.09073.
