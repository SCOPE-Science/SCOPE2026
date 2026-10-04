# The finite mapping space from \(X_2\) to \(X_1\) has circle core
## Finding
Let \(X_2=S^0\oplus S^0\oplus S^0\) and \(X_1=S^0\oplus S^0\) be the canonical six-point and four-point minimal finite sphere models, with each \(S^0\) a two-point antichain and \(\oplus\) the ordinal sum. The compact-open mapping space \(\operatorname{Map}(X_2,X_1)\) has exactly \(44\) points. Its four constant maps form a subspace canonically homeomorphic to \(X_1\), and there is a sequence of \(40\) Stong beat-point deletions reducing the full mapping space exactly to this constant-map subspace. Hence the constant maps are a strong deformation retract, the Stong core of \(\operatorname{Map}(X_2,X_1)\) is \(X_1\), and its order complex has homotopy type \(S^1\).

This gives more than the statement that all maps \(X_2\to X_1\) are homotopic: the entire finite function space retains a noncontractible core, namely the four-point minimal circle.

## Assumptions and scope
A finite \(T_0\)-space is identified with its specialization poset. Write \(S^0\) for a two-point antichain and \(P\oplus Q\) for the ordinal sum, so every point of \(P\) is below every point of \(Q\). Define
\[
X_2=S^0\oplus S^0\oplus S^0,\qquad X_1=S^0\oplus S^0.
\]
Thus \(X_2\) has three two-point levels \(A<B<C\), while \(X_1\) has a lower two-point level \(L\) and an upper two-point level \(U\). Barmak and Minian identify these as the canonical minimal finite models of the \(2\)-sphere and \(1\)-sphere, respectively.

The mapping space means the compact-open space of continuous maps \(X_2\to X_1\). For finite spaces, May's function-space description identifies its specialization order with the pointwise order
\[
f\le g\quad\Longleftrightarrow\quad f(x)\le g(x)\ \text{for every }x\in X_2.
\]

The theorem is only asserted for this exact canonical pair \(X_2\to X_1\). No statement about arbitrary finite sphere models or all cross-height weak orders is inferred from the finite computation.

## Proof
Continuous maps between finite \(T_0\)-spaces are exactly order-preserving maps. Count them by the image of the middle source level \(B\).

If the two points of \(B\) have distinct images, they cannot be two distinct points of \(L\), because then no point of \(X_1\) lies below both; similarly, they cannot be two distinct points of \(U\), because then no point lies above both. Hence the two images consist of one \(\ell\in L\) and one \(u\in U\). The lower source level \(A\) is then forced constantly to \(\ell\), the upper source level \(C\) is forced constantly to \(u\), and the two points of \(B\) can be assigned \(\ell,u\) in either order. This contributes
\[
2\cdot 2\cdot 2=8
\]
maps.

If \(B\) is constant at some \(\ell\in L\), then \(A\) is forced constantly to \(\ell\), while each point of \(C\) may independently map to \(\ell\) or either point of \(U\). This gives \(3^2=9\) maps for each of the two choices of \(\ell\), hence \(18\). Dually, if \(B\) is constant at some \(u\in U\), then \(C\) is forced constantly to \(u\), while each point of \(A\) has three choices, giving another \(18\). Therefore
\[
|\operatorname{Map}(X_2,X_1)|=8+18+18=44.
\]

It remains to determine the finite homotopy type of this \(44\)-point mapping poset. The accompanying exact certificate lists \(40\) successive Stong beat-point deletions. At every step it records either the unique minimal element strictly above the deleted point or the unique maximal element strictly below it, in the current surviving pointwise poset. The verifier reconstructs all \(44\) order-preserving maps from the \(4^6=4096\) set maps and checks every one of these beat-point conditions against the complete surviving poset.

After the \(40\) deletions, precisely the four constant maps remain:
\[
c_y(x)=y\qquad (y\in X_1).
\]
Their induced order is exactly
\[
c_y\le c_z\quad\Longleftrightarrow\quad y\le z,
\]
so the constant-map subspace is canonically homeomorphic to \(X_1\). It has no beat points. A beat-point deletion is a strong deformation retract, and a composition of these \(40\) deletions therefore gives a strong deformation retraction of \(\operatorname{Map}(X_2,X_1)\) onto the constant-map copy of \(X_1\). By uniqueness of finite cores, that copy is the Stong core.

Finally, the order complex of \(X_1\) is the four-cycle \(K_{2,2}\), hence is homeomorphic to \(S^1\). Therefore the order complex of the full mapping space has homotopy type \(S^1\).

## Verification
Run
`python3 verify.py`
in the directory containing `verify.py` and `beat_certificate.json`. The script independently enumerates every function \(X_2\to X_1\), filters exactly the order-preserving maps, reconstructs the pointwise order, and checks all \(40\) certified beat-point deletions. It also verifies that the four survivors are exactly the constant maps, that their induced order is \(X_1\), and that none is a beat point.

The expected terminal line is:
`VERIFY_OK maps=44 deletions=40 up=20 down=20 core=4`

The certificate is exhaustive for this finite mapping space. It is not evidence for any unasserted infinite family.

## Relationship to prior work
Barmak and Minian prove that the canonical \(2n+2\)-point spaces \(S^nS^0\) are the unique minimal finite models of spheres at that cardinality, and recall Stong's theory of beat points and cores. Their work supplies the objects and the reduction theorem but does not compute this function space.

May gives the compact-open topology on finite function spaces and proves that its specialization order is the pointwise order; he also identifies homotopy classes with path components. That framework explains why the pointwise mapping poset is the relevant object, but his notes do not calculate the \(X_2\to X_1\) mapping space or its core.

Speed studies the Möbius function of the general hom-poset \(\operatorname{Hom}(P,Q)\). That result concerns an incidence-algebra invariant of the hom-poset and does not determine its Stong core or supply this \(44\)-point calculation.

The present statement is also strictly stronger than merely knowing that all maps \(X_2\to X_1\) lie in one homotopy class: path connectedness of a finite mapping space does not imply contractibility or identify its core. Here the core is noncontractible and is exactly \(X_1\).

## Limitations
The result is an exact theorem for the canonical six-point \(X_2\) and four-point \(X_1\). The proof does not classify mapping-space cores for \(X_n\to X_m\) in general. The beat-point certificate is finite and exhaustive, but no closed-form deletion scheme for a parameterized family is claimed.

A residual bibliographic risk is that an older computation of this exact small hom-poset may exist in non-indexed notes or tables. The inspected finite-space, function-space, and hom-poset sources did not contain this calculation.

## References
1. J. A. Barmak and E. G. Minian, *Minimal Finite Models*, arXiv:math/0611156v1, 6 November 2006.
2. J. A. Barmak and E. G. Minian, *Simple Homotopy Types and Finite Spaces*, arXiv:math/0611158v1, 6 November 2006.
3. J. P. May, *Finite Topological Spaces*, Notes for REU, revised 2010, Section 7.
4. T. P. Speed, *On the Möbius function of Hom(P,Q)*, Bulletin of the Australian Mathematical Society 29 (1984), 39–46, DOI 10.1017/S0004972700021250.
