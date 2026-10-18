# An integral cohomology and Chow ring presentation for odd biisotropic two-plane Grassmannians

## Finding

For every integer \(n\ge 2\), let \(X_n\) be the smooth variety of two-dimensional linear subspaces of \(\mathbb C^{2n+1}\) isotropic for both members of a general pencil of alternating forms. This is the odd biisotropic Grassmannian \(\mathrm{S}_2\mathrm{Gr}(2,2n+1)\). Write \(\mathcal U\) for the restricted universal two-plane subbundle and set
\[
 u=c_1(\mathcal U^\vee),\qquad v=c_2(\mathcal U^\vee).
\]
Use the same letters for their Chow and integral singular cohomology classes. Set \(h_0=1\), \(h_1=u\), and recursively \(h_r=uh_{r-1}-vh_{r-2}\) for \(r\ge2\). In \(\mathbb Z[u,v]\), let \(I_n=(h_{2n},h_{2n+1})\) and form its ideal quotient
\[
 I_n:(u^2)=\{f\in\mathbb Z[u,v]:u^2f\in I_n\}.
\]
Then restriction of tautological Chern classes induces **integral graded-ring isomorphisms**
\[
 \boxed{\quad CH^*(X_n)\ \cong\ H^{2*}(X_n;\mathbb Z)\ \cong\ \mathbb Z[u,v]/(I_n:(u^2)),\qquad H^{2*+1}(X_n;\mathbb Z)=0.\quad}
\]
In the Chow grading, \(\deg u=1\) and \(\deg v=2\); the corresponding singular-cohomology degrees are twice these values.

A stronger explicit middle-degree statement supplies the key integral calculation. Let \(m=2n-2\). The restrictions of the Grassmannian Schubert classes \(\sigma_{(m-i,i)}\), \(0\le i\le n-1\), form an integral basis of \(H^{2m}(X_n;\mathbb Z)\). Its intersection matrix \(M_n\) has entries
\[
 (M_n)_{ij}=\begin{cases}
 2,&i=j<n-1,\\
 1,&i=j=n-1,\\
 1,&|i-j|=1,\\
 0,&\text{otherwise},
 \end{cases}\qquad \det M_n=1.
\]
Thus the entire integral ring—not just its Betti numbers or a distinguishing Plücker intersection number—is determined by an explicit two-generator ideal quotient.

## Assumptions and scope

The ground field is \(\mathbb C\). The alternating-form pencil is general so that the stated common zero locus is smooth; no assertions concern degenerate pencils, singular fibers, other values of the plane dimension, or characteristic-positive geometry. Let \(G=\operatorname{Gr}(2,2n+1)\), a smooth Grassmannian of complex dimension \(4n-2\). The variety \(X_n\subset G\) is a smooth complete intersection of two Plücker hyperplanes, of complex dimension \(d=4n-4\). Its cohomology is torsion-free and concentrated in even degrees, with the same graded ranks as \(\operatorname{Gr}(2,2n)\), by the affine paving and additive theorem of Fonarev--Kuznetsov. Neither the equality of additive ranks nor the earlier Plücker-degree distinction is claimed as new here.

## Proof

**1. An ambient integral presentation.** Put \(W=2n-1\), so \(G=\operatorname{Gr}(2,W+2)\). The classical integral Schubert presentation is
\[
 H^{2*}(G;\mathbb Z)=CH^*(G)=\mathbb Z[u,v]/(h_{W+1},h_{W+2})=\mathbb Z[u,v]/I_n.
\]
Indeed \(u,v\) are the elementary symmetric functions of the Chern roots of \(\mathcal U^\vee\), and the \(h_r\) are complete symmetric polynomials in those roots. Each alternating form defines a section of \(\bigwedge^2\mathcal U^\vee=\mathcal O_G(1)\); the two independent equations cut out \(X_n\), with \([X_n]=u^2\) in the Chow ring and in integral cohomology of \(G\).

**2. Low-degree classes and the middle intersection matrix.** Set \(m=W-1=d/2\). The integral weak Lefschetz theorem gives an isomorphism \(H^{2j}(G;\mathbb Z)\to H^{2j}(X_n;\mathbb Z)\) for \(j<m\), and injectivity for \(j=m\). The additive theorem cited in the assumptions gives \(\operatorname{rank}H^{2m}(X_n;\mathbb Z)=n\). The ambient degree-\(m\) Schubert basis is indexed by \(\lambda_i=(m-i,i)\), \(0\le i\le n-1\), so it also has rank \(n\).

For two such partitions \(\lambda_i,\lambda_j\), their intersection on \(X_n\) is the Grassmannian integral
\[
 \int_{X_n}i^*\sigma_{\lambda_i}\,i^*\sigma_{\lambda_j}
 =\int_G\sigma_{\lambda_i}\sigma_{\lambda_j}u^2.
\]
The Pieri identity \(u^2=\sigma_{(2,0)}+\sigma_{(1,1)}\), together with complement partitions in the \(2\times W\) rectangle, gives exactly the matrix \(M_n\) displayed above. To compute its determinant, let \(D_k\) denote the determinant of the \(k\times k\) tridiagonal matrix with diagonal \(2\) and adjacent off-diagonal entries \(1\). Then \(D_0=1\), \(D_1=2\), \(D_k=2D_{k-1}-D_{k-2}=k+1\). Expanding the final diagonal entry \(1\) of \(M_n\) shows \(\det M_n=D_{n-1}-D_{n-2}=1\).

