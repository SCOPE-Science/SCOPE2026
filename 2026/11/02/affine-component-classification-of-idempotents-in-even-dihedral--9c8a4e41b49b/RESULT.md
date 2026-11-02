# Affine-component classification of idempotents in even dihedral quandle algebras

## Finding

For every odd integer \(m\ge 1\), let \(R_{2m}=\mathbb Z/(2m)\mathbb Z\) have dihedral quandle product \(i\triangleright j=2j-i\), and let \(A_{2m}=\mathbb C[R_{2m}]\) be its complex nonassociative quandle algebra, with \(e_i e_j=e_{2j-i}\). Its **idempotent algebraic set**
\[
\mathscr E_{2m}=\{a\in A_{2m}:a^2=a\}
\]
is a finite disjoint union of complex affine spaces. Under the natural algebra homomorphism \(\pi_*:A_{2m}\to A_m=\mathbb C[R_m]\) induced by reduction of subscripts modulo \(m\), every fiber over an idempotent \(b\in A_m\) is one irreducible connected component, **canonically an affine translate of the \(+1\) right-Peirce eigenspace** \(\ker(R_b-I)\), where \(R_b(v)=vb\). Thus it is isomorphic to \(\mathbb A^{D(b)}_{\mathbb C}\), where
\[
D(b)=\varepsilon(b)+\tfrac12\#\{t\in\mathbb Z/m\mathbb Z\setminus\{0\}:\widehat b(t)\ne0\}.
\]
Here \(\varepsilon(b)=\sum_j b_j\in\{0,1\}\) is augmentation and \(\widehat b(t)=\sum_j b_j\exp(2\pi i tj/m)\). In particular, zero is the unique isolated idempotent; all nonzero idempotents belong to positive-dimensional affine families. The maximum component dimension is \((m+1)/2\).

The **component-dimension polynomial**, which counts irreducible components rather than individual complex points, is exactly
\[
\boxed{\quad
P_{2m}(z):=\sum_{\text{irreducible components }C\subseteq\mathscr E_{2m}}z^{\dim C}
=(1+z)\prod_{\substack{d\mid m\\d>1}}
\left(1+\Delta_d z^{h_d/2}\right)^{\varphi(d)/h_d}.\quad}
\]
Here \(h_d=|\langle-1,2\rangle\le(\mathbb Z/d\mathbb Z)^\times|\), \(r_d=\operatorname{ord}_d(2)\), and
\[
\Delta_d=\begin{cases}
2^{r_d/2}+1,&-1\in\langle2\rangle\pmod d,\\
2^{r_d}-1,&-1\notin\langle2\rangle\pmod d.
\end{cases}
\]
The first case necessarily has even \(r_d\). The empty product for \(m=1\) is one.

In particular, the number of connected components is \(P_{2m}(1)\), their ordinary cohomology is concentrated in degree zero, and the number of maximal-dimensional components is \(\prod_{d\mid m,\,d>1}\Delta_d^{\varphi(d)/h_d}\). The new assertion concerns **even-order lifting geometry**; the arithmetic root multiplicities of nonzero Fourier orbits in the odd-order base are a separate, previously accessible enumeration and are rederived below only to make this classification self-contained.

## Assumptions and scope

All algebraic sets are considered over \(\mathbb C\), with their reduced affine-variety structures. Idempotents include zero. The operation is a right-distributive quandle multiplication, extended bilinearly; no associativity is assumed. The integer \(m\) is odd and at least one, so the assertion covers orders \(2,6,10,14,18,\ldots\) but not orders divisible by four. The field is \(\mathbb C\) throughout the theorem; finite-field calculations in verification are illustrations, not assertions in characteristic dividing the modulus. The Poincaré polynomial here records component **dimensions**, not graded ordinary singular cohomology.

## Proof

**1. The square-zero covering and the Peirce fiber.** Let \(e_i\) denote basis elements of \(A_{2m}\), and write \(\bar e_i\) for basis elements of \(A_m\). Define \(s(\bar e_i)=\tfrac12(e_i+e_{i+m})\), and \(\kappa_i=(-1)^i(e_i-e_{i+m})\), with indices \(i\) understood modulo \(m\). Because \(m\) is odd, \(\kappa_{i+m}=\kappa_i\). Direct basis multiplication gives
\[
s(\bar e_i)s(\bar e_j)=s(\bar e_{2j-i}),\qquad
s(\bar e_i)\kappa_j=0,\qquad
\kappa_i\kappa_j=0,\qquad
\kappa_i s(\bar e_j)=\kappa_{2j-i}.
\]
Consequently \(s\) is an algebra-homomorphic section of \(\pi_*\), and its kernel \(K\) is a right-annihilator square-zero ideal. Under the linear module identification \(\kappa_i\leftrightarrow\bar e_i\), the right \(A_m\)-action on \(K\) is the ordinary right regular action. Any element of \(A_{2m}\) has a unique expression \(s(b)+\kappa(w)\), and its square is \(s(b^2)+\kappa(wb)\). Therefore the complete idempotent equation is **equivalent** to \(b^2=b\) together with \(R_b(w)=w\). This already proves the Peirce-fiber identification, without restricting \(b\) to trivial idempotents.

