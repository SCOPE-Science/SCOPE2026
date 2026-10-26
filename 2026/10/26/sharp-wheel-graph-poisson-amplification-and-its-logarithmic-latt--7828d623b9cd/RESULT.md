# Sharp wheel-graph Poisson amplification and its logarithmic lattice phase

## Finding
For each integer \(m\ge3\), let \(W_{m+1}=K_1\vee C_m\) be the unweighted wheel with \(m\) rim vertices and one hub, and let \(G_m=L(W_{m+1})^\dagger\) be its unnormalized graph-Laplacian Moore--Penrose inverse, acting on all vertex functions with counting-measure \(\ell^1\) or \(\ell^\infty\) norms. Put
\[
q=\frac{3-\sqrt5}{2},\qquad \alpha=\log(1/q),\qquad c_m=\frac{m+2}{(m+1)^2},\qquad a_{m,d}=\frac{q^d+q^{m-d}}{\sqrt5(1-q^m)}\quad(0\le d<m).
\]
The exact, attained endpoint norms are
\[
\boxed{\|G_m\|_{\infty\to\infty}=\|G_m\|_{1\to1}=2\sum_{d=0}^{m-1}(a_{m,d}-c_m)_+.}
\]
For \(m\ge4\), every maximizing row is a rim row, not the hub row; for \(m=3\), all four rows tie and the norm is \(3/8\). In a maximizing rim row the positive Green entries are exactly those with \(a_{m,d}>c_m\). A sign vector matching that row attains the norm.

A sharper structural result describes the second-order defect. Define
\[
T_m=\frac{\log(m/\sqrt5)}{\alpha},\qquad u_m=\{T_m\}\in[0,1),\qquad
\Phi(u)=2-4u+\frac{4q^{1-u}}{1-q}.
\]
Then, uniformly as integer \(m\to\infty\),
\[
\boxed{\|G_m\|_{\infty\to\infty}=2-\frac{1}{m}\left[\frac4\alpha\log\left(\frac m{\sqrt5}\right)+\Phi(u_m)\right]+O(m^{-2}).}
\]
The function \(\Phi\) extends continuously to the circle since \(\Phi(0)=\Phi(1^-)=2\sqrt5\), but is nonconstant. Put
\[
u_*=1+\frac1\alpha\log\left(\frac{1-q}{\alpha}\right)\in(0,1).
\]
For \(D_m=m(2-\|G_m\|_{\infty\to\infty})-4\log(m/\sqrt5)/\alpha\), the **exact accumulation interval** is
\[
\boxed{\left[\Phi(u_*),\ 2\sqrt5\right],\qquad
\Phi(u_*)=2-4u_*+\frac4\alpha\approx3.9969901378.}
\]
In particular, \(m(2-\|G_m\|)/\log m\to4/\alpha\); there is no constant second term after the logarithmic correction. This phase effect arises from the integer jump of the sign-changing radius of the Green kernel.

## Assumptions and scope
The wheel has unit weights on all rim edges and spokes; the rim cycle is the simple cycle of length \(m\ge3\). The Laplacian is \(L=D-A\), with no normalization by degrees or vertex count. The pseudoinverse annihilates the constant function. The norms above are unrestricted matrix-induced norms, **not** operator norms on a separately renormed mean-zero input subspace. Real or complex inputs give the same constants. Positive-part notation is \((t)_+=\max(t,0)\). No assertion is made for weighted wheels, other joins, or other input exponents.

## Proof
**1. Exact Green matrix.** Order rim vertices first and the hub last, and set \(B=I+L(C_m)=3I-S-S^{-1}\), where \(S\) is the cyclic shift. Split the vertex space orthogonally into the rim mean-zero subspace, the span of \((1,\ldots,1,-m)\), and the constant subspace. The Laplacian restricts to \(B\) on the first summand, has eigenvalue \(m+1\) on the second, and vanishes on the third. Consequently, with \(J\) the all-ones rim matrix,
\[
G_m=\begin{pmatrix}B^{-1}-c_mJ&-(m+1)^{-2}\mathbf1\\-(m+1)^{-2}\mathbf1^T&m(m+1)^{-2}\end{pmatrix}.
\]
The infinite-line inverse of \(3I-S-S^{-1}\) has coefficients \(q^{|d|}/\sqrt5\): these satisfy \(3b_d-b_{d-1}-b_{d+1}=\mathbf1_{d=0}\) because \(q+q^{-1}=3\) and \(q^{-1}-q=\sqrt5\). Periodizing yields \((B^{-1})_{0d}=a_{m,d}\). This derivation is also an independent verification of the boundary terms for all \(m\ge3\).

**2. Exact endpoint norm and extremizers.** Every row of \(G_m\) sums to zero. Its hub row has positive diagonal and negative off-diagonals, hence absolute row sum \(2m/(m+1)^2\). In a rim row the hub entry is negative and the positive entries are exactly \(a_{m,d}-c_m>0\). By zero row sum its absolute row sum equals twice the sum of these positive entries, as displayed. For \(m\ge4\), \(a_{m,0}>1/\sqrt5>2/(m+1)\), so the rim norm exceeds the hub norm; when \(m=3\) one checks directly that both are \(3/8\). Symmetry gives equality of \(\ell^1\) and \(\ell^\infty\) norms. At a selected rim vertex, choose input signs equal to the signs of its Green row (arbitrary signs at zero entries); its output attains the sharp absolute row sum. The same works with any common unimodular complex phase.

