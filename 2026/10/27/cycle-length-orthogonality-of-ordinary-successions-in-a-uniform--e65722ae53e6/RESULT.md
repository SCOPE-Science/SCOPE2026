# Cycle-length orthogonality of ordinary successions in a uniform permutation

## Finding
Let \(\Pi\) be a uniformly random permutation of \([n]\), \(n\ge2\), written in one-line notation. Let
\[
S=\sum_{i=1}^{n-1} A_i,\qquad A_i=\mathbf1\{\Pi(i+1)=\Pi(i)+1\},
\]
and let \(C_j\) be the number of cycles of length \(j\) in the **same permutation**. For every \(1\le j\le n\),
\[
\boxed{\operatorname{Cov}(S,C_j)=
\frac{2\mathbf1\{j=1\}-\mathbf1\{j=2\}-\mathbf1\{j=n-1\}}{n(n-1)}
+\frac{\mathbf1\{j=n\}}{n^2}.}
\]
Coincident indicator positions are added: the formula also covers \(n=2,3\). In particular, \(\operatorname{Cov}(S,C_j)=0\) identically for every \(3\le j\le n-2\) (whenever that interval is nonempty). The signs of the four possible nonzero contributions are positive at lengths \(1,n\), negative at \(2,n-1\), with the prescribed combinations for small \(n\).

A sharper positionwise statement holds for \(n\ge5\). Write \(p_i=\mathbf1\{i\ge2\}+\mathbf1\{i\le n-2\}\) for \(1\le i<n\). Then
\[
\boxed{\operatorname{Cov}(A_i,C_j)=
\begin{cases}
\dfrac{p_i}{n(n-1)(n-2)},&j=1,\\[3pt]
\dfrac{1-p_i}{n(n-1)(n-3)},&j=2,\\[3pt]
0,&3\le j\le n-2,\\[3pt]
\dfrac{p_i-(n-2)}{n(n-1)(n-2)(n-3)},&j=n-1,\\[3pt]
\dfrac{1}{n^2(n-1)},&j=n.
\end{cases}}
\]
Thus every *single* ordinary-succession indicator is uncorrelated with every intermediate cycle-length count, even though those indicators are not independent of the full cycle-type vector. Summing the length spectrum gives \(\operatorname{Cov}(S,\sum_j C_j)=1/n^2\); this scalar identity is included only as a consistency check and was previously established for the total cycle count.

## Assumptions and scope
All permutations of \([n]=\{1,\ldots,n\}\) are equally likely. A succession is an adjacent pair **in the one-line word** whose values rise by exactly one; it is not a succession written inside a disjoint-cycle representation. Cycle counts refer to disjoint cycles of that same mapping, without changing to a different permutation under a bijection. Expectations and covariances use this one probability space. Zero covariance is not a claim of independence.

## Proof
Fix \(1\le i<n\) and \(1\le b<n\), and prescribe both arrows \(\Pi(i)=b\) and \(\Pi(i+1)=b+1\). Denote this event by \(E_{i,b}\). The events \(E_{i,b}\), as \(b\) varies, are disjoint and exhaust \(A_i\). Each has probability \(1/[n(n-1)]\). View a permutation as a directed union of cycles. The two prescribed arrows have precisely three possible configurations:

* **L:** \(b=i\): two fixed loops, at \(i\) and \(i+1\).
* **P:** \(b=i-1\) (when \(i\ge2\)) or \(b=i+1\) (when \(i\le n-2\)): one directed path of two edges.
* **D:** all other \(b\): two disjoint directed paths, each of one edge.

Contract the prescribed path edges, or remove the two forced loops. In each case completions of the prescribed arrows correspond bijectively to arbitrary permutations on \(m=n-2\) objects. In P one contracted object is marked and its resulting cycle expands by two vertices. In D two contracted objects are marked and each containing cycle expands by the number of marks it carries. The bijection is uniform because every completion has probability \((n-2)!/n!\). Put \(L_j,P_j,D_j\) for the three resulting conditional expectations of \(C_j\).

For a uniform permutation of \(m\) objects, the expected count of \(r\)-cycles is \(1/r\). A specified mark belongs to an \(r\)-cycle with probability \(1/m\). With two different marks, the expected number of \(r\)-cycles containing exactly \(s\) marks is
\[
\frac1r\,\frac{\binom{2}{s}\binom{m-2}{r-s}}{\binom mr}\quad(s=0,1,2),
\]
where binomial coefficients with inadmissible arguments are zero. These statements follow by summing over the \(\binom mr\) possible vertex sets of an \(r\)-cycle, each having expected cycle-count contribution \(1/[r\binom mr]\).

For \(n\ge4\), hence \(m\ge2\), the three conditional expectations have the following complete table:

| Cycle length | \(L_j\) | \(P_j\) | \(D_j\) |
|---|---:|---:|---:|
| \(j=1\) | \(3\) | \(1-1/m\) | \(1-2/m\) |
| \(j=2\) | \(1/2\) | \(1/2-1/m\) | \(1/2+1/[m(m-1)]\) |
| \(3\le j\le m\) | \(1/j\) | \(1/j\) | \(1/j\) |
| \(j=m+1\) | \(0\) | \(1/m\) | \((m-2)/[m(m-1)]\) |
| \(j=m+2\) | \(0\) | \(1/m\) | \(1/m\) |

