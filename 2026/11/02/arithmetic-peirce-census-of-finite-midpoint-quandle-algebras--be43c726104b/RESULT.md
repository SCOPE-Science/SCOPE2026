# Arithmetic Peirce census of finite midpoint-quandle algebras

## Finding

Let \(G\) be any finite abelian group of odd order \(m\geq1\), let \(Q=M(G)\) be the midpoint quandle with \(x*y=(x+y)/2\), and let \(\mathcal A_K=K[Q]\) for \(K=\mathbb C\) or \(K=\mathbb R\). Multiplication in this (generally nonassociative) algebra is the bilinear extension of the quandle product. Write \(\operatorname{Idem}(\mathcal A_K)=\{u:u^2=u\}\), including zero, and \(\rho_u(v)=vu\).

Let \(\widehat G\) be the group of complex characters, and let \(\sigma\) permute it by \((\sigma\chi)(g)=\chi(g/2)\). For each \(\sigma\)-orbit \(O\), let \(\ell(O)=|O|\) and \(-O=\{\chi^{-1}:\chi\in O\}\). Partition the orbits into the singleton trivial orbit \(O_0=\{1\}\), nontrivial self-dual orbits \(\mathcal S=\{O\neq O_0:-O=O\}\), and unordered pairs \(\mathcal P=\{\{O,-O\}:O\neq -O\}\). Every orbit in \(\mathcal S\) has even length.

For an idempotent, its Peirce characteristic polynomial means \(P_u(t)=\det(tI-\rho_u)\), with eigenvalues taken over \(\mathbb C\) even when \(u\) is real. There is a complete factorization rule: each orbit \(O\) is either inactive, contributing \(t^{\ell(O)}\), or active, contributing \(t^{\ell(O)}-1\); in the real case, paired orbits must be simultaneously active or inactive. The exact weighted generating polynomials of these activation profiles are

\[
\mathcal F_{\mathbb C}=\prod_{O}\left(T_{\ell(O)}+(2^{\ell(O)}-1)Z_{\ell(O)}\right),
\]
\[
\mathcal F_{\mathbb R}=(T_1+Z_1)
\prod_{O\in\mathcal S}\left(T_{\ell(O)}+(2^{\ell(O)/2}+1)Z_{\ell(O)}\right)
\prod_{\{O,-O\}\in\mathcal P}\left(T_{\ell(O)}^2+(2^{\ell(O)}-1)Z_{\ell(O)}^2\right).
\]

These are polynomial identities with independent formal variables \(T_j,Z_j\). A term's coefficient is the number of idempotents having that orbit-activity profile: \(T_j\) records an inactive block of size \(j\), and \(Z_j\) an active block of size \(j\). Consequently substituting \(T_j=t^j\), \(Z_j=t^j-1\) produces the sum of all Peirce characteristic polynomials, with full multiplicity information retained by the unreduced multivariate expression. Substituting \(T_j=1\), \(Z_j=z^j\) gives the exact Peirce-rank enumerator. In particular,

\[
|\operatorname{Idem}(\mathcal A_{\mathbb C})|=2^m,
\qquad
|\operatorname{Idem}(\mathcal A_{\mathbb R})|
=2\prod_{O\in\mathcal S}(2^{\ell(O)/2}+2)
\prod_{\{O,-O\}\in\mathcal P}2^{\ell(O)}.
\]

For a cyclic group \(G=\mathbb Z/p\mathbb Z\) of odd prime order \(p\), put \(d=\operatorname{ord}_p(2)\). If \(d\) is odd, the real count is \(2^{(p+1)/2}\). If \(d\) is even, the real count is \(2(2^{d/2}+2)^{(p-1)/d}\). For two different groups of order nine, the real counts distinguish their midpoint quandles:

\[
|\operatorname{Idem}(\mathbb R[M(\mathbb Z/9\mathbb Z)])|=80,
\qquad
|\operatorname{Idem}(\mathbb R[M((\mathbb Z/3\mathbb Z)^2)])|=512.
\]

Both corresponding complex algebras have \(512\) idempotents. By the midpoint classification of finite medial commutative quandles, the theorem applies to every finite quandle in that class, not merely to cyclic quandles.

## Assumptions and scope

The coefficient fields in the theorem are exactly \(\mathbb R\) and \(\mathbb C\). The finite abelian group has odd order, so doubling is invertible and the midpoint operation is defined. Right multiplication \(\rho_u\) is a linear operator of dimension \(m\); it is not assumed to be a projection. Counts refer to distinct algebra elements, not isomorphism classes, and include zero. Every idempotent is included with no restriction on coefficient support or augmentation. The proof does not assert an analogous formula in positive coefficient characteristic.

