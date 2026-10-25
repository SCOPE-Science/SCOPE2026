# Complete higher-indicator spectra for abelian-kernel cyclic Frobenius doubles

## Finding
Let \(A\) be any nontrivial finite abelian group, written additively, and let \(H=\langle s\rangle\) be cyclic of order \(m\ge2\), acting by automorphisms on \(A\) so that every nonidentity element of \(H\) fixes only zero. Set \(G=A\rtimes H\), \(N=|A|\). For each integer \(k\ge1\), put \(d_k=\gcd(k,m)\) and \(t_k=|A[k]|\), where \(A[k]=\{a\in A:ka=0\}\). All representations and Drinfeld doubles below are over \(\mathbb C\).

Every irreducible module of \(D(G)\) has exactly one of the following forms, up to the standard conjugacy-class/centralizer parametrization, and its \(k\)-th higher Frobenius–Schur indicator is as displayed:

1. The identity class and an inflated one-dimensional character \(\lambda\in\widehat H\):
\[\nu_k(1,\lambda)=\mathbf1_{\lambda^k=1}.\]
2. The identity class and an irreducible character \(\operatorname{Ind}_A^G\eta\), where \(\eta\in\widehat A\setminus\{1\}\) is chosen up to the \(H\)-action:
\[\nu_k(1,\operatorname{Ind}\eta)=d_k-1+\mathbf1_{\eta^k=1}.\]
3. The conjugacy class of \(a\in A\setminus\{0\}\), chosen up to the \(H\)-action, with any \(\psi\in\widehat A\):
\[\nu_k(a,\psi)=d_k-1+\mathbf1_{ka=0}\mathbf1_{\psi^k=1}.\]
4. The conjugacy class of \(h\in H\setminus\{1\}\), with any \(\lambda\in\widehat H\):
\[\nu_k(h,\lambda)=\mathbf1_{h^k=1}\left(\mathbf1_{\lambda^k=1}+\frac{(N-1)(d_k-2)+2(t_k-1)}m\right).\]

The corresponding module dimensions are \(1,m,m,N\), respectively. These formulas give the **complete indicator sequence of every irreducible** of \(D(G)\), uniformly in \(A\), \(H\), and \(k\). Every indicator is a nonnegative integer.

Moreover, the multiset of dimension-tagged complete indicator sequences depends only on the abstract abelian group \(A\) and the complement order \(m\), not on the fixed-point-free action. Conversely this multiset recovers both \(m\) and the isomorphism type of \(A\). In particular, the nonisomorphic groups \((\mathbb F_7^2)\rtimes C_3\) defined by \(s\mapsto\operatorname{diag}(2,2)\) and \(s\mapsto\operatorname{diag}(2,4)\) have **identical dimension-tagged higher-indicator multisets** for their doubles, at every positive index.

## Assumptions and scope
The fixed-point-free hypothesis means \(h-1\) is invertible as an endomorphism of \(A\) for every \(h\in H\setminus\{1\}\). In particular, the group \(G\) is a Frobenius group with abelian kernel and cyclic complement. The indicator \(\nu_k(g,\rho)\) is the standard higher Frobenius–Schur indicator of the irreducible \(D(G)\)-module indexed by the conjugacy class of \(g\) and an irreducible representation \(\rho\) of \(C_G(g)\). The indicators of characters \(\eta\) and \(\lambda\) are defined by pointwise powers of their values. No primality restriction is imposed on \(N\), \(m\), or \(k\). The formulas concern ordinary complex representations, not modular-character indicators.

## Proof
**Classification.** Write a group element as \((b,u)\), with \(b\in A\), \(u\in H\), and \((b,u)(c,v)=(b+u(c),uv)\). Fixed-point-freeness gives three types of conjugacy classes: \(\{1\}\); the free \(H\)-orbits in \(A\setminus\{0\}\), each with centralizer \(A\); and the \(m-1\) classes represented by \(h\in H\setminus\{1\}\), each with centralizer \(H\). Indeed \(h-1\) is bijective, so translating conjugates \((0,h)\) through all \(b\in A\) and \(C_G(h)=H\). The dual action of \(H\) on \(\widehat A\setminus\{1\}\) is likewise free, since its fixed-point equation is the dual of an invertible endomorphism. Clifford theory therefore yields \(m\) inflated linear characters and \((N-1)/m\) irreducible induced characters of degree \(m\) for \(G\). The standard conjugacy-class/centralizer parametrization of \(D(G)\) proves the asserted exhaustive list and dimensions.

