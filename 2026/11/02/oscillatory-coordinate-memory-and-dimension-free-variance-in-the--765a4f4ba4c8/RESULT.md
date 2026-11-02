# Oscillatory coordinate memory and dimension-free variance in the twisted baker map

## Finding
For every integer \(M\ge 2\), consider the twisted baker map introduced by Saiki, Takahasi and Yorke, with normalized Lebesgue initial distribution. Write \(Z_k=F^kZ_0\), and let \(f(Z)=Z_1\) be the first *spatial* coordinate, whose stationary mean is zero. Its lag-\(n\) autocovariance \(C_n=\mathbb E[f(Z_0)f(Z_n)]\), for \(n\ge0\), has the **exact rational generating function**
\[
\boxed{\displaystyle
\sum_{n\ge0}C_nz^n
=\frac13\frac{(1-z/2)^{M-1}}
{(1-z/4)(1-z/2)^{M-1}+z^M/2^{M+1}}.}
\]
All its finite complex poles are nonreal; the covariance sequence takes strictly positive and strictly negative values infinitely often. Nonetheless its entire positive-lag sum cancels exactly:
\[
\boxed{\quad C_1=\frac1{12},\qquad \sum_{n\ge1}C_n=0.\quad}
\]
Furthermore, for every fixed \(M\ge2\),
\[
\boxed{\displaystyle
\frac1{\sqrt N}\sum_{k=0}^{N-1}f(Z_k)
\ \Longrightarrow\ \mathcal N(0,1/3),\qquad
\lim_{N\to\infty}\frac1N\operatorname{Var}\left(\sum_{k=0}^{N-1}f(Z_k)\right)=\frac13.}
\]
Thus the long-run variance of this physical coordinate equals its one-time variance in *every* dimension, although adjacent observations are positively correlated and later correlations repeatedly change sign. This combination is explained by an explicit martingale--coboundary decomposition.

## Assumptions and scope
Fix an integer \(M\ge2\), and write \(X=[-1,1]\times[0,1]^{M-1}\), endowed with \(m=(1/2)\operatorname{Leb}_M\). The one-step map is
\[
F(x_1,\ldots,x_M)=
\begin{cases}
(1+2x_1,x_2,\ldots,x_M),&x_1<0,\\
(1-2x_M,x_1,\ldots,x_{M-1}),&x_1\ge0.
\end{cases}
\]
The boundary convention is immaterial to \(m\)-almost-sure statements. Each branch covers \(X\) and has absolute Jacobian determinant two, so \(m\) is invariant. Ergodicity (indeed mixing) for \((F,m)\) is established in Saiki--Takahasi--Yorke, Theorem D. Throughout, expectations and limits refer to \(Z_0\sim m\) and one-step physical time (not a return section). A dimension \(M\) is fixed when \(N\to\infty\); no dimension-uniform central limit theorem is asserted.

## Proof
**1. Adjoint transfer action.** The two inverse branches at a point \(y\in X\) are
\[
G_Ly=((y_1-1)/2,y_2,\ldots,y_M),\qquad
G_Ry=(y_2,\ldots,y_M,(1-y_1)/2).
\]
Consequently the Lebesgue adjoint of the Koopman operator is
\(P\varphi(y)=\tfrac12\varphi(G_Ly)+\tfrac12\varphi(G_Ry)\).
Use centered coordinates \(u_1(x)=x_1\) and \(u_j(x)=x_j-1/2\) for \(2\le j\le M\). Direct substitution gives
\[
Pu_1=\tfrac14u_1+\tfrac12u_2,\quad
Pu_j=\tfrac12(u_j+u_{j+1})\ (2\le j<M),\quad
Pu_M=-\tfrac14u_1+\tfrac12u_M.
\]
Let \(B_M\) denote the row-coefficient matrix of these identities in basis \((u_1,\ldots,u_M)\); specifically its first row has entries \((1/4,1/2,0,\ldots,0)\), rows \(2,\ldots,M-1\) have two consecutive \(1/2\)'s on the diagonal and superdiagonal, and the last row has entries \((-1/4,0,\ldots,0,1/2)\). Since the coordinates are independent under \(m\), \(\int u_1u_j\,dm=\delta_{1j}/3\). The adjoint identity \(\int v(w\circ F^n)\,dm=\int(P^nv)w\,dm\) therefore gives
\[
C_n=\frac13(B_M^n)_{11}.
\]
A cofactor calculation on \(I-zB_M\) yields
\[
\det(I-zB_M)=(1-z/4)(1-z/2)^{M-1}+\frac{z^M}{2^{M+1}},
\]
while its principal minor obtained by deleting row and column one is \((1-z/2)^{M-1}\). The resolvent identity \(\sum_{n\ge0}(zB_M)^n=(I-zB_M)^{-1}\) proves the asserted generating function, first as a formal series and subsequently in its convergence disk.

