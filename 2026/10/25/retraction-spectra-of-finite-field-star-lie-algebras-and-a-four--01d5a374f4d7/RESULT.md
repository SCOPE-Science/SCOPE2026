# Retraction spectra of finite-field star Lie algebras and a four-phase discrete-Gaussian law

## Finding

Let \(q\) be any prime power, \(m\ge2\), and \(U=\mathbb F_q^m\). The star-graph two-step nilpotent Lie algebra is
\[
 L_m=(\mathbb F_qc\oplus U)\oplus Z,\qquad Z=\{z_u:u\in U\}\cong U,
 \qquad [c,u]=z_u,\quad [U,U]=[L_m,Z]=0.
\]
All Lie algebra endomorphisms and all ranks below are \(\mathbb F_q\)-linear. A retraction is an idempotent Lie algebra endomorphism \(F\), meaning \(F^2=F\).

Write \(G_q(n,r)={n\brack r}_q\) for the Gaussian binomial coefficient, and let \(t\) record the full \(\mathbb F_q\)-dimension of the image \(\operatorname{im}F\). Then the **complete image-dimension enumerator of all retractions** is
\[
 \begin{aligned}
 P_{m,q}(t)={}&1+G_q(m+1,1)q^{2m}t
 +\sum_{r=2}^mG_q(m,r)q^{r(2m-r+1)}t^r\\
 &+\sum_{s=1}^mG_q(m,s)q^{(3s+2)(m-s)}t^{2s+1}.
 \end{aligned}
\]
The enumerator of **distinct retract subalgebras**, counted once per actual subspace rather than once per map, is
\[
 \begin{aligned}
 Q_{m,q}(t)={}&1+G_q(m+1,1)q^mt
 +\sum_{r=2}^mG_q(m,r)q^{mr}t^r\\
 &+\sum_{s=1}^mG_q(m,s)q^{(s+2)(m-s)}t^{2s+1}.
 \end{aligned}
\]
Every nonzero proper retract is either abelian or isomorphic to the corresponding smaller star Lie algebra \(L_s\) for some \(1\le s<m\). No nonzero proper retract is an ideal.

If \(F\) is uniformly chosen among the retractions and \(R_m=\dim\operatorname{im}(F\bmod Z)\), let
\[
 \alpha_m=\frac{3m+1}{4},\quad k_m=\lfloor\alpha_m\rfloor,\quad \delta_m=\alpha_m-k_m.
\]
For every fixed \(q\) and each residue class of \(m\) modulo four, the integer-valued random variable \(R_m-k_m\) converges in **total variation** to the discrete-Gaussian law
\[
 \Pr(J=j)=\frac{q^{-2(j-\delta)^2}}{\displaystyle\sum_{h\in\mathbb Z}q^{-2(h-\delta)^2}},\quad j\in\mathbb Z,
\]
where \(\delta\in\{1/4,0,3/4,1/2\}\) corresponds respectively to \(m\equiv0,1,2,3\pmod4\). In particular \(R_m/m\to3/4\) in probability, and the proportion of retractions with nonabelian image tends to zero at rate \(q^{-m^2/8+O(m)}\).

## Assumptions and scope

The center and derived algebra of \(L_m\) are both \(Z\), since the bracket has trivial radical on \(\mathbb F_qc\oplus U\). This assertion remains valid in characteristic two: the bracket is alternating, with \([u,c]=-z_u\). No restriction on the characteristic or on \(q\) being prime is needed. The initial term \(1\) counts the zero retraction; the last summand at \(s=m\) counts the identity map.

The summands with image dimension \(r\) are abelian retracts; those with image dimension \(2s+1\) are nonabelian, so equal exponents of \(t\) in different summands must be added. The claim concerns all Lie-homomorphism idempotents, including maps that do not preserve the displayed grading.

## Proof

