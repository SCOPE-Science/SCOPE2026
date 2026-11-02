# Characteristic-two Heisenberg-to-traceless-two-matrix homomorphism varieties and image-rank spectra

## Finding

Let \(H_{2n+1}(k)=W\oplus kz\) be the Heisenberg Lie algebra over a field \(k\), where \(n\ge1\), \(\dim W=2n\), and \([u,v]=\omega(u,v)z\) for a nondegenerate alternating form \(\omega\). Let \(\mathcal H_n(k)=\operatorname{Hom}_{\mathrm{Lie}}(H_{2n+1}(k),\mathfrak{sl}_2(k))\). The representation variety is defined in fixed bases by its bracket-preservation equations; image rank is the dimension of the image as a \(k\)-vector space.

**Characteristic two, higher Heisenberg rank (principal classification).** If \(\operatorname{char}k=2\) and \(n\ge2\), every homomorphism kills \(z\). On writing a traceless matrix uniquely as \(ah+be+cf\), where \(h=I_2\), \(e=E_{12}\), and \(f=E_{21}\), the images of \(W\) are parametrized by one unrestricted covector \(a\in W^*\) and a rank-at-most-one linear map \(L=(b,c):W\to k^2\). Thus, as reduced affine varieties over any characteristic-two field,
\[
\mathcal H_n{}_{\mathrm{red}}\simeq\mathbb A_k^{2n}\times D_{2,2n}^{\le1},\qquad n\ge2,
\]
where \(D_{a,b}^{\le1}\) is the rank-at-most-one determinantal variety of \(a\)-by-\(b\) matrices. This variety is geometrically irreducible and has dimension \(4n+1\), with singular locus exactly \(\mathbb A_k^{2n}\times\{0\}\), of dimension \(2n\).

Over \(k=\mathbb F_q\) with even \(q\), write \(t=q^{2n}\). The complete image-rank counts for \(n\ge2\) are
\[
N_0=1,\qquad N_1=(t-1)(q^2+q+1),\qquad N_2=(t-1)(t-q)(q+1),\qquad N_r=0\ (r\ge3).
\]
The total number is
\[
\#\mathcal H_n(\mathbb F_q)=t\bigl(1+(q+1)(t-1)\bigr).
\]

**Low-rank characteristic-two boundary.** For \(n=1\), the *full* (not merely reduced) homomorphism scheme is \(\mathbb A_k^6\): the two generating images are arbitrary in \(\mathfrak{sl}_2(k)\), and the central generator maps to their commutator. Hence the count is \(q^6\). Put \(R=(q-1)(q+1)^2\). Its complete image-rank counts are
\[
N_0=1,\quad N_1=q^2-1+qR,\quad N_2=(q^2-q)R,\quad N_3=q^2(q^2-1)(q^2-q).
\]
The existence of faithful two-dimensional representations in this small case is classical; only the uniform rank-resolved comparison is included here.

**Odd-characteristic comparator (previously covered in commuting-variety literature).** If \(\operatorname{char}k\ne2\), then every homomorphism kills \(z\), and its generating images form a rank-at-most-one \(3\)-by-\(2n\) matrix. Thus \(\mathcal H_n{}_{\mathrm{red}}\simeq D_{3,2n}^{\le1}\), of dimension \(2n+2\), singular only at zero. Over odd \(\mathbb F_q\), the rank distribution is \(N_0=1\), \(N_1=(q^3-1)(q^{2n}-1)/(q-1)\), and \(N_r=0\) for \(r\ge2\). This odd-characteristic determinantal result is not claimed original: it is a consequence of the commuting-variety theorem of Ngo (2012).

## Assumptions and scope

Throughout, \(n\ge1\), \(k\) is an arbitrary field, and \(\omega\) is a nondegenerate alternating bilinear form. Choose a symplectic basis \(x_1,\ldots,x_n,y_1,\ldots,y_n\), with \([x_i,y_j]=\delta_{ij}z\) and all other basic brackets zero. The target is the Lie algebra of trace-zero \(2\)-by-\(2\) matrices with the matrix-commutator bracket, not \(\mathfrak{gl}_2\), the full automorphism group, or the group \(\mathrm{SL}_2\).

“Variety” means the reduced affine variety over \(k\), obtained from the ideal of Lie relations by taking its radical; only the \(n=1\), characteristic-two scheme is also asserted to be isomorphic to affine space scheme-theoretically. The singular-locus statements concern reduced geometric fibers over an algebraic closure. Counts concern labelled homomorphisms in the displayed bases, not conjugacy classes.

