# Exact and unique fastest diffusion on two-price even cycles

## Finding

Let \(m\ge2\) be an integer, let \(B,c_A,c_B>0\), and let \(C_{2m}\) have vertices \(0,1,\ldots,2m-1\) in cyclic order. The edge \(\{j,j+1\}\) (indices modulo \(2m\)) has price \(c_A\) when \(j\) is even and \(c_B\) when \(j\) is odd. Independently assign a nonnegative conductance \(w_j\) to every edge, subject to the exact budget \(\sum_{j\text{ even}}c_Aw_j+\sum_{j\text{ odd}}c_Bw_j=B\). Let \(L(w)\) be the weighted graph Laplacian and \(\lambda_2(L(w))\) its second-smallest eigenvalue, counting multiplicities.

Put
\[
\tau=\frac{\pi}{m},\qquad d=\cos\tau,\qquad
\Delta=c_A+c_B+2\sqrt{c_Ac_B}\,d.
\]
The **unique** globally optimal conductances, even when the \(2m\) edges are all independent decision variables, are alternating:
\[
\boxed{\begin{aligned}
w_{2j}=a_*&=\frac{B}{m}\frac{c_A+\sqrt{c_Ac_B}\,d}{c_A\Delta},\\
w_{2j+1}=b_*&=\frac{B}{m}\frac{c_B+\sqrt{c_Ac_B}\,d}{c_B\Delta}
\end{aligned}\quad (0\le j<m).}
\]
Their exact maximal spectral gap is
\[
\boxed{\sup_{w_j\ge0,\,\sum c_jw_j=B}\lambda_2(L(w))=
\frac{2B\sin^2(\pi/m)}{m\left(c_A+c_B+2\sqrt{c_Ac_B}\cos(\pi/m)\right)}.}
\]
In particular, on the four-cycle \(m=2\) one has \(a_*=b_*\) irrespective of the price contrast. For every \(m>2\), \(a_*>b_*\) exactly when \(c_A<c_B\). For fixed distinct prices, \(a_*/b_*\) moves strictly away from one as \(m\) increases and converges to \(\sqrt{c_B/c_A}\). At fixed total budget,
\[
\lambda_2^*\sim\frac{2B\pi^2}{m^3(\sqrt{c_A}+\sqrt{c_B})^2}\qquad(m\to\infty).
\]

## Assumptions and scope

The graph is the simple undirected even cycle of order at least four. Prices are strictly positive, constant on each alternating edge class; conductances may independently vanish, but no self-loops or other edges are offered. The total expenditure is fixed and positive. The objective is the **continuous-time** symmetric Markov mixing rate, equivalently the algebraic connectivity of the unnormalized weighted Laplacian: the associated process has generator \(-L(w)\). This is not the discrete-time second-largest-eigenvalue-modulus problem, and the conductances are not probabilities constrained by row sums. The optimum is unique as a labelled edge vector, not merely unique modulo symmetry.

## Proof

**1. A simultaneous upper bound for arbitrary conductances.** Define \(A=\sqrt{c_A}\), \(D=\sqrt{c_B}\), and choose the unique \(\alpha\in(0,\tau)\) satisfying
\[
\frac{\sin\alpha}{\sin(\tau-\alpha)}=\frac{A}{D}.
\]
Existence and uniqueness follow because \(\sin\alpha/\sin(\tau-\alpha)\) increases strictly from zero to infinity on that interval; the case \(m=2\) is included. Write \(\beta=\tau-\alpha\). Direct trigonometry gives
\[
\sin\alpha=\frac{A\sin\tau}{\sqrt\Delta},\quad
\sin\beta=\frac{D\sin\tau}{\sqrt\Delta},\quad
\cos\alpha=\frac{D+A\cos\tau}{\sqrt\Delta},\quad
\cos\beta=\frac{A+D\cos\tau}{\sqrt\Delta}.
\]
Set \(R=\sqrt\Delta/(2\sin\tau)\), and place \(2m\) vectors in the plane at
\[
X_{2j}=R(\cos(2j\tau),\sin(2j\tau)),\qquad
X_{2j+1}=R(\cos(2j\tau+2\alpha),\sin(2j\tau+2\alpha)).
\]
Because each parity class is a set of \(m\) equally spaced points, \(\sum_iX_i=0\). Moreover, successive chords have squared lengths exactly \(4R^2\sin^2\alpha=c_A\) and \(4R^2\sin^2\beta=c_B\). If \(X\) is the \(2m\)-by-two matrix of their coordinates, then for **every** feasible (possibly asymmetric and partially zero) conductance vector,
\[
\operatorname{tr}(X^{\mathsf T}L(w)X)
=\sum_j w_j\|X_j-X_{j+1}\|^2=B,
\qquad \operatorname{tr}(X^{\mathsf T}X)=2mR^2.
\]
The two columns of \(X\) are orthogonal to the constant vector. The variational definition of the second Laplacian eigenvalue gives
\[
\lambda_2(L(w))\operatorname{tr}(X^{\mathsf T}X)
\le\operatorname{tr}(X^{\mathsf T}L(w)X),
\]
so \(\lambda_2(L(w))\le B/(2mR^2)=2B\sin^2\tau/(m\Delta)\). This is a direct dual/geometric bound; no symmetry assumption about the unknown optimizer was used.

