# A denser explicit Barrycade construction

## Theorem

For every integer \(h\ge 2\), there exists a \((14h-13)\)-barrycade of height \(h-1\). Consequently, if \(H(n)\) denotes the maximum possible height of an \(n\)-barrycade, then
\[
H(14h-13)\ge h-1,
\qquad
\limsup_{n\to\infty}\frac{H(n)}n\ge \frac1{14}.
\]

This sharpens the explicit \(24h\)-construction of Dębski, Grytczuk, Naroski, Pawlik, Przybyło, and Śleszyńska-Nowak, *Finite and infinite barrycades* (arXiv:2609.18476v1, 2026), which gives height \(h-1\).

## Definitions

An \(n\)-barrycade is a collection of permutations of \([n]=\{1,\ldots,n\}\) such that the sets of proper prefix sums of any two permutations are disjoint. Its height is the number of rows/permutations.

The construction follows the framework of the cited paper but tightens the only quantitative collision count that controls the size of the auxiliary blocks.

## 1. Auxiliary blocks

Fix \(h\ge2\). Set
\[
x_1=2h+1.
\]
For \(i=2,\ldots,h-1\), choose \(x_i\) greedily as the least integer \(d>x_{i-1}\) for which
\[
J_i(d)=\{d+i,\ d+2i,\ d+i+2h\}
\]
is disjoint from every earlier set
\[
J_k=\{x_k+k,\ x_k+2k,\ x_k+k+2h\},\qquad k<i.
\]

### Three-skip lemma
For a fixed earlier \(k<i\), at most three values of \(d>x_k\) can be forbidden by a collision with \(J_k\).

Indeed, the nine possible equalities between a new joint and an old joint reduce to the following three that can have \(d-x_k>0\):
\[
\begin{aligned}
 d+i &= x_k+2k, & d-x_k&=2k-i,\\
 d+i &= x_k+k+2h, & d-x_k&=2h+k-i,\\
 d+2i &= x_k+k+2h, & d-x_k&=2h+k-2i.
\end{aligned}
\]
The other six give a negative right-hand side:
\[
k-i,\quad k-2i,\quad 2k-2i,\quad k-i-2h,\quad 2k-i-2h,\quad k-i.
\]
Hence each earlier \(x_k\) causes at most three skipped candidate values in the entire greedy process.

Only \(k\le h-2\) can obstruct a future choice. Starting from \(x_1=2h+1\), there are \(h-2\) mandatory increments and at most \(3(h-2)\) skips, so
\[
x_{h-1}\le (2h+1)+(h-2)+3(h-2)=6h-7.
\]

Put \(X=x_{h-1}\) and
\[
L=2X+2h+1.
\]
For \(1\le i<h\), define
\[
P_i=(x_i,\ i,\ 2h-i,\ 2X+1-x_i),
\]
and let
\[
P_h=(L).
\]
Every \(P_i\) has total length \(L\). Moreover:

* every block length occurring among the \(P_i\) is globally unique;
* the lengths \(h\) and \(2h\) do not occur;
* \(i\) is followed by \(2h-i\) in \(P_i\) for \(i<h\);
* placing the \(P_i\) with start points one unit apart creates no coincident joints, by construction of the \(x_i\); the final joints are also distinct and lie beyond all earlier internal joints;
* all block lengths are at most \(L\).

Finally,
\[
L\le 2(6h-7)+2h+1=14h-13.
\]

## 2. Assemble the rows

Start with \(h\) rows. Row \(i\) begins with the single block \(i\), followed by \(P_i\). Since the \(P_i\) have equal total length and are started one unit apart, their joints do not collide and the row endpoints are consecutive.

For each round \(j=1,\ldots,h-1\):

1. append the block \(h\) to row \(j\), which is the current leftmost row and moves it to the right end of the consecutive endpoint window;
2. append to row \(i\) the auxiliary block list \(P_{i-j\pmod h}\), interpreting residue \(0\) as \(h\).

Because all \(P_r\) have total length \(L\), and because their internal joint patterns are collision-free under unit shifts, the endpoints remain consecutive and no new joint collision is introduced.

After the \(h-1\) rounds, every row contains exactly one copy of every \(P_1,\ldots,P_h\). Rows \(1,\ldots,h-1\) have also received one block \(h\); row \(h\) has not. Their endpoints are
\[
hL+h+i \quad (1\le i<h),\qquad hL+h \quad(i=h).
\]
Delete row \(h\). The remaining \(h-1\) endpoints are consecutive.

Each surviving row now contains every length in the same common auxiliary set; in row \(i\), the only duplicated small length is \(i\), because of its initial block and the occurrence of \(i\) inside \(P_i\). The used common set includes \(1,\ldots,h\), while \(2h\) is still unused.

Let
\[
n=14h-13.
\]
For every length \(\ell\le n\) that has not yet been used and with \(\ell\ne2h\), append \(\ell\) to every surviving row. Every such \(\ell\) is greater than \(h\), while the endpoint window has width \(h-2\), so each new joint lies strictly to the right of the previous endpoint window; the endpoints remain consecutive and no collision is created.

Finally append \(2h-i\) to row \(i\). Since the endpoint of row \(i\) differs from the leftmost endpoint by \(i-1\), these final blocks align all total row lengths. The common final endpoint is the full sum of the completed permutations, so it is not a proper prefix and is allowed to coincide.

Inside the copy of \(P_i\) in row \(i\), replace the consecutive pair
\[
(i,\,2h-i)
\]
by the single block \(2h\). This preserves total length, deletes one internal joint, introduces no new joint, removes the duplicate occurrences of \(i\) and \(2h-i\), and inserts the previously reserved length \(2h\).

Thus every surviving row is a permutation of \([n]\), and the proper prefix-sum sets of distinct rows are disjoint. Therefore the rows form an \((14h-13)\)-barrycade of height \(h-1\).

## 3. Quantitative consequence

The public v1 construction in arXiv:2609.18476 uses \(n=24h\) for height \(h-1\), giving asymptotic guaranteed density \(1/24\). The construction above gives asymptotic density \(1/14\), a factor
\[
\frac{1/14}{1/24}=\frac{12}{7}\approx1.714
\]
improvement in guaranteed height per symbol.

## 4. Reproducibility

The companion script `scope_barrycade_14h_minus13_verify.py` independently implements the greedy \(x_i\), constructs all rows, verifies that every row is a permutation of \([14h-13]\), and checks pairwise disjointness of all proper prefix-sum sets. It has been run successfully for \(h=2,\ldots,15\) and selected values through \(h=100\).

## Source

M. Dębski, J. Grytczuk, P. Naroski, B. Pawlik, J. Przybyło, M. Śleszyńska-Nowak, *Finite and infinite barrycades*, arXiv:2609.18476v1 (submitted 16 September 2026), https://arxiv.org/abs/2609.18476