## Proof

**1. Reduction.** A homomorphism is specified by a linear map \(\psi:W\to\mathfrak{sl}_2(k)\) and \(Z=\phi(z)\). Its necessary and sufficient equations are
\[
[\psi(u),\psi(v)]=\omega(u,v)Z,\qquad [\psi(u),Z]=0\quad(u,v\in W).
\]
These equations include all pairs of generators, since \(z\) is central and the bracket on \(W\) has one-dimensional image.

**2. Odd characteristic.** The centralizer in \(\mathfrak{sl}_2(k)\) of any nonzero traceless \(2\)-by-\(2\) matrix is the line it spans: over an extension field its centralizer in all matrices is \(kI_2+kX\), and trace zero forces the scalar coefficient to vanish because \(2\ne0\). If \(Z\ne0\), all \(\psi(u)\) lie on the same line, so the first equation forces \(Z=0\), a contradiction. Thus \(Z=0\). Pairwise commutation of traceless \(2\)-by-\(2\) matrices likewise forces their linear span to have dimension at most one. Conversely, arbitrary rank-one-or-less \(\psi\) with \(Z=0\) is a homomorphism. Rank-one matrix parametrization \(uv^T\) identifies the reduced variety with \(D_{3,2n}^{\le1}\). Its dimension, singular set and finite-field point count are the standard rank-one determinantal formulas; the geometric assertions are already encompassed by Ngo’s commuting-variety analysis.

**3. Characteristic two.** In characteristic two, \(h=I_2\) has trace zero and is central in \(\mathfrak{sl}_2(k)\). Its other standard basis elements obey \([e,f]=h\), and \([h,e]=[h,f]=0\). Write \(\psi(u)=a(u)h+b(u)e+c(u)f\) for three covectors \(a,b,c\) on \(W\). Every bracket in the target is a scalar multiple of \(h\). Because \(\omega\ne0\), the first homomorphism equation forces \(Z=\lambda h\) for some \(\lambda\in k\), and it becomes
\[
b(u)c(v)-b(v)c(u)=\lambda\omega(u,v)\quad\text{for all }u,v\in W.
\]
In characteristic two subtraction is addition, but the displayed alternating exterior product is valid in every characteristic. The left side is a decomposable alternating two-form of rank at most two. If \(n\ge2\), the right side has rank \(2n\ge4\) when \(\lambda\ne0\), so \(\lambda=0\). Hence \(b\wedge c=0\), equivalently \(\operatorname{rank}L\le1\), where \(L=(b,c)\); no constraint applies to \(a\). Conversely, these conditions imply both Lie equations. The equations \(b\wedge c=0\) are precisely the \(2\)-by-\(2\) minors of the \(2\)-by-\(2n\) matrix of \(L\), which define a prime determinantal ideal. On the reduced homomorphism variety the extra coordinate \(\lambda\) is zero, giving the product decomposition.

For the rank-at-most-one \(2\)-by-\(2n\) determinantal cone with \(n\ge2\), a nonzero rank-one matrix lies on a smooth open stratum of dimension \(2n+1\), while at zero all defining minors have vanishing derivatives and tangent dimension \(4n>2n+1\). Thus its singular locus is the vertex alone, and the affine factor preserves the singular locus, proving the stated dimension \(4n+1\) and its singular set \(\mathbb A_k^{2n}\times\{0\}\).

For \(n=1\), every alternating two-form on \(W\) is a scalar multiple of \(\omega\). The bracket \([\psi(x_1),\psi(y_1)]\) uniquely determines \(Z\), which is central in the target automatically. Thus an unrestricted ordered pair of traceless matrices defines a homomorphism, giving \(\mathbb A^6\) even before reduction.

