# Exact opposite-corner heat-kernel separation on the reflecting square

## Finding
Let \(Q=[0,1]^2\) and let \(P_t=e^{t\Delta_N}\) be the Neumann heat semigroup, normalized with generator \(\Delta\) (not \(\Delta/2\)). For \(t>0\), let \(\mu_t^{00}\) and \(\mu_t^{11}\) be its probability kernels from \((0,0)\) and \((1,1)\). Define
\[D(t)=\sup_{A\subset Q}|\mu_t^{00}(A)-\mu_t^{11}(A)|.\]
The (essentially unique) maximizing measurable set is the strict lower triangle \(A_*=\{(u,v)\in Q:u+v<1\}\), or its complement for the reversed signed difference. For \(a_k(t)=e^{-\pi^2 k^2 t}\),
\[
\boxed{D(t)=\frac{16}{\pi^2}\left(\sum_{\substack{k\ge1\\k\text{ odd}}}\frac{a_k(t)}{k^2}-2\sum_{\substack{k\ge1\text{ odd}\\\ell\ge2\text{ even}}}\frac{a_k(t)a_\ell(t)}{\ell^2-k^2}\right).}
\]
The sums converge absolutely for every \(t>0\). The first mixed mode creates an intermediate exponential rate:
\[D(t)=\frac{16}{\pi^2}e^{-\pi^2t}-\frac{32}{3\pi^2}e^{-5\pi^2t}+O(e^{-9\pi^2t}),\quad t\to\infty.\]
The opposite, short-time regime exhibits the diagonal geometric barrier
\[1-D(t)\sim 8\sqrt{\frac2\pi}\,\sqrt t\,\exp\!\left(-\frac1{8t}\right),\qquad t\downarrow0.\]
This identifies one natural two-point total-variation benchmark for reflecting-square mixing. It **does not determine** the supremum over arbitrary pairs of starting locations.

## Assumptions and scope
The Neumann Laplacian is self-adjoint on \(L^2(Q)\), with reflection on all four sides and Lebesgue stationary probability. Its heat kernel is a product of one-dimensional reflected heat kernels. Total variation is normalized as half the \(L^1\) distance of probability densities, equivalently the maximum signed probability difference. Boundary starts are defined through the continuous heat kernel. The same formulas for a square of side length \(L>0\) follow after replacing \(t\) by \(t/L^2\).

## Proof
**1. One-dimensional strict likelihood-ratio ordering.** For \(x,z\in[0,1]\) let
\[p_t(x,z)=1+2\sum_{k\ge1}e^{-\pi^2k^2t}\cos(k\pi x)\cos(k\pi z).\]
The one-dimensional Neumann heat kernel is strictly totally positive of order two: if \(x_1<x_2\), \(z_1<z_2\), and \(t>0\), then
\[p_t(x_1,z_1)p_t(x_2,z_2)>p_t(x_1,z_2)p_t(x_2,z_1).\]
For completeness, the determinant on the left minus the right is the heat kernel for two independent reflected diffusions killed upon collision, on the wedge \(0<z_1<z_2<1\). It solves \(\partial_t h=(\partial_{z_1}^2+\partial_{z_2}^2)h\) with zero boundary data on the diagonal and Neumann conditions at the two outer sides. Its initial restriction to the wedge is the nonnegative point mass at \((x_1,x_2)\); the strong maximum principle, followed by continuity for endpoint starts, gives strict positivity. This is the classical Karlin–McGregor determinant argument, with the boundary conditions explicit.

Put \(p(z)=p_t(0,z)\), \(q(z)=p_t(1,z)\). Both are strictly positive, and \(p(z)=q(1-z)\) by reflection. Thus \(r(z)=\log(p(z)/q(z))\) is strictly decreasing and obeys \(r(1-z)=-r(z)\).

**2. Exact sign region.** Product separation is
\[p(u)p(v)-q(u)q(v)=q(u)q(v)\left(e^{r(u)+r(v)}-1\right).\]
By strict monotonicity and odd reflection, \(r(u)+r(v)>0\) exactly when \(u<1-v\). The densities agree only on the diagonal \(u+v=1\), which has area zero; hence the lower triangle is the unique sign-positive TV extremal event. A half-turn of the square interchanges the two corner laws and maps the triangle to its complement. Consequently,
\[D(t)=2\int_0^1p(u)\int_0^{1-u}p(v)\,dv\,du-1.\]

