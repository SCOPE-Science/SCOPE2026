# Two temperature switches in a three-dimensional Bayesian E-optimal design

## Finding

A binary choice between two rank-one experimental updates in dimension three can select the **unique E-optimal experiment at both low and high entropic smoothing, but the strictly inferior, singular experiment at every intermediate smoothing parameter in one nonempty interval**. The two switches are exact and exhaustive. Dimension three is minimal for this endpoint-agreement/interior-reversal phenomenon: for any pair of symmetric matrices of dimension at most two, strict dominance of one matrix in both minimum eigenvalue and trace makes it better at every positive smoothing parameter.

Explicitly, let
\[
C=\operatorname{diag}(0,1,4),\qquad
u=(\sqrt{2},0,\sqrt{3})^{\mathsf T},\qquad
v=(0,2,0)^{\mathsf T},
\]
and allow exactly one experiment from \(\{u,v\}\), producing \(M_u=C+uu^{\mathsf T}\) or \(M_v=C+vv^{\mathsf T}\). For \(\mu>0\) define the normalized entropic soft minimum
\[
F_\mu(M)=-\mu\log\left(\frac{1}{3}\operatorname{tr}e^{-M/\mu}\right).
\]
Let \(r_-<r_+\) be the two roots in \((0,1)\) of
\[
Q(t)=t^7+t^6+t^5-t^3-t^2-t+1
\]
and define \(\mu_\pm=-1/\log r_\pm\). Then the unique maximizing choice for \(F_\mu\) is \(u\) when \(0<\mu<\mu_-\) or \(\mu>\mu_+\), but \(v\) when \(\mu_-<\mu<\mu_+\). Both choices tie at precisely \(\mu_-\) and \(\mu_+\). Numerically,
\[
(\mu_-,\mu_+)=(1.879597222729\ldots,\ 6.819744289599\ldots).
\]
Nevertheless, \(\lambda_{\min}(M_u)=1\) while \(\lambda_{\min}(M_v)=0\) for every \(\mu\): the inferior choice at intermediate smoothing loses one full unit of the unsmoothed minimum-eigenvalue objective.

## Assumptions and scope

The feasible binary experiment selections are precisely \((1,0)\) and \((0,1)\); there is no fractional design, stochastic observation error, or claim about an optimization algorithm's iterates. The prior \(C\) is positive semidefinite and both experiment updates are positive semidefinite of rank one. The parameter \(\mu\) ranges over all positive real numbers, and the matrix exponential is exact. This is Bayesian E-optimal design, where the prior information matrix is nonzero, and uses the same log-trace-exponential smoothed minimum eigenvalue studied in the cited literature.

The dimension-minimality statement is more general. If real symmetric matrices \(A,B\) of dimension \(d\le2\) obey \(\lambda_{\min}(A)>\lambda_{\min}(B)\) and \(\operatorname{tr} A>\operatorname{tr} B\), then \(F_\mu(A)>F_\mu(B)\) for every \(\mu>0\), where the normalization is \(1/d\).

## Proof

**1. Exact spectra and E-optimality.** The two information matrices are
\[
M_u=\begin{pmatrix}2&0&\sqrt6\\0&1&0\\\sqrt6&0&7\end{pmatrix},\qquad
M_v=\operatorname{diag}(0,5,4).
\]
The nontrivial \(2\times2\) block of \(M_u\) has trace \(9\) and determinant \(2\cdot7-6=8\); its eigenvalues are \(1\) and \(8\). Thus the full ordered spectra are \((1,1,8)\) and \((0,4,5)\). Hence \(M_u\) is positive definite, \(M_v\) is singular, and the exact E-optimal design is uniquely \(u\). Their traces are respectively \(10\) and \(9\).

**2. Reduction to a polynomial.** Put \(t=e^{-1/\mu}\in(0,1)\). Monotonicity of the negative logarithm shows that \(F_\mu(M_u)>F_\mu(M_v)\) if and only if
\[
P(t):=2t+t^8-1-t^4-t^5<0.
\]
Direct polynomial multiplication gives
\[
P(t)=(t-1)Q(t),\quad Q(t)=t^7+t^6+t^5-t^3-t^2-t+1.
\]
Descending coefficients of \(Q\), omitting the zero coefficient of \(t^4\), have the signs \(+,+,+,-,-,-,+\). Descartes' sign rule therefore bounds the number of positive real zeros of \(Q\), counted with multiplicities, by two. Yet exact rational evaluation gives
\[
Q(1/2)=23/128>0,\qquad
Q(3/5)=-1843/78125<0,\qquad
Q(9/10)=1612279/10000000>0.
\]
The intermediate-value theorem forces a zero in each of \((1/2,3/5)\) and \((3/5,9/10)\). They are the *only* positive roots, are simple (otherwise the multiplicity bound would be exceeded), and have the signs \(Q>0,Q<0,Q>0\) in the three remaining intervals of \((0,1)\). Since \(t-1<0\), the sign of \(P\) is respectively negative, positive, negative. Finally, \(\mu\mapsto e^{-1/\mu}\) is strictly increasing from \(0\) to \(1\), so the claimed choice and exact two ties follow for every \(\mu>0\). There are no unexamined parameter ranges.

