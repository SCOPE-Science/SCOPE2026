# Complete first disparity layer for the Slater and Markov tournament solutions
## Finding
Let \(T=(A,\succ)\) be a finite tournament.

The **Slater set** \(SL(T)\) consists of the maximal alternatives of those linear orders on \(A\) that maximize the number of directed edges on which the order agrees with \(T\).

For the **Markov set**, let \(M\) be the adjacency matrix with
\[
M_{ij}=1
\]
when alternative \(i\) defeats alternative \(j\), and let \(c_i\) be the outdegree of \(i\). For \(|A|>1\), define
\[
N=\frac{M+\operatorname{diag}(c_1,\ldots,c_{|A|})}{|A|-1}.
\]
This matrix is column-stochastic. If \(p\) is its unique stationary probability vector,
\[
Np=p,
\]
then
\[
MA(T)=\arg\max_{i\in A}p_i.
\]

Prior exhaustive work establishes the disparity index
\[
d(SL,MA)=5:
\]
the two tournament solutions agree on every tournament of order at most \(4\), while some tournament of order \(5\) separates them.

The complete first disparity layer is
\[
\#\{T:\ |T|=5,\ SL(T)\ne MA(T)\}=240.
\]
Since there are
\[
2^{\binom52}=1024
\]
labeled five-alternative tournaments, the exact uniform incidence is
\[
\frac{240}{1024}=\frac{15}{64}.
\]

Every strict case has the same set-theoretic direction:
\[
MA(T)\subsetneq SL(T).
\]
Thus the first disparity does not yet produce disjoint or crossing choice sets. Instead the Markov solution strictly refines the Slater choice set.

There are exactly two strict size patterns:
\[
(|SL(T)|,|MA(T)|)=(3,1)
\]
for exactly \(120\) labeled tournaments, and
\[
(|SL(T)|,|MA(T)|)=(2,1)
\]
for exactly \(120\) labeled tournaments.

Up to relabeling, these \(240\) tournaments form exactly two isomorphism classes. Each class has orbit size
\[
120=5!,
\]
so both canonical tournaments have trivial automorphism group.

Using alternatives \(A,B,C,D,E\), a canonical representative of the first class has out-neighborhoods
\[
A\to\{C,E\},\quad
B\to\{A\},\quad
C\to\{B\},\quad
D\to\{A,B,C\},\quad
E\to\{B,C,D\}.
\]
For this tournament,
\[
SL(T)=\{A,D,E\},
\qquad
MA(T)=\{E\},
\]
and the exact stationary vector is
\[
p=\frac1{43}(9,3,1,13,17).
\]

A canonical representative of the second class has out-neighborhoods
\[
A\to\{D,E\},\quad
B\to\{A\},\quad
C\to\{A,B\},\quad
D\to\{B,C\},\quad
E\to\{B,C,D\}.
\]
For this tournament,
\[
SL(T)=\{A,E\},
\qquad
MA(T)=\{E\},
\]
and the exact stationary vector is
\[
p=\left(\frac14,\frac1{12},\frac16,\frac18,\frac38\right).
\]

The full order-\(5\) joint-size census is
\[
\begin{array}{c|c|r}
|SL(T)|&|MA(T)|&\text{labeled tournaments}\\
\hline
1&1&720\\
2&1&120\\
3&1&120\\
3&3&40\\
5&5&24.
\end{array}
\]
The two unequal rows are exactly the two divergent isomorphism classes above.

## Assumptions and scope
A tournament is a complete asymmetric directed graph.

For the one-alternative tournament, both solutions are the unique singleton by convention. For larger tournaments, the Markov matrix is defined exactly as above.

The Slater score of a linear order is the number of tournament arcs oriented forward in that order. Only the maximal alternative of each optimal order contributes to \(SL(T)\).

The theorem exhausts every labeled tournament on one through five alternatives. It does not assert a frequency formula for larger tournaments.

The disparity threshold \(d(SL,MA)=5\) is prior work. The new claim is restricted to the complete labeled and unlabeled structure of the threshold layer.

## Proof
For every order
\[
1\le n\le5,
\]
the verifier enumerates all
\[
2^{\binom n2}
\]
labeled tournaments.

The Slater set is computed independently in two exact ways.

First, all \(n!\) linear orders are enumerated. Each order is scored by the number of tournament arcs pointing forward, and the maximal elements of all score-maximizing orders are collected.

