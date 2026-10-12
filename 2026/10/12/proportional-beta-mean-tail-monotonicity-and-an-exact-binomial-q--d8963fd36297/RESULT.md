# Proportional-beta mean-tail monotonicity and an exact binomial quantile threshold

## Finding

For every \(p\in(0,1)\) and \(\tau>0\), let
\[
X_{p,\tau}\sim\operatorname{Beta}(p\tau,(1-p)\tau),
\qquad F_p(\tau)=\Pr(X_{p,\tau}\le p).
\]
If \(p>1/2\), then \(F_p\) is **strictly increasing** on \((0,\infty)\), with
\[
1-p<F_p(\tau)<\frac12,\qquad
\lim_{\tau\downarrow0}F_p(\tau)=1-p,\qquad
\lim_{\tau\to\infty}F_p(\tau)=\frac12.
\]
If \(p<1/2\), the function is strictly decreasing with the same two endpoint limits, in reverse order; for \(p=1/2\), it is identically \(1/2\).

In particular, for every integer \(n\ge3\), the sequence
\[
a_{n,t}=\Pr\!\left\{\operatorname{Bin}(nt-1,1/n)<t\right\},
\qquad t=1,2,\ldots,
\]
is strictly increasing, while for \(n=2\) it equals \(1/2\) identically. Thus, for every integer \(n\ge2\),
\[
\boxed{\inf_{t\ge1}a_{n,t}=a_{n,1}=\left(1-\frac1n\right)^{n-1}.}
\]
This settles the exact binomial-tail conjecture in Remark 2 of Babichenko, Feldman, Holzman, and Narayan [1]. As their remark explains, this is the precise finite-agent critical quantile for feasibility of quantile shares over matroid-rank valuations; it does not settle the separate universal-feasibility conjectures for arbitrary valuations.

## Assumptions and scope

All beta shapes are strictly positive; \(p\) and \(\tau\) are real and range over the indicated open intervals. The beta distribution has density proportional to \(x^{p\tau-1}(1-x)^{(1-p)\tau-1}\) on \((0,1)\). The binomial consequence assumes integers \(n\ge2\), \(t\ge1\), and ordinary independent Bernoulli trials with success probability \(1/n\). Strictness for the discrete sequence holds precisely when \(n>2\).

## Proof

**1. Paired relative-entropy level sets.** Fix \(1/2<p<1\) and put
\[
A=p(1-p),\quad B=2p-1>0,\quad \rho=\frac{1-p}{p}<1,
\quad H(x)=p\log\frac p x+(1-p)\log\frac{1-p}{1-x}.
\]
The strictly convex function \(H\) decreases from infinity to zero on \((0,p)\) and increases from zero to infinity on \((p,1)\). For each \(s>0\), write its two inverse branches as
\[
x_-(s)=p-u(s),\qquad x_+(s)=p+v(s),
\]
where \(0<u(s)<p\), \(0<v(s)<1-p\), and \(H(p-u)=H(p+v)=s\). Both \(u\) and \(v\) increase continuously with \(s\). We prove that their ratio \(r(s)=v(s)/u(s)\) decreases strictly from \(1\) to \(\rho\).

