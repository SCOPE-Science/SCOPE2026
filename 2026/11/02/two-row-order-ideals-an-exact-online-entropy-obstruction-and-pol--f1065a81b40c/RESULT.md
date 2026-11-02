# Two-row order ideals: an exact online entropy obstruction and polynomial recurrence

## Finding
For an integer \(n\ge1\), let \(P_n=[2]\times[n]\) with the product order, and let \(\mathcal J_n\) be its set of order ideals, regarded as Boolean functions on \(P_n\) by membership. Then \(|\mathcal J_n|=\binom{n+2}{2}\). The VC dimension is one for \(n=1\), and two for every \(n\ge2\). Put \(U_n=\lfloor\log_2\binom{n+2}{2}\rfloor\). For all \(n\ge1\),
\[
U_n-2\le \operatorname{Ldim}(\mathcal J_n)\le U_n.
\]
There is an exact finite-state recurrence, with at most \(O(n^4)\) states and \(O(n)\) transitions per state, computing \(\operatorname{Ldim}(\mathcal J_n)\) in \(O(n^5)\) arithmetic operations. Its exact values for \(1\le n\le60\) are specified by the least \(n\) attaining each positive dimension:
\[
\begin{array}{c|rrrrrrrrrr}
 d&1&2&3&4&5&6&7&8&9&10\\\hline
 n_{\min}(d)&1&2&3&5&8&12&17&25&36&52
\end{array}.
\]
Precisely, within \(1\le n\le60\), the dimension is the largest \(d\in\{1,\ldots,10\}\) with \(n\ge n_{\min}(d)\). In particular, \(n=7\) is the first case in this family where the universal information bound is not attained:
\[
\operatorname{VCdim}(\mathcal J_7)=2,\quad
\operatorname{Ldim}(\mathcal J_7)=4
<5=\lfloor\log_2 36\rfloor.
\]

## Assumptions and scope
The poset is the Cartesian product of a two-point chain and an \(n\)-point chain. Queries are single-element membership in an unknown order ideal; they are not comparison queries or noisy-label observations. Write the lengths of the ideal's upper and lower rows as \(a,b\), so that \(0\le a\le b\le n\). A query in the upper row at column \(j\) returns one iff \(a\ge j\), and in the lower row it returns one iff \(b\ge j\). Thus ideals are in bijection with such integer pairs, giving the displayed cardinality. Littlestone dimension is complete binary adaptive-query shattering depth, with value zero for a singleton concept family.

## Proof
**VC dimension.** A membership support is shattered by all order ideals of any finite poset exactly when it is an antichain. If two queried points are comparable, the answer assigning one to the ideal and its predecessor outside is impossible. Conversely, for any antichain and any desired positive subcollection, its downward closure contains exactly those positive points on the antichain. The width of \(P_n\) is one at \(n=1\) and exactly two at \(n\ge2\): each of its two rows is a chain, and \((1,2)\), \((2,1)\) are incomparable when \(n\ge2\).

**Exact all-size recurrence.** Every nonempty version space after finitely many coordinate queries has precisely the form
\[
H(A,B,C,D)=\{(a,b)\in\mathbb Z^2:A\le a\le B,\ C\le b\le D,\ a\le b\}.
\]
Normalize \(B\leftarrow\min(B,D)\) and \(C\leftarrow\max(C,A)\). If the resulting space is empty it is not a valid decision-tree child; if it contains exactly one pair its depth is zero. Otherwise define \(F(A,B,C,D)\) to be the maximum, over every cut \(A<j\le B\) and \(C<j\le D\) with two nonempty children, of
\[
1+\min\{F(H_0),F(H_1)\},
\]
where a cut on \(a\) restricts \(a<j\) versus \(a\ge j\), and a cut on \(b\) restricts \(b<j\) versus \(b\ge j\). Here \(F(H_i)\) means the same four-bound function on the updated interval endpoints. This recurrence is exact by induction on the number of pairs: a shattered depth-\(k\) tree has a first query whose two children shatter depth \(k-1\) trees, and conversely such children can be joined at their query root. It terminates because each proper split strictly reduces both child families. Each normalized state has four endpoints from \(\{0,\ldots,n\}\), giving \(O(n^4)\) states, with at most \(2n\) cuts per state. The initial answer is \(F(0,n,0,n)\). The included verifier implements this recurrence and a second, independent recurrence directly on concept bitsets.

