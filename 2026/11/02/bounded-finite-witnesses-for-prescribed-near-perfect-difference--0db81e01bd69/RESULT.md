# Bounded finite witnesses for prescribed near-perfect difference functions

## Finding
For a set \(A\subseteq\mathbb N=\{1,2,\ldots\}\), write \(d_A(t)=\#\{(a,b)\in A^2:a-b=t\}\) for positive \(t\). Fix a finite nonempty set \(S\subset\mathbb N\) and prescribed integers \(f(s)\ge2\) for \(s\in S\); prescribe \(f(t)=1\) for all \(t\notin S\). Set
\[
R=\sum_{s\in S}f(s),\quad M=\max S,\quad W=2RM,\quad H=4W+M+1,\quad B=H4^{2R}+W+1.
\]
There exists an infinite set \(A\subseteq\mathbb N\) with \(d_A(t)=f(t)\) for **every** positive integer \(t\) if and only if there is a set \(F\subseteq\{1,\ldots,B\}\) of at most \(2R\) elements for which
\[
d_F(s)=f(s)\quad(s\in S),\qquad d_F(t)\le1\quad(t\notin S).
\]
Consequently, realizability is decidable by a finite, explicitly bounded search. Moreover, for any fixed \(u\ge1\), the prescription \(f(u)=r\), \(f(t)=1\) for \(t\ne u\), is realizable exactly when \(r\in\{1,2\}\). (For \(r=1\) the exceptional set is empty.)

## Assumptions and scope
All sets consist of positive integers. Each difference is positive, hence an ordered representation \((a,b)\) with \(a>b\) is counted once. Prescriptions are finite-valued, and the set of positions with requested multiplicity greater than one is finite. The bound \(B\) is elementary and deliberately not optimized; the asserted decision procedure need not be computationally efficient.

## Proof
**1. Preservation under remote insertion.** Let \(F\subset\mathbb N\) be finite nonempty and let \(u\ge1\) have \(d_F(u)=0\). Put \(m=\max F\), \(x=2m+u+1\), and \(F'=F\cup\{x,x+u\}\). Every previous positive difference is at most \(m-1\). All cross differences involving one new and one old element are greater than \(m+u\), hence neither a previous difference nor \(u\). Differences \(x-a\) with \(a\in F\) are mutually distinct, as are differences \(x+u-a\). A coincidence between these two classes would give \(b-a=u\) for some \(a,b\in F\), contrary to \(d_F(u)=0\). Finally the difference between the two new elements is exactly \(u\). Thus \(d_{F'}(u)=1\), all old difference counts are unchanged, and each other newly represented difference occurs once. Apply this operation sequentially to the least positive difference still unrepresented, skipping ones already represented; the increasing union \(A\) satisfies
\[
d_A(t)=\max\{1,d_F(t)\}\qquad(t\ge1).
\]
At most one insertion is required for each successive \(t\). The resulting set is necessarily infinite, since it represents every positive difference.

**2. Finite extraction from any solution.** Suppose \(A\) has the prescribed difference counts. For every \(s\in S\), retain both endpoints of all its \(f(s)\) representations. Their union \(F\) contains at most \(2R\) points. It has exactly \(d_F(s)=f(s)\) for \(s\in S\), and \(d_F(t)\le1\) outside \(S\), since \(F\subseteq A\).

**3. Bounded compression of the finite seed.** On these \(F\) vertices connect pairs at distances belonging to \(S\), and let \(C_0,\ldots,C_{c-1}\) be the connected components. Every vertex is an endpoint of such an edge, and \(c\le|F|\le2R\). In each component, a path of at most \(2R-1\) edges, each of length at most \(M\), connects any two vertices. Hence every component has diameter at most \(W\).

Distinct components have disjoint sets of positive differences. Indeed, if components \(C_i,C_j\) each had a pair at the same positive distance \(v\), their two pairs would form a parallelogram and hence give two different representations of the same positive cross-component difference. That cross-component difference cannot lie in \(S\), since otherwise its endpoints would join the two components. This contradicts \(d_F(t)\le1\) off \(S\).

