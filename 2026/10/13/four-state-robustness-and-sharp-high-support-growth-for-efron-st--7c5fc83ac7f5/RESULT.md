# Four-state robustness and sharp high-support growth for Efron–Stein telescoping

## Finding

For an integer \(K\ge2\), let \(B_K\) be the least constant that works **simultaneously for every finite number of coordinates** in the following inequality. Suppose the pairs \((X_i,Y_i)\), \(1\le i\le n\), are independent across coordinates; within a pair, dependence is arbitrary, but \(X_i\) and \(Y_i\) have the same distribution, supported on at most \(K\) values. For every real-valued bounded measurable \(f\), put

\[
Z_j=f(X_1,\ldots,X_j,Y_{j+1},\ldots,Y_n),\qquad 0\le j\le n.
\]

Then the sharp dimension-free constant in

\[
\mathbb E(Z_n-Z_0)^2\le B_K\sum_{j=1}^n\mathbb E(Z_j-Z_{j-1})^2
\]

satisfies

\[
\boxed{B_2=B_3=B_4=1,\qquad B_5=\frac{3+\sqrt5}{4},\qquad B_6=\frac32.}
\]

In particular, **four-point marginal support does not require exchangeability** for the classical constant to hold, whereas a directed five-cycle is the smallest support obstruction.

Define \(\tau\in(0,\pi/2)\) as the unique positive solution of \(\tan\tau=2\tau\), and let

\[
c_*:=\frac{\sin^2\tau}{\pi\tau}=0.23065095754814657\ldots.
\]

The optimal constants have the sharp high-support asymptotic law

\[
\boxed{\lim_{K\to\infty}\frac{B_K}{K}=c_*.}
\]

For every integer \(K\ge4\), a dimension-independent, nonasymptotic bound improving the previously available \(K/2\) scale asymptotically is

\[
B_K\le \frac{\pi}{K\sin^2(\pi/K)}\,\frac{\sin^2\tau}{\tau}.
\]

## Assumptions and scope

The number of pairs \(n\) is arbitrary and finite, and may depend on \(K\). The variables within each pair need not be independent or exchangeable, and their coordinate-specific marginal laws need not agree across coordinates. The only within-pair hypothesis is equality of the two marginal distributions. All variables may take values in arbitrary measurable spaces with finite marginal support; relabeling makes their support finite integers. No integrability issue arises for bounded \(f\). The zero-denominator case is interpreted as a trivial inequality, not a ratio.

The claimed \(B_K\) is the **supremum over all such admissible instances**, not a fixed-\(n\) constant. The high-support limit does not claim an exact formula for every finite \(K\ge7\).

## Proof

**Reduction to directed cycles.** Equal row and column sums of the finite joint mass matrix \(p_i(a,b)=\Pr(X_i=a,Y_i=b)\) make it a nonnegative circulation. Each nonnegative finite circulation is a convex combination of normalized simple directed cycle flows, including loops: remove the smallest positive flow along a directed cycle and iterate. After normalizing by total mass, the convex weights sum to one. The expectation difference of squares is separately linear in each pair law, so a constant valid for products of uniform directed cycles is valid for arbitrary admissible product laws. This is the cycle reduction underpinning Theorem 5 of Baslingker–Virág [1].

On a cycle of length \(m_i\le K\), write \(X_i\) uniformly on \(\mathbb Z/m_i\mathbb Z\) and \(Y_i=X_i+1\) modulo \(m_i\). Orthogonality of product characters and Parseval turn the optimal squared-difference constant into the following **exact** Fourier supremum (terms with zero denominator are excluded):

\[
B_K=\sup_{n\ge1}\;\max_{\substack{1\le m_i\le K\\0\le u_i<m_i}}
\frac{\sin^2\!\left(\pi\sum_{i=1}^{n}u_i/m_i\right)}
{\sum_{i=1}^{n}\sin^2(\pi u_i/m_i)}.
\tag{1}
\]

For real \(f\), conjugate frequencies give the same quotient, and a cosine character attains each nonzero quotient; hence the complex-character calculation is also sharp for the stated real-valued inequality. A frequency with exactly one nonzero component has quotient one. All other configurations have at least two active components.

**Two active components.** Set \(\alpha=\pi/K\), and write \(a=\pi u/m\), \(b=\pi v/\ell\) for nonzero frequencies, so \(a,b\in[\alpha,\pi-\alpha]\). The elementary identity

\[
\sin^2(a+b)=\sin^2a+\sin^2b+2\sin a\sin b\cos(a+b)
\]

and \(2\sin a\sin b\le\sin^2a+\sin^2b\) apply. Since \(a+b\in[2\alpha,2\pi-2\alpha]\), \(\cos(a+b)\le\cos(2\alpha)\). If \(K\ge4\), the last cosine is nonnegative, and the quotient is at most

\[
1+\cos(2\alpha)=2\cos^2\alpha.
\tag{2}
\]

Equality is obtained with two coordinates on directed \(K\)-cycles, both frequencies equal to one.

