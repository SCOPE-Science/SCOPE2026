# Sharp coordinate Fourier spectrum on the finite-field Plücker cone

## Finding
For every prime power \(q\ge2\) and integer \(m\ge4\), the constant additive character and all nontrivial one-coordinate additive characters on the cone of decomposable bivectors have an explicit complete Gram spectrum, with exact equality eigenspaces. The sharp least-eigenvalue mode switches strictly at an arithmetic threshold that depends on \(q\), including characteristic two.

Write \(E=\binom m2\), and put
\[
W=q^{2m}-(q+1)q^m+q^3,\quad
A=q^{2m-2}-(q+1)q^m+q^3,\quad
B=q^{2m-4}-(q+1)q^m+q^3,
\]
\[
a=A/W,\quad b=B/W,\quad
C=1-a,
\]
\[
R=1+(q-2)a+(q-1)((m-4)a-(m-3)b),
\]
\[
D=1-qa+(q-1)b,\quad
H=1+(q-2)a+(q-1)(2(m-2)a+\tbinom{m-2}{2}b),
\]
\[
h=a\sqrt{E(q-1)},\qquad L_{\pm}=\frac{1+H\pm\sqrt{(1-H)^2+4h^2}}2.
\]
The full multiset of eigenvalues of the normalized Gram matrix is
\[
\begin{array}{c|ccccc}
\text{eigenvalue}&L_-&L_+&C&R&D\\\hline
\text{multiplicity}&1&1&E(q-2)&m-1&m(m-3)/2
\end{array}
\]
with zero multiplicities omitted and any coincident values combined. The family is linearly independent. Its sharp upper Riesz bound is \(L_+\), and its sharp lower bound is
\[
\min\{D,L_-\}=\begin{cases}D,&4\le m<M_q,\\ L_-,&m\ge M_q,\end{cases}
\quad
M_q=\begin{cases}10,&q=2,\\4q+3,&q=3,4,\\4q+4,&q\ge5.\end{cases}
\]
No equality occurs at the transition. The optimal squared Riesz condition number is \(L_+/\min\{D,L_-\}\).

## Assumptions and scope
Let \(V=\mathbb F_q^m\) and let \(X=\{u\wedge v:u,v\in V\}\subseteq\bigwedge^2 V\); the zero bivector is included. For each pair \(e=\{i,j\}\), \(i<j\), denote the Plücker coordinate by \(x_e\). Fix *any* nontrivial additive character \(\psi:\mathbb F_q\to\mathbb C^\times\). In \(L^2(X,\mu)\), where \(\mu\) is uniform probability measure, form the family
\[
\mathcal F=\{1\}\cup\{x\mapsto\psi(t x_e):e\in\tbinom{[m]}2,\quad t\in\mathbb F_q^\times\}.
\]
Its size is \(1+E(q-1)\). The matrix is the Gram matrix of these displayed functions, using the standard \(\ell^2\) norm for coefficient vectors. The result concerns this specific coordinate character band, not all additive characters on the ambient exterior-power space.

## Proof
**Counting and exact character averages.** An ordered pair \((u,v)\in V^2\) satisfies \(u\wedge v=0\) in precisely \((q+1)q^m-q\) cases. Every fixed nonzero decomposable bivector has exactly \(|\mathrm{SL}_2(\mathbb F_q)|=q(q^2-1)\) ordered preimages, since a choice of ordered basis of its plane with a prescribed wedge is an \(\mathrm{SL}_2\)-torsor. Therefore
\[
|X|=\frac{q^{2m}-(q+1)q^m+q^3}{q(q^2-1)}=\frac W{q(q^2-1)}.
\]
For any alternating bilinear form \(\Xi:V\times V\to\mathbb F_q\) of even matrix rank \(r\), character orthogonality in the second argument gives
\[
\sum_{u,v\in V}\psi(\Xi(u,v))=q^{2m-r}.
\]
Separating the dependent pairs and using the same preimage count yields the *exact*, not asymptotic, transform
\[
\frac1{|X|}\sum_{x\in X}\psi(\langle\Xi,x\rangle)
=\frac{q^{2m-r}-(q+1)q^m+q^3}{W}.
\]
The alternating functional corresponding to one nonzero coordinate has rank two. A nontrivial difference of coordinate frequencies also has rank two if the two coordinate edges are identical or intersect, and rank four if their edges are disjoint. Thus all distinct nonconstant columns have inner product \(a\) when their two edges meet, or \(b\) when disjoint; every nonconstant column has inner product \(a\) with the constant column, and all diagonal Gram entries are one. The values are real, even when the additive character takes nonreal values.