**2. Fourier equations.** For \(n\ge 2\) set \(\zeta_n=\exp(2\pi i/n)\) and define \(F_t(a)=\sum_{x=0}^{n-1}a_x\zeta_n^{tx}\), with indices modulo \(n\). By the multiplication rule,
\[
F_t(a^2)=\sum_{x,y}a_xa_y\zeta_n^{t(2y-x)}=F_{-t}(a)F_{2t}(a).
\]
Fourier inversion is an invertible linear change of complex coordinates. Thus the complete idempotent system is \(F_t=F_{-t}F_{2t}\), for every residue \(t\). Its zeroth equation is \(F_0\in\{0,1\}\).

**3. The odd base.** Write \(n=m\) with \(m\) odd. Since multiplication by \(2\) and by \(-1\) permutes all residues, the nonzero residues split into orbits of \(H_m=\langle2,-1\rangle\). On each orbit, either all Fourier coordinates vanish or none does. Indeed, if one is nonzero, both successors under \(-1\) and \(2\) are nonzero, and the finite generated permutation action is transitive. On a nonzero orbit \(\mathcal O\), the binomial equations define an isogeny kernel in a complex torus: the integer exponent matrix is \(I-P_{-1}-P_2\), with \(P_u\) the permutation matrix indexed by multiplication by \(u\). Its determinant is nonzero. A complex torus monomial homomorphism with integer nonsingular exponent matrix has precisely the absolute determinant many solutions (Smith normal form), each isolated and reduced; on a zero Fourier orbit the Jacobian is the identity, so the all-zero orbit solution is reduced as well.

For a Fourier character of additive order \(d>1\), the orbit has length \(h_d\). If \(-1\) is not generated by \(2\), its permutation group is \(C_{r_d}\times C_2\); simultaneous diagonalization gives eigenvalues \(1-s-\omega\) for \(s=\pm1\) and \(\omega^{r_d}=1\). The absolute product is \(2^{r_d}-1\). If \(-1=2^{r_d/2}\pmod d\), the group is \(C_{r_d}\), and the eigenvalues are \(1-(-1)^j-\exp(2\pi ij/r_d)\); their absolute product is \(2^{r_d/2}+1\). In either case the nonzero-solution count is \(\Delta_d\). There are \(\varphi(d)/h_d\) such orbits. Hence the odd-base idempotents form a **finite discrete** set with independent zero or \(\Delta_d\) nonzero choices on each orbit, as well as the augmentation choice \(0\) or \(1\).

A further identity needed below holds for every nonzero base Fourier coefficient: \(F_t F_{-t}=1\). To see this, choose a nonzero \(F_s\) with \(2s=t\), possible because doubling permutes the odd-base orbit. The paired equations \(F_s=F_{-s}F_t\) and \(F_{-s}=F_sF_{-t}\) imply \(F_tF_{-t}=1\).

