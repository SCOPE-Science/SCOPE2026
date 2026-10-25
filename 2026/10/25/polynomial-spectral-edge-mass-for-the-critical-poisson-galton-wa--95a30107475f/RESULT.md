# Polynomial spectral-edge mass for the critical Poisson Galton–Watson tree

## Finding

Let \(\mathcal T\) be a critical Poisson\((1)\) Galton–Watson tree. For a Borel set \(B\subseteq[0,\infty)\), define
\[
\sigma_1(B)=\mathbb E\!\left[|V(\mathcal T)|^{-1}\operatorname{Tr}\mathbf 1_B(\Delta_{\mathcal T})\right],
\]
where \(\Delta_{\mathcal T}=D-A\) is the combinatorial graph Laplacian. There are constants \(c,E_0>0\) such that
\[
\sigma_1((0,E])\ge cE^{3/2}\qquad(0<E<E_0).
\]
In particular, no \(c_0>0\) can satisfy
\[
\sigma_1((0,E])\le \exp(-c_0E^{-1/2})
\]
for every sufficiently small \(E\).

## Assumptions and scope

The offspring distribution is Poisson with mean one, so extinction occurs almost surely and \(\mathcal T\) is finite almost surely. The Laplacian is the unnormalised combinatorial Laplacian of the finite tree. The measure is defined by the expected normalised trace; equivalently, conditional on the total progeny, the root is uniform among vertices and the expected root spectral measure equals the normalised trace. The result concerns this critical tree-law spectral measure. It does not assert a separate convergence theorem for the zero-eigenvalue mass of finite Erdős–Rényi graphs.

## Proof

Write \(N=|V(\mathcal T)|\). If \(F(z)=\mathbb E[z^N]\), the branching recursion for Poisson\((1)\) offspring gives \(F(z)=z\exp(F(z)-1)\). Lagrange inversion yields
\[
\Pr(N=n)=[z^n]F(z)=\frac1n[u^{n-1}]\exp(n(u-1))
=\frac{e^{-n}n^{n-1}}{n!}.
\]
Stirling's formula therefore gives constants \(a_1,a_2>0\) and \(n_0\) such that
\[
a_1n^{-3/2}\le \Pr(N=n)\le a_2n^{-3/2}\qquad(n\ge n_0).
\]

Conditional on \(N=n\), a Poisson Galton–Watson tree, after forgetting child order and assigning labels uniformly, is a uniform rooted Cayley tree. By label symmetry its root is uniform among the vertices. The finite-variance conditioned Galton–Watson height theorem implies that the height divided by \(\sqrt n\) converges in distribution to a nondegenerate positive limit. Hence there exist \(a,p_0>0\) and \(n_1\) such that
\[
\Pr\!\left(H(\mathcal T)\ge a\sqrt n\mid N=n\right)\ge p_0
\qquad(n\ge n_1).
\]
The diameter \(d\) is at least the height.

For any finite tree \(T\) of diameter \(d\ge1\), choose a diameter path \(v_0,\ldots,v_d\). Define \(f(v_i)=i\), and extend \(f\) constantly to every component attached to \(v_i\) after the path edges are removed. Its Dirichlet energy is
\[
\sum_{\{x,y\}\in E(T)}(f(x)-f(y))^2=d.
\]
Its variance around the global mean is bounded below by the contribution of the path vertices:
\[
\sum_{x\in V(T)}(f(x)-\bar f)^2
\ge \min_{z\in\mathbb R}\sum_{i=0}^{d}(i-z)^2
=\frac{d(d+1)(d+2)}{12}.
\]
The Rayleigh–Ritz principle consequently gives
\[
\lambda_2(\Delta_T)\le\frac{12}{(d+1)(d+2)}\le\frac{12}{d^2}.
\]

On the event \(H(\mathcal T)\ge a\sqrt n\), this implies
\[
\lambda_2(\Delta_{\mathcal T})\le \frac{K}{n},
\qquad K=\frac{12}{a^2}.
\]
Thus whenever \(n\ge K/E\), that event forces at least one positive eigenvalue into \((0,E]\). The normalised trace of the spectral projection on \((0,E]\) is then at least \(1/n\). Summing over total progeny gives, for sufficiently small \(E>0\),
\[
\begin{aligned}
\sigma_1((0,E])
&\ge p_0\sum_{n\ge\lceil K/E\rceil}\frac{\Pr(N=n)}{n}\\
&\ge a_1p_0\sum_{n\ge\lceil K/E\rceil}n^{-5/2}
\ge cE^{3/2}
\end{aligned}
\]
for some \(c>0\). Since \(E^{3/2}\exp(c_0E^{-1/2})\to\infty\) as \(E\downarrow0\), this lower bound rules out any upper bound of the form \(\exp(-c_0E^{-1/2})\) with \(c_0>0\). This proves the claim.

## Verification

The total-progeny formula follows directly from the branching generating-function identity and Lagrange inversion. The only asymptotic inputs are Stirling's formula and the finite-variance conditioned-tree height theorem. The spectral estimate is a Rayleigh quotient calculation with an explicit test function; no numerical experiment is used. All constants are existential and depend on the height-limit event. The argument proves a lower bound only, not a matching upper bound or an exact asymptotic.

## Relationship to prior work

Heydenreich, Müller and Terveer prove a lower-edge Lifshitz-tail result for the supercritical Poisson Galton–Watson spectral measure and explicitly note that the critical case is not studied in their paper. Khorunzhiy, Kirsch and Müller establish the corresponding Lifshitz-tail theorem for subcritical Erdős–Rényi graphs with mean parameter strictly below one; their theorem does not cover the critical value. Kersting's conditioned-tree height theorem supplies the \(\sqrt n\)-scale geometric input used here. The present claim is a critical-parameter polynomial lower bound for the tree-law spectral measure, not a full description of the critical finite-graph integrated density of states.

## Limitations

The exponent \(3/2\) is a proved lower-bound exponent, not an asserted exact asymptotic. No upper bound for \(\sigma_1((0,E])\) is established. The constants are not made explicit. The result does not settle whether the positive spectral mass of finite Erdős–Rényi graph Laplacians converges with the same zero-atom convention at criticality.

## References

1. M. Heydenreich, P. Müller and S. Terveer, “Return probability on Bienaymé–Galton–Watson trees and spectral asymptotics of sparse Erdős–Rényi random graphs,” arXiv:2603.00344, first submitted 27 February 2026.
2. G. Kersting, “On the Height Profile of a Conditioned Galton-Watson Tree,” arXiv:1101.3656.
3. O. Khorunzhiy, W. Kirsch and P. Müller, “Lifshitz tails for spectra of Erdős–Rényi random graphs,” Annals of Applied Probability 16 (2006), 295–309; arXiv:math-ph/0502054.
