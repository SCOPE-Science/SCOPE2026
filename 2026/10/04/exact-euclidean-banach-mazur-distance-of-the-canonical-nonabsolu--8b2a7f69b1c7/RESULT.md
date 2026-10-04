# Exact Euclidean Banach--Mazur distance of the canonical nonabsolute Day--James octagon
## Finding
Let \(\psi:[0,1]\to\mathbb R\) be the function
\[
\psi(t)=
\begin{cases}
1-t,&0\le t\le \frac18,\\
\frac{11-4t}{12},&\frac18\le t\le\frac12,\\
\frac{1+t}2,&\frac12\le t\le1.
\end{cases}
\]
Let \(X=\ell_\psi-\ell_\infty\) be the real generalized Day--James plane: in the quadrants with nonnegative coordinate product its norm is the absolute normalized norm associated with \(\psi\), and in the quadrants with nonpositive coordinate product its norm is \(\ell_\infty\). Then
\[
d_{\mathrm{BM}}(X,\ell_2^2)^2=\frac{13}9,
\qquad
d_{\mathrm{BM}}(X,\ell_2^2)=\frac{\sqrt{13}}3.
\]
An optimal Euclidean pullback norm, up to positive scaling, is
\[
|(x,y)|_*=\sqrt{x^2+\frac{10}{13}xy+y^2}.
\]

## Assumptions and scope
The scalar field is real. The multiplicative Banach--Mazur distance is
\[
d_{\mathrm{BM}}(X,\ell_2^2)=\inf_T\|T\|\,\|T^{-1}\|,
\]
where \(T\) ranges over invertible real linear maps from \(X\) to the Euclidean plane. The 2006 source introducing this particular example states that its unit sphere is an octagon and uses it as an explicit normalized norm that is not linearly isometric to any absolute normalized plane. From the displayed \(\psi\) and the \(\ell_\infty\) branch, its unit ball is the centrally symmetric octagon with vertices
\[
(0,1),\ \left(\frac23,\frac23\right),\ \left(1,\frac17\right),\ (1,-1)
\]
and their negatives.

## Proof
Every Euclidean pullback norm has the form \(|z|_q=\sqrt{q(z)}\) for a positive-definite quadratic form \(q\). On the unit sphere \(S_X\), put
\[
m(q)=\min_{z\in S_X}q(z),
\qquad
M(q)=\max_{z\in S_X}q(z).
\]
The squared distortion of this pullback is exactly \(M(q)/m(q)\).

For the lower bound, define two unit-ball vertices
\[
v_1=\left(\frac23,\frac23\right),
\qquad
v_2=(1,-1),
\]
and two boundary points
\[
z_1=\left(1,-\frac5{13}\right),
\qquad
z_2=\left(\frac5{13},-1\right).
\]
The points \(z_1\) and \(z_2\) lie respectively on the vertical edge joining \( (1,1/7)\) to \( (1,-1)\) and on the horizontal edge joining \( (1,-1)\) to \( (0,-1)\). A direct matrix identity is
\[
\frac4{13}v_1v_1^{\mathsf T}+\frac9{13}v_2v_2^{\mathsf T}
=
\frac{13}9\cdot\frac12
\left(z_1z_1^{\mathsf T}+z_2z_2^{\mathsf T}\right).
\]
Taking the trace after multiplication by the symmetric matrix representing any \(q\) gives
\[
\frac4{13}q(v_1)+\frac9{13}q(v_2)
=
\frac{13}9\cdot\frac{q(z_1)+q(z_2)}2.
\]
Because \(q(v_i)\le M(q)\) and \(q(z_i)\ge m(q)\), this forces
\[
M(q)\ge\frac{13}9m(q).
\]
Hence every linear isomorphism from \(X\) to a Euclidean plane has squared distortion at least \(13/9\).

For the matching upper bound, take
\[
q_*(x,y)=x^2+\frac{10}{13}xy+y^2.
\]
Its matrix has eigenvalues \(1\pm5/13\), so it is positive definite. Since \(q_*\) is convex, its maximum on the octagonal unit ball is attained at a vertex. The vertex values are
\[
1,\quad \frac{16}{13},\quad \frac{720}{637},\quad \frac{16}{13}
\]
on the four displayed vertices, and the opposite vertices give the same values. Thus
\[
M(q_*)=\frac{16}{13}.
\]
Minimizing \(q_*\) separately on the four boundary edges from \((0,1)\) to \((0,-1)\) through the right half of the polygon gives, in order,
\[
\frac{64}{65},\quad \frac{72}{65},\quad \frac{144}{169},\quad \frac{144}{169}.
\]
Central symmetry gives the same four minima on the opposite half, so
\[
m(q_*)=\frac{144}{169}.
\]
Therefore
\[
\frac{M(q_*)}{m(q_*)}
=
\frac{16/13}{144/169}
=
\frac{13}9.
\]
The lower and upper bounds coincide, proving the claim.

## Verification
The accompanying checker uses exact rational arithmetic. It reconstructs the eight vertices, verifies the matrix certificate for the universal lower bound, computes all vertex values of \(q_*\), minimizes the quadratic exactly on each edge, and checks that the resulting ratio is \(13/9\). Its successful output is `VERIFY_OK d2=13/9`.

## Relationship to prior work
Nilsrakoo and Saejung introduced generalized Day--James spaces and singled out exactly the above piecewise-linear \(\psi\) as an explicit normalized example whose sphere is an irregular octagon and which is not linearly isometric to any absolute normalized norm. Their paper studies James constants and uniform nonsquareness, not the Euclidean Banach--Mazur distance of this octagon. Alonso later showed that every two-dimensional normed space is isometrically isomorphic to a generalized Day--James space and classified that work under MSC 46B20. A later paper of Mitani, Saito, and Takahashi computes Banach--Mazur distances for classical \(\ell_p-\ell_q\) Day--James spaces in a parameter regime; its inspected theorem concerns those classical power norms, not this nonabsolute generalized octagon. Targeted database and exact-coefficient searches found no prior statement of the value \(\sqrt{13}/3\) for this example.

## Limitations
The result concerns this single canonical nonabsolute generalized Day--James octagon. It does not give a formula for arbitrary generalized Day--James planes, and it does not classify every optimal linear map. The originality assessment is based on targeted semantic, exact-expression, and literature searches; an unindexed specialist source could still contain the same affine invariant.

## References
1. W. Nilsrakoo and S. Saejung, “The James constant of normalized norms on \(\mathbb R^2\),” Journal of Inequalities and Applications, 2006, Article ID 26265, DOI 10.1155/JIA/2006/26265. Published 4 May 2006.
2. J. Alonso, “Any two-dimensional Normed space is a generalized Day-James space,” Journal of Inequalities and Applications 2011, Article 2, DOI 10.1186/1029-242X-2011-2.
3. K.-I. Mitani, K.-S. Saito, and Y. Takahashi, “Von Neumann-Jordan constant of \(\ell_p-\ell_q\) spaces,” RIMS Kôkyûroku 2041 (2017), 72–76.
