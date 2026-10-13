# Randomized Borel list coloring at a local \(d+d_G^+(x)+1\) bound
## Finding
Let \(G\subseteq X\times X\) be a Borel digraph on a standard Borel space, let \(d\in\mathbb N\), and assume \(d_G^+(x)\le d\) for every vertex \(x\). If \(L:X\to[\mathbb N]^{<\omega}\) is a Borel finite-list assignment with \(|L(x)|\ge d+d_G^+(x)+1\) for every \(x\), then there are a Borel probability space \((\Omega,\mathbb P)\) and a Borel map \(c:\Omega\times X\to\mathbb N\) such that \(c(\omega,x)\in L(x)\) for every \((\omega,x)\), and for every directed edge \(x\to y\) one has \(\mathbb P[c(\omega,x)\ne c(\omega,y)]=1\). In particular, arbitrary Borel lists of size \(2d+1\) always suffice. The uniform constant \(2d+1\) is best possible, already for regular orientations of \(K_{2d+1}\).


This is a list-coloring refinement of the randomized Borel coloring theorem of Bernshteyn, Hou, Shinko, and Weilacher. The refinement is local: a vertex with out-degree \(r\) needs only \(d+r+1\) permitted colors, while the random update still uses the same \(d+1\) choices that control possible conflicts created at neighboring sources.

## Assumptions and scope
The vertex space \(X\) is standard Borel. The edge relation \(G\subseteq X\times X\) is Borel and loopless, with finite out-degree \(d_G^+(x)\le d\), where \(d\ge1\) is fixed. The list assignment \(L\) is Borel and takes values in finite subsets of \(\mathbb N\), with \(|L(x)|\ge d+d_G^+(x)+1\).

A random Borel list coloring means a Borel probability space \((\Omega,\mathbb P)\) together with a Borel map \(c:\Omega\times X\to\mathbb N\) such that \(c(\omega,x)\in L(x)\) for all \((\omega,x)\), while every fixed edge is nonmonochromatic with probability one. It does not assert that one realization is a Borel proper coloring on all edges simultaneously.

## Proof
Use the independent-set family from Lemma 8 of Bernshteyn--Hou--Shinko--Weilacher. Thus there is a Borel set \(I\subseteq2^\mathbb N\times X\) such that each section \(I_y\) is independent and every vertex belongs to \(I_y\), for random \(y\), with the same probability
\[
p=2^{-d-1}.
\]
Let
\[
\Omega=((\{0,\ldots,d\}\times2^\mathbb N)^\mathbb N,\mathbb P)
\]
with product measure, where at each stage the first coordinate is uniform on \(\{0,\ldots,d\}\) and the second has the Bernoulli product measure used in the cited lemma.

Start with the Borel list coloring \(c_0(x)=\min L(x)\). Given \(c_n\), call \(x\) sad when some out-neighbor \(z\) has \(c_n(z)=c_n(x)\). At stage \(n\), write the fresh random coordinate as \((i,y)\). If \(x\) is sad and \(x\in I_y\), recolor \(x\) to the \(i\)-th smallest member of
\[
A_n(x)=L(x)\setminus\{c_n(z):x\to z\}.
\]
Otherwise leave its color unchanged. Since at most \(d_G^+(x)\) colors are excluded,
\[
|A_n(x)|\ge |L(x)|-d_G^+(x)\ge d+1,
\]
so the update is always defined and remains inside \(L(x)\).

The update is Borel. For a fixed natural-number color \(k\), the condition that no out-neighbor of \(x\) has color \(k\) is Borel: the relevant edge relation has finite vertical sections, so the projection detecting an offending out-neighbor is Borel by the standard countable-section selection theorem. Ordering the finitely many permitted natural-number colors then makes the \(i\)-th available choice Borel.

