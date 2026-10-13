# Exact multi-rainbow domination of two-subset Kneser graphs

## Finding

**Theorem.** For all integers \(k\ge3\) and \(n\ge k+1\),
\[
\gamma_{rk}(KG(n,2))=2k.
\]
Here \(KG(n,2)\) is the Kneser graph whose vertices are the two-element subsets of \([n]\), adjacent precisely when disjoint. The subscript \(rk\) denotes the standard \(k\)-rainbow domination parameter, not \(k\)-tuple domination. The result includes the disconnected boundary graph \(KG(4,2)\).

The upper bound admits a uniform explicit six-vertex witness, regardless of the size of \(n\). It is an exact statement for the whole specified two-parameter domain, not an asymptotic bound or a finite search extrapolation.

## Assumptions and scope

All graphs are finite and simple. For an integer \(k\ge1\), a \(k\)-rainbow dominating function is a map \(f:V(G)\to 2^{[k]}\) such that, for each vertex \(v\) with \(f(v)=\varnothing\),
\[
\bigcup_{u\in N_G(v)}f(u)=[k].
\]
Its weight is \(w(f)=\sum_{v\in V(G)}|f(v)|\), and \(\gamma_{rk}(G)\) is the minimum possible weight. Labeled vertices are allowed to carry multiple colors, and a nonempty-labeled vertex is not required to see any color in its own neighborhood. The theorem assumes exactly \(k\ge3\) and \(n\ge k+1\), so in particular \(n\ge4\).

## Proof

**Upper bound.** Choose four distinct ground elements \(1,2,3,4\). Their six two-subsets split into the three perfect matchings
\[
M_1=\{\{1,2\},\{3,4\}\},\quad
M_2=\{\{1,3\},\{2,4\}\},\quad
M_3=\{\{1,4\},\{2,3\}\}.
\]
Partition the \(k\) colors into three nonempty disjoint blocks \(C_1,C_2,C_3\). For each two-subset \(e\in M_i\), set \(f(e)=C_i\); label every other two-subset by \(\varnothing\). Then \(w(f)=2(|C_1|+|C_2|+|C_3|)=2k\). For any zero-labeled two-subset \(x\), the two edges in each \(M_i\) are disjoint, so \(x\) cannot intersect both: at least one is disjoint from \(x\) and hence adjacent to \(x\) in the Kneser graph. Thus \(x\) sees every \(C_i\), so \(f\) is \(k\)-rainbow dominating.

**Lower bound.** Suppose to the contrary that a \(k\)-rainbow dominating function \(f\) has weight \(w(f)\le 2k-1\). If some color is absent everywhere, no vertex can carry the empty set, since such a vertex cannot see the absent color. Every one of the \(\binom n2\) vertices must then carry a nonempty label, giving
\[
w(f)\ge\binom n2\ge\binom{k+1}{2}\ge 2k\quad(k\ge3),
\]
a contradiction. Therefore every color appears at least once. Counting color incidences, \(w(f)\le2k-1\) forces some color \(c\) to occur on exactly one vertex, say \(e=\{a,b\}\).

Every two-subset meeting \(e\) must carry a nonempty label: it has no neighbor bearing color \(c\). Exactly \(2n-3\) two-subsets meet \(e\), whence
\[
w(f)\ge 2n-3.
\]
If \(n\ge k+2\), this is at least \(2k+1\), contradicting the assumed weight. It remains to handle \(n=k+1\). Now \(2n-3=2k-1\), so equality is forced throughout: the nonempty vertices are precisely the two-subsets meeting \(\{a,b\}\), and each carries a singleton color. In particular \(f(\{a,b\})=\{c\}\).

Put \(X=[n]\setminus\{a,b\}\), with \(|X|=k-1\ge2\). Every two-subset of \(X\) is empty-labeled. Fix another color \(d\ne c\). Each vertex bearing \(d\) must be a spoke \(\{a,x\}\) or \(\{b,x\}\), with \(x\in X\). If only one spoke bore \(d\), choosing another \(y\in X\setminus\{x\}\) would make the empty vertex \(\{x,y\}\) intersect the sole bearer of \(d\). It would have no adjacent vertex bearing \(d\), a contradiction. Hence each of the \(k-1\) colors other than \(c\) appears at least twice, and \(c\) appears once. Because \(w(f)=2k-1\), every other color appears on exactly two spokes.

Choose the two spokes bearing one such color \(d\), say \(\{p,x\}\) and \(\{q,y\}\), where \(p,q\in\{a,b\}\) and \(x,y\in X\). If \(x\ne y\), the empty vertex \(\{x,y\}\) intersects both spokes. If \(x=y\), choose \(z\in X\setminus\{x\}\) and use the empty vertex \(\{x,z\}\), which again intersects both spokes. In either case an empty vertex has no neighbor bearing \(d\), contradicting rainbow domination. Thus \(w(f)\ge2k\), completing the proof.

## Verification

The standard-library script `verify.py` constructs the three-matching witness and checks its domination condition directly from the disjointness adjacency matrix for every \(4\le n\le15\) and \(3\le k<n\), 78 parameter pairs. Independently, it exhausts every possible placement of fewer than six color incidences on \(KG(4,2)\) and \(KG(5,2)\) for \(k=3\): respectively 12,616 and 174,437 incidence subsets, with no counterexample. The captured output is `verify_output.txt`; reproduce using `python3 verify.py`. These finite tests do not prove the infinite theorem; the case-complete argument above does.

## Relationship to prior work

Cornet and Torres [1], and Brešar, Cornet, Dravec and Henning [2], prove exact results for ordinary \(k\)-tuple, \(k\)-, and \(k\)-tuple-total domination in Kneser graphs. These impose **counts of adjacent selected vertices**, rather than distinct color coverage with multi-color labels, and do not entail the asserted \(k\)-rainbow optimum. Zec and Grbić [3] address Roman variants on Kneser graphs, also a different local condition. The general equivalence \(\gamma_{rk}(G)=\gamma(G\square K_k)\), described in [4], provides a second formulation: the theorem computes domination of \(KG(n,2)\square K_k\) in the stated range. The proof uses no claimed new result from these papers and does not claim novelty for general rainbow-domination definitions, generalized Petersen graph cases with smaller color palettes, or ordinary domination of Kneser graphs.

## Limitations

The theorem does **not** classify all minimizers, treat palette sizes \(k=1,2\), determine arbitrary \(KG(n,r)\) for \(r\ne2\), or assert the equality for \(n\le k\). Literature search cannot establish uniqueness of discovery; differently indexed results for domination of Cartesian products remain a residual overlap risk. The lower bound relies essentially on \(n\ge k+1\), and the witness is not claimed optimal outside that domain. Independent external validation has not been performed.

## References

[1] M. G. Cornet and P. Torres, *\(k\)-tuple domination on Kneser graphs*, arXiv:2308.15603 (first public version 2023-08-29), https://arxiv.org/abs/2308.15603 .

[2] B. Brešar, M. G. Cornet, T. Dravec and M. A. Henning, *\(k\)-Domination invariants on Kneser graphs*, arXiv:2312.15464 (2023), https://arxiv.org/abs/2312.15464 .

[3] T. Zec and M. Grbić, *Several Roman domination graph invariants on Kneser graphs*, arXiv:2204.05664 (2022), https://arxiv.org/abs/2204.05664 .

[4] T. Kraner Šumenjak, D. F. Rall and A. Tepeh, *Rainbow domination in the lexicographic product of graphs*, arXiv:1210.0514 (2012), https://arxiv.org/abs/1210.0514 .
