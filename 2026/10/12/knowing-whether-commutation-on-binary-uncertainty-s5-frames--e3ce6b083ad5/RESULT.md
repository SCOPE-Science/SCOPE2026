# Knowing-whether commutation on binary-uncertainty S5 frames

## Finding

Let \(W\) be any nonempty set and let \(R,S\) be equivalence relations on \(W\). Assume that all \(R\)-classes and \(S\)-classes have size at most two. For a subset \(X\subseteq W\) define the *knowing-whether* (non-contingency) operator
\[
\Delta_R(X)=\{w\in W:[w]_R\subseteq X\text{ or }[w]_R\cap X=\varnothing\},
\]
and define \(\Delta_S\) analogously. Thus a formula \(\Delta_R\varphi\) means that the truth value of \(\varphi\) is constant on the \(R\)-information cell.

**Theorem.** The following are equivalent:

1. \(\Delta_R(\Delta_S(X))=\Delta_S(\Delta_R(X))\) for every \(X\subseteq W\).
2. The two-agent modal principle \(\Delta_R\Delta_Sp\leftrightarrow\Delta_S\Delta_Rp\) holds at every world for every valuation (and hence the two orderings agree for every formula).
3. In the two-edge-colored undirected graph with an \(R\)-edge for every two-point \(R\)-class and an \(S\)-edge for every two-point \(S\)-class, each connected component is one of: an isolated singleton; two vertices joined by an \(R\)-edge, an \(S\)-edge, or both; four vertices forming a square whose edges alternate in color.
4. The two involutions \(r,s:W\to W\), which exchange the elements of each two-point information cell and fix the singleton cells, commute.

For \(n\ge0\), let \(a_n\) count ordered pairs of such equivalence relations on a *labeled* \(n\)-point set satisfying these equivalent conditions. The exact exponential generating function is
\[
\sum_{n\ge0}a_n\frac{z^n}{n!}=\exp\left(z+\frac{3z^2}{2}+\frac{z^4}{4}\right).
\]
The values for \(n=0,1,\ldots,7\) are \(1,1,4,10,52,196,1216,5944\). There is no counterexample on fewer than three worlds; on three worlds, an \(R\)-edge and an \(S\)-edge that share exactly one endpoint give a counterexample.

## Assumptions and scope

All structures are ordinary S5 information frames, i.e. \(R\) and \(S\) are equivalence relations, not arbitrary accessibility relations. Each information cell contains one or two worlds; the relations need not be equal, and \(W\) need not be finite. The modal language has Boolean truth values and two non-contingency modalities. Validity quantifies over every valuation of the atomic proposition, not only some chosen valuation. The counting statement, unlike the structural equivalence, concerns finite *labeled* frames and counts ordered pairs \((R,S)\).

## Proof

For an equivalence relation \(T\) with cells of size at most two, let \(E_T\) be the set of its two-element cells. For any \(X\subseteq W\), the set \(\Delta_T(X)\) is the union of the \(T\)-cells on which membership in \(X\) is constant. In particular, if \(T\) has a singleton cell at \(w\) then \(\Delta_T(\{w\})=W\); if \(\{w,u\}\in E_T\) then \(\Delta_T(\{w\})=W\setminus\{w,u\}\).

For any two-element set \(B\), define \(\partial_T B\) to be the union of the two-point \(T\)-cells meeting \(B\) in exactly one element. Directly from the definition, the crucial identity is
\[
\Delta_T(W\setminus B)=W\setminus\partial_T B.
\]
The identity holds because complementing a set preserves the property of being constant on a cell; cells not cut by \(B\) contribute both endpoints or their sole singleton, while cells cut by \(B\) contribute neither endpoint.

Assume condition 1. Suppose \(\{w,u\}\in E_R\) while \(w\) is an \(S\)-singleton. With \(X=\{w\}\), the left composition is \(\Delta_R(\Delta_S X)=W\). The right composition is \(W\setminus\partial_S\{w,u\}\), so the boundary is empty. As \(w\) is an \(S\)-singleton, this forces \(u\) also to be an \(S\)-singleton. By symmetry, an edge present in exactly one color and incident to no edge of the other color must be an isolated two-vertex component. If both relations share the same edge, it already forms an isolated two-vertex component, since each color is a matching.

