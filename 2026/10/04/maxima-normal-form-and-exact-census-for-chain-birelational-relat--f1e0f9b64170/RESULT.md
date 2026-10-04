# Maxima normal form and exact census for chain birelational relations
## Finding

Becker--Das--Marin--Padhiar define the intuitionistic tense semantics of their second-order system on a partial order
\[
(W,\le)
\]
equipped with an accessibility relation \(R\) satisfying two interaction conditions. In their terminology, \(R\) is a **bisimulation on** \(\le\).

On a finite intuitionistic chain these two quantified conditions admit an exact one-dimensional normal form.

Let
\[
C_n=\{0<1<\cdots<n-1\},
\]
and let
\[
R\subseteq C_n\times C_n.
\]

For every row define
\[
a_i=
\begin{cases}
\max\{j:iRj\},&\text{if the row is nonempty},\\
-1,&\text{if the row is empty},
\end{cases}
\]
and for every column define
\[
b_j=
\begin{cases}
\max\{i:iRj\},&\text{if the column is nonempty},\\
-1,&\text{if the column is empty}.
\end{cases}
\]

Then the two source conditions hold **if and only if**
\[
a_0\le a_1\le\cdots\le a_{n-1}
\]
and
\[
b_0\le b_1\le\cdots\le b_{n-1}.
\]

Thus, on a chain, the entire frame condition is equivalent to monotonicity of the rightmost \(1\) in each row and the bottommost \(1\) in each column, with \(-1\) recording an empty row or column.

There is also an exact reconstruction and enumeration.

Fix nondecreasing
\[
a,b\in\{-1,0,\ldots,n-1\}^n.
\]
A relation with these exact row and column maxima exists if and only if
\[
i\le b_{a_i}
\qquad\text{whenever }a_i\ge0,
\]
and
\[
j\le a_{b_j}
\qquad\text{whenever }b_j\ge0.
\]

For such an admissible pair define
\[
A(a,b)=
\{(i,j):j\le a_i\text{ and }i\le b_j\}
\]
and
\[
F(a,b)=
\{(i,a_i):a_i\ge0\}
\cup
\{(b_j,j):b_j\ge0\}.
\]

Then
\[
\boxed{
R\text{ has maxima }(a,b)
\iff
F(a,b)\subseteq R\subseteq A(a,b).
}
\]

Consequently the number of relations with fixed maxima \((a,b)\) is
\[
2^{|A(a,b)|-|F(a,b)|}.
\]

Writing \(\mathcal P_n\) for the admissible nondecreasing pairs, the exact census is
\[
\boxed{
N_n=
\sum_{(a,b)\in\mathcal P_n}
2^{|A(a,b)|-|F(a,b)|}.
}
\]

The first values are
\[
\boxed{
N_1=2,\quad
N_2=9,\quad
N_3=118,\quad
N_4=4849,\quad
N_5=697066,\quad
N_6=378458905.
}
\]

This gives both a structural normal form and an exact finite search-space formula for the accessibility relations in the new second-order intuitionistic tense semantics when the intuitionistic reduct is a chain.

## Assumptions and scope

The frame condition is exactly Definition 3.1 of the source. On a partial order \((W,\le)\), the accessibility relation \(R\) must satisfy:

\[
vRw\le w'
\Longrightarrow
\exists v'\ge v\;v'Rw',
\]
and
\[
v'\ge vRw
\Longrightarrow
\exists w'\ge w\;v'Rw'.
\]

The theorem specializes only these relational conditions to the fixed finite chain \(C_n\).

The result does not classify the domains of predicates used for second-order quantification, valuations, comprehensive structures, or formula validity. It therefore does not by itself give a finite-model property for the second-order logic.

The count is for relations on the labelled chain. A finite chain has only the identity order automorphism, so the same count is also the number of isomorphism classes of expansions of that fixed ordered set.

The empty relation is allowed by Definition 3.1 and is included in the census.

## Proof

We prove the two monotonicity equivalences separately.

### The row condition

Suppose the second source condition holds:
\[
v'\ge vRw
\Longrightarrow
\exists w'\ge w\;v'Rw'.
\]

Take
\[
i\le i'.
\]

