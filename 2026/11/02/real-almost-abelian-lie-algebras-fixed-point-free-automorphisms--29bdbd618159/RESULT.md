# Real almost-abelian Lie algebras: fixed-point-free automorphisms and the imaginary-Jordan parity obstruction

## Finding

Let \(V\) be a nonzero finite-dimensional real vector space and \(A\in\operatorname{GL}_{\mathbb R}(V)\). Form the centerless almost-abelian real Lie algebra
\[
\mathfrak g(A)=\mathbb R v\ltimes_A V,\qquad [v,x]=Ax,\quad [V,V]=0.
\]
An automorphism is *fixed-point-free* (f.p.f.) when its only fixed vector is zero. For each \(\omega>0\) and integer \(j\ge1\), let \(m_{\omega,j}\) be the number of complex Jordan blocks of size \(j\) of \(A_{\mathbb C}\) with eigenvalue \(i\omega\). The following three statements hold.

**(A) Arbitrary-order criterion.** The algebra \(\mathfrak g(A)\) admits an f.p.f. real automorphism if and only if \(A\) is similar over \(\mathbb R\) to \(-A\). Equivalently, for each nonzero complex eigenvalue \(\lambda\) and each Jordan size \(j\), the multiplicity of \(J_j(\lambda)\) equals that of \(J_j(-\lambda)\).

**(B) Periodic criterion.** It admits an f.p.f. real automorphism of *finite order* if and only if \(A\sim_{\mathbb R}-A\) and every \(m_{\omega,j}\) is even. When these conditions hold, there is an f.p.f. automorphism of order exactly four.

