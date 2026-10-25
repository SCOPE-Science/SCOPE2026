# Balanced quadrilaterals span every signed complete-bipartite cycle space

## Finding

For integers \(m,n\ge2\) and any signing \(s_{ij}\in\{\pm1\}\) of the edges of \(K_{m,n}\), orient edges from the \(m\)-vertex class \(\{a_i\}\) to the \(n\)-vertex class \(\{b_j\}\). Over \(\mathbb R\), define the signed incidence map
\[
\partial_s\colon\mathbb R^{mn}\longrightarrow\mathbb R^{m+n},\qquad \partial_s(e_{ij})=s_{ij}b_j-a_i.
\]
Call a quadrilateral with distinct \(i,k\) and distinct \(j,l\) **balanced** if \(s_{ij}s_{kj}s_{kl}s_{il}=+1\). Let \(B_s\) be the span of the signed cycle chains of these balanced quadrilaterals. Then
\[
B_s=\ker\partial_s,\qquad
\dim B_s=\begin{cases}
(m-1)(n-1),&s\text{ balanced on every cycle},\\
(m-1)(n-1)-1,&\text{otherwise}.
\end{cases}
\]
In the real signed **regular GLMY** path homology defined via the deck-anti-invariant chain complex of the bidirected signed double cover, this implies
\[
H^{\mathrm{signed\ GLMY}}_1(K_{m,n},s;\mathbb R)=0
\]
for every signing, including unbalanced ones.

## Assumptions and scope

Graphs are finite, simple, undirected complete bipartite graphs with both directed arcs present when forming their regular path complexes. The signs lie in \(\{\pm1\}\) and the field is \(\mathbb R\). The signed cover has vertices \((v,\epsilon)\) for \(\epsilon\in\{\pm1\}\), and arcs \((u,\epsilon)\to(v,\epsilon s_{uv})\) for each underlying arc \(u\to v\); the deck involution reverses \(\epsilon\). The anti-invariant chain groups are the negative-one eigenspaces of this involution. A signing is balanced if the product of signs around **every** closed walk is positive. No claim is made for an integral coinvariant model, an arbitrary orientation with missing reverse arcs, or higher homology.

## Proof

**1. Explicit signed square boundaries.** For a balanced quadrilateral with corners \((i,j),(k,j),(k,l),(i,l)\), the chain
\[
q_{ik;jl}=e_{ij}-s_{ij}s_{kj}e_{kj}+s_{ij}s_{kj}e_{kl}-e_{il}
\]
has zero signed boundary. Indeed the two row coefficients cancel; the coefficient of \(b_j\) is \(s_{ij}-s_{ij}s_{kj}^{2}=0\), while the coefficient of \(b_l\) is \(s_{ij}s_{kj}s_{kl}-s_{il}=0\) by balance. Thus \(B_s\subseteq\ker\partial_s\).

**2. Gauge normalization.** Switching signs at vertices conjugates the incidence map by invertible diagonal maps and carries each balanced square chain to a nonzero scalar multiple of the corresponding switched chain. We may therefore assume \(s_{i0}=s_{0j}=+1\) for all \(i,j\), where row and column zero are fixed.

**3. Parametrize all cycles.** For a kernel vector \(c=(c_{ij})\), let \(x_{ij}=c_{ij}\) for \(i,j\ge1\). The row equations give
\[
c_{i0}=-\sum_{j\ge1}x_{ij}\quad(i\ge1),
\]
and the nonzero-column equations give
\[
c_{0j}=-\sum_{i\ge1}s_{ij}x_{ij}\quad(j\ge1).
\]
The row-zero equation then gives \(c_{00}=\sum_{i,j\ge1}s_{ij}x_{ij}\); its column-zero equation is precisely
\[
\sum_{i,j\ge1}(s_{ij}-1)x_{ij}=0.
\]
Hence \(\ker\partial_s\) identifies with all interior arrays \(x\) satisfying \(\sum_{s_{ij}=-1}x_{ij}=0\). There is no constraint if all interior signs are positive, and exactly one independent real constraint if any is negative, proving the displayed dimension formula. Gauge normalization also shows that the signing is balanced exactly when no interior negative entries remain.

