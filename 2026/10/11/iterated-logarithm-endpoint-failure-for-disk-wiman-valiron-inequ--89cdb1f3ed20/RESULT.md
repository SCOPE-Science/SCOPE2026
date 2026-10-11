# Iterated-logarithm endpoint failure for disk Wiman–Valiron inequalities

## Finding

Let \(\log_j\) denote the \(j\)-fold iterated natural logarithm. Define the positive-coefficient analytic function on \(\mathbb D\)
\[
f(z)=\sum_{k=2000}^{\infty}\exp\!\left(\frac{k}{\log\log k}\right)z^k.
\]
For \(0<r<1\), set
\[
M(r)=\max_{|z|=r}|f(z)|,\quad
\mu(r)=\max_{k\ge0}|a_k|r^k,\quad
A(r)=\frac{\mu(r)}{1-r}.
\]
Then
\[
\lim_{r\uparrow1}\frac{M(r)}{A(r)\sqrt{\log A(r)}\log_2 A(r)}=+\infty.
\]
More quantitatively, the following lower bound holds:
\[
\liminf_{r\uparrow1}
\frac{M(r)}{A(r)\sqrt{\log A(r)}\log_2 A(r)\log_3 A(r)}
\ge\frac1{40e\sqrt2}.
\]
Thus the \(n=2\) endpoint obtained by substituting \(\delta=0\) in Maciá's 2026 finite-logarithmic-exceptional-measure bound is impossible, even with an arbitrary positive multiplicative constant.

## Assumptions and scope

All logarithms are natural. Indices begin at \(2000\) so that the defining coefficient profile is positive, increasing, and strictly concave. The displayed iterated logarithms are used only for radii sufficiently close to \(1\), where their arguments are defined and positive. No assumption about coefficient cancellation is needed: every nonzero coefficient is positive. The conclusion concerns only the two-logarithm endpoint \(n=2\), not the corresponding higher-level endpoint questions.

An exceptional set \(E\subset(0,1)\) has finite logarithmic measure when
\[
\int_E\frac{dr}{1-r}<\infty.
\]
The theorem's divergence occurs as \(r\uparrow1\) along *all* real radii, and therefore persists outside every exceptional set of this type.

## Proof

**Analyticity and positivity.** For \(k\ge2000\), the \(k\)-th root of the coefficient is \(\exp(1/\log\log k)\to1\), so the power series has radius of convergence exactly \(1\). All coefficients are positive, hence \(M(r)=f(r)\). Moreover \(f(r)\ge\sum_{k\ge2000}r^k=r^{2000}/(1-r)\to\infty\); the analytic function is unbounded on the disk.

**Concave saddle.** For real \(x\ge2000\), set
\[
u=\log x,\qquad L=\log u,\qquad g(x)=\frac{x}{L}.
\]
Direct differentiation gives
\[
g'(x)=\frac1L-\frac1{uL^2},\qquad
g''(x)=-\frac1{xuL^2}\left(1-\frac1u-\frac2{uL}\right).
\]
For \(x\ge2000\), the parenthesis is strictly positive, so \(g\) is strictly concave. Its positive derivative decreases to \(0\). Consequently each sufficiently small \(s>0\) uniquely determines \(x=x(s)>2000\) by \(s=g'(x)\), and \(x(s)\to\infty\) as \(s\downarrow0\). Set \(r=e^{-s}\) and \(h_s(y)=g(y)-sy\). Strict concavity gives the unique maximum at \(y=x\), of value
\[
H=h_s(x)=g(x)-xg'(x)=\frac{x}{uL^2}.
\]
For all integers \(k\ge2000\), \(h_s(k)\le H\), hence \(\mu(r)\le e^H\). Taking an integer within \(1/2\) of \(x\) and applying Taylor's theorem on that unit interval gives \(\mu(r)\ge e^{H-1}\) for all sufficiently large \(x\), because \(g''(x)\to0\). Therefore \(\log\mu(r)=H+O(1)\).

**A broad flat peak.** Put
\[
q=\sqrt{xu}\,L,\qquad W=\left\lfloor\frac q{10}\right\rfloor.
\]
Since \(W/x\to0\), the displayed formula for \(g''\) implies that, for all sufficiently large \(x\),
\[
\sup_{|y-x|\le W}|g''(y)|\le\frac2{xuL^2}.
\]
Taylor's theorem and \(h_s'(x)=0\) then yield, for every integer \(k\) satisfying \(|k-x|\le W\),
\[
h_s(k)\ge H-\frac{W^2}{xuL^2}\ge H-\frac1{100}.
\]
There are at least \(2W-1\ge q/10\) such integers once \(q\ge30\). Using \(M(r)=\sum_{k\ge2000}e^{h_s(k)}\) and \(\mu(r)\le e^H\), we obtain the uniform bound
\[
\frac{M(r)}{\mu(r)}\ge e^{-1}\frac{\sqrt{xu}\,L}{10}.
\]
The constants are intentionally conservative.

