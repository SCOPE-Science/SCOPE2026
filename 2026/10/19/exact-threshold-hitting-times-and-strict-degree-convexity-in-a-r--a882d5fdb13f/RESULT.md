# Exact threshold-hitting times and strict degree convexity in a resetting network-growth model

## Finding

The discrete degree process associated with uniform network growth and node deletion has an exact first-passage mean, and this mean is **strictly convex in every integer target degree**, with no parameter-dependent change of ordinary discrete curvature.

For any \(\alpha>0\), \(r>0\), and integer \(n\geq1\), let \(K_t\) start at zero and have upward jumps \(k\to k+1\) at rate \(\alpha\), downward jumps \(k\to k-1\) at rate \(rk\) when \(k\geq1\), and full resets \(k\to0\) at independent rate \(r\). Define \(\tau_n=\inf\{t\geq0:K_t=n\}\) and \(M_n=\mathbb E_0[\tau_n]\), with \(M_0=0\).

Write \(x=r/\alpha\) and \((n)_{\underline j}=n!/(n-j)!\) for \(0\leq j\leq n\). Then

\[
\boxed{M_n=\frac1r\sum_{j=1}^{n}(n)_{\underline j}x^j
=\frac n\alpha\bigl(1+rM_{n-1}\bigr).}
\]

All sums are finite and the expressions hold at every positive parameter pair. For all \(n\geq1\),

\[
\boxed{M_{n+1}-2M_n+M_{n-1}
=\frac1r\sum_{j=2}^{n+1}j(j-1)(n-1)_{\underline{j-2}}x^j
\;>\;0.}
\]

Here a falling factorial vanishes if its lower index exceeds its upper nonnegative integer. In particular the curvature is at least \(2r/\alpha^2\). For fixed \(\alpha,r>0\) and integer \(n\to\infty\),

\[
\boxed{M_n\sim\frac{e^{\alpha/r}}{r}\,n!\left(\frac r\alpha\right)^n.}
\]

Thus the continuum approximation's suggested concave-to-convex transition does not occur in the ordinary mean-versus-integer-target sequence of the exact discrete degree model.

## Assumptions and scope

The state space is \(\mathbb Z_{\geq0}\). Each birth and neighbor deletion is memoryless and has the rates just specified; a full reset erases the present degree but not the underlying stochastic clock. A reset occurring at degree zero is a null event. The target is an **integer** \(n\geq1\), not a continuously interpolated threshold. This is the degree-level Markov description appearing in Artime's network-growth model, as given by its master equations (1) and (17)–(19). In the physical finite network the degree of a particular node need not be an exactly autonomous Markov chain with these rates; the present theorem is about the stated exact discrete master-equation process, not an unquantified finite-network approximation.

For completeness the Laplace transform of \(\tau_n\) is also explicit through finite polynomials. Set \(P_0(s)=1\), \(P_1(s)=1+(s+r)/\alpha\), and for integers \(k\geq1\),

\[
P_{k+1}(s)=\left(1+\frac{s+(k+1)r}{\alpha}\right)P_k(s)-\frac{kr}{\alpha}P_{k-1}(s).
\]

Then, for all \(s\geq0\),

\[
\mathbb E_0[e^{-s\tau_n}]=\frac{s+r}{sP_n(s)+r}.
\]

This statement is equivalent to the same first-passage process, not an additional independent finding.

## Proof

**1. Discounted hitting before resetting.** Temporarily omit the full resets but keep upward rate \(\alpha\) and downward rate \(rk\). Let \(H_n\) be the hitting time of \(n\) in this immigration–death chain, and let \(E\sim\operatorname{Exp}(r)\) be an independent full-reset clock. For \(s\geq0\), the functions \(h_k(s)=\mathbb E_k[e^{-(s+r)H_n}]\) satisfy

\[
\alpha h_{k+1}(s)+rk h_{k-1}(s)
=(\alpha+rk+s+r)h_k(s),\qquad 0\leq k<n,
\]

with the downward term omitted at \(k=0\) and boundary \(h_n(s)=1\). These finite equations have the solution \(h_k(s)=P_k(s)/P_n(s)\), where the polynomials above are obtained by setting \(P_0(s)=1\) and recursively solving the same homogeneous equation. In particular,

\[
p_n:=\mathbb P_0(H_n<E)=\mathbb E_0[e^{-rH_n}]=\frac1{P_n(0)}>0.
\]

Because a sequence of \(n\) births without deletions or full resets has positive probability, the target is eventually reached with finite mean after independent reset trials. The positive denominator also follows directly from the recurrence below.

**2. Exact renewal identity.** During a reset trial, the process runs until \(H_n\wedge E\). If \(E<H_n\), it restarts independently from zero. Consequently,

\[
M_n=\mathbb E_0[H_n\wedge E]+(1-p_n)M_n,
\qquad
\mathbb E_0[H_n\wedge E]=\frac{1-p_n}{r}.
\]

Thus \(M_n=(P_n(0)-1)/r\). The same renewal decomposition with a Laplace parameter gives

\[
\mathbb E_0[e^{-s\tau_n}]
=\frac{(s+r)\mathbb E_0[e^{-(s+r)H_n}]}
{s+r\mathbb E_0[e^{-(s+r)H_n}]}
=\frac{s+r}{sP_n(s)+r}.
\]

