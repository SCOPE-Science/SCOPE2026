# Exact factor-two homogeneity defect of Pouzet’s weak Fraïssé order reduct

## Finding
Let \(M=(\mathbb Q,R)\), where
\[
R(x,y,z)\quad\Longleftrightarrow\quad x<y\land x<z\land y\ne z.
\]
For \(n\ge1\), let \(p_n\) be the number of complete \(\emptyset\)-types realized by ordered \(n\)-tuples of \(M\), and let \(q_n\) be the number of realized quantifier-free \(n\)-types. Writing
\[
F_n=\sum_{k=1}^n {n\brace k}k!
\]
for the ordered Bell (Fubini) number, one has
\[
p_n=F_n,\qquad q_n=\frac{F_n+1}2.
\]
Every quantifier-free type with at least two distinct coordinate values splits into exactly two complete types; the two completions differ only by reversing the top two distinct value-blocks. The constant quantifier-free type does not split. In particular, for injective ordered \(n\)-tuples the complete-type count is \(n!\), while the quantifier-free-type count is \(n!/2\) for \(n\ge2\). Finally, among finite \(\emptyset\)-definable relational expansions that homogenize \(M\), the least possible maximum arity of an added relation is exactly \(2\).

## Assumptions and scope
The structure is the Pouzet example studied by Krawczyk, Kruckman, Kubiś, and Panagiotopoulos. Their paper records that \(<\) is existentially definable in \(M\), that \(M\) is weakly homogeneous but not homogeneous, and that adding the definable order produces the homogeneous expansion \((\mathbb Q,R,<)\). The counts here concern ordered tuples, with repetitions allowed unless explicitly stated otherwise.

## Proof
Because \(<\) is definable in \(M\), every automorphism of \(M\) preserves \(<\); conversely every order automorphism preserves \(R\). Thus
\[
\operatorname{Aut}(M)=\operatorname{Aut}(\mathbb Q,<).
\]
The orbits of this group on ordered \(n\)-tuples are exactly weak orders on the coordinate set: first partition the coordinates into equality blocks, then linearly order those blocks. If there are \(k\) blocks, there are \({n\brace k}k!\) possibilities. Summing over \(k\) gives \(p_n=F_n\).

Now fix an equality pattern with \(k\) distinct value-blocks. Atomic \(R\)-information on three distinct blocks records exactly which of the three is least. Suppose the blocks are linearly ordered from bottom to top as \(B_1<\cdots<B_k\). The block \(B_i\) occurs as the least member of exactly
\[
\binom{k-i}2
\]
three-block subsets. These numbers are pairwise distinct for \(i=1,\ldots,k-2\), while the top two blocks both occur zero times. Hence the full order of the blocks is recovered from the quantifier-free \(R\)-diagram except for the order of the top two. Conversely, exchanging the top two blocks changes no equality statement and no least-element-of-a-triple statement, so it changes no atomic or quantifier-free formula. Therefore each equality pattern with \(k\ge2\) has exactly \(k!/2\) realized quantifier-free types, each with exactly two complete-type completions. For \(k=1\) there is one quantifier-free type and one complete type. Thus
\[
q_n=1+\frac12\sum_{k=2}^n {n\brace k}k!
=\frac{F_n+1}2.
\]
When the tuple is injective, \(k=n\), giving the stated \(n!\) versus \(n!/2\) counts.

It remains to identify the least homogenizing arity. A binary relation suffices: the definable expansion by \(<\) is homogeneous. Unary relations cannot suffice. The automorphism group of \(M\) is transitive on \(\mathbb Q\), so every \(\emptyset\)-definable unary relation is either empty or all of \(\mathbb Q\). Adding finitely many such relations adds no information. Since \(M\) itself is not homogeneous, no unary definable expansion can homogenize it. Therefore the minimum possible maximum arity is \(2\).

## Verification
A self-contained verifier enumerates every weak order on \(n\) labeled coordinates for \(1\le n\le6\), computes its complete atomic \(R\)-signature together with equality, and groups weak orders by that signature. It reproduces
\[
F_n=1,3,13,75,541,4683
\]
and
\[
q_n=1,2,7,38,271,2342,
\]
with exactly one singleton signature class (the constant tuple) and every other signature class of size two. It also checks the injective counts through \(n=6\). The finite replay is a check of the combinatorial classification, not a substitute for the all-\(n\) proof above.

## Relationship to prior work
Krawczyk, Kruckman, Kubiś, and Panagiotopoulos introduce this exact structure and explicitly identify the mechanism behind non-homogeneity: exchanging the two greatest elements of a finite tuple preserves all quantifier-free formulas but fails to preserve the existentially definable order. They also note that the expansion by \(<\) is homogeneous. The present result sharpens that qualitative mechanism into an exact all-arity classification: every nonconstant quantifier-free type has defect exactly two, yielding the closed profile \((F_n+1)/2\), and it identifies binary arity as minimal for definable homogenization. Ahlman's earlier work supplies the general notion of homogenizable structure. Exact-phrase, implication-shaped, and semantic-index searches located no source stating these enumerative or minimal-arity conclusions.

## Limitations
The key top-two ambiguity is already visible in the 2019 source; the contribution here is the exact global enumeration, uniform two-to-one splitting statement, and minimal homogenizing-arity consequence, not a new obstruction mechanism. The originality search cannot exclude unpublished or unindexed folklore. The result is specific to this reduct and does not classify arbitrary weakly homogeneous structures.

## References
1. Adam Krawczyk, Alex Kruckman, Wiesław Kubiś, and Aristotelis Panagiotopoulos, *Examples of weak amalgamation classes*, arXiv:1907.09577 (first posted 2019-07-22), especially the discussion of Pouzet's example and homogenizability.
2. Ove Ahlman, *Homogenizable structures and model completeness*, arXiv:1601.07304 (first posted 2016-01-27).
3. The ordered Bell/Fubini numbers count weak orders on a labeled finite set; equivalently \(F_n=\sum_{k=1}^n {n\brace k}k!\).