**Uniform near-entropy bound.** Let \(q=\lfloor n/2\rfloor\). Restrict to the subfamily \(0\le a\le q\), \(q\le b\le n\); the two coordinates are now independent threshold classes with \(q+1\) and \(n-q+1\) possibilities. Binary splitting of each chain gives a complete adaptive tree of depth
\[
L=\lfloor\log_2(q+1)\rfloor+\lfloor\log_2(n-q+1)\rfloor,
\]
by concatenating the two trees. Write \(X=q+1\), \(Y=n-q+1\) and \(N=\binom{n+2}{2}\). Direct substitution for even and odd \(n\) shows \(N<2XY\). Hence \(\lfloor\log_2N\rfloor\le\lfloor\log_2(XY)\rfloor+1\le L+2\). The reverse inequality follows from the fact that a complete depth-\(k\) tree requires at least \(2^k\) distinct concepts.

**First strict bound.** At \(n=7\), there are \(36\) ideals. The fourteen possible query columns have positive-branch sizes drawn from \(\{1,3,6,8,10,15,21,26,28,30,33,35\}\). Every first query has a child of size at most fifteen, so no depth-five tree can exist, because each depth-four child needs at least sixteen different concepts. On the other hand the sixteen pairs \(0\le a\le3\), \(4\le b\le7\) form a product of two four-choice threshold classes. Concatenate two depth-two threshold trees to shatter a tree of depth four. For \(n=1,\ldots,6\), the exact recurrence gives dimensions \(1,2,3,3,4,4\), equal to \(\lfloor\log_2\binom{n+2}{2}\rfloor\). Therefore seven is first.

**Finite cutoff values.** The exact recurrence computes each value for \(1\le n\le52\). A separate bitset recurrence checks twenty-four sizes, including every stated later jump. For \(53\le n\le60\), monotonicity under adding a final column yields the lower bound ten from \(n=52\), and \(\binom{62}{2}=1891<2048\) supplies the upper bound ten. These steps prove the displayed finite threshold list without extrapolating it to larger \(n\).

## Verification
Run `python3 verify_grid_ideal_learning.py` with Python 3 and its standard library. The program checks all exact threshold boundaries, cross-checks independent representations at twenty-four sizes, enumerates the twelve distinct first-query branch sizes at seven columns, and tests the arithmetic near-entropy bound on a large finite range as a consistency check. The all-size bound and recurrence are proved above independently of the finite arithmetic tests. A machine-readable complete table through sixty columns is included as `exact_table_1_to_60.json`.

## Relationship to prior work
Ghazi, Golowich, Kumar and Manurangsi (arXiv:2007.03668, first public 2020-07-07; PMLR 2021) establish general closure bounds for Littlestone dimension, not this exact order-constrained two-threshold family. Hanneke (PMLR 2024) develops general structural relationships among combinatorial dimensions and version spaces, without the present exact table or first-obstruction value. The underlying order-ideal/monotone-staircase interpretation is standard; neither it nor the generic cardinality bound is claimed as new. Searches under lattice-path, Ferrers, nested-threshold, monotone-staircase, and order-ideal terminology did not locate a prior source implying the combined specific result. This is a qualified literature comparison, not a proof of priority.

## Limitations
The finite exact classification stops at sixty columns. The polynomial recurrence applies for every finite \(n\), but no closed form for its threshold locations beyond the stated range is asserted. No statement is made about taller rectangular posets, other query types, or optimized computation time beyond the proved polynomial bound. Earlier publications might contain these exact values under different terminology. The finite verifier is reproducibility evidence, not independent mathematical auditing.

## References
1. B. Ghazi, N. Golowich, R. Kumar and P. Manurangsi, *Near-tight closure bounds for Littlestone and threshold dimensions*, arXiv:2007.03668v1 (2020-07-07); PMLR 132 (2021), 686–696. https://arxiv.org/abs/2007.03668 ; https://proceedings.mlr.press/v132/ghazi21a.html .
2. S. Hanneke, *The Star Number and Eluder Dimension: Elementary Observations About the Dimensions of Disagreement*, PMLR 247 (2024), 2308–2359. https://proceedings.mlr.press/v247/hanneke24a.html .
