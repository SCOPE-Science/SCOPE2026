# Three hidden-entropy classes for binary tree shifts with one forbidden star

## Finding

**Theorem.** Label the vertices of an infinite complete rooted *ordered* binary tree by \(0\) and \(1\). Fix exactly one forbidden star \(v=(v_0,v_L,v_R)\in\{0,1\}^3\): no vertex may have parent/left-child/right-child labels equal to \(v\). Let \(S_n(v)\) count admissible labelings of the complete subtree with \(n\) levels, including its root, and put
\[
\alpha(v)=\lim_{n\to\infty}2^{-n}\log S_n(v).
\]
All eight one-star prohibitions have topological entropy \(\log 2\) in the double-logarithmic tree-shift convention, but their strictly positive hidden entropies take **exactly three distinct values**. The three counting classes, specified by representatives and their images under global symbol complementation and simultaneous left/right child exchange, are
\[
\begin{array}{c|c|c|c}
\text{class}&\text{representative}&\text{patterns}&S_3\\\hline
M&111&\{111,000\}&89\\
P&001&\{001,010,101,110\}&86\\
F&011&\{011,100\}&82.
\end{array}
\]
Here the displayed symmetries preserve the number of admissible rooted blocks; no topological conjugacy preserving separately named child-shift actions is asserted.

Write \(p_{M,1}=p_{P,1}=p_{F,1}=1/2\). For every \(n\ge1\), recursively define
\[
\begin{array}{c|c|c}
i&q_i(p)&f_i(p)\\\hline
M&2-p^2&(1-p^2)/(2-p^2)\\
P&2-p(1-p)&1/(2-p(1-p))\\
F&2-p^2&1/(2-p^2)
\end{array},
\qquad p_{i,n+1}=f_i(p_{i,n}).
\]
Then the three hidden entropies have absolutely convergent, effective expressions
\[
\boxed{\displaystyle
\alpha_i=\frac{\log2}{2}+\sum_{j=1}^{\infty}2^{-j-1}\log q_i(p_{i,j})
}\qquad(i\in\{M,P,F\}),
\]
with the **strict ordering**
\[
\boxed{\alpha_M>\alpha_P>\alpha_F>0.}
\]
The values are approximately \(0.634567276475\), \(0.627092951428\), and \(0.612234028416\), respectively. If the sum is truncated after terms \(j<N\), the discarded positive tail is less than \((\log2)2^{-N}\), independently of the class.

There is also a sharp multiplicative finite-height asymptotic. Let \(p_i^*\) be the unique fixed point of \(f_i\) in the intervals described below. Then
\[
\boxed{\displaystyle S_n(i)=\frac{1}{q_i(p_i^*)}\exp(\alpha_i2^n)
\left(1+O\bigl((27/49)^n\bigr)\right).}
\]
The prefactors \(1/q_i(p_i^*)\) are approximately \(0.554958132087\), \(0.569840290998\), and \(0.618033988750\). The fixed points are, respectively, the unique roots in the stated intervals of
\[
\begin{aligned}
&p^3-p^2-2p+1=0 &&(M),\\
&p^3-p^2+2p-1=0 &&(P),\\
&p^2+p-1=0 &&(F).
\end{aligned}
\]
In particular \(p_F^*=(\sqrt5-1)/2\). The complete finite-level count sequences satisfy \(S_n(M)>S_n(P)>S_n(F)\) for all \(n\ge3\).

## Assumptions and scope

A rooted \(n\)-block consists of exactly the vertices at depths \(0,1,\ldots,n-1\), hence \(2^n-1\) vertices. A forbidden star is tested only at vertices having both children within this block. The root and two child positions are distinguished. The count \(S_n(v)\) equals the number of length-\(n\) blocks appearing in the infinite tree shift: every locally admissible finite block extends to an infinite one. Indeed, for representatives \(111\), \(001\), \(011\), appending zeros below every leaf never creates the forbidden star, and complementing the labels handles their complementary patterns. Child exchange handles the remaining representatives. Thus no finite-level recurrence counts spurious nonextendible patterns.

