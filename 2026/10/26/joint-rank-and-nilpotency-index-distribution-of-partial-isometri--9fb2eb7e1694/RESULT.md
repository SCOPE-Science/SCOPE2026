# Joint rank and nilpotency-index distribution of partial isometries of a finite chain

## Finding

For every integer \(n\ge1\), let \(X_n=\{1,\ldots,n\}\) with its ordinary distance, and let \(\mathcal{DP}_n\) be the monoid of all distance-preserving partial injections \(f:X_n\rightharpoonup X_n\), including the empty map \(0\). The rank is \(\rho(f)=|\operatorname{dom}f|\); for a nilpotent map define \(\nu(f)=\min\{k\ge1:f^k=0\}\), so \(\nu(0)=1\). For \(k\ge1\), set
\[
H_{n,k}(t)=\sum_{\substack{f\in\mathcal{DP}_n\\f\text{ nilpotent},\,\nu(f)\le k}}t^{\rho(f)}.
\]

For \(k\ge2\), define the binary-run polynomial \(B_{L,k}(t)\) by \(B_{L,k}(t)=\sum t^{\#\text{ selected}}\), summing over subsets of an ordered \(L\)-element chain containing no run of \(k\) consecutive selected positions. Its recurrence is specified in the proof. Set
\[
L_c=\min\{c-1,2n+1-c\},\qquad m_c=\lfloor L_c/2\rfloor\quad(2\le c\le2n).
\]
The complete joint rank and nilpotency-index distribution is the coefficientwise identity
\[
\boxed{H_{n,1}(t)=1,\quad H_{n,k}(t)=1+2\sum_{d=1}^{n-1}\left[\prod_{j=1}^{d}B_{\lfloor(n-j)/d\rfloor,k}(t)-1\right]+\sum_{c=2}^{2n}\left[(1+2t)^{m_c}-1\right]-n(n-1)t\quad(k\ge2).}
\]
In particular, the number with rank \(r\) and **exact** nilpotency index \(k\) is \([t^r](H_{n,k}(t)-H_{n,k-1}(t))\) for \(k\ge2\), with one empty map at \((r,k)=(0,1)\).

Put \(h=\lfloor n/2\rfloor\), and \(\delta_n=1\) for even \(n\) and \(\delta_n=3\) for odd \(n\). The rank counts \(M_{n,r}=\#\{f\in\mathcal{DP}_n:f\text{ nilpotent},\rho(f)=r\}\) satisfy
\[
\boxed{M_{n,0}=1,\quad M_{n,1}=n(n-1),\quad M_{n,r}=2\binom n{r+1}+2^r\left(4\binom h{r+1}+\delta_n\binom h r\right)\quad(r\ge2),}
\]
with binomial coefficients zero outside their usual ranges. The total is
\[
\boxed{\#\operatorname{Nil}(\mathcal{DP}_n)=2^{n+1}-n^2-3n-4+\begin{cases}3^{n/2+1},&n\text{ even},\\5\cdot3^{(n-1)/2},&n\text{ odd}.\end{cases}}
\]
Consequently the asymptotic proportion of nilpotent elements in the entire monoid is \(1/3\), using the known order of \(\mathcal{DP}_n\). For \(n\ge2\), exactly two elements have nilpotency index \(n\); for \(n\ge4\), exactly four have index \(n-1\).

## Assumptions and scope

The distance on \(X_n\) is the ordinary absolute difference \(|x-y|\), **not** the graph distance on a cycle. A partial isometry is an injective map defined on an arbitrary subset of \(X_n\), not necessarily on an interval. Composition of partial maps uses the usual partial-map convention. All assertions are exact for arbitrary positive integers \(n\). The transfer polynomial uses \(k\ge2\) and \(B_{0,k}(t)=1\); in the finite enumeration \(H_{n,k}\) stabilizes by \(k=n\). The zero map has index one.

## Proof

**1. Unique affine extension in rank at least two.** If \(f\) preserves pairwise distances and has two distinct domain points, the images of these points fix a sign \(\varepsilon\in\{+1,-1\}\) and intercept \(b\in\mathbb Z\) such that \(f(x)=\varepsilon x+b\) on the whole domain. Indeed each subsequent point lies on the integer line at prescribed distances from both marked points, forcing the same orientation. For rank at least two this affine extension is unique. A nonempty translation of offset zero is a partial identity and cannot be nilpotent. Translations with nonzero offset are nilpotent because every orbit is strictly monotone. Reflections have the form \(f(x)=c-x\). Rank-one maps, however, have both a translation and a reflection extension; these duplicates must be removed explicitly.

**2. Nonzero translations.** For a positive offset \(d\in\{1,\ldots,n-1\}\), the allowed source points are \(1,\ldots,n-d\), divided by residue classes \(j\in\{1,\ldots,d\}\) into progressions of lengths \(\lfloor(n-j)/d\rfloor\). Choosing the domain independently in each progression defines an isometry. Its nilpotency index is one plus the longest run of selected consecutive points on any progression. Consequently the polynomial counting such domain subsets with index at most \(k\) is \(\prod_{j=1}^d B_{\lfloor(n-j)/d\rfloor,k}(t)\). Excluding the empty domain subtracts one. Negative offsets contribute an equal count, giving the factor two. A direct finite recurrence for \(B_{L,k}\) is obtained from states \(a_j^{(m)}\), \(0\le j<k\), where \(a_j^{(m)}\) enumerates selected subsets in the first \(m\) positions with final selected-run length \(j\): initialize \(a_0^{(0)}=1\), all others zero; then
\[
a_0^{(m+1)}=\sum_{j=0}^{k-1}a_j^{(m)},\qquad a_j^{(m+1)}=t\,a_{j-1}^{(m)}\quad(1\le j<k),\qquad B_{L,k}=\sum_{j=0}^{k-1}a_j^{(L)}.
\]
These equations count all permitted binary words exactly, not only finite samples.

**3. Reflections.** An admissible reflection has some \(c\in\{2,\ldots,2n\}\) and acts by \(x\mapsto c-x\) on a chosen subset of its \(L_c\) admissible source positions. Those positions split into \(m_c\) two-point mirror pairs and at most one fixed midpoint. A reflected partial map is nilpotent exactly if its domain omits the fixed midpoint and contains at most one endpoint of each mirror pair: selecting the midpoint creates a fixed point, and selecting both endpoints creates a two-cycle; conversely, in their absence every orbit terminates after one application. Thus every nonzero nilpotent reflection has index two and its domain polynomial is \((1+2t)^{m_c}-1\). Any rank-one partial map \(x\mapsto y\) with \(x\ne y\) is counted once as a nonzero translation and once as a reflection. There are exactly \(n(n-1)\) such maps; no rank-two-or-higher duplication is possible by step 1. Subtracting \(n(n-1)t\), and restoring the unique empty map, proves the formula for \(H_{n,k}\).

**4. Closed rank formula.** At \(k=n\) the translation restrictions are unrestricted and \(B_{L,n}=(1+t)^L\), because \(L\le n-1\). For rank \(r\ge1\), their contribution is \(2\sum_{d=1}^{n-1}\binom{n-d}{r}=2\binom n{r+1}\). For a reflection, coefficient \(t^r\) is \(2^r\binom{m_c}{r}\). For even \(n=2h\), the positive pair-count levels \(1,\ldots,h-1\) each occur four times, and \(h\) occurs once. For odd \(n=2h+1\), those levels occur four times and \(h\) occurs three times. Therefore for \(r\ge1\), by the hockey-stick identity,
\[
\sum_{c=2}^{2n}\binom{m_c}{r}=4\binom h{r+1}+\delta_n\binom h r.
\]
Subtracting the rank-one duplication yields the displayed \(M_{n,r}\) (and the empty map supplies \(M_{n,0}=1\)).

**5. Total and asymptotics.** Summing the nonempty translation contribution at \(t=1\) gives \(2^{n+1}-2n-2\). The nonempty reflection contribution is \(3^{h+1}-2n-3\) in even degree, or \(5\cdot3^h-2n-3\) in odd degree. Subtracting \(n(n-1)\) rank-one duplicates and adding one empty map gives the claimed total. The published ambient-monoid count is \(|\mathcal{DP}_n|=3\cdot2^{n+1}-(n+2)^2-1\), so the quotient tends to \(1/3\); the remaining exponential error \(O(3^{n/2})\) is smaller than \(2^n\). For \(n\ge2\), an index-\(n\) map must be a nonzero translation supported on a run of \(n-1\) consecutive source points; only the two offsets \(\pm1\) permit this, with one choice each. For \(n\ge4\), analogous runs of length \(n-2\) can only occur with offsets \(\pm1\), with two choices per sign. Reflections have index at most two, so do not interfere.

## Verification

The accompanying standalone Python script `verify.py` directly enumerates all partial injections on \(n\le8\) points, independently filters by pairwise distance preservation and nilpotence, and obtains the rank and exact-index distribution from actual partial-map iteration. It then independently evaluates the transfer recurrence and checks every coefficient. In a separate algebraic check, it validates the closed rank and total formulas for all \(1\le n\le100\). The observed nilpotent totals for \(n=1,\ldots,8\) are \(1,3,9,27,65,151,317,663\); the program prints `VERIFY_OK_CHAIN_PARTIAL_ISOMETRY_RANK_INDEX`. These finite tests corroborate but do not substitute for the preceding all-\(n\) argument.

## Relationship to prior work

Kehinde and Umar's 2010 preprint, subsequently published with Al-Kharousi, develops the chain partial-isometry semigroup, affine-orientation structure, Green relations and algebraic properties. Al-Kharousi, Kehinde and Umar (2014), Proposition 2.14 and Theorem 2.15, give rank enumerations and the ambient order; their Proposition 2.17 treats fixed points. Those results are inputs and are not claimed here as new. In particular, *zero fixed points does not imply nilpotence*: restricting a reflection to a full mirror pair creates a two-cycle with no fixed point. Neither a marginal rank count nor a fixed-point count determines the simultaneous distribution by nilpotency index. A later analysis of nilpotents in partial **contractions** treats a larger, different semigroup and selected height classes, not this full joint polynomial. Classical enumeration of nilpotents in the unrestricted symmetric inverse semigroup concerns another, much larger family of partial injections. The specific new claim assessed here is the closed entire nilpotent rank polynomial together with the run-transfer formula resolving each exact nilpotency index, not the established ambient-semigroup cardinality or chain-extension lemma.

## Limitations

The result is a complete count of **labeled** partial maps. It does not enumerate conjugacy or isomorphism classes, nilpotent-generated subsemigroups, or partial isometries of cycles or arbitrary metric spaces. It relies on the one-dimensional affine extension property. Independent validation and exhaustive historical-priority verification have not been performed; an implicit equivalent enumerator in uninspected older literature remains possible.

## References

1. R. Kehinde and A. Umar, *On the semigroup of partial isometries of a finite chain*, arXiv:1101.0049v1, first public 2010-12-30, https://arxiv.org/abs/1101.0049.
2. F. Al-Kharousi, R. Kehinde and A. Umar, *Combinatorial results for certain semigroups of partial isometries of a finite chain*, Australasian Journal of Combinatorics **58** (2014), 365–375, https://ajc.maths.uq.edu.au/pdf/58/ajc_v58_p365.pdf.
3. M. M. Zubairu and B. Ali, *On the nilpotents of the semigroup of partial contractions of a finite chain*, International Journal of Mathematical Analysis and Modelling **7** (2024), https://journal.tnsmb.org/index.php/ijmam/article/view/158.
4. A. Umar, *On the Number of Nilpotents in the Partial Symmetric Semigroup*, 2004 (comparison of objects: unrestricted partial injections).
