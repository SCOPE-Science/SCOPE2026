# Automorphism schemes of mixed-height truncated polynomial algebras in characteristic \(p\)

## Finding

Let \(k\) be a field of characteristic \(p>0\), let \(e_1,\ldots,e_r\) be positive integers, and define
\[
A=k[x_1,\ldots,x_r]/(x_i^{p^{e_i}}:1\le i\le r),\qquad N=\dim_k A=\prod_{j=1}^r p^{e_j}.
\]
For each height \(h\), write \(m_h=|\{i:e_i=h\}|\), and put
\[
c_i=p^{\sum_{j:e_j>e_i}(e_j-e_i)}.
\]
As a scheme, not generally as a group scheme, the full automorphism scheme has the coordinate decomposition
\[
\operatorname{Aut}_k(A)\cong
\left(\prod_{i=1}^r\alpha_{p^{e_i}}^{\,c_i}\right)
\times\left(\prod_{h:m_h>0}\operatorname{GL}_{m_h}\right)
\times\mathbb A_k^{\,rN-\sum_i c_i-\sum_h m_h^2},
\]
where \(\alpha_{p^e}=\operatorname{Spec}k[z]/(z^{p^e})\). Therefore
\[
\dim\operatorname{Aut}_k(A)=rN-\sum_i c_i,\qquad
\dim_k\operatorname{Der}_k(A)=\dim T_1\operatorname{Aut}_k(A)=rN.
\]
The exact non-smoothness defect is \(\sum_i c_i\), which depends on the full exponent-height profile, not only on the number of generators.

## Assumptions and scope

The field has positive characteristic \(p\); every truncation exponent is a positive power \(p^{e_i}\). The algebra is commutative, unital, finite-dimensional, and local. The displayed product is an isomorphism of schemes only; no direct-product assertion about the group law is made. General truncation exponents not equal to powers of \(p\) are outside the claim.

## Proof

Use the monomial basis \(x^\alpha=x_1^{\alpha_1}\cdots x_r^{\alpha_r}\), with \(0\le\alpha_j<p^{e_j}\). A homomorphism over a commutative \(k\)-algebra \(R\) is specified by \(f_i=\sum_\alpha a_{i,\alpha}x^\alpha\), subject to \(f_i^{p^{e_i}}=0\). Frobenius additivity gives
\[
f_i^{p^{e_i}}=\sum_\alpha a_{i,\alpha}^{p^{e_i}}x^{p^{e_i}\alpha}.
\]
The monomial indexed by \(\alpha\) survives precisely when \(\alpha_j=0\) for every \(j\) with \(e_j\le e_i\), and \(0\le\alpha_j<p^{e_j-e_i}\) for every \(j\) with \(e_j>e_i\). These surviving monomials are distinct. Hence the relation is equivalent to the independent equations \(a_{i,\alpha}^{p^{e_i}}=0\) for exactly \(c_i\) coefficient coordinates, where
\[
|\{\alpha:\text{the monomial survives}\}|=\prod_{j:e_j>e_i}p^{e_j-e_i}=c_i.
\]
All other coefficient coordinates are unrestricted.

The constrained coordinates form a nilpotent ideal in the coefficient scheme. After reducing by that ideal, the linear coefficient matrix of \((f_i)\), ordered by increasing height, is block triangular, with diagonal block of size \(m_h\) at each height \(h\). An endomorphism of this finite local algebra over a residue field is invertible exactly when its induced map on the maximal ideal modulo its square is invertible. Thus the automorphism locus is obtained by inverting the determinants of these diagonal blocks. Lifting across the nilpotent coefficient ideal preserves invertibility, so these are also the exact scheme-theoretic open conditions. The coordinate scheme is consequently the product of the indicated \(\alpha_{p^{e_i}}\) factors, the diagonal-block general linear groups, and an affine space for the remaining free coefficients. Counting free coordinates gives dimension \(rN-\sum_i c_i\).

For any derivation \(D\), each defining relation satisfies
\[
D(x_i^{p^{e_i}})=p^{e_i}x_i^{p^{e_i}-1}D(x_i)=0,
\]
so the values \(D(x_i)\in A\) are arbitrary and \(\dim_k\operatorname{Der}_k(A)=rN\). Equivalently, every power-equation defining a constrained coefficient has zero differential in characteristic \(p\), so the tangent space of the automorphism scheme at the identity has dimension \(rN\). Since every \(c_i\ge1\), this exceeds the scheme dimension by exactly \(\sum_i c_i>0\). This proves the stated decomposition and non-smoothness.

## Verification

The coefficient equations were derived for arbitrary \(R\), not only for field-valued points. The open automorphism condition was checked after reduction to residue fields and then lifted across the nilpotent coefficient ideal. The standalone finite sanity check `verify_small_case.py` enumerates \(A=\mathbb F_2[x,y]/(x^2,y^4)\): it finds \(64\) admissible images of \(x\), \(128\) admissible images of \(y\), and exactly \(2048=2^{11}\) automorphisms, agreeing with the formula \(N=8\), \((c_1,c_2)=(2,1)\), and scheme dimension \(13\). This finite check is corroborative only; the general result is proved by the coefficient argument above.

## Relationship to prior work

Chang, Shu, and Yao study automorphisms of truncated polynomial algebras in characteristic \(p\) with a common truncation height \(p^s\), and give a field-valued automorphism criterion. Their inspected statement does not classify the full automorphism scheme for mixed heights. Tziolas gives the basic non-smooth example \(\operatorname{Aut}(k[x]/(x^2))\cong\alpha_2\rtimes\mathbb G_m\) and identifies the Lie algebra of an automorphism group scheme with derivations, but does not give the mixed-height coefficient formula. The present result extends the common-height setting to arbitrary positive height vectors and computes the exact scheme dimension and tangent excess. The one-variable case is included as a special case and is not claimed as a separate new result.

## Limitations

The formula relies on every defining exponent being a power of the characteristic. It does not classify the group law up to a semidirect-product presentation, treat arbitrary exponents, or establish a classification of all automorphism schemes of finite local algebras. Literature searches and inspected texts support the comparison but cannot prove absolute novelty; independent audit has not been performed.

## References

- H. Chang, B. Shu, and Y.-F. Yao, “Inverse limits of automorphisms of truncated polynomials and applications related to Jacobian conjecture,” arXiv:2401.11072 (first public version: 2024-01-20), especially §§2–3 and Lemma 3.1.
- N. Tziolas, “Topics in group schemes and surfaces in positive characteristic,” *Annali dell’Università di Ferrara* 70 (2024), 891–954, DOI 10.1007/s11565-024-00514-8, Example 3.11 and Proposition 3.19.
