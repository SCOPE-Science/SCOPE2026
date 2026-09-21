# Exact ideal profile for differences of bounded graph projections

## Statement

Let \(H,K\) be Hilbert spaces and let \(A,B\in\mathcal B(H,K)\). Denote by
\(P_A,P_B\) the orthogonal projections in \(H\oplus K\) onto the graphs
\[
G(A)=\{(x,Ax):x\in H\},\qquad G(B)=\{(x,Bx):x\in H\}.
\]
Set
\[
C_T=(I+T^*T)^{-1/2}\quad\text{on }H,\qquad
D_T=(I+TT^*)^{-1/2}\quad\text{on }K
\]
for \(T=A,B\), and define the two normalized relative differences
\[
S_{A,B}=D_B(A-B)C_A,\qquad
S_{B,A}=D_A(B-A)C_B.
\]

Then there is a canonical unitary \(U_A:H\oplus K\to H\oplus K\), adapted to
\(G(A)\oplus G(A)^\perp\), such that
\[
\boxed{
U_A^*\,|P_A-P_B|\,U_A
=
|S_{A,B}|\oplus |S_{B,A}^*|.
}
\tag{1}
\]
Thus the full ideal-theoretic size of the difference of the graph projections is
the orthogonal sum of two normalized copies of \(A-B\), one in each direction.

### Consequences

1. **Finite-rank doubling.** If \(A-B\) has finite rank \(r\), then
\[
\boxed{\operatorname{rank}(P_A-P_B)=2r.}
\tag{2}
\]
In particular, the qualitative finite-rank equivalence for bounded graph
perturbations admits an exact rank formula.

2. **Compact singular-value profile.** If \(A-B\) is compact, the nonzero singular
values of \(P_A-P_B\), counted with multiplicity, are exactly the multiset union
of the singular values of \(S_{A,B}\) and \(S_{B,A}\).

Writing
\[
c(A,B)=\frac{1}{\sqrt{(1+\|A\|^2)(1+\|B\|^2)}},
\]
one has, for every \(n\ge1\),
\[
c(A,B)s_n(A-B)
\le s_{2n}(P_A-P_B)
\le s_{2n-1}(P_A-P_B)
\le s_n(A-B).
\tag{3}
\]

3. **Exact Schatten identity.** For every \(0<p<\infty\),
\[
P_A-P_B\in S_p
\quad\Longleftrightarrow\quad
A-B\in S_p,
\tag{4}
\]
and whenever these conditions hold,
\[
\boxed{
\|P_A-P_B\|_{S_p}^p
=
\|S_{A,B}\|_{S_p}^p+\|S_{B,A}\|_{S_p}^p.
}
\tag{5}
\]
Consequently,
\[
2^{1/p}c(A,B)\|A-B\|_{S_p}
\le
\|P_A-P_B\|_{S_p}
\le
2^{1/p}\|A-B\|_{S_p}.
\tag{6}
\]
For \(p\ge1\), this makes the bounded graph map locally bi-Lipschitz in Schatten
\(p\)-norm on every operator-norm bounded set; for \(0<p<1\), the same two-sided
estimate holds for the usual Schatten quasi-norm.

4. **Exact essential-norm formula.** Without assuming compactness,
\[
\boxed{
\|P_A-P_B\|_{\mathrm e}
=
\max\{\|S_{A,B}\|_{\mathrm e},\|S_{B,A}\|_{\mathrm e}\}.
}
\tag{7}
\]
Hence
\[
c(A,B)\|A-B\|_{\mathrm e}
\le
\|P_A-P_B\|_{\mathrm e}
\le
\|A-B\|_{\mathrm e}.
\tag{8}
\]
The known equivalence
\[
P_A-P_B\text{ compact}\iff A-B\text{ compact}
\]
is recovered immediately.

