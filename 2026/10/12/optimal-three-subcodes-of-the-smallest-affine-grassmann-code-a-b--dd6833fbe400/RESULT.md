# Optimal three-subcodes of the smallest affine Grassmann code: a binary exception

## Finding
Let \(q\) be any prime power and let \(C=C^{\mathbb A}(2,4)\) be the length-\(q^4\), dimension-\(6\) affine Grassmann evaluation code on the matrices in \(M_2(\mathbb F_q)\). Let \(N_q\) be the number of *distinct three-dimensional linear subcodes* of \(C\) whose union of coordinate supports has the minimum possible cardinality. Then
\[
 d_3(C)=q^4-q^2,\qquad
 N_q=\begin{cases}
 60,&q=2,\\
 2q^2(q+1),&q>2.
 \end{cases}
\]
There is a bijective geometric classification of all these subcodes: they are precisely the spaces of evaluation functions vanishing on affine two-planes \(P\subset M_2(\mathbb F_q)\) on which the determinant restricts to an affine-linear function. For \(q>2\), the directions of these planes are the two classical rulings of rank-at-most-one matrix spaces. For \(q=2\), the directions are instead all totally isotropic planes of the determinant's nondegenerate alternating polar form; this produces the exceptional multiplicity \(60\).

## Assumptions and scope
Identify a generic matrix with \(X=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\), and set \(\Delta(X)=ad-bc\). The six-dimensional function space is
\[
 V=\operatorname{span}_{\mathbb F_q}\{1,a,b,c,d,\Delta\}.
\]
The evaluation map \(\operatorname{ev}:V\longrightarrow\mathbb F_q^{q^4}\) evaluates at every \(X\in M_2(\mathbb F_q)\) once, in any fixed order. It is injective: the first five generators are linearly independent affine functions, and the mixed second difference of \(\Delta\) on a suitable coordinate two-plane is nonzero, so \(\Delta\) is not affine-linear, including when \(q=2\). Thus \(C=\operatorname{ev}(V)\) has dimension six.

For a subspace \(D\le V\), define its common-zero set by \(Z(D)=\{X\in M_2(\mathbb F_q):f(X)=0\text{ for every }f\in D\}\). Its subcode has union-of-support size \(q^4-|Z(D)|\). For each integer \(1\le r\le6\), \(d_r(C)\) denotes the minimum such size over \(r\)-dimensional subspaces of \(V\). Only \(r=3\) is classified here. All counts distinguish subspaces, not choices of generator bases.

## Proof
**1. Every three-subcode has at most \(q^2\) common zeros.** Let \(D\le V\) have dimension three. Let \(\pi:V\to\mathbb F_q\) extract the coefficient of \(\Delta\). If \(\pi(D)=0\), then \(D\) consists of affine-linear functions. If their common equations are consistent, their linear parts have rank three (otherwise a nonzero constant would lie in \(D\), making the system inconsistent), and the zero set is an affine line of \(q\) points. Hence \(|Z(D)|\le q\).

If \(\pi(D)\ne0\), then \(D\cap\ker\pi\) consists of two independent affine functions. Their common equations are either inconsistent or cut out an affine plane \(P\) with \(q^2\) points. The remaining equation in \(D\), which has a nonzero determinant coefficient, can only reduce that intersection. Therefore \(|Z(D)|\le q^2\) in every case.

**2. Equality is equivalent to a special affine plane.** Let \(P=X_0+W\) be an affine plane with \(\dim W=2\). The restrictions of \(1,a,b,c,d\) to \(P\) span all affine-linear functions on \(P\), a space of dimension three. Consequently, the restriction of \(V\) to \(P\) has dimension three exactly when \(\Delta|_P\) is affine-linear. In that event its kernel
\[
 K(P)=\{f\in V:f|_P=0\}
\]
has dimension three; its common zero set is exactly \(P\) by Step 1, so it is optimal. Conversely, any optimal \(D\) has \(|Z(D)|=q^2\), falls in the second case of Step 1, and equals \(K(P)\), where \(P=Z(D)\). Different planes give different kernels because their common zero sets differ. An example is the affine plane of matrices with zero first row: its determinant vanishes identically, proving that the upper bound \(q^2\) is attained. This also establishes \(d_3(C)=q^4-q^2\).

