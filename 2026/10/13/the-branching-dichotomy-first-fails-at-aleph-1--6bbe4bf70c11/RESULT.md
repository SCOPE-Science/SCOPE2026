# The branching dichotomy first fails at \(\aleph_1\)
## Finding

Let
\[
D=X\sqcup Y,
\qquad
|X|=\aleph_0,
\qquad
|Y|=\aleph_1.
\]
Define
\[
Q=\{A\subseteq D:D\setminus A\text{ is finite}\},
\]
so \(Q\) is the cofinite filter, and define
\[
P_0=\{A\subseteq D:|A\cap X|\ge2\},
\]
\[
P_1=\{A\subseteq D:|A\cap Y|=\aleph_1\},
\qquad
P=P_0\cup P_1.
\]
Then \(P\) and \(Q\) are proper upward monotone unary generalized quantifiers and
\[
P\triangleright Q,
\]
but both branching alternatives fail:
\[
P\cdot Q\ne P\boxtimes Q
\]
and
\[
Q^d\cdot P^d\ne Q^d\boxtimes P^d.
\]

Engström proves that on every countable domain, scope dominance forces at least one of these two equalities. Hence \(\aleph_1\) is exactly the least domain cardinality at which the branching dichotomy can fail.

## Assumptions and scope

For a relation \(R\subseteq D^2\), write
\[
R_x=\{y:(x,y)\in R\}.
\]
For upward monotone quantifiers \(A,B\subseteq\mathcal P(D)\), their iteration and branching product are
\[
A\cdot B
=
\{R\subseteq D^2:\{x:R_x\in B\}\in A\}
\]
and
\[
A\boxtimes B
=
\{R\subseteq D^2:(\exists C\in A)(\exists E\in B)\ C\times E\subseteq R\}.
\]
The dual is
\[
A^d=\{C\subseteq D:D\setminus C\notin A\}.
\]
Scope dominance \(A\triangleright B\) means that every \(A\)-then-\(B\) relation yields the reversed \(B\)-then-\(A\) reading.

The source's central branching question asks whether dominance always forces either
\[
A\cdot B=A\boxtimes B
\]
or the dual upper equality
\[
B^d\cdot A^d=B^d\boxtimes A^d.
\]
It proves a positive answer on countable domains and gives a general counterexample on a domain of size \(\aleph_2\). The result here closes that cardinal gap.

All arguments are in ZFC. No continuum hypothesis or large-cardinal assumption is used.

## Proof

First compute the duals needed below. Since \(Q\) is the cofinite filter,
\[
Q^d=\{A\subseteq D:A\text{ is infinite}\}.
\]
Also
\[
P_0^d
=
\{A\subseteq D:|X\setminus A|\le1\}
\]
and
\[
P_1^d
=
\{A\subseteq D:|Y\setminus A|\le\aleph_0\}.
\]
Therefore
\[
P^d=P_0^d\cap P_1^d
=
\{A\subseteq D:|X\setminus A|\le1\text{ and }|Y\setminus A|\le\aleph_0\}.
\]

### Dominance

The quantifier \(P_0\) is \(\omega\)-small: every member of \(P_0\) contains a two-point subset that is still in \(P_0\). The filter \(Q\) is \(\omega\)-complete, because it is closed under finite intersections. Engström's smallness/completeness lemma gives
\[
P_0\cdot Q=P_0\boxtimes Q,
\]
and hence
\[
P_0\triangleright Q.
\]

Next, \(Q^d\) is \(\omega_1\)-small: every infinite set contains a countably infinite subset. The quantifier \(P_1^d\) is \(\omega_1\)-complete, since the intersection of countably many sets whose complements in \(Y\) are countable again has countable complement in \(Y\). Applying the same lemma gives
\[
Q^d\cdot P_1^d=Q^d\boxtimes P_1^d.
\]
Thus
\[
Q^d\triangleright P_1^d,
\]
and duality gives
\[
P_1\triangleright Q.
\]

Dominance is preserved under unions of outer quantifiers. Since
\[
P=P_0\cup P_1,
\]
we obtain
\[
P\triangleright Q.
\]

### Failure of the lower branching equality

Define \(R\subseteq D^2\) by
\[
R_y=D\setminus\{y\}\quad(y\in Y),
\qquad
R_x=\varnothing\quad(x\in X).
\]
Every row indexed by \(Y\) is cofinite, and
\[
Y\in P_1\subseteq P.
\]
Hence
\[
R\in P\cdot Q.
\]

Suppose that a branching rectangle existed:
\[
A\times B\subseteq R,
\qquad
A\in P,
\qquad
B\in Q.
\]
Because \(B\ne\varnothing\), the empty rows indexed by \(X\) force
\[
A\subseteq Y.
\]
Thus \(A\notin P_0\), so \(A\in P_1\) and therefore
\[
|A|=\aleph_1.
\]
Since \(B\) is cofinite, choose
\[
y\in A\cap B.
\]
Then \((y,y)\in A\times B\), but \((y,y)\notin R\), a contradiction. Therefore
\[
R\notin P\boxtimes Q.
\]
So the lower equality fails.

