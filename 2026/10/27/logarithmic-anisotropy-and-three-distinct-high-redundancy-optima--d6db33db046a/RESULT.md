# Logarithmic anisotropy and three distinct high-redundancy optima for an exponential Gabor window

## Finding

Consider the unit-norm two-sided exponential window \(g(t)=e^{-|t|}\) and the rectangular integer-density Gabor lattice \(\Lambda_{n,\eta}=(\eta/n)\mathbb Z\times\eta^{-1}\mathbb Z\), where \(n\ge2\) is an integer and \(\eta>0\). Let \(A_n(\eta),B_n(\eta)\) be the sharp lower and upper frame bounds, and let \(\kappa_n(\eta)=B_n(\eta)/A_n(\eta)\). A common positive normalization of the two bounds does not alter any of the three optimization problems.

Denote by \(\eta_{A,n}\) the unique maximizer of the lower bound, by \(\eta_{B,n}\) the unique minimizer of the upper bound, and by \(\eta_{K,n}\) the unique minimizer of \(\kappa_n\). Put \(L_n=2\log n\). As \(n\to\infty\),

\[
\begin{aligned}
\eta_{B,n}&=L_n+\log3+O(L_n^3/n^2),\\
\eta_{K,n}&=L_n+\log4+O(L_n^3/n^2),\\
\eta_{A,n}&=L_n+\log6+O(L_n^3/n^2).
\end{aligned}
\]

Consequently, the optimal lattice parameters are asymptotically strongly anisotropic, and their persistent optimality gaps satisfy
\[
\lim_{n\to\infty}(\eta_{K,n}-\eta_{B,n})=\log(4/3),\qquad
\lim_{n\to\infty}(\eta_{A,n}-\eta_{K,n})=\log(3/2).
\]

Writing \(u_n=L_n+\log4\), the sharp minimum condition number obeys
\[
\min_{\eta>0}\kappa_n(\eta)
=1+\frac{u_n^2/2+u_n+1}{n^2}
+O\!\left(\frac{L_n^4}{n^4}\right).
\]

For comparison, the square lattice has \(\eta=\sqrt n\) and
\[
\kappa_n(\sqrt n)=1+\frac1{2n}+O(n^{-2}+\sqrt n\,e^{-\sqrt n}).
\]
Therefore its excess condition number divided by the optimally achievable excess satisfies
\[
\frac{\kappa_n(\sqrt n)-1}{\min_{\eta>0}\kappa_n(\eta)-1}
\sim\frac{n}{4(\log n)^2}.
\]

More strongly, this optimization is governed by a universal three-objective boundary layer. Define the positive functions \(a_n,b_n\) in the next section, and put \(k_n=b_n/a_n\). Uniformly for \(c\) in each compact real interval,
\[
\begin{aligned}
\frac{n^2}{L_n}[a_n(L_n+c)-a_n(L_n)]&\longrightarrow 2-\frac c3-2e^{-c},\\
\frac{n^2}{L_n}[b_n(L_n+c)-b_n(L_n)]&\longrightarrow \frac{2c}3+2e^{-c}-2,\\
\frac{n^2}{L_n}[k_n(L_n+c)-k_n(L_n)]&\longrightarrow c+4e^{-c}-4.
\end{aligned}
\]
Each limiting profile has exactly one optimizer of the appropriate type, respectively at \(\log6\), \(\log3\), and \(\log4\).

## Assumptions and scope

Use the Fourier transform \(\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-2\pi i\xi t}\,dt\) and the standard Gabor system \(\{e^{2\pi ikt/\eta}g(t-m\eta/n):k,m\in\mathbb Z\}\). The lattice density is the positive integer \(n\), the window is fixed, and optimization is over all positive rectangular aspect parameters \(\eta\). The known exact frame-bound expressions, after removing a common positive factor that depends only on \(n\), are
\[
\begin{aligned}
 a_n(\eta)&=\tanh(\eta/2)\left[\frac\eta n\,\operatorname{csch}(\eta/n)-\eta\,\operatorname{csch}\eta\right],\\
 b_n(\eta)&=\coth(\eta/2)\left[\frac\eta n\,\coth(\eta/n)+\eta\,\operatorname{csch}\eta\right].
\end{aligned}
\]
They have exactly the same extremizing parameters and condition number as the physical frame bounds: \(\kappa_n=b_n/a_n\). The existence, uniqueness and global character of the three extrema follow from Faulhuber–Shafkulovska, Theorem 2.7 and Section 8, and are used as established input rather than asserted to be newly proved here. The novelty claimed here is the high-density boundary-layer law, its three distinct additive constants, and the sharp square-lattice conditioning gap.

## Proof