If row \(i\) is empty, then
\[
a_i=-1\le a_{i'}
\]
automatically.

Otherwise
\[
iRa_i.
\]
Applying the source condition with
\[
v=i,\qquad v'=i',\qquad w=a_i
\]
gives some
\[
w'\ge a_i
\]
with
\[
i'Rw'.
\]
Thus row \(i'\) is nonempty and
\[
a_{i'}\ge w'\ge a_i.
\]

Hence
\[
a_0\le a_1\le\cdots\le a_{n-1}.
\]

Conversely, assume \((a_i)\) is nondecreasing. Suppose
\[
i'\ge iRj.
\]
Then
\[
a_i\ge j.
\]
By monotonicity,
\[
a_{i'}\ge a_i\ge j.
\]
The row \(i'\) is therefore nonempty, and its rightmost point
\[
w'=a_{i'}
\]
satisfies
\[
w'\ge j
\]
and
\[
i'Rw'.
\]

So the second source condition is equivalent to monotonicity of the row maxima.

### The column condition

The first source condition is
\[
vRw\le w'
\Longrightarrow
\exists v'\ge v\;v'Rw'.
\]

Applying the preceding argument to columns gives the exact dual statement:
\[
b_0\le b_1\le\cdots\le b_{n-1}.
\]

Explicitly, if
\[
j\le j'
\]
and column \(j\) is nonempty, then
\[
b_jRj.
\]
The first source condition supplies some
\[
i'\ge b_j
\]
with
\[
i'Rj',
\]
so
\[
b_{j'}\ge i'\ge b_j.
\]

Conversely, if the column maxima are nondecreasing and
\[
iRj\le j',
\]
then
\[
b_j\ge i
\]
and therefore
\[
b_{j'}\ge b_j\ge i.
\]
Taking
\[
i'=b_{j'}
\]
gives the required witness.

This proves the maxima normal form.

### Reconstructing a relation from its maxima

Fix nondecreasing sequences
\[
a,b\in\{-1,0,\ldots,n-1\}^n.
\]

If \(R\) has these row and column maxima, every edge \((i,j)\in R\) must satisfy
\[
j\le a_i
\]
and
\[
i\le b_j.
\]
Therefore
\[
R\subseteq A(a,b).
\]

Also, whenever
\[
a_i\ge0,
\]
the row maximum itself must occur:
\[
(i,a_i)\in R.
\]
Likewise, whenever
\[
b_j\ge0,
\]
the column maximum must occur:
\[
(b_j,j)\in R.
\]
Thus
\[
F(a,b)\subseteq R.
\]

The forced cells are legal exactly when
\[
(i,a_i)\in A(a,b)
\]
for every nonempty row and
\[
(b_j,j)\in A(a,b)
\]
for every nonempty column.

These conditions reduce respectively to
\[
i\le b_{a_i}
\]
and
\[
j\le a_{b_j}.
\]

Hence they are precisely the displayed admissibility conditions.

Now suppose the pair \((a,b)\) is admissible and choose any relation satisfying
\[
F(a,b)\subseteq R\subseteq A(a,b).
\]

If
\[
a_i=-1,
\]
then row \(i\) contains no allowed cell, so it is empty.

If
\[
a_i\ge0,
\]
the forced cell \((i,a_i)\) is present, while \(A(a,b)\) contains no cell to its right. Thus the exact row maximum is \(a_i\).

The same argument shows that every exact column maximum is \(b_j\).

Therefore every intermediate relation has maxima \((a,b)\), and every relation with those maxima is obtained uniquely in this way.

There are
\[
|A(a,b)|-|F(a,b)|
\]
unforced allowed cells, each independently present or absent. This gives
\[
2^{|A(a,b)|-|F(a,b)|}
\]
relations for the fixed pair.

Finally, every admissible relation has one unique maxima pair. Summing over all admissible nondecreasing pairs proves the census formula.

## Verification

The bundled checker performs two independent calculations.

First, for
\[
1\le n\le4,
\]
it enumerates every one of the
\[
2^{n^2}
\]
binary relations on the chain and tests the two conditions of Definition 3.1 literally, with their existential witnesses.

It independently computes the row and column maxima and checks their monotonicity. The two predicates agree for every relation.

The resulting direct counts are
\[
2,\ 9,\ 118,\ 4849.
\]

Second, through
\[
n=6,
\]
the checker enumerates all nondecreasing maxima sequences, tests the two compatibility inequalities, forms \(A(a,b)\) and \(F(a,b)\), and sums
\[
2^{|A(a,b)|-|F(a,b)|}.
\]

It obtains
\[
2,\ 9,\ 118,\ 4849,\ 697066,\ 378458905.
\]

For
\[
n\le4,
\]
the formula counts agree exactly with the direct relation-level exhaustive census.

The script prints `VERIFY_OK`.

## Relationship to prior work

Becker--Das--Marin--Padhiar develop second-order intuitionistic tense logic and use a standard birelational semantics following Fischer Servi, Ewald, and Simpson. Their Definition 3.1 gives the two interaction conditions above and calls \(R\) a bisimulation on the intuitionistic order.

The checked full text does not specialize these conditions to finite chains, characterize them by row and column extrema, or enumerate the resulting accessibility relations. Its occurrences of “chain” concern proof-search chains rather than linearly ordered Kripke frames.

Davoren's earlier topological study identifies Fischer Servi's two interaction conditions with lower semicontinuity of the relation and its inverse in the corresponding topology. That gives a broad semantic reformulation but does not provide the finite-chain maxima normal form or an exact relation census.

Related work on finite birelational frames establishes finite-model properties for particular intuitionistic modal logics, but the checked sources do not give the exact chain parameterization above.

Targeted searches for finite-chain birelational frames, stable relations on chains, row/column-maxima formulations, Egli--Milner-style aliases, and the initial numerical census did not locate an equivalent statement.

## Limitations

The theorem uses totality of the intuitionistic order essentially. For a general finite partial order, one row or column need not have a single extremal witness that summarizes the corresponding interaction condition.

The census concerns only accessibility relations satisfying Definition 3.1. It does not count predicate domains, valuations, comprehensive models, or formulas.

The exact finite sum is not simplified here to a known closed-form sequence or recurrence.

The first six values are proved by the exact formula, but no asymptotic estimate for \(N_n\) is claimed.

An equivalent enumeration may exist in the combinatorics of monotone set-valued maps or order-compatible binary relations under terminology unrelated to intuitionistic modal logic; no such identification was located in the checked searches.

## References

[1] Justus Becker, Anupam Das, Sonia Marin, and Paaras Padhiar, “The proof theory and semantics of second-order (intuitionistic) tense logic,” arXiv:2602.06253, first posted 5 February 2026.

[2] Jennifer M. Davoren, “On intuitionistic modal and tense logics and their classical companion logics: Topological semantics and bisimulations,” *Annals of Pure and Applied Logic* 161 (2010), 349–367. DOI:10.1016/j.apal.2009.07.009.

[3] Alex K. Simpson, *The Proof Theory and Semantics of Intuitionistic Modal Logic*, PhD thesis, University of Edinburgh, 1994.