The hidden entropy normalization is \(2^{-n}\log S_n\), not the logarithm per number \(2^n-1\) of vertices (the two have the same limit). The coarser topological entropy uses \(\lim_{n\to\infty}n^{-1}\log\log S_n\). All logarithms are natural. The theorem concerns exactly one excluded height-two star; it does not classify arbitrary sets of forbidden stars or claim that all eight shifts are conjugate.

## Proof

**Exact counting recurrences.** Let \(A_n\) and \(B_n\) be counts of admissible \(n\)-blocks whose root is \(0\) and \(1\), respectively, and write \(S_n=A_n+B_n\), \(p_n=B_n/S_n\). Initially \(A_1=B_1=1\). For any root label, the two child subtrees can be chosen independently, giving \(S_n^2\) possibilities, except for the single ordered pair of forbidden child-root labels. Therefore, with \(S=A_n+B_n\), the three representatives satisfy
\[
\begin{array}{c|cc}
&i\text{-class }A_{n+1}&i\text{-class }B_{n+1}\\\hline
M&S^2&S^2-B_n^2\\
P&S^2-A_nB_n&S^2\\
F&S^2-B_n^2&S^2.
\end{array}
\]
Equivalently \(S_{n+1}=S_n^2q_i(p_n)\) and \(p_{n+1}=f_i(p_n)\), exactly as stated. The first two levels have \(S_1=2\), \(S_2=7\) in all classes. The third has \(89\), \(86\), \(82\) patterns in classes \(M,P,F\), respectively. Complementation and left/right interchange generate the listed orbits of forbidden words; the distinct third-level totals prove there are no additional block-count coincidences among these classes.

