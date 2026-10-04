# The anticanonical model of the weak-Fano Hessenberg fourfold with \(h=(3,3,4,4)\)
## Finding
Let \(S=\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3,\lambda_4)\) have pairwise distinct complex eigenvalues, and set \(X=\operatorname{Hess}(S,(3,3,4,4))\). Then the anticanonical model of \(X\) is the image of the projection that forgets \(V_3\):
\[
\pi:X\longrightarrow Y=\{(L\subset P)\in\operatorname{Fl}(1,2;4):P\cap SP\ne0\}.
\]
If
\[
Z=\{P\in\operatorname{Gr}(2,4):P\cap SP\ne0\},
\]
then \(Y\to Z\) is a \(\mathbb P^1\)-bundle. In Plücker space \(\mathbb P^5\), \(Z\) is a complete intersection of two quadrics and has exactly six ordinary double points, located at the six \(S\)-invariant coordinate two-planes. Thus \(\operatorname{Sing}(Y)\) is six disjoint projective lines. The map \(\pi\) is a small crepant resolution; its exceptional locus is six disjoint copies of \(\mathbb P^1\times\mathbb P^1\), each mapped to one singular line by a ruling. Finally,
\[
-K_X=\pi^*A,
\]
where \(A\) is the ample weight-\(2\varpi_1+\varpi_2\) line bundle on \(Y\subset\operatorname{Fl}(1,2;4)\). In particular, \(Y\) is the anticanonical model. As a numerical check, \((-K_X)^4=192\).

## Assumptions and scope
The base field is \(\mathbb C\). The matrix \(S\) is regular semisimple, so its eigenvalues are pairwise distinct. The Hessenberg function is exactly \(h=(3,3,4,4)\). Abe--Fujita--Zeng prove that this regular semisimple Hessenberg variety is smooth and weak Fano and compute its anticanonical bundle as the line bundle associated with the Hessenberg weight. The statement here identifies the resulting anticanonical contraction and its singular target.

## Proof
Write a flag as \(L=V_1\subset P=V_2\subset H=V_3\subset\mathbb C^4\). For \(h=(3,3,4,4)\), the defining conditions are \(SL\subset H\) and \(SP\subset H\); the first follows from the second because \(L\subset P\). Hence forgetting \(H\) maps \(X\) to
\[
Y=\{(L\subset P):P\cap SP\ne0\}.
\]
Indeed, a hyperplane \(H\) containing \(P+SP\) exists exactly when \(\dim(P+SP)\le3\), equivalently \(P\cap SP\ne0\).

Let \(p_{12},p_{13},p_{14},p_{23},p_{24},p_{34}\) be Plücker coordinates on \(\operatorname{Gr}(2,4)\). The Grassmannian equation is
\[
G=p_{12}p_{34}-p_{13}p_{24}+p_{14}p_{23}=0.
\]
If \(P=\langle u,v\rangle\), then \(P\cap SP\ne0\) is equivalent to
\[
\det[u,v,Su,Sv]=0.
\]
For
\[
A=(\lambda_1-\lambda_3)(\lambda_2-\lambda_4),\qquad
B=-(\lambda_1-\lambda_2)(\lambda_3-\lambda_4),
\]
the determinant reduces on decomposable bivectors to
\[
Q=A p_{12}p_{34}+B p_{13}p_{24}=0.
\]
Thus \(Z=V(G,Q)\subset\mathbb P^5\). The identities
\[
A\ne0,\qquad B\ne0,\qquad A+B=(\lambda_1-\lambda_4)(\lambda_2-\lambda_3)\ne0
\]
show that the two quadrics are independent and define a codimension-two complete intersection.

Consider the pencil \(Q-tG\). Its three complementary coordinate blocks have coefficients \(A-t\), \(B+t\), and \(-t\). Because \(0\), \(A\), and \(-B\) are distinct, the only singular pencil members occur at those three parameters, each with a two-dimensional kernel. Intersecting each kernel with the base locus gives exactly the two coordinate points in that kernel. Therefore \(Z\) has exactly six singular points, namely the coordinate points corresponding to the six \(S\)-invariant two-planes.

For example, on the chart \(p_{12}=1\), eliminating \(p_{34}\) using \(G=0\) gives the local equation
\[
(A+B)p_{13}p_{24}-A p_{14}p_{23}=0.
\]
Its quadratic Hessian is nonsingular because \(A(A+B)\ne0\). The five other coordinate charts are identical after relabeling. Hence every singularity of \(Z\) is an ordinary double point. Since \(Y\to Z\) is the base change of the smooth \(\mathbb P^1\)-bundle \(\operatorname{Fl}(1,2;4)\to\operatorname{Gr}(2,4)\),
\[
\operatorname{Sing}(Y)=\bigsqcup_{1\le i<j\le4}\mathbb P^1_{ij},
\]
and transversely along each component the local equation is the threefold node \(xy-zw=0\).

