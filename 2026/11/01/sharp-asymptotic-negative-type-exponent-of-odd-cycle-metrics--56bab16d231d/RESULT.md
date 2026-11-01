# Sharp asymptotic negative-type exponent of odd cycle metrics

## Finding

For each odd integer \(N\ge5\), let \(d_N(a,b)=\min\{|a-b|,N-|a-b|\}\) denote shortest-path distance on the cycle \(\mathbb Z/N\mathbb Z\). Define its supremal negative-type exponent by
\[
\beta_N=\sup\bigl\{s\ge0:\ \sum_{a,b\in\mathbb Z/N\mathbb Z}c_a c_b d_N(a,b)^s\le0\quad\text{for every real }(c_a)\text{ with }\sum_a c_a=0\bigr\}.
\]
Then, as \(N\to\infty\) through odd integers,
\[
\boxed{\lim N^2(\beta_N-1)=\frac{2\pi^2}{\displaystyle\int_0^{2\pi}\frac{1-\cos u}{u}\,du}
=\frac{2\pi^2}{\gamma+\log(2\pi)-\operatorname{Ci}(2\pi)}
=8.09762735686653\ldots.}
\]
More precisely, writing \(C\) for this constant, for every fixed \(0<c<C\), the powered metric \(d_N^{1+c/N^2}\) is conditionally negative definite for all sufficiently large odd \(N\); for every fixed \(c>C\), it is not conditionally negative definite for all sufficiently large odd \(N\). The novel assertion is the lower, all-Fourier-mode half, not merely the previously known single-mode upper obstruction.

## Assumptions and scope

The kernel is the unweighted graph shortest-path metric of an odd simple cycle. Fourier modes are indexed \(1\le k\le (N-1)/2\). All asymptotics take \(N\) odd; constants \(c\) are fixed independently of \(N\). We do not assert that the exact finite-\(N\) supremal exponent equals the zero of one specified Fourier mode.

## Proof

**1. Fourier criterion and second differences.** Set \(N=2m+1\), \(\alpha=1+\delta\) and
\[
F_{N,k}(\alpha)=2\sum_{r=1}^{m}r^\alpha\cos(2\pi kr/N),\qquad 1\le k\le m.
\]
The real circulant powered-distance matrix is conditionally negative semidefinite exactly when \(F_{N,k}(\alpha)\le0\) for every nonzero Fourier frequency. Put
\[
a=m^\alpha-(m-1)^\alpha,\quad
b_r=(r+1)^\alpha-2r^\alpha+(r-1)^\alpha\quad(1\le r<m),
\]
where \(0^\alpha=0\). For \(\delta>0\), \(b_r\ge0\) and \(\sum_{r<m}b_r=a-1\). Taking a discrete second difference of the periodic sequence \(d_N(0,r)^\alpha\) yields the exact identity
\[
-4\sin^2(\pi k/N)F_{N,k}(\alpha)
=2+2\sum_{r=1}^{m-1}b_r\cos(2\pi kr/N)
 -2a(-1)^k\cos(\pi k/N).
\tag{1}
\]
For odd \(k\), half the right side is at least \(2-a+a\cos(\pi k/N)>0\) once \(a<2\). Consequently all odd Fourier multipliers are negative.

For even \(k\), (1) equals twice
\[
H_{N,k}=a[1-\cos(\pi k/N)]
 -\sum_{r=1}^{m-1}b_r[1-\cos(2\pi kr/N)].
\tag{2}
\]
Thus positivity of \(H_{N,k}\) for all even \(k\) proves conditional negative definiteness.

**2. The high even modes.** Fix \(c>0\) and \(\delta=c/N^2\). From the mean-value theorem, \(a-1=O(c\log N/N^2)\). As \(\sum b_r=a-1\) and \(0\le1-\cos\theta\le2\), (2) and \(1-\cos(\pi k/N)\ge2k^2/N^2\), valid for \(1\le k\le m\), give
\[
H_{N,k}\ge\frac{2k^2}{N^2}-O\left(\frac{c\log N}{N^2}\right).
\]
Uniformly over every even \(k\ge\lceil\log N\rceil\), the right side is strictly positive for sufficiently large \(N\).

