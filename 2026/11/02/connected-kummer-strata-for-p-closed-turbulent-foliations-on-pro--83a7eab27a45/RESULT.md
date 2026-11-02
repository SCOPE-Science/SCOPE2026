# Connected Kummer strata for \(p\)-closed turbulent foliations on products of ordinary elliptic curves

## Finding
Let \(k\) be algebraically closed of characteristic \(p\ge3\). Let \(E\) and \(Y\) be ordinary elliptic curves over \(k\), and fix invariant nonzero differentials \(\omega_E,\omega_Y\), normalized so that Cartier fixes each. For \(d\ge2\), let \(U_d\) denote the configuration variety of reduced effective divisors of degree \(d\) on \(Y\). The logarithmic-derivative locus of turbulent foliations on \(E\times Y\) with a prescribed pole divisor in \(U_d\) is classified on geometric points by the finite étale Kummer covers constructed below. More specifically, connected covering strata are indexed by multiplicities \(m_1,\ldots,m_{p-1}\) satisfying
\[
\sum_{j=1}^{p-1}m_j=d,\qquad \sum_{j=1}^{p-1}j m_j\equiv0\pmod p.
\]
The connected stratum corresponding to a multiplicity vector has degree \(p d! /\prod_jm_j!\) above \(U_d\). Thus the number of connected strata is
\[
C_{p,d}=\frac1p\left[\binom{d+p-2}{p-2}+(p-1)(\mathbf1_{p\mid d}-\mathbf1_{p\mid(d-1)})\right],
\]
and the number of distinct normalized logarithmic-derivative \(p\)-closed foliations over *every* reduced degree-\(d\) divisor is
\[
N_{p,d}=(p-1)^d+(p-1)(-1)^d.
\]
Here the connected strata refer to the **natural finite étale Kummer parameter cover**, not to any unverified scheme-theoretic identification with the possibly nonreduced full foliation moduli locus.

## Assumptions and scope
A turbulent foliation here is specified by a differential \(\omega_E+f\omega_Y\) with \(f\in k(Y)\) nonconstant, considered with the fixed normalization on the \(E\)-component. We consider only foliations with \(p\)-closedness characterized by \(\mathscr C_Y(f\omega_Y)=f\omega_Y\); this is the ordinary-elliptic case of Andreatta--Goren, Proposition 1.8.3. Its Cartier criterion, via the logarithmic differential theorem, gives \(f\omega_Y=d\log g\) for \(g\in k(Y)^*\). The polar divisor is reduced and each pole is simple. We do not classify nonreduced pole divisors, additive- or inseparable-case foliations, or nilpotent structure on a coarse foliation moduli scheme. The natural Kummer parameter covers are finite étale over the reduced-divisor configuration space.

## Proof
**1. Residue vectors and logarithmic divisors.** A logarithmic differential \(d\log g\) has residues in \(\mathbb F_p\) (the orders in \(\mathbb Z\) reduced modulo \(p\)). Thus, if its poles are precisely the distinct points \(P_1,\ldots,P_d\), the residues \(r_i\in\mathbb F_p^*\) satisfy \(\sum_i r_i=0\) by the residue theorem. Conversely, choose integers \(a_i\equiv r_i\pmod p\) with \(\sum_i a_i=0\). Put \(\Delta=\sum_i a_i[P_i]\in\operatorname{Div}^0Y\) and \(b=[\Delta]\in\operatorname{Pic}^0(Y)=Y\), using a fixed origin. For any degree-zero divisor \(Z\) with class \(e\) satisfying \([p]e=b\), the divisor \(\Delta-pZ\) is principal. A rational function \(g\) with \(\operatorname{div}g=\Delta-pZ\) has precisely the required logarithmic residues. Changing \(Z\) within its linear equivalence class multiplies \(g\) by a \(p\)-th power and leaves \(d\log g\) unchanged. Conversely, from \(d\log g\) the divisor \(\operatorname{div}g-\Delta\) is divisible by \(p\), and its divided class determines such \(e\). Two logarithmic derivatives with the same class \(e\) differ by a logarithmic derivative of a rational function with divisor divisible by \(p\) and trivial divided divisor class; their quotient is a \(p\)-th power, so the derivatives coincide. Therefore logarithmic differentials with ordered residue vector correspond bijectively to solutions of \([p]e=b\) in \(Y(k)\). The choice of integer lifts does not affect the residue-class partition or geometric cover up to canonical translation.