**Invariant intervals and attraction.** After the first update, the three proportions equal \(3/7,4/7,4/7\). Direct rational endpoint substitution shows that the following intervals are forward invariant under the corresponding \(f_i\):
\[
I_M=[3/7,40/89],\qquad I_P=[9/16,4/7],\qquad I_F=[4/7,2/3].
\]
For \(p\) in these respective intervals,
\[
|f'_M(p)|\le16/49,\qquad |f'_P(p)|\le16/147,\qquad
|f'_F(p)|\le27/49.
\]
The first two derivative bounds follow from \(f'_M(p)=-2p/(2-p^2)^2\) and \(f'_P(p)=(1-2p)/(2-p(1-p))^2\). The third follows from \(f'_F(p)=2p/(2-p^2)^2\). Each is a strict contraction on its compact invariant interval, so it has a unique fixed point there, and
\[
|p_{i,n}-p_i^*|\le C_i(27/49)^n.
\]
Substitution in the three fixed-point equations gives the asserted polynomials. For \(F\), the root in \(I_F\) equals \((\sqrt5-1)/2\).

**Effective hidden entropy and its strict classification.** Taking logarithms of \(S_{n+1}=S_n^2q_i(p_n)\) and telescoping gives, for every \(n\ge1\),
\[
2^{-n}\log S_n=\frac{\log2}{2}
+\sum_{j=1}^{n-1}2^{-j-1}\log q_i(p_{i,j}).
\]
Since \(1<q_i(p)<2\) along all these orbits, the series converges absolutely and its omitted terms have positive sum less than \((\log2)2^{-N}\) after \(j<N\). In particular, \(\alpha_i>0\), and the double-logarithmic entropy is \(\log2\).

For all \(j\ge2\), the invariant intervals give
\[
(p_{M,j})^2\le(40/89)^2
<12/49\le p_{P,j}(1-p_{P,j})\le1/4
<(4/7)^2\le(p_{F,j})^2.
\]
Consequently \(q_M(p_{M,j})>q_P(p_{P,j})>q_F(p_{F,j})\) for every \(j\ge2\). The \(j=1\) factors all equal \(7/4\). Thus every later contribution in the series is strictly ordered. This proves \(\alpha_M>\alpha_P>\alpha_F\), and the same recursion, with common \(S_2\), proves \(S_n(M)>S_n(P)>S_n(F)\) for every \(n\ge3\). No floating-point comparison is used for these strict inequalities.

**Sharp prefactor.** The exact tail identity is
\[
\alpha_i2^n-\log S_n
=\sum_{k=0}^{\infty}2^{-k-1}\log q_i(p_{i,n+k}).
\]
Each \(\log q_i\) is Lipschitz on its invariant interval. By the contraction estimates, the right-hand side equals
\[
\log q_i(p_i^*)+O((27/49)^n).
\]
Exponentiating yields \(S_n(i)=q_i(p_i^*)^{-1}e^{\alpha_i2^n}(1+O((27/49)^n))\) with a constant independent of \(n\) for each fixed class. This also yields \(S_{n+1}/S_n^2\to q_i(p_i^*)\).

## Verification

The included Python 3 program `verify.py` uses no external packages. Run `python3 verify.py` from the directory containing it. It independently enumerates all binary labelings on three representative rooted trees through four levels, evaluates the recurrence, checks all eight forbidden-star symmetry classes at level three, verifies contraction-interval endpoint inclusions using exact rational arithmetic, and compares the finite-level ordering through eight levels. It then evaluates the defining series and fixed points using 75-digit decimal arithmetic; the mathematical tail bound gives a universal, certified **truncation** error smaller than \((\log2)2^{-50}\) when terms \(j<50\) are retained. Decimal rounding error is not a formally certified interval enclosure; the printed decimal digits are approximations, not a basis for proving the strict classification.

The executed program returned `VERIFY_OK: 54 exact finite-enumeration, symmetry, interval, and high-precision assertions`. Representative printed hidden-entropy approximations were \(0.634567276474948\), \(0.627092951428398\), and \(0.612234028416001\). The all-height mathematical proof consists of the exact recursion, interval contraction, and ordered infinite series, not finite brute-force enumeration.

## Relationship to prior work

Ban and Chang introduce tree-shifts, nonlinear recursion counting, and the hidden-entropy normalization; their 2015 manuscript (arXiv:1509.08325, Sections 1–2 and Section 5) establishes coarse entropy \(0\) or \(\log2\) for binary two-symbol Markov tree shifts, and explicitly poses computing hidden entropy even in this low-dimensional setting. Those general foundations and the \(\log2\) conclusion are not claimed as new. Their 2017 follow-up (arXiv:1705.03138, Section 2) again treats the broad problem of hidden entropy as unresolved in general. Petersen and Salama (arXiv:1909.05153, Sections 2–5) study entropy normalization and approximation methods for tree shifts, particularly nearest-neighbor golden-mean restrictions. That framework gives general context, but its inspected statements do not give the three single-forbidden-star constants or their strict comparison.

The claim here is restricted to the natural *complete one-exclusion census* of all eight height-two binary stars, with strict hidden-entropy ordering and an explicit finite-height prefactor. It is a specialization of established nonlinear-recursion methodology, so earlier implicit computations or unindexed exact evaluations remain possible; this is not an independently certified priority claim.

## Limitations

The classification is about the *number of rooted blocks*, not a classification up to conjugacy of the two labeled child-shift actions. The strictly ordered entropy constants are given by convergent iterative series, not proved to have elementary closed forms. The finite prefactor is derived for the one-star rules only; general finite forbidden sets can have other dynamical and combinatorial behavior. Numerical decimals are supplementary and do not certify transcendence or arithmetic independence of the constants. The literature comparison does not exclude all historical implicit derivations.

## References

1. J.-C. Ban and C.-H. Chang, *Tree-Shifts: The Entropy of Tree-Shifts of Finite Type*, first public preprint 2015-09-28, arXiv:1509.08325, https://arxiv.org/abs/1509.08325.
2. J.-C. Ban and C.-H. Chang, *Characterization for Entropy of Shifts of Finite Type on Cayley Trees*, arXiv:1705.03138, https://arxiv.org/abs/1705.03138.
3. K. Petersen and I. Salama, *Entropy on Regular Trees*, arXiv:1909.05153, https://arxiv.org/abs/1909.05153.
4. N. Aubrun and M.-P. Béal, *Tree-shifts of finite type*, Theoretical Computer Science 459 (2012), 16–25, https://doi.org/10.1016/j.tcs.2012.07.020 (conjugacy and tree-shift background; only abstract and bibliographic record inspected).
