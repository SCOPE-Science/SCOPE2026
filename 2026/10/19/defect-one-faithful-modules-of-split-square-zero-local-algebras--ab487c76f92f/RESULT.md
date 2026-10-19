# Defect-one faithful modules of split square-zero local algebras over finite fields

## Finding
Fix an integer \(s\geq2\), a finite field \(K=\mathbb F_q\), and a fixed \(K\)-vector space \(J\) of dimension \(r=s^2-1\). Equip \(A=K\oplus J\) with its split local algebra structure \(J^2=0\). The minimum dimension of a faithful left \(A\)-module is \(2s\). We determine all their possible radical/socle profiles, count their isomorphism classes over the **fixed** algebra \(A\), and compute each endomorphism ring.

Define \(g_n(q)=|\operatorname{GL}_n(K)|=\prod_{i=0}^{n-1}(q^n-q^i)\), with \(g_0(q)=1\), and
\[
R_{s,t}(q)=\begin{bmatrix}s\\t\end{bmatrix}_q^2g_t(q)
\qquad(1\leq t\leq s),
\]
the number of rank-\(t\) matrices in \(M_s(K)\). The exact class counts are:
\[
C_{-}(s,q)=C_{+}(s,q)
=\frac{(q-1)g_{s^2-1}(q)}{g_{s-1}(q)g_{s+1}(q)},
\qquad
C_t(s,q)=\frac{g_{s^2-1}(q)R_{s,t}(q)}{g_s(q)^2}.
\]
The two \(C_\pm\) count distinct rectangular radical/socle profiles. For \(1\leq t\leq s\), \(C_t\) counts the balanced profile with rank-\(t\) normal to the image hyperplane. Thus the total number of isomorphism classes is
\[
\boxed{\;2C_{+}(s,q)+\sum_{t=1}^s C_t(s,q)\;}.
\]
Every rectangular-profile module is self-centralizing: its represented algebra equals its endomorphism algebra, of dimension \(s^2\). Every balanced-profile module has endomorphism algebra of dimension \(s^2+1\), so its represented algebra is a **codimension-one subalgebra of its own commutant**. In every case the endomorphism algebra is commutative and local, with square-zero radical.

In the first nontrivial case \(s=2\), \(r=3\), the class counts are \(72\) for \(q=2\) (balanced ranks: \(42,28\)) and \(392\) for \(q=3\) (balanced ranks: \(156,234\)); there is one class of each rectangular profile for either field.

## Assumptions and scope
All vector spaces, isomorphisms, and representations are over \(K\), with \(q\) any prime power. The algebra \(A\), including the action of every distinguished element of \(J\), is **fixed**. A-module isomorphism does not permit changing generators through an automorphism of \(A\). The conclusion covers every \(s\geq2\), including characteristic two; it does not classify higher-dimensional modules or representations with a non-split residue division algebra.

For a faithful \(A\)-module \(M\), write \(U=JM\), \(W=\operatorname{Ann}_M(J)\), \(u=\dim U\), and \(k=\dim(M/W)\). Since \(J^2=0\), \(U\subseteq W\), and faithfulness supplies an injection
\[
J\longhookrightarrow\operatorname{Hom}_K(M/W,U),\qquad a\longmapsto(v+W\mapsto av).
\]
Hence \(uk\geq r\), while \(u+k\leq\dim M\).

## Proof
**(1) Minimum degree and profiles.** If \(\dim M\leq2s-1\), then \(uk\leq\lfloor(2s-1)^2/4\rfloor=s(s-1)<s^2-1=r\), a contradiction. Conversely, choose a decomposition \(K^{2s}=K^s\oplus K^s\) and any injection \(J\hookrightarrow M_s(K)\) as a hyperplane; sending \(a\in J\) to \(\begin{psmallmatrix}0&\phi(a)\\0&0\end{psmallmatrix}\) gives a faithful module. Thus \(\dim M=2s\) is optimal.