**4. Generate the constraint space by balanced squares.** Each positive interior entry \((i,j)\) admits the balanced square with row zero and column zero. Its interior array is the elementary coordinate vector at \((i,j)\). Remove all such coordinates using these squares. It remains to generate the zero-sum arrays on the set \(N\) of negative interior entries. If two entries of \(N\) share a row, the balanced square using that row and row zero with their two columns has interior array a nonzero multiple of their difference. The corresponding statement for entries sharing a column follows using column zero. For any two negative entries \((i,j)\), \((k,l)\) in distinct rows and columns, inspect the two cross entries \((i,l)\), \((k,j)\). If either cross entry is negative, the two chosen entries are connected by two same-row/column moves through that cross entry. If both cross entries are positive, the four negative-positive-positive-negative corners form a balanced square whose interior array, after subtracting positive-coordinate square generators, is a nonzero multiple of the difference of the chosen negative coordinates. Thus the balanced squares generate every difference between negative interior coordinates and hence the whole sum-zero subspace. It follows that \(\ker\partial_s\subseteq B_s\), completing the signed cycle-space theorem.

**5. From squares to signed path homology.** In the regular GLMY complex of the bidirected double cover, the boundary of a permitted two-step backtrack is the sum of the two reverse directed edges. Passing to the deck-anti-invariant subcomplex and quotienting by these boundaries identifies degree-one chains with one oriented generator per undirected edge, and its differential is precisely \(\partial_s\). For each balanced quadrilateral, choose a lifted start vertex in the signed cover. Balance ensures that its two length-two paths around the quadrilateral have the same lifted endpoint. Their difference is a permitted regular two-chain with boundary the lifted square; taking its deck-anti-invariant combination yields \(q_{ik;jl}\) (up to an invertible scalar). Consequently every cycle class is killed by a boundary, since the signed cycle space equals \(B_s\), and degree-one signed path homology vanishes.

## Verification

The included standalone `verify_signed_glmy.py` uses exact SymPy arithmetic. It exhausts all normalized sign patterns for six small parameter pairs (606 cases), comparing the dimension of the square span to the kernel of signed incidence. In 94 further cases it independently constructs the bidirected signed cover's anti-invariant degree-one/degree-two relations from backtracks and equal-endpoint two-path differences and checks vanishing first homology. These finite checks are reproducibility tests; the preceding argument supplies the all-parameter proof. Run: `python verify_signed_glmy.py` (Python 3 and SymPy required).

## Relationship to prior work

Bai, Li, and Yau (2026) introduce the real signed GLMY theory through signed double covers and describe its degree-zero response to balancedness. Chaplin's path-homology treatment explains the standard backtrack and two-path-difference generators in the regular degree-two chain group. Kempton, Münch, and Yau discuss graph covers, gain graphs, and three-/four-cycle relations. The present claim concerns a distinct, explicit all-signings spanning property for the complete-bipartite family and its degree-one vanishing consequence; the general signed construction and ordinary path-chain relations are prior work.

## Limitations

The result is specific to complete bipartite graphs, real anti-invariant regular signed GLMY homology, and dimension one. Higher path homology, arbitrary graph signings, and **integral deck-coinvariant** versions are not determined here. Unbalanced covers can still have nonzero ordinary first graph homology: for instance, the unbalanced four-cycle lifts to an eight-cycle. No assertion of independent external audit or exhaustive literature uniqueness is made. The full Bai–Li–Yau preprint was not accessible in this review, leaving a residual risk of uninspected equivalent statements.

## References

- Bai, Li, and Yau, *Signed GLMY Homology of Signed Graphs via Double Covers*, arXiv:2609.25557, first publicly posted 2026-09-22.
- T. Chaplin, *First Betti number of the path homology of random directed graphs*, arXiv:2111.13493; published in *Journal of Applied and Computational Topology*, DOI 10.1007/s41468-022-00108-3. Section on first homology and regular path relations.
- M. Kempton, F. Münch, and S.-T. Yau, *Relationships between cycle spaces, gain graphs, graph coverings, path homology, and graph curvature*, arXiv:1710.01264.
