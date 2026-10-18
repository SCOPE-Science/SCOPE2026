# A parity barrier for globally minimal defensive alliances in clique windmills

## Finding
For integers \(r\ge2\) and \(m_1,\ldots,m_r\ge2\), let \(W_{\mathbf m}=K_1\vee(K_{m_1}\sqcup\cdots\sqcup K_{m_r})\): one common hub is adjacent to the vertices of \(r\) pairwise nonadjacent clique blades \(B_i\) of respective orders \(m_i\). Put \(k_i=\lfloor m_i/2\rfloor\), \(M=\sum_i m_i\), and \(o=|\{i:m_i\text{ is odd}\}|\). A globally minimal defensive alliance means a nonempty defensive alliance containing no proper nonempty defensive-alliance subset.

Every globally minimal defensive alliance is precisely one of the following two disjoint types:

1. A hub-free set of \(k_i+1\) vertices taken from exactly one blade \(B_i\), with no selected vertices in other blades.
2. If and only if \(o\le1\), the hub together with exactly \(k_i\) arbitrary vertices from **every** blade \(B_i\).

Consequently, writing \(P_{\mathbf m}(z)=\sum_{S\text{ globally minimal}}z^{|S|}\), the complete enumerator is
\[
P_{\mathbf m}(z)=\sum_{i=1}^r \binom{m_i}{k_i+1}z^{k_i+1}+\mathbf1_{\{o\le1\}}\left(\prod_{i=1}^r\binom{m_i}{k_i}\right)z^{1+\lfloor M/2\rfloor}.
\]
In the uniform even-blade and odd-blade cases, respectively,
\[
P_{(2k)^r}(z)=r\binom{2k}{k+1}z^{k+1}+\binom{2k}{k}^{r}z^{rk+1},\qquad
P_{(2k+1)^r}(z)=r\binom{2k+1}{k+1}z^{k+1},\quad r\ge2,\ k\ge1.
\]
Thus the *upper defensive alliance number*, the largest size of a globally minimal defensive alliance, equals \(rk+1\) in the even case and \(k+1\) in the odd case. Adding one vertex to each even blade decreases this upper number by \((r-1)k\), despite increasing the graph order. When \((r-1)k\ge2\), the even case has no globally minimal defensive alliance of any cardinality \(k+2,k+3,\ldots,rk\); these gaps can grow arbitrarily long.

## Assumptions and scope
All graphs are finite, simple, and undirected. The join \(K_1\vee H\) adds one hub adjacent to every vertex of \(H\); no edges connect distinct blades. A *defensive alliance* is a nonempty vertex set \(S\) such that for every \(v\in S\),
\[
|N[v]\cap S|\ge|N(v)\setminus S|,
\]
or equivalently \(2|N(v)\cap S|+1\ge\deg(v)\), where \(N[v]\) is the closed neighborhood. Inclusion-minimality is with respect to *all* nonempty proper subsets, not merely the result of deleting one vertex. This is not the global defensive-alliance condition requiring domination of the graph: "globally minimal" modifies minimality, not domination. The domain is all \(r\ge2\) and blade orders \(m_i\ge2\), with no uniformity or parity assumption unless stated.

## Proof
Let \(h\) denote the hub, \(S\) a nonempty set, \(s_i=|S\cap B_i|\), and \(x=\sum_i s_i\). Every peripheral vertex in \(B_i\) has degree \(m_i\); the hub has degree \(M\).

**Case 1: the hub is omitted.** Each selected peripheral vertex in \(B_i\) has \(s_i-1\) neighbors in \(S\), so its defensive inequality is
\[
2(s_i-1)+1\ge m_i\quad\Longleftrightarrow\quad s_i\ge\lfloor m_i/2\rfloor+1=k_i+1.
\]
Thus a hub-free set is a defensive alliance exactly when every occupied blade has at least \(k_i+1\) selected vertices. If two or more blades are occupied, or any occupied blade has more than \(k_i+1\) selected vertices, a proper nonempty subset consisting of exactly \(k_i+1\) vertices of one occupied blade is itself defensive. Conversely, a single blade with exactly \(k_i+1\) selected vertices is defensive and no proper nonempty subset is. This proves Type 1.