## Proof

**1. Fourier transport and all complex solutions.** Write \(\tau(g)=g/2\), and identify the vector space \(\mathbb C[Q]\) with the ordinary group algebra \(\mathbb C[G]\). Since \(x*y=\tau(x+y)\), the quandle multiplication is

\[
u\star v=\tau_*(uv),
\]

where juxtaposition is the associative group-algebra product. For \(\chi\in\widehat G\), put \(c_\chi=\widehat u(\chi)=\sum_g a_g\chi(g)\) when \(u=\sum_g a_g e_g\). Fourier inversion is bijective since the characters of \(G\) form an orthogonal basis. The Fourier transform of the product satisfies

\[
\widehat{u\star v}(\chi)=\widehat u(\sigma\chi)\widehat v(\sigma\chi).
\]

Thus idempotency is **equivalent**, in both directions, to the complete system

\[
c_\chi=c_{\sigma\chi}^2\quad(\chi\in\widehat G).
\]

On any \(\sigma\)-cycle \(O=(\chi_0,\ldots,\chi_{\ell-1})\), this implies \(c_{\chi_0}^{2^\ell}=c_{\chi_0}\). There are exactly \(2^\ell\) roots of \(z^{2^\ell}=z\) in \(\mathbb C\): zero and the \(2^\ell-1\) roots of unity of order dividing \(2^\ell-1\). Conversely, choose any such starting value \(w\); set \(c_{\chi_0}=w\) and, for \(1\leq j<\ell\), \(c_{\chi_j}=w^{2^{\ell-j}}\). These values satisfy every equation of the cycle. Different cycles are independent under Fourier inversion. Therefore the product of their solution counts is \(\prod_O2^{\ell(O)}=2^m\), and each cycle is either entirely zero or entirely nonzero.

**2. Reality and inversion of characters.** The inverse Fourier transform has all real coefficients precisely when

\[
c_{\chi^{-1}}=\overline{c_\chi}\qquad(\chi\in\widehat G).
\]

Inversion commutes with \(\sigma\). A non-self-dual pair \(\{O,-O\}\) is determined by choosing the data on one orbit and taking complex conjugates on the other. It consequently has exactly \(2^\ell\) real-compatible choices: one both-inactive choice and \(2^\ell-1\) both-active choices.

For a self-dual nontrivial orbit, inversion acts as a fixed-point-free involution on the cycle: since \(G\) has odd order, no nontrivial character equals its inverse. Thus the length is \(2h\) and inversion sends \(\chi_0\) to \(\chi_h\). If \(w=c_{\chi_0}\neq0\), the cycle equations give \(c_{\chi_h}=w^{2^h}\). Because \(w\) is a root of unity, the realness condition is equivalent to

\[
w^{2^h}=\overline w=w^{-1},\qquad\text{or}\qquad w^{2^h+1}=1.
\]

Exactly \(2^h+1\) nonzero choices satisfy this, plus the all-zero choice. The trivial-character orbit has precisely the real choices zero and one. Multiplying the independently admissible orbit counts proves the real formula and its multivariate enumerator.

**3. Peirce blocks and characteristic polynomials.** For an idempotent \(u\), Fourier transformation conjugates \(\rho_u\) to

\[
(\widehat{\rho_u(v)})_\chi=c_{\sigma\chi}\widehat v(\sigma\chi).
\]

Each \(\sigma\)-orbit is an invariant coordinate block of length \(\ell\). If its \(c\)-coordinates are zero, the block is the zero operator with characteristic polynomial \(t^\ell\). Otherwise it is a weighted cyclic permutation with all weights nonzero. Multiplying the idempotency equations over the orbit gives \(P=P^2\) for \(P=\prod_{\chi\in O}c_\chi\); since \(P\neq0\), necessarily \(P=1\). A weighted cyclic permutation of length \(\ell\) and weight product one has characteristic polynomial \(t^\ell-1\): its cyclic basis vectors imply its \(\ell\)-th power is identity, and its characteristic polynomial is the standard companion polynomial. Every active block has rank \(\ell\), every inactive block rank zero. Combining this with the choices from steps 1 and 2 proves both spectral enumerators, as well as the prescribed substitutions for characteristic polynomials and ranks. The claim does not depend on numerical diagonalization.