**3. Exponential-to-logarithmic threshold.** Let \(\delta_m(d)=\min(d,m-d)\), and let \(b_{m,d}=q^{\delta_m(d)}/\sqrt5\). The periodization formula and the geometric series show
\[
\sum_{d=0}^{m-1}|a_{m,d}-b_{m,d}|=O(q^{m/2}).
\]
Also \(c_m=1/m-1/[m(m+1)^2]\), so the Lipschitz property of positive part gives
\[
2\sum_d(a_{m,d}-c_m)_+=2\sum_d(b_{m,d}-1/m)_++O(q^{m/2}+m^{-2}).
\]
For all sufficiently large \(m\), the positive surrogate entries lie at the distinct cyclic distances \(0,1,\ldots,k_m\), where \(k_m=\lfloor T_m\rfloor<m/2\); if equality occurs at the terminal distance, including the corresponding zero term changes nothing. Summing the two geometric tails, using \((1+q)/(\sqrt5(1-q))=1\), gives
\[
2\sum_d(b_{m,d}-1/m)_+=2-\frac{4q^{k_m+1}}{\sqrt5(1-q)}-\frac{2(2k_m+1)}m.
\]
Since \(k_m=T_m-u_m\) and \(q^{T_m}=\sqrt5/m\), substitution proves the stated expansion with a uniform \(O(m^{-2})\) error.

**4. Sharp accumulation interval.** The derivative \(\Phi'(u)=-4+4\alpha q^{1-u}/(1-q)\) is strictly increasing on \([0,1]\), negative at zero and positive at one. Thus \(\Phi\) has the unique minimum \(u_*\), while equal endpoint values give the maximum \(2\sqrt5\). The phases \(\{\log(m/\sqrt5)/\alpha\}\) are dense in \([0,1]\): given \(u\in(0,1)\), the integers nearest to \(\sqrt5e^{\alpha(j+u)}\) realize phases tending to \(u\); one-sided approximations handle zero and one. Continuity and the uniform error prove that the accumulation set of \(D_m\) is the claimed whole interval.

## Verification
Run `python3 verify.py` from the directory containing that standalone file. It independently constructs rational wheel Laplacians, computes exact rational pseudoinverses as \((L+J/(m+1))^{-1}-J/(m+1)\), verifies all Green entries and row sums for rim sizes \(3\) through \(17\), and checks the sharp-row reduction. Additional independent Fourier calculations and logarithmic-phase comparisons test larger sizes. The checker reports 2,336 passed exact-entry and numerical/asymptotic checks. Numerical tests do not establish the asymptotic theorem; Steps 1--4 above do.

## Relationship to prior work
Yang (2012) computes exact resistance distances and random-walk hitting times on wheel graphs, not the unrestricted sharp induced \(\ell^\infty\) norm or its logarithmic phase. Ipsen and Mallik (2022, arXiv:2201.02579, especially Theorem 3.6) explicitly derive the wheel Laplacian pseudoinverse; its full kernel is therefore **prior mathematics**, and no novelty is asserted for that matrix formula. What is asserted here is the global sharp absolute-row optimization, the logarithmic cutoff, the uniform second-order phase expansion, and the full nondegenerate accumulation interval. The previously studied sharp Poisson norms of cycles and Cartesian-product graph families do not dominate the wheel result: the wheel has an apex vertex and a massive spectral gap, and its relevant positive-entry radius grows logarithmically rather than linearly. A separate known wheel edge-gradient projection norm is an operator on edges, not this vertex Poisson inverse; its dependence on a few extremal inverse-circulant entries does not provide the sign-tail sum or the phase law.

## Limitations
The result concerns only unweighted wheels and unrestricted endpoint operator norms. It says nothing about all weighted wheels, general graph joins, or \(\ell^p\) spaces with \(1<p<\infty\). The exact formula uses a positive-part sum rather than an elementary piecewise expression for every finite \(m\), but it is explicit and finite. The second-order phase is proved to uniform order \(m^{-2}\), not to all asymptotic orders. Earlier full Green-kernel formulas substantially reduce the algebra needed here; the claimed contribution is the sharp sign threshold and its logarithmic-phase consequences. Historical priority requires independent checking, especially against literature using the alternative terms Green-function Lebesgue constant or maximum-principle stability.

## References
1. Y. Yang, *Simple random walks on wheel graphs*, Applied Mathematics & Information Sciences 6 (2012), 123S--128S; published online 2012-01-01. https://www.naturalspublishing.com/files/published/90uo7hk8rzs133.pdf
2. J. Ipsen and S. Mallik, *Incidence and Laplacian matrices of wheel graphs and their inverses*, arXiv:2201.02579 (2022), especially Corollary 3.3 and Theorem 3.6. https://arxiv.org/abs/2201.02579
3. H. Zhang and Y. Yang, *Resistance distance and Kirchhoff index in circulant graphs*, International Journal of Quantum Chemistry 107 (2007), 330--339; first published 2006-09-05. https://doi.org/10.1002/qua.21068
