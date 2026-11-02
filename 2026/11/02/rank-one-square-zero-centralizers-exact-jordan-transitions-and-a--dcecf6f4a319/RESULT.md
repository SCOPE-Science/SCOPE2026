# Rank-one square-zero centralizers: exact Jordan transitions and a reducibility threshold

## Finding
Let \(k=\mathbb F_q\) be an arbitrary finite field, let \(V=k^n\) with \(n\ge2\), and fix any nilpotent endomorphism \(N\) of Jordan type \(\lambda\). Let \(a,b,c\) be, respectively, the numbers of Jordan blocks of sizes one, two, and at least three. Put \(r=a+b+c\) and \(s=b+c\). Define
\[
\mathcal X_N(k)=\{T\in\operatorname{End}_k(V):\operatorname{rank}T\le1,\ T^2=0,\ TN=NT\}.
\]
For nonzero \(T\) in this set, let \(\Delta(T)=\operatorname{rank}(N+T)-\operatorname{rank}N\). The following formulas count actual matrices, not conjugacy classes. The unrefined total \(C\) is already implicit in an earlier rank-one commutator-spectrum census; it is reproduced here only to normalize the **new** rank-transition multiplicities and component classification:
\[
\begin{aligned}
C&=\#\{T\in\mathcal X_N(k):T\ne0\}
 =\frac{(q^s-1)(q^r-1)+(q^r-q^s)(q^{r-1}-1)}{q-1},\\
C_+&=\#\{T:\Delta(T)=1\}
 =\frac{(q^a-1)q^s(q^{r-1}-q^s)}{q-1},\\
C_-&=\#\{T:\Delta(T)=-1\}
 =\begin{cases}\displaystyle\frac{(q^b-1)q^c q^{s-1}}{q-1},&b>0,\\0,&b=0,\end{cases}\\
C_0&=\#\{T\ne0:\Delta(T)=0\}=C-C_+-C_-.
\end{aligned}
\]
For every such \(T\), including \(T=0\), one has \((N+T)^j=N^j\) for every integer \(j\ge2\). Thus the Jordan type of \(N+T\) differs from \(\lambda\) only by replacing two blocks of size one with one block of size two when \(\Delta=1\), or by the reverse replacement when \(\Delta=-1\); it is unchanged when \(\Delta=0\). Both changes occur precisely when the relevant count is positive: the upward change requires \(a\ge2\), and the downward change requires \(b\ge1\).

The reduced algebraic variety \(\mathcal X_N\) over \(k\), base-changed to an algebraic closure, obeys a sharp component criterion:

- If \(a=0\), it is geometrically irreducible of dimension \(2r-1\).
- If \(a=1\), it has exactly two geometrically irreducible components, both of dimension \(2r-2\), with irreducible intersection of dimension \(2r-3\).
- If \(a\ge2\), it is geometrically irreducible of dimension \(2r-2\).