**4. Prime and nine-element illustrations.** For \(G=\mathbb Z/p\mathbb Z\), the action of \(\sigma\) on nontrivial characters has orbit length \(d=\operatorname{ord}_p(2)\). When \(d\) is odd, inversion pairs the \((p-1)/d\) orbits, giving the stated power of two. When \(d\) is even, the unique element of order two in \((\mathbb Z/p\mathbb Z)^\times\) is \(2^{d/2}=-1\); all nontrivial orbits are self-dual, giving the stated product. For \(\mathbb Z/9\mathbb Z\) the nontrivial orbits have lengths two and six, both self-dual, and the real count is \(2\cdot4\cdot10=80\). For \((\mathbb Z/3\mathbb Z)^2\), the eight nontrivial characters split into four self-dual orbits of length two, and the real count is \(2\cdot4^4=512\). These are consequences of the general theorem, not additional assumptions.

## Verification

Run `python3 verify.py` with Python 3 and the standard library. The verifier derives doubling-orbits from scratch for the cyclic groups of orders \(1,3,5,7,9,11,13\), enumerates every real-compatible Fourier solution, checks its real inverse transform and the full idempotent equation in the original quandle basis, and compares the characteristic polynomial of the concrete multiplication matrix with the predicted orbit factorization. It separately checks all \(512\) real idempotents for the noncyclic group \((\mathbb Z/3\mathbb Z)^2\). Outputs include complex counts \(2^m\), real counts \(2,8,12,16,80,68,132\) for those cyclic orders, and real count \(512\) for the noncyclic nine-element example. The final output is `VERIFY_OK`.

The code uses numerical complex arithmetic for finite-instance corroboration, with explicit tolerances; the general theorem is proved symbolically in the preceding section. Neither enumeration nor numerical tolerance is used as an infinite proof or an assertion of exhaustive historical novelty.

## Relationship to prior work

Zhang's October 2026 treatment of Alexander quandle rings establishes Fourier transport and the idempotent cycle equation used in step 1, primarily to classify **integral** idempotents of finite commutative midpoint quandles. In particular, the complex orbit equation and its immediate complex solution count follow from that work; the standalone complex cardinality is **not** asserted to be an independently new structural theorem. The contribution here is the **simultaneous real idempotent and Peirce characteristic-polynomial distribution** for every finite medial commutative quandle: conjugate-orbit pairing, self-dual character arithmetic, spectral block factorization, and exact weighted enumerators, including the contrast between the two order-nine examples.

Ta's midpoint classification supplies the reduction from general finite medial commutative quandles to finite odd-order abelian groups. Sangare and Ta study integral/characteristic-two idempotents and quandle automorphisms, not this real Peirce census. Churchill and collaborators address integer-coefficient idempotent equations for the order-five cyclic midpoint quandle. Elhamdadi, Nunez, and Singh study complex Peirce spectra for the **dihedral core** quandles, which have a different multiplication except at order three. A published three-element result giving eight idempotents for the dihedral algebra in coefficient characteristic different from three agrees with, but cannot cover, the all-odd-group real spectrum and rank classification here.

Searches for aliases including real midpoint-quandle idempotents, weighted Fourier cycles, medial commutative Peirce spectra, and cyclic quandle characteristic polynomials did not locate an equivalent general real-spectrum enumerator. Absence from searches is not a proof of historical uniqueness.

## Limitations

The result concerns finite medial commutative quandles and coefficients in \(\mathbb R\) or \(\mathbb C\), not general Alexander quandles, noncommutative quandles, or positive-characteristic coefficients. These counts are basis-independent under quandle isomorphism but do not by themselves classify every quandle up to isomorphism. The complex cardinality is a direct consequence of an established Fourier equation; novelty and mathematical value are assessed specifically for the real and spectral joint distribution. Older equivalent results under different language could exist, and independent mathematical validation has not been carried out.

## References

1. Z.-L. Zhang, *Group-ring methods for Alexander quandle rings*, arXiv:2610.08204 (first posted 2026-10-06), Sections 2 and 5. <https://arxiv.org/abs/2610.08204>
2. L. Ta, *On medial Latin quandles and affine modules*, arXiv:2602.08875 (2026), Corollary 4.2. <https://arxiv.org/abs/2602.08875>
3. B. Sangare and L. Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550v2 (2026), Sections 3 and 4. <https://arxiv.org/html/2608.01550v2>
4. G. Churchill, I. R. Churchill, N. Fernando, and B. Kousik, *A further study of quandles and quandle rings*, arXiv:2608.09149v1 (2026), Section 4. <https://arxiv.org/html/2608.09149v1>
5. M. Elhamdadi, B. Nunez, and M. Singh, *Enhancements of link colorings via idempotents of quandle rings*, arXiv:2207.09257 (2022 preprint; later publication), Section 7. <https://arxiv.org/abs/2207.09257>
