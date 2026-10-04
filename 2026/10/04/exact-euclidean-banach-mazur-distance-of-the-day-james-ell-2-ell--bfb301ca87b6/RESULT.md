# Exact Euclidean Banach--Mazur distance of the Day--James \(\ell_2-\ell_1\) plane
## Finding
Let \(X=(\mathbb R^2,N)\) be the real Day--James plane with
\[
N(x,y)=\begin{cases}
\sqrt{x^2+y^2},&xy\ge 0,\\
|x|+|y|,&xy\le 0.
\end{cases}
\]
Then
\[
d_{\mathrm{BM}}(X,\ell_2^2)^2=C_{\mathrm{NJ}}(X)=\frac32.
\]
An optimal Euclidean pullback norm is, up to a positive scalar factor,
\[
|(x,y)|_*^2=\frac{(x+y)^2+2(x-y)^2}{2}.
\]
Thus \(d_{\mathrm{BM}}(X,\ell_2^2)=\sqrt{3/2}\).

## Assumptions and scope
The scalar field is real and the dimension is exactly two. The Banach--Mazur distance is
\[
d_{\mathrm{BM}}(X,\ell_2^2)=\inf_T\|T\|\,\|T^{-1}\|,
\]
where the infimum ranges over invertible real linear maps \(T:X\to\ell_2^2\). For a positive-definite quadratic form \(q\), define
\[
R_q(z)=\frac{q(z)}{N(z)^2}\qquad(z\ne0).
\]
The squared distortion associated with \(q(z)=\|Tz\|_2^2\) is
\[
\frac{\sup R_q}{\inf R_q}.
\]
No assertion is made for general Day--James \(\ell_p-\ell_q\) spaces.

## Proof
Put
\[
u=\frac{x+y}{\sqrt2},\qquad v=\frac{x-y}{\sqrt2}.
\]
Since \(xy=(u^2-v^2)/2\), the norm becomes
\[
N(u,v)^2=\begin{cases}
u^2+v^2,&|u|\ge |v|,\\
2v^2,&|v|\ge |u|.
\end{cases}
\]
The two formulas agree on \(|u|=|v|\).

It remains to justify that an arbitrary linear isomorphism may be reduced to a one-parameter quadratic form. Let \(S(x,y)=(y,x)\). The norm \(N\) is invariant under \(S\). Suppose a positive-definite quadratic form \(q\) satisfies
\[
mN(z)^2\le q(z)\le MN(z)^2\qquad(z\in\mathbb R^2).
\]
Then the averaged form
\[
\bar q(z)=\frac{q(z)+q(Sz)}2
\]
satisfies the same two inequalities. Hence averaging cannot increase the ratio \(M/m\). The matrix of \(\bar q\) commutes with \(S\), so in the \((u,v)\)-coordinates it is diagonal. After an irrelevant positive rescaling, every averaged candidate therefore has the form
\[
q_t(u,v)=u^2+tv^2\qquad(t>0).
\]
Thus the global Banach--Mazur minimization, including all linear isomorphisms, reduces without loss to minimizing the distortion of \(q_t\).

On the sector \(|u|\ge|v|\), set \(r=|v/u|\in[0,1]\). Then
\[
\frac{q_t}{N^2}=\frac{1+tr^2}{1+r^2},
\]
whose endpoint values are \(1\) and \((1+t)/2\). On the sector \(|v|\ge|u|\), set \(s=|u/v|\in[0,1]\). Then
\[
\frac{q_t}{N^2}=\frac{s^2+t}{2},
\]
whose endpoint values are \(t/2\) and \((1+t)/2\). Consequently
\[
D(t):=\frac{\sup R_{q_t}}{\inf R_{q_t}}
=\frac{\max\{1,t/2,(1+t)/2\}}{\min\{1,t/2,(1+t)/2\}}.
\]
Elementary ordering of the three terms gives
\[
D(t)=\begin{cases}
2/t,&0<t\le1,\\
1+1/t,&1\le t\le2,\\
(1+t)/2,&t\ge2.
\end{cases}
\]
The unique minimum of this reduced problem is \(D(2)=3/2\). Therefore
\[
d_{\mathrm{BM}}(X,\ell_2^2)^2=\frac32,
\]
and \(q_2=u^2+2v^2\) supplies the stated optimal pullback norm.

For the von Neumann--Jordan constant, choosing \(x=(1,0)\) and \(y=(0,1)\) gives
\[
\frac{N(x+y)^2+N(x-y)^2}{2(N(x)^2+N(y)^2)}=\frac{2+4}{4}=\frac32,
\]
so \(C_{\mathrm{NJ}}(X)\ge3/2\). Conversely, for any Euclidean pullback satisfying \(mN^2\le q\le MN^2\), the parallelogram identity for \(q\) gives \(C_{\mathrm{NJ}}(X)\le M/m\). Taking the infimum over pullbacks and using the exact Banach--Mazur value yields \(C_{\mathrm{NJ}}(X)\le3/2\). Hence equality holds.

## Verification
The proof is exact and symbolic. The all-isomorphism step is the averaging argument for arbitrary positive-definite quadratic forms, not an assumption that the optimal ellipse is axis-aligned. The two sectors \(|u|\ge|v|\) and \(|v|\ge|u|\) exhaust \(\mathbb R^2\), including their common boundary, and the ratio extrema on each sector occur at the displayed endpoints because each ratio is monotone in the squared sector parameter. No finite experiment is used to infer the global optimum.

## Relationship to prior work
Kato, Maligranda, and Takahashi introduce this exact Day--James \(\ell_2-\ell_1\) norm as Example 2 and later develop Banach--Mazur stability inequalities for geometric constants. Their Section 5 gives comparison inequalities involving \(d(X,Y)\), while their Day--James discussion records only bounds for the constants and poses a broader constant-computation problem; the inspected full text does not state the exact Euclidean Banach--Mazur distance for this plane. Dinarvand later records the exact known value \(C_{\mathrm{NJ}}(\ell_2-\ell_1)=3/2\), identifies its dual Day--James plane, and again uses Banach--Mazur distance only for stability inequalities in the inspected material. The finding here is the exact affine distance and an explicit optimal Euclidean pullback; the equality with \(C_{\mathrm{NJ}}\) follows from the same proof.

Semantic searches for the Day--James plane together with “Banach--Mazur distance,” “ellipsoid,” and the candidate value did not locate a prior exact-distance statement. Those negative searches are supporting evidence only and are not treated as a proof of novelty.

## Limitations
The result concerns one canonical two-dimensional Day--James norm. It does not compute Banach--Mazur distances for general \(\ell_p-\ell_q\) spaces and does not classify every optimal isomorphism; it gives an optimal representative obtained after symmetry averaging. A residual bibliographic risk remains that an older specialist source or table not exposed by the searched databases contains the same exact affine distance.

## References
1. M. Kato, L. Maligranda, and Y. Takahashi, “On James and Jordan--von Neumann constants and the normal structure coefficient of Banach spaces,” *Studia Mathematica* 144 (2001), 275--295. DOI: 10.4064/sm144-3-5.
2. M. Dinarvand, “Heinz means and triangles inscribed in a semicircle in Banach spaces,” *Mathematical Inequalities & Applications* 22 (2019), 275--290. DOI: 10.7153/MIA-2019-22-21.
