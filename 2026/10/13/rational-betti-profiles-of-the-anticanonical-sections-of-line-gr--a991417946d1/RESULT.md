# Rational Betti profiles of the anticanonical sections of line-Grassmannian Fano varieties

## Finding
Let \(N\ge6\) be any **even integer**, and over \(\mathbb C\) let \(F_N\subset\operatorname{Gr}(2,N)\) be a general complete intersection of \(N-1\) Plücker hyperplanes. The smooth index-one Fano variety \(F_N\) has complex dimension \(N-3\). Its general anticanonical divisor \(X_N\in|-K_{F_N}|\) is the smooth intersection of \(N\) Plücker hyperplanes, with trivial canonical bundle and dimension \(d=N-4\).

The **entire rational Betti polynomial** \(B_N(t)=\sum_{j=0}^{2d}\dim_{\mathbb Q}H^j(X_N,\mathbb Q)t^j\) is determined for all such \(N\) by the following explicit coefficient formula. Let \([P(x,y)]_d\) mean the homogeneous part of total degree \(d\) of the formal Taylor expansion at \((0,0)\), and set
\[
C_N(x,y)=\left[\frac{(1+x)^N(1+y)^N}{(1-(x-y)^2)(1+x+y)^N}\right]_d,\quad
E_N=[x^{N-1}y^{N-2}](x-y)(x+y)^N C_N(x,y).
\]
For each integer \(s\) with \(0\le 2s<d\), put \(a_s=\lfloor s/2\rfloor+1\). Then
\[
\boxed{\quad B_N(t)=\sum_{0\le 2s<d}a_s(t^{2s}+t^{2d-2s})+
\left(E_N-2\sum_{0\le2s<d}a_s\right)t^d.\quad}
\]
In particular \(\chi_{\mathrm{top}}(X_N)=E_N\). The primitive middle rational Betti rank, relative to the image of \(H^d(\operatorname{Gr}(2,N),\mathbb Q)\), is
\[
E_N-2\sum_{0\le2s<d}a_s-\left(\lfloor d/4\rfloor+1\right).
\]
For the first three non-surface cases, the exact topological Euler characteristics are \(E_8=636\), \(E_{10}=24920\), and \(E_{12}=1082256\). In the naturally first six-dimensional Calabi–Yau case \(N=10\),
\[
\boxed{B_{10}(t)=1+t^2+2t^4+24912t^6+2t^8+t^{10}+t^{12},\quad b_6^{\mathrm{prim}}=24910.}
\]
The surface case \(N=6\) supplies the K3 consistency check \(B_6(t)=1+22t^2+t^4\) and \(E_6=24\).

## Assumptions and scope
All varieties are over the complex numbers. A general collection of \(N\) Plücker hyperplanes is chosen so that each successive intersection is smooth; Bertini supplies such a choice. The ambient Grassmannian has \(\dim_{\mathbb C}\operatorname{Gr}(2,N)=2N-4\) and \(K_{\operatorname{Gr}(2,N)}\cong\mathcal O(-N)\). The word *Betti* always means the dimensions of singular cohomology with **rational** coefficients; no torsion statement or full Hodge diamond is claimed. The restriction to even \(N\) is the natural odd-projective-dimension branch of the 2026 index-one Fano constructions. The displayed formulas are **uniform**, not finite-experimental conjectures.

## Proof
Write \(G=\operatorname{Gr}(2,N)\), let \(S\) and \(Q\) be its universal subbundle and quotient bundle, and write \(x,y\) for formal Chern roots of \(S^\vee\). The Plücker hyperplane class is \(H=x+y\). The universal sequence and \(T_G=S^\vee\otimes Q\) yield, in complex \(K\)-theory, \([T_G]=N[S^\vee]-[S^\vee\otimes S]\). Since the formal Chern roots of \(S^\vee\otimes S\) are \(0,0,x-y,y-x\), we obtain the total Chern class
\[
c(T_G)=\frac{(1+x)^N(1+y)^N}{1-(x-y)^2}.
\]
The tangent-normal exact sequence for the complete intersection gives \(c(T_{X_N})=i^*c(T_G)(1+H)^{-N}\). Hence \(c_d(T_{X_N})\) is the pullback of the degree-\(d\) symmetric polynomial \(C_N(x,y)\). Gauss–Bonnet and the projection formula give
\[
\chi_{\mathrm{top}}(X_N)=\int_{X_N}c_d(T_{X_N})=\int_G H^N C_N(x,y).
\]
The two-row Schur basis proves the integration identity for any symmetric homogeneous polynomial \(f(x,y)\) of degree \(2N-4\):
\[
\int_G f(x,y)=[x^{N-1}y^{N-2}](x-y)f(x,y).
\]
Indeed, \((x-y)s_{(a,b)}(x,y)=x^{a+1}y^b-x^by^{a+1}\), and the only two-row Schubert class in top codimension is \(s_{(N-2,N-2)}\), whose integral is \(1\). This proves the coefficient expression for \(E_N\) for every even \(N\ge6\), without interpolation.