**2. Decay and sign changes.** Every eigenvalue \(\lambda\) of \(B_M\) obeys
\[
(\lambda-1/4)(\lambda-1/2)^{M-1}=-2^{-(M+1)}.
\]
If \(|\lambda|\ge1\), the left side has absolute value at least \((3/4)(1/2)^{M-1}=3\cdot2^{-(M+1)}\), a contradiction. Thus \(\rho(B_M)<1\) and \(\sum_{n\ge0}|C_n|<\infty\).

Set \(w=2\lambda-1\). The characteristic equation becomes
\[
(2w+1)w^{M-1}=-1.
\]
For real \(w\ge0\) or \(w\le-1/2\) with even \(M\), the product on the left is nonnegative. For \(-1/2<w<0\), its absolute value is strictly less than one. Hence even \(M\) admits no real eigenvalues. For odd \(M\), the exponent \(M-1\) is even: the only real solution is \(w=-1\) (on \(w<-1/2\) the equation \((2|w|-1)|w|^{M-1}=1\) has the unique solution \(|w|=1\)). This is the eigenvalue \(\lambda=0\). The denominator and numerator of the generating function have no common finite zero: the numerator vanishes only at \(z=2\), where the denominator equals \(1/2\). Thus all its **finite poles** come from nonzero, nonreal eigenvalues. Its radius of convergence is finite because it has at least one such pole. If its coefficients were eventually all nonnegative, subtracting the finite initial polynomial would produce a nonpolynomial power series with nonnegative coefficients but no singularity at its positive radius of convergence, contradicting Pringsheim's theorem. Apply the same argument to the negated tail to rule out eventual nonpositivity. Therefore infinitely many \(C_n\) are positive and infinitely many are negative.

**3. Exact cancellation.** Evaluating the generating function at \(z=1\), permitted because \(\rho(B_M)<1\), gives
\[
\sum_{n\ge0}C_n=\frac13\frac{2^{-(M-1)}}{(3/4)2^{-(M-1)}+2^{-(M+1)}}=\frac13=C_0.
\]
Also \(C_1=\frac13(B_M)_{11}=1/12\), proving the positive-lag cancellation is nontrivial.

**4. Martingale mechanism and central limit.** Define the bounded function
\[
h(x)=\sum_{j=2}^M(x_j-1/2),\qquad
d(x)=\begin{cases}x_1,&x_1<0,\\x_M,&x_1\ge0.\end{cases}
\]
Checking the two branches separately gives the pointwise identity
\[
\boxed{\quad f=d+h\circ F-h.\quad}
\]
Moreover \(d(G_Ly)=(y_1-1)/2\) and \(d(G_Ry)=(1-y_1)/2\), so \(Pd=0\) **pointwise**. The two halves of \(X\) each have \(m\)-mass \(1/2\). Integrating their squared conditional values gives \(\int d\,dm=0\), \(\int d^2\,dm=(1/2)(1/3)+(1/2)(1/3)=1/3\).

