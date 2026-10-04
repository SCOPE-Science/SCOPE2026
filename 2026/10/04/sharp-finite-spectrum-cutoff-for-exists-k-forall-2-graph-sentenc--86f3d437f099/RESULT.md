# Sharp finite-spectrum cutoff for \(\exists^k\forall^2\) graph sentences

## Finding
Let
\[
\Phi=\exists x_1\cdots\exists x_k\,\forall y\,\forall z\,\psi(\bar x,y,z)
\]
be a first-order sentence in the language of finite simple undirected graphs, where \(\psi\) is quantifier-free. If \(\Phi\) has a finite model with more than
\[
k+2^k
\]
vertices, then \(\Phi\) has a finite model of every order \(n\ge k+2\). Consequently every such sentence has either finite spectrum with maximum at most \(k+2^k\), or a cofinite spectrum containing every integer from \(k+2\) onward.

The finite-spectrum bound is sharp for every \(k\ge0\). For \(k\ge1\), the sentence asserting that the witnesses \(x_1,\ldots,x_k\) are distinct and that no two vertices outside the witness set have the same adjacency pattern to all witnesses has spectrum
\[
\{k,k+1,\ldots,k+2^k\}.
\]
For \(k=0\), the sentence \(\forall y\forall z\,(y=z)\) has the unique nonempty spectrum value \(1=2^0\).

Thus \(k+2^k\) is the exact largest possible endpoint of a finite spectrum in the \(\exists^k\forall^2\) graph prefix class.

## Assumptions and scope
Graphs are finite, nonempty, simple, and undirected, with adjacency and equality in the vocabulary. Existential variables are allowed to take equal values. The result concerns spectra by graph order, not formula length or satisfiability complexity. The bound is parameterized by the number \(k\) of existential quantifiers and uses exactly two universal variables.

## Proof
Assume \(G\models\Phi\) and fix a witnessing tuple \(\bar a=(a_1,\ldots,a_k)\). Let \(U\) be the set of distinct values occurring in \(\bar a\), and put \(u=|U|\le k\). If
\[
|G|>k+2^k,
\]
then
\[
|G\setminus U|>2^u.
\]
Every vertex outside \(U\) has one of only \(2^u\) adjacency vectors to \(U\). Hence there are distinct \(b,c\in G\setminus U\) with the same adjacency vector to \(U\).

Let \(H=G[U\cup\{b,c\}]\). Because \(H\) is an induced subgraph containing all witness values and \(\psi\) is quantifier-free, \(H\models\Phi\) with the same witness tuple. The vertices \(b\) and \(c\) have identical adjacency to \(U\), so interchanging them while fixing \(U\) is an automorphism of \(H\).

For any integer \(t\ge2\), replace \(b,c\) by a set \(C\) of \(t\) clones. Each clone has the same adjacency to \(U\) as \(b\), and two distinct clones are adjacent exactly when \(b\) and \(c\) are adjacent in \(H\). Call the resulting graph \(H_t\). Every ordered pair assigned to \((y,z)\) in \(H_t\) has the same atomic type over the witness tuple as one of four kinds of pairs already present in \(H\): two vertices of \(U\); one vertex of \(U\) with \(b\); the diagonal pair \((b,b)\); or the distinct pair \((b,c)\). Therefore the quantifier-free matrix \(\psi\) has the same truth value on every required assignment, and \(H_t\models\Phi\).

Now fix \(n\ge k+2\) and take \(t=n-u\). Since \(u\le k\), we have \(t\ge2\), and \(|H_t|=u+t=n\). Hence every order \(n\ge k+2\) lies in the spectrum.

For sharpness, when \(k\ge1\) use
\[
\Theta_k=\exists x_1\cdots\exists x_k\,\forall y\,\forall z\;\Bigg(
\bigwedge_{i<j}x_i\ne x_j\;\wedge\;
\Big[
\big((\bigwedge_i y\ne x_i)\wedge(\bigwedge_i z\ne x_i)\wedge
\bigwedge_i(E(y,x_i)\leftrightarrow E(z,x_i))\big)
\rightarrow y=z
\Big]\Bigg).
\]
The witnesses are distinct, and the implication says that vertices outside the witness set have pairwise distinct \(k\)-bit adjacency vectors to the witnesses. Thus there are at most \(2^k\) outside vertices, giving order at most \(k+2^k\). Conversely, for every \(m\in\{0,\ldots,2^k\}\), choose \(m\) distinct bit vectors and realize them as the witness-adjacency patterns of \(m\) outside vertices; arbitrary remaining edges complete a model of order \(k+m\). This proves sharpness.

## Verification
The proof was checked by separating the only two nontrivial mechanisms: pigeonhole compression to two vertices with the same witness-neighborhood vector, and preservation of every atomic two-variable type under cloning. The accompanying `verify.py` exhaustively checks the sharpness construction for \(0\le k\le12\) at the level of available binary profiles and checks that the clone-pair type table has representatives for all equality/adjacency cases.

The computation is only a sanity check. The theorem itself is the symbolic argument above.

## Relationship to prior work
Pikhurko and Verbitsky's 2010 survey states Ramsey's classical theorem for Bernays--Schönfinkel graph sentences
\[
\exists^k\forall^\ell\,\Psi:
\]
the spectrum is finite or cofinite, and a general bound obtained from Ramsey theory says that either no spectrum value reaches \(2^k4^\ell\), or all orders from \(k+\ell\) onward occur. For \(\ell=2\), this gives a finite-spectrum cutoff below \(16\cdot2^k\). The present argument exploits the special fact that a homogeneous set of size two needs no Ramsey theorem: two vertices with the same neighborhood on the witnesses are already interchangeable. This yields the exact optimal cutoff \(k+2^k\), while retaining the classical cofinite start \(k+2\).

Kieroński and Michaliszyn explicitly identify the Bernays--Schönfinkel class with two universally quantified variables as a natural two-variable universal fragment. Their work studies satisfiability after adding transitive closure and does not state the exact plain-graph spectrum cutoff above.

Targeted searches for the formula \(k+2^k\), equivalent twin/neighborhood formulations, and finite-spectrum statements for the \(\exists^k\forall^2\) graph fragment did not locate an earlier statement of this sharp threshold. The result should therefore be read as a sharpened special-case spectrum theorem, not as a new decidability result.

## Limitations
The exact cutoff uses the graph vocabulary in an essential way: outside a fixed witness set, a vertex has only \(2^u\) unary adjacency patterns. Richer relational vocabularies have more one-point types, and the numerical bound changes. With three or more universal variables, cloning requires control of higher-arity configurations among several outside vertices, so the two-variable argument does not directly extend.

Priority risk remains because the sharpening is elementary and could have appeared in an unindexed note, thesis, or textbook exercise under different terminology. The searches performed found the classical Ramsey bound and later work on the two-universal-variable fragment, but no exact \(k+2^k\) spectrum endpoint.

## References
1. Oleg Pikhurko and Oleg Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865 (first posted 25 March 2010), especially Theorem 7.7 on spectra of Bernays--Schönfinkel graph sentences.
2. Emanuel Kieroński and Jakub Michaliszyn, *Two-Variable Universal Logic with Transitive Closure*, CSL 2012, pp. 396--410. DOI: 10.4230/LIPIcs.CSL.2012.396.