**Diagonalizing the Gram matrix.** On each edge the \(q-1\) character columns split orthogonally into the one-dimensional constant-across-labels direction and a \(q-2\)-dimensional label-contrast space. The latter has eigenvalue \(C=1-a\). On the edge-uniform subspace, the remaining edge Gram operator is
\[
\bigl(1+(q-2)a\bigr)I+(q-1)aA_J+(q-1)bA_K,
\]
where \(A_J\) is adjacency for intersecting edges in the Johnson graph \(J(m,2)\), and \(A_K\) is adjacency for disjoint edges, with \(I+A_J+A_K=J\) (the all-ones matrix). The eigenvalues of \(A_J\) are \(2(m-2)\), \(m-4\), and \(-2\) on, respectively, the uniform edge vector, the vertex-incidence contrasts, and the kernel of the vertex-edge incidence map; their dimensions are \(1\), \(m-1\), and \(m(m-3)/2\). On the last two spaces \(A_K=-I-A_J\), giving exactly \(R\) and \(D\).

The constant character couples only with the normalized uniform edge mode. Their two-dimensional Gram block is
\[
\begin{pmatrix}1&h\\h&H\end{pmatrix},\qquad h=a\sqrt{E(q-1)},
\]
whose eigenvalues are \(L_\pm\). This proves all multiplicities and identifies each equality coefficient space: label contrasts, centered vertex-incidence weights \(w_{ij}=v_i+v_j\) with \(\sum_i v_i=0\), cycle weights \(\sum_{j\ne i}w_{ij}=0\) for every vertex, and the two eigenlines in the constant/uniform block.

**Strict positivity and the largest eigenvalue.** Each single-coordinate axis \(\{t e_i\wedge e_j:t\in\mathbb F_q\}\) lies in \(X\). If a linear combination of the displayed characters vanishes on \(X\), its restriction to every such axis, followed by additive Fourier inversion, forces all nonzero-frequency coefficients for that edge to vanish. Repeating for all edges forces the constant coefficient to vanish. Hence the Gram matrix is positive definite for all \(q,m\). Moreover \(A>B\), and
\[
D=\frac{q^{2m-4}(q^2-1)(q^2-q+1)}W>0,\qquad R>C>D.
\]
Finally \(H-R=m(q-1)\bigl(a+(m-3)b/2\bigr)>0\). For \(m\ge6\), both \(A\) and \(B\) are positive; for \(m=4,5\), direct substitution shows the parenthesized expression is positive. Since \(h>0\), \(L_+>H>R>C>D\), so the upper bound is always \(L_+\).

**Exact least-eigenvalue transition.** Since \(D<1\), the position of \(D\) relative to \(L_-\) is determined by the determinant of the constant/uniform block minus \(D I\). Direct factorization gives
\[
(1-D)(H-D)-h^2
=\frac{(m-1)(q-1)(A-B)}{2W^2}\,S(q,m),
\]
\[
S(q,m)=4\bigl(qA-(q-1)B\bigr)-m\bigl(A-(q-1)B\bigr).
\]
The factor preceding \(S\) is strictly positive. Because \(D<1<L_+\), a positive determinant means \(D<L_-\), whereas a negative determinant means \(L_-<D\). For \(m=4,5\) direct substitution gives \(S>0\). For \(6\le m\le4q\), the decomposition \(S=(4q-m)A+(q-1)(m-4)B\) and \(A,B>0\) show \(S>0\).