**3. Uniform asymptotics for low even modes.** Let \(B_r=(r+1)\log(r+1)-2r\log r+(r-1)\log(r-1)\), interpreting \(0\log0=0\). Taylor's theorem, or the triangular-kernel integral for second differences, gives for \(r\ge2\)
\[
b_r=\delta B_r+O\left(\delta^2\frac{(1+\log r)^2}{r}\right),\qquad
B_r=\frac1r+O(r^{-3}),
\]
with the \(r=1\) case bounded separately. The total remainder is \(O(\delta^2\log^3N)\). For \(1\le k\le\lceil\log N\rceil\), the bound \(1-\cos x\le x^2/2\) and a Riemann sum with uniformly \(O(k^2)\)-Lipschitz integrand yield
\[
\sum_{r=1}^{m-1}B_r[1-\cos(2\pi kr/N)]
=J_k+O\left(\frac{k^2}{N}+\frac{k^2\log N}{N^2}\right),
\quad J_k=\int_0^{\pi k}\frac{1-\cos u}{u}\,du.
\]
Also \(N^2a[1-\cos(\pi k/N)]=\pi^2 k^2/2+o(1)\) uniformly on this range. Inserting \(\delta=c/N^2\) in (2), we conclude
\[
\boxed{N^2H_{N,k}=\frac{\pi^2k^2}{2}-cJ_k+o(1)}
\tag{3}
\]
uniformly over all low even modes.

**4. The second mode dominates the scaled obstruction.** Write an even integer \(k=2j\). Using \(|\sin(jv/2)|\le j|\sin(v/2)|\) pointwise,
\[
J_{2j}=\int_0^{2\pi}\frac{1-\cos(jv)}v\,dv
\le j^2\int_0^{2\pi}\frac{1-\cos v}v\,dv
=\frac{k^2}4J_2.
\tag{4}
\]
The strict positivity \(J_2>0\) follows directly from the integral. Set \(C=2\pi^2/J_2\). If \(c<C\), (3)–(4) give the uniform strict bound
\[
N^2H_{N,k}\ge\frac{k^2}{4}(2\pi^2-cJ_2)+o(1)>0
\]
for every low even \(k\). Combined with steps 1–2, all nonconstant powered-distance Fourier multipliers are strictly negative for sufficiently large odd \(N\). In particular \(\beta_N\ge1+c/N^2\).

If \(c>C\), take \(k=2\). Equation (3) gives \(N^2H_{N,2}=2\pi^2-cJ_2+o(1)<0\), so (1) gives \(F_{N,2}(1+c/N^2)>0\); conditional negative definiteness fails. The classical downward-closure of negative type exponents (for example, by the integral representation of fractional powers of a conditionally negative kernel) implies \(\beta_N\le1+c/N^2\). Since \(c<C\) and \(c>C\) can approach \(C\) arbitrarily closely, the claimed limit follows.

## Verification

Run the accompanying standalone standard-library program with `python verify_cycle.py`. It checks the exact finite discrete-Laplacian identity numerically for all modes of nine odd cycle sizes and several exponents; separately, it checks strict all-mode negativity below, and positive second-mode obstruction above, the predicted scale for four larger sizes. It reports 1,598 passed finite checks. The infinite asymptotic theorem follows from the uniform estimates in steps 1–4, not from this finite test set. The constant \(J_2\) is evaluated in the program by the absolutely convergent entire series for its integral.

## Relationship to prior work

Horak, LaRose, Moore, Rooney and Rosenthal establish exact ordinary *roundness* formulas for cycle graph metrics and convergence of those ordinary-roundness exponents to one. Ordinary roundness is distinct from the supremal negative-type/generalized-roundness exponent here. Wolf and Sánchez develop the negative-type gap and supremal-exponent framework; Sánchez treats cycles, including explicit low-order calculations. A previously documented computation of the *second Fourier multiplier alone* already gave the same constant \(C\) as an upper obstruction and explicitly did **not** prove that all other Fourier modes remained nonpositive. The new step here is the uniform all-mode inequality (2)–(4), upgrading that single-mode obstruction to the exact asymptotic supremal negative-type exponent. The same constant is therefore not independently claimed as a newly calculated constant.

## Limitations

This is an odd-order large-size asymptotic statement. It does not identify \(\beta_N\) exactly for every finite odd \(N\), prove exact finite-order dominance of mode two, or give higher-order corrections. Mathematical verification is self-review only; independent mathematical validation has not been performed. An earlier equivalent all-mode asymptotic argument may exist in literature not inspected exhaustively.

## References

- M. Horak, E. LaRose, J. Moore, M. Rooney, H. Rosenthal, *Roundness properties of graphs*, Involve 3 (2010), 67–91. https://doi.org/10.2140/involve.2010.3.67 ; full text https://msp.org/involve/2010/3-1/involve-v3-n1-p05-p.pdf .
- R. Wolf, *On the gap of finite metric spaces of p-negative type* (public preprint dated 2010-08-05), https://arxiv.org/abs/1008.0964v1 .
- S. Sánchez, *On the supremal p-negative type of a finite metric space* (public preprint dated 2011-08-02), https://arxiv.org/abs/1108.0451v1 .