For any module attaining it, \(u+k\) cannot be at most \(2s-1\), so \(u+k=2s\), forcing \(U=W\). With \(u+k=2s\), the inequality \(uk\geq s^2-1\) gives exactly the three ordered pairs \((u,k)=(s-1,s+1),(s,s),(s+1,s-1)\). Conversely every injective map \(\phi:J\to M_{u\times k}(K)\) in these profiles is faithful, has \(JM=U\), and has \(\operatorname{Ann}_M(J)=U\). For the rectangular profiles this is immediate because \(\phi\) is onto. For the balanced profile, the hyperplane \(\phi(J)\) contains an invertible matrix, proved below, so both conclusions follow.

**(2) Classification by matrix frames.** Choose \(K\)-linear identifications of \(U\) and \(M/U\) with \(K^u\) and \(K^k\). The radical action is an injection \(\phi:J\to M_{u\times k}(K)\). Two actions yield isomorphic modules if and only if their frame maps lie in the same \(\operatorname{GL}_u(K)\times\operatorname{GL}_k(K)\)-orbit, with \((P,Q)\) acting by \(\phi(a)\mapsto P\phi(a)Q^{-1}\). A change of splitting induces only an upper-right shear and does not change \(\phi\). Conversely all such left/right frame changes extend to module isomorphisms.

In a rectangular profile, \(uk=r\), so \(\phi\) is an isomorphism onto all \(M_{u\times k}(K)\). There are exactly \(g_r(q)\) frame maps \(\phi\). The pointwise stabilizer consists precisely of \((\lambda I_u,\lambda I_k)\), \(\lambda\in K^\times\); the matrix units prove this assertion. Each orbit therefore has size \(g_u(q)g_k(q)/(q-1)\), proving both rectangular formulas.

In the balanced profile the image \(H=\phi(J)\) is a hyperplane in \(M_s(K)\). Nondegeneracy of the trace pairing gives a projectively unique nonzero normal \(B\), namely
\[
H=\{X\in M_s(K):\operatorname{tr}(BX)=0\}.
\]
The rank \(t=\operatorname{rank}B\in\{1,\ldots,s\}\) is preserved under left/right equivalence. There are \(R_{s,t}(q)/(q-1)\) such hyperplanes, with \(g_r(q)\) frames into each.

**(3) Hyperplane stabilizer lemma.** For \(s\geq2\), every matrix hyperplane \(H\subset M_s(K)\) contains an invertible matrix. Indeed, by independent row and column coordinate changes its normal becomes \(\operatorname{diag}(I_t,0)\), and the cyclic permutation matrix (with zero diagonal) lies in that hyperplane and is invertible; undoing the changes proves the statement.

Suppose \((P,Q)\in\operatorname{GL}_s(K)^2\) fixes *each* \(X\in H\), i.e. \(PX=XQ\). Taking an invertible \(X_0\in H\) gives \(Q=X_0^{-1}PX_0\). Therefore \(P\) centralizes the codimension-one subspace \(HX_0^{-1}\subseteq M_s(K)\). For any nonscalar \(P\), choose \(v\in K^s\) for which \(v,Pv\) are independent. A matrix commuting with \(P\) is determined on \(Pv\) by its value on \(v\), so its centralizer has dimension at most \(s+s(s-2)=s^2-s<s^2-1\). This contradicts the presence of \(HX_0^{-1}\). Thus \(P=\lambda I_s\), and consequently \(Q=\lambda I_s\). The pointwise stabilizer has exactly \(q-1\) elements.

Hence each frame orbit in the balanced profile has size \(g_s(q)^2/(q-1)\). Dividing the number \(g_r(q)R_{s,t}(q)/(q-1)\) of rank-\(t\) framed hyperplanes by that size proves \(C_t(s,q)\). The rank-\(t\) matrix count follows from choosing its image and kernel (two Gaussian coefficients) and the induced isomorphism between their \(t\)-dimensional quotients (\(g_t(q)\) choices).

