# ID-derivation deficiency and semicompleteness of almost-abelian Lie algebras
## Finding
Let \(K\) be a field, \(V\) a finite-dimensional vector space of dimension \(n\), and \(T\in\operatorname{End}_K(V)\). The almost-abelian Lie algebra \(L_T=Ke\oplus V\) has brackets \([e,v]=Tv\), \([V,V]=0\), and \([e,e]=0\). An **ID derivation** is a derivation \(D\) with \(D(L_T)\subseteq[L_T,L_T]\); the algebra is **semicomplete** when every ID derivation is inner. With \(t\) acting on \(V\) as \(T\), there is, for \(T\ne0\), a natural vector-space isomorphism
\[
\operatorname{IDer}(L_T)/\operatorname{ad}(L_T)
 \cong \operatorname{Hom}_{K[t]}(V,tV)/(K\cdot T).
\]
In particular, define \(\Phi(T)=\dim_K\operatorname{Hom}_{K[t]}(V,tV)\). Then the dimension of outer ID derivations is \(\Phi(T)-1\) if \(T\ne0\), and zero if \(T=0\).

For each monic irreducible polynomial \(f\in K[t]\), list the exponents of the \(f\)-primary elementary divisors as \(\lambda_{f,1},\ldots,\lambda_{f,r_f}\). Omitting empty sums, the exact finite formula is
\[
\Phi(T)=\sum_{f\ne t}(\deg f)\sum_{i,j=1}^{r_f}\min(\lambda_{f,i},\lambda_{f,j})
+\sum_{i,j=1}^{r_t}\min\{\lambda_{t,i},\max(\lambda_{t,j}-1,0)\}.
\]
Consequently the **complete semicompleteness criterion** is
\[
\boxed{L_T\text{ semicomplete}\ \Longleftrightarrow\ T=0\text{ or }\bigl(\operatorname{rank}T=1\text{ and }(T^2\ne0\text{ or }n=2)\bigr).}
\]
No algebraic-closure or characteristic restriction is necessary. If \(T\ne0\), the inner derivation dimension is \(\operatorname{rank}T+1\). Thus \(\dim\operatorname{IDer}(L_T)=\operatorname{rank}T+\Phi(T)\).

## Assumptions and scope
All spaces and maps are finite-dimensional over an arbitrary field \(K\). The Lie bracket is alternating also in characteristic two. The term **ID derivation** means a *derivation whose whole image is contained in the derived ideal*, not an *almost-inner derivation* satisfying pointwise \(D(x)\in[L_T,x]\); these concepts are different. The index \(t\) in the elementary-divisor formula denotes the degree-one zero-eigenvalue polynomial, not an arbitrary linear factor.

## Proof
First \([L_T,L_T]=W=TV\). An ID derivation necessarily maps \(e\) to some \(c\in W\) and maps \(V\) by some \(K\)-linear map \(E:V\to W\). The derivation identity on \([e,v]=Tv\) is precisely \(ET=TE\), and all other bracket pairs impose no further condition. Conversely, any \((c,E)\in W\oplus\operatorname{Hom}_{K[t]}(V,W)\) defines a derivation, since \(D([e,v])=ETv=TEv=[e,D(v)]\) and \([D(e),v]=0\). Consequently
\[
\operatorname{IDer}(L_T)\cong W\oplus\operatorname{Hom}_{K[t]}(V,W).
\]
For \(a\in K\) and \(v\in V\), the inner derivation \(\operatorname{ad}(ae+v)\) has \(D(e)=-Tv\) and \(D|_V=aT\). Its image in the displayed direct sum is \(W\oplus KT\) when \(T\ne0\), so the quotient and dimension formula follow. When \(T=0\), \(W=0\) and both ID and inner derivations vanish.

For the elementary-divisor count, regard \(V\) as a torsion \(K[t]\)-module. Its primary pieces are \(K[t]/(f^a)\). On each primary piece with \(f\ne t\), multiplication by \(t\) is invertible, so that entire summand remains in \(tV\). On a \(t\)-primary piece of length \(b\), its image under \(t\) is a module of length \(\max(b-1,0)\). The elementary module identity
\[
\dim_K\operatorname{Hom}_{K[t]}(K[t]/(f^a),K[t]/(f^b))
 =(\deg f)\min(a,b)
\]
then gives the asserted two sums. Homomorphisms between distinct primary factors vanish, and every summand is counted with source index \(i\) and target index \(j\).