5. **A compact-difference geodesic consequence.** When \(H=K\), if \(A-B\) is
compact, then \(G(A)\) and \(G(B)\) can be joined by a minimal geodesic in the
Grassmann manifold. Neither \(A\) nor \(B\) need be compact.

## Proof

For \(T\in\mathcal B(H,K)\), define
\[
J_T:H\to H\oplus K,\qquad
J_Tx=(C_Tx,TC_Tx),
\]
and
\[
V_T:K\to H\oplus K,\qquad
V_Ty=(-T^*D_Ty,D_Ty).
\]
Since \(C_T\) commutes with \(T^*T\) and \(D_T\) commutes with \(TT^*\),
\[
J_T^*J_T
=
C_T(I+T^*T)C_T
=
I_H,
\]
while
\[
V_T^*V_T
=
D_T(I+TT^*)D_T
=
I_K.
\]
Moreover,
\[
J_T^*V_T=0.
\]
Thus \(J_T\) and \(V_T\) are isometries onto \(G(T)\) and \(G(T)^\perp\),
respectively, and
\[
U_T=[\,J_T\ \ V_T\,]:H\oplus K\to H\oplus K
\]
is unitary. In particular,
\[
P_T=J_TJ_T^*.
\]

The cross terms are especially simple:
\[
V_B^*J_A
=
D_B(A-B)C_A
=
S_{A,B},
\tag{9}
\]
and
\[
V_A^*J_B
=
D_A(B-A)C_B
=
S_{B,A}.
\tag{10}
\]

Put \(\Delta=P_A-P_B\). Since \(\Delta\) is selfadjoint and
\[
\Delta^2=P_A+P_B-P_AP_B-P_BP_A,
\]
a direct multiplication gives
\[
P_A\Delta^2=\Delta^2P_A=P_A-P_AP_BP_A.
\]
Hence \(\Delta^2\) is block diagonal relative to
\(G(A)\oplus G(A)^\perp\).

On \(G(A)\), equations (9) and \(I-P_B=V_BV_B^*\) give
\[
J_A^*\Delta^2J_A
=
J_A^*(I-P_B)J_A
=
(V_B^*J_A)^*(V_B^*J_A)
=
S_{A,B}^*S_{A,B}.
\]
On \(G(A)^\perp\), equations (10) and \(P_B=J_BJ_B^*\) give
\[
V_A^*\Delta^2V_A
=
V_A^*P_BV_A
=
(V_A^*J_B)(V_A^*J_B)^*
=
S_{B,A}S_{B,A}^*.
\]
Therefore
\[
U_A^*\Delta^2U_A
=
S_{A,B}^*S_{A,B}\oplus S_{B,A}S_{B,A}^*.
\]
Taking positive square roots proves (1).

Each of \(C_A,C_B,D_A,D_B\) is invertible, with
\[
\|C_T\|,\|D_T\|\le1,\qquad
\|C_T^{-1}\|,\|D_T^{-1}\|\le\sqrt{1+\|T\|^2}.
\tag{11}
\]
Thus \(S_{A,B}\) and \(S_{B,A}\) have the same finite rank as \(A-B\).
Equation (1) now proves (2).

If \(A-B\) is compact, the ideal inequality
\[
s_n(RXS)\le\|R\|\,s_n(X)\,\|S\|
\]
and (11) imply, for both directed terms,
\[
c(A,B)s_n(A-B)\le s_n(S_{\bullet,\bullet})\le s_n(A-B).
\tag{12}
\]
Since (1) says that the singular-value sequence of \(\Delta\) is the decreasing
rearrangement of the two directed sequences, (3) follows. Summing the \(p\)-th
powers of this multiset identity gives (5); (12) gives (4) and (6).

The essential norm is invariant under unitary conjugation, unchanged on passing
from \(X\) to \(|X|\), and on a finite direct sum equals the maximum of the
essential norms of the summands. Hence (1) yields (7). Applying the same
two-sided multiplication estimates in the Calkin algebra gives (8).