**(4) Endomorphisms and the centralizer jump.** Relative to \(M=U\oplus T\), the image of \(J\) consists of \(N_X=\begin{psmallmatrix}0&X\\0&0\end{psmallmatrix}\) for \(X\in H=\phi(J)\). An endomorphism \(F=\begin{psmallmatrix}P&Z\\G&Q\end{psmallmatrix}\) commutes with all \(N_X\) exactly when \(PX=XQ\), \(XG=0\), and \(GX=0\) for every \(X\in H\). The full rectangular matrix space, or an invertible element of a balanced hyperplane, forces \(G=0\). The same matrix-unit / hyperplane lemma used above, now for arbitrary (not necessarily invertible) \(P,Q\), shows \(P=\lambda I_u\) and \(Q=\lambda I_k\): to see the balanced case, if nonscalar \(P\) centralized a hyperplane its centralizer-dimension bound still applies; the rectangular matrix units give the other case. Thus
\[
\operatorname{End}_A(M)=
\left\{\begin{pmatrix}\lambda I_u&Z\\0&\lambda I_k\end{pmatrix}:\lambda\in K,\ Z\in M_{u\times k}(K)\right\}.
\]
The represented algebra has dimension \(r+1=s^2\). Since \(uk=r\) in rectangular profiles and \(uk=r+1\) in the balanced profile, the endomorphism dimensions are respectively \(s^2\) and \(s^2+1\). The multiplication rule makes the displayed endomorphism algebra commutative local with square-zero radical, completing the proof. \(\square\)

## Verification
The accompanying standalone program `verification/check.py` uses only standard-library Python. Its finite-field computations give a full orbit census of the \(2520\) ordered bases of \(2\times2\) matrix hyperplanes over \(\mathbb F_2\): every frame orbit has size \(36\), and the normal-rank class counts are \(42\) and \(28\). A separate sweep of all \(40\) projective hyperplane normals over \(\mathbb F_3\) directly checks pointwise stabilizers of size \(2\); the normal-rank counts are \(16\) and \(24\), yielding \(156\) and \(234\) fixed-algebra module classes. Integer evaluations are also checked at \(s=2,3,4\) and \(q=2,3,4,5\), but they are formula evaluations, not separate extension-field module censuses.

Run `python3 verification/check.py` from a directory containing that file. No external data or dependencies are needed. The general assertion rests on the proof, not finite experimentation.

## Relationship to prior work
The Schur–Jacobson bound for commutative subalgebras of matrix algebras implies the minimum faithful degree in this case; that lower bound is **not** claimed as new. Bergman's bilinear-map description and inequalities for minimal faithful Artinian modules supply a related general framework. The geometric description of modules for radical-square-zero algebras by Bleher, Chinburg, and Huisgen-Zimmermann concerns representation varieties and irreducible components. The present result instead makes a defect-one, fixed-algebra classification explicit, with finite-field orbit counts by hyperplane-normal rank and an endomorphism-algebra codimension jump. The identified primary results do not state the displayed fixed-algebra class-count formulas.

## Limitations
Classification is only for faithful modules of the smallest possible dimension over the specified split algebra; automorphisms of the source algebra are *not* quotiented out. This is a mathematical derivation with exhaustive checks in small prime-field cases, not a computer-certified proof or independent mathematical audit. Related work in the broader representation-variety and matrix-subspace orbit literature may contain equivalent formulations; the comparisons in the references do not exhaust that literature.

## References
1. George M. Bergman, “Minimal faithful modules over Artinian rings,” arXiv:1310.5365v1 (first publicly posted 2013-10-20); later version v2, 2014. https://arxiv.org/abs/1310.5365
2. Frauke Bleher, Ted Chinburg, and Birge Huisgen-Zimmermann, “The geometry of finite dimensional algebras with vanishing radical square,” arXiv:1407.3045v1 (2014). https://arxiv.org/abs/1407.3045
3. J. Szigeti, J. van den Berg, L. van Wyk, and M. Ziembowski, “The maximum dimension of a Lie nilpotent subalgebra of \(M_n(F)\) of index \(m\),” arXiv:1608.04562v1 (2016). https://arxiv.org/abs/1608.04562