For \(m>4q\), put \(P(q,m)=4(q^3-q+1)-m(q^2-q+1)\). Then
\[
S=q^{2m-4}P(q,m)-\bigl((q+1)q^m-q^3\bigr)\bigl(4+(q-2)m\bigr).
\]
For \(m\ge4q+4\), \(P<0\), so \(S<0\). For the three borderline values \(m=4q+r\), \(r\in\{1,2,3\}\), one has \(P=4(q-1)^2-r(q^2-q+1)\). Whenever \(P>0\), it is a positive integer and
\[
q^{m-4}\ge q^{4q-3}\ge q^5\ge4q^3>(q+1)\bigl[4+(q-2)(4q+3)\bigr],
\]
so \(S>0\); whenever \(P<0\), \(S<0\). The borderline sign changes occur at \(r=2\) for \(q=2\), \(r=3\) for \(q=3,4\), and \(r=4\) for \(q\ge5\). All signs are strict, establishing the advertised \(M_q\). No continuum asymptotics or finite enumeration is used for the universal conclusion.

## Verification
The supplied independent checker constructs \(X\) from ordered pairs, forms the full complex Fourier Gram matrix by direct summation, compares every entry with the rank-two/rank-four predictions, and tests explicit contrast, incidence, cycle and mixed eigenvectors. It covers eight full finite-field cases, including \(\mathbb F_4\), and independently tests \(3{,}642\) exact-integer threshold signs for the claimed field-dependent crossover. The checker uses only Python standard-library modules. These finite checks corroborate the unconditional proof but do not establish it for untested parameters.

## Relationship to prior work
The finite-field Plücker model and decomposable-vector rank classification are treated by Ghorpade, Patil and Pillai in their work on higher weights of Grassmann codes (arXiv:0710.5161, especially Sections 1, 3, 5 and 6). The classical alternating-form association scheme of Delsarte and Goethals determines rank-sensitive harmonic data on the ambient alternating-form space. Those are foundational ingredients rather than new assertions here. Johnson-graph eigenspaces are likewise classical. The contribution here is the specific coordinate-restricted *complex Fourier Gram spectrum*, exact sharp eigenmodes, and arithmetic dimension crossover of the Plücker-cone frame. Matrix rank-one, Veronese-cone and Grassmann-incidence Fourier/frame classifications on other underlying sets do not directly imply these constants. Bibliographic and abstract records, rather than full text, were available for the 1975 alternating-form article, so a hidden equivalent specialization remains a priority risk.

## Limitations
The result does not classify all frequency subsets, arbitrary weighted Plücker cones, all singular values of the full ambient Fourier restriction operator, or optimal frames among other sampling choices. It is not a proof of historical uniqueness. Verification of the full 1975 Delsarte–Goethals text and an independent mathematical audit remain outstanding; these access limitations do not enter the self-contained correctness proof.

## References
1. S. R. Ghorpade, A. R. Patil, H. K. Pillai, “Decomposable Subspaces, Linear Sections of Grassmann Varieties, and Higher Weights of Grassmann Codes,” arXiv:0710.5161 (first public version, 26 October 2007), https://arxiv.org/abs/0710.5161 .
2. P. Delsarte, J.-M. Goethals, “Alternating Bilinear Forms over GF(q),” *Journal of Combinatorial Theory, Series A* **19** (1975), 26–50, DOI:10.1016/0097-3165(75)90090-4 .
3. C. Maldonado, D. Penazzi, “Lattices and Norton algebras of Johnson, Grassmann and Hamming graphs,” arXiv:1204.1947 (2012), https://arxiv.org/abs/1204.1947 .
4. M. Fickus, D. G. Mixon, “Tables of the existence of equiangular tight frames,” arXiv:1504.00253 (first public version, 1 April 2015), https://arxiv.org/abs/1504.00253 .