**2. Finite étale Kummer parameter cover.** Over the ordered configuration variety \(B_d=Y^d\setminus\bigcup_{i<j}\{P_i=P_j\}\), define the weighted Abel map
\[
\Phi_{\mathbf a}(P_1,\ldots,P_d)=\sum_i[a_i]P_i\in Y.
\]
The ordinary elliptic curve has \([p]=V\circ F\), where the relative Frobenius \(F:Y\to Y^{(p)}\) is radicial and bijective on geometric points, while Verschiebung \(V:Y^{(p)}\to Y\) is a connected separable isogeny of degree \(p\), hence finite étale with cyclic deck group of order \(p\). Set
\[
W_{\mathbf r}=B_d\times_{\Phi_{\mathbf a},Y,V}Y^{(p)}.
\]
This is finite étale of degree \(p\), with geometric points identified through \(F\) with the p-division classes above. It is connected: fix \(P_2,\ldots,P_d\) at pairwise distinct values and vary \(P_1\) on the remaining punctured elliptic curve. The restriction of \(\Phi_{\mathbf a}\) is \([a_1]P_1+c\). Because \(p\nmid a_1\), pullback of the cyclic degree-\(p\) Verschiebung torsor along \([a_1]\) remains a connected degree-\(p\) cover: the induced homomorphism on the cyclic quotient of the étale fundamental group is multiplication by a nonzero residue modulo \(p\). Deleting finitely many points preserves connectedness. Any connected component of a finite étale cover of connected \(B_d\) must surject onto \(B_d\); therefore the connected restricted cover forces the whole \(W_{\mathbf r}\) to be connected.

**3. Unordered strata and covering degrees.** The symmetric group \(S_d\) freely permutes the positions of the ordered divisor and simultaneously permutes the residues. For each fixed multiset \(\{r_1,\ldots,r_d\}\), its orbit contains \(d!/\prod_jm_j!\) distinct residue assignments. Their connected labeled covers are permuted transitively by \(S_d\). Hence their quotient over \(U_d=B_d/S_d\) is connected, finite étale of degree \(p d!/\prod_jm_j!\). Every residue multiset with nonzero entries and sum zero gives one component, and distinct multisets cannot merge because residue multiplicities are locally constant.

**4. Exact component and point counts.** Character orthogonality on \(\mathbb F_p\) shows that the number of ordered nonzero residue vectors with sum zero is
\[
\frac1p\bigl((p-1)^d+(p-1)(-1)^d\bigr).
\]
Multiplying by the p geometric points in every Verschiebung fiber yields \(N_{p,d}\). For multisets, the ordinary generating function for zero-sum multiplicities is
\[
\frac1p\left((1-t)^{-(p-1)}+(p-1)\frac{1-t}{1-t^p}\right).
\]
Indeed, the nontrivial character term is \(\prod_{j=1}^{p-1}(1-\zeta^jt)^{-1}=(1-t)/(1-t^p)\). Extracting the coefficient of \(t^d\) gives \(C_{p,d}\). This exhausts all strata and proves the degree and total-fiber formulas.

## Verification
Run `python3 check_foliation_residues.py` with standard Python 3. The script enumerates every nonzero residue vector and multiplicity partition for thirteen test instances with \(p\in\{3,5,7\}\), compares the root-of-unity formula and the sum of covering degrees, and prints `VERIFY_OK`. The finite checker tests only combinatorial consequences; the isogeny, connectedness, and logarithmic correspondence are established by the preceding general proof, not by finite experiments.

## Relationship to prior work
Andreatta--Goren (2026), Proposition 1.8.3, establishes the Cartier/logarithmic criterion for \(p\)-closed turbulent foliations when the elliptic factor is ordinary; Theorem 1.9.4 gives existence conditions for reduced poles, and Section 2 constructs the surrounding moduli loci. These substantive results are used as inputs and are **not** claimed as discoveries here. What is added is the finite étale Kummer model on geometric points, connectivity of each fixed-residue cover, the decomposition by unordered residue multiplicities, and complete formulas for component counts and covering degrees. The generalized-Jacobian and p-torsion literature may contain equivalent parametrizations; a definitive global priority claim is not made.

## Limitations
The component assertion applies to the constructed finite étale Kummer parameter space. The pointwise identification with normalized foliation data does not assert an isomorphism of moduli schemes or reduced structures; Frobenius is radicial rather than an isomorphism of schemes. The result assumes both elliptic curves ordinary, characteristic at least three, and reduced pole divisors. It does not handle nonordinary curves, arbitrary abelian surfaces, wild multiplicity of poles, or schemes parametrizing non-closed foliations. Historical literature priority and independent mathematical validation are outstanding.

## References
1. F. Andreatta and E. Z. Goren, *Foliations on abelian surfaces in positive characteristic* (2026), arXiv:2610.32975v1, especially Proposition 1.8.3, Theorem 1.9.4 and Section 2. https://arxiv.org/html/2610.32975v1
2. *Logarithmic Hurwitz Spaces in Mixed and Positive Characteristic with Wild Ramification* (2026), arXiv:2602.16434v1, relevant Cartier discussion; different moduli problem. https://arxiv.org/abs/2602.16434
3. Classical Cartier logarithmic-differential criterion and separable--radicial factorization of multiplication by \(p\) on ordinary elliptic curves (standard results used in the proof).
