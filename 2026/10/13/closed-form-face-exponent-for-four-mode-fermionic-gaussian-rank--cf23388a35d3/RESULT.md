# Closed-form face exponent for four-mode fermionic Gaussian rank
## Finding
For the four-mode even-parity state
\[
|M_t\rangle=\frac{{|0000\rangle+t|1111\rangle}}{{\sqrt{{1+t^2}}}},\qquad 0<t\le1,
\]
consider the weighted-Gram exponent introduced in arXiv:2610.02172v1. Set
\[
\theta_t=\frac{{t^2}}{{1+t^2}},\qquad N_t=\exp(h(\theta_t)),
\]
where \(h\) is binary entropy with natural logarithms. Restrict the source entropy maximization to the face \(w_3=0\). Define
\[
D_t=\sqrt{{\frac{{11N_t-8}}{{3N_t}}}},\qquad r_t=\frac{{D_t-1}}2.
\]
Then the restricted optimum is exactly
\[
\widehat B_t
=\frac{{1+4N_t r_t+3N_t r_t^2}}{{(1+r_t)^4}}
=\frac{{8(3N_t-2+N_tD_t)}}{{(1+D_t)^4}}>1.
\]
The unique optimizing weights on this face are
\[
(w_0,w_1,w_2,w_3)
=\frac1{{Z_t}}(1,4N_t r_t,3N_t r_t^2,0),
\qquad Z_t=1+4N_t r_t+3N_t r_t^2.
\]
Because the source base \(B_t\) maximizes the same objective over the full simplex,
\[
B_t\ge \widehat B_t.
\]
Combining this with the source's weighted-Gram rank theorem gives, for every fixed \(0\le\delta<1\),
\[
\liminf_{{k\to\infty}}\frac1k\log \underline\chi_{{\mathrm G}}^{{(\delta)}}(|M_t\rangle^{{\otimes k}})
\ge \log\widehat B_t.
\]
Finally, in the near-Gaussian limit,
\[
\log\widehat B_t
=\frac43 h(\theta_t)^2-\frac{{56}}{{27}}h(\theta_t)^3+O(h(\theta_t)^4),
\]
and therefore
\[
\log\widehat B_t\sim \frac{{16}}3 t^4\log^2(1/t)\qquad(t\to0).
\]
Thus the source's qualitative statement \(B_t>1\) admits a closed-form, fully explicit lower certificate for every \(t\), together with a quantitative collapse law as the state approaches the Gaussian vacuum.

## Assumptions and scope
The claim uses exactly the four-mode normal form and weighted local Gram matrix of arXiv:2610.02172v1. It concerns the approximate border Gaussian rank lower bound supplied by that method. It does not assert that \(\widehat B_t=B_t\) for \(0<t<1\), nor that the displayed face is globally optimal. At \(t=1\), the face value is about \(1.382955\), while the source's full optimization gives \(B_1=343/243\), so the distinction is explicit.

The face \(w_3=0\) retains the identity block, all eight degree-one Majorana columns, and the six degree-two columns whose local Gram pairs have the common two-point spectrum. It removes the exceptional degree-two pair whose block couples to the identity sector. This is why the restricted entropy is exactly solvable.