**Exact first values.** Any active frequency contributes at least \(s_K=\sin^2(\pi/K)\) to the denominator of (1), whereas its numerator is at most one. With \(t\) active components, the quotient is therefore at most \(1/(t s_K)\). For \(K=2,3\), this is below one whenever \(t\ge2\), so \(B_2=B_3=1\). For \(K=4\), (2) bounds the two-active case by one; for \(t\ge3\), the bound is at most \(2/3\). Thus \(B_4=1\). For \(K=5\), \(s_5=(5-\sqrt5)/8>1/3\), so every \(t\ge3\) gives a quotient below one, while the two-active sharp value is \(2\cos^2(\pi/5)=(3+\sqrt5)/4>1\). For \(K=6\), every \(t\ge3\) gives at most \(4/3\), whereas the two-active sharp value is \(2\cos^2(\pi/6)=3/2\). This proves all exact values. For \(K=5,6\), the witnessing example uses \(n=2\), independent uniform directed \(K\)-cycles and \(f(x_1,x_2)=\cos(2\pi(x_1+x_2)/K)\).

**Sharp asymptotic upper bound.** Fix \(K\ge4\). For every active fraction \(u_i/m_i\), take its principal signed angle \(\varepsilon_i\delta_i\), where \(\varepsilon_i\in\{-1,1\}\), \(\delta_i\in[\alpha,\pi/2]\) and \(\pi u_i/m_i\equiv\varepsilon_i\delta_i\pmod\pi\). Let \(s\in[0,\pi/2]\) be the distance from \(\sum_i\varepsilon_i\delta_i\) to the nearest multiple of \(\pi\). Then

\[
\sin^2\!\left(\pi\sum_i u_i/m_i\right)=\sin^2s,
\qquad s\le\sum_i\delta_i.
\]

The function \(q(x)=\sin^2x/x\) on \((0,\pi/2]\) increases to one maximum at \(x=\tau\) and then decreases. Indeed its nonzero stationary points solve \(\tan x=2x\), and strict convexity of \(\tan x-2x\) gives exactly one positive root. Since \(\alpha\le\pi/4<\tau\) and

\[
q(\alpha)\le q(\pi/4)=q(\pi/2)=2/\pi,
\]

the minimum of \(q\) on \([\alpha,\pi/2]\) is \(q(\alpha)\). Consequently

\[
\sum_i\sin^2\delta_i
\ge\frac{\sin^2\alpha}{\alpha}\sum_i\delta_i
\ge\frac{\sin^2\alpha}{\alpha}s.
\]

If \(s=0\) the numerator is zero. Otherwise the quotient in (1) is at most

\[
\frac{\alpha}{\sin^2\alpha}\frac{\sin^2s}{s}
\le\frac{\alpha}{\sin^2\alpha}\frac{\sin^2\tau}{\tau},
\]

proving the nonasymptotic upper bound and

\[
\limsup_{K\to\infty}\frac{B_K}{K}\le\frac{\sin^2\tau}{\pi\tau}.
\]

**Matching lower bound.** For large \(K\), take \(n_K=\lfloor\tau K/\pi\rfloor\) independent directed \(K\)-cycles, with first Fourier frequency one in every coordinate. The cosine character provides the exact quotient

\[
B_K\ge
\frac{\sin^2(\pi n_K/K)}{n_K\sin^2(\pi/K)}.
\]

As \(K\to\infty\), \(\pi n_K/K\to\tau\), and multiplication by \(1/K\) makes the right-hand side converge to \(\sin^2\tau/(\pi\tau)\). Together with the upper bound this proves the limit.

## Verification

The standalone standard-library program `check_efron_constants.py` dynamically scans the exact discrete Fourier phase state space for \(K=2,3,4,5,6\). It retains the minimum denominator at each phase for each active-coordinate count, and terminates only after the analytic \(1/(t\sin^2(\pi/K))\) bound excludes larger counts. It independently enumerates small directed-cycle cosine expectations, tests the analytic angle inequality on finite grids, and compares finite-\(K\) witnesses with the proved asymptotic upper envelope. These are consistency tests: the universally quantified theorem is proved above, not by its finite tests. Run `python3 check_efron_constants.py` with Python 3.9 or newer.

## Relationship to prior work

Baslingker and Virág [1, Theorem 5] establish the cycle-flow/Fourier variational representation (1), with the general upper estimate \(B_K\le K/2\). The present theorem **evaluates** their sharp constant at the first nontrivial support sizes, finds the precise support threshold for failure of constant one, and derives its exact asymptotic slope; it does not claim their cycle reduction or the Efron–Stein inequality itself as new. The numerical large-\(K\) coefficient \(0.2306509575\ldots\) is less than half of their bound's coefficient \(1/2\).

Aldous and Fill [2, §4.6.3] give a product-chain Poincaré/Efron–Stein variance bound involving a one-coordinate replacement and relaxation time. It does not establish the **two-endpoint telescoping** constant here, and its conclusion cannot be substituted for (1). The classical independent-resampling results of Efron–Stein and Steele, cited in [1], cover another assumption class.

## Limitations

No exact value is claimed for general finite \(K\ge7\). The asymptotic coefficient concerns a supremum over arbitrarily many coordinates, and is not necessarily the sharp coefficient for fixed \(n\). The bound on the full support class is not a characterization of equality for every nonuniform coupling, and the result does not control unbounded support. Although the accessible sources and targeted searches did not reveal an equivalent evaluation, unindexed earlier optimizations of the same cyclic Fourier quotient remain a priority risk.

## References

[1] J. Baslingker and B. Virág, *The Efron–Stein inequality for identically distributed pairs*, arXiv:2605.05388v1, first posted 6 May 2026, especially Lemma 4, Theorem 5, and the finite-support proof. https://arxiv.org/html/2605.05388v1

[2] D. Aldous and J. Fill, *Reversible Markov Chains and Random Walks on Graphs*, §4.6.3, Corollaries 4.46–4.47. https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch4.S6.html
