# A Brauer-tree cover for the nonmonomial endomorphism algebras \(B_m\)
## Finding
For every integer \(m\ge 1\), consider the Liu--Xin Example 6.3 family
\[
A_m=kQ/R_Q^{3m+1},\qquad T_m=S_1\oplus P_1\oplus P_3,
\]
and write
\[
B_m=\operatorname{End}_{A_m}(T_m).
\]
Liu and Xin prove that \(T_m\) is a Gorenstein-projective \(\tau\)-tilting module and give the presentation
\[
B_m\cong kQ_B/\langle uv,\ ub,\ av,\ vu-(ba)^m\rangle,
\]
where
\[
u:S_1\to P_1,
\quad v:P_1\to S_1,
\quad b:P_1\to P_3,
\quad a:P_3\to P_1.
\]
They also prove \(\dim_k B_m=4m+5\) and that \(B_m\) admits no monomial presentation.

Define
\[
C_m=kQ_B/\langle ub,\ av,\ vu-(ba)^m\rangle.
\]
Then \(C_m\) is the Brauer tree algebra of a three-edge path whose two internal vertices have multiplicities \(1\) and \(m\). Moreover,
\[
B_m\cong C_m/\langle uv\rangle,
\]
and \(uv\) spans a nonzero one-dimensional two-sided socle ideal of \(C_m\). Consequently
\[
\dim_k C_m=4m+6,
\qquad
\dim_k B_m=4m+5,
\]
and \(B_m\) is representation-finite for every \(m\ge1\).

Thus the entire explicit non-G-condition family in Example 6.3 gives affirmative instances of Liu--Xin Problem 5.4. This does not settle that problem for arbitrary representation-finite string algebras.

## Assumptions and scope
The field \(k\) is algebraically closed, as in the Liu--Xin source. Paths are composed left to right. The parameter \(m\) is an arbitrary integer with \(m\ge1\).

Let the Brauer tree have vertices \(x_0,x_1,x_2,x_3\) and edges
\[
e_1=x_0x_1,
\qquad e_2=x_1x_2,
\qquad e_3=x_2x_3.
\]
Give \(x_0\) and \(x_3\) multiplicity \(1\), give \(x_1\) multiplicity \(1\), and give \(x_2\) multiplicity \(m\). The endpoints \(x_0,x_3\) are truncated. Identify the quiver vertices corresponding to \(e_1,e_2,e_3\) with \(S_1,P_1,P_3\), respectively. The cyclic ordering at \(x_1\) yields arrows \(u:S_1\to P_1\) and \(v:P_1\to S_1\); the cyclic ordering at \(x_2\) yields arrows \(b:P_1\to P_3\) and \(a:P_3\to P_1\).

No assertion is made that \(B_m\) itself is a Brauer tree algebra. The claim is that it is a one-dimensional socle quotient of the Brauer tree algebra \(C_m\).

## Proof
For the three-edge Brauer tree just described, the special cycles at the internal vertex \(x_1\) are \(uv\) and \(vu\), and the special cycles at \(x_2\) are \(ba\) and \(ab\). At the central edge \(e_2\), both endpoints are nontruncated. The type-I Brauer-graph relation is therefore
\[
vu-(ba)^m=0.
\]
The only composable arrow pairs that do not lie on one of the four special cycles are \(ub\) and \(av\). Hence the type-III relations are
\[
ub=0,
\qquad av=0.
\]

The standard minimal-relation criterion for Brauer graph algebras says that type-I and type-III relations are always minimal, while a type-II relation at a truncated edge is minimal only when the immediate successor at the other endpoint is itself truncated at its other endpoint. Here the successor of \(e_1\) at \(x_1\) is \(e_2\), which is not truncated at \(x_2\); similarly for \(e_3\). Thus no additional type-II relation is needed in a minimal generating set. Concretely, the relevant type-II consequences follow already from the three displayed relations. For example,
\[
(uv)u=u(vu)=u(ba)^m=0
\]
because \(ub=0\), and
\[
(ab)^m a=a(ba)^m=avu=0
\]
because \(av=0\). The remaining cycle-ending relations follow analogously. Hence the Brauer graph algebra of this tree is precisely
\[
C_m=kQ_B/\langle ub,\ av,\ vu-(ba)^m\rangle.
\]
Because the Brauer graph is a tree, \(C_m\) is a Brauer tree algebra and therefore has finite representation type.

