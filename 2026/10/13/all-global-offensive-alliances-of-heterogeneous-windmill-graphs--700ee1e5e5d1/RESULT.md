# All global offensive alliances of heterogeneous windmill graphs
## Finding
Let \(r\ge2\) and let \(m_1,\ldots,m_r\) be positive integers. Define the heterogeneous windmill
\[
W(m_1,\ldots,m_r)=K_1\vee(K_{m_1}\cup\cdots\cup K_{m_r}),
\]
with universal center \(c\) and pairwise disjoint clique blades \(B_i\) of sizes \(m_i\). For a set \(S\subseteq V(W)\), write \(s_i=|S\cap B_i|\) and \(a_i=\lfloor m_i/2\rfloor\).

Then \(S\) is a global offensive alliance exactly in either of the following two cases:

1. \(c\in S\) and \(s_i\ge a_i\) for every \(i\).
2. \(c\notin S\) and \(s_i\ge a_i+1\) for every \(i\).

Hence, with
\[
A_m(x)=\sum_{j=\lfloor m/2\rfloor}^m\binom{m}{j}x^j,
\qquad
B_m(x)=\sum_{j=\lfloor m/2\rfloor+1}^m\binom{m}{j}x^j,
\]
the cardinality enumerator of all global offensive alliances is
\[
\mathcal O_W(x)=x\prod_{i=1}^r A_{m_i}(x)+\prod_{i=1}^r B_{m_i}(x).
\]
In particular,
\[
\gamma_o(W)=1+\sum_{i=1}^r\left\lfloor\frac{m_i}2\right\rfloor,
\]
every minimum global offensive alliance contains \(c\), and the number of minimum global offensive alliances is
\[
\prod_{i=1}^r\binom{m_i}{\lfloor m_i/2\rfloor}.
\]
For the uniform generalized windmill \(K_1\vee rK_m\), this specializes to \(\gamma_o=1+r\lfloor m/2\rfloor\) with \(\binom{m}{\lfloor m/2\rfloor}^r\) minimum sets. For the friendship graph \(K_1\vee rK_2\), it gives \(\gamma_o=r+1\) and exactly \(2^r\) minimum sets.

## Assumptions and scope
A global offensive alliance is a nonempty set \(S\) such that every vertex \(v\notin S\) satisfies
\[
|N(v)\cap S|\ge |N(v)\setminus S|+1.
\]
This is the standard definition used by Sigarreta and Rodriguez. The result concerns all heterogeneous windmills with at least two blades and positive blade sizes; no regularity or equality among the \(m_i\) is assumed.

## Proof
Suppose first that \(c\in S\). For a vertex \(v\in B_i\setminus S\), the neighbors of \(v\) inside \(S\) are the center and the \(s_i\) selected vertices of its own blade, so \(|N(v)\cap S|=1+s_i\). Its neighbors outside \(S\) are the other unselected vertices of the same blade, so \(|N(v)\setminus S|=m_i-s_i-1\). The global offensive inequality is therefore
\[
1+s_i\ge m_i-s_i,
\]
which is equivalent to \(s_i\ge\lfloor m_i/2\rfloor=a_i\). These inequalities also guarantee domination because the center lies in \(S\).

Now suppose that \(c\notin S\). For \(v\in B_i\setminus S\), one has \(|N(v)\cap S|=s_i\) and \(|N(v)\setminus S|=m_i-s_i\), because the unselected center is an additional outside neighbor. Thus
\[
s_i\ge m_i-s_i+1,
\]
which is equivalent to \(s_i\ge a_i+1\). It remains to check the outside center. Put \(M=\sum_i m_i\). The blade inequalities imply
\[
2\sum_i s_i\ge 2\sum_i(a_i+1)=M-o+2r,
\]
where \(o\) is the number of odd blade sizes. Since \(o\le r\), we have \(M-o+2r\ge M+1\). Hence \(2|S|\ge M+1\), which is exactly the global offensive inequality at \(c\). This proves the set classification.

The enumerator follows by choosing independently, in each blade, at least \(a_i\) vertices when the center is present and at least \(a_i+1\) vertices when it is absent. The smallest center-containing size is \(1+\sum_i a_i\), whereas the smallest center-absent size is \(\sum_i(a_i+1)=\sum_i a_i+r\). Because \(r\ge2\), the first is strictly smaller. Equality in that first size forces exactly \(a_i\) chosen vertices in each blade, yielding the stated product count.

## Verification
The accompanying checker exhaustively enumerates every subset for all ordered blade-size tuples with two through four blades, each blade size between one and four, and total graph order at most twelve. It directly computes the global offensive condition from adjacency, compares it against the theorem's threshold classification, compares every coefficient of the enumerator, and checks the minimum size and number of minimum sets. The replay output is:

`VERIFY_OK tuples=269 subset_checks=365080 criterion_checks=365080 coefficient_checks=2798 minimum_checks=538 max_order=12`

The computation is a finite stress test of the symbolic proof, not a substitute for the proof for arbitrary blade sizes.

## Relationship to prior work
Sigarreta and Rodriguez define global offensive alliances and prove general bounds for connected graphs; their full text records AMS classification 05C69 and gives examples such as cocktail-party graphs, but it does not state a windmill or friendship-graph classification. The first public arXiv version inspected is dated 2006-02-20.

A later thesis on the defensive alliance polynomial explicitly treats friendship graphs \(K_1\vee rK_2\), but its friendship result concerns a defensive-alliance polynomial and graph recognition, not global offensive alliances. That source is relevant because it confirms the standard windmill/friendship terminology while leaving the present parameter distinct.

Searches for “global offensive alliance” together with “windmill graph”, “generalized windmill”, and “friendship graph” did not locate a published theorem giving the threshold classification, heterogeneous-blade enumerator, or minimum-set count proved here. A recent complete-multipartite result is not implication-equivalent because a windmill with a blade of size at least two contains intra-blade edges and is not complete multipartite.

## Limitations
The theorem is restricted to the global offensive condition with margin one. It does not claim the corresponding strong-offensive or general \(k\)-offensive classifications, although similar local counting may be possible. The literature search cannot rule out poorly indexed or inaccessible older results, especially results stated only for friendship graphs without “windmill” terminology.

## References
1. J. M. Sigarreta and J. A. Rodriguez, “On the global offensive alliance number of a graph,” arXiv:math/0602432, first public version 2006-02-20, https://arxiv.org/abs/math/0602432.
2. O. Favaron et al., “Offensive alliances in graphs,” Discussiones Mathematicae Graph Theory 24 (2004), 263–275, DOI 10.7151/DMGT.1230.
3. H. Ibrahim, “Defensive alliance polynomial,” Master's thesis, Hochschule Mittweida, 2018, https://monami.hs-mittweida.de/frontdoor/deliver/index/docId/11398/file/mainContant.pdf.
