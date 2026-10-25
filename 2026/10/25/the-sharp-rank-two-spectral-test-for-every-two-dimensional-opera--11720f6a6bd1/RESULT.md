# The sharp rank-two spectral test for every two-dimensional operator pencil

## Finding
Let \(X\) be a Banach space over \(\mathbb F\in\{\mathbb R,\mathbb C\}\), and let \(\mathcal V\subset\mathcal B(X)\) be a two-dimensional \(\mathbb F\)-linear subspace. A **common right spectral detector** is an operator \(T\in\mathcal B(X)\) such that \(r(CT)>0\) for every nonzero \(C\in\mathcal V\). Define \(d(\mathcal V)\) as its smallest possible rank, or \(\infty\) if none exists. Then
\[
d(\mathcal V)=\begin{cases}
2,&\exists C\in\mathcal V:\operatorname{rank}C\ge2,\\
\infty,&\operatorname{rank}C\le1\text{ for every }C\in\mathcal V.
\end{cases}
\]
If \(A,B\) is a basis with \(\operatorname{rank}A\ge2\), the rank-two detector may be chosen to satisfy
\[
\operatorname{tr}(AT)=0,\qquad
\operatorname{tr}((AT)^2)=2,\qquad
\operatorname{tr}(BT)\ne0.
\]
For this single detector, \(\inf_{|\lambda|+|\mu|=1}r((\lambda A+\mu B)T)>0\). All assertions hold in both scalar fields and all ambient dimensions supporting a two-dimensional operator subspace.

## Assumptions and scope
All operators are bounded. Ranks and traces of finite-rank operators use the usual algebraic definitions. In the real case, the spectral radius of a real operator is that of its complexification. The quantifiers on the detector are **one** \(T\) for **every** nonzero member of the given operator pencil. No reflexivity, Hilbert structure, approximation property, or finite dimensionality of \(X\) is assumed.

## Proof
**1. A nonscalar two-dimensional compression.** Choose independent \(A,B\in\mathcal B(X)\) with \(\operatorname{rank}A\ge2\). We show that there are bounded \(U:\mathbb F^2\to X\) and \(V:X\to\mathbb F^2\) such that
\[
VAU=I_2,\qquad M:=VBU\text{ is not a scalar matrix}.
\]
Indeed, if every such pair produced a scalar \(M\), choose any \(x,y\in X\) with \(Ax,Ay\) independent and put \(U(s,t)=sx+ty\). By Hahn–Banach there is \(V\) with \(VAU=I_2\). Changing either coordinate functional of \(V\) by an arbitrary functional annihilating \(\operatorname{span}\{Ax,Ay\}\) preserves this identity. The assumption that all resulting \(VBU\) are scalar then forces \(Bx,By\in\operatorname{span}\{Ax,Ay\}\). Since \(VBU\) itself is scalar and \(VAU=I_2\), there is \(c_{x,y}\in\mathbb F\) with \(Bx=c_{x,y}Ax\) and \(By=c_{x,y}Ay\). Every \(z\) with \(Az\ne0\) can be paired with a vector having independent \(A\)-image. Comparing such pairs (using a third independent image if the original two images are collinear) makes the coefficient a single scalar \(c\) independent of \(z\). For \(z\in\ker A\), apply the same conclusion to \(x+z\) and \(x\), whose nonzero \(A\)-images coincide; it follows that \(Bz=0\). Thus \(B=cA\), contrary to independence. The required \(U,V\) exist.

**2. A trace-separating involution.** Every nonscalar matrix \(M=\begin{pmatrix}a&b\\c&d\end{pmatrix}\) over \(\mathbb F\) admits a matrix \(H\) with \(H^2=I_2\), \(\operatorname{tr}H=0\), and \(\operatorname{tr}(HM)\ne0\). When \(a\ne d\) take \(H=\operatorname{diag}(1,-1)\). Otherwise, if \(b\ne0\), take \(H=\begin{pmatrix}1&0\\1&-1\end{pmatrix}\); if \(b=0\), necessarily \(c\ne0\), and take \(H=\begin{pmatrix}1&1\\0&-1\end{pmatrix}\). The three relevant traces are respectively \(a-d\), \(b\), and \(c\). The displayed choices work equally over the real and complex fields.

