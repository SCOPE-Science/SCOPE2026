# Complete seven-alternative Banks–uncovered disparity census
## Finding
Let \(T\) be a finite tournament. The **Banks set** \(BA(T)\) consists of the maximal elements of inclusion-maximal transitive subtournaments. The **uncovered set** \(UC(T)\) consists of the alternatives that are not covered, where \(y\) covers \(x\) when \(y\) defeats \(x\) and every alternative defeated by \(x\) is also defeated by \(y\).

It is classical that
\[
BA(T)\subseteq UC(T),
\]
that equality holds for every tournament on at most \(6\) alternatives, and that order \(7\) is the first order where strict inclusion can occur.

The complete first-disparity layer is as follows. Among all
\[
2^{\binom72}=2^{21}=2097152
\]
labeled tournaments on seven alternatives, exactly
\[
13440
\]
satisfy
\[
BA(T)\subsetneq UC(T).
\]
Thus, under the uniform distribution on labeled seven-vertex tournaments, the exact disparity probability is
\[
\frac{13440}{2097152}=\frac{105}{16384}.
\]

Every divergent tournament has
\[
|UC(T)|=|BA(T)|+1.
\]
The complete strict size-pair census is
\[
\begin{array}{c|r}
(|BA(T)|,|UC(T)|) & \text{labeled tournaments}\\ \hline
(3,4) & 1680\\
(4,5) & 5040\\
(5,6) & 5040\\
(6,7) & 1680
\end{array}
\]

Up to relabeling, these \(13440\) tournaments form exactly four isomorphism classes: one class for each of the four size pairs above. Their labeled orbit sizes are respectively
\[
1680,\qquad5040,\qquad5040,\qquad1680.
\]

A canonical representative for each class is given below by its out-neighbor sets, with alternatives numbered \(1,\ldots,7\).

For the \((3,4)\) class:
\[
\begin{aligned}
1&\to\{2,3,5,7\},&
2&\to\{3,7\},&
3&\to\{4,6\},\\
4&\to\{1,2\},&
5&\to\{2,3,4\},&
6&\to\{1,2,4,5\},\\
7&\to\{3,4,5,6\},
\end{aligned}
\]
with
\[
BA=\{1,6,7\},
\qquad
UC=\{1,5,6,7\}.
\]

For the \((4,5)\) class:
\[
\begin{aligned}
1&\to\{2,7\},&
2&\to\{3,6\},&
3&\to\{1,5\},\\
4&\to\{1,2,3\},&
5&\to\{1,2,4\},&
6&\to\{1,3,4,5\},\\
7&\to\{2,3,4,5,6\},
\end{aligned}
\]
with
\[
BA=\{1,5,6,7\},
\qquad
UC=\{1,4,5,6,7\}.
\]

For the \((5,6)\) class:
\[
\begin{aligned}
1&\to\{3,7\},&
2&\to\{1,6\},&
3&\to\{2,5\},\\
4&\to\{1,2,3\},&
5&\to\{1,2,4\},&
6&\to\{1,3,4,5\},\\
7&\to\{2,3,4,5,6\},
\end{aligned}
\]
with
\[
BA=\{1,2,5,6,7\},
\qquad
UC=\{1,2,4,5,6,7\}.
\]

For the \((6,7)\) class:
\[
\begin{aligned}
1&\to\{2,3,5,7\},&
2&\to\{4,7\},&
3&\to\{2,6\},\\
4&\to\{1,3\},&
5&\to\{2,3,4\},&
6&\to\{1,2,4,5\},\\
7&\to\{3,4,5,6\},
\end{aligned}
\]
with
\[
BA=\{1,2,3,4,6,7\},
\qquad
UC=\{1,2,3,4,5,6,7\}.
\]

Hence the first possible Banks–uncovered disparity is not a heterogeneous collection of small exceptions. It consists of exactly four unlabeled tournament types, and strict inclusion always deletes exactly one uncovered alternative.

## Assumptions and scope
A tournament is a complete asymmetric directed graph. The Banks and uncovered sets are used in their standard tournament-solution definitions.

The census includes every labeled tournament on seven alternatives. Isomorphism means equality up to a permutation of the seven alternatives.

The lower-order equality statement is independently replayed for all tournaments of orders \(1,\ldots,6\), but it is also established in the prior literature and is not claimed as new.

The new finite claim is the complete order-seven census and isomorphism classification. No statement is made about disparity frequencies for tournaments of order \(8\) or higher.

## Proof
For a fixed labeled tournament \(T\), the uncovered set is computed directly from out-neighbor containment. An alternative \(x\) is covered if some \(y\) defeats \(x\) and satisfies
\[
N^+(x)\subseteq N^+(y).
\]

The Banks set is computed by enumerating every vertex subset. A subset is transitive exactly when it has a vertex that defeats every other vertex in the subset and whose deletion leaves a transitive subset. This recursive characterization gives an exact dynamic program for transitivity. A transitive subset is inclusion-maximal when no outside vertex can be added while preserving transitivity. Its unique maximal element contributes to \(BA(T)\).