The process \(d\circ F^k\) consists of bounded reverse martingale differences for the decreasing filtration \(F^{-k}\mathcal B\), because \(\mathbb E[d\circ F^k\mid F^{-(k+1)}\mathcal B]=(Pd)\circ F^{k+1}=0\). Ergodicity of \((F,m)\) and boundedness give the conditional quadratic-variation limit by Birkhoff's theorem and the martingale central limit theorem. Consequently \(N^{-1/2}\sum_{k=0}^{N-1}d\circ F^k\) converges to \(\mathcal N(0,1/3)\). The exact telescoping equality
\[
\sum_{k=0}^{N-1}f\circ F^k
=\sum_{k=0}^{N-1}d\circ F^k+h\circ F^N-h
\]
has a uniformly bounded remainder for each fixed \(M\), proving the claimed central limit. Orthogonality of distinct reverse martingale differences and the bounded remainder imply the variance limit \(1/3\) as well. Equivalently, absolute covariance summability and the identity in Step 3 give the Green--Kubo value \(C_0+2\sum_{n\ge1}C_n=1/3\).

For orientation, when \(M=2\), with \(\cos\vartheta=3/4\) and \(\sin\vartheta=\sqrt7/4\), the result specializes to
\[
C_n=\frac1{3\,2^n}\left(\cos(n\vartheta)-\frac{\sin(n\vartheta)}{\sqrt7}\right),
\]
which displays the oscillatory behavior explicitly.

## Verification
The standalone `CHECK.py` independently partitions the *forward physical map* into exact-rational itinerary rectangles, integrates the first-coordinate product on those rectangles, and compares it with matrix predictions for dimensions \(M=2,3,4,5\) and horizons \(0\le n\le9\). It also tests the pointwise martingale--coboundary identity and conditional transfer cancellation across dimensions \(2\le M\le19\). Execute with `python CHECK.py` using the Python standard library only. The checker reports 346 successful exact equalities and sample covariance lists. This finite test validates normalization, branch order and explicit algebraic specializations, but **does not replace** the all-dimension cofactor proof, the nonreal-pole argument or the ergodic martingale central limit theorem.

## Relationship to prior work
Saiki, Takahasi and Yorke [1] define exactly this full-branch twisted baker map; their Theorems A--D concern hyperbolic periodic-point spectra, density, equidistribution and mixing, and their coding establishes a Bernoulli representation. Those results justify ergodicity here but do not state the physical-coordinate correlation generating function, Green--Kubo cancellation or dimension-independent asymptotic variance. A separately published exact real-spectrum residue law [2] concerns eigenvalues of *iterate Jacobians at periodic points*, not the transfer action on coordinate observables, stationary correlations or martingale decomposition; matching the word "spectrum" does not make the statements equivalent. General martingale--coboundary central limit theory [3] supplies the last implication once the present explicit transfer identity is established, rather than supplying the identity or its coefficient. Work on heterochaos baker maps [4] studies a different piecewise-affine family with different center dynamics and does not imply these exact coordinate formulas.

## Limitations
This result is specific to the map [1], its normalized Lebesgue law and the first physical coordinate. It does not establish a global spectral gap on unspecified transfer-operator function spaces; the computed eigenvalues describe the finite-dimensional invariant linear-observable subspace and the poles of *this* coordinate correlation function. No dimension-uniform Gaussian approximation, a statement for nonstationary initial laws, or a claim about arbitrary observables is made. Standard martingale central limit theory is invoked, not reproduced in full. Possible earlier equivalent formulas derived within general baker-map methods remain a publication-priority risk; a finite index search cannot establish absolute novelty.

## References
1. Y. Saiki, H. Takahasi and J. A. Yorke, *The twisted baker map*, arXiv:2202.04304, first publicly posted 2022-02-09; Nonlinearity 36 (2023), 1776--1788, DOI 10.1088/1361-6544/acb4d3. In particular map definition (1.1)--(1.3) and Theorems A--D.
2. *Exact real-spectrum residue law for the twisted baker map*, published-finding corpus public research record, 2026-10-11, identifier `2026/10/11/SCOPE-exact-real-spectrum-residue-law-for-the-twisted-baker-map--f1bd1c74fb3b`, public result at https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-real-spectrum-residue-law-for-the-twisted-baker-map--f1bd1c74fb3b/.
3. M. I. Gordin, *The central limit theorem for stationary processes*, Soviet Math. Dokl. 10 (1969), 1174--1176 (martingale-coboundary method).
4. H. Takahasi, *Exponential mixing for heterochaos baker maps and the Dyck system*, arXiv:2307.08119 (first posted 2023-07-16), cited for contextual distinction, not for a conclusion about the present model.