Empty rows are omitted. To verify D in the middle range, the three contributions from cycles with zero, one, or two marks simplify identically:
\[
D_j=\frac{(m-j)(m-j-1)/j+2(m-j+1)+(j-3)}{m(m-1)}=\frac1j
\quad(3\le j\le m).
\]
The boundary entries follow directly from the same marked-cycle formula; P and L follow from the single marked-cycle and two-loop constructions.

For a fixed \(i\), the number of P choices is \(p_i\), the number of L choices is one, and the number of D choices is \(m-p_i\). Since \(\mathbb E A_i=1/n\) and \(\mathbb E C_j=1/j\),
\[
\operatorname{Cov}(A_i,C_j)
=\frac{L_j+p_iP_j+(m-p_i)D_j}{n(n-1)}-\frac1{nj}.
\]
Substitution of the table and elementary cancellation give the asserted five-case positionwise formula for \(n\ge5\). In particular, all three category expectations are \(1/j\) throughout \(3\le j\le n-2\), so the entire middle band vanishes *before any sum over positions*.

There are \(n-1\) L choices, \(2(n-2)\) P choices, and \((n-2)(n-3)\) D choices in the aggregate over all pairs \((i,b)\). Therefore
\[
\mathbb E[SC_j]
=\frac{(n-1)L_j+2(n-2)P_j+(n-2)(n-3)D_j}{n(n-1)},
\]
while \(\mathbb E S=(n-1)/n\). Subtracting \((n-1)/(nj)\) yields the boxed cycle-length spectrum for \(n\ge4\).

For the two remaining sizes, direct enumeration gives \(n=2\): covariance vector \((1/2,-1/4)\); and \(n=3\): \((1/3,-1/3,1/9)\). Both coincide with the general indicator formula. This completes the proof for all claimed dimensions and cycle lengths.

## Verification
The standalone `verify.py` independently enumerates every permutation for \(2\le n\le8\), directly determines each cycle length and ordinary succession position, and compares exact rational covariances against both formulas. It also independently checks the contraction-category table and its algebraic summation for \(5\le n\le150\). Invoke `python verify.py` with Python 3; no external packages or data are needed. A successful run reports 46,232 exhaustively enumerated permutations, 183 exact enumeration comparisons, and 1,136,245 algebraic category/aggregation comparisons. The infinite claim follows from the proof, not from the finite computations.

## Relationship to prior work
Reilly and Tanny (1979) enumerate ordinary one-line successions. Diaconis, Evans, and Graham (2013/2014) prove that their random set is equidistributed with a subset of the fixed-point set; this is a marginal identity, not a joint identity with cycle counts of the original permutation. A previous calculation of the full **total-cycle-count** law under conditioning on an adjacent numerical jump includes the scalar \(\operatorname{Cov}(S,\sum_j C_j)=1/n^2\), but does not determine how the covariance is distributed over cycle lengths. The present result resolves that finer dependence spectrum and its positionwise cancellations.

Mansour and Shattuck (2016) enumerate *successions within disjoint-cycle notation* jointly with the number of cycles. Their correspondence converts ordinary successions into cycle successions of a different permutation and does not preserve the original permutation's cycle-type vector; the authors specifically note differences in joint distributions with other statistics. Ma, Qi, J. Yeh, and Y.-N. Yeh (2024) study successions jointly with Eulerian and related statistics. Their appearance of \(\mathrm{cyc}\) on the opposite side of a distributional identity does not itself give the same-permutation cycle-length cross-moments here. Searches described in the companion review identified no established formula implying the boxed length spectrum. This is a best-knowledge originality assessment, not proof of historical priority.

## Limitations
The result concerns linear one-line successions and uniform permutations only, not circular successions, cyclic-word successions, weighted permutations, or independence. The numerical covariances are often small, though the exact middle-band cancellation holds at every finite \(n\). Older or less-indexed literature may contain an equivalent identity; no independent historical-priority audit has been performed.

## References
1. J. W. Reilly and S. M. Tanny, *Counting Successions in Permutations*, Studies in Applied Mathematics 61 (1979), 73–81. DOI: `10.1002/sapm197961173`.
2. P. Diaconis, S. N. Evans, and R. Graham, *Unseparated Pairs and Fixed Points in Random Permutations*, Berkeley Statistics Technical Report 822, public report dated 2013-08-01; later Advances in Applied Mathematics 61 (2014), 102–124. `https://statistics.berkeley.edu/tech-reports/822`.
3. T. Mansour and M. Shattuck, *Counting permutations by the number of successions within cycles*, Discrete Mathematics 339 (2016), 1368–1376. DOI: `10.1016/j.disc.2015.12.004`.
4. S.-M. Ma, H. Qi, J. Yeh, and Y.-N. Yeh, *On the joint distributions of succession and Eulerian statistics*, arXiv:2401.01760 (2024). `https://arxiv.org/abs/2401.01760`.
