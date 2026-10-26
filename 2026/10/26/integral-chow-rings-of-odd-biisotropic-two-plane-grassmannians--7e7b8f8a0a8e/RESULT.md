# Integral Chow rings of odd biisotropic two-plane Grassmannians

## Finding
For each integer \(n\geq 3\), let \(X_n=\operatorname{S_2Gr}(2,2n+1)\) be the smooth variety of two-planes simultaneously isotropic for a general pencil of alternating forms on \(\mathbb C^{2n+1}\). Let \(S\) be the tautological rank-two bundle on \(G_n=\operatorname{Gr}(2,2n+1)\), let \(x=c_1(S^\vee)\) and \(y=c_2(S^\vee)\), and define integral polynomials by \(f_0=1\), \(f_1=x\), and \(f_j=xf_{j-1}-yf_{j-2}\) for \(j\geq2\). Then the restriction map induces graded ring isomorphisms
\[
\operatorname{CH}^{*}(X_n)\;\cong\;H^{2*}(X_n;\mathbb Z)\;\cong\;\frac{\mathbb Z[x,y]}{(f_{2n},f_{2n+1}):x^2},\qquad \deg_{\operatorname{CH}}x=1,\quad\deg_{\operatorname{CH}}y=2.
\]
The colon denotes ideal quotient in the polynomial ring: \(I:x^2=\{a\mid x^2a\in I\}\). All odd integral cohomology groups vanish. This statement is also true for \(n=2\), but that case is included only as a calibration: the cohomology ring of the corresponding quintic del Pezzo fourfold was already computed by Godinho and collaborators.

There is a concrete integral middle-degree invariant. With \(m=2n-2\) and ordinary Grassmannian Schubert classes \(\sigma_{(m-j,j)}\), the \(n\) classes
\[
e_j=\sigma_{(m-j,j)}|_{X_n},\qquad 0\le j\le n-1,
\]
form an integral basis of \(H^{4n-4}(X_n;\mathbb Z)\). Their Poincaré cup-product matrix has entries \(2\) on the diagonal except for the last entry \(1\), entries \(1\) directly above and below the diagonal, and all other entries zero. Its determinant is \(1\) for every \(n\ge2\).

Although the integral Betti numbers of \(X_n\) coincide degree by degree with those of \(\operatorname{Gr}(2,2n)\), their *graded integral cohomology rings are not isomorphic*. Indeed, the primitive ample generator has top self-intersection
\[
\int_{X_n}x^{4n-4}=\frac{(4n-2)!}{(2n-1)!(2n)!}=C_{2n-1},\qquad C_j=\frac{1}{j+1}\binom{2j}{j},
\]
whereas the corresponding top self-intersection on \(\operatorname{Gr}(2,2n)\) is \(C_{2n-2}\). These positive integers differ for every \(n\ge2\).

## Assumptions and scope
The ground field is \(\mathbb C\). The alternating-pencil is general, so its common isotropic locus is smooth of the expected complex dimension \(D=4n-4\), as in Fonarev–Kuznetsov. For two-planes each isotropy equation is a Plücker hyperplane, hence \(X_n\subseteq G_n\) is a smooth intersection of two hyperplanes, with cohomology class \([X_n]=x^2\). The conclusion concerns ordinary integral singular cohomology and the integral Chow ring, not quantum or equivariant multiplication. The graded cohomology-ring classification uses only the ordinary ring and makes no claim about diffeomorphism or homotopy classification.

## Proof
**1. Cell decomposition and ranks.** Fonarev–Kuznetsov, Theorem 1.1, proves that \(X_n\) admits an algebraic affine-cell decomposition and has exactly the integral Betti numbers of \(\operatorname{Gr}(2,2n)\). Consequently the integral cohomology is free, concentrated in even degrees, and the codimension-\(m\) group \(H^{2m}(X_n;\mathbb Z)\), where \(m=2n-2\), has rank \(n\). The cellular cycle-class isomorphism \(\operatorname{CH}^{*}(X_n)\cong H^{2*}(X_n;\mathbb Z)\) preserves multiplication.

**2. Integral basis in the middle.** Let \(w=2n-1\) be the width of the two-row Schubert rectangle for \(G_n\). By the integral Schubert Poincaré pairing and \([X_n]=x^2\),
\[
\int_{X_n}e_i e_j=\int_{G_n}\sigma_{(m-i,i)}\,x^2\,\sigma_{(m-j,j)}.
\]
The complementary partition to \((m-i,i)\) in the \(2\times w\) rectangle is \((w-i,i+1)\). Twice applying the Pieri rule shows that the coefficient of this partition in \(x^2\sigma_{(m-j,j)}\) is \(2\) when \(i=j<n-1\), \(1\) when \(i=j=n-1\), \(1\) when \(|i-j|=1\), and \(0\) otherwise. Denote the resulting tridiagonal matrix by \(B_n\). The upper-left \(s\times s\) principal minor for \(s<n\) has determinant \(s+1\), by the determinant recurrence, and \(\det B_n=n-(n-1)=1\). Since integral Poincaré duality supplies a unimodular middle pairing on the torsion-free cohomology of \(X_n\), the sublattice spanned by \(e_0,\ldots,e_{n-1}\) has index \(1\). It is therefore an integral basis.

