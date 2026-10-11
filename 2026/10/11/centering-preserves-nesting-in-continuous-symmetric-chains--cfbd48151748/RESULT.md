# Centering preserves nesting in continuous symmetric chains
## Finding
Let \(d\ge1\), and let
\[
(A_t)_{t\in[0,1]}
\]
be a nested family of nonempty compact centrally symmetric subsets of \(\mathbb R^d\):
\[
A_s\subseteq A_t
\qquad
(s<t).
\]
Assume the order-continuity conditions
\[
A_t=
\overline{\bigcup_{r<t}A_r}
\qquad
(t>0),
\]
and
\[
A_t=
\bigcap_{u>t}A_u
\qquad
(t<1).
\]
Write \(c_t\) for the center of symmetry of \(A_t\). Then
\[
A_s-c_s\subseteq A_t-c_t
\qquad
(s<t).
\]

Consequently, a continuously indexed strongly nested family of centrally symmetric compact sets remains at least ordinarily nested after every member is translated to its own center.

This proves the 2009 conjecture that the pairwise noncontainment phenomenon illustrated by Dawson's Figure 1 cannot occur inside a continuously indexed strongly nested family. The stronger question whether recentering preserves *strong* nesting remains open under the present argument.

## Assumptions and scope
Central symmetry means
\[
A_t=2c_t-A_t.
\]
For any nonempty bounded centrally symmetric subset of Euclidean space, the center is unique. Indeed, if \(c\ne d\) were two centers, the composition of the two half-turns would translate the set by the nonzero vector \(2(d-c)\); iterating that translation would contradict boundedness.

No convexity assumption is needed in the theorem. Compactness, nesting, central symmetry, and the two order-continuity identities are the only hypotheses.

The conclusion is ordinary inclusion after recentering. It does not assert
\[
A_s-c_s\subset \operatorname{int}(A_t-c_t).
\]

## Proof
We first record two continuity facts.

### 1. Order-continuity gives Hausdorff continuity
Suppose \(r\uparrow t\). Since
\[
A_t=\overline{\bigcup_{u<t}A_u}
\]
and \(A_t\) is compact, for every \(\eta>0\) one may choose finitely many points of the union whose \(\eta\)-balls cover \(A_t\). All chosen points belong to one sufficiently late set \(A_r\), by nesting. Hence
\[
d_H(A_r,A_t)\longrightarrow0.
\]

Now suppose \(u\downarrow t\). If Hausdorff convergence failed, there would be \(\eta>0\), a decreasing sequence \(u_j\downarrow t\), and points
\[
x_j\in A_{u_j}
\]
with distance at least \(\eta\) from \(A_t\). All \(x_j\) lie in the fixed compact set \(A_{u_1}\). Passing to a convergent subsequence gives \(x_j\to x\). For every \(v>t\), eventually \(u_j<v\), so nesting gives
\[
x_j\in A_v.
\]
Thus
\[
x\in\bigcap_{v>t}A_v=A_t,
\]
a contradiction. Therefore
\[
d_H(A_u,A_t)\longrightarrow0.
\]
Combining the two one-sided statements shows that \(t\mapsto A_t\) is Hausdorff-continuous.

### 2. Centers vary continuously
Suppose centrally symmetric compact sets \(K_j\) converge in Hausdorff distance to \(K\), with centers \(c_j\). The points \(c_j\) lie in
\[
\operatorname{conv}(K_j),
\]
hence are bounded. Let a subsequence satisfy \(c_j\to c_*\). For any \(x\in K\), choose \(x_j\in K_j\) with \(x_j\to x\). Since
\[
2c_j-x_j\in K_j,
\]
Hausdorff convergence yields
\[
2c_*-x\in K.
\]
Thus \(K\) is centrally symmetric about \(c_*\). By uniqueness of the center,
\[
c_*=c(K).
\]
Every convergent subsequence of the centers has the same limit, so
\[
c_j\to c(K).
\]
Applied to \(A_t\), this proves continuity of
\[
t\longmapsto c_t.
\]

We now prove the inclusion. Fix
\[
s<t
\]
and
\[
y\in A_s-c_s.
\]
Then
\[
p_0=c_s+y\in A_s.
\]

Choose a partition
\[
s=t_0<t_1<\cdots<t_N=t.
\]
Put
\[
v_i=c_{t_i}-c_{t_{i-1}}.
\]
Because \(c_\bullet\) is uniformly continuous on \([s,t]\), partitions can be chosen so that
\[
\delta:=\max_i\|v_i\|
\]
is arbitrarily small.

We use a finite vector-rounding lemma.

**Lemma.** Given vectors
\[
v_1,\ldots,v_N\in\mathbb R^d,
\]
there are coefficients
\[
\varepsilon_i\in\{0,1\}
\]
such that
\[
\left\|
\sum_{i=1}^N
\left(\varepsilon_i-\frac12\right)v_i
\right\|
\le
\frac d2
\max_i\|v_i\|.
\]

