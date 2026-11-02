# Sharp factorial unimodality transition for diagonal-deleted multipartite graphs

## Finding

For integers \(a\ge5\) and \(r\ge2a+4\), let \(T^*(r,a)\) be the graph on vertices \((i,j)\), with \(1\le i\le a\), \(1\le j\le r\), whose distinct vertices are adjacent exactly when both their row and column indices differ. Write \(\psi(T^*(r,a);x)=\sum_{k=0}^{r}c_kx^k\), where \(c_k\) counts the vertex subsets with no three members on one geodesic. Put

\[
R_a=(a+1)(a-1)!+2a+2.
\]

**Theorem.** Throughout this two-parameter region,

\[
\psi(T^*(r,a);x)\text{ is unimodal}\quad\Longleftrightarrow\quad r\ge R_a.
\]

For \(2a+4\le r<R_a\), the sequence has a strict descent and immediate ascent at index \(a+1\): \(c_a>c_{a+1}<c_{a+2}\). For \(r\ge R_a\), the entire sequence is unimodal. The threshold is exact for every \(a\ge5\), with no asymptotic or sufficiently-large qualification.

For example, \(R_5=156\). At \(r=155\), the consecutive coefficients \((c_5,c_6)=(87315863405,87315863250)\) descend, while \(c_7>c_6\). At \(r=156\), \((c_5,c_6)=(90207117156,90808497780)\), and the full polynomial is unimodal.

## Assumptions and scope

Graphs are finite and simple. A general-position set \(S\) is one for which no three distinct members \(u,v,w\) satisfy \(d(u,w)=d(u,v)+d(v,w)\) in any order. Unimodality of \((c_0,\ldots,c_r)\) means it is nondecreasing up to some index and nonincreasing thereafter. All binomial coefficients outside their usual integer range are zero. The falling factorial is \((r)_k=r(r-1)\cdots(r-k+1)\). The theorem concerns \(a\ge5\), \(r\ge2a+4\); it does not classify other pairs.

## Proof

**1. Counting lemma and classification.** Two vertices are adjacent if their row and column are both different; otherwise they are at distance two (as \(a,r\ge3\)). For a set with at least three vertices, the general-position condition prohibits a selected common neighbor of any selected nonadjacent pair. If all selected pairs are adjacent, the set is a clique, meeting each row and column at most once. If the set contains two vertices in one row and also a vertex outside that row, the latter must have one of their two column labels. An additional vertex outside the resulting two-row, two-column rectangle would be a common neighbor of some selected nonadjacent pair. Interchanging rows and columns covers the other possibility. Thus every general-position set of size at least three is uniquely one of: a subset of one row; a subset of one column; a clique with distinct rows and columns; or a three- or four-vertex subset of a two-by-two rectangle. These types are mutually exclusive for sizes at least three; each rectangle is determined by its selected vertices. This reconstructs the corrected coefficient formula of Rather, Theorem 5.3:

\[
\begin{aligned}
c_0&=1,\qquad c_1=ar,\qquad c_2=\binom{ar}{2},\\
c_k&=a\binom rk+r\binom ak+k!\binom ak\binom rk
   +\binom a2\binom r2\binom4k\quad(k\ge3).
\end{aligned}
\]

The four terms count, respectively, single-row sets, single-column sets, cliques, and rectangle sets. For \(k\ge a+1\), because \(a\ge5\), this simplifies to \(c_k=a\binom rk\).

**2. Strict increase through index \(a\).** Define \(B_k=a\binom rk\), \(Q_k=\binom ak(r)_k\), and \(\beta=\binom a2\binom r2\). For \(3\le k\le a\), the coefficient is \(c_k=B_k+r\binom ak+Q_k+\beta\binom4k\). In our region, \(B_3<B_4<\cdots<B_a\). Also \(1<ar<\binom{ar}{2}\). The rectangle contribution alone makes the next inequality strict, because

\[
4\beta-\binom{ar}{2}
=\frac{ar}{2}\bigl((a-2)r-(2a-3)\bigr)>0,
\]

so \(c_2<c_3\).

For the exceptional step \(3\to4\),
\[
\frac{Q_4}{Q_3}=\frac{(a-3)(r-3)}4\ge\frac{11}{2},\qquad
\frac{Q_3}{\beta}=\frac{2(a-2)(r-2)}3\ge24,\qquad
\frac{r\binom a3}{Q_3}\le\frac1{156}.
\]