**4. The even lift and fiber dimension.** Now put \(n=2m\). The even frequencies \(F_{2j}(a)\) are precisely the Fourier coordinates of \(\pi_*(a)\) on \(R_m\), and form a closed autonomous copy of the odd-base idempotent equations. Fix one odd-base solution \(b\) and its even-frequency data. Every odd frequency \(k\) other than \(m\) pairs with a distinct odd frequency \(-k\). Write \(c=F_{2k}(a)\), \(c'=F_{-2k}(a)\). The remaining equations are the homogeneous linear system
\[
F_k=cF_{-k},\qquad F_{-k}=c'F_k.
\]
If \(c=0\), the odd-base orbit condition also forces \(c'=0\), so both odd coordinates vanish. If \(c\ne0\), step 3 gives \(cc'=1\), and this system has one unrestricted complex parameter. As \(k\mapsto2k\) is a bijection from odd residues modulo \(2m\) to even residues, each nonzero base orbit of length \(h_d\) supplies exactly \(h_d/2\) independent affine parameters. There is exactly one self-opposite odd frequency, \(k=m\); its equation reads \(F_m=F_mF_0\), so it contributes one free parameter when \(F_0=1\) and none when \(F_0=0\).

Therefore the fiber of \(\mathscr E_{2m}\to\mathscr E_m\) above \(b\) is a **linear** affine subspace of dimension \(D(b)\), with no additional hidden equations. Each base solution is isolated and reduced by the nonsingular exponent-matrix calculation; a finite discrete base decomposes the total reduced algebraic set into disjoint closed-and-open fibers. Each such fiber is irreducible and smooth, proving the component description and smoothness of the reduced variety.

**5. Component count and extremal dimensions.** The two independent augmentation values contribute \(1+z\). An order-\(d\) orbit contributes either zero dimension with one choice, or dimension \(h_d/2\) with \(\Delta_d\) choices; multiplying the factors gives \(P_{2m}(z)\). Every orbit can be chosen active, and the augmentation can be one, yielding dimension \((m-1)/2+1=(m+1)/2\). Exactly the product of all the \(\Delta_d\) choices achieves this maximum. Only the all-zero base Fourier solution with augmentation zero yields dimension zero, hence zero is the sole isolated idempotent. Each affine component is analytically contractible, proving the cohomological statement.

## Verification

The supplied standalone script `verify.py` checks the integer exponent determinants independently by fraction-free Bareiss elimination for all Fourier orbits with odd \(m\in\{1,3,5,7,9,11,13,15,21,25,31\}\), and compares each to the arithmetic expression for \(\Delta_d\). It then *independently* enumerates all coefficient tuples over \(\mathbb F_5\) for \(R_2\) and over \(\mathbb F_7\) for \(R_6\), computing the quandle square directly without Fourier equations. Grouping these solutions by the even Fourier projection yields respectively the fiber-size histograms \(\{1:1,5:1\}\) and \(\{1:1,7:4,49:3\}\). In particular the latter has exactly \(176\) idempotents, in eight fibers, as predicted by \(P_6(z)=1+4z+3z^2\) after evaluating dimensions over the field. These are finite checks only; the proof for all odd \(m\) is algebraic.

Examples of dimension polynomials include \(P_2(z)=1+z\), \(P_6(z)=1+4z+3z^2\), \(P_{10}(z)=1+z+5z^2+5z^3\), and \(P_{18}(z)=1+4z+3z^2+9z^3+36z^4+27z^5\).

## Relationship to prior work

Elhamdadi–Nunez–Singh–Swain (2022), Theorem 4.5 and Corollary 4.8, give quandle-covering descriptions **conditional on the base algebra having only trivial idempotents**; this condition does not hold for the complex algebras of nontrivial odd dihedral quandles. The new component theorem handles every complex odd-base idempotent, including nontrivial and augmentation-zero ones. Elhamdadi–Nunez–Singh (2022) compute idempotents over the integers and fields of characteristic two for small quandles, and discuss complex Peirce spectra; that is distinct from a whole-family affine-component classification. Elhamdadi–Ta–Virgin (2026), especially Proposition 3.4 and Section 4, derive the complex Fourier idempotence relation and prove **integral** odd-core rigidity; their Fourier relation is a known ingredient rather than a new assertion here. Sangare–Ta (2026) treat automorphism groups for the even dihedral family, not the complex idempotent component scheme. Zhang (2026) treats integral filtration and odd-core Peirce spectra, not this even-order idempotent variety. The orbit-root counts in step 3 are included for completeness, not proposed as an independent new result. The claimed new mathematical content is the explicit square-zero/Peirce *even-order fiber geometry*, smooth affine decomposition, component dimension generating polynomial and topological consequences.

## Limitations

The classification is restricted to modulus exactly twice an odd number. When the modulus is divisible by four, the doubling map has longer transient branches; the linear fiber argument in step 3 no longer applies directly and no conclusion is claimed. The result is over \(\mathbb C\), and does not automatically describe the arithmetic or scheme structure over fields of positive characteristic. The word 'smooth' refers to the **reduced complex algebraic set**; no assertion about a possibly nonreduced presentation scheme is necessary. Novelty is assessed against the sources examined, not certified global priority. No independent mathematical audit has been performed.

## References

1. M. Elhamdadi, B. Nunez, M. Singh, D. Swain, *Idempotents, free products and quandle coverings*, arXiv:2204.11288 (first public version 2022-04-24), especially Sections 3–4.
2. M. Elhamdadi, B. Nunez, M. Singh, *Enhancements of link colorings via idempotents of quandle rings*, arXiv:2207.09257 (first public version 2022-07-19), especially Sections 6–7.
3. B. Sangare, L. Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550 (2026), Sections 3–4.
4. M. Elhamdadi, L. Ta, B. Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799 (2026), Proposition 3.4 and Section 4.
5. Z.-L. Zhang, *Group-ring methods for Alexander quandle rings*, arXiv:2610.08204 (2026), Sections 3–5.
