# A cubic-root modal distance for the expected leaf count in Cayley trees

## Finding
Let \(T_n\) be a uniform random unrooted tree on the labelled set \([n]=\{1,\ldots,n\}\), with \(n\ge2\). Write \(D_n=d_{T_n}(1,2)\) and \(L_n=|\{v:\deg_{T_n}(v)=1\}|\). For every \(n\ge3\), and every integer \(1\le k\le n-2\),
\[
\boxed{\mathbb E[L_n\mid D_n=k]=\left(n-k+1-\frac{2}{k+1}\right)\left(\frac{n-1}{n}\right)^{n-k-2}.}
\]
At the opposite endpoint \(k=n-1\), the conditioned tree is a spanning path and the mean is \(2\). For the interior transitions \(1\le k\le n-3\),
\[
\boxed{\mathbb E[L_n\mid D_n=k+1]-\mathbb E[L_n\mid D_n=k]
=\left(\frac{n-1}{n}\right)^{n-k-3}
\frac{2n-(k^2+1)(k+2)}{n(k+1)(k+2)}.}
\]
The final transition, from \(k=n-2\) to \(n-1\), is \((3-n)/(n-1)\).

Consequently this conditional mean is exactly unimodal. If \(n\ge3\), its **first maximizing distance** is
\[
\boxed{k_*(n)=\min\{k\ge1:(k^2+1)(k+2)\ge2n\}.}
\]
It has precisely two consecutive modes, \(k_*\) and \(k_*+1\), when \((k_*^2+1)(k_*+2)=2n\), and otherwise exactly one. This includes the flat two-value case \(n=3\). The case \(n=2\) has only \(D_n=1\) and \(L_n=2\). In particular,
\[
k_*(n)=(2n)^{1/3}+O(1),\qquad
\max_{1\le k<n}\mathbb E[L_n\mid D_n=k]-\mathbb E[L_n\mid D_n=1]=e^{-1}+O(n^{-1/3}).
\]
Thus the **conditional leaf count is maximal at a cubic-root distance**, even though distances between typical uniformly chosen vertices have square-root order in this model.

## Assumptions and scope
All trees are simple, unrooted, uniformly distributed and **vertex-labelled**, with no prescribed degree sequence. The distance is the number of edges between the two fixed distinguished vertices \(1,2\), not a leaf-to-leaf distance conditioned on both endpoints being leaves. The leaf count refers to every vertex, including the two distinguished endpoints if they have degree one. The conditioning event has positive probability for each \(k\in\{1,\ldots,n-1\}\). Every statement above is finite and exact except the explicitly asymptotic consequences.

## Proof
**(1) Path-conditioned rooted forests.** Specify an ordered path of length \(k\) from vertex \(1\) to vertex \(2\). It contains \(s=k+1\) distinct path vertices and leaves \(r=n-s=n-k-1\) other vertices. Every tree in which it is the \(1\)-to-\(2\) path is obtained uniquely by attaching a labelled forest whose \(s\) components are rooted at the specified path vertices. For \(1\le s<n\), the number of such forests is
\[
F(n,s)=\det(nI_r-J_r)=s\,n^{r-1},
\]
by the rooted matrix-tree theorem, because the \(r\times r\) principal minor of the complete-graph Laplacian is \(nI_r-J_r\): its eigenvalues are \(n\) with multiplicity \(r-1\) and \(n-r=s\) once. When \(s=n\), the only completion is the path and we put \(F(n,n)=1\). Thus all ordered choices of the \(k-1\) interior path labels have exactly the same number of completions and their conditioned rooted forests are uniform.

**(2) Leaf probabilities.** Suppose \(r\ge1\) and set \(a=(n-1)/n\). For an off-path vertex \(x\), forcing \(x\) to be a leaf is equivalent to choosing one of the \(n-1\) other vertices as its unique neighbor and choosing a rooted forest on the remaining \(n-1\) vertices with the same roots. Hence
\[
\mathbb P(x\text{ is a leaf}\mid\text{the given path})
=\frac{(n-1)F(n-1,s)}{F(n,s)}=a^{r-1}.
\]
For either of the two path endpoints, being a leaf means receiving no attached forest edge. Deleting that path root leaves a rooted forest on \(n-1\) vertices with \(s-1\) roots, so
\[
\mathbb P(\text{endpoint is a leaf}\mid\text{the given path})
=\frac{F(n-1,s-1)}{F(n,s)}=\frac{s-1}{s}a^{r-1}.
\]
The \(s-2\) interior path vertices already have path-degree two and cannot be leaves. Summing \(r\) off-path contributions and two endpoint contributions gives
\[
\mathbb E[L_n\mid D_n=k]=\left(r+2\frac{s-1}{s}\right)a^{r-1}
=\left(n-k+1-\frac{2}{k+1}\right)a^{n-k-2}.
\]
This remains valid for \(r=1\). For \(r=0\), the only conditioned trees are spanning paths, so \(L_n=2\).