Suppose now that \(w\) has distinct partners \(u\) under \(R\) and \(v\) under \(S\). Apply condition 1 to \(X=\{w\}\). The singleton calculation and boundary identity give
\[
\partial_R\{w,v\}=\partial_S\{w,u\}.
\]
The left boundary contains \(\{w,u\}\), and the right contains \(\{w,v\}\). Thus \(u\) must have an \(S\)-partner, say \(t'\), distinct from \(w,v\); similarly \(v\) must have an \(R\)-partner, say \(t\), distinct from \(w,u\). The two boundaries are respectively \(\{w,u,v,t\}\) and \(\{w,u,v,t'\}\), hence \(t=t'\). The two matchings therefore close into a four-cycle with alternating colors. No edge can leave it, because each vertex already has its unique partner in each matching. This proves condition 3 in all cases, including when \(W\) is infinite.

Conversely assume condition 3. On an isolated singleton, both \(\Delta\)-operators return that entire component. On any two-vertex component, each operator is either the identity on valuations restricted to that component (if the color gives only singleton cells) or sends every valuation to the entire component (if the color gives one double cell); in either case the two operators commute.

On an alternating square, arrange the truth values of \(X\) in a \(2\)-by-\(2\) Boolean matrix, with \(R\)-cells as rows and \(S\)-cells as columns:
\[
\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad a,b,c,d\in\{0,1\}.
\]
After applying \(\Delta_S\), each column consists entirely of a common flag: it is \(1\) if its two original entries agree, otherwise \(0\). Applying \(\Delta_R\) yields the full square if these two column flags agree and the empty square otherwise. Reversing the order yields the full square if the two *row* agreement flags agree and the empty square otherwise. But equality of the column flags says \((a\oplus c)=(b\oplus d)\), while equality of the row flags says \((a\oplus b)=(c\oplus d)\); both are equivalent to \(a\oplus b\oplus c\oplus d=0\), where \(\oplus\) is Boolean exclusive-or. Thus the two compositions agree on each square. The definition of \(\Delta\) respects disjoint components because all its cells lie inside their components. Commutation on every component therefore implies commutation on \(W\). This establishes \(3\Rightarrow1\).

Conditions 1 and 2 are equivalent because an atomic valuation can be an arbitrary subset of \(W\), and the truth set of any formula is a subset of \(W\). To see that conditions 3 and 4 are equivalent, regard each matching as an involution. Commuting involutions generate orbits of size at most four: the orbit of \(w\) is contained in \(\{w,r(w),s(w),rs(w)\}\), and the cases where this set has one, two, or four elements are precisely the listed component types. Conversely the two matching permutations plainly commute on each listed component.

For the census, each permitted connected component has respectively \(1\) type on a fixed labeled singleton, \(3\) types on a fixed labeled two-set (first color only, second only, or both), and \(3\) ways to choose one perfect matching on a labeled four-set, followed by \(2\) other choices for a distinct perfect matching, giving \(6\) alternating squares on a fixed labeled four-set. The labeled exponential formula therefore gives the stated generating function: singleton weight \(z\), dyad weight \(3z^2/2!\), square weight \(6z^4/4!\). This counts every ordered pair exactly once through its unique connected-component decomposition.

## Verification

The self-contained Python 3 standard-library verifier `verify.py` enumerates every equivalence partition into blocks of size one or two for \(n=1,\ldots,7\). For each ordered pair, it tests both compositions on all \(2^n\) valuations, independently checks the claimed graph-component classification, and compares the accepted count to an exact rational coefficient calculation from the exponential generating function. It prints `VERIFY_OK` on success. The counts of ordered frame pairs tested at the seven sizes are \(1,4,16,100,676,5776,53824\), altogether \(60397\). The finite checks do not prove the infinite-world statement, which follows from the structural argument above.

## Relationship to prior work

Wang and Zenger's 2026 work develops proof systems for non-contingency logic and motivates its interpretation as knowing whether; the present theorem asks a different, two-agent semantic commutation question on S5 frames with cells of size at most two. Fan, Wang, and van Ditmarsch's earlier *Knowing Whether* develops the multi-agent syntax and semantics. Classical combinatorics already gives the orbit structure of pairs of commuting involutions and the related labeled counting mechanism. These facts are *inputs or comparisons*, not claimed discoveries here. The claimed distinction is the exact equivalence between the nonnormal knowing-whether commutation axiom and that orbit structure. It does not follow merely by substituting noncontingency operators for ordinary knowledge modalities without proof.

## Limitations

No result is asserted for equivalence classes of size three or more, non-equivalence accessibility frames, alternative multivalued semantics, or other epistemic operators. The enumerative formula also counts classical commuting involution pairs and should not be interpreted as an independently new integer sequence. The literature search may have missed an older equivalent treatment of two-agent knowing-whether commutation. No independent audit has been performed.

## References

1. Yunsong Wang and Lukas Zenger, *Proof Theory for Non-Contingency Logic*, arXiv:2609.38975v1 (first submitted 2026-09-30), https://arxiv.org/abs/2609.38975.
2. Jie Fan, Yanjing Wang and Hans van Ditmarsch, *Knowing Whether*, arXiv:1312.0144v3, https://arxiv.org/abs/1312.0144.