It remains to classify when \(\operatorname{Hom}_{K[t]}(V,tV)=KT\). Suppose first \(T\ne0\). If \(T^2\notin KT\), then \(T\) and \(T^2\) are two independent commuting maps into \(tV\), so semicompleteness fails. Otherwise \(T^2=\lambda T\) for some \(\lambda\in K\). If \(\lambda\ne0\), then \(V=\ker T\oplus\operatorname{im}T\) and \(T\) restricts to \(\lambda I\) on \(\operatorname{im}T\). Arbitrary linear endomorphisms of \(\operatorname{im}T\), extended by zero on \(\ker T\), form \(\operatorname{Hom}_{K[t]}(V,tV)\). Hence \(\Phi(T)=(\operatorname{rank}T)^2\), equal to one exactly for rank one.

If \(\lambda=0\), then \(T^2=0\), so \(W=\operatorname{im}T\subseteq\ker T\). Every linear map \(V/W\to W\) produces a commuting map \(E:V\to W\), and these are all such maps, because \(TE=0\) and \(ET=0\). Therefore \(\Phi(T)=r(n-r)\), where \(r=\operatorname{rank}T\) and \(n\ge2r\). For positive \(r\), equality \(r(n-r)=1\) holds precisely when \(r=1,n=2\). Combining these cases proves the classification, including fields of characteristic two.

## Verification
The standalone Python 3 program `verify.py` independently computes the dimension of the linear solution space \(\{E:ET=TE,\ \operatorname{im}E\subseteq TV\}\) by row reduction, using a basis for the left annihilator of \(TV\). It exhaustively checks the criterion for every binary matrix of sizes \(1,2,3\) (respectively \(2,16,512\) matrices), and evaluates additional Jordan, diagonal, and irreducible-block examples over characteristics two and three. Execution prints `ALL_BINARY_ENDOMORPHISMS_DIMENSIONS_AND_SEMICOMPLETE_BOUNDARY_OK`, `PRIMARY_COMPONENT_DIMENSION_EXAMPLES_OK`, and `VERIFY_OK`. This is finite corroboration only; the proof above establishes the arbitrary-field result.

## Relationship to prior work
Malangpoo, Pongprasert, and Siripitakchai (2026) motivate the subject with semicomplete Leibniz algebras, structural properties, and bounded-dimensional classifications, but their publicly accessible early-access abstract does not state the all-dimensional almost-abelian ID-derivation quotient or the primary-decomposition formula. Boyle (2018), Chapter 6, gives the definitions of ID derivations and semicompleteness and general preliminary properties. Alemi, Saeedi, and Srivastava (2019) discuss derivation algebras of direct sums, but not the displayed all-dimensional elementary-divisor computation. Previously known classifications of *almost-inner* derivations do not imply the result for the weaker derived-ideal-image condition. General rational canonical form and Hom computations are standard algebra; their application here supplies the explicit deficiency invariant and the semicompleteness boundary.

## Limitations
The theorem concerns the almost-abelian family \(L_T\), not every finite-dimensional Lie or Leibniz algebra. The exact module-theoretic dimension formula follows from classical linear algebra, and the present work does not claim that elementary-divisor or Hom theory is new. The 2026 motivating paper's full text was not accessible in the present source inspection; prior equivalent formulations could exist under other terminology. Independent scholarly validation and historical priority checks remain unperformed.

## References
1. C. Malangpoo, S. Pongprasert, and N. Siripitakchai, “Semicomplete Leibniz Algebras,” *Mathematics* **14** (2026), 3222, doi:10.3390/math14173222 (published 2026-09-06; publisher abstract accessed).
2. K. J. Boyle, *On Derivations of Leibniz Algebras*, PhD dissertation, North Carolina State University (2018), Chapter 6 (institutional repository full-text PDF).
3. M. R. Alemi, F. Saeedi, and H. M. Srivastava, “Derivation algebra of direct sum of lie algebras,” *Cogent Mathematics & Statistics* (2019), doi:10.1080/25742558.2019.1624244.