**3. Integral restriction in every degree.** The integral weak Lefschetz theorem for the two successive smooth hyperplane sections gives \(H^q(G_n;\mathbb Z)\xrightarrow{\sim}H^q(X_n;\mathbb Z)\) for \(q<D\). Step 2 establishes surjectivity for \(q=D\). For each \(p\) with \(0\le p\le 2n-3\), multiplication by \(x^2\colon H^{2p}(G_n;\mathbb Z)\to H^{2p+4}(G_n;\mathbb Z)\) has *primitive image*. To see this integrally, list source partitions \((p-j,j)\) in increasing \(j\) and target partitions \((p+2-i,i)\) in increasing \(i\). The first as many target partitions as source partitions all fit in the \(2\times w\) rectangle; in the corresponding square minor of the Pieri multiplication matrix the entries with \(i<j\) vanish (boxes cannot be removed from the second row), and the diagonal entries are \(1\) (add both boxes to the first row). Thus this minor is unitriangular with determinant \(1\). In particular the map is a split injection of free abelian groups.

By integral Poincaré duality, restriction in complementary high degrees is the transpose of the Gysin map \(i_*\colon H^{2p}(X_n;\mathbb Z)\to H^{2p+4}(G_n;\mathbb Z)\). For \(p<2n-2\), weak Lefschetz identifies this Gysin map with multiplication by \(x^2\). Its primitive image makes the dual restriction surjective in every high degree. Consequently \(i^*\colon H^{2*}(G_n;\mathbb Z)\twoheadrightarrow H^{2*}(X_n;\mathbb Z)\) is surjective in every degree.

**4. Kernel.** For a smooth codimension-two complete intersection the projection formula gives \(i_*i^*(a)=x^2a\). Because restriction is surjective in all degrees, integral Poincaré duality implies \(i_*\) is injective in all degrees. Hence \(\ker i^*=\operatorname{Ann}_{H^{2*}(G_n;\mathbb Z)}(x^2)\). The classical rank-two Grassmannian presentation
\[
H^{2*}(G_n;\mathbb Z)=\mathbb Z[x,y]/(f_{2n},f_{2n+1})
\]
now gives exactly the asserted colon-ideal quotient. This identifies the entire integral multiplicative ring, not only graded ranks.

**5. Distinction from the additive Grassmannian partner.** Schubert calculus gives \(\int_{G_n}x^{4n-2}=C_{2n-1}\). Since \([X_n]=x^2\), the displayed degree formula follows. On \(\operatorname{Gr}(2,2n)\) the analogous degree is \(C_{2n-2}\). Both spaces have a rank-one second cohomology group with a primitive ample class. Any graded integral ring isomorphism must send the generator to its positive or negative, so it preserves the absolute top self-intersection. Strict increase of Catalan numbers proves nonisomorphism.

## Verification
The standalone file `verify.py` uses exact integer arithmetic and the integral Pieri rule. For every \(2\le n\le15\) it constructs \(B_n\), checks its determinant is \(1\), checks a unimodular minor of multiplication by \(x^2\) in every complementary low degree, and computes the Grassmannian top Plücker power. Sample degrees for \(n=2,3,4,5,6\) are \(5,42,429,4862,58786\). The checker is a finite consistency test; the five proof steps above establish the theorem for all integers \(n\ge3\).

## Relationship to prior work
Fonarev and Kuznetsov (2026), Theorem 1.1 and Remark 1.2, establish the affine paving and *additive* cohomology groups, and explicitly identify determination of multiplication as a separate problem. They are essential inputs, not independently reproved claims. Benedetti (2018/2021) determines equivariant Chevalley multiplication for two-plane *even-dimensional* bisymplectic Grassmannians \(\operatorname{I_2Gr}(2,2s)\); those are different varieties from the present odd-dimensional-pencil spaces \(\operatorname{S_2Gr}(2,2n+1)\). Godinho and collaborators (2025) compute the ordinary and equivariant ring of the quintic del Pezzo fourfold, exactly the \(n=2\) special case; novelty is claimed only for the uniform family \(n\ge3\), its colon-ideal description, integral lattice basis and ring separation. Standard weak Lefschetz, integral Schubert Pieri, and Grassmannian Chern presentations are credited classical tools. Searches of semantic mathematical research records did not reveal this full odd-family statement, but negative searches are not proofs of priority.

## Limitations
The theorem does not address \(k\ge3\), where isotropy equations are not simply two Plücker hyperplanes; nor does it give quantum/equivariant rings. The statement concerns smooth general pencils. The invariant \(C_{2n-1}\) distinguishes the rings from their additive comparison partner, not from all possible Grassmannians or other Fano varieties. The generic family argument relies on the published smoothness and cellular decomposition results. Although a direct equivalent in the inspected sources was not found, a prior implicit colon-ideal computation for linear sections is a remaining originality risk. No independent audit has been performed.

## References
1. A. Fonarev and A. Kuznetsov, *Betti Numbers of Odd Biisotropic Symplectic Grassmannians*, arXiv:2610.03309v1 (October 2, 2026), especially Theorem 1.1 and Remark 1.2.
2. V. Benedetti, *Bisymplectic Grassmannians of planes*, arXiv:1809.10902v1 (September 28, 2018); *Journal of Algebraic Combinatorics*, DOI:10.1007/s10801-020-00945-4.
3. L. Godinho et al., *On a symplectic generalization of a Hirzebruch problem*, *Journal of Fixed Point Theory and Applications* (2025), DOI:10.1007/s11784-025-01224-0, especially Corollary 1.2 and Theorem 5.12.
4. Standard integral Grassmannian Schubert calculus (Pieri and complementary-partition Poincaré pairing), the integral Lefschetz hyperplane theorem and the cellular cycle-class theorem.