For the final geodesic consequence, assume \(H=K\) and \(A-B\) compact. The
bounded-graph geodesic criterion is
\[
\dim\ker(I+B^*A)=\dim\ker(I+A^*B).
\tag{13}
\]
Now
\[
I+B^*A=(I+A^*A)+(B^*-A^*)A
\]
is a compact perturbation of the positive invertible operator \(I+A^*A\).
Therefore it is Fredholm of index zero. Its adjoint is \(I+A^*B\), so (13)
holds. This proves the stated existence of a minimal Grassmann geodesic.

## Relation to known results

Azizov, Behrndt, Jonas and Trunk (2009) use differences of graph projections to
define finite-rank and compact perturbations of closed operators and relations.
For bounded \(A,B\), their Corollary 3.5 proves
\[
P_A-P_B\text{ finite rank}\iff A-B\text{ finite rank},
\]
and Corollary 4.6 proves
\[
P_A-P_B\text{ compact}\iff A-B\text{ compact}.
\]
No Schatten-class refinement or exact rank formula was located in the inspected text.

Andruchow (2015) studies the graph map inside the Grassmann manifold. In a
fixed chart based at the horizontal subspace, Proposition 4.1 and Corollary 4.5
identify Schatten-\(p\) graph coordinates with the corresponding restricted
Grassmannian component. That one-base result is not claimed as new here.

The contribution claimed here is the two-graph identity (1) for arbitrary
bounded \(A,B\), and the exact two-directed singular-value, rank, Schatten and
essential-norm consequences (2)--(8). The geodesic corollary combines this
compact-difference viewpoint with the bounded-graph criterion used in current
Grassmannian work.

## Originality and limitations

Originality is claimed **to the best of our knowledge** only for the exact
two-graph ideal profile and the consequences explicitly identified above.

Targeted searches covered graph projections, differences of graph projections,
finite-rank and compact graph perturbations, Schatten ideals, trace ideals,
singular values, approximation numbers, gap metrics, and Grassmannian graph
charts. The 2009 perturbation paper was inspected at its bounded finite-rank and
compact corollaries, and full-text searches located no occurrence of “Schatten”
or “trace class.” The 2015 graph-map paper explicitly contains a fixed-base
Schatten result, which is therefore excluded from the novelty claim. A current
2026 paper on graphs in the Grassmann manifold was also checked: it treats
bounded graph charts, compact graphs and geodesics, but no Schatten treatment was
located in the inspected text.

A residual literature risk remains. K. Y. Chung's 1993 paper *Subspaces and
graphs*, and older two-subspace/canonical-angle literature, were not exhaustively
inspected for an equivalent singular-value statement in different terminology.
Because (1) is an elementary but structurally useful block identity, an older
unstated or differently phrased version is plausible. The originality claim is
therefore deliberately limited to the best of our knowledge.

The theorem is stated only for bounded operators. No corresponding exact profile
is asserted here for general closed unbounded operators or linear relations.

## References

1. T. Ya. Azizov, J. Behrndt, P. Jonas, C. Trunk,
   “Compact and Finite Rank Perturbations of Closed Linear Operators and Relations
   in Hilbert Spaces,” *Integral Equations and Operator Theory* 63 (2009), 151–163.
   https://doi.org/10.1007/s00020-008-1650-1
2. E. Andruchow, “Parametrizing projections with selfadjoint operators,”
   *Linear Algebra and its Applications* 466 (2015), 307–328.
   https://doi.org/10.1016/j.laa.2014.10.029
3. K. Y. Chung, “Subspaces and graphs,” *Proceedings of the American Mathematical
   Society* 119 (1993), 141–146.
4. E. Andruchow, L. Recht, A. Varela,
   “Graphs of operators as points in the Grassmann manifold,” arXiv:2608.30120
   (2026). https://arxiv.org/abs/2608.30120