**4. Finite-field rank census.** A rank-one \(a\)-by-\(b\) matrix over \(\mathbb F_q\) has exactly \((q^a-1)(q^b-1)/(q-1)\) possible values: choose nonzero column and row vectors and quotient by the free scaling action of \(\mathbb F_q^\times\). This supplies the odd-characteristic counts. In even characteristic, let \(t=q^{2n}\) and \(n\ge2\). There are \((q+1)(t-1)\) nonzero rank-one choices of \(L\), each with a uniquely determined nonzero row-covector line \(U\subset W^*\). For any such \(L\), the \(t\) possibilities for \(a\) comprise exactly \(q\) values in \(U\), which give image rank one, and \(t-q\) outside \(U\), which give image rank two. If \(L=0\), the map has image rank zero for \(a=0\) and rank one for the other \(t-1\) values. Therefore
\[
N_1=(t-1)+q(q+1)(t-1)=(t-1)(q^2+q+1),\qquad N_2=(q+1)(t-1)(t-q).
\]
For \(n=1\), rank \(L\) is zero, one or two. If \(L=0\), varying \(a\) yields one zero map and \(q^2-1\) rank-one maps. There are \(R=(q^2-1)^2/(q-1)\) rank-one choices of \(L\); among \(q^2\) possible \(a\), exactly \(q\) lie in its row line and yield rank one, with the other \(q^2-q\) giving rank two. There are \((q^2-1)(q^2-q)\) invertible choices of \(L\). They force \(Z\ne0\), so the full image spans \(h,e,f\), and their \(q^2\) possible covectors \(a\) yield rank three. These cases exhaust all homomorphisms and prove the asserted formulas.

## Verification

Run the included standalone `verify.py` with a Python 3 interpreter. It constructs the traceless matrix Lie bracket over \(\mathbb F_2\), \(\mathbb F_3\) and \(\mathbb F_4\), explicitly checks all generator-pair Lie relations for every linear map, computes image ranks via finite-field elimination, and compares with both classification and counting formulas. Exhaustive cases: \((n,q)=(1,2),(1,3),(2,2),(1,4)\). They respectively visit \(512,19683,32768,262144\) input linear maps and find \(64,105,736,4096\) homomorphisms. Their respective rank spectra are \((1,21,18,24)\), \((1,104)\), \((1,105,630)\), \((1,315,900,2880)\). The checker ends with `HEISENBERG_TO_SL2_HOM_OK 4 exhaustive field/rank cases`. These are finite consistency checks; the proof above covers arbitrary fields and unbounded ranks.

## Relationship to prior work

Ngo (2012), *Commuting varieties of r-tuples over Lie algebras*, Section 4.2, Proposition 4.2.2, proves the normal irreducible determinantal description for commuting tuples in \(\mathfrak{sl}_2\) when the characteristic differs from two. The odd-characteristic portion here follows from that antecedent and is **not** a novelty claim. Rojas (2012), *Minimal Faithful Representation of the Heisenberg Lie Algebra with Abelian Factor*, studies minimal faithful representation degree in characteristic zero, rather than these characteristic-two parameter spaces, image ranks or point counts. The special three-dimensional characteristic-two Heisenberg Lie algebra has a familiar faithful two-dimensional representation, also posed in Berkeley’s 2010 Lie-theory problem set; its existence is **not** claimed new.

The new contribution assessed here is the higher-rank characteristic-two Hom-variety decomposition, the positive-dimensional singular locus, and the complete finite-field image-rank distribution with its sharp transition at \(n=1\). Published research-record searches for equivalent Heisenberg-to-traceless-matrix parameter spaces, rank spectra, and possible stronger representation-variety classifications located no equivalent result. This is a best-knowledge comparison, not a global priority certificate.

## Limitations

The reduced structure is classified for arbitrary characteristic-two fields, but the potentially nonreduced defining scheme at \(n\ge2\) is not. The classification covers traceless two-by-two target matrices and fixed labelled source bases, not full two-by-two target matrices or orbits under change of basis. For characteristic two, the familiar faithful representation of \(H_3\) and its existence criterion are not novel. No independent proof review or exhaustive search of all pre-digital historical Lie-representation sources has been performed.

## References

1. Nadina E. Rojas, *Minimal Faithful Representation of the Heisenberg Lie Algebra with Abelian Factor*, arXiv:1206.5867, first posted 2012-06-26, https://arxiv.org/abs/1206.5867 .
2. Nham V. Ngo, *Commuting varieties of r-tuples over Lie algebras*, arXiv:1209.1659, first posted 2012-09-07, especially Section 4.2 and Proposition 4.2.2, https://arxiv.org/abs/1209.1659 .
3. Berkeley Mathematics 261A, Problem Set 4 (2010), Problem 8 (faithful two-dimensional characteristic-two Heisenberg representations), https://math.berkeley.edu/~mhaiman/math261A-fall10/problems04.pdf .