To prove the lemma, begin with all coefficients equal to \(1/2\). If more than \(d\) coefficients are fractional, the corresponding vectors are linearly dependent. Move the fractional coefficient vector along a nonzero linear dependence until at least one coefficient reaches \(0\) or \(1\); the represented vector sum does not change. Repeat until at most \(d\) coefficients remain fractional. Round those remaining coefficients to the nearer endpoint. Each final coefficient changes by at most \(1/2\), so the norm error is at most
\[
\frac d2\max_i\|v_i\|.
\]
This proves the lemma.

Apply the lemma to the increments \(v_i\). Starting from \(p_0\), process the partition intervals in increasing order. Whenever \(\varepsilon_i=1\), first reflect the current point about \(c_{t_{i-1}}\), then reflect it about \(c_{t_i}\). The composition of these two central reflections is translation by
\[
2(c_{t_i}-c_{t_{i-1}})=2v_i.
\]

Every reflection is legal. Before the first reflection for interval \(i\), the current point belongs to \(A_{t_{i-1}}\); central symmetry preserves that set. Nesting then places the reflected point in \(A_{t_i}\), where the second reflection is also valid. If \(\varepsilon_i=0\), nesting alone carries membership forward.

After all intervals, we therefore obtain a point
\[
p_\delta\in A_t
\]
with
\[
p_\delta
=
c_s+y+2\sum_{i=1}^N\varepsilon_i v_i.
\]
Since
\[
c_t-c_s=\sum_{i=1}^N v_i,
\]
we have
\[
p_\delta-(c_t+y)
=
2\sum_{i=1}^N
\left(\varepsilon_i-\frac12\right)v_i.
\]
Hence
\[
\|p_\delta-(c_t+y)\|
\le
d\delta.
\]

Let the mesh tend to zero. Then
\[
\delta\to0,
\]
so \(p_\delta\to c_t+y\). Since \(A_t\) is closed and every \(p_\delta\in A_t\),
\[
c_t+y\in A_t.
\]
Thus
\[
y\in A_t-c_t.
\]
Because \(y\in A_s-c_s\) was arbitrary,
\[
A_s-c_s\subseteq A_t-c_t.
\]

## Verification
The supplied `verify.py` replays the finite vector-rounding step using exact rational arithmetic. It repeatedly eliminates fractional coefficients along exact nullspace directions, verifies that the vector sum is preserved, and checks the final
\[
\frac d2\max_i\|v_i\|
\]
bound on several dimensions and nontrivial vector families.

The script also verifies symbolically that the composition of central reflections about \(a\) and \(b\) is
\[
x\longmapsto x+2(b-a),
\]
which is the algebraic mechanism used in the proof.

The infinite-family statement is not inferred from finite computation. Hausdorff continuity, center continuity, the rounding lemma, and the limiting argument are all proved above.

## Relationship to prior work
Dawson's 2009 Banach Center paper studies nested and strongly nested families in convex-body hyperspaces and explicitly observes that recentering two nested centrally symmetric sets need not preserve inclusion in general. Immediately after that example, the paper conjectures that this phenomenon cannot arise inside a continuously indexed strongly nested family.

The Open Problem Session in the same volume formulates the stronger question: if a continuously indexed strongly nested family consists of centrally symmetric sets with centers \(c_i\), must the recentered family
\[
A_i-c_i
\]
remain strongly nested?

The present theorem settles the weaker conjecture from the paper itself: continuity prevents outright loss of inclusion. It also reduces the stronger open problem to a strictness issue, namely whether boundary contact can occur after recentering.

A 2010 follow-up on monotone and Čebyšev arcs gives a detailed theory for convex hyperspace arcs, including strongly nested arcs and support-function characterizations. That full text does not provide the above recentering theorem, and its methods assume convexity in the relevant structural results, whereas the present proof does not.

Targeted searches for the exact recentering statement, the Figure 1 conjecture, centered translates of continuously nested symmetric sets, and equivalent inclusion formulations did not locate a published resolution.

## Limitations
The theorem proves only ordinary nesting after recentering. It does not prove that
\[
A_s-c_s
\subset
\operatorname{int}(A_t-c_t)
\]
when the original family is strongly nested.

No quantitative lower bound is obtained for the distance between the recentered boundaries.

The proof is Euclidean and finite-dimensional because the vector-rounding step uses dimension \(d\). No infinite-dimensional analogue is asserted.

Historical indexing is incomplete, so an unindexed later resolution of Dawson's conjecture remains a residual originality risk.

## References
1. R. J. MacG. Dawson, *Some Čebyšev sets with dimension \(d+1\) in hyperspaces over \(\mathbb R^d\)*, Banach Center Publications 84 (2009), 89--110. DOI: 10.4064/bc84-0-6. Primary MSC 52A20.
2. *Open Problem Session*, Banach Center Publications 84 (2009), 217--222, Problem 2.
3. R. Dawson and M. Moszyńska, *Čebyšev Sets in Hyperspaces over \(\mathbb R^n\)*, Canadian Journal of Mathematics 61 (2009), 299--314. DOI: 10.4153/CJM-2009-015-x. Published 2009-04-01.
4. R. J. MacG. Dawson, *Monotone and Čebyšev arcs in hyperspaces*, Journal of Geometry 98 (2010), 1--19. DOI: 10.1007/s00022-010-0044-0.