**3. Double Fourier evaluation.** Expand \(p(u)p(v)\) and integrate over the triangle. Direct antiderivatives give, for positive integers \(k,\ell\),
\[\int_{u+v<1}\cos(k\pi u)\,du\,dv=\frac{1-(-1)^k}{\pi^2k^2},\]
and
\[\int_{u+v<1}\cos(k\pi u)\cos(\ell\pi v)\,du\,dv=
\begin{cases}
\displaystyle\frac{2(-1)^{\ell+1}}{\pi^2(\ell^2-k^2)},& k+\ell\text{ odd},\\[3pt]
0,&k+\ell\text{ even}.
\end{cases}\]
The denominator is never zero in the odd-parity case. Pairing \((k,\ell)\) and \((\ell,k)\) yields the stated absolutely convergent double series. The two smallest spectral exponents present are \(1\) and \(5=1^2+2^2\), followed by \(9\). This proves the long-time expansion.

**4. Short-time expansion.** The image representation at a reflecting corner identifies each coordinate, up to the first crossing of the opposite boundary, with the absolute value of a centered Gaussian \(N(0,2t)\). A coupling with these unfolded Gaussian variables shows that replacing the two reflected coordinates by \((|B_1|,|B_2|)\), independent \(B_i\sim N(0,2t)\), changes probabilities by at most \(O(\sqrt t\,e^{-1/(4t)})\): only \(|B_i|>1\) can differ. Thus
\[1-D(t)=2\mathbb P(|B_1|+|B_2|>1)+O(\sqrt t\,e^{-1/(4t)}).\]
By quadrant symmetry and the orthogonal change \(U=(B_1+B_2)/\sqrt2\), \(V=(B_1-B_2)/\sqrt2\), the relevant first-quadrant event is \(U>1/\sqrt2\), \(|V|<U\). As \(U,V\) are independent \(N(0,2t)\), dropping \(|V|<U\) changes the probability by at most the product of two Gaussian tails, exponentially smaller than the main term. Hence
\[1-D(t)=8\Phi\!\left(-\frac1{2\sqrt t}\right)(1+o(1))\sim8\sqrt{\frac2\pi}\,\sqrt t\,e^{-1/(8t)},\]
where \(\Phi\) denotes the standard-normal distribution function. The stated normalization and constants follow.

## Verification
Run the standalone file `verify.py` with Python 3 (standard library only). It compares the double Fourier formula with direct one-dimensional quadrature of the triangular probability, checks positivity of the sign pattern on interior sample points, and displays short- and long-time scaling. These finite calculations are consistency tests, not the justification for the infinite sum, global sign region, or asymptotics; those are proved above.

## Relationship to prior work
Karlin and McGregor's total-positivity framework gives the strict ordering input. Kolokoltsov's stochastic-monotonicity analysis treats ordered one-dimensional Markov kernels. Gaubert and Qu identify the abstract Dobrushin/Hopf oscillation norm. Loper's full-text theorem bounds total variation for reflected Brownian motion in **any** convex domain by a diameter-dependent one-dimensional survival function; its one-dimensional lower-bound argument gives the exact interval benchmark but does **not** evaluate the two-dimensional opposite-corner event or its mixed Fourier exponent. In the square, the upper bound from that theorem uses the diameter \(\sqrt2\) and has exponential scale \(e^{-\pi^2t/2}\), while the explicitly evaluated opposite-corner distance has scale \(e^{-\pi^2t}\). Thus the general upper bound is not an exact evaluation of this fixed-pair invariant.

## Limitations
No universal square Dobrushin coefficient (supremum over **all** pairs of starts) is asserted. In dimensions three and higher, the zero set of the product likelihood ratio generally need not be a plane, so the diagonal argument is special to two dimensions. No claim of independent verification or exhaustive historical novelty is made; an equivalent unindexed corner-pair evaluation is a residual risk. The 1960 original total-positivity report was identifiable by bibliographic record but its full text was not available through the retrieval route used here.

## References
1. S. Karlin and J. McGregor, *Classical Diffusion Processes and Total Positivity*, Stanford technical report KAR NSF 1 (January 1960), https://statistics.stanford.edu/technical-reports/classical-diffusion-processes-and-total-positivity.
2. V. Kolokoltsov, *Stochastic monotonicity and duality for one-dimensional Markov processes*, arXiv:1002.4773v1 (25 February 2010), https://arxiv.org/abs/1002.4773.
3. S. Gaubert and Z. Qu, *Dobrushin ergodicity coefficient for Markov operators on cones, and beyond*, arXiv:1302.5226v1 (21 February 2013), https://arxiv.org/abs/1302.5226.
4. J. Loper, *Uniform Ergodicity for Brownian Motion in a Bounded Convex Set*, Journal of Theoretical Probability, first online 31 July 2018, https://doi.org/10.1007/s10959-018-0848-7.
