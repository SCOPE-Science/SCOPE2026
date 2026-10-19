# Involution fibers and cubic conjugacy obstructions in truncated free associative algebras

## Finding

For any integer \(n\geq3\) and finite field \(k=\mathbb F_q\), let \(V=k^n\) and let
\[
A_n(k)=T_k(V)/(V)^{3}=k\oplus V\oplus(V\otimes_k V).
\]
Here \((V)\) denotes the two-sided augmentation ideal in the tensor algebra, so multiplication by words of total length at least three is zero. Let \(I_n(q)\) denote the number of unital \(k\)-algebra automorphisms \(g\) of \(A_n(k)\) satisfying \(g^2=\mathrm{id}\), including the identity. Write \({a\brack b}_q\) for the Gaussian binomial coefficient, with \(0\le b\le a\), and \(|\mathrm{GL}_0(k)|=1\).

**Odd characteristic.** For \(q\) odd, the exact rank-resolved count is
\[
\boxed{I_n(q)=\sum_{v=0}^{n}{n\brack v}_q\,q^{v(n-v)+3(n-v)^2v+v^3}.}
\]
More precisely, if the induced map on \(V\) has a \((-1)\)-eigenspace of dimension \(v\), then there are \({n\brack v}_q q^{v(n-v)}\) possible induced maps and exactly \(q^{3(n-v)^2v+v^3}\) involutory lifts above each one. Every such lift is conjugate by an automorphism acting trivially on \(V\) to the corresponding *linear* automorphism; hence each fiber is one orbit under the kernel of reduction to \(\mathrm{GL}(V)\).

**Characteristic two.** For \(q\) even, write \(s=n-2r\). The rank-resolved count is
\[
\boxed{I_n(q)=\sum_{r=0}^{\lfloor n/2\rfloor}{n\brack r}_q{n-r\brack r}_q|\mathrm{GL}_r(k)|\;q^{(n^3+s^3)/2}.}
\]
Here \(r=\operatorname{rank}(g_{\mathrm{lin}}-I)\). For each fixed square-one linear map of rank \(r\), its involutory lifts form exactly \(q^{s^3}\) distinct conjugacy orbits under automorphisms inducing identity on \(V\); each such orbit has size \(q^{(n^3-s^3)/2}\). Thus the \(s^3\) residual dimension is an exact obstruction to eliminating quadratic terms by a quadratic change of generators. In particular, when \(s=0\), all lifts over a fixed linear part are conjugate; if \(s>0\), genuinely distinct classes remain.

In either characteristic, subtracting one from \(I_n(q)\) counts automorphisms of **exact** order two.

## Assumptions and scope

All maps are unital \(k\)-algebra maps, required to fix \(k\) pointwise; they are not arbitrary linear involutions of the underlying vector space. A square-one automorphism may be the identity, and thus the formula includes it. The restrictions are finite fields, \(n\ge3\), tensor-word cutoff three, and conjugacy specifically by the normal subgroup acting identically on \(V=J/J^2\). No full-group conjugacy classification is claimed. The formulas are uniform in prime powers, including nonprime finite fields.

## Proof

**1. Automorphism coordinates.** Let \(J=V\oplus(V\otimes V)\). It is the unique maximal ideal and \(J^3=0\). An algebra endomorphism that fixes \(k\) is determined by the images of a chosen basis of \(V\), and each image belongs to \(J\). Therefore the image map has a unique form \(v\mapsto Lv+Bv\), where \(L\in\operatorname{End}_k(V)\) and \(B\in\operatorname{Hom}_k(V,V\otimes V)\). It is invertible exactly when \(L\) is invertible, since its matrix in the grading is block-upper-triangular with diagonal blocks \(1,L,L\otimes L\).