For each \(j<d\), successive weak Lefschetz isomorphisms identify \(H^j(X_N,\mathbb Q)\) with \(H^j(G,\mathbb Q)\). Cellular Schubert decomposition implies the odd groups of \(G\) vanish, and its even-degree Betti number in degree \(2s<d\) counts partitions of \(s\) into at most two parts, namely \(a_s=\lfloor s/2\rfloor+1\). (The rectangle width restriction is automatic because \(s<d/2<N-2\).) Poincaré duality supplies the groups above the middle. Since \(d\) is even, the Euler characteristic is the sum of all rational Betti numbers; solving for the sole undetermined rank \(b_d\) gives exactly \(B_N(t)\) above. The ambient middle group has dimension \(\lfloor d/4\rfloor+1\), and hard Lefschetz ensures the ambient class image embeds in middle cohomology; subtracting yields the primitive rank. The tangent-normal sequence and Schubert integration account for every displayed integer.

For the explicit sixfold, the degree-six polynomial is
\[
C_{10}=x^6+24x^5y+195x^4y^2+380x^3y^3+195x^2y^4+24xy^5+y^6.
\]
The coefficient expression evaluates to \(E_{10}=24920\), and the ambient Betti ranks below the middle are \(1,1,2\). Thus \(b_6=24920-2(1+1+2)=24912\) and \(b_6^{\mathrm{prim}}=24912-2=24910\). Similarly, \(E_6=24\), \(E_8=636\), and \(E_{12}=1082256\).

## Verification
Run the complete standard-library Python checker (`check.py`) with Python 3. It independently implements both the Schur-alternant coefficient integration and torus-fixed-point localization at the distinct weights \(0,1,\dots,N-1\); it verifies agreement for \(N=6,8,10,12\), the top Schubert-class normalization, the Betti-polynomial coefficients, and the stated primitive ranks. Expected final line: \(`GRASSMANNIAN_CY_BETTI_EXACT_OK`\). These finite computations verify the examples, **not** the infinite theorem; the all-\(N\) proof is the Chern, Schubert and Lefschetz argument above.

## Relationship to prior work
Bolognesi–Ciliberto–Verra (September 2026) study the index-one Fano \((N-1)\)-hyperplane sections and their Pfaffian birational models. Taking the anticanonical hyperplane is a natural boundary operation, but the exact rational Betti profile of the resulting \(N\)-hyperplane section is a different invariant from their birational results. Benedetti's earlier classification includes the \(\operatorname{Gr}(2,8)\) example defined by eight Plücker hyperplanes and gives \(\chi(\mathcal O)=2\); that arithmetic/holomorphic Euler characteristic is distinct from the topological Euler characteristic \(636\). The separate later 2026 study of these Calabi–Yau line-Grassmannian sections develops Pfaffian and focal geometry rather than the uniform Betti evaluation displayed here. The use of universal characteristic classes, Schubert integration and weak Lefschetz is classical; the claim is their **specific uniform evaluation for this motivated family**, not any new general formula for Grassmannians.

## Limitations
No claim is made about integral cohomology torsion, Hodge decomposition within the middle degree, a new geometric correspondence, motivic decomposition, or classification of non-general sections. The 2026 September initiating paper's full text was not accessible in the present comparison, leaving some risk of an implicit equivalent calculation there. Older characteristic-class machinery can derive this profile, so its originality is the explicit family-wide evaluated statement, not the general method. No independent mathematical audit has been performed.

## References
1. M. Bolognesi, C. Ciliberto, A. Verra, *On Fano varieties of index one that are linear sections of Grassmannians of lines*, arXiv:2609.21503v1 (first public 2026-09-18).
2. V. Benedetti, *Manifolds of low dimension with trivial canonical bundle in Grassmannians*, arXiv:1609.02695v3 (2017), especially §3, Appendix A and Table 2.
3. M. Bolognesi, C. Ciliberto, A. Verra, *On Calabi–Yau varieties that are linear sections of Grassmannians of lines*, arXiv:2610.11925v1 (2026), geometric context and a literature comparator.
4. Standard Schubert-calculus integration on \(\operatorname{Gr}(2,N)\), and weak Lefschetz, Poincaré duality, adjunction and Gauss–Bonnet as applied explicitly in the proof above.