**3. Classifying plane directions.** Let \(U,V\) be an independent basis of \(W\) and write the symmetric polar expression \(B(Y,Z)=\Delta(Y+Z)-\Delta(Y)-\Delta(Z)\). For every \(s,t\in\mathbb F_q\),
\[
\begin{aligned}
 \Delta(X_0+sU+tV)={}&\Delta(X_0)+sB(X_0,U)+tB(X_0,V)\\
 &+s^2\Delta(U)+stB(U,V)+t^2\Delta(V).
\end{aligned}
\]
If \(q>2\), a polynomial of degree at most two in either variable cannot agree as a function on \(\mathbb F_q^2\) with an affine-linear function unless all its quadratic coefficients vanish. Hence the criterion is
\[
 \Delta(U)=\Delta(V)=B(U,V)=0,
\]
equivalently every matrix in \(W\) has determinant zero. Take two independent nonzero rank-one matrices \(U=uv^{\mathsf T}\) and \(V=xy^{\mathsf T}\). The identity \(\Delta(sU+tV)=st\det[u,x]\det[v,y]\) shows that their linear span consists entirely of rank-at-most-one matrices precisely when \(u,x\) are proportional or \(v,y\) are proportional. Thus \(W\) has either a fixed image line or a fixed kernel line. Each choice of a projective line in \(\mathbb F_q^2\) gives exactly one two-space \(W\); the two types are disjoint because their simultaneous condition has dimension one. There are \(2(q+1)\) directions and \(q^4/q^2=q^2\) affine translates of each. This proves \(N_q=2q^2(q+1)\) for \(q>2\), including nonprime fields and fields of even order greater than two.

For \(q=2\), every scalar satisfies \(s^2=s\), so the restrictions of both square terms are already affine-linear. The criterion is solely \(B(U,V)=0\). On the four-dimensional matrix space the explicit form
\[
 B(U,V)=u_{11}v_{22}+u_{22}v_{11}+u_{12}v_{21}+u_{21}v_{12}
\]
is nondegenerate and alternating over \(\mathbb F_2\). Hence its totally isotropic two-spaces are counted by choosing \(U\ne0\) in \(15\) ways and then \(V\in U^{\perp}\setminus\langle U\rangle\) in \(8-2=6\) ways, and dividing by the \((2^2-1)(2^2-2)=6\) ordered bases of each two-space. There are \(15\) directions. Each has \(2^{4-2}=4\) affine translates, giving \(N_2=60\). This completes the classification. \(\square\)

## Verification
The accompanying standard-library Python program `verify.py` independently enumerates *all* three-dimensional coefficient subspaces in reduced row-echelon form for \(q=2,3,4\) (respectively \(1395,33880,376805\) spaces). It evaluates their common zero sets directly on all matrices and independently enumerates the affine-plane directions satisfying the determinant-linearity criterion. The resulting maximum common-zero sizes are respectively \(4,9,16\); the numbers of extremizers are \(60,72,160\); the numbers of qualifying directions are \(15,8,10\). In each case the two independently formed counts satisfy \(N_q=q^2\times(\text{qualifying directions})\). Run `python3 verify.py` to reproduce the terminal marker `VERIFY_OK`. These finite checks test the formulas; the proof of the assertions for every prime power is algebraic and does not rely on extrapolating the computations.

## Relationship to prior work
Affine Grassmann codes are introduced by Beelen, Ghorpade and Høholdt. Datta and Ghorpade study initial and terminal generalized Hamming *weight values*; the value of the third weight is not presented here as an independent novelty claim. Piñero and Singh give a weight spectrum counting individual codewords for the level-two family. Yadav's 2026 preprint revisits that one-codeword weight spectrum. By contrast, the finding here counts and geometrically classifies all *three-dimensional subcodes attaining minimum union of supports*, a statistic not determined just by one-codeword weights or a single generalized-weight value. For this parameter set the calculation also identifies a field-two exception that does not extend to higher even fields.

## Limitations
The theorem is specific to the full affine Grassmann code \(C^{\mathbb A}(2,4)\) and to three-dimensional subcodes. It gives no multiplicity formulas for other levels, matrix dimensions or generalized weights. The independent finite verifier covers \(q=2,3,4\) only; it is not a substitute for the proof over arbitrary prime-power fields. Full text of the 2015 generalized-weights preprint and of the 2026 weight-spectrum preprint was not available for comprehensive overlap comparison, so an earlier unindexed equality-case enumeration cannot be ruled out solely by searches. No independently performed audit is claimed.

## References
1. R. Yadav, *Revisiting the Weight Spectrum of the Affine Grassmann Code* \(C^{\mathbb A}(2,m)\), arXiv:2609.10274, first available 2026-09-09, https://arxiv.org/abs/2609.10274.
2. M. Datta and S. R. Ghorpade, *Higher Weights of Affine Grassmann Codes and Their Duals*, arXiv:1503.02196 (2015), https://arxiv.org/abs/1503.02196.
3. F. L. Piñero and P. Singh, *The weight spectrum of certain affine Grassmann codes*, Designs, Codes and Cryptography 87 (2019), 817–830, DOI:10.1007/s10623-018-0567-1. Accepted manuscript: https://backend.orbit.dtu.dk/ws/files/204176529/Pin_Sin_Weight_Spec_of_Aff_Grass_code.pdf.
4. P. Beelen, S. R. Ghorpade and T. Høholdt, *Affine Grassmann Codes*, IEEE Transactions on Information Theory 56 (2010), 3166–3176, arXiv:0911.1298, https://arxiv.org/abs/0911.1298.