**2. A positive allocation attaining the bound.** The displayed \(a_*,b_*\) are strictly positive and satisfy \(m(c_Aa_*+c_Bb_*)=B\). The four trigonometric identities above imply
\[
a_*\sin(2\alpha)=b_*\sin(2\beta).
\]
At every even or odd vertex, this identity cancels the tangential component of the two incident edge forces in the plane. The remaining radial component is
\[
a_*(1-\cos(2\alpha))+b_*(1-\cos(2\beta))
=2a_*\sin^2\alpha+2b_*\sin^2\beta
=\frac{c_Aa_*+c_Bb_*}{2R^2}
=\frac{B}{2mR^2}=:\Lambda.
\]
Thus \(L(w_*)X=\Lambda X\). To confirm that this is the *second* eigenvalue rather than a higher one, use the Bloch decomposition by rotations through two vertices. The complete multiset of eigenvalues of an alternating-rate even cycle is
\[
\lambda_\pm(k)=a_*+b_*\pm\sqrt{a_*^2+b_*^2+2a_*b_*\cos(2\pi k/m)},
\qquad k=0,1,\ldots,m-1.
\]
Here \(\lambda_-(0)=0\), and the smallest strictly positive eigenvalue is \(\lambda_-(1)=\lambda_-(m-1)\) (only one copy when \(m=2\)). The two planar coordinates use the first Bloch frequency. They belong to its *lower* branch because
\[
a_*\cos(2\alpha)+b_*\cos(2\beta)
=\frac{a_*\sin(2\tau)}{\sin(2\beta)}\ge0,
\]
where equality occurs only for \(m=2\). Therefore \(\lambda_2(L(w_*))=\Lambda\), establishing the claimed optimal value.

**3. Uniqueness among all edge assignments.** Suppose another feasible vector \(v\) attains \(\lambda_2(L(v))=\Lambda\). The upper bound in step 1 is an equality. As \(L(v)-\Lambda(I-\mathbf1\mathbf1^{\mathsf T}/(2m))\) is positive semidefinite, equality of its quadratic-form traces against \(X\) forces *both* columns of \(X\) into its kernel. Hence \(L(v)X=\Lambda X\). At each vertex \(i\), this vector equation is
\[
v_{i-1}(X_i-X_{i-1})+v_i(X_i-X_{i+1})=\Lambda X_i.
\]
The two displayed edge displacement vectors are linearly independent: three distinct points on a circle cannot be collinear. Therefore the ordered pair \((v_{i-1},v_i)\) is uniquely determined by this equation. The constructed optimal rates satisfy every equation, so \(v=w_*\) edge by edge. This also proves uniqueness at both equal-price and four-cycle boundaries.

**4. Price contrast and size.** With \(d=\cos(\pi/m)\),
\[
\frac{a_*}{b_*}
=\sqrt{\frac{c_B}{c_A}}\,
\frac{\sqrt{c_A}+\sqrt{c_B}d}{\sqrt{c_B}+\sqrt{c_A}d}.
\]
As \(m\) rises from two, \(d\) rises strictly from zero to one. The derivative of this ratio with respect to \(d\) has the sign of \(c_B-c_A\). The limit is \(\sqrt{c_B/c_A}\). Expanding sine and cosine at zero gives the displayed fixed-budget spectral-gap asymptotic.

## Verification

The accompanying `verify.py` checks symbolic budget and characteristic-polynomial identities, exact full Laplacian spectra in the four- and six-vertex cases (using several distinct positive rational prices), and 842 asserted algebraic/full-matrix/numerical conditions overall. Numerical checks include every edge-chord length, both planar eigenvector equations, independent-edge feasible competitors, and the sharp spectral-gap formula on cycles through 24 vertices. Execute `python verify.py` with Python 3, NumPy and SymPy available. This finite sample is not an exhaustive argument; the proof in steps 1–4 covers all orders and all positive real parameters.

## Relationship to prior work

Sun, Boyd, Xiao, and Diaconis formulated continuous-time fastest mixing as a weighted-budget semidefinite optimization problem, proved a general maximum-variance-unfolding dual, solved equal-cost cycles, and noted that arbitrary-cost cycles are more complicated. In particular, their Result 6 proves a two-dimensionality statement for optimal cycle configurations; neither their result nor the equal-cost calculation gives the present explicit period-two tariff formula or labelled-edge uniqueness. The upper bound in step 1 deliberately uses their established geometric viewpoint, rather than presenting it as new. Boyd, Diaconis, Parrilo, and Xiao developed discrete-time symmetry reductions and solved the standard uniform-cost cycle under a different mixing objective. The contribution here is the complete exact solution, with a global uniqueness proof, of the continuously optimized two-price family under arbitrary independent edge allocations.

## Limitations

The scope is limited to alternating **two-class** prices on even cycles. Neither arbitrary (nonperiodic) edge prices nor the discrete-time fastest-mixing problem is resolved. The numerical script supplies additional checks but not the infinite-family proof. Although the most directly relevant primary full texts and focused searches were examined, unindexed or otherwise inaccessible results could contain an equivalent period-two specialization.

## References

1. J. Sun, S. Boyd, L. Xiao, and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699, DOI: 10.1137/S0036144504443821. Full text: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf (published electronically 2 November 2006).
2. S. Boyd, P. Diaconis, P. A. Parrilo, and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, preprint dated 6 September 2007, arXiv:0709.0955, published in SIAM Journal on Optimization 20 (2009), 792–819. Full text: https://arxiv.org/pdf/0709.0955. Its discrete-time eigenvalue-modulus objective differs from the continuous-time spectral-gap objective here.
