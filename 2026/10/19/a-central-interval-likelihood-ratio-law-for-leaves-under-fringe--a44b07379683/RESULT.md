# A central-interval likelihood-ratio law for leaves under fringe-occurrence bias in Catalan trees

## Finding

Let \(T_n\) be uniform on the \(C_{n-1}\) rooted ordered trees on \(n\) vertices, where \(C_a=\binom{2a}{a}/(a+1)\). Fix a rooted ordered tree \(\tau\) with \(k\ge2\) vertices and \(\ell\) leaves, and suppose \(n\ge k+1\). Write \(F_\tau(t)\) for the number of vertices whose entire descendant fringe subtree is isomorphic to \(\tau\), and \(L_n\) for the leaf count. The **fringe-occurrence Palm law** is

\[
\mathbb P_\tau(T_n=t)=\frac{F_\tau(t)}{\sum_{u\in\mathcal T_n}F_\tau(u)}.
\]

This weights **trees according to occurrence count**; it is not the law obtained by choosing an occurrence uniformly *within* a previously uniformly drawn tree.

Put \(m=n-k+1\ge2\). Under this law,

\[
L_n\overset{d}{=}\ell-1+L_m^*,\qquad
\mathbb P(L_m^*=j)=\frac{j\,\mathbb P(L_m=j)}{\mathbb EL_m}.
\]

Thus the Palm leaf law depends on the marked shape only through \(k\) and \(\ell\). Let \(p_n(r)=\mathbb P(L_n=r)\), \(q_{n,\tau}(r)=\mathbb P_\tau(L_n=r)\) and \(R(r)=q_{n,\tau}(r)/p_n(r)\) for \(1\le r\le n-1\), taking \(R(r)=0\) outside the Palm support. **The likelihood ratio \(R\) is log-concave, with strictly decreasing adjacent ratios wherever defined.** Therefore, for every \(c>0\), the set \(\{r:R(r)>c\}\) is an integer interval (possibly empty). In particular, an optimal Neyman–Pearson test based solely on \(L_n\) of the ordinary law against the occurrence-enriched law can select a contiguous interval, using boundary randomization when needed. If \(\ell\ge2\), the likelihood-ratio-above-one interval is nonempty and excludes both \(r=1\) and \(r=n-1\), where the Palm likelihood ratio is zero.

A complete finite-size dependence classification accompanies this likelihood law:

\[
\frac{\operatorname{Cov}(L_n,F_\tau)}{\mathbb EF_\tau}
=\ell-\frac{k+1}{2}+\frac{m-2}{2(2m-3)}.
\]

It is strictly negative for \(2\ell\le k\), strictly positive for \(2\ell>k+1\), and in the remaining possible case \(2\ell=k+1\), zero when \(m=2\) and strictly positive when \(m\ge3\). Thus the sign is shape-independent and nearly entirely controlled by whether leaves occupy more than half of the marked fringe tree.

## Assumptions and scope

All trees are unlabeled, rooted and ordered (their children have a fixed left-to-right ordering), of **vertex size** \(n\). A leaf has outdegree zero. Occurrences are complete rooted descendant subtrees, not arbitrary embedded motifs. For \(n\ge2\) the leaf count ranges over \(1,\ldots,n-1\). The principal theorem assumes \(k\ge2\) and \(n\ge k+1\); the exceptional \(n=k\) case has a deterministic Palm leaf count \(\ell\), with covariance divided by \(\mathbb EF_\tau\) equal to \(\ell-k/2\), and is not included in the two-tail interval assertion. The one-vertex tree has one leaf.

The Narayana enumeration gives, for \(a\ge2\),

\[
A_a(j)=\#\{t\in\mathcal T_a:L_a(t)=j\}
=\frac1{a-1}\binom{a-1}{j}\binom{a-1}{j-1},\quad 1\le j\le a-1.
\]

For \(a=1\), define \(A_1(1)=1\). These formulas fix all counting normalizations.

## Proof

**1. Mark-and-contract bijection.** Consider a pair \((t,v)\), with \(t\in\mathcal T_n\) and the complete descendant tree at \(v\) equal to \(\tau\). Replace that fringe tree by one marked leaf. The remaining plane tree has exactly \(m=n-k+1\) vertices; its designated vertex is a leaf. Conversely, expanding the designated leaf back to \(\tau\) restores a unique \((t,v)\), with child order preserved. Hence

\[
\sum_{t\in\mathcal T_n}F_\tau(t)=\sum_{u\in\mathcal T_m}L_m(u)
\]

and the leaf-count identity under the occurrence Palm law follows: expansion turns one old leaf into \(\ell\) leaves, increasing the total by \(\ell-1\). No extra automorphism factor arises for ordered tree shapes.

**2. Explicit likelihood ratio and strict adjacent-ratio decrease.** For \(m\ge2\), the Palm mass at \(r=j+\ell-1\) is

\[
q_{n,\tau}(r)=\frac{jA_m(j)}{\sum_a aA_m(a)},\quad 1\le j\le m-1.
\]

The ordinary mass is \(p_n(r)=A_n(r)/C_{n-1}\). All displayed denominators are positive. For \(1\le j\le m-2\), elementary cancellation of Narayana ratios yields

\[
\frac{R(j+\ell)}{R(j+\ell-1)}
=\frac{(m-j-1)(m-j)}{(m-j+k-\ell-1)(m-j+k-\ell)}\;
\frac{(j+\ell-1)(j+\ell)}{j^2}.
\tag{1}
\]

Set \(A=m-j\ge2\), \(s=\ell-1\ge0\), and \(t=k-\ell\ge1\). The first factor of (1) is

\[
\frac{A-1}{A+t-1}\frac{A}{A+t},
\]

