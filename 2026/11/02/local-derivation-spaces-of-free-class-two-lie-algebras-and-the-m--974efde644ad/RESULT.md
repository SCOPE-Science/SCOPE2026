# Local derivation spaces of free class-two Lie algebras and the modular exterior-square defect

## Finding
For any field \(k\), let \(V\) be a vector space of dimension \(n\ge3\), let \(W=\bigwedge^2 V\), and form the free class-two Lie algebra \(L=V\oplus W\) with \([v+w,v'+w']=v\wedge v'\). Define the derived exterior-square action
\[
\rho(A)(u\wedge v)=Au\wedge v+u\wedge Av,
\qquad A\in\operatorname{End}_k(V).
\]
A linear map \(T:L\to L\) is a local derivation if and only if it has the form
\[
T(v+w)=Pv+Qv+Rw,
\qquad P\in\operatorname{End}_k(V),\quad Q\in\operatorname{Hom}_k(V,W),
\]
with \(R\) belonging to the following explicit space:
\[
R\in\begin{cases}
\rho(\operatorname{End}_k(V)),&\operatorname{char}k\ne2,\\
\rho(\operatorname{End}_k(V))+k I_W,&\operatorname{char}k=2.
\end{cases}
\]
In characteristic two, the identity map \(I_W\) is not in the image of \(\rho\) for \(n\ge3\); it supplies one additional central-layer direction. Nevertheless, the dimension of the permissible \(R\)-space is \(n^2\) in every characteristic. Therefore
\[
\dim_k\operatorname{LocDer}(L)=2n^2+n\binom{n}{2},\qquad
\dim_k\operatorname{Der}(L)=n^2+n\binom{n}{2}.
\]
Inside the normal form, ordinary derivations are exactly those satisfying \(R=\rho(P)\). For a finite field \(\mathbb F_q\), these are vector spaces of cardinalities
\[
q^{2n^2+n\binom n2}\quad\text{and}\quad q^{n^2+n\binom n2},
\]
respectively. Thus the local-to-ordinary count ratio is \(q^{n^2}\), without dependence on the characteristic.

## Assumptions and scope
The field is arbitrary, including fields of characteristic two and fields with two elements. The algebra \(L\) is the free two-step nilpotent **alternating** Lie algebra on \(n\ge3\) generators; in characteristic two, alternating means \([x,x]=0\) and does not require an antisymmetric sign convention. A local derivation is required to be \(k\)-linear, and the matching derivation may depend on the point. No continuity, algebraic-closedness, or field-size restriction is assumed. We make no assertion about nonlinear two-local maps or arbitrary quotients of \(L\).

## Proof
**Step 1: ordinary derivations.** The commutator ideal and center both equal \(W\). Any derivation preserves \(W\). Since \(W=[V,V]\), an ordinary derivation is uniquely determined by its restriction \(v\mapsto Av+Bv\) on \(V\), with \(A\in\operatorname{End}(V)\) and \(B\in\operatorname{Hom}(V,W)\). On the commutator ideal it acts by \(\rho(A)\). Conversely, for any such \(A,B\), the operator
\[
D_{A,B}(v+w)=Av+Bv+\rho(A)w
\]
is a derivation. Its parameters are unique, giving \(n^2+n\binom n2\) dimensions.

**Step 2: evaluation condition for local derivations.** A linear local derivation \(T\) must preserve \(W\) because all ordinary derivations do. Hence it has a unique block form \(T(v+w)=Pv+Qv+Rw\). If \(v\ne0\), choose an arbitrary \(A\) with \(Av=Pv\), and then choose \(B\) so that
\[
Bv=Qv+Rw-\rho(A)w.
\]
Such \(B\) exists for every specified right-hand side, so any block map can be matched at every vector having nonzero \(V\)-component. At points in \(W\), the matching condition is precisely
\[
\forall w\in W\quad \exists A_w\in\operatorname{End}(V)
\quad Rw=\rho(A_w)w.\tag{1}
\]
It remains to classify this exterior-square algebraic reflexive hull.

**Step 3: tangent-space lemma, off-diagonal entries.** Fix a basis \(e_1,\ldots,e_n\). Because \(R(e_i\wedge e_j)\) must equal \(\rho(A_{ij})(e_i\wedge e_j)\), it belongs to \(e_i\wedge V+e_j\wedge V\). For each distinct triple \(i,j,h\), write \(c_{hi}^{(j)}\) for the coefficient of \(e_h\wedge e_j\) in \(R(e_i\wedge e_j)\). Applying condition (1) to the decomposable bivector \(e_i\wedge(e_j+e_l)\), for four distinct indices \(i,j,l,h\), forces \(c_{hi}^{(j)}=c_{hi}^{(l)}\). When \(n=3\) there is just one allowable \(j\) for each ordered pair \((h,i)\), so no compatibility is needed. Thus in every dimension \(n\ge3\) the coefficients are independent of the partner index. Choose an endomorphism \(A_0\) with off-diagonal entries \((A_0)_{hi}=c_{hi}^{(j)}\). Subtracting \(\rho(A_0)\) from \(R\) leaves a diagonal operator on the wedge basis:
\[
(R-\rho(A_0))(e_i\wedge e_j)=d_{ij}(e_i\wedge e_j),\quad d_{ij}=d_{ji}.
\]
Here the use of \(e_i\wedge e_j\) with reversed indices is merely a notation for the same coefficient, not an equality of oriented bivectors.

**Step 4: diagonal entries.** Evaluate condition (1) on \((e_i+e_h)\wedge(e_j+e_l)\), with four distinct indices. Its four coefficients must be tangent to a rank-one \(2\times2\) matrix. Consequently
\[
d_{ij}+d_{hl}=d_{il}+d_{hj}.\tag{2}
\]
For \(n=3\) there are no four-index constraints, and every triple of diagonal scalars has the form \(d_{ij}=a_i+a_j+c\). For \(n\ge4\), relation (2) likewise gives exactly this form. To see this without division, choose anchors \(1,2\). The four-index identities show \(d_{1i}-d_{2i}\) is independent of \(i\ge3\). Write this common difference as \(s\), put \(c=d_{12}+s\), \(a_1=0\) and \(a_j=d_{1j}-c\) for \(j>1\). The remaining four-index identities then give \(d_{ij}=a_i+a_j+c\) for every pair. Hence
\[
R=\rho(A_0+\operatorname{diag}(a_1,\ldots,a_n))+c I_W.\tag{3}
\]
For characteristic other than two, absorb \(cI_W\) into \(\rho((c/2)I_V)\). In characteristic two it is a potentially independent direction.

**Step 5: sufficiency, including characteristic two.** Every \(\rho(A)\) satisfies condition (1) using a single \(A\). The identity \(I_W\) also satisfies (1) over every field. Indeed, any alternating bivector admits a decomposition \(w=\sum_{r=1}^t u_r\wedge v_r\) with independent vectors \(u_1,v_1,\ldots,u_t,v_t\). Define \(A_w u_r=u_r\), \(A_w v_r=0\), and let \(A_w\) vanish on a complement. Then \(\rho(A_w)w=w\). Thus every map in (3) is locally induced. In conjunction with Step 2, this proves the iff classification.

**Step 6: dimensions and characteristic boundary.** When \(n\ge3\), the kernel of \(\rho\) is zero if \(\operatorname{char}k\ne2\), and consists precisely of scalar endomorphisms if \(\operatorname{char}k=2\). To check this, apply \(\rho(A)\) to all basis wedges: off-diagonal coefficients force \(A\) diagonal, and \(a_i+a_j=0\) for every pair forces the stated conclusion. Moreover, in characteristic two, the equations \(a_i+a_j=1\) for all distinct \(i,j\) are inconsistent when \(n\ge3\); hence \(I_W\notin\rho(\operatorname{End}V)\). Both characteristic cases give an \(n^2\)-dimensional permissible \(R\)-space. The independent \(P,Q,R\) blocks yield the asserted local dimension, and the derivation dimension follows from Step 1. Finite-field counts follow from vector-space cardinalities.

## Verification
A standalone deterministic prime-field checker accompanies this result. It constructs all elementary \(\rho(E_{ij})\) matrices, enumerates every bivector in the tested finite fields, computes the linear system defining condition (1), and checks its dimension against the theorem. It also constructs sample normal-form local maps and checks the local-matching condition at **every element** of the tested finite Lie algebras. The tested dimensions of the allowable center block are \(9,16,25\) in ranks \(3,4,5\) over \(\mathbb F_2\), and \(9,16\) in ranks \(3,4\) over \(\mathbb F_3\), with a further rank-\(3\) check over \(\mathbb F_5\). Direct full-algebra tests cover \((n,q)=(3,2),(4,2),(3,3)\), comprising respectively \(64,1024,729\) algebra elements. Run `python3 checks/verify.py`; it prints `FREE_CLASS2_LOCAL_DERIVATIONS_OK`. These finite checks corroborate, but do not replace, the all-field proof.

## Relationship to prior work
Ayupov and Kudaybergenov (2015 preprint; 2016 journal) establish foundational local-derivation theory and exhibit explicit filiform examples, but do not give the rank-uniform classification here for the free class-two Lie algebra. Benito and Roldán-López (2019) describe ordinary derivations and automorphisms of free nilpotent Lie algebras; their ordinary derivations are antecedent and are not claimed as new. Khudoyberdiyev and Jumaniyozov (2024) establish that every two-step nilpotent Lie algebra over fields of characteristic unequal to two admits a non-derivation local derivation, and they discuss characteristic-two exceptions. That existence result does not give this complete exterior-square reflexive hull, the modular scalar correction, or the exact pointwise-local census. The known Heisenberg center-line classification is not a dominating special case for ranks \(n\ge3\), where \(\dim W=\binom n2\ge3\) and additional Plücker tangent constraints occur.

## Limitations
Only **linear** local derivations are classified. The statement does not address nonlinear two-local derivations, Lie algebra quotients, or free nilpotent algebras of class greater than two. Publication-priority verification is not exhaustive: some related 2026 literature on algebraic reflexive hulls was available only in partial form. The theorem is supported by a complete written proof and finite computational checks but not by independent mathematical review.

## References
- Sh. Ayupov and K. Kudaybergenov, *Local derivations on finite-dimensional Lie algebras*, arXiv:1508.03939 (initially public 17 August 2015); *Linear Algebra Appl.* 493 (2016), 381–398. https://arxiv.org/abs/1508.03939
- P. Benito and J. Roldán-López, *Derivations and automorphisms of free nilpotent Lie algebras and their quotients*, arXiv:1911.01897 (2019). https://arxiv.org/abs/1911.01897
- A. Khudoyberdiyev and D. Jumaniyozov, *Local derivations and automorphisms of nilpotent Lie algebras*, arXiv:2405.04209 (2024). https://arxiv.org/abs/2405.04209
- Z. Hao and L. Chen, *Two conjectures and applications on local and almost inner derivations* (2026), broad structural comparison; only abstracts and limited excerpts checked. https://doi.org/10.13140/RG.2.2.26969.48480