**(C) Genuine separation.** If \(A\sim_{\mathbb R}-A\) but some \(m_{\omega,j}\) is odd, the algebra has f.p.f. real automorphisms but none of finite order. The smallest example is the three-dimensional Euclidean-motion Lie algebra with
\[
A=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
Here \(v\mapsto-v\), \(x\mapsto\operatorname{diag}(2,-2)x\) is f.p.f. and of infinite order. Doubling the rotation block instead produces a five-dimensional algebra admitting an f.p.f. automorphism of order four.

The conditions are basis-independent and include nonsemisimple matrices. There is no assumption that \(A\) be diagonalizable.

## Assumptions and scope

The field is exactly \(\mathbb R\), characteristic zero. The dimension of \(V\) is finite and positive, and \(A\) is invertible. This last condition ensures \([\mathfrak g,\mathfrak g]=V\), so \(V\) is characteristic, and \(Z(\mathfrak g)=0\). No assertion is made here for singular \(A\), positive characteristic, or non-almost-abelian Lie algebras.

The eigenvalues and Jordan blocks in the criteria are computed after complexification, but the automorphisms to be classified are **real-linear**. The sign-similarity criterion is stronger than the mere evenness of the characteristic polynomial: multiplicities must match at every Jordan-block size.

## Proof

**1. Reduction to an anti-commuting matrix.** Because \([\mathfrak g(A),\mathfrak g(A)]=V\), every automorphism has the form
\[
\varphi(v)=av+w,\qquad \varphi(x)=Bx\quad(x\in V),
\]
where \(a\in\mathbb R^\times\), \(w\in V\), and \(B\in\operatorname{GL}_{\mathbb R}(V)\). Preserving \([v,x]=Ax\) is equivalent to
\[
BA=aAB.
\]
Conversely, every such triple determines an automorphism. Its matrix is block triangular, so
\[
\varphi\text{ is f.p.f.}\quad\Longleftrightarrow\quad a\ne1\text{ and }1\notin\operatorname{spec}(B).
\]
The similarity \(BAB^{-1}=aA\) shows that the finite nonzero multiset of complex eigenvalues of \(A\) is stable under multiplication by the real scalar \(a\). Hence \(|a|=1\), so \(a=\pm1\). For an f.p.f. automorphism necessarily \(a=-1\), and thus \(BA=-AB\). Conversely, if \(A\sim_{\mathbb R}-A\), there is an invertible real \(B_0\) with \(B_0A=-AB_0\). Choose a nonzero real scalar \(c\) outside the finite set of reciprocals of the nonzero real eigenvalues of \(B_0\). Then \(B=cB_0\) has no eigenvalue one, and \(\varphi(v)=-v\), \(\varphi|_V=B\) is f.p.f. This proves (A). Complex Jordan normal form gives the equivalent matched-block criterion. Since \(A\) and \(-A\) are real, complex similarity between them also implies real similarity (e.g. by the common real rational canonical form).

**2. Real Jordan-block decomposition.** Assume \(A\sim_{\mathbb R}-A\). Partition its nonzero complex eigenvalues into orbits under sign and conjugation. There are two kinds. If an orbit has four members \(\lambda,-\lambda,\bar\lambda,-\bar\lambda\), or consists of two nonzero real eigenvalues \(\lambda,-\lambda\), its corresponding real primary space splits as \(W_+\oplus W_-\), with \(A_-S=-SA_+\) for some real isomorphism \(S:W_+\to W_-\). On this summand set
\[
B(x,y)=(-S^{-1}y,Sx).
\]
Then \(BA=-AB\) and \(B^2=-I\). The only remaining type is \(\{i\omega,-i\omega\}\), with \(\omega>0\). Here the real primary space is the realification of complex Jordan blocks for \(i\omega\). On one block of length \(j\), write \(A=i\omega I+N\) in complex Jordan coordinates and put
\[
D=\operatorname{diag}(1,-1,1,-1,\ldots),\qquad K(z)=D\bar z.
\]
As real maps, \(K^2=I\) and \(KA=-AK\), because \(DN=-ND\). If every multiplicity \(m_{\omega,j}\) is even, pair identical real Jordan blocks, and on each pair put \(B(x,y)=(-Ky,Kx)\). Again \(BA=-AB\) and \(B^2=-I\). Taking the direct sum over all summands yields a real \(B\) with \(BA=-AB\), \(B^2=-I\). Consequently \(\varphi(v)=-v\), \(\varphi|_V=B\) is f.p.f. with \(\varphi^4=I\) and \(\varphi^2\ne I\). This proves sufficiency in (B).

**3. The parity obstruction is necessary.** Conversely suppose \(\varphi\) is an f.p.f. real automorphism of finite order. From Step 1 its scalar is \(-1\), and its restriction \(B\) has finite order, no eigenvalue one, and \(BA=-AB\). Fix \(\omega>0\). In the complexification let \(E\) be the generalized \(i\omega\)-eigenspace of \(A\) and \(N=A-i\omega I\) on \(E\). As \(B\) is real and reverses \(A\), the map
\[
C:E\longrightarrow E,\qquad C(z)=\overline{Bz}
\]
is invertible and complex-antilinear, has finite order, and satisfies \(CN=-NC\). For every \(j\ge1\), define the *primitive Jordan quotient*
\[
P_j=\frac{\ker N^j}{\ker N^{j-1}+N(\ker N^{j+1})}.
\]
It has complex dimension exactly \(m_{\omega,j}\), and \(C\) preserves all spaces in this quotient. The induced \(C_j\) is therefore a finite-order antilinear automorphism of \(P_j\). It cannot fix a nonzero vector: if it did, its fixed vector and complex conjugate would give an eigenvalue one of the induced action of \(B\) on the corresponding quotient of \(E\oplus\bar E\). That contradicts the absence of eigenvalue one for \(B\) (eigenvalues on invariant subquotients are among those of the original operator).

For a complex \(m\)-space, every invertible antilinear map is \(C_j(z)=H\bar z\) for some \(H\in\operatorname{GL}_m(\mathbb C)\). Viewed as a real linear map on dimension \(2m\), its determinant is
\[
\det_{\mathbb R} C_j=(-1)^m|\det_{\mathbb C}H|^2.
\]
On the other hand, every finite-order real automorphism of an **even**-dimensional real space without eigenvalue one has positive determinant: its eigenvalues are roots of unity, nonreal ones occur in conjugate pairs, and the remaining eigenvalues are \(-1\) with even total multiplicity. Hence \((-1)^m=1\) and \(m\) is even. This holds for every \(\omega,j\), proving necessity in (B). Part (C) follows from (A) and (B).

**4. Explicit smallest separation.** For the real rotation matrix \(A=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\), the real reflection \(K=\operatorname{diag}(1,-1)\) anticommutes with \(A\). Then \(B=2K\) has eigenvalues \(2,-2\), so the Lie algebra automorphism \(\operatorname{diag}(-1,2,-2)\) is f.p.f. but has infinite order. Here \(m_{1,1}=1\), excluding every finite-order f.p.f. automorphism. For two copies of this rotation block, choose \(B(x,y)=(-Ky,Kx)\), obtaining \(B^2=-I\), as stated.

## Verification

The accompanying `verify.py` uses exact SymPy arithmetic and constructs \(19\) explicit reversible matrices and f.p.f. automorphisms, including positive and negative real eigenvalues with Jordan chains, paired purely imaginary Jordan blocks of lengths one through four, unpaired imaginary blocks with infinite-order examples, and off-axis complex eigenvalues. It verifies \(BA=-AB\), absence of the eigenvalue one, and \(B^2=-I\) in the finite-order cases. A symbolic two-dimensional calculation confirms that every antilinear anti-commuter of a single rotation block has negative real determinant. The command is `python verify.py`; its recorded output was `VERIFY_OK exact_matrix_constructions=19 parity_obstruction_symbolic=1`.

These tests are finite checks only. The all-dimensional result and impossibility direction are proved in Steps 1–3; no exhaustive computer enumeration or external formal certification is claimed.

## Relationship to prior work

Burde and Dekimpe, *Fixed-point-free automorphisms of solvable Lie algebras*, arXiv:2604.27916v1 (first posted 30 April 2026), Theorems 5.4 and 5.7, characterize the **complex** almost-abelian case by cyclotomic operators and treat finite orders in several complex low-dimensional examples. The present result concerns real automorphisms of centerless real forms and identifies an additional parity obstruction for finite order; neither assertion follows merely by replacing \(\mathbb C\) with \(\mathbb R\) in the complex theorem. The authors' low-dimensional split-real example of an order-four f.p.f. automorphism also appears in an earlier 2025 Mathematics Stack Exchange discussion; that example is not presented as new.

A pertinent earlier framework is Lamb and Roberts' 1999 classification of reversible-equivariant real linear systems under compact symmetry groups. The available abstract is relevant to the operator identity \(BA=-AB\), but its full text could not be inspected in this review; its representation-theoretic results might imply an equivalent criterion. Thus the claimed originality is expressly qualified, not a declaration of historical uniqueness. The proof uses standard real and complex Jordan decompositions and the determinant sign of antilinear maps.

## Limitations

This is an exact existence classification for centerless real almost-abelian Lie algebras, not a classification of all individual automorphisms, their possible finite orders, or their conjugacy classes. The criterion does not address singular \(A\), arbitrary non-centerless almost-abelian Lie algebras, or other base fields. The finite-order assertion guarantees the existence of order four when any finite order is possible; it does not claim all finite orders are multiples of four. The claim of historical novelty is qualified pending wider human-led literature review, and the mathematical proof has not received an independent audit.

## References

1. D. Burde and K. Dekimpe, *Fixed-point-free automorphisms of solvable Lie algebras*, arXiv:2604.27916v1, 30 April 2026. https://arxiv.org/html/2604.27916v1. Relevant: Sections 2–5, especially Theorems 5.4 and 5.7.
2. D. Burde, answer in *Example of a finite-dimensional Lie algebra with a fixed-point-free automorphism of prime power order which is not nilpotent*, Mathematics Stack Exchange, 17 July 2025. https://math.stackexchange.com/questions/5083590/example-of-a-finite-dimensional-lie-algebra-with-a-fixed-point-free-automorphism. Contains the pre-existing rational split-real example.
3. J. G. Zha, *Fixed-point-free automorphisms of Lie algebras*, Acta Math. Sinica (N.S.) 5 (1989), 95–96, as cited and summarized in Reference 1 (not separately inspected in full).
4. J. S. W. Lamb and M. Roberts, *Reversible equivariant linear systems*, J. Differential Equations 159 (1999), 239–279, DOI 10.1006/jdeq.1999.3632. Repository abstract: https://wrap.warwick.ac.uk/id/eprint/106374/. Full paper not inspected; potential stronger-coverage risk.