**Indicator identity.** We use the established finite-group Drinfeld-double formula (Kashina–Sommerhäuser–Zhu, as stated in Keilberg [1, Corollary 1.8] and Iovanov–Mason–Montgomery [2, (2.2)]):
\[\nu_k(g,\rho)=\frac1{|C_G(g)|}\sum_{x\in G:\ (gx)^k=x^k}\chi_\rho(x^k).\]
The condition implies \(x^k\in C_G(g)\), so the character evaluation is well-defined. For \(u\in H\), write \(S_k(u)=1+u+\cdots+u^{k-1}\) as an endomorphism of \(A\). Then \((b,u)^k=(S_k(u)b,u^k)\). For \(u\ne1\), the identity \((u-1)S_k(u)=u^k-1\) and fixed-point-freeness show that \(S_k(u)=0\) if \(u^k=1\), while \(S_k(u)\) is invertible otherwise.

**Identity class.** An inflated character \(\lambda\) has indicator \((Nm)^{-1}\sum_{b,u}\lambda(u^k)=\mathbf1_{\lambda^k=1}\). For \(\chi=\operatorname{Ind}_A^G\eta\), its values vanish off \(A\), and on \(A\) equal \(\sum_{u\in H}\eta(u(b))\). Exactly \(d_k-1\) nonidentity elements \(u\in H\) satisfy \(u^k=1\); all corresponding \((b,u)^k\) are the identity and contribute \(d_k-1\) after normalization. The \(u=1\) term is \((1/N)\sum_{b\in A}\eta(kb)=\mathbf1_{\eta^k=1}\). This establishes the first two formulas.

**Nonzero kernel classes.** Fix \(a\ne0\) and \(x=(b,u)\). The condition \(((a,1)x)^k=x^k\) is \(S_k(u)a=0\). For nonidentity \(u\), this happens exactly for the \(d_k-1\) nonidentity \(k\)-th roots of unity in \(H\), and then \(x^k=1\), giving \(d_k-1\) after dividing by \(|C_G(a)|=N\). For \(u=1\), the condition is \(ka=0\), and the remaining sum is \(N^{-1}\sum_b\psi(kb)=\mathbf1_{\psi^k=1}\). This proves the third formula.

**Complement classes.** Fix \(h_0\ne1\) and \(x=(b,u)\). Projection to \(H\) forces \(h_0^k=1\). Assume this. The equation \((h_0x)^k=x^k\) becomes
\[\bigl(h_0S_k(h_0u)-S_k(u)\bigr)b=0.\]
For \(u=1\) or \(u=h_0^{-1}\), this operator is respectively \(-k\) or \(h_0k\), up to the sign convention, so exactly \(t_k\) vectors \(b\) solve it. For the other \(d_k-2\) elements \(u\) satisfying \(u^k=1\), the operator vanishes and all \(N\) vectors solve it. If \(u^k\ne1\), both \(u-1\) and \(h_0u-1\) are invertible and the operator factors as a product of invertible factors including \((1-h_0)(u^k-1)\); hence only \(b=0\) solves it. The \(m\) choices \(b=0\) contribute \(\sum_{u\in H}\lambda(u^k)=m\mathbf1_{\lambda^k=1}\). Every additional solution \(b\ne0\) has \(x^k=1\), giving \((d_k-2)(N-1)+2(t_k-1)\) further contributions. Division by \(|C_G(h_0)|=m\) proves the final formula. The sign of the two special operators has no effect on their kernels.

**Integrality and reconstruction.** The subgroup \(A[k]\) is \(H\)-stable; \(H\) acts freely on its nonzero elements, so \(m\mid(t_k-1)\), and similarly \(m\mid(N-1)\). All displayed terms are therefore nonnegative integers. The dimensions of the simple modules are precisely \(1,m,N\), with \(1<m<N\), recovering \(m,N\) from the dimension-tagged spectrum. A prime dividing both \(|A|\) and \(m\) would give an order-prime element of \(H\) acting on nonzero \(p\)-torsion with a nonzero fixed vector, contradiction; hence \(\gcd(m,|A|)=1\). For any \(\ell\ge1\), all maximal-dimension modules have
\[\nu_{m\ell}=1+\frac{(N-1)(m-2)+2(t_\ell-1)}m,\]
since \(A[m\ell]=A[\ell]\). Thus the indicator multiset determines \(t_\ell\) for every \(\ell\). The values \(|A[p^j]|\) for every prime \(p\) and \(j\ge1\) determine all elementary divisors of the finite abelian group \(A\).

