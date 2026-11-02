# Independent-domination polynomials of central graphs of triangle-free graphs

## Finding
For a finite simple triangle-free graph \(G=(V,E)\) with minimum degree at least two, write \(m=|E|\), \(d(v)=d_G(v)\), and \(C(G)\) for its central graph. The independent-domination polynomial is
\[
D_i(C(G),z)=z^m+\sum_{v\in V}z^{m-d(v)+1}+\sum_{uv\in E}z^{m-d(u)-d(v)+3}.
\]
In particular, there are exactly \(1+|V|+m\) independent dominating sets. For \(M=\max_{uv\in E}(d(u)+d(v))\),
\[
i(C(G))=m+3-M,
\]
and its number of minimum sets is
\[
|\{uv\in E:d(u)+d(v)=M\}|+|\{v\in V:d(v)=M-2\}|.
\]
The complete polynomial distinguishes some graphs having the same degree sequence.

## Assumptions and scope
A central graph is constructed by replacing each edge \(uv\) of \(G\) by the two-edge path \(u,s_{uv},v\) and adding the edge \(uw\) exactly when the two original vertices \(u,w\) are nonadjacent in \(G\). In particular no two subdivision vertices are adjacent. An independent dominating set is a vertex subset with no internal edge such that every omitted vertex has a neighbor in the set. The polynomial \(D_i(H,z)\) sums \(z^{|S|}\) over **all** independent dominating sets, rather than over arbitrary independent sets. The graph \(G\) is finite and simple, has no triangles, and satisfies \(d(v)\ge2\) for each original vertex. Connectedness is unnecessary.

## Proof
Let \(S\) be any independent dominating set of \(C(G)\) and put \(I=S\cap V\). Since the central graph joins two distinct original vertices exactly when they are nonadjacent in \(G\), the set \(I\) is a clique of \(G\). Triangle-freeness implies that \(I\) is empty, a singleton, or the endpoints of an edge of \(G\).

For each original edge \(e=uv\), its subdivision vertex \(s_e\) is adjacent only to its original endpoints. If either endpoint belongs to \(I\), independence prohibits \(s_e\) from belonging to \(S\). If neither endpoint belongs to \(I\), domination requires \(s_e\in S\), because neither of its only two neighbors is selected. Consequently, for a fixed \(I\) the set \(S\) is uniquely determined as
\[
S(I)=I\cup\{s_{uv}:uv\in E,\ u\notin I,\ v\notin I\}.
\]
This construction is independent for any clique \(I\) of \(G\). It remains to verify that every allowed \(I\) dominates all original vertices outside \(I\).

If \(I=\varnothing\), every original vertex has a selected incident subdivider. If \(I=\{v\}\), a vertex \(w\ne v\) not adjacent to \(v\) in \(G\) is adjacent to \(v\) in \(C(G)\). If \(w\) is adjacent to \(v\) in \(G\), its degree at least two supplies an edge \(wx\) other than \(wv\); the subdivider \(s_{wx}\) is selected. Finally, if \(I=\{u,v\}\) with \(uv\in E\), no original vertex \(w\notin I\) is adjacent in \(G\) to both \(u\) and \(v\), since that would form a triangle. Hence \(w\) is adjacent in the central graph to at least one of the selected originals \(u,v\). Therefore all \(I\) of the three forms produce independent dominating sets, and there are no others.

Their sizes are respectively \(m\), \(m-d(v)+1\), and \(m-d(u)-d(v)+3\), because an edge \(uv\) has \(d(u)+d(v)-1\) incident edges. This proves the polynomial and total count. For every \(v\), choose a neighbor \(w\) with \(d(w)\ge2\). The edge-produced size is at most the singleton-produced size, since
\[
m-d(v)-d(w)+3\le m-d(v)+1.
\]
The all-subdivider set is strictly larger than some edge-produced set. Hence the minimum is realized by an edge whose endpoint degrees have maximum sum \(M\); a singleton ties precisely when \(d(v)=M-2\). The count of minimizers follows.

For degree-sequence sensitivity, consider these two triangle-free graphs on vertices \(0,1,2,3,4,5\). Graph \(G_1\) has edges \(01,03,05,12,23,34,45\); graph \(G_2\) has edges \(01,04,05,12,23,34,35\). Each has degree sequence \((2,2,2,2,3,3)\) and seven edges, but the formulas yield
\[
D_i(C(G_1),z)=z^7+6z^6+6z^5+z^4,
\qquad D_i(C(G_2),z)=z^7+5z^6+8z^5.
\]
The minimum sizes are four and five, respectively.

## Verification
The standalone file `verify.py` builds the central graph directly from the definition and enumerates its independent dominating vertex subsets without using the formula. It compares the resulting cardinality polynomial with the theorem for every labelled triangle-free graph on four through six vertices whose minimum degree is at least two: 560 graphs in total. It also checks both explicit six-vertex examples and the minimum-set counts. Run with `python verify.py`; expected final output is `VERIFY_OK`.

## Relationship to prior work
Cabrera-Martínez, López-Carmona, Rios-Villamar, and Serrano-Díaz (arXiv:2609.16357, first public 2026-09-14) investigate the independent domination **number** of central graphs and motivate the subject. The present statement enumerates **every** independent dominating set and its size for the entire triangle-free minimum-degree-two class, and determines the full polynomial and minimum-set multiplicities. Earlier general work introduced independent-domination polynomials. The graph classes and parameters are therefore related, but a numerical formula for the minimum does not itself enumerate the other cardinality coefficients. The 2026 full preprint was not accessible for line-by-line theorem comparison, so historical priority is provisional.

## Limitations
The statement excludes triangles and degree-zero or degree-one originals. The polynomial refers to a single centralization, not higher iterates. It counts labelled vertex sets, not symmetry orbits. Exhaustive verification up to six vertices checks the finite cases but is not a substitute for the proof for arbitrary finite order. A complete comparison with every theorem and appendix of the inaccessible 2026 preprint and independent expert validation remain outstanding.

## References
Cabrera-Martínez, A., López-Carmona, J. L., Rios-Villamar, I., and Serrano-Díaz, A., *Independent domination in central graphs*, arXiv:2609.16357 (2026), https://arxiv.org/abs/2609.16357.

Shivaswamy, P. M., Nandappa, S. D., and Alwardi, A., *Independent Dominating Polynomial in Graphs* (2014), bibliographic record available at https://www.researchgate.net/profile/Soner-Nandappa-D.