### Failure of the upper branching equality

Choose pairwise distinct points
\[
x_n\in X,
\qquad
k_n\in Y
\qquad(n\in\omega),
\]
and put
\[
K=\{k_n:n\in\omega\}.
\]
Define \(S\subseteq D^2\) by
\[
S_{k_n}=D\setminus\{x_n\}
\qquad(n\in\omega),
\]
and
\[
S_z=\varnothing
\qquad(z\notin K).
\]
Each special row belongs to \(P^d\): it omits exactly one point of \(X\) and no point of \(Y\). The set of \(P^d\)-large rows is exactly \(K\), which is infinite and hence belongs to \(Q^d\). Thus
\[
S\in Q^d\cdot P^d.
\]

Suppose
\[
C\times B\subseteq S,
\qquad
C\in Q^d,
\qquad
B\in P^d.
\]
Every member of \(P^d\) is nonempty, so the empty rows force
\[
C\subseteq K.
\]
Because \(C\in Q^d\), the set \(C\) is infinite. Hence \(B\) must lie inside
\[
\bigcap_{k_n\in C}(D\setminus\{x_n\}).
\]
Consequently \(B\) omits infinitely many points of \(X\), contradicting the defining condition
\[
|X\setminus B|\le1
\]
for membership in \(P^d\). Therefore
\[
S\notin Q^d\boxtimes P^d.
\]
So the upper equality fails.

### Minimality

Engström's Theorem 6.1 proves that on every countable domain, for proper upward monotone quantifiers, scope dominance is equivalent to the disjunction of the lower and upper branching equalities. The earlier theorem of Altman, Peterzil, and Winter gives the corresponding complete countable-domain characterization in their FIN/DCC language.

Thus no finite or countably infinite domain supports a counterexample to the branching dichotomy. The construction above works on a domain of size \(\aleph_1\). Therefore the exact least possible domain cardinality is
\[
\aleph_1.
\]

## Verification

The proof was reconstructed directly from the definitions of iteration, branching product, duality, and scope dominance.

The four nonstandard source inputs were checked in the full primary text:

1. if an outer quantifier is \(\kappa\)-small and the inner quantifier is \(\kappa\)-complete, iteration equals the branching product;
2. scope dominance is preserved by duality;
3. scope dominance is preserved by unions of outer quantifiers;
4. on countable domains, dominance forces one of the two branching equalities.

The cardinal arithmetic used in the new construction is only that a countable union of countable sets is countable. The two non-equality claims are proved by explicit relations, not by finite experiments or search exhaustion.

The dual calculations were checked symbolically:
\[
Q^d=\{A:A\text{ is infinite}\},
\]
\[
P_0^d=\{A:|X\setminus A|\le1\},
\]
\[
P_1^d=\{A:|Y\setminus A|\le\aleph_0\},
\]
and
\[
P^d=P_0^d\cap P_1^d.
\]

## Relationship to prior work

Altman, Peterzil, and Winter characterize scope dominance for upward monotone quantifiers on countable domains. Their result supplies the countable side of the minimum-cardinality boundary.

Engström reformulates the countable characterization in branching-product language and asks whether dominance always forces one of the lower or upper branching equalities. His Theorem 7.2 answers negatively in ZFC by an explicit construction on a domain of cardinality \(\aleph_2\). That construction also combines two outer quantifiers whose dominance mechanisms use opposite branching alternatives.

The present construction uses the same general union mechanism but changes both the small component and the inner filter. The finite-witness component
\[
P_0=\{A:|A\cap X|\ge2\}
\]
works against the cofinite filter, while the dual side needs only countably many special rows. This lowers the domain from \(\aleph_2\) to \(\aleph_1\), and the countable theorem proves that no further lowering is possible.

Targeted searches using the phrases “scope dominance,” “branching product,” “branching dichotomy,” “\(\aleph_1\),” “least uncountable domain,” and equivalent cutoff formulations located the 2005 countable theorem and the 2026 \(\aleph_2\) counterexample, but no statement of an \(\aleph_1\) counterexample or the exact minimum-cardinality theorem.

## Limitations

The theorem concerns arbitrary proper upward monotone local quantifiers. It does not lower the consistency strength of the much more rigid two-filter counterexample problem; here only \(Q\) is a filter.

The construction deliberately uses a distinguished partition \(D=X\sqcup Y\), so it is not a permutation-invariant generalized quantifier construction.

The result identifies the first domain cardinal at which the general branching dichotomy fails; it does not classify all dominance pairs on \(\aleph_1\).

Because the motivating preprint is very recent, a later revision could independently record the same cardinal sharpening. The originality claim is restricted to the checked literature state and the exact theorem proved above.

## References

[1] Fredrik Engström, “Generalized Quantifiers: Scope Dominance and Branching,” arXiv:2609.31243v1, first posted 25 September 2026.

[2] Alon Altman, Ya'acov Peterzil, and Yoad Winter, “Scope Dominance with Upward Monotone Quantifiers,” *Journal of Logic, Language and Information* 14 (2005), 445–455, DOI:10.1007/s10849-005-4960-6.
