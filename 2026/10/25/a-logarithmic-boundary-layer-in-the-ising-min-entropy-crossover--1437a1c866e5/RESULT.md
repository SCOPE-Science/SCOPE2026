# A logarithmic boundary layer in the Ising min-entropy crossover

## Finding

For the critical boundary-Ising flow, let \(X=2\lambda\ell\) be the dimensionless distance, let \(L=\log(1/X)\), and define the min-entropy boundary term by
\[
\mathfrak s_\infty(X)=-\int_0^{1/2}\log\mathfrak t_\beta(X)\,d\beta,
\]
where \(\mathfrak t_\beta(X)\) is the normalized twist-field scaling function from the exact boundary-Ising solution. As \(X\downarrow0\),
\[
\boxed{\mathfrak s_\infty(X)=\frac12\log 2-\frac{X}{\pi^2}L^2\bigl(L-2\log L\bigr)+O(XL^2).}
\]
In particular, the leading deficit is \(\frac{X}{\pi^2}\log^3(1/X)\,(1+o(1))\). The additional logarithm compared with the fixed-replica expansion comes from the singular endpoint \(\beta\uparrow\tfrac12\), not from an ordinary termwise integration of that expansion.

## Assumptions and scope

The statement concerns the universal scaling-limit boundary contribution in the critical Ising boundary-renormalization-group flow described by a relevant boundary magnetic field. The coupling \(\lambda\) is positive, the interval length \(\ell\) is positive, and the limit is \(X=2\lambda\ell\downarrow0\). The twist parameter satisfies \(0\le\beta\le\tfrac12\), and all logarithms are natural. The result does not assert a finite-lattice error bound, a formula for a general conformal field theory, or monotonicity of every Rényi boundary entropy.

## Proof

The exact solution expresses \(\mathfrak t_\beta(X)\) as a linear combination of two Meijer-G functions with argument \(X^2/4\); it also gives \(\mathfrak t_\beta(0)=\cos(\pi\beta)\) and the fixed-\(\beta\) expansion
\[
\log\mathfrak t_\beta(X)=\log\cos(\pi\beta)+XL^2\frac{2\beta}{\pi}\tan(\pi\beta)+\text{lower-order terms}.
\]
Expanding the unlogged exact expression at the repeated Mellin poles yields the endpoint-uniform form
\[
\mathfrak t_\beta(X)=\cos(\pi\beta)+XL^2\frac{2\beta}{\pi}\sin(\pi\beta)+O(XL),
\]
uniformly for \(0\le\beta\le\tfrac12\). This unlogged form is needed because the logarithmic coefficient above diverges at \(\beta=\tfrac12\).

At \(X=0\), the boundary term is
\[
-\int_0^{1/2}\log\cos(\pi\beta)\,d\beta=\frac12\log2.
\]
Write \(\delta=\tfrac12-\beta\) and \(\varepsilon=XL^2\). As \(\delta\downarrow0\),
\[
\cos(\pi\beta)=\pi\delta+O(\delta^3),\qquad
\frac{2\beta}{\pi}\sin(\pi\beta)=\frac1\pi+O(\delta).
\]
Consequently the endpoint layer has leading form \(\mathfrak t_{1/2-\delta}(X)=\pi\delta+\varepsilon/\pi+O(\delta^3+\delta\varepsilon+XL)\). In the overlap region \(\varepsilon\ll\delta\ll1\), this gives
\[
\log\frac{\mathfrak t_{1/2-\delta}(X)}{\cos(\pi(\tfrac12-\delta))}
=\frac{\varepsilon}{\pi^2\delta}+O\!\left(\varepsilon+\frac{XL}{\delta}+\frac{\varepsilon^2}{\delta^2}\right).
\]
The error terms integrate to \(O(\varepsilon)\) over \(\delta\in[\varepsilon,\delta_0]\), for any fixed sufficiently small \(\delta_0>0\). The inner layer \(0<\delta<\varepsilon\) contributes only \(O(\varepsilon)\), since after rescaling \(\delta=\varepsilon u\) its leading logarithm is \(\log(1+1/(\pi^2u))\), which is integrable at \(u=0\). Away from the endpoint the integral is also \(O(\varepsilon)\). Therefore
\[
\begin{aligned}
\mathfrak s_\infty(0)-\mathfrak s_\infty(X)
&=\int_0^{1/2}\log\frac{\mathfrak t_\beta(X)}{\cos(\pi\beta)}\,d\beta\\
&=\frac{\varepsilon}{\pi^2}\log\frac1\varepsilon+O(\varepsilon).
\end{aligned}
\]
Since \(\varepsilon=XL^2\) and \(\log(1/\varepsilon)=L-2\log L\), the boxed asymptotic follows. The coefficient \(1/\pi^2\) is fixed by \((2\beta/\pi)\tan(\pi\beta)\sim1/(\pi^2\delta)\); it is not a fitted numerical constant.

## Verification

The proof uses the exact Meijer-G representation and its small-argument expansion, followed by an explicit endpoint-layer integral. The endpoint-uniform expansion is stated separately from the fixed-\(\beta\) logarithmic expansion, avoiding an invalid exchange of the \(X\downarrow0\) limit with the \(\beta\)-integral. The error scale is \(O(XL^2)\) after integration. No finite numerical scan is used as proof, and no finite-lattice estimate is claimed.

## Relationship to prior work

Cornfeld and Sela derive the exact twist scaling function, the finite-index Rényi expression, the min-entropy integral, and the short-distance expansion of the von Neumann boundary term. Their displayed short-distance calculation treats the replica parameter away from the singular endpoint; it does not state the min-entropy asymptotic proved here. Because the coefficient \((2\beta/\pi)\tan(\pi\beta)\) diverges at \(\beta=\tfrac12\), direct termwise integration of their fixed-\(\beta\) formula is not justified and misses the endpoint-layer logarithm. The entropic \(g\)-theorem of Casini, Salazar Landea, and Torroba concerns a monotone von Neumann boundary function, not this high-Rényi asymptotic. Work on Rényi entropy of a line in a two-dimensional Ising cylinder treats a different geometry and observable.

## Limitations

The conclusion is an asymptotic statement for the boundary-Ising scaling function only. It does not establish an exact closed form for \(\mathfrak s_\infty(X)\) at arbitrary \(X\), a finite-lattice correction, or a universal law for other boundary flows. The uniform remainder is obtained from the exact Meijer-G representation; an independent specialist audit has not been performed.

## References

1. E. Cornfeld and E. Sela, “Entanglement entropy and boundary renormalization group flow: exact results in the Ising universality class,” arXiv:1705.04181v1 (first public 2017-05-11), especially the exact twist expression and Appendix D.
2. H. Casini, I. Salazar Landea, and G. Torroba, “The \(g\)-theorem and quantum information theory,” arXiv:1607.00390v2 (2016).
3. J.-M. Stéphan, G. Misguich, and V. Pasquier, “Rényi entropy of a line in two-dimensional Ising models,” arXiv:1006.1605v2 (2010).