**3. Optimal detector and spectral separation.** Set \(T=UHV\). Since \(VAU=I_2\), \(U\) is injective and \(V\) is surjective; as \(H\) is invertible, \(\operatorname{rank}T=2\). Cyclicity of finite-rank trace gives
\[
\operatorname{tr}(AT)=\operatorname{tr}H=0,\quad
\operatorname{tr}((AT)^2)=\operatorname{tr}(H^2)=2,\quad
\operatorname{tr}(BT)=\operatorname{tr}(HM)\ne0.
\]
For scalars \(\lambda,\mu\), the operator \((\lambda A+\mu B)T\) factors as \((\lambda A+\mu B)U\cdot HV\). The elementary \(PQ/QP\) principle gives exactly the same *nonzero* spectrum as the two-by-two matrix
\[
H(\lambda I_2+\mu M).
\]
If \(\mu\ne0\), this matrix has nonzero trace \(\mu\operatorname{tr}(HM)\), hence a nonzero eigenvalue. If \(\mu=0\) and \(\lambda\ne0\), it is \(\lambda H\), whose eigenvalues are \(\lambda\) and \(-\lambda\). Thus the product is not quasinilpotent for every nonzero pencil parameter, for real parameters as well as complex parameters. Spectral radius is continuous on two-by-two matrices. Its strictly positive values on the compact sphere \(\{|\lambda|+|\mu|=1\}\) therefore have a positive minimum.

**4. Sharpness and the low-rank boundary.** For any \(T\) of rank at most one, the products \(CT\) have rank at most one and their traces give a linear functional \(C\mapsto\operatorname{tr}(CT)\) on the two-dimensional \(\mathcal V\). Its kernel contains some nonzero \(C\). A rank-at-most-one operator with zero trace has square zero and hence spectral radius zero. Thus no rank-one detector works. If, instead, every \(C\in\mathcal V\) has rank at most one, then for **every** bounded \(T\), even of infinite rank, all \(CT\) have rank at most one. The same trace-functional kernel argument shows that no detector exists at all. This proves the stated dichotomy.

## Verification
The proof is independent of finite-dimensional enumeration. An accompanying exact-arithmetic script `support/check_rank2.py` uses Python 3 and SymPy. Execute `python support/check_rank2.py` after extracting it from this package; it checks \(309\) independent real/complex matrix pencils with \(9{,}888\) exact assertions, including sparse kernel/range edge cases. The script checks two-by-two compression, rank, traces, and all nonzero integer parameter pairs in a bounded grid. These are diagnostic finite tests, not certificates of the theorem in arbitrary Banach spaces.

## Relationship to prior work
Aznay–Chabbabi (2026), Lemma 3.2, prove that a two-dimensional complex operator subspace containing an operator of rank at least two admits *some finite-rank* common right multiplier making every nonzero product non-quasinilpotent. Their proof takes a rank-two seed and adds another unspecified finite-rank operator, and no sharp rank bound is claimed. The result here strengthens that lemma to **rank exactly two, which is optimal**, produces an explicit two-dimensional compression/involution and trace normalization, covers real Banach spaces, and settles the no-detector rank-one alternative. Their Section 5 already explains the rank-one trace obstruction; that underlying obstruction is credited, not presented as new. Li–Šemrl–Sze (2007) treat nilpotence-preserving maps rather than minimal common multipliers. Khatskevich–Ostrovskii–Shulman (2005) study spectral-radius maximization of individual operators by multipliers, not a fixed low-rank multiplier separating a whole pencil. The new content is the uniform, optimal detector rank for a **single common** multiplier.

## Limitations
This theorem concerns **two-dimensional** pencils; it does not assert that rank two works for larger subspaces or determine analogous detector ranks for higher-dimensional families. The positive spectral-radius lower bound depends on the operators and the chosen detector; there is no claimed universal numerical bound under norm normalization. Historical equivalence under alternate operator-pencil terminology remains a priority risk; literature searches do not constitute a proof of originality. The numerical checker covers only a finite sample.

## References
1. Z. Aznay and F. Chabbabi, *Surjective maps preserving quasi-nilpotence of products of operators*, arXiv:2610.21840v1 (first submitted 15 October 2026), especially Lemma 3.2 and Sections 3–5. https://arxiv.org/html/2610.21840v1
2. C.-K. Li, P. Šemrl and N.-S. Sze, *Maps preserving the nilpotency of products of operators*, Linear Algebra and its Applications **424** (2007), 222–239.
3. V. A. Khatskevich, M. I. Ostrovskii and V. S. Shulman, *Extremal problems for operators in Banach spaces arising in the study of linear operator pencils*, Integral Equations and Operator Theory **51** (2005), 109–119, DOI:10.1007/s00020-002-1249-x.
