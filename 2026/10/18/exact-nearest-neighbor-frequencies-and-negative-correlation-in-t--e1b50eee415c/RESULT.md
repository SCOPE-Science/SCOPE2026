# Exact nearest-neighbor frequencies and negative correlation in the Padovan nested recurrence

## Finding
For integers \(n\ge0\), define the binary increments \(d(n)=a(n+1)-a(n)\), where \(a(0)=0\), \(a(1)=1\) and \(a(n)=n-a(n-a(n-a(n-1)))\) for \(n\ge2\). Write \(\rho>1\) for the plastic number satisfying \(\rho^3=\rho+1\). The natural frequencies of the four consecutive increment pairs exist and are
\[
\begin{aligned}
P_{11}&=\frac{4+9\rho-8\rho^2}{7}=0.269062897889881736\ldots,\\
P_{01}=P_{10}&=\frac{3-2\rho+\rho^2}{7}=0.300777393108171\ldots,\\
P_{00}&=\frac{-3-5\rho+6\rho^2}{7}=0.129382315893775\ldots.
\end{aligned}
\]
In particular, successive increments exhibit a strictly negative covariance:
\[
\lim_{N\to\infty}\frac1N\sum_{n=0}^{N-1}d(n)d(n+1)
-\left(\lim_{N\to\infty}\frac1N\sum_{n=0}^{N-1}d(n)\right)^2
=\frac{11+2\rho-8\rho^2}{7}<0.
\]

## Assumptions and scope
The statement applies to every positive integer prefix length in the limiting process, with no statistical or independence assumptions. The recurrence and the fact that its increments form the binary morphic word are taken from Cloitre, Ma and Zhang's morphic representation theorem. Its substitution has initial letter \(S\), with \(\nu(S)=Sq_1\); the transient \(S\) has zero limiting frequency. The 25 productive letters and their images are encoded in the accompanying standalone `verify.py`, transcribed from Table 2 of that source. Frequencies refer to overlapping consecutive positions, not disjoint pairs.

## Proof
Put \(\mathcal A=\{q_1,q_2,q_3,q_4,q_5,q_7,q_8,q_9,q_{10},q_{11},q_{12},q_{13},q_{14},q_{15},q_{16},q_{17},q_{18},q_{19},q_{20},q_{22},q_{23},q_{24},q_{25},q_{26},q_{27}\}\). For the non-erasing substitution \(\nu\) of Table 2, form its 25-by-25 incidence matrix \(M\). An exact Boolean matrix calculation verifies that every entry of \(M^{20}\) is positive. Its Perron root is \(\rho\); solve \(Mv=\rho v\) with \(\sum_{q\in\mathcal A}v_q=1\). All coordinates are positive. Thus the limiting letter frequency vector is \(v\).

For each ordered symbolic pair \((u,v)\), let \(F(u,v)=(\operatorname{last}\nu(u),\operatorname{first}\nu(v))\). Beginning with all ordered pairs occurring internally in the words \(\nu(q)\) and closing under \(F\) yields exactly 67 pairs. Let \(Q\) be the 67-by-67 matrix that sends each pair basis vector to that of its image under \(F\). Put \(b_{uv}=\sum_q v_q\,\#\{uv\text{ occurring internally in }\nu(q)\}\). Replacing one symbol by \(\nu(q)\) creates its internal pairs; replacing one existing pair creates exactly one cross-boundary pair. Consequently, the limiting ordered-symbolic-pair vector \(w\) obeys
\[
\rho w=b+Qw,\qquad w=(\rho I-Q)^{-1}b.
\]
The inverse exists since \(Q\) is a deterministic transition matrix and \(\rho>1\). Primitivity implies convergence of the pair frequencies; alternatively the displayed affine recurrence contracts after normalization by \(\rho\).

Let \(\eta\) be the binary output morphism of Table 2. A symbolic letter \(q\) contributes \(|\eta(q)|\) binary positions; the mean output length is \(L=\sum_qv_q|\eta(q)|\). The number of `11` blocks per symbolic letter equals its internal contributions, plus cross-boundary contributions from pairs \((u,v)\) whose output ends and begins in `1`, respectively. Thus
\[
P_{11}=\frac{\sum_qv_q\,\#_{11}(\eta(q))+
\sum_{(u,v)}w_{uv}\mathbf1_{\{\operatorname{last}\eta(u)=1\}}\mathbf1_{\{\operatorname{first}\eta(v)=1\}}}{L}.
\]
Exact row reduction in the cubic field \(\mathbb Q(\rho)\), using \(\rho^3=\rho+1\), gives
\[
L=1-\rho+\rho^2,\quad
\text{numerator}=3+2\rho-3\rho^2,\quad
P_{11}=\frac{4+9\rho-8\rho^2}{7}.
\]
The companion code performs this exact field solve and checks these identities, rather than fitting a formula from decimals. The established one-letter density is \(c=\rho^{-2}=1+\rho-\rho^2\). Stationarity gives \(P_{01}=P_{10}=c-P_{11}\) and \(P_{00}=1-2c+P_{11}\), yielding the formulas. Since \(c^2=\rho-1\), covariance is \((11+2\rho-8\rho^2)/7\). As \(\rho>33/25\) and \(11+2x-8x^2\) is strictly decreasing for \(x>1/8\), while its value at \(33/25\) is \(-187/625\), the covariance is negative.

## Verification
Run `python verify.py` with Python 3 and SymPy. The program directly verifies the 25-letter substitution and its primitivity, exact cubic-field letter and pair equations, the closed-form identity, all required normalizations, and strict covariance sign. It separately evaluates 8193 increments from the nested recurrence and checks the corresponding binary prefix of the substitution. The executable terminates with `VERIFY_OK`. These finite prefix checks are independent diagnostics; the proof for all indices is the exact Perron–Frobenius calculation together with the published morphic identity.

## Relationship to prior work
Cloitre, Ma and Zhang (arXiv:2609.33421, September 27, 2026) identify the recurrence and give the complete 26-letter substitution, first-order increment frequency, nonperiodicity, and sharp balance constant. Those results are essential premises and are not claimed here. Their full text, including Section 5 and Table 2, does not state the two-point frequency law or the covariance formula. Shallit's work on the Narayana morphism studies a different word. The numerical invariant and the explicit strict repulsion conclusion are additional to the published first-order statistics. An equivalent implicit calculation elsewhere remains possible.

## Limitations
This is the lag-one joint distribution only; higher-order correlations, mixing rates and finite-prefix discrepancy estimates are not established. The exact solution uses a pre-existing morphic presentation, and it does not provide an independent proof of that presentation. Independent mathematical review has not been performed.

## References
Cloitre, B., Ma, H., and Zhang, W., *A Padovan-automatic description of a nested recurrence*, arXiv:2609.33421v1 (2026-09-27), especially Proposition 5.2, Corollary 5.3 and Table 2. https://arxiv.org/abs/2609.33421

Shallit, J., *The Narayana Morphism and Related Words*, arXiv:2503.01026 (2025). https://arxiv.org/abs/2503.01026

OEIS A076502, the nested recurrence sequence. https://oeis.org/A076502
