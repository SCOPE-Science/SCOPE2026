# Mixed tensor products in Lam’s delooping family retain the smaller obstruction
## Finding
Let \(k\) be an algebraically closed field. For each integer \(r\ge2\), let \(A_r=kQ_r/(\operatorname{rad}kQ_r)^2\), where \(Q_r\) has vertices \(1,\ldots,r+2\), a loop \(\delta:1\to1\), arrows \(\alpha:1\to2\) and \(\gamma:r+2\to2\), and arrows \(\beta_i:i+1\to i+2\) for \(1\le i\le r-1\). Let \(T_r\) denote the simple right \(A_r\)-module at vertex \(r+2\).

For all \(m,n\ge2\), set
\[
R_{m,n}=A_m\otimes_k A_n,\qquad S_{m,n}=T_m\otimes_k T_n,\qquad q=\min\{m,n\}.
\]
Then
\[
\operatorname{dell}_{R_{m,n}}(S_{m,n})>q.
\]
In particular,
\[
\operatorname{dell}(A_m\otimes_k A_n)\ge q+1.
\]
Lam proves \(\operatorname{dell}(A_r)=1\) for every \(r\ge2\), so the nonadditivity defect satisfies
\[
\operatorname{dell}(A_m\otimes_k A_n)-\operatorname{dell}(A_m)-\operatorname{dell}(A_n)\ge \min\{m,n\}-1,
\]
with the evident extended-value interpretation if the left side is infinite. Hence the obstruction is unbounded even along genuinely rectangular pairs, for example along \((m,n)=(r,2r)\).

## Assumptions and scope
All algebras are finite-dimensional over the algebraically closed field \(k\), and all modules are finitely generated right modules, matching Lam’s conventions. The claim concerns the ordinary delooping level, not the derived delooping level. It is a lower bound; no exact value of \(\operatorname{dell}(A_m\otimes_k A_n)\) is asserted.

Write \(P_i^{(r)}\) for the indecomposable projective at vertex \(i\) of \(A_r\). Lam’s minimal projective resolution of \(T_r\) is
\[
0\longrightarrow P_{r+1}^{(r)}\longrightarrow P_r^{(r)}\longrightarrow\cdots\longrightarrow P_2^{(r)}\longrightarrow P_{r+2}^{(r)}\longrightarrow T_r\longrightarrow0,
\]
and Lam computes
\[
\operatorname{Ext}_{A_r}^i(T_r,A_r)\cong
\begin{cases}
k,&i=1\text{ or }i=r,\\0,&\text{otherwise.}\end{cases}
\]
Lam also proves \(\operatorname{dell}(A_r)=\operatorname{dell}_{A_r}(T_r)=1\).

## Proof
Fix \(m,n\ge2\), let \(q=\min\{m,n\}\), and abbreviate \(R=R_{m,n}\), \(S=S_{m,n}\).

By the Künneth formula applied to the displayed Ext profiles,
\[
\operatorname{Ext}_{R}^j(S,R)
\cong
\bigoplus_{a+b=j}
\operatorname{Ext}_{A_m}^a(T_m,A_m)\otimes_k
\operatorname{Ext}_{A_n}^b(T_n,A_n).
\]
Therefore the only possible positive degrees are
\[
2,\quad m+1,\quad n+1,\quad m+n,
\]
with multiplicities added when two of these degrees coincide. In particular,
\[
\operatorname{Ext}_{R}^j(S,R)=0\qquad(3\le j\le q).
\]
Every finitely generated projective \(R\)-module is a direct summand of a finite direct sum of copies of \(R\), so the same vanishing holds with \(R\) replaced by an arbitrary projective target. Dimension shifting now gives
\[
\operatorname{Ext}_{R}^1(\Omega^{j-1}S,Q)=0\qquad(3\le j\le q)
\]
for every projective \(Q\). Consequently, in the short exact sequence from the minimal projective resolution
\[
0\longrightarrow\Omega^jS\longrightarrow P\longrightarrow\Omega^{j-1}S\longrightarrow0,
\]
the inclusion \(\Omega^jS\to P\) is a left projective approximation. Using the left adjoint \(\Sigma\) to syzygy, exactly as in Lam’s proof, this yields
\[
\Sigma\Omega^jS\cong\Omega^{j-1}S\qquad(3\le j\le q),
\]
and hence
\[
\Sigma^{q+1}\Omega^qS\cong\Sigma^3\Omega^2S.
\]

It remains to locate the support of the right side. The degree-two part of the tensor product of the two minimal resolutions uses only \(P_{m+2}^{(m)},P_2^{(m)},P_3^{(m)}\) in the first factor and \(P_{n+2}^{(n)},P_2^{(n)},P_3^{(n)}\) in the second. Directly from those projectives,
\[
\Omega^2S
\]
has top supported at
\[
(m+2,3),\quad(2,2),\quad(3,n+2)
\]
and socle supported at
\[
(2,3),\quad(3,2).
\]
Lam’s three-step left-projective-approximation calculation for the diagonal case only uses the projective types \(P_{(1,1)}\), \(P_{(m+2,2)}\), \(P_{(2,n+2)}\), and \(P_{(m+2,n+2)}\), followed by finite direct sums of \(P_{(1,1)}\). Their Loewy structures depend only on the local arrows at vertices \(1,2,3\) and at the distinguished endpoint vertices. Those local structures are identical in the two factors even when \(m\ne n\). Thus the same calculation gives
\[
U:=\Sigma^3\Omega^2S
\]
with support contained in the four-vertex set
\[
W=\{(1,1),(1,2),(2,1),(2,2)\}.
\]