Thus \((Q_4-Q_3)+r(\binom a4-\binom a3)\ge(9/2-1/156)Q_3>3\beta\). After adding the positive difference \(B_4-B_3\), this proves \(c_4>c_3\), notwithstanding the loss of three rectangle units.

For \(4\to5\),
\[
\frac{Q_5}{Q_4}=\frac{(a-4)(r-4)}5\ge2,\qquad
\frac{Q_4}{\beta}=\frac{(a-2)(a-3)(r-2)(r-3)}6\ge132,\qquad
\frac{r\binom a4}{Q_4}\le\frac1{1716}.
\]

Consequently \((Q_5-Q_4)+r(\binom a5-\binom a4)\ge(1-1/1716)Q_4>\beta\), and hence \(c_5>c_4\).

Finally, if \(5\le k<a\),
\[
\frac{Q_{k+1}}{Q_k}=\frac{(a-k)(r-k)}{k+1}
\ge\frac{r-a+1}{a}\ge1+\frac5a.
\]

The possible negative change of \(r\binom ak\) is at most \(r\binom ak\), whereas the increase of \(Q_k\) is at least \(5Q_k/a>r\binom ak\), since \((r)_k\ge r(r-1)>ar/5\). Together with \(B_{k+1}>B_k\), this proves \(c_{k+1}>c_k\). We have established
\[
c_0<c_1<\cdots<c_a.
\]

**3. One sharp boundary.** The tail \((c_{a+1},\ldots,c_r)\) equals the scaled binomial row \((a\binom r{a+1},\ldots,a\binom rr)\), hence is unimodal. Moreover \(c_{a+2}>c_{a+1}\) because \(r\ge2a+4\). Combining with Step 2, the full polynomial is unimodal if and only if \(c_{a+1}\ge c_a\).

Since \(a\ge5\),
\[
c_a=(a+a!)\binom ra+r,\qquad c_{a+1}=a\binom r{a+1},
\]

and subtraction yields the exact gap
\[
\boxed{c_{a+1}-c_a=\frac{a}{a+1}\binom ra(r-R_a+1)-r.}
\]

If \(r<R_a\), the first term is nonpositive and the gap is negative. If \(r\ge R_a\), then \(r-R_a+1\ge1\) and
\[
\frac a{a+1}\binom ra-r
=r\left(\frac{\binom{r-1}{a-1}}{a+1}-1\right)>0,
\]

since \(\binom{r-1}{a-1}\ge r-1>a+1\). Hence the gap is strictly positive exactly from \(R_a\) onward, proving the theorem. \(\square\)

## Verification

Execute `python3 verify.py` with Python 3. Its graph-level enumerator independently constructs all general-position sets for \((a,r)=(3,3),(3,4),(3,5),(4,3),(4,4)\) and matches the coefficient formula without relying on the four-type argument. Exact-integer checks test all boundary cases \(r\in\{2a+4,2a+5,R_a-2,R_a-1,R_a,R_a+1,R_a+2\}\) for \(5\le a\le11\), including the initial strict increases and the sharp transition. Complete coefficient sequences were also inspected for selected parameters with \(a=5,6\). The script returned `VERIFY_OK`. Finite tests are consistency checks, not the proof for unbounded parameters.

## Relationship to prior work

Iršič, Klavžar, Rus and Tuite introduced general-position polynomials and, in Problem 5.2, asked which \(T^*(r,a)\) have unimodal polynomials. The coefficient formula originally printed for these graphs is not used here: Rather's 2026 Theorem 5.3 corrects it, and his Theorem 5.6 and Corollary 5.7 determine selected small-parameter behavior, especially \(a=3\). The present theorem uses the corrected enumeration to derive and prove an exact factorial boundary on the previously unclassified unbounded region \(a\ge5, r\ge2a+4\). It does not claim a new general coefficient formula or a resolution of the entire open problem.

## Limitations

No assertion is made for \(a\le4\) or \(r<2a+4\), and no log-concavity classification is supplied. The argument assumes the stated corrected graph enumeration; its combinatorial classification is independently reconstructed above and checked in finite instances. Publication-priority uncertainty remains for unindexed or inaccessible equivalent work. The proof has received self-review only, not independent mathematical audit.

## References

1. V. Iršič, S. Klavžar, G. Rus, J. Tuite, *General Position Polynomials*, arXiv:2401.05696, first posted 2024-01-11; especially Section 4 and Problem 5.2. https://arxiv.org/abs/2401.05696
2. B. A. Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930, first posted 2026-03-06, v3 dated 2026-06-24; especially Theorems 5.3 and 5.6 and Corollary 5.7. https://arxiv.org/abs/2603.06930