The verifier exhausts every labeled tournament for orders \(1,\ldots,7\). It checks the classical inclusion
\[
BA(T)\subseteq UC(T)
\]
on every tournament. No disparity occurs through order \(6\).

At order \(7\), the complete \(2^{21}\)-tournament census gives the joint size histogram
\[
\begin{array}{c|r}
(|BA|,|UC|) & \text{count}\\ \hline
(1,1)&229376\\
(3,3)&402640\\
(3,4)&1680\\
(4,4)&525840\\
(4,5)&5040\\
(5,5)&486528\\
(5,6)&5040\\
(6,6)&330960\\
(6,7)&1680\\
(7,7)&108368.
\end{array}
\]
The four strict cells sum to
\[
1680+5040+5040+1680=13440.
\]

Every divergent labeled tournament is then canonicalized under all
\[
7!=5040
\]
vertex permutations. Exactly four canonical representatives occur. Their orbit sizes are
\[
5040,\quad5040,\quad1680,\quad1680,
\]
which sum to \(13440\). Matching them to the four strict size cells shows that there is exactly one isomorphism class for each of
\[
(3,4),\quad(4,5),\quad(5,6),\quad(6,7).
\]

An independent Python implementation recomputes the Banks and uncovered sets for the four canonical representatives directly from their tournament relations, confirming the displayed choice sets.

## Verification
The embedded `verify_banks_uncovered_first_layer.c` performs the exhaustive labeled census using exact bit operations and no external libraries.

It verifies:
- every tournament of orders \(1,\ldots,7\);
- the inclusion \(BA(T)\subseteq UC(T)\) throughout the tested domain;
- no Banks–uncovered disparity for orders at most \(6\);
- exactly \(13440\) divergent seven-alternative tournaments;
- the full order-seven joint size histogram;
- the exact fraction \(105/16384\);
- exactly four isomorphism classes among the divergent tournaments;
- orbit sizes \(5040,5040,1680,1680\).

Compile and run:

`cc -O3 -std=c11 verify_banks_uncovered_first_layer.c -o verify_banks_uncovered_first_layer`

`./verify_banks_uncovered_first_layer`

The terminal output must contain `VERIFY_OK`.

The embedded `verify_banks_uncovered_canons.py` is an independent direct checker for the four canonical representatives. It reconstructs transitive subsets recursively and the covering relation directly, then verifies the Banks and uncovered sets displayed in the finding.

Run:

`python3 verify_banks_uncovered_canons.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Banks introduced the tournament solution now bearing his name. Miller, Grofman, and Feld proved that every Banks alternative is uncovered and reported that the Banks and uncovered sets coincide whenever the tournament has at most six alternatives, while strict inclusion can occur from seven alternatives onward.

Brandt, Dau, and Seedig later performed an exhaustive computer analysis of roughly ten million non-isomorphic tournaments of order at most ten. In their discussion of the Banks and uncovered sets they again identify order seven as the first possible disparity and exhibit a minimal seven-alternative example with
\[
|BA|=3,\qquad |UC|=4.
\]
Their published table records disparity indices over orders \(5\) through \(10\), but it does not provide the complete order-seven count of divergent labeled tournaments or an isomorphism census of the first disparity layer.

The contribution here is therefore not the order-seven threshold itself. It is the exact classification of the whole first layer: \(13440\) labeled tournaments, probability \(105/16384\), strict size-pair counts \(1680,5040,5040,1680\), and exactly four unlabeled classes.

## Limitations
The result is a complete finite classification at order \(7\), not a general formula for larger tournament orders.

The isomorphism census is obtained by direct relabeling under all \(7!\) permutations rather than by invoking a separate graph-isomorphism package.

The originality search did not locate the exact \(13440\) count, the probability \(105/16384\), or the four-class first-layer census. An unindexed historical note, data file, thesis, or unpublished output from earlier exhaustive searches could contain an equivalent enumeration.

The original 1984 Banks working paper is represented in the checked institutional archive by metadata and a publication notice rather than the full historical manuscript. The scientific comparison with prior coverage therefore relies primarily on later full-text sources that explicitly state the inclusion and first-disparity threshold.

## References
1. J. S. Banks, “Sophisticated Voting Outcomes and Agenda Control,” California Institute of Technology Social Science Working Paper 524, 1984; later *Social Choice and Welfare* 1 (1985), 295–306. DOI: 10.1007/BF00649265.
2. N. R. Miller, B. Grofman, and S. L. Feld, “The Structure of the Banks Set,” *Public Choice* 66 (1990), 243–251. DOI: 10.1007/BF00125776.
3. F. Brandt, “Minimal Stable Sets in Tournaments,” arXiv:0803.2138, first submitted 14 March 2008.
4. F. Brandt, A. Dau, and H. G. Seedig, “Bounds on the disparity and separation of tournament solutions,” *Discrete Applied Mathematics* 187 (2015), 41–49. DOI: 10.1016/j.dam.2015.01.041.
5. H. Moulin, “Choosing from a tournament,” *Social Choice and Welfare* 3 (1986), 271–291. DOI: 10.1007/BF00292732.