Now put
\[
V=\{(i,j):1\le i\le m+1,\ 1\le j\le n+1\}.
\]
This is successor-closed in the Cartesian product quiver of \(R\), and \(W\subseteq V\). Lam’s support lemma therefore gives
\[
\operatorname{supp}(\Omega^tU)\subseteq V\qquad(t\ge0).
\]
In particular, \(\Omega^{q+1}U\) is supported in \(V\).

On the other hand, the tensor product of the two displayed minimal resolutions is again minimal. Its degree-\(q\) term contains the summand
\[
P_{m+2}^{(m)}\otimes_k P_{q+1}^{(n)},
\]
because \(q\le n\). The vertical component of the total differential is nonzero at the vertex
\[
v=(m+2,q+1).
\]
No other degree-\(q\) summand has support at \(v\), since every other summand has a first-coordinate projective different from \(P_{m+2}^{(m)}\). Hence
\[
v\in\operatorname{supp}(\Omega^qS).
\]
But \(v\notin V\). Since the tensor resolution is minimal, \(\Omega^qS\) has no projective direct summand. Thus at least one nonprojective indecomposable summand of \(\Omega^qS\) has support outside \(V\).

If \(\operatorname{dell}_R(S)\le q\), the Gélinas criterion used by Lam would make \(\Omega^qS\) a stable retract of
\[
\Omega^{q+1}\Sigma^{q+1}\Omega^qS\cong\Omega^{q+1}U.
\]
The target is supported in \(V\). By Krull–Schmidt, a nonprojective indecomposable summand of the source of a stable retract must occur among the nonprojective indecomposable summands of the target; a projective summand cannot absorb it. This contradicts the support outside \(V\). Therefore
\[
\operatorname{dell}_R(S)>q.
\]
The algebra-level and defect bounds follow immediately from the definition of \(\operatorname{dell}(R)\) as the supremum over simple modules and Lam’s identity \(\operatorname{dell}(A_r)=1\).

## Verification
The proof uses three source-level ingredients that were checked in the full text: Lam’s family and identity \(\operatorname{dell}(A_r)=1\), Lam’s Ext profile for \(T_r\), and Lam’s support/left-approximation argument. The mixed extension was then reconstructed independently: the Künneth degrees were recomputed, the local three-step approximation was checked to involve no tail projectives, the successor-closed set was checked in the rectangular product quiver, and the outside-support vertex \((m+2,q+1)\) was traced in the minimal total tensor resolution.

The accompanying program `verify_mixed_delooping.py` checks the degree and support combinatorics for every pair \(2\le m,n\le12\), including the coalescing Ext degrees when parameters agree. It reports `CHECK_OK pairs=121 range=2..12`. These finite checks are stress tests only; the theorem above is proved symbolically for all \(m,n\ge2\).

## Relationship to prior work
Lam’s 2026 paper constructs the family \(A_r\), proves \(\operatorname{dell}(A_r)=1\), and proves an unbounded lower bound for the diagonal self-tensors \(A_r\otimes_k A_r\). The inspected paper formulates and proves the family only with the same parameter in both tensor factors; searches of the full text for mixed notation and mixed-product terminology found no rectangular statement. The present result keeps Lam’s mechanism but separates the two parameters and shows that the smaller arm controls the surviving obstruction.

Guo’s tensor-product results concern the derived delooping level and impose finite global dimension on one factor (or stronger related hypotheses). Lam’s \(A_r\) has infinite global dimension because of the loop at vertex \(1\), and the claim here is about ordinary delooping. Thus those theorems neither imply nor dominate the rectangular lower bound above. Guo’s dissertation contains the same tensor-product direction and predates Lam’s family.

## Limitations
The result proves a lower bound, not an exact formula for \(\operatorname{dell}(A_m\otimes_k A_n)\). It uses the algebraically closed base-field convention of Lam’s paper; no claim is made here about weakening that field hypothesis. The finite checker is not an infinite proof. A residual originality risk remains that a very recent or poorly indexed source could have independently written down the same rectangular extension, although targeted semantic and full-text searches found no such statement.

## References
1. Ryan Lam, *Tensor Product Does Not Behave Additively on Delooping Level*, arXiv:2609.39745v1, 2026.
2. Ruoyu Guo, *Symmetry of Derived Delooping Level*, arXiv:2406.00253v2, 2025 version.
3. Ruoyu Guo, *Developments in the finitistic dimension conjecture*, doctoral dissertation, DOI:10.48617/etd.1424, 2025.
4. Vincent Gélinas, *The depth, the delooping level and the finitistic dimension*, Advances in Mathematics 394 (2022), 108052.