If \(P\) is not \(S\)-invariant, then \(\dim(P+SP)=3\), so there is a unique hyperplane \(H=P+SP\), and \(\pi\) is an isomorphism there. If \(P\) is \(S\)-invariant, then \(P+SP=P\); for each line \(L\subset P\), the hyperplanes containing \(P\) form another \(\mathbb P^1\). Thus over each singular line of \(Y\) the exceptional surface is
\[
\mathbb P(P)\times\mathbb P((\mathbb C^4/P)^*)\cong\mathbb P^1\times\mathbb P^1.
\]
These six surfaces are disjoint and have codimension two in the fourfold \(X\), so \(\pi\) is small.

Abe--Fujita--Zeng identify \(-K_X\) with the Hessenberg weight line bundle. Here the root sum is
\[
\xi_h=\alpha_{12}+\alpha_{13}+\alpha_{23}+\alpha_{34}=2\varpi_1+\varpi_2.
\]
The zero \(\varpi_3\)-coefficient means that this line bundle is pulled back from \(\operatorname{Fl}(1,2;4)\), while the positive coefficients of \(\varpi_1\) and \(\varpi_2\) make the descended bundle \(A\) ample. Hence \(-K_X=\pi^*A\). The variety \(Z\) is a nodal complete intersection, hence normal and Gorenstein, and the \(\mathbb P^1\)-bundle \(Y\to Z\) is also normal and Gorenstein. Since \(\pi\) is a small birational morphism from smooth \(X\), there are no exceptional divisors in the discrepancy formula, so \(K_X=\pi^*K_Y\). Therefore \(A\cong-K_Y\), and for all sufficiently divisible \(m>0\), the complete linear system \(|-mK_X|\) is the pullback of the very ample system \(|mA|\) on \(Y\). This proves that \(Y\) is the anticanonical model and \(\pi\) is crepant.

## Verification
The accompanying exact symbolic checker verifies the determinant identity \(\det[u,v,Su,Sv]=Q\), the factorization \(A+B=(\lambda_1-\lambda_4)(\lambda_2-\lambda_3)\), and nonzero Hessian determinants in all six coordinate charts. Each Hessian determinant factors as a square of a product of four pairwise eigenvalue differences, so the node test is uniform for every regular semisimple \(S\). The checker also verifies \(\xi_h=2\varpi_1+\varpi_2\) and independently evaluates the equivariant localization sum \((-K_X)^4=192\). It terminates with `VERIFY_OK`.

## Relationship to prior work
Abe--Fujita--Zeng, arXiv:2003.12286v1, classify regular semisimple Hessenberg weak-Fano varieties, explicitly single out \(h=(3,3,4,4)\), and compute anticanonical bundles via the weight \(\xi_h\). Their results establish the weak-Fano premise and the anticanonical class used here, but do not identify this anticanonical image, its six nodal strata, or the small crepant resolution.

Cherepanov, DOI:10.1070/SM9278, studies torus actions and orbit spaces for Hessenberg varieties and includes the same Hessenberg function in its GKM analysis. That work concerns orbit-space topology and does not provide the anticanonical contraction above. Brosnan et al., arXiv:2405.18313v1, study automorphisms and deformations of regular semisimple Hessenberg varieties, with principal structural results focused on deformation and automorphism questions rather than this codimension-two anticanonical model.

## Limitations
The result is specific to the four-dimensional regular semisimple Hessenberg variety with \(h=(3,3,4,4)\). It does not classify anticanonical models for arbitrary weak-Fano Hessenberg functions. The originality comparison found no equivalent published description under the searched aliases, but an uncatalogued birational description of the same fourfold could exist. The symbolic checker verifies the algebraic identities used in the proof; it is not a substitute for the literature comparison.

## References
1. H. Abe, N. Fujita, H. Zeng, *Fano and weak Fano Hessenberg varieties*, arXiv:2003.12286v1 (first public 2020-03-27), primary MSC 14M15.
2. D. Cherepanov, *Orbit spaces for torus actions on Hessenberg varieties*, DOI:10.1070/SM9278.
3. P. Brosnan et al., *Automorphisms and deformations of regular semisimple Hessenberg varieties*, arXiv:2405.18313v1.