Let \(M=\operatorname{Hom}_k(V,V\otimes V)\), an additive group of dimension \(n^3\). Let \(u_C\) denote the automorphism \(u_C(v)=v+Cv\), and \(\ell_L\) the linear automorphism \(\ell_L(v)=Lv\). Because substitutions of a quadratic word into a quadratic word have degree at least three, \(u_Cu_D=u_{C+D}\). Conjugation gives
\[
\ell_Lu_C\ell_L^{-1}=u_{\rho(L)C},\quad \rho(L)C=(L\otimes L)CL^{-1}.
\]
Thus \(\operatorname{Aut}_k(A_n(k))\cong M\rtimes\operatorname{GL}(V)\), with \(M\) a vector group. Every automorphism is uniquely \(u_C\ell_L\). Its square equals \(u_{C+\rho(L)C}\ell_{L^2}\), whence
\[
(u_C\ell_L)^2=1\ \Longleftrightarrow\ L^2=I\ \text{and}\ (I+\rho(L))C=0.
\tag{1}
\]
Moreover conjugation by \(u_D\) changes \(C\) by \((I-\rho(L))D\). Consequently, the conjugacy-orbit set within a fixed fiber is exactly
\[
\ker(I+\rho(L))\big/\operatorname{im}(I-\rho(L)).
\tag{2}
\]
For \(L^2=I\), the image in (2) is contained in the kernel, as required.

**2. Odd characteristic.** Since \(2\ne0\), each square-one \(L\) diagonalizes: \(V=V_+\oplus V_-\), with dimensions \(u=n-v\), \(v\). The \(\pm1\)-eigenspaces of \(L\otimes L\) have dimensions \(u^2+v^2\) and \(2uv\). Hence the \((-1)\)-eigenspace of \(\rho(L)\) on \(\operatorname{Hom}(V,V\otimes V)\) has dimension
\[
u(2uv)+v(u^2+v^2)=3u^2v+v^3.
\]
Equation (1) allows exactly \(q^{3u^2v+v^3}\) quadratic maps. There are \({n\brack v}_q\) choices of \(V_-\) and \(q^{uv}\) complementary choices for \(V_+\), giving the first summation. Since \(I-\rho(L)\) acts by \(2\) on the negative eigenspace, its image is all of \(\ker(I+\rho(L))\). Formula (2) has precisely one orbit, including the representative \(C=0\).

**3. Characteristic two.** Write \(L=I+N\), with \(N^2=0\) and \(r=\operatorname{rank}N\), so \(0\le r\le\lfloor n/2\rfloor\). Choose \(\operatorname{im}N\) (\({n\brack r}_q\) choices), then \(\ker N\) containing it (\({n-r\brack r}_q\) choices), then the induced isomorphism \(V/\ker N\to\operatorname{im}N\) (\(|\mathrm{GL}_r(k)|\) choices). These classify every \(N\) once.

Regard \(V\) as a representation of the cyclic group \(C_2\) generated by \(L\). The Jordan decomposition says
\[
V\cong P^{\oplus r}\oplus k^{\oplus s},\qquad s=n-2r,
\]
where \(P=k[C_2]\) is the two-dimensional regular module and \(k\) is the one-dimensional trivial module. The dual of either indecomposable is isomorphic to itself. The action \(\rho(L)\) on \(M\) is the diagonal tensor action on \(V\otimes V\otimes V^*\). Tensoring a regular module with any \(C_2\)-module under the diagonal action is free: the explicit change of variables \(h\otimes w\mapsto h\otimes h^{-1}w\), for \(h\in C_2\), transforms the diagonal action to the regular action on the first factor. Consequently all triple tensor summands involving at least one copy of \(P\) are regular. The unique non-free contribution comes from three trivial factors, of dimension \(s^3\). Since \(\dim M=n^3\), as a \(C_2\)-module
\[
M\cong P^{\oplus F}\oplus k^{\oplus s^3},\quad F=(n^3-s^3)/2.
\tag{3}
\]
On each \(P\), the map \(I+\rho(L)=I-\rho(L)\) has rank one and one-dimensional kernel; on each trivial summand it is zero. Equations (1)--(3) therefore give
\[
\dim\ker(I+\rho(L))=F+s^3=(n^3+s^3)/2,
\]
\[
\dim\operatorname{im}(I-\rho(L))=F,
\quad \dim \bigl(\ker(I+\rho(L))/\operatorname{im}(I-\rho(L))\bigr)=s^3.
\]
This establishes both the second summation and its quadratic-conjugacy orbit refinement. The proof includes \(r=0\), where \(L=I\), \(M\) is entirely trivial, and every quadratic shear squares to the identity. No divisibility or boundary cases are excluded.

## Verification