Set \(L=L_n=2\log n\), let \(\eta=L+c\), and let \(c\) vary in a fixed compact real interval. Then \(z=e^{-\eta}=e^{-c}/n^2\) and \(x=\eta/n\to0\). The convergent Taylor expansions
\[
\begin{aligned}
 x\operatorname{csch}x&=1-x^2/6+7x^4/360+O(x^6),\\
 x\coth x&=1+x^2/3-x^4/45+O(x^6),\\
 \tanh(\eta/2)&=(1-z)/(1+z)=1-2z+O(z^2),\\
 \coth(\eta/2)&=(1+z)/(1-z)=1+2z+O(z^2),\\
 \eta\operatorname{csch}\eta&=2\eta z/(1-z^2)
\end{aligned}
\]
are uniform on every such interval, together with their first two derivatives in \(\eta\). Substitution gives, with remainders bounded by \(O(L^4/n^4)\),
\[
\begin{aligned}
 a_n(\eta)&=1-\frac{\eta^2}{6n^2}-2(\eta+1)e^{-\eta}+O(L^4/n^4),\\
 b_n(\eta)&=1+\frac{\eta^2}{3n^2}+2(\eta+1)e^{-\eta}+O(L^4/n^4),\\
 k_n(\eta)&=1+\frac{\eta^2}{2n^2}+4(\eta+1)e^{-\eta}+O(L^4/n^4).
\end{aligned}
\]
The same remainder bound applies after one differentiation. Thus
\[
\begin{aligned}
 a_n'(L+c)&=\frac{L+c}{n^2}\left(-\tfrac13+2e^{-c}\right)+O(L^4/n^4),\\
 b_n'(L+c)&=\frac{L+c}{n^2}\left(\tfrac23-2e^{-c}\right)+O(L^4/n^4),\\
 k_n'(L+c)&=\frac{L+c}{n^2}\left(1-4e^{-c}\right)+O(L^4/n^4).
\end{aligned}
\]
For each of the three objectives the coefficient in parentheses changes sign once, respectively at \(c=\log6\), \(c=\log3\), and \(c=\log4\). Fix a small positive \(\varepsilon\). For sufficiently large \(n\), the derivatives at \(L+c_*\pm\varepsilon\) have opposite signs. For sufficiently large \(n\), both test points lie inside the interval used in the cited Section 8 uniqueness proof, where the lower-bound logarithm is strictly concave and the condition-number logarithm is strictly convex; the upper bound is globally strictly convex. Each derivative sign change therefore brackets the unique global optimizer, proving convergence of its additive offset. Since the derivative of the respective parenthesized coefficient is nonzero at \(c_*\), a local mean-value estimate refines the error to \(O(L^3/n^2)\). These arguments do not infer global optimality merely from a local Taylor approximation; global uniqueness is an explicit prior premise.

Evaluating the three uniform expansions at the optimizers and using the derivative estimate yields the optimal-value expansions. In particular, at \(u_n=L+\log4\), \(e^{-u_n}=1/(4n^2)\), so the \(k_n\) expansion becomes \(1+[u_n^2/2+u_n+1]/n^2+O(L^4/n^4)\). Subtracting the value at \(c=0\), multiplying by \(n^2/L\), and letting \(n\to\infty\) gives the three compact-uniform boundary-layer profiles. Their first derivatives establish the specified unique extrema.

For the square lattice \(\eta=\sqrt n\), write \(x=n^{-1/2}\). The exact quotient is \(\coth^2(\sqrt n/2)\cosh x\) multiplied by \(1+O(\sqrt n e^{-\sqrt n})\), because the shared \(\eta\operatorname{csch}\eta\) term is exponentially small. The displayed square-lattice expansion follows. Finally the optimal excess condition number is asymptotic to \(2(\log n)^2/n^2\); division proves the sharp divergence factor.

## Verification

The self-contained script `checker.py` evaluates the displayed exact functions at arbitrary precision and checks the three optimizing shifts, their ordering, the optimal-value expansions, the square-lattice gap, and the entire compact-scale profile at specified test points. It ran successfully with 85 finite high-precision assertions. Run it using `python checker.py` with `mpmath` installed. The analytic Taylor bounds, sign changes, and prior uniqueness result—not the finite test—prove the asymptotic assertions.

## Relationship to prior work

The exact sharp rectangular frame-bound expressions and global uniqueness of the three optimizers are from Faulhuber and Shafkulovska, *Gabor frame bound optimizations*, arXiv:2204.02917, Section 8 and Theorem 2.7. They establish a qualitative ordering and coarse optimizer localization near \(2\operatorname{arccosh} n\); the present statement resolves the noncoalescing additive offsets, sharp high-density conditioning, boundary-layer tradeoff and comparison with the square lattice. Their closed expressions are essential input, so the result is an asymptotic refinement within that exact model rather than a new general Gabor-frame existence theorem. Kloos and Stöckler, arXiv:1311.7359, study even exponential frames and a different limit, approaching critical density. A public conference poster of the first paper describes optimizers as asymptotically close to the reference point without resolving the three additive gaps.

## Limitations

Only the two-sided exponential window and integer oversampling on rectangular lattices are covered; the result does not address sheared lattices, general totally positive windows, noninteger densities, or quantitative bounds uniform in arbitrarily growing \(c\). The proof of global uniqueness and the base exact frame formulas are explicitly inherited from the cited primary literature, while the asymptotic extraction is given here. A fully general historical-priority claim is not established; earlier analyses might already have expressed equivalent additive offsets or distortion asymptotics. No independent audit has been performed.

## References

1. M. Faulhuber and I. Shafkulovska, *Gabor frame bound optimizations*, arXiv:2204.02917, first posted 2022-04-06, especially Theorem 2.7 and Section 8; full text https://arxiv.org/html/2204.02917v2.
2. T. Kloos and J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359, 2013, especially Section 5; https://arxiv.org/abs/1311.7359.
3. M. Faulhuber and S. Steinerberger, *Optimal Gabor frame bounds for separable lattices and estimates for Jacobi theta functions*, Journal of Mathematical Analysis and Applications 445 (2017), 407–422; DOI 10.1016/j.jmaa.2016.07.074.
