# The fourth-torsion threshold for Peirce spectra of finite abelian core quandles

## Finding

Let \(G\) be a finite abelian group, written additively, and let \(A_G\) be the complex vector space on basis elements \(e_g\), with bilinear multiplication
\[
e_x e_y=e_{2y-x},\qquad x,y\in G.
\]
For a **nonzero** idempotent \(u\in A_G\), let \(R_u(v)=vu\). The right Peirce spectrum is the union of the eigenvalue sets of \(R_u\) over all such \(u\). The complete classification is
\[
\operatorname{Spec}_{P}(A_G)=
\begin{cases}
\mathbb C,&\text{if }G\text{ has an element of order }4,\\
\{0,1,-1\},&\text{if }G\text{ has no order-four element but has a nontrivial odd-order element},\\
\{1\},&\text{if }2G=\{0\}.
\end{cases}
\]
The alternatives are exhaustive and disjoint (in the middle case, the entire \(2\)-primary subgroup has exponent at most \(2\)). In particular, even cyclic cores of order divisible by four have **every complex number** as a Peirce eigenvalue, whereas cores of even order congruent to two modulo four retain the discrete three-valued spectrum, except for the trivial quandle on two elements.

## Assumptions and scope

Throughout, the coefficient field is \(\mathbb C\). The group \(G\) is finite abelian, possibly trivial. The quandle is the core quandle with operation \(x*y=2y-x\). Only right multiplication by **nonzero** algebra idempotents is considered; including the zero idempotent would add \(0\) to the last case. This is the nonzero-idempotent convention in Zhang, Section 5.3, and in the earlier quandle Peirce literature. No assertion is made for nonabelian groups or other coefficient fields.

## Proof

Write \(\widehat G\) for the finite character group and, for \(a=\sum_g a_g e_g\), put \(c_\chi(a)=\sum_g a_g\chi(g)\). Character orthogonality makes \(a\mapsto(c_\chi(a))_{\chi\in\widehat G}\) a linear isomorphism. The defining multiplication gives, by setting \(z=2y-x\),
\[
c_\chi(vw)=c_{\chi^{-1}}(v)c_{\chi^2}(w).
\tag{1}
\]
For an idempotent \(u\), abbreviate \(c_\chi=c_\chi(u)\). Then
\[
c_\chi=c_{\chi^{-1}}c_{\chi^2},\qquad
c_\chi(R_uv)=c_{\chi^2}c_{\chi^{-1}}(v).
\tag{2}
\]
Set \(P_\chi=c_\chi c_{\chi^{-1}}\). Multiplying the first equation at \(\chi\) and \(\chi^{-1}\) gives
\[
P_\chi=P_\chi P_{\chi^2}.
\tag{3}
\]
The second equation implies that \(R_u^2\) is diagonal in Fourier coordinates, with eigenvalue \(P_{\chi^2}\) at coordinate \(\chi\).

Assume first that \(G\) has no element of order four. Its \(2\)-primary subgroup is elementary abelian, so \(\widehat G=E\times H\) with \(E\) of exponent at most two and \(H\) of odd order. Every square \(\chi^2\) lies in \(H\), and squaring permutes \(H\). For any \(\eta\in H\), either \(P_\eta=0\) or equation (3) gives \(P_{\eta^2}=1\). Iterating around the finite squaring cycle that returns to \(\eta\) proves \(P_\eta=1\) in the latter case. Therefore \(R_u^2\) has eigenvalues only \(0\) and \(1\), so every eigenvalue of \(R_u\) belongs to \(\{0,1,-1\}\).

When \(2G=\{0\}\), the multiplication is \(e_xe_y=e_x\). Thus \(u^2=\varepsilon(u)u\), where \(\varepsilon\) is the sum of coefficients. Any nonzero idempotent has \(\varepsilon(u)=1\); its right multiplication is the identity, giving exactly \(\{1\}\).

Suppose instead that \(G\) has a nontrivial odd-order element. The basis idempotent \(e_0\) has right multiplication \(e_g\mapsto e_{-g}\). An element of odd order greater than one supplies a two-element inversion orbit; hence \(1\) and \(-1\) occur. The nonzero uniform idempotent \(\omega=|G|^{-1}\sum_g e_g\) gives \(R_\omega(e_x)=|2G|^{-1}\sum_{h\in 2G}e_{h-x}\). Since \(2G\neq\{0\}\), choose distinct \(x,x'\) in the same coset of \(2G\), and \(R_\omega(e_x-e_{x'})=0\). This supplies \(0\), proving the middle case.