If the image of middle restriction were a proper finite-index sublattice of the torsion-free middle cohomology, its restricted intersection determinant would be divisible by the square of that index, contradicting \(\det M_n=1\). Hence middle restriction is an integral isomorphism.

**3. High-degree surjectivity by a unit triangular pairing.** Fix codimension \(m<j\le d\), and put \(\ell=d-j<m\). The rank of the target \(H^{2j}(X_n;\mathbb Z)\) is \(r=\lfloor\ell/2\rfloor+1\), by even-degree Poincaré duality and low-degree weak Lefschetz. Choose the low-degree Schubert basis \(\mu_t=(\ell-t,t)\), \(0\le t<r\), whose restrictions form a basis of \(H^{2\ell}(X_n;\mathbb Z)\). In ambient codimension \(j\) choose classes indexed by \(\lambda_s=(W-s,j-W+s)\), \(0\le s<r\); these are valid two-row partitions contained in the \(2\times W\) rectangle.

The matrix of intersection pairings is
\[
 B_{st}=\int_X i^*\sigma_{\lambda_s}\,i^*\sigma_{\mu_t}
 =\int_G\sigma_{\lambda_s}\sigma_{\mu_t}u^2.
\]
The complement of \(\lambda_s\) is \(\nu_s=(\ell+2-s,s)\). The two-step Pieri rule makes \(B_{st}=0\) whenever \(s<t\), because \(\nu_s\) then has a shorter second row than \(\mu_t\). On the diagonal \(s=t\), precisely the horizontal two-box strip, both added to the first row, contributes, giving \(B_{ss}=1\). Thus the selected \(r\times r\) matrix is lower triangular with unit diagonal; its determinant is \(1\). By the unimodular integral Poincaré pairing on \(X_n\) and the complete low-degree basis, these high-degree restricted classes form a basis. It follows that the ambient restriction map \(H^{2*}(G;\mathbb Z)\to H^{2*}(X_n;\mathbb Z)\) is surjective **in every degree**, not merely over \(\mathbb Q\).

**4. The exact kernel.** Write \(R=H^{2*}(G;\mathbb Z)\). For \(a\in R\), surjectivity and Poincaré duality on \(X_n\) imply
\[
 i^*a=0\ \Longleftrightarrow\ \int_{X_n}i^*(a b)=0\text{ for every complementary }b\in R.
\]
By the projection formula and \([X_n]=u^2\), this is equivalent to \(\int_G a b u^2=0\) for every such \(b\). The ambient Schubert intersection pairing is perfect over \(\mathbb Z\), so the latter condition is equivalent to \(a u^2=0\) in \(R\). Thus \(\ker i^*=\operatorname{Ann}_R(u^2)\). Lifting to the polynomial ring gives exactly the ideal quotient \(I_n:(u^2)\), as claimed.

**5. From cohomology to Chow.** The affine paving from Fonarev--Kuznetsov identifies the integral cycle-class map \(CH^j(X_n)\to H^{2j}(X_n;\mathbb Z)\) as an isomorphism of abelian groups, and it is multiplicative. All odd cohomology vanishes. The same polynomial quotient therefore describes the full integral Chow ring.

## Verification

The accompanying standalone standard-library checker implements both Littlewood--Richardson/Pieri coefficient counting and an independent two-variable Schubert-root coefficient extraction. For all \(2\le n\le35\) it reconstructs the middle tridiagonal matrix and determinant and the high-degree unit triangular minors. For \(2\le n\le12\) it also compares the two independent pairing computations entry by entry. The executed check printed \(\texttt{VERIFY\_OK}\); it also reproduces the Plücker degrees \(5,42,429,4862,58786\) for \(n=2,3,4,5,6\). The proof above, not the finite checks, establishes all \(n\ge2\). The verifier requires only Python's standard library; execute \(\texttt{python3 CHECK.py}\).

## Relationship to prior work

Fonarev and Kuznetsov, arXiv:2610.03309v1, prove additive integral Betti-number coincidences for odd biisotropic Grassmannians and supply the affine paving; their Remark 1.2 explicitly separates ring structures as a further question. The present finding answers this multiplicative question in the complete two-plane subfamily, giving an integral two-generator presentation and middle pairing. Earlier degree-based work distinguishes these ring structures from those of ordinary Grassmannians but stops short of computing them. Benedetti, arXiv:1809.10902, computes cohomological structures for **even-ambient** bisymplectic Grassmannians; the odd-ambient family and its integral colon-ideal presentation are different objects. The underlying Grassmannian Pieri identity and integral Poincaré duality are classical. The novelty claim concerns the combined uniform ring identification, not those general tools.

## Limitations

No complete ring presentation is asserted for odd biisotropic \(k\)-plane Grassmannians with \(k>2\), singular pencil members, or positive characteristic. The ideal quotient is an effective, canonical finite presentation, but no minimal generating set for its ideal is claimed. The calculation does not assert quantum ring, Hodge-theoretic, or enumerative consequences. Priority remains subject to the possibility that a more general earlier theorem implicitly yields the same presentation; no independent historical audit has been performed.

## References

Fonarev, A., and Kuznetsov, A., *Betti Numbers of Odd Biisotropic Symplectic Grassmannians*, arXiv:2610.03309v1 (first posted 2026-10-02), especially Theorem 1.1 and Remark 1.2.

Benedetti, V., *Bisymplectic Grassmannians of planes*, arXiv:1809.10902v1 (2018), introduction and cohomology-ring section.

Standard ingredients: integral weak Lefschetz theorem, Schubert calculus on \(\operatorname{Gr}(2,N)\), the two-box Pieri rule, and Poincaré duality.