**3. Finite-polynomial simplification.** Put \(P_k=P_k(0)\) and \(x=r/\alpha\). The polynomial recurrence reads

\[
P_0=1,\qquad P_1=1+x,\qquad
P_{k+1}=[1+(k+1)x]P_k-kxP_{k-1}.
\]

Induction gives \(P_{k+1}=1+(k+1)xP_k\): subtracting the displayed three-term recurrence from the proposed formula leaves \(1-P_k+kxP_{k-1}\), which vanishes by the preceding induction step. Iteration yields

\[
P_n=1+\sum_{j=1}^{n}\frac{n!}{(n-j)!}x^j.
\]

Substituting into \(M_n=(P_n-1)/r\) proves the finite sum and the recursion \(M_n=\frac n\alpha(1+rM_{n-1})\). The base case is \(M_1=1/\alpha\).

**4. Uniform strict discrete convexity.** Extend the sum by the convention \((n)_{\underline j}=0\) for \(j>n\). The elementary forward-difference identity

\[
(n+1)_{\underline j}-(n)_{\underline j}=j(n)_{\underline{j-1}}
\]

implies, for integer \(n\geq1\),

\[
(n+1)_{\underline j}-2(n)_{\underline j}+(n-1)_{\underline j}
=j(j-1)(n-1)_{\underline{j-2}}.
\]

Each term with \(j\geq2\) is nonnegative, and the \(j=2\) term is \(2x^2/r=2r/\alpha^2>0\), proving strict convexity for all \(n\), even where \(n<\alpha/r\). The same positive-coefficient formula proves strict growth in \(n\).

**5. Fixed-rate large-target asymptotics.** Re-indexing the sum gives the exact identity

\[
P_n=n!x^n\sum_{m=0}^{n}\frac{1}{m!x^m}.
\]

For fixed \(x>0\), the finite series tends monotonically to \(e^{1/x}\), whereas \(n!x^n\to\infty\). Therefore \(M_n=(P_n-1)/r\sim e^{1/x}n!x^n/r\), proving the announced asymptotic. No exchange of a vanishing reset-rate and diverging target-degree limit is asserted.

## Verification

A standalone Python program, `check.py`, reconstructs the finite transient generator independently of the renewal proof and solves its exact rational linear equations for multiple rates and thresholds. It also checks the rational first-passage Laplace transform, the finite-sum formula, the recursion and strict discrete curvature. Execution produced `PASS 1296 exact generator, resolvent, strict-curvature and polynomial checks`. These finite checks are cross-checks; the all-parameter assertions follow from the preceding identities.

For example, at \(\alpha=2\) and \(r=1/2\), the first four means are \(M_1=1/2\), \(M_2=5/4\), \(M_3=39/16\), and \(M_4=71/16\), giving strictly positive successive second differences. The zero-reset limit at each fixed integer target is \(\lim_{r\downarrow0}M_n=n/\alpha\).

## Relationship to prior work

Artime (2022), arXiv:2211.01869v1, establishes the degree master equation and derives first-passage master equations (17)–(19); its first-passage treatment then passes to a continuous-degree Fokker–Planck approximation, with a stated concave-to-convex inflection expectation near \(n=\alpha/r\). The exact discrete first-passage mean and its strict ordinary discrete convexity are not stated in that inspected analysis. The paper's plots use a logarithmic vertical scale, where visual curvature must not be conflated with ordinary curvature of \(M_n\) itself.

Immigration–death processes with catastrophes have an earlier queueing-theory literature. Kapodistria, Phung-Duc and Resing (2015) analyze transient and stationary laws under binomial catastrophes, including total catastrophes as a boundary case; Chao and Zheng (2003) analyze transient and equilibrium behavior under total catastrophes. The general process representation and renewal method are therefore not claimed to be new. The contribution assessed here is the exact formula and the sharp all-parameter curvature conclusion for the network-degree first-passage question left to approximation in the motivating paper.

## Limitations

The result does not establish the corresponding first-passage formula for a finite network with degree-dependent edge-addition corrections, correlated finite-size degrees or prohibitions on multiple edges. It concerns ordinary differences of raw mean hitting times across **integer** target degrees, not the second derivative of a continuum interpolation or the curvature of a logarithmically transformed plot. The factorial law is a fixed-positive-rate asymptotic, not uniform as \(r\downarrow0\). Prior queueing theory could conceal an equivalent specialization; an independent priority assessment has not been performed.

## References

- O. Artime, *Stochastic resetting in a networked multiparticle system with correlated transitions*, arXiv:2211.01869v1, submitted 2022-11-03; Journal of Physics A: Mathematical and Theoretical 55 (2022) 484004, DOI 10.1088/1751-8121/aca63a. https://arxiv.org/abs/2211.01869
- S. Kapodistria, T. Phung-Duc, J. Resing, *Linear birth/immigration-death process with binomial catastrophes*, 2015 preprint, DOI 10.1017/S0269964815000297. https://www.eurandom.tue.nl/reports/2015/006-report.pdf
- X. Chao, Y. Zheng, *Transient analysis of immigration birth-death processes with total catastrophes*, Probability in the Engineering and Informational Sciences 17 (2003), 83–106, DOI 10.1017/S0269964803171057.