**Step 1: general homomorphisms.** Put \(V=\mathbb F_qc\oplus U\) and identify \(Z\) with \(U\) through \(u\mapsto z_u\). Since \(Z=[L_m,L_m]\), every Lie endomorphism has a unique block description
\[
 F(v,z)=(Av,f(v)+\psi z),\qquad A\in\operatorname{End}(V),\quad f\in\operatorname{Hom}(V,Z),\quad\psi\in\operatorname{End}(Z).
\]
Write \(A\) in blocks relative to \(V=\mathbb F_qc\oplus U\):
\[
 A=\begin{pmatrix}a&\ell\\w&M\end{pmatrix},\quad a\in\mathbb F_q,\ \ell\in U^*,\ w\in U,\ M\in\operatorname{End}(U).
\]
Preservation of \([c,u]\) forces \(\psi=aM-w\ell\); preservation of \([u,v]=0\) forces \(\ell(u)Mv-\ell(v)Mu=0\) for all \(u,v\in U\). These conditions are sufficient for the homomorphism property. Idempotence is equivalent to
\[
 A^2=A,\quad \psi^2=\psi,\quad fA+\psi f=f.
\]
If \(A\) is idempotent of rank \(h\), and \(\psi\) has rank \(k\), the last equation has precisely
\[
 q^{h(m-k)+(m+1-h)k}
\]
solutions \(f\). Indeed, with \(V=\operatorname{im}A\oplus\ker A\), it says \(f(\operatorname{im}A)\subseteq\ker\psi\) and \(f(\ker A)\subseteq\operatorname{im}\psi\).

**Step 2: classification of quotient projections.** If \(\ell\ne0\), the condition on pairs in \(U\) forces \(M=t\ell\) for some \(t\in U\). Thus \(A(U)=\mathbb F_q(c+t)\), and \(\operatorname{rank}A\le2\). If \(A^2=A\) and its rank were two, its image would meet \(U\) in a nonzero vector \(u\); then \(u=Au\in A(U)\), contradicting \(A(U)\cap U=0\). Consequently \(\operatorname{rank}A=1\). Conversely every rank-one idempotent \(A\) preserves the bracket kernel \(\bigwedge^2U\), and its forced central map is \(\psi=0\).

If \(\ell=0\), the idempotence equations give \(a\in\{0,1\}\), \(M^2=M\), and either \(Mw=w\) when \(a=0\), or \(Mw=0\) when \(a=1\). In these cases \(\psi=aM\). This exhausts all possibilities and separates them without overlap into the zero map; all quotient-rank-one retractions; abelian-image retractions with \(a=0\) and \(\operatorname{rank}M=r\ge2\); and star-image retractions with \(a=1\) and \(\operatorname{rank}M=s\ge1\).

**Step 3: map counts.** A rank-\(r\) projection on an \(m\)-space can be chosen in \(G_q(m,r)q^{r(m-r)}\) ways: choose its image and a complementary kernel. Every rank-one projection on \(V\) can be chosen in \(G_q(m+1,1)q^m\) ways, and the central lift \(f\) contributes \(q^m\). In the \(a=0\) family, the vector \(w\) is any of the \(q^r\) elements of \(\operatorname{im}M\), and \(f\) contributes \(q^{mr}\). This gives \(G_q(m,r)q^{r(2m-r+1)}\). In the \(a=1\) family, \(w\in\ker M\) has \(q^{m-s}\) choices; here \(\operatorname{rank}A=s+1\), \(\operatorname{rank}\psi=s\), so \(f\) contributes \(q^{(2s+1)(m-s)}\). Thus the count is \(G_q(m,s)q^{(3s+2)(m-s)}\). Each such image has dimension \(2s+1\), giving \(P_{m,q}\).

**Step 4: image counts.** For rank one, choose a line in \(V\) and an arbitrary central graph over it: \(G_q(m+1,1)q^m\) images. For abelian rank \(r\ge2\), choose \(W\in\operatorname{Gr}(r,U)\) and a graph \(W\to Z\), giving \(G_q(m,r)q^{mr}\) images. For star rank \(s\), choose the derived central subspace \(W\in\operatorname{Gr}(s,U)\), then a quotient image \(E=\mathbb F_q(c+w)\oplus W\subseteq V\), where \(w+W\in U/W\) has \(q^{m-s}\) choices, and finally a central graph \(E\to Z/W\) with \(q^{(s+1)(m-s)}\) choices. This yields \(G_q(m,s)q^{(s+2)(m-s)}\) images and \(Q_{m,q}\). The numbers of maps onto an individual image are respectively \(q^m\), \(q^{r(m-r+1)}\), and \(q^{2s(m-s)}\); the endpoint \(s=m\) has one map. An abelian proper image has a noncentral vector whose bracket with some ambient vector lies outside the image. A proper star image has \(s<m\), and bracketing its outside-\(U\) generator with a leaf outside its derived central subspace also leaves the image. Hence none is an ideal.