**Comparison with the critical scale.** As \(x\to\infty\),
\[
s=\frac1L\left(1-\frac1{uL}\right)\ge\frac1{2L},
\quad 1-r=1-e^{-s}\ge\frac1{4L}.
\]
The saddle bounds imply
\[
\log A(r)=H+O(\log L),\qquad H=\frac{x}{uL^2}\to\infty.
\]
In particular, for all sufficiently large \(x\), \(\log A(r)\le2H\) and \(\log_2 A(r)\le u\), because \(2H<x\) eventually. Combining the last three estimates gives
\[
\frac{M(r)}{A(r)\sqrt{\log A(r)}\log_2 A(r)}
=\frac{M(r)}{\mu(r)}\frac{1-r}{\sqrt{\log A(r)}\log_2 A(r)}
\ge\frac{L}{40e\sqrt2}.
\]
Here \(L=\log\log x\to\infty\), proving the divergence for all \(r\uparrow1\), rather than for a chosen subsequence.

Finally \(\log A(r)=H+O(\log L)\) implies
\[
\log_2 A(r)=u-\log u-2\log L+o(1)\sim u,
\qquad \log_3 A(r)=L+o(1).
\]
Dividing the displayed lower bound by \(\log_3 A(r)\) proves the quantitative liminf assertion.

**Failure outside finite-logarithmic-measure sets.** For every constant \(C>0\), the critical quotient eventually exceeds \(C\) at every radius \(r\in(r_C,1)\). Any exceptional set on which the proposed estimate is allowed to fail must contain this whole terminal interval. But \(\int_{r_C}^1 dr/(1-r)=\infty\), contradicting finite logarithmic measure. This completes the proof.

## Verification

The three exact identities for \(g'(x)\), \(g''(x)\), and \(g(x)-xg'(x)\) were independently simplified symbolically to zero residuals. The standalone script `check_saddle.py` evaluates the derivative identities and the flat-peak inequalities at representative finite saddle locations, together with a finite-window lower bound. Such finite computations illustrate the formulas; the infinite-radius assertion follows entirely from the preceding analytic inequalities.

Run `python3 check_saddle.py` using the Python standard library. It prints the saddle locations, certified-from-formulas finite peak counts and related numerical diagnostic ratios. No numerical experiment is needed to infer uniformity in \(r\).

## Relationship to prior work

Maciá, *Wiman–Valiron inequalities in the unit disk outside sets of finite logarithmic measure*, arXiv:2609.28814v1 (publicly posted September 23, 2026), Theorem 1.1 proves the two-logarithm bound with exponent \(1+\delta\) on \(\log_2 A\) for every \(\delta>0\). Its Remark 5.2 expressly leaves the \(\delta=0\) endpoint undecided in the disk; the example with coefficients \(\exp(\sqrt k)\) in Proposition 5.1 establishes only sharpness of the leading \(\sqrt{\log A}\) exponent. The present coefficient profile forces divergence at the excluded endpoint.

Grosse-Erdmann, *A note on the Wiman–Valiron inequality*, arXiv:2409.06499v1, Section 2.6 formulates the disk problem for positive \(\delta\); its Section 1.1 explains that the analogous entire-function endpoint was already known to fail. That entire-function statement does not directly cover the present radius-one series with the boundary factor \((1-r)^{-1}\). Fenton and Strumia's 2009 study provides earlier disk theory; its summary in Grosse-Erdmann's Theorem 1.5 has an additional boundary logarithmic factor and does not imply the present lower bound.

## Limitations

This proves failure at the \(n=2\) iterated-logarithm endpoint. It neither proves optimality of any replacement factor involving \(\log_3 A\) nor resolves \(\delta=0\) at all higher levels. The explicit liminf constant is a conservative lower bound, not an optimized asymptotic constant. Finite diagnostics do not certify the asymptotic argument. An unindexed equivalent example is possible; the full text of the 2009 Fenton–Strumia paper was not available through the attempted lawful access routes, leaving a specifically identified residual literature risk.

## References

1. V. J. Maciá, *Wiman–Valiron inequalities in the unit disk outside sets of finite logarithmic measure*, arXiv:2609.28814v1 (September 23, 2026), Sections 1 and 5, especially Theorem 1.1 and Remark 5.2. https://arxiv.org/html/2609.28814v1
2. K.-G. Grosse-Erdmann, *A note on the Wiman–Valiron inequality*, arXiv:2409.06499v1 (September 10, 2024), Sections 1.1, 1.2 and Question 2.6. https://arxiv.org/html/2409.06499v1
3. P. C. Fenton and M. M. Strumia, *Wiman–Valiron theory in the disc*, Journal of the London Mathematical Society 79 (2009), 478–496, DOI:10.1112/jlms/jdp001 (abstract available; full text not inspected).