**3. Why two dimensions cannot exhibit this endpoint agreement and interior reversal.** In dimension two, write the ordered spectra \(a_1\le a_2\) and \(b_1\le b_2\), where \(a_1>b_1\) and \(a_1+a_2>b_1+b_2\). If \(a_2\ge b_2\), strict componentwise spectral dominance gives \(\sum_i e^{-a_i/\mu}<\sum_i e^{-b_i/\mu}\). Otherwise \(a_2<b_2\). Set \(\delta=a_1-b_1\) and \(\varepsilon=b_2-a_2\); the trace inequality gives \(\delta>\varepsilon>0\), while ordering places the interval \([b_1,a_1]\) wholly to the left of \([a_2,b_2]\). Since \(s\mapsto e^{-s/\mu}/\mu\) is strictly decreasing, we have
\[
\int_{b_1}^{a_1}\frac{e^{-s/\mu}}{\mu}\,ds
>
\int_{a_2}^{b_2}\frac{e^{-s/\mu}}{\mu}\,ds.
\]
Equivalently \(e^{-b_1/\mu}-e^{-a_1/\mu}>e^{-a_2/\mu}-e^{-b_2/\mu}\), so the trace-exponential of \(A\) is smaller and its smoothed minimum greater, for every positive \(\mu\). The one-dimensional case is immediate. The explicit construction in step 1 establishes that dimension three is attainable, completing minimality.

## Verification

The independent-of-symbolic-software script `verify.py` and recorded output `verification_output.txt` are included. Running `python verify.py` verifies both characteristic polynomials and their factorization, the three exact rational sign witnesses, and the two sign changes of the nonzero coefficients of \(Q\); it then bisects the two roots and checks the reported values of \(\mu_\pm\). It also compares both trace-exponential objectives at eight smoothing parameters and performs 5,029 seeded random two-dimensional spectral comparisons at seven temperatures each. The exact proof above—not these finite tests—establishes the universal assertions.

## Relationship to prior work

Hendrych, Besançon and Pokutta (2026), arXiv:2608.27024, define precisely this normalized entropic spectral soft minimum in their equation (4), discuss Bayesian E-optimal design in Section 1, prove that sufficiently small smoothing preserves the discrete optimum, and investigate smoothing selection in their computational Section 7. Those results explain the low-smoothing behavior but do not state the three-dimensional two-switch information-matrix construction or the all-temperature dimension-two boundary in the inspected main results, experiments, and relevant appendix proofs. D'Aspremont (arXiv:math/0512344) studies matrix-exponential smoothing for semidefinite optimization and approximate gradients, not exact repeated reversals in a binary rank-one experimental design. Polynomial sign counting and the dimension-two exponential-order argument use standard elementary mathematics; neither technique, nor the underlying smoothing definition, is claimed as new.

## Limitations

The phenomenon is proved for one explicitly specified two-choice Bayesian design, not for every data set or for the globally continuous design relaxation. The two thresholds depend on its particular spectral data. We do not establish an upper bound of two switches for arbitrary three-dimensional designs or an algorithmic instability theorem. The two-dimensional comparison requires strict minimum-eigenvalue and trace advantages for the same alternative; it is not asserted under merely one of those assumptions. The literature search cannot exclude an equivalent construction in older work on exponential-polynomial crossings, Laplace-transform order, or temperature-dependent design selection. Independent priority validation has not been performed.

## References

1. D. Hendrych, M. Besançon and S. Pokutta, *Discrete eigenvalue optimization from entropic smoothing and first-order methods*, arXiv:2608.27024v1, first posted 2026-08-27. https://arxiv.org/abs/2608.27024
2. A. d'Aspremont, *Smooth Optimization with Approximate Gradient*, arXiv:math/0512344 (2005; revised 2008), *SIAM Journal on Optimization* 19 (2008), 1171–1183. https://arxiv.org/abs/math/0512344
3. Y. Nesterov, *Smoothing technique and its applications in semidefinite optimization*, *Mathematical Programming* 110 (2007), 245–259. https://doi.org/10.1007/s10107-006-0001-8