Let \(m_i=\min C_i\) and form
\[
F^*=\bigcup_{i=0}^{c-1}\{H4^i+(a-m_i):a\in C_i\}.
\]
Internal component differences are unchanged. Every cross-component difference has magnitude at least \(H-W>M+W\), so no cross difference equals an internal difference or a member of \(S\). Differences between distinct ordered component pairs lie within \(W\) of distinct numbers \(H(4^j-4^i)\), \(j>i\). Those centers are distinct integral multiples of \(H\) (factor out the highest power of \(4\)), hence their \(W\)-neighborhoods are disjoint because \(H>2W\). For a fixed pair of components, equality of two cross differences with different endpoint pairs would require their internal difference sets to share a positive number, excluded above. Consequently every cross-component difference in \(F^*\) occurs exactly once, and all multiplicities in \(S\) agree with those of \(F\). Also
\[
1\le\min F^*,\qquad\max F^*\le H4^{c-1}+W<B.
\]
This yields the stated bounded seed.

**4. Equivalence and decision.** A solution implies such a bounded seed by steps 2 and 3. Conversely, any bounded seed with the displayed counts yields a solution by step 1. The existence of a bounded seed is a finite test over subsets of \(\{1,\ldots,B\}\) with at most \(2R\) elements, checking all their pairwise distances. This is a terminating decision algorithm.

**5. Singleton defect.** Two representations of a fixed \(u\) are realized by \(F=\{1,1+u,1+2u\}\), which has counts \(d_F(u)=2\) and \(d_F(2u)=1\). Step 1 completes it. If \(r\ge3\), choose three distinct starts \(a_1<a_2<a_3\) of pairs \(\{a_i,a_i+u\}\). Among their three positive pairwise differences some \(v\ne u\) occurs. The starts and the shifted starts furnish two distinct representations of \(v\), contrary to the required \(d_A(v)=1\). The \(r=1\) case is the usual perfect-difference construction, obtained from a singleton by step 1.

## Verification
The supplied standard-library Python script checks the remote-pair insertion invariants through target differences \(8\), \(14\), and \(25\) for four values of \(u\), and checks preservation under bounded component compression for 360 pseudorandom finite examples and exhaustively for all 808 qualifying subsets of \(\{1,\ldots,10\}\). It returns `VERIFY_OK`. This computation is illustrative: the unrestricted assertion follows from the preceding arguments, not from finite enumeration.

## Relationship to prior work
Ma and Wu, *Dense Sets with Prescribed Difference Representation Functions*, arXiv:2610.27786v1 (first submitted 2026-10-20), analyze higher multiplicities under eventual or long-interval hypotheses. Their Section 1 specifically shows that multiplicity three at distance one and multiplicity one elsewhere is impossible; their Theorems 1.1–1.3 require many indices of multiplicity at least two. The present finite-defect theorem treats the complementary regime, where only finitely many indices have higher multiplicity, and supplies an explicit decision bound. Their Section 5 remote-insertion principle motivates the construction but does not state this criterion. Cilleruelo and Nathanson, *Perfect difference sets constructed from Sidon sets* (2006, arXiv:math/0609244), treat multiplicity one at every distance and a related remote-pair completion; neither published statement supplies the bounded finite-defect test. The compression argument is needed for the effective bound.

## Limitations
No density lower bound, efficient algorithm, or classification for infinitely supported excess multiplicities is asserted. The explicit decision bound is large. The novelty comparison is to the inspected sources and the available mathematical-record search, not a claim of absolute priority against all unpublished computations or unindexed literature.

## References
1. W.-X. Ma and B.-L. Wu, *Dense Sets with Prescribed Difference Representation Functions*, arXiv:2610.27786v1, submitted 2026-10-20, https://arxiv.org/html/2610.27786v1.
2. J. Cilleruelo and M. B. Nathanson, *Perfect difference sets constructed from Sidon sets*, arXiv:math/0609244, submitted 2006-09-08, https://arxiv.org/abs/math/0609244.