Finally suppose that \(G\) contains an element of order four. By finite abelian duality, there is \(\theta\in\widehat G\) of order four. Put \(\psi=\theta^2\), an order-two character. For each arbitrary \(t\in\mathbb C\), define
\[
u_t=\frac1{|G|}\sum_{g\in G}(1+t\psi(g))e_g.
\tag{4}
\]
The Fourier coefficients of \(u_t\) are \(c_1=1\), \(c_\psi=t\), and all others zero. They satisfy the first identity in (2), because \(\psi^{-1}=\psi\) and \(\psi^2=1\); hence \(u_t^2=u_t\), and \(u_t\neq0\) because \(c_1=1\). Formula (2) shows that, on the Fourier-coordinate pair \(\theta,\theta^{-1}\), right multiplication by \(u_t\) has matrix
\[
\begin{pmatrix}0&t\\t&0\end{pmatrix},
\]
with eigenvalues \(t\) and \(-t\). Since \(t\) is arbitrary, every complex number occurs. This proves the first case and completes the classification. \(\square\)

## Verification

The standalone `verify.py` constructs the multiplication and right-multiplication matrices with exact rational arithmetic. Its 27 checks comprise 18 explicit parameter/group tests with four-torsion and nine tests of the no-four-torsion cases. It verifies directly the idempotent relation, the prescribed \(\pm t\) eigenvectors, and the \(\{0,1,-1\}\) or \(\{1\}\) eigenvalue witnesses. The finite computations are sanity checks; the argument above applies to every finite abelian group and every complex parameter without enumeration.

## Relationship to prior work

Zhang, *Group-ring methods for Alexander quandle rings* (arXiv:2610.08204v1, Sections 5.1 and 5.3), proves the Fourier product identity and the odd-order case \(\{0,1,-1\}\). That established odd-order theorem is **not** claimed new here. Its proof relies on squaring being a permutation of the entire character group; for even groups the relevant square map is not invertible. The new assertion is the **complete even-order boundary**: a discrete spectrum when the Sylow-two subgroup has exponent at most two, and the unrestricted complex spectrum as soon as an element of order four exists.

Kaur and Singh, *A note on idempotents in quandle rings* (arXiv:2609.09183v1, Section 3), treat odd dihedral orders. Elhamdadi, Nunez, and Singh, *Enhancements of link colorings via idempotents of quandle rings* (arXiv:2207.09257v1, Section 7), demonstrate full complex spectrum for a different non-Latin quandle of order three and a discrete spectrum for the Latin dihedral quandle of order three; their theorem is not an even-core classification. The current result shows that non-Latinity alone does **not** determine the Peirce spectrum: elementary-two cores are non-Latin yet have spectrum \(\{1\}\).

## Limitations

The originality comparison is based on the inspected papers, targeted research-record searches, and accessible related results; it is not an exhaustive proof that no equivalent argument appears elsewhere. The recent paper of Elhamdadi, Ta, and Virgin on Fourier idempotents (arXiv:2609.03799) was identified, but its complete text was not inspected and may conceal a relevant equivalent formulation; its abstract describes integral idempotents rather than Peirce spectra. This classification concerns right multiplication only and does not classify individual idempotent varieties, multiplicities of all eigenvalues, or arbitrary Alexander operations. Independent external mathematical validation has not been performed.

## References

1. Zhi-Lin Zhang, *Group-ring methods for Alexander quandle rings*, arXiv:2610.08204v1 (October 6, 2026), https://arxiv.org/html/2610.08204v1.
2. Dilpreet Kaur and Pushpendra Singh, *A note on idempotents in quandle rings*, arXiv:2609.09183v1 (August 29, 2026), https://arxiv.org/html/2609.09183v1.
3. Mohamed Elhamdadi, Brandon Nunez, and Mahender Singh, *Enhancements of link colorings via idempotents of quandle rings*, arXiv:2207.09257v1 (2022), https://arxiv.org/html/2207.09257v1.
4. Mohamed Elhamdadi, Luc Ta, and Bryce Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799v1 (September 3, 2026), https://arxiv.org/abs/2609.03799.
5. Birama Sangare and Luc Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550 (August 3, 2026), https://arxiv.org/abs/2608.01550.