**(3) Exact shape.** Substitute the displayed conditional means at consecutive indices. For \(1\le k\le n-3\), elementary simplification yields the exact increment stated above. The factor outside the numerator is positive. The cubic
\[
g(k)=(k^2+1)(k+2)=k^3+2k^2+k+2
\]
is strictly increasing for integral \(k\ge1\), and the increment's sign is that of \(2n-g(k)\). From \(k=n-2\) to \(n-1\) the difference is \((3-n)/(n-1)\), negative for \(n\ge4\) and zero for \(n=3\). For \(n\ge3\), the threshold \(g(k)\ge2n\) is first met by some \(k\le n-2\), yielding the asserted unimodality and exact tie criterion, with no unexamined boundary cases.

**(4) Location and limiting height difference.** For \(k\ge1\), \(k^3\le g(k)<(k+2)^3\), so at the threshold \(k_*(n)=(2n)^{1/3}+O(1)\). Expanding \(\log(1-1/n)\), uniformly over \(1\le k=O(n^{1/3})\), gives
\[
\mathbb E[L_n\mid D_n=k]
=\frac{n}{e}+\frac{1}{e}\left(\frac52-\frac{2}{k+1}\right)
+O\left(\frac{(k+1)^2}{n}\right).
\]
At \(k=k_*(n)\) this is \((n+5/2)/e+O(n^{-1/3})\). At \(k=1\) it is \((n+3/2)/e+O(n^{-1})\). Their difference tends to \(1/e\) with the indicated remainder.

## Verification
The standalone script `verify.py` uses no nonstandard dependencies. Execute `python3 verify.py` in a directory containing that file. It reconstructs the complete labelled-tree sample space by Prüfer codes for \(2\le n\le8\) (\(280{,}392\) trees total), computing leaf counts, pair distances, conditional means and distance frequencies exactly as rational numbers. It independently checks \(35\) rooted-forest principal minors by determinant expansion and \(11{,}026\) exact finite-difference identities and \(148\) modal cases through \(n=150\). All of these checks passed. The proof above is the all-\(n\) argument; finite checks do not substitute for its determinant, bijection or algebra.

## Relationship to prior work
Janson's 2003 study of the Wiener index of simply generated random trees includes uniform labelled trees and develops global pair-distance moments and mixed moments with internal path length; these do not state the full finite-distance regression of **global leaf count** or its cubic-root mode. Berzunza Ojeda and Janson's 2021 distance-profile study gives limit laws and a construction biased by leaf count, but its leaf-marking construction and distance-profile convergence do not imply the exact conditioned regression or finite mode threshold as a stated consequence. Wagner's 2014 additive-functional work includes the leaf count as an example but does not investigate the fixed-pair metric conditioning in the available article summary. The rooted-forest count is classical; the joint conditioning and sharp modal transition, rather than that count alone, are the finding.

## Limitations
This result concerns uniformly random labelled Cayley trees, not random recursive trees, uniformly random unlabelled trees or bounded-degree models. It establishes a conditional **mean**, not conditional stochastic monotonicity, a variance formula, or a full joint distribution. The finite checks establish no facts outside their ranges. Other historical degree-distance or path-conditioned enumerators might imply the same regression without using these names; independent literature validation has not been performed. The asymptotic peak lies far below the typical distance scale, and the absolute mean enhancement is of constant order, not linear order.

## References
1. S. Janson, “The Wiener Index of Simply Generated Random Trees,” *Random Structures & Algorithms* 22 (2003), 337–358. DOI: 10.1002/rsa.10074. First published 2003-03-03.
2. G. Berzunza Ojeda and S. Janson, “The distance profile of rooted and unrooted simply generated trees,” *Combinatorics, Probability and Computing* 31 (2022), 368–410. DOI: 10.1017/S0963548321000304. First published online 2021-08-18.
3. S. Wagner, “Central Limit Theorems for Additive Tree Parameters with Small Toll Functions,” *Combinatorics, Probability and Computing* 24 (2015), 329–353. DOI: 10.1017/S0963548314000443. First published online 2014-09-08.
4. S. Wagner, “Additive tree functionals with small toll functions and subtrees of random trees,” *DMTCS Proceedings* (2012). DOI: 10.46298/dmtcs.2984. Published online 2011-12-31 according to its record.