strictly increasing with \(A\), hence strictly decreasing with \(j\). The second factor is

\[
\frac{(j+s)(j+s+1)}{j^2}
=1+\frac{2s+1}{j}+\frac{s(s+1)}{j^2},
\]

also strictly decreasing with \(j\). Thus their product is strictly decreasing with \(j\). The positive support is contiguous; extending by zero retains log-concavity at its two boundaries. This proves strict log-concavity for each interior positive triple, with the cases \(m=2\) and \(m=3\) automatic because their positive support has at most two values. Superlevel sets of any positive log-concave sequence are intervals.

The two laws are distinct because \(R(n-1)=0\), while the ordinary distribution gives positive mass there; normalization \(\sum_r p_n(r)R(r)=1\) therefore forces at least one \(R(r)>1\). If \(\ell\ge2\), the Palm support is \([\ell,\ell+m-2]\), lying strictly within \([1,n-1]\), so \(R(1)=R(n-1)=0\). The likelihood-ratio-above-one set is accordingly nonempty and central. The Neyman–Pearson rejection assertion follows by ranking observed leaf counts by \(R\) and randomizing only on cutoff ties; no assertion is made that a single deterministic interval realizes every desired exact test size.

**3. Exact covariance classification.** The Narayana mean and variance, valid for all \(m\ge2\), are

\[
\mathbb EL_m=\frac m2,\qquad
\operatorname{Var}(L_m)=\frac{m(m-2)}{4(2m-3)}.
\]

Therefore

\[
\mathbb E_\tau L_n=\ell-1+\frac{\mathbb E L_m^2}{\mathbb E L_m}
=\ell-1+\frac m2+\frac{m-2}{2(2m-3)}.
\]

Since \(\mathbb EL_n=n/2\) for \(n\ge2\), and since occurrence bias gives \(\mathbb E_\tau L_n-\mathbb E L_n=\operatorname{Cov}(L_n,F_\tau)/\mathbb EF_\tau\), the exact formula follows. The correction term is zero at \(m=2\) and strictly between zero and \(1/4\) for \(m\ge3\). Comparing integer \(2\ell\) with \(k\) and \(k+1\) gives every claimed sign. Finally, the marked-fringe mean is

\[
\mathbb EF_\tau=\frac{mC_{m-1}}{2C_{n-1}},\quad m\ge2.
\]

This is also the exact normalization used in the likelihood calculation.

## Verification

The standalone `verify.py` enumerates every rooted ordered tree of vertex sizes \(2\) through \(10\), and every fringe pattern size up to \(5\). It verifies the occurrence-weighted leaf histogram, the Narayana counts, the exact covariance regression, interval superlevel sets, and finite adjacent-ratio log-concavity. It also checks strict adjacent-ratio decrease using exact fractions across 232,286 parameter triples with \(2\le k<75\), \(1\le\ell<k\), and \(4\le m<90\). All checks passed. The finite tests support the theorem; the proof above establishes arbitrary admissible sizes.

## Relationship to prior work

The Catalan/Narayana leaf distribution and general enumeration of ordered-tree pattern occurrences are classical: Dershowitz–Zaks (1984/1989) treats general pattern occurrences and includes Narayana counts. In particular, the contraction-and-marking technique and elementary counting formula are **not** offered as novel independent discoveries. Janson (arXiv:1312.1211v1, 2013) gives asymptotic joint fringe-count covariances, including the leaf count as a one-vertex fringe tree; our covariance's leading asymptotic follows from his formulas, and is **not** claimed as new. Berzunza Ojeda–Holmgren–Janson (2025), especially their free-fringe-tree reduction in Section 3, provides a related general contraction framework. The assessed further result is the global **finite-sample log-concave Palm likelihood ratio**, its central-interval optimal testing consequence and the completely resolved finite-size sign boundaries.

The accessible 1984 full report, Janson's full original preprint, and the full 2025 primary article were compared at the corresponding statements and proofs. The 2009 Dershowitz–Zaks paper on further pattern/leaf enumerations was located but its full text was inaccessible, so hidden equivalence or a stronger earlier statement remains a material originality risk.

## Limitations

This is a statement about **occurrence-weighted** trees, not a tree sampled uniformly and then conditioned to contain at least one occurrence. It is not a claim of independence of leaf and pattern counts. The variance/covariance regression is exact, but no joint distribution of the complete count \(F_\tau\) is given. The inequality does not extend automatically to arbitrary nonplane tree models or nonuniform offspring weights. The mathematical literature comparison is best-knowledge, not an independently certified novelty determination; possible implicit coverage via general pattern enumeration and the unavailable 2009 full text remains.

## References

1. S. Janson, *Asymptotic normality of fringe subtrees and additive functionals in conditioned Galton–Watson trees*, arXiv:1312.1211v1, first public 4 December 2013, especially Corollary 1.8 and Example 2.1. https://arxiv.org/pdf/1312.1211
2. N. Dershowitz and S. Zaks, *Patterns in Trees*, MIT-LCS-TM-271, 1984 preprint; subsequent paper *Discrete Applied Mathematics* 25 (1989), 241–255. https://groups.csail.mit.edu/tds/papers/Zaks/TM-271.pdf
3. N. Dershowitz and S. Zaks, *More Patterns in Trees: Up and Down, Young and Old, Odd and Even*, *SIAM Journal on Discrete Mathematics* 23 (2009), 447–465, doi:10.1137/070687475 (abstract inspected; full text inaccessible).
4. G. Berzunza Ojeda, C. Holmgren, and S. Janson, *Fringe Trees for Random Trees With Given Vertex Degrees*, *Random Structures & Algorithms* 66 (2025), e70001, doi:10.1002/rsa.70001, Section 3. https://onlinelibrary.wiley.com/doi/full/10.1002/rsa.70001
