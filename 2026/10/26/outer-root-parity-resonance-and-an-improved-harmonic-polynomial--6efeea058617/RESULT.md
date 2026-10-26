# Outer-root parity resonance and an improved harmonic-polynomial valence bound

## Finding
For every pair of integers \(n>m\ge 1\), there exist complex polynomials \(p,q\) of degrees \(n,m\) for which the harmonic polynomial \(p(z)+\overline{q(z)}\) has at least
\[
R(n,m):=\min\{r\in\mathbb Z:r\ge n(1+\sqrt m),\ r\equiv n\pmod 2\}
\]
distinct zeros in the complex plane. In particular, \(R(77,5)=251\), while the historical Wilmshurst proposed value at these degrees is \(3(77)-2+5(5-1)=249\). Thus the assertion of equality to that proposed value fails already at fixed coanalytic degree \(5\).

A sharper probabilistic statement explains the improvement. Consider the Gaussian Kostlan polynomial and harmonic perturbation
\[
q_m(z)=\sum_{k=0}^{m}c_kz^k,\qquad
c_k\sim\mathcal N_{\mathbb C}(0,\tbinom mk)\ \text{independently},\qquad
H_{\varepsilon}(z)=\varepsilon z^n+q_m(z)+\overline{q_m(z)},
\]
where \(\varepsilon>0\) and the standard circular complex normal has mean-square magnitude one. Let \(Z_\varepsilon\) denote the number of distinct complex zeros of \(H_\varepsilon\). Then
\[
\boxed{\lim_{\varepsilon\downarrow0}\mathbb E Z_\varepsilon=n(1+\sqrt m).}
\]
Almost surely, the count is eventually constant for sufficiently small positive \(\varepsilon\), and its limiting decomposition is the count of finite real Kostlan roots on \(n\) lines plus a completely classified outer-root count.

Write \(d=n-m\). When \(d\) is odd, the outer count is exactly \(n\). When \(d\) is even, put
\[
g=\gcd\left(n,\frac{n+m}{2}\right),\qquad L=\frac n g.
\]
For even \(L\), the outer count is again exactly \(n\); for odd \(L\), it is \(n-g\) or \(n+g\), each with probability \(1/2\). Thus its mean is \(n\) in all cases, and its variance is \(g^2\) precisely in the even-\(d\), odd-\(L\) regime and zero otherwise. The finite and outer counts need not be independent; only linearity of expectation is used.

## Assumptions and scope
All zero counts are for distinct complex zeros. Almost-sure statements refer to the independent circular Gaussian coefficients \(c_k\). Each real-line polynomial used below has only simple roots almost surely for fixed \(\varepsilon>0\), and the limiting degree-\(m\) polynomials are almost surely squarefree with nonzero leading coefficients. The origin is almost surely not a zero of \(H_\varepsilon\), because \(H_\varepsilon(0)=2\operatorname{Re}c_0\ne0\). The assertion is existential for arbitrary degrees, not an explicit list of numerical coefficients for the degree-\((77,5)\) case. No fixed positive \(\varepsilon\) is claimed to work uniformly over all coefficient samples.

## Proof
**1. Exact line reduction.** The imaginary part of \(H_\varepsilon\) equals \(\varepsilon\operatorname{Im}(z^n)\). Therefore every zero lies on exactly one of the \(n\) distinct lines \(z=xe^{i\theta_j}\), with \(x\in\mathbb R\) and \(\theta_j=\pi j/n\) for \(0\le j<n\). Multiplying its real equation by \((-1)^j\) gives
\[
P_{\varepsilon,j}(x)=\varepsilon x^n+f_j(x),\qquad
f_j(x)=\sum_{k=0}^{m}b_{k,j}x^k,
\quad b_{k,j}=2(-1)^j\operatorname{Re}(c_ke^{ik\theta_j}).
\]
For each fixed \(j\), the \(b_{k,j}\) are independent centered real Gaussians with variances \(2\binom mk\), so \(f_j/\sqrt2\) is a standard real Kostlan polynomial. Distinct lines meet only at the origin, which is not a zero almost surely. Consequently \(Z_\varepsilon=\sum_{j=0}^{n-1}N_{\mathbb R}(P_{\varepsilon,j})\) almost surely, where \(N_{\mathbb R}\) counts distinct real roots.