Let \(S_n(x)\) be the event that \(x\) is sad after stage \(n\), and put
\[
\alpha=1-\frac{p}{d+1}<1.
\]
The proof from the fixed-palette case carries over because only two numerical facts are used: every recolored vertex has at least \(d+1\) available choices, and the recoloring set is independent. Conditional on the past, a sad \(x\) fails to be selected with probability \(1-p\). If a conflict is newly created at \(x\), some out-neighbor \(z\) must be selected and choose the old color of \(x\); for each such \(z\), at most one of the \(d+1\) equally likely indices \(i\) can do this. Hence, inductively,
\[
\mathbb P(S_{n+1}(x))
\le \alpha^n\left((1-p)+d_G^+(x)\frac{p}{d+1}\right)
\le \alpha^{n+1}.
\]
Therefore \(\sum_n\mathbb P(S_n(x))<\infty\), and Borel--Cantelli gives that every fixed vertex is sad only finitely often almost surely. A vertex changes color only when it is sad, so \((c_n(x))_n\) is eventually constant almost surely.

Define \(c(\omega,x)\) to be the eventual value when the sequence stabilizes, and \(\min L(x)\) otherwise. This is Borel because eventual equality to each \(k\in\mathbb N\) is a countable Boolean combination of Borel conditions. It always lies in \(L(x)\). For a fixed edge \(x\to y\), with probability one the colors of \(x\) and all finitely many out-neighbors of \(x\) stabilize and \(x\) is eventually never sad. After the last change, the limiting colors on that edge are therefore distinct. Thus
\[
\mathbb P[c(\omega,x)\ne c(\omega,y)]=1.
\]

For the uniform corollary, \(|L(x)|\ge2d+1\) implies the local hypothesis because \(d_G^+(x)\le d\). Sharpness follows from a regular tournament orientation of \(K_{2d+1}\): it has maximum out-degree \(d\), while its underlying graph needs \(2d+1\) colors. If every list were the same set of only \(2d\) colors, then on this finite graph the edgewise probability-one conditions would intersect to a probability-one proper \(2d\)-coloring, which is impossible.

## Verification
The critical nonstandard input is exactly the independent-set family in Lemma 8 of arXiv:2609.21286v1. The rest of the argument was reconstructed with the varying-list update above. The recurrence was checked with the local out-degree retained explicitly; its worst case is \(d_G^+(x)=d\), giving the same contraction factor as the source. No finite experiment is used as evidence for the infinite statement.

The measurability point introduced by varying lists was checked separately: finite out-neighbor sections make availability of each natural-number color a Borel predicate, so selecting the ordered \(i\)-th available list color is Borel.

## Relationship to prior work
Bernshteyn, Hou, Shinko, and Weilacher prove the fixed-palette randomized Borel \((2d+1)\)-coloring theorem and use exactly \(d+1\) available colors at every update. The present statement replaces the common palette by arbitrary Borel vertex lists and records the resulting local threshold \(d+d_G^+(x)+1\).

Pelayo-Gómez proves the measurable fixed-palette \((2n+1)\) theorem for graphs generated by \(n\) Borel functions. His proof does use a list argument when extending a coloring from a conull forward-invariant core, but those lists are the residual subsets of one common \((2n+1)\)-color palette created by the already chosen core coloring; it is not an arbitrary input-list theorem.

Conley--Marks--Tucker-Drob prove a Borel degree-list-coloring theorem for locally finite Borel graphs whose components are not Gallai trees. That theorem is not comparable in the needed direction: bounded out-degree allows unbounded in-degree, so the underlying graph need not be locally finite, and the present bound depends on out-degree rather than total degree.

## Limitations
The conclusion is edgewise almost sure; no single Borel realization is claimed to be proper on every edge of an uncountable graph. Sharpness is proved for the universal uniform threshold \(2d+1\), not for every individual value of the local expression \(d+d_G^+(x)+1\). Targeted semantic and literature searches reduce, but do not eliminate, the possibility of an equivalent arbitrary-list formulation under different terminology.

## References
1. Anton Bernshteyn, Edward Hou, Forte Shinko, Felix Weilacher, *Randomized Borel \((2d+1)\)-coloring of digraphs*, arXiv:2609.21286v1, 2026. Primary MSC 03E15.
2. José de Jesús Pelayo Gómez, *The measure half of the \(2n+1\) problem*, arXiv:2609.19038v1, 2026.
3. Clinton T. Conley, Andrew S. Marks, Robin D. Tucker-Drob, *Brooks's theorem for measurable colorings*, Forum of Mathematics, Sigma 4 (2016), e16.