Put \(D_-(w)=H(p-w)\) and \(D_+(w)=H(p+w)\), on their natural domains. Direct differentiation gives
\[
D_-'(w)=\frac{w}{A+Bw-w^2},\qquad
D_+'(w)=\frac{w}{A-Bw-w^2}.
\]
First, if \(0<w<p\), the identity
\[
[A-B\rho w-\rho^2w^2]-\rho^2[A+Bw-w^2]
=\frac{(1-p)(p-w)B}{p^2}>0
\]
implies \(\frac{d}{dw}D_+(\rho w)<D_-'(w)\). Integration from zero gives \(D_+(\rho w)<D_-(w)\). Thus \(v/u>\rho\). Conversely, if \(w<1-p\), then \(D_+'(w)>D_-'(w)\), so \(D_+(w)>D_-(w)\); if \(w\ge1-p\), then \(v<1-p\le w\) automatically. In either case \(v/u<1\). Therefore \(\rho<r(s)<1\).

For any fixed \(r\in[\rho,1]\), wherever \(0<w<p\) and \(rw<1-p\), consider the derivative ratio
\[
R_r(w)=\frac{\frac{d}{dw}D_+(rw)}{D_-'(w)}
=\frac{r^2(A+Bw-w^2)}{A-Brw-r^2w^2}.
\]
Its derivative is
\[
R_r'(w)=\frac{r^2(1+r)J_r(w)}{(A-Brw-r^2w^2)^2},\qquad
J_r(w)=AB-2A(1-r)w+Brw^2.
\]
The expression \(J_r(w)\) is increasing in \(r\), because \(\partial_rJ_r(w)=2Aw+Bw^2>0\); moreover,
\[
J_\rho(w)=\frac{B(1-p)(p-w)^2}{p}>0.
\]
Hence \(R_r\) is strictly increasing. Integrating the numerator and denominator of the ratio from zero shows that
\[
Q_r(w):=\frac{D_+(rw)}{D_-(w)}
=\frac{\int_0^w R_r(z)D_-'(z)\,dz}{\int_0^w D_-'(z)\,dz}
\]
is strictly increasing wherever defined: it is a weighted running average of the strictly increasing function \(R_r\), with positive weights.

Let \(0<u_1<u_2<p\), and let \(r_i=v(u_i)/u_i\) solve \(D_+(r_i u_i)=D_-(u_i)\). If \(r_1u_2\ge1-p\), then \(r_2u_2<1-p\le r_1u_2\) and \(r_2<r_1\). Otherwise, \(Q_{r_1}(u_1)=1\) and strict increase yields \(Q_{r_1}(u_2)>1\), which again forces \(r_2<r_1\) since \(D_+\) is strictly increasing. Therefore \(r\) is strictly decreasing with \(s\). Taylor expansion of \(H\) at \(p\) gives \(r(s)\to1\) as \(s\downarrow0\), while both inverse branches approach their respective endpoints as \(s\to\infty\), so \(r(s)\to(1-p)/p=\rho\).

**2. Exponential-tilt representation.** Change coordinates to the log-odds \(y=\log(x/(1-x))\). Since \(dx=x(1-x)\,dy\), the beta density times \(dx\) is, up to a constant independent of \(y\), exactly \(e^{-\tau H(x(y))}\,dy\). As
\[
\frac{dH}{dy}=x-p,
\]
the energy coordinate \(s=H(x)\) has left-branch Jacobian \(1/u(s)\) and right-branch Jacobian \(1/v(s)\). Consequently, with
\[
w(s)=\frac1{u(s)}+\frac1{v(s)},\qquad
k(s)=\frac{1/u(s)}{1/u(s)+1/v(s)}=\frac{r(s)}{1+r(s)},
\]
we have the exact representation
\[
F_p(\tau)=\frac{\int_0^\infty e^{-\tau s}w(s)k(s)\,ds}
{\int_0^\infty e^{-\tau s}w(s)\,ds}.
\]
The denominator is finite and positive for every \(\tau>0\), and \(k\) is continuous and strictly decreasing with endpoint values \(k(0+)=1/2\), \(k(\infty)=1-p\). When \(\tau\) increases, the probability law with density proportional to \(e^{-\tau s}w(s)\) becomes strictly smaller in likelihood-ratio order: for \(\tau_2>\tau_1\), its density ratio is a positive constant times \(e^{-(\tau_2-\tau_1)s}\), strictly decreasing in \(s\). Integrating the strictly decreasing function \(k\) therefore gives \(F_p(\tau_2)>F_p(\tau_1)\), as well as \(1-p<F_p(\tau)<1/2\).

As \(\tau\to\infty\), these tilted laws concentrate near \(s=0\), whence \(F_p(\tau)\to1/2\). As \(\tau\downarrow0\), their mass escapes every bounded \(s\)-interval: indeed \(\int_0^\infty w(s)\,ds=\infty\), since this is precisely the total length of the log-odds line, whereas \(\int_0^S w(s)\,ds<\infty\) for finite \(S\). Therefore \(F_p(\tau)\to1-p\). If \(p<1/2\), reflect the beta variable using \(1-X_{p,\tau}\overset{d}=X_{1-p,\tau}\) and continuity to reverse monotonicity. Symmetry gives \(F_{1/2}(\tau)=1/2\).

**3. Binomial consequence.** For positive integers \(n,t\), the binomial–beta identity is
\[
\Pr\{\operatorname{Bin}(nt-1,1/n)\le t-1\}
=I_{1-1/n}((n-1)t,t)
=F_{(n-1)/n}(nt).
\]
For \(n\ge3\), the beta mean \((n-1)/n\) exceeds \(1/2\), so the right-hand side increases strictly with \(t\). At \(t=1\) the binomial event is the zero-success event, giving \(((n-1)/n)^{n-1}\). For \(n=2\), beta symmetry gives constant probability \(1/2\). This proves the asserted infimum and all strictness statements.

## Verification

Run `python3 check_beta_binomial.py` from this directory. This standard-library-only verifier computes binomial-tail probabilities as exact rational numbers for \(2\le n\le25\), \(1\le t\le25\), checks all consecutive inequalities and the exact initial values, and tests the derivative polynomial identity and positivity at 3,469 rational parameter triples. The run produced: `PASS: 600 exact binomial tail values; 576 exact consecutive comparisons; 3469 exact rational derivative checks`. These are finite independent consistency checks; the quantified theorem follows from the preceding analytic proof, not from any grid or numerical approximation.

## Relationship to prior work

Babichenko, Feldman, Holzman, and Narayan [1, Remark 2] introduce this precise binomial infimum and explicitly conjecture its attainment at \(t=1\), obtaining an asymptotic estimate instead. Their valuation-theoretic argument identifies its implication for matroid-rank quantile feasibility, but does not establish the discrete monotonicity. Hornik [2] proves that the beta mean CDF decreases when one shape parameter increases **and the other stays fixed**; this does not imply the simultaneous proportional-shape trend, which has competing effects. Karp [3] studies separate-coordinate log-concavity and related Turán expressions; those statements likewise do not imply the sign of a derivative along a proportional-shape ray. Leobacher and Steinicke [4, Section 2 and Lemma 18] prove a related incomplete-beta monotonicity when one beta shape stays fixed and the other grows, but not when **both** shapes grow proportionally. The new argument uses paired equal-relative-entropy branches to handle precisely that latter variation.

## Limitations

This result establishes only the stated beta and binomial distributions and the quantile-threshold consequence already described in [1]. It does not prove a general monotone-likelihood-ratio ordering of beta laws on their original sample space, nor the Erdős matching conjectures, nor universal feasibility for unrestricted monotone valuations. The published-source priority comparison covers the identified works and targeted searches but cannot exclude an earlier equivalent theorem under different terminology.

## References

[1] Y. Babichenko, M. Feldman, R. Holzman, and V. V. Narayan, *Fair Division via Quantile Shares*, arXiv:2312.01874v1 (first public version 4 December 2023), Remark 2 and Proposition 6. https://arxiv.org/pdf/2312.01874

[2] K. Hornik, *Two Monotonicity Results for Beta Distribution Functions*, Entropy **26** (2024), 938. https://doi.org/10.3390/e26110938

[3] D. B. Karp, *Normalized Incomplete Beta Function: Log-Concavity in Parameters and Other Properties*, arXiv:1509.05120v1 (2015), §§1–3. https://arxiv.org/pdf/1509.05120

[4] G. Leobacher and A. Steinicke, *A Dice Game, a Multinomial Walk, and the Inverted Dirichlet Distribution*, arXiv:2605.21424v1 (2026), §2 and Lemma 18. https://arxiv.org/html/2605.21424v1