## Proof
On \(w_3=0\), the weighted Gram spectrum in arXiv:2610.02172v1 separates into the identity eigenvalue \(w_0\), four identical degree-one two-by-two blocks, and three identical degree-two two-by-two blocks. Since
\[
\frac{{1-\sigma_t}}2=\theta_t,\qquad \frac{{1+\sigma_t}}2=1-\theta_t,
\]
each nonzero two-by-two block contributes the same internal binary entropy \(h(\theta_t)=\log N_t\). Consequently
\[
H(\rho_t(w))
=H(w_0,w_1,w_2)+w_1\log4+w_2\log3+(w_1+w_2)\log N_t.
\]
Let
\[
m=w_1+2w_2,
\]
which is the source mean degree on this face. For \(0\le m\le2\), put
\[
r=\frac{m}{4-m}.
\]
Then
\[
4h(m/4)=4\log(1+r)-m\log r.
\]
Therefore the face objective is
\[
F_t(w)=H(w_0,w_1,w_2)+w_1\log(4N_t)+w_2\log(3N_t)+m\log r-4\log(1+r).
\]
For fixed \(r\), the Gibbs variational identity gives
\[
H(w_0,w_1,w_2)+w_1\log(4N_t r)+w_2\log(3N_t r^2)
\le \log(1+4N_t r+3N_t r^2),
\]
with equality exactly for weights proportional to \((1,4N_t r,3N_t r^2)\). Hence every feasible \(w\) obeys
\[
F_t(w)\le \Phi_t(r)
:=\log\frac{{1+4N_t r+3N_t r^2}}{{(1+r)^4}}.
\]
Differentiation yields a numerator with the same sign as
\[
4(N_t-1)-6N_t r-6N_t r^2.
\]
Because \(1<N_t\le2\), this expression has a unique positive zero
\[
r_t=\frac12\left(\sqrt{{\frac{{11N_t-8}}{{3N_t}}}}-1\right)<1.
\]
It is positive before \(r_t\) and negative after it, so \(\Phi_t\) has a unique global maximum there. The defining equation is
\[
r_t(1+r_t)=\frac{{2(N_t-1)}}{{3N_t}}.
\]
For the Gibbs weights at \(r_t\), direct substitution gives
\[
w_1+2w_2=\frac{{4r_t}}{{1+r_t}},
\]
so their induced value \(m/(4-m)\) is exactly \(r_t\). Thus the upper bound is attained by a feasible face point, proving both the exact face optimum and uniqueness. Since \(\Phi_t(0)=0\) and \(\Phi_t\) initially increases, \(\widehat B_t>1\).

For the asymptotic expansion, write \(s=h(\theta_t)\), so \(N_t=e^s\). Substituting the closed form for \(r_t\) into \(\Phi_t\) and expanding at \(s=0\) gives
\[
\log\widehat B_t=\frac43s^2-\frac{{56}}{{27}}s^3+O(s^4).
\]
Also \(\theta_t\sim t^2\) and
\[
h(\theta_t)\sim t^2\log(1/t^2)=2t^2\log(1/t),
\]
which yields the displayed \(16/3\) coefficient.

## Verification
A standalone standard-library checker evaluates the closed forms for several values of \(t\), verifies the stationarity equation, the self-consistency relation between \(r_t\) and the mean degree, the equality between the entropy objective and \(\log\widehat B_t\), strict positivity, and dense-grid dominance on the face. It also checks numerical convergence of \(\log\widehat B_t/h(\theta_t)^2\) to \(4/3\).

These finite computations are regression checks only. The all-\(t\) statement follows from the exact Gram-spectrum reduction, Gibbs variational identity, one-variable derivative sign, and the analytic expansion above.

## Relationship to prior work
Wei, Wu, Liu, and Liu define \(B_t\) by a three-parameter entropy maximization and prove \(1<B_t\le N_t\), with \(B_1=343/243\) and \(B_t\to1\) as \(t\to0\). Their positivity proof evaluates only the narrower line \((w_0,w_1,w_2,w_3)=(1-u,u,0,0)\) for sufficiently small \(u\). The inspected source does not optimize the larger face \(w_3=0\), provide the closed form \(\widehat B_t\), or state the near-Gaussian coefficient \(4/3\) for this certificate.

Cudby and Strelchuk introduced Gaussian rank for matchgate simulation and studied small-copy decompositions and Gaussian extent. Their inspected Gaussian-rank results do not give the weighted-Gram tensor-power lower exponent for \(|M_t\rangle\), nor the face optimization above. Dias and Koenig study sampling complexity for coherent superpositions of tractable states; their framework is relevant to simulation costs but does not imply this lower-bound exponent.

## Limitations
The result is an explicit lower certificate for the full base \(B_t\), not an exact solution of the source's full simplex optimization. In particular, the full optimizer can leave \(w_3=0\), as already demonstrated at \(t=1\). The asymptotic formula describes \(\widehat B_t\), and therefore a certified lower exponent, not necessarily the exact asymptotic of \(B_t\).

A residual priority risk remains that an equivalent entropy-face calculation could appear under different weighted-Gram or matchgate terminology, especially because the motivating preprint is only days old. Targeted semantic searches and inspection of the closest Gaussian-rank literature found no such statement.

## References
1. F. Wei, K.-W. Wu, Z. Liu, and Z.-W. Liu, “Robust exponential lower bounds for fermionic and bosonic Gaussian ranks,” arXiv:2610.02172v1, first submitted 1 October 2026.
2. J. Cudby and S. Strelchuk, “Gaussian decomposition of magic states for matchgate computations,” arXiv:2307.12654v4.
3. R. Dias and R. Koenig, “On the sampling complexity of coherent superpositions,” arXiv:2501.17071v1.