**Case 2: the hub is selected.** For each selected peripheral vertex in \(B_i\), the number of selected neighbors is \(s_i\) (the hub plus its \(s_i-1\) selected blade neighbors), and its defensive inequality is
\[
2s_i+1\ge m_i\quad\Longleftrightarrow\quad s_i\ge k_i.
\]
The hub's defensive inequality is \(2x+1\ge M\), equivalent for integer \(x\) to \(x\ge T:=\lfloor M/2\rfloor\). If any \(s_i\ge k_i+1\), then \(S\) contains a proper hub-free defensive alliance of Type 1. Therefore, in every globally minimal hub-containing alliance, each \(s_i\) belongs to \(\{0,k_i\}\), and consequently
\[
T\le x\le\sum_i k_i=\frac{M-o}{2}
=\left\lfloor\frac M2\right\rfloor-\left\lfloor\frac o2\right\rfloor.
\]
This is possible only when \(o\le1\). In that case equality must hold throughout, all \(s_i=k_i\), and \(x=T\): since \(k_i\ge1\), no blade may be absent.

Conversely, suppose \(o\le1\) and choose the hub and \(k_i\) peripheral vertices in each blade. The peripheral inequalities hold, and \(x=\sum k_i=T\) makes the hub defensive. Every proper subset omitting the hub has at most \(k_i\) vertices in each blade, so is not defensive by Case 1. Every proper subset containing the hub has fewer than \(T\) peripheral vertices, making its hub nondefensive. Hence the set is globally minimal, proving Type 2 and exhausting all possibilities.

There are \(\binom{m_i}{k_i+1}\) Type 1 sets of cardinality \(k_i+1\) per blade and, if \(o\le1\), exactly \(\prod_i\binom{m_i}{k_i}\) Type 2 sets of cardinality \(1+\sum_i k_i=1+\lfloor M/2\rfloor\). Their disjointness follows from hub membership, and the formula results.

For \(m_i=2k\), all \(k_i=k\) and \(o=0\); for \(m_i=2k+1\), all \(k_i=k\) and \(o=r\ge2\), forbidding Type 2. These substitutions yield the displayed even/odd polynomials. As \(r\ge2\), the even Type 2 size \(rk+1\) is larger than \(k+1\), and the odd case has only size \(k+1\). The stated upper numbers, parity drop and missing cardinalities follow. This completes the proof.

## Verification
The standalone script `verify.py` constructs graph adjacency from the definition. For each nonempty vertex subset, it evaluates defensive inequalities from degrees and computes whether *any* defensive proper subset exists, not merely whether a one-vertex deletion remains defensive. It compares the entire set of globally minimal masks and the entire size-count distribution with the theorem. The independent exhaustive comparison covers 136 ordered blade-size profiles with two to four blades and individual orders among \(2,3,4,5\), restricted to at most 12 peripheral vertices: 537,880 nonempty vertex subsets and 6,023 globally minimal sets. A further 42 uniform arithmetic checks test both parity formulas at \(2\le r\le7\), \(1\le k\le7\). The output is recorded in `verification_output.txt`. Computation verifies these finite cases only; the proof above establishes the theorem for the entire stated domain.

## Relationship to prior work
The defensive alliance definition and the distinction between locally and globally minimal alliances are established in the literature. Feng, Fernau and Mann (2023) study enumeration algorithms for both kinds on general graphs and selected graph classes. Gaikwad and Maity (2022) analyze parameterized complexity of globally minimal defensive alliances; Bazgan, Fernau and Tuza (2018) study the upper defensive alliance parameter. Their relevant accessible full texts describe algorithms, parameterized results and extremal problems, but no statement identified there implies the exact two-family enumeration for heterogeneous clique windmills or the parity suppression of hub-containing minimal alliances. Ibrahim's defensive alliance polynomial is defined using a different weighted counting of connected vertex sets; its friendship-graph computation does not enumerate inclusion-minimal defensive alliances. The specific complete family and parity result are assessed against that literature and relevant available prior mathematical records, not asserted to be definitively first in all literature.

## Limitations
The classification is confined to one-hub clique windmills with \(r\ge2\) and \(m_i\ge2\); it makes no assertion for unequal attachment patterns beyond this graph family or for stronger/alliance variants. Full bibliographic priority against unindexed and inaccessible materials cannot be certified. An independently conducted scientific audit has not been performed. The computational check is finite and provides corroboration, not an infinite-domain proof.

## References
- Z. Feng, H. Fernau, K. Mann, *Enumerating Minimal Defensive Alliances*, arXiv:2312.11963v1 (first posted 19 December 2023), https://arxiv.org/abs/2312.11963.
- V. Gaikwad and S. Maity, *Globally Minimal Defensive Alliances: A Parameterized Perspective*, arXiv:2202.02010 (2022), https://arxiv.org/abs/2202.02010.
- C. Bazgan, H. Fernau and Zs. Tuza, *Aspects of Upper Defensive Alliances*, Discrete Applied Mathematics, DOI:10.1016/j.dam.2018.05.061.
- H. Ibrahim, *Defensive Alliance Polynomial*, arXiv:1811.10089 (2018), https://arxiv.org/abs/1811.10089.