The Liu--Xin presentation differs from the presentation of \(C_m\) by exactly the additional relation \(uv=0\). Therefore
\[
B_m\cong C_m/\langle uv\rangle.
\]
The path \(uv\) is nonzero in \(C_m\): it is the special-cycle power at the edge \(e_1\), and it is not among the minimal relations above. It is annihilated by the radical on both sides. Indeed, the only outgoing arrow from its base vertex is \(u\), and
\[
(uv)u=u(vu)=u(ba)^m=0;
\]
the only incoming arrow is \(v\), and
\[
v(uv)=(vu)v=(ba)^m v=0
\]
because the last arrow of \((ba)^m\) is \(a\) and \(av=0\). Hence \(k(uv)\) is a one-dimensional two-sided socle ideal.

A direct path reduction gives a basis of \(C_m\) consisting of the source basis for \(B_m\), together with the single additional path \(uv\). Thus
\[
\dim_k C_m=4m+6.
\]
This also agrees with the source value \(\dim_k B_m=4m+5\).

Finally, finite representation type passes to quotients: every module over a quotient algebra inflates to a module over the original algebra, and its endomorphism ring and decomposition behavior are unchanged. Since \(C_m\) is representation-finite, so is its quotient \(B_m\).

## Verification
The proof was checked at the level of quivers, path orientation, relation types, and all boundary cases \(m\ge1\). In particular, the source composes paths left to right, so \(vu\) and \(ba\) are loops at the central vertex \(P_1\), exactly as required by the type-I Brauer-tree relation.

The dimension check is independent of representation-type theory: the source exhibits \(4m+5\) linearly independent basis maps for \(B_m\), while adjoining the single nonzero socle path \(uv\) gives \(4m+6\) paths for \(C_m\). No finite experiment is used as a substitute for the all-\(m\) proof.

## Relationship to prior work
Liu and Xin formulate Problem 5.4 asking whether \(\operatorname{End}_A(T)\) is representation-finite whenever \(A\) is a representation-finite string algebra and \(T\) is a basic Gorenstein-projective support \(\tau\)-tilting module. Their Example 6.3 is deliberately outside the G-condition. They prove that \(A_m\) is representation-finite, that \(T_m\) has the required Gorenstein-projective \(\tau\)-tilting property, and that \(B_m\) is nonmonomial; they explicitly state that this nonmonomiality does not decide the representation type of \(B_m\) and therefore does not settle Problem 5.4.

Schroll's survey gives the standard type-I, type-II, and type-III relations for Brauer graph algebras, the minimality criterion used above, and the characterization that a Brauer graph algebra has finite representation type exactly when its graph is a tree. Applying those standard structural facts to the exact Liu--Xin presentation yields the new representation-type conclusion for their whole family.

Focused searches for the exact relation pattern, the Example 6.3 family, Brauer-tree quotients, and equivalent representation-finite formulations did not locate a prior statement identifying these \(B_m\) as socle quotients of a three-edge Brauer tree algebra.

## Limitations
This is a family-level result, not a solution of Liu--Xin Problem 5.4. It uses the exact presentation of Example 6.3 and does not show that arbitrary endomorphism algebras outside the G-condition admit Brauer-tree covers. The motivating preprint is very recent, so an equivalent observation could exist in material not yet indexed. The originality conclusion is therefore a literature-based assessment rather than an absolute uniqueness claim.

## References
1. Y.-Z. Liu and Z. Xin, *Endomorphism algebras of Gorenstein-projective modules over string algebras*, arXiv:2610.00937v1, 2026.
2. S. Schroll, *Brauer graph algebras: a survey on Brauer graph algebras, associated gentle algebras and their connections to cluster theory*, arXiv:1612.00061v3, 2017.