**Action-blindness and example.** The numbers of \(H\)-orbits in each fixed-order subset of \(A\setminus\{0\}\) and of \(\widehat A\setminus\{1\}\) equal their cardinalities divided by \(m\). Each indicator formula depends only on those orders, \(N\), \(m\), and \(t_k\), proving action-independence of the multiset. Over \(\mathbb F_7\), both matrices \(\operatorname{diag}(2,2)\) and \(\operatorname{diag}(2,4)\) have order three, and neither they nor their squares have eigenvalue one. The resulting semidirect products are not isomorphic: their characteristic Sylow-seven subgroup has conjugation action by the complement which is scalar in the first group and nonscalar in the second, a distinction invariant under changing the complement generator. The indicator spectra nevertheless coincide by the theorem.

## Verification
The included `verify_affine_double.py` enumerates group elements and computes the character sum in the indicator identity directly, independently of the closed formulas. It exhaustively tests all relevant module labels over scalar affine groups of orders \(3\cdot2\), \(4\cdot3\), \(5\cdot2\), \(5\cdot4\), \(7\cdot2\), \(7\cdot3\), \(7\cdot6\), \(8\cdot7\), \(9\cdot2\), \(9\cdot4\), and \(9\cdot8\) through the reported indices, including extension-field arithmetic. It also enumerates semidirect products with kernels \(C_9\), \(C_{25}\), and \(C_9^2\), exhibiting the genuinely nonelementary torsion term. It reports `VERIFY_OK_AFFINE_DOUBLE_INDICATORS` and `VERIFY_OK_ALL_FINITE_ABELIAN_KERNELS` if all checks pass. These are finite cross-checks and not a substitute for the proof.

## Relationship to prior work
The Drinfeld-double indicator identity is due to Kashina–Sommerhäuser–Zhu [3]; it is used, not re-proved, here. Keilberg [1] computed full higher-indicator formulas for semidirect products of cyclic groups with a **prime-order automorphism**, including nonabelian groups of order the product of two primes. These cases overlap with specializations here, but do not give the all-abelian-kernel, arbitrary-cyclic-complement distribution, its torsion-subgroup uniformity, or its action-blindness/reconstruction dichotomy. Iovanov–Mason–Montgomery [2] study integrality and related general criteria, rather than these full family-by-family values. Schauenburg [4] gives a character-table method for arbitrary Drinfeld doubles; it is a general computational framework, not an explicit evaluation for the family and signatures above. Existing general theory makes computation possible and leaves a historical-priority risk; the claim is limited to the explicit uniform evaluation and consequences just proved.

## Limitations
This result covers Drinfeld doubles of finite Frobenius groups with **abelian** kernel and **cyclic** complement; neither noncyclic complements nor nonabelian kernels are treated. It does not assert that the higher-indicator signature determines the semidirect-product action. The example explicitly shows that it does not. Literature priority is subject to further external historical review, and no independent mathematical audit has been performed.

## References
[1] M. Keilberg, *Higher indicators for some groups and their doubles*, arXiv:1004.1763 (first version 11 April 2010); especially Definition 2.1 and Sections 4–5. https://arxiv.org/abs/1004.1763

[2] M. Iovanov, G. Mason, S. Montgomery, *FSZ-groups and Frobenius–Schur indicators of quantum doubles*, arXiv:1208.4153 (first version 21 August 2012); especially Section 2. https://arxiv.org/abs/1208.4153

[3] Y. Kashina, Y. Sommerhäuser, Y. Zhu, *On higher Frobenius–Schur indicators*, Memoirs of the AMS 181 (2006), no. 855; especially the Drinfeld-double formula (as stated in [1] and [2]).

[4] P. Schauenburg, *Higher Frobenius–Schur indicators for Drinfeld doubles of finite groups through characters of centralizers*, arXiv:1604.02378 (first version 8 April 2016); especially Sections 2–3. https://arxiv.org/abs/1604.02378