Every component in these statements is defined over \(k\). In particular, the rank-at-most-one square-zero locus inside the nilpotent centralizer is reducible **if and only if** the fixed nilpotent has exactly one singleton Jordan block. The rational point count is \(\#\mathcal X_N(k)=C+1\).

## Assumptions and scope
The theorem requires only \(n\ge2\), that \(k\) is a finite field, and that \(N\) is nilpotent. It includes all characteristics and all Jordan partitions. The geometric claim concerns the underlying reduced variety: it does not assert that a particular ideal of defining equations is radical. Algebraic-geometric dimensions are Krull dimensions after passage to an algebraic closure. The zero perturbation is included in \(\mathcal X_N\) but excluded from \(C,C_+,C_-,C_0\).

## Proof
**1. Rank-one centralizer reduction.** Every nonzero rank-one linear map has a tensor expression \(T=u\otimes\varphi\), meaning \(T(v)=\varphi(v)u\), unique up to \((u,\varphi)\mapsto(tu,t^{-1}\varphi)\) for \(t\in k^\times\). The commutation identity reads
\[
(Nu)\otimes\varphi=u\otimes(\varphi N).
\]
If either side were nonzero, both would be nonzero and equality of nonzero decomposable tensors would force \(Nu=\mu u\) with \(\mu\ne0\), contradicting nilpotence of \(N\). Hence \(Nu=0\) and \(\varphi N=0\); conversely these imply commutation. Moreover \(T^2=\varphi(u)T\), so square-zero is exactly \(\varphi(u)=0\).

Set \(K=\ker N\), \(B=\operatorname{im}N\), and \(H=\operatorname{Ann}(B)\subset V^*\). Both \(K\) and \(H\) have dimension \(r\). The restricted evaluation pairing \(K\times H\to k\) has rank \(a\): in a Jordan-string basis, the head and socle are different positions for every block of size at least two and the same position precisely for blocks of size one. Its left radical \(E=K\cap B\) has dimension \(s\), while its right radical \(H_0=\operatorname{Ann}(B+K)\) also has dimension \(s\).

**2. Total count.** For each nonzero \(u\in E\), all \(q^r-1\) nonzero covectors in \(H\) annihilate \(u\). There are \(q^s-1\) choices of such \(u\). For each of the remaining \(q^r-q^s\) nonzero \(u\in K\), the equation \(\varphi(u)=0\) has \(q^{r-1}-1\) nonzero solutions in \(H\). Divide their sum by \(q-1\) because each rank-one operator has exactly \(q-1\) tensor representatives. This gives \(C\).

**3. Detecting the change in rank.** The elementary rank-one update criterion, valid over any field, states that for a linear map \(A\) and nonzero \(u,\varphi\), the rank of \(A+u\otimes\varphi\) increases by one if and only if \(u\notin\operatorname{im}A\) and \(\varphi|_{\ker A}\ne0\). It decreases by one if and only if \(u\in\operatorname{im}A\), \(\varphi|_{\ker A}=0\), and \(\varphi(w)=-1\) for any \(w\) with \(Aw=u\). Otherwise it is unchanged. To derive this criterion, choose complements to \(\ker A\) and \(\operatorname{im}A\) so the nonzero block of \(A\) is an identity; then eliminate the off-diagonal blocks of the rank-one update. The downward condition is the scalar determinant lemma on the identity block.

For the upward case here, \(u\in K\setminus E\), giving \((q^a-1)q^s\) possible \(u\). The covectors in \(H\) satisfying \(\varphi(u)=0\) number \(q^{r-1}\), of which exactly \(q^s\) lie in \(H_0\) and thus vanish on all of \(K\). The remaining covectors produce the stated \(C_+\) after dividing by \(q-1\).

For the downward case, \(u\in E\) and \(\varphi\in H_0\). Define a well-defined linear map
\[
\delta:E\longrightarrow V/(B+K),\qquad \delta(u)=[w]\quad\text{for }Nw=u.
\]
Different choices of \(w\) differ by an element of \(K\). In a Jordan-string basis, \(\delta\) has rank exactly \(b\): the socle of every length-two block maps to its nonzero head class, whereas the predecessor of the socle of a longer block belongs to \(B\). Consequently exactly \((q^b-1)q^c\) vectors \(u\in E\) have \(\delta(u)\ne0\). For each, the functional \(\varphi\mapsto\varphi(w)\) on the \(s\)-dimensional space \(H_0\) is nonzero; exactly \(q^{s-1}\) covectors satisfy \(\varphi(w)=-1\). Scaling gives \(C_-\). The remaining nonzero tensors give \(C_0\).

**4. Jordan type and boundary cases.** From \(NT=TN=T^2=0\) we obtain \((N+T)^2=N^2\), hence \((N+T)^j=N^j\) for all \(j\ge2\). The rank sequence of powers determines nilpotent Jordan multiplicities by
\[
 m_j=\operatorname{rank}(A^{j-1})-2\operatorname{rank}(A^j)+\operatorname{rank}(A^{j+1}).
\]
Only the rank at the first power can change. If its change is \(d\), the size-one block multiplicity changes by \(-2d\), the size-two multiplicity by \(d\), and all other multiplicities stay fixed. This proves the stated replacement rule. In the formulas \(C_+>0\) exactly when \(a\ge2\); \(C_->0\) exactly when \(b\ge1\).

**5. Components.** Under the linear embedding \(K\otimes H\hookrightarrow\operatorname{End}(V)\), the rank-at-most-one locus is the affine cone over the Segre variety \(\mathbb P(K)\times\mathbb P(H)\). The square-zero equation is the projective bilinear incidence equation \(\varphi(u)=0\), whose matrix rank is \(a\). If \(a=0\), the equation vanishes identically, so the entire Segre cone is irreducible of dimension \(2r-1\). If \(a=1\), the equation is a product of one linear coordinate in each factor: the locus is the union of the two Segre sub-cones obtained by setting either coordinate to zero. Since \(n\ge2\) forces \(r\ge2\) in this case, both components are nonempty and distinct, each of dimension \(2r-2\), with intersection dimension \(2r-3\). If \(a\ge2\), the bilinear equation is irreducible over the algebraic closure (a bilinear polynomial factors only when its coefficient matrix has rank at most one). Its hypersurface in the product of projective spaces is irreducible: the open set where a first-factor coefficient is nonzero is an affine hyperplane bundle, dense in the whole incidence locus; the boundary fibers have smaller dimension and lie in its closure. Thus the affine cone is irreducible of dimension \(2r-2\). All equations and descriptions are defined over \(k\), which completes the proof.

## Verification
The standalone programs `verify.py` and `verify_ambient.py`, together with their captured UTF-8 outputs, are included in the accompanying package. `verify.py` constructs Jordan matrices over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\) (using an irreducible quadratic), and \(\mathbb F_5\), exhaustively enumerates the rank-one tensor parameter space for 90 configurations, and directly checks matrix rank, commutation, square-zero, and equality of second powers. `verify_ambient.py` independently enumerates **all** matrices in eight smaller ambient matrix spaces before imposing the rank, square-zero and commutation tests, so it does not rely on the completeness of the tensor parameterization. All comparisons passed.