The accompanying `artifacts/verify.py` directly composes every pair of generator images for \(n=2\) over \(\mathbb F_2\) and \(\mathbb F_3\); these smaller cases test the formulas outside their claimed range. Counts including identity are respectively \(304\) and \(7534\). Independently of the representation-module argument, the program constructs the coefficient matrix of \((I+\rho(L))C=0\), row-reduces over the ground field, and enumerates every square-one \(L\) in \(\operatorname{GL}_3(\mathbb F_2)\) and \(\operatorname{GL}_3(\mathbb F_3)\). The resulting complete counts are respectively \(134561792\) and \(7626343628152\). The latter uses Gaussian elimination for each linear part, not exhaustive traversal of all quadratic maps. The same rank test runs over \(\mathbb F_4\) for \(n=2\), yielding \(69376\). Replaying the included script prints `VERIFY_OK` and `VERIFY_GF4_OK`. Finite tests do not establish the arbitrary-\(n\) formulas, which follow from the proof.

## Relationship to prior work

The structure of automorphisms of free and relatively free associative algebras and the induced tensor action are classical subjects; these are ingredients and not claimed to be new. Drensky and Gupta (2004) study invariant subalgebras under unipotent transformations of relatively free algebras in characteristic zero, including quotients by invariant ideals. Their results concern constants and generators, not numbers of involutive automorphisms or the characteristic-two quadratic-conjugacy obstruction of the stated truncated tensor algebras. Dangovski, Drensky, and Findik (2013) similarly study characteristic-zero Weitzenböck derivation invariants in free metabelian associative algebras. Drensky and Yu (2007) survey automorphisms fixing a generator of free rank-three associative algebras, rather than involutions in the finite quotient defined here.

The published finite-field tensor fixed-space calculation titled *The dimension-two fixed-tensor distribution over every finite field* enumerates eigenvalue-one eigenspaces of \(L^T\otimes L^T\otimes L^{-1}\) for \(2\times2\) matrices in counting variable bilinear products; its rank-two calculation overlaps a linear-algebra technique in the present theorem. It neither asserts the dimension-at-least-three involution census nor computes the conjugacy obstruction in the quadratic automorphism kernel. Similarly, the published result *Automorphisms of truncated coordinate-cross algebras over arbitrary fields* analyzes a quotient imposing vanishing cross-products: it does not determine the automorphism involutions of the full truncated tensor algebra. Classical group cohomology explains the quotient in (2); the calculated \(s^3\) dimension and exact rank-stratified frequencies in this particular algebra family are the claim.

## Limitations

The classification is for square-one automorphisms, including the identity, rather than all finite-order automorphisms; it gives conjugacy only under the quadratic-kernel subgroup for a fixed linear part, not under the full automorphism group. The formula uses the special tensor cutoff three; the normal nonlinear subgroup ceases to be additive at higher cutoffs. It does not classify involutions of the untruncated free algebra. A stronger unlocated finite-group cohomological or truncated-automorphism classification could imply these results; no literature search is a uniqueness certificate.

## References

1. V. Drensky and C. K. Gupta, *Constants of Weitzenböck derivations and invariants of unipotent transformations acting on relatively free algebras*, arXiv:math/0412399v1 (first public 20 December 2004), `https://arxiv.org/html/math/0412399v1`, *Journal of Algebra* 292 (2005), 393–428, DOI `10.1016/j.jalgebra.2005.07.004`.
2. R. Dangovski, V. Drensky, and S. Findik, *Weitzenböck derivations of free metabelian associative algebras*, arXiv:1308.6596v1 (29 August 2013), revised text `https://arxiv.org/html/1308.6596v2`.
3. V. Drensky and J.-T. Yu, *Coordinates and automorphisms of polynomial and free associative algebras of rank three*, *Frontiers of Mathematics in China* 2 (2007), 13–46, DOI `10.1007/s11464-007-0002-9`.
4. N. D. Verhulst, *Counting finite-dimensional algebras over finite fields*, arXiv:1909.03717 (2019), `https://arxiv.org/html/1909.03717v2`, for the distinct fixed-tensor problem of classifying variable algebra products.
5. *The dimension-two fixed-tensor distribution over every finite field*, published mathematical record `2026/10/4/SCOPE-the-dimension-two-fixed-tensor-distribution-over-every-finite-fi--568adf24efd6`, text at `https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-dimension-two-fixed-tensor-distribution-over-every-finite-fi--568adf24efd6`.
6. *Automorphisms of truncated coordinate-cross algebras over arbitrary fields*, published mathematical record `2026/10/4/SCOPE-automorphisms-of-truncated-coordinate-cross-algebras-over-arbitr--625ba30274cb`.