**Step 5: asymptotic law.** Write \(C_q=\prod_{j\ge1}(1-q^{-j})^{-1}<\infty\). The standard finite-product identity gives
\[
 1\le G_q(m,r)q^{-r(m-r)}\le C_q,
\]
and this factor tends to \(C_q\) whenever \(r\to\infty\) and \(m-r\to\infty\). The abelian summand of rank \(r\ge2\) is therefore
\[
 G_q(m,r)q^{r(2m-r+1)}=H_{m,r}q^{r(3m-2r+1)},\quad 1\le H_{m,r}\le C_q.
\]
Completing the square gives
\[
 r(3m-2r+1)=\frac{(3m+1)^2}{8}-2(r-\alpha_m)^2.
\]
The nonabelian summands are bounded by \(C_qq^{(4s+2)(m-s)}\) and hence by \(C_qq^{m^2+m+1/4}\). Meanwhile an abelian term within distance \(1/2\) of \(\alpha_m\) is at least \(q^{(3m+1)^2/8-1/2}\), so nonabelian probability is \(q^{-m^2/8+O(m)}\). The rank-zero and rank-one terms are negligible at the same scale. For \(r=k_m+j\), the normalized abelian weights converge pointwise to \(C_qq^{-2(j-\delta)^2}\) along each fixed residue class, and the uniform discrete-Gaussian bound \(C_qq^{-2(j-\delta)^2}\) allows summation and total-variation convergence. Tightness on an \(O(1)\) rank window proves \(R_m/m\to3/4\).

## Verification

The accompanying standalone `verify.py` exhaustively enumerates all quotient projectors satisfying the bracket relation for \((q,m)=(2,2),(3,2),(2,3)\), checks their induced central maps and all rank strata against \(P_{m,q}\), and, when \(m=2\), independently enumerates every central lift \(f\) satisfying idempotence. For \((q,m)=(2,2)\), it explicitly constructs distinct images as vector subspaces and verifies their fibre multiplicities against \(Q_{m,q}\). The expected map totals are \(274\), \(2756\), and \(21186\) in that order; these are finite checks and do not establish the general theorem. The proof above supplies the unrestricted argument. Run with `python verify.py` (standard library only).

## Relationship to prior work

The graphical construction of two-step nilpotent Lie algebras is established in the literature, and is **not** claimed here. Chakrabarti–Mainkar–Swiatlowski study automorphism subgroups of Lie algebras arising from edge-colored complete graphs; their 2018 preprint has no retraction or idempotent-endomorphism classification. Godoy Molina–Lagos describe graph ideals and graded derivations for labeled graph Lie algebras, including complete bipartite graphs; their 2023 paper does not count all idempotent Lie endomorphisms. The free class-two Lie retract enumeration for complete graphs and earlier Lie-ideal/commutativity spectra for multipartite graphs concern different properties: the present star quotient is not a parameter specialization of their counts, because its bracket relations impose additional restrictions on quotient projections. Standard Gaussian-binomial counts are used as ingredients, not asserted to be new. No exhaustive literature-priority claim is made.

## Limitations

This is a complete classification only for the star (equivalently \(K_{1,m}\)) graphical Lie algebra with independently labeled edges. It does not treat all graphical Lie algebras, all idempotents of the underlying associative endomorphism ring, or any claim of independent audit or publication. The finite verifier covers prime fields only; extension-field and arbitrary-dimension results follow from linear algebra, not from finite enumeration. Related results under alternate terminology such as split Lie extensions, retracts of nilpotent Lie algebras, or idempotent morphisms of bilinear-map quotients may require further human literature review.

## References

1. D. Chakrabarti, M. Mainkar, S. Swiatlowski, *Automorphism Groups of Nilpotent Lie Algebras Associated to Certain Graphs*, arXiv:1812.09439, initial public version 2018-12-22, MSC 17B30.
2. M. Godoy Molina, D. Lagos, *Lie Algebras Associated with Labeled Directed Graphs*, arXiv:2308.00272, initial public version 2023-08-01, MSC 17B30/17B40.
3. P. Benito, D. de-la-Concepción, J. Laliena, *Free Nilpotent and Nilpotent Quadratic Lie Algebras*, Linear Algebra and its Applications 519 (2017), 296–326, DOI 10.1016/j.laa.2017.01.007; background on free nilpotent Lie mappings, not a source for the present enumeration.