**2. Root-count perturbation lemma.** Let \(f(x)=a_mx^m+\cdots+a_0\) have real coefficients, \(a_m\ne0\), and simple complex roots, and let \(n>m\). As \(\varepsilon\downarrow0\), each root of \(f\) persists as exactly one nearby root of \(f+\varepsilon x^n\); a simple real root remains real, and simple nonreal roots remain nonreal. For the remaining \(d=n-m\) roots set \(\tau=\varepsilon^{1/d}\), \(x=y/\tau\). Then
\[
\tau^mP_\varepsilon(y/\tau)
=y^n+a_my^m+\sum_{k=0}^{m-1}a_k\tau^{m-k}y^k
\longrightarrow y^m(y^d+a_m).
\]
By continuity of simple polynomial zeros (or Rouché's theorem on disjoint small circles around the nonzero limit roots), exactly one root converges to each nonzero solution of \(y^d=-a_m\). Those roots diverge in the original \(x\) coordinate, and their eventual number on the real axis is
\[
\eta_d(a_m)=\begin{cases}
1,& d\text{ odd},\\
2,&d\text{ even and }a_m<0,\\
0,&d\text{ even and }a_m>0.
\end{cases}
\]
This proves the eventual identity \(N_{\mathbb R}(f+\varepsilon x^n)=N_{\mathbb R}(f)+\eta_d(a_m)\). It applies simultaneously to all finitely many \(f_j\) almost surely. Genericity follows because their coefficient vectors have nonsingular Gaussian densities; a polynomial discriminant and its leading coefficient vanish only on proper algebraic null sets.

**3. Arithmetic resonance of the outer roots.** For \(d\) odd, every line contributes one outer root. For \(d\) even, write \(c_m=|c_m|e^{i\phi}\), where \(\phi\) is uniform modulo \(2\pi\), to obtain
\[
\operatorname{sgn}(b_{m,j})=\operatorname{sgn}\cos\left(\phi+\frac{\pi(n+m)j}{n}\right)
=\operatorname{sgn}\cos\left(\phi+\frac{2\pi k j}{n}\right),\qquad k=\frac{n+m}{2}.
\]
The \(n\) angles visit an equally spaced \(L=n/\gcd(n,k)\) point grid, each grid point repeated \(g\) times. A semicircle contains exactly \(L/2\) grid points when \(L\) is even. When \(L\) is odd, it contains either \((L-1)/2\) or \((L+1)/2\), with equal probabilities under uniform rotation \(\phi\); equality on a boundary has probability zero. Each negative leading coefficient contributes two exterior real roots. This establishes the stated two-point law, expectation and variance.

**4. Kostlan expectation and valence.** The covariance kernel of the normalized real Kostlan polynomial \(f_j/\sqrt2\) is \((1+xy)^m\). The one-dimensional Kac–Rice formula therefore gives real-zero intensity \(\sqrt m/[\pi(1+x^2)]\), and hence
\[
\mathbb E N_{\mathbb R}(f_j)=\int_{-\infty}^\infty \frac{\sqrt m}{\pi(1+x^2)}\,dx=\sqrt m.
\]
By Steps 1–3 the almost-sure limit \(Z_0:=\lim_{\varepsilon\downarrow0}Z_\varepsilon\) exists. Since \(0\le Z_\varepsilon\le n^2\) almost surely, dominated convergence yields
\[
\lim_{\varepsilon\downarrow0}\mathbb E Z_\varepsilon
=\sum_{j=0}^{n-1}\mathbb E N_{\mathbb R}(f_j)+\mathbb E(\text{outer count})
=n\sqrt m+n.
\]
For fixed \(\varepsilon>0\), each \(P_{\varepsilon,j}\) is a real polynomial of degree \(n\), with simple roots almost surely, so its number of real roots is congruent to \(n\) modulo \(2\). Thus \(Z_\varepsilon\equiv n^2\equiv n\pmod2\). By definition, \(R(n,m)-2<n(1+\sqrt m)\). For sufficiently small deterministic \(\varepsilon>0\), we have \(\mathbb E Z_\varepsilon>R(n,m)-2\). If every realization had \(Z_\varepsilon<R(n,m)\), the parity restriction would force \(Z_\varepsilon\le R(n,m)-2\) almost surely, a contradiction. A realization with at least \(R(n,m)\) distinct zeros therefore exists; take \(p(z)=\varepsilon z^n+q_m(z)\). At \((n,m)=(77,5)\), \(249<77(1+\sqrt5)<251\), the admissible parity is odd, and \(R(77,5)=251\).

## Verification
The supplied standalone `verification.py` checks six exact rational real-polynomial perturbation cases using Sturm root counts; it checks the parity-resonance outer-root counts for \(2\le n<45\), \(1\le m<n\), at five test phases per degree pair; and it checks the integer inequalities at \((77,5)\). The finite computations corroborate but are not used to infer the all-degree theorem. A separate simulation of small positive perturbations on moderate degrees is consistent with the limit, but near-colliding roots make finite-precision counts unreliable at large degrees. The analytical proof above uses only polynomial-root continuity, the exact Kostlan Kac–Rice intensity, and finite root bounds.

## Relationship to prior work
Lundberg, *The valence of harmonic polynomials viewed through the probabilistic lens* (initial public arXiv release 2022-01-03), introduced this exact random perturbation and obtained \(\lceil n\sqrt m\rceil\) zeros by preserving roots in bounded real intervals. The present theorem uses the roots escaping along those same lines; the arithmetic resonance law and the stronger \(n(1+\sqrt m)\) valence bound are not stated in that paper. Root escape under polynomial-degree perturbations is a standard mechanism and is not itself claimed as new. Khavinson–Lee–Saez (2018) provide distinct deterministic lower bounds and perturbative root-count methods, but not the present Gaussian phase-grid law or the stated universal strengthened expectation. Lee–Lerario–Lundberg (2015) and Hauenstein–Lerario–Lundberg–Mehta (2015) construct and count other harmonic-polynomial counterexamples, including in modest coanalytic degrees; the present finding does not claim those degree ranges were previously untouched. Kac–Rice and the real Kostlan expected zero count are classical. These comparisons do not establish exhaustive historical novelty, and independently developed equivalent statements remain possible.

## Limitations
The bound is existential and may be weaker than other constructions for particular \((n,m)\); it is not a formula for the actual maximal valence. In particular, no claim of a novel upper bound is made. The outer-root variance law describes only the count of roots escaping in the specified small-perturbation Gaussian ensemble, not the variance of the full valence count. The finite and outer components are correlated in general. The \(\varepsilon\downarrow0\) limit is not uniform in the Gaussian sample or in the degrees. Exact priority requires further specialist checking, especially in older literature on real-root escape and harmonic valence.

## References
1. E. Lundberg, *The valence of harmonic polynomials viewed through the probabilistic lens*, arXiv:2201.00788 (initial submission 2022-01-03), https://arxiv.org/abs/2201.00788 ; doi:10.1090/proc/16152.
2. D. Khavinson, S.-Y. Lee, and A. Saez, *Zeros of harmonic polynomials, critical lemniscates, and caustics*, Complex Analysis and its Synergies 4 (2018), doi:10.1186/s40627-018-0012-2, https://doi.org/10.1186/s40627-018-0012-2.
3. S.-Y. Lee, A. Lerario, and E. Lundberg, *Remarks on Wilmshurst's theorem*, Indiana Univ. Math. J. 64 (2015), 1153–1167, arXiv:1308.6474, https://arxiv.org/abs/1308.6474.
4. J. D. Hauenstein, A. Lerario, E. Lundberg, and D. Mehta, *Experiments on the zeros of harmonic polynomials using certified counting*, Experimental Mathematics 24 (2015), 133–141, https://academicweb.nd.edu/~jhauenst/preprints/hllmHarmonic.pdf.
5. A. Edelman and E. Kostlan, *How many zeros of a random polynomial are real?*, Bull. Amer. Math. Soc. 32 (1995), 1–37, https://math.mit.edu/~edelman/publications/how_many_zeros.pdf.
6. *On the average number of zeros of random harmonic polynomials with iid coefficients: precise asymptotics*, arXiv:2308.10333 (2023), https://arxiv.org/abs/2308.10333.