Second, a subset dynamic program computes the largest possible forward-arc count recursively. For each possible first alternative \(i\), its forward arcs to the remaining subset are added to the optimal score of that subset. The alternatives attaining the global optimum are exactly the Slater winners. The two calculations agree on every enumerated tournament.

The Markov set is also computed independently in two exact ways.

First, the rational linear system
\[
(M+\operatorname{diag}(c)-(n-1)I)p=0,
\qquad
\sum_i p_i=1
\]
is solved by exact fraction Gaussian elimination.

Second, the directed matrix-tree theorem is applied to
\[
L=(n-1)I-M-\operatorname{diag}(c).
\]
The diagonal cofactors of \(L\) give integer stationary weights, which are then normalized. These vectors agree exactly with the linear-system solutions for every enumerated tournament.

The number of Slater–Markov disparities by tournament order is
\[
0,\ 0,\ 0,\ 0,\ 240
\]
for orders \(1,2,3,4,5\), respectively.

For every one of the \(240\) five-alternative disparities, the verifier additionally checks
\[
MA(T)\subsetneq SL(T).
\]

Every divergent tournament is canonicalized under all
\[
5!=120
\]
permutations of the alternative labels. Exactly two canonical encodings occur, and each has \(120\) labeled realizations. Direct orbit generation from each canonical representative also produces all \(120\) relabelings, proving that both automorphism groups are trivial.

The exact stationary vectors and choice sets displayed above are then replayed directly for both canonical representatives.

## Verification
The embedded `verify_slater_markov_first_layer.py` uses only the Python standard library and exact integer or rational arithmetic.

It verifies:
- all labeled tournaments on one through five alternatives;
- two independent exact Slater-set computations;
- two independent exact Markov stationary-vector computations;
- equality \(SL(T)=MA(T)\) for every tournament through order \(4\);
- exactly \(240\) disparities at order \(5\);
- exact incidence \(15/64\);
- strict containment \(MA(T)\subsetneq SL(T)\) in every first-layer disparity;
- exactly \(120\) cases with choice-set sizes \((3,1)\);
- exactly \(120\) cases with choice-set sizes \((2,1)\);
- exactly two divergent isomorphism classes;
- orbit size \(120\) and automorphism-group order \(1\) for both classes;
- both displayed canonical tournaments;
- both displayed stationary probability vectors.

Run:

`python3 verify_slater_markov_first_layer.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
The Slater and Markov sets are classical tournament solutions with sharply different constructions: one optimizes a global linear ranking, while the other chooses maxima of a stationary distribution generated by the tournament.

Brandt, Dau, and Seedig define both solutions in a common framework and exhaustively compare tournament solutions on non-isomorphic tournaments of order at most \(10\). Their published disparity/separation table establishes
\[
d(SL,MA)=5
\]
and
\[
s(SL,MA)=6.
\]
Thus the order-\(5\) onset is prior and is not claimed here.

Their paper does not publish a count of the order-\(5\) Slater–Markov disparities or an isomorphism classification of that threshold layer. The exact first layer above sharpens the published threshold by showing that all \(240\) first disparities are still nested,
\[
MA(T)\subsetneq SL(T),
\]
and collapse to only two asymmetric tournament types.

The nesting also explains the gap between the known disparity and separation thresholds at the first layer: order \(5\) can distinguish the two rules, but every such distinction retains the unique Markov winner inside the Slater set.

Targeted searches using both solution names, the order-\(5\) threshold, the exact count \(240\), the fraction \(15/64\), and a two-isomorphism-class formulation did not locate an equivalent published census.

## Limitations
This is a finite classification of the first disparity layer, not a general distribution theorem for random tournaments of arbitrary order.

The earlier exhaustive study necessarily computed the relevant five-alternative tournaments internally; unpublished data or software output from that study could contain the same census even though the inspected paper does not state it.

An unindexed thesis appendix, historical table, or software test corpus could likewise contain an equivalent classification.

No claim is made about the structure or frequency of Slater–Markov disparities beyond order \(5\).

## References
1. F. Brandt, “Minimal Stable Sets in Tournaments,” arXiv:0803.2138, first submitted 14 March 2008.
2. F. Brandt, A. Dau, and H. G. Seedig, “Bounds on the disparity and separation of tournament solutions,” *Discrete Applied Mathematics* 187 (2015), 41–49. DOI: 10.1016/j.dam.2015.01.041.
3. J.-F. Laslier, *Tournament Solutions and Majority Voting*, Springer, 1997.