As an arithmetic illustration over \(\mathbb F_3\), the Jordan partitions \((4,2,1)\) and \((3,3,1)\) both have \(r=3\), \(a=1\), \(s=2\), and exactly \(176\) nonzero admissible perturbations, but the first admits exactly \(9\) rank-decreasing perturbations while the second admits none. Both corresponding reduced varieties have two four-dimensional components. For the partition \((2,1,1)\) over \(\mathbb F_3\), the exact rank-change spectrum is \((C_-,C_0,C_+)=(1,49,72)\).

## Relationship to prior work
An earlier finite-field rank-one square-zero commutator-spectrum result (record 9ca4dfd9-ead7-482a-8f1c-273e1396ba1f) counts the zero-commutator fiber \(Z=(q-1)[L_sL_r+(L_r-L_s)L_{r-1}]\), where \(L_j=(q^j-1)/(q-1)\). Algebraic simplification shows \(Z=C\), the total nonzero point count in this theorem. **That total is prior art, not a new finding.** The previous result classifies the Jordan type of the commutator \([N,T]\), not the rank transitions of \(N+T\) within the commuting fiber, and it depends on \(n,r,a\) rather than the separate number \(b\) of size-two blocks. In particular, \((4,2,1)\) and \((3,3,1)\) have identical old invariants but different new downward-transition multiplicities; thus the refined transition statement cannot follow merely from the earlier census. The geometric component condition is also not stated there.

Britnell and Wildon (public preprint 2010) analyze which nilpotent similarity classes contain commuting representatives, including two-block phenomena depending on the finite field. Their class-existence results do not supply the point counts, three-way Jordan **transition multiplicities**, or rank-one centralizer variety component criterion here. Iarrobino and Khatami (2012) study the generic Jordan type of the **full** nilpotent centralizer over infinite fields, proving bounds via partition posets; they do not enumerate rank-one square-zero perturbations. Iarrobino, Khatami, Van Steirteghem and Zhao (2014) classify fibers of the generic-Jordan-type map for certain stable partitions, a different parameter problem. Bogdanić, Đurić, Koljančić, Oblak and Šivic (2022) study the nilpotent classes meeting centralizers of matrices with two equal blocks, but do not give arbitrary-partition finite-field rank-one perturbation multiplicities or the incidence reducibility threshold. The full author-hosted paper of Moro and Dopico, first published electronically on 2003-09-17, proves a generic complex-matrix low-rank perturbation criterion; its elementary rank-update mechanism is treated here as classical, not original. Its all-complex-perturbation genericity theorem does not give the restricted finite-field point counts and geometric incidence classification asserted here. Publication priority for the combined exact geometric/arithmetic theorem is provisional; an unidentified more general determinantal or centralizer formula could subsume it.

## Limitations
The result is restricted to square-zero perturbations of rank at most one commuting with a **nilpotent** fixed operator. It does not classify arbitrary elements of the nilpotent centralizer or higher-rank perturbations, and it does not assert scheme-theoretic reducedness for an unreduced equation presentation. Finite computations check sample fields and partitions; the symbolic proof establishes the all-field claim. An independent expert audit and exhaustive publication-priority review have not been performed.

## References
1. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811, first posted 2010-01-06, https://arxiv.org/abs/1001.0811.
2. A. Iarrobino and L. Khatami, *Bound on the Jordan type of a generic nilpotent matrix commuting with a given matrix*, arXiv:1204.4635, first posted 2012-04-20, https://arxiv.org/abs/1204.4635.
3. A. Iarrobino, L. Khatami, B. Van Steirteghem and R. Zhao, *Nilpotent matrices having a given Jordan type as maximum commuting nilpotent orbit*, arXiv:1409.2192, first posted 2014-09-08, https://arxiv.org/abs/1409.2192.
4. D. Bogdanić, A. Đurić, S. Koljančić, P. Oblak and K. Šivic, *Jordan structures of nilpotent matrices in the centralizer of a nilpotent matrix with two Jordan blocks of the same size*, arXiv:2212.08425, first posted 2022-12-16, https://arxiv.org/abs/2212.08425.
5. J. Moro and F. M. Dopico, *Low rank perturbation of Jordan structure*, SIAM J. Matrix Anal. Appl. 25 (2003), 495–506, DOI 10.1137/S0895479802417118; first published electronically 2003-09-17 (as recorded in the original author-hosted PDF at https://gauss.uc3m.es/fdopico/papers/SIMAX2003-lowrankjordan.pdf).
