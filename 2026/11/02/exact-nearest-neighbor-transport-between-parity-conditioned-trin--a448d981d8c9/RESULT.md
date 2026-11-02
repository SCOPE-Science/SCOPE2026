# Exact nearest-neighbor transport between parity-conditioned trinomial sums

## Finding
Let \(n\ge 1\), and let \(X_1,\ldots,X_n\) be independent random variables supported on \(\{0,\frac12,1\}\), with arbitrary (possibly zero) probabilities. Set \(S=\sum_{i=1}^n X_i\). Assume \(\Pr(S\in\mathbb Z)>0\) and \(\Pr(S\in\mathbb Z+\frac12)>0\). Write \(E\) and \(O\) for the respective conditional laws of \(S\).

For every integer \(k\), their distribution functions obey the sharp neighboring-lattice sandwich
\[
\Pr(O\le k-\tfrac12)\le\Pr(E\le k)\le\Pr(O\le k+\tfrac12).
\]
Consequently, there exists a coupling \((\widehat E,\widehat O)\) with these marginals such that
\[
|\widehat E-\widehat O|=\tfrac12\quad\text{almost surely}.
\]
For every \(1\le p\le\infty\), the exact Wasserstein distance is therefore
\[
\boxed{W_p(E,O)=\tfrac12.}
\]
In particular, \(|\mathbb E[E]-\mathbb E[O]|\le\frac12\), sharply improving the bound of \(1\) obtained by combining the two separate mean comparisons in the motivating work. The distance and mean constants are attainable.

## Assumptions and scope
Write \(L_i=\Pr(X_i=0)\), \(T_i=\Pr(X_i=\frac12)\), and \(W_i=\Pr(X_i=1)\), with \(L_i,T_i,W_i\ge0\) and \(L_i+T_i+W_i=1\). No identical-distribution assumption is made. Both conditional parity events must have positive probability. A Wasserstein distance of order \(p\in[1,\infty)\) is the infimum over couplings of the \(p\)-th absolute displacement moment to power \(1/p\); the order-\(\infty\) distance minimizes the essential-supremum displacement.

## Proof
**1. Integer rescaling and parity polynomials.** Set \(H=2S\) and
\[
F(w)=\mathbb E[w^H]=\prod_{i=1}^n(L_i+T_iw+W_iw^2)=P(w^2)+wQ(w^2).
\]
Then \(P(z)/P(1)\) is the probability generating function of \(E\), and \(Q(z)/Q(1)\) is that of \(O-\frac12\). This follows by extracting the even and odd coefficients of \(F\).

**2. Strictly interlacing zeros for positive parameters.** Initially suppose every \(L_i,T_i,W_i\) is strictly positive. For \(x>0\), the complex number \(L_i-W_ix^2+\mathrm{i}T_ix\) has a continuous argument \(\theta_i(x)\in(0,\pi)\), with \(\theta_i(0+)=0\), \(\theta_i(\infty)=\pi\), and
\[
\theta'_i(x)=\frac{T_i(L_i+W_ix^2)}{(L_i-W_ix^2)^2+T_i^2x^2}>0.
\]
Hence the argument \(\theta(x)=\sum_i\theta_i(x)\) of \(F(\mathrm{i}x)\) increases strictly from \(0\) to \(n\pi\). Since
\[
F(\mathrm{i}x)=P(-x^2)+\mathrm{i}xQ(-x^2),
\]
the \(n\) successive crossings \(\theta=(j-\frac12)\pi\) are exactly the positive \(x\)-zeros of \(P(-x^2)\), and the \(n-1\) crossings \(\theta=j\pi\) are the positive zeros of \(Q(-x^2)\). Degree counting excludes additional zeros. Therefore, if the negative roots of \(P\) are \(-a_1,\ldots,-a_n\), and those of \(Q\) are \(-b_1,\ldots,-b_{n-1}\), we have
\[
0<a_1<b_1<a_2<b_2<\cdots<b_{n-1}<a_n.
\]
This also independently verifies the orientation of the Hermite–Biehler interlacing required here.

**3. Two stochastic orderings.** Factoring the normalized polynomials gives a Poisson-binomial representation: \(E\) is a sum of \(n\) independent Bernoulli random variables with probabilities \(u_i=(1+a_i)^{-1}\); \(O-\frac12\) is a sum of \(n-1\) independent Bernoulli variables with probabilities \(v_i=(1+b_i)^{-1}\). The ordered parameters satisfy
\[
u_1>v_1>u_2>v_2>\cdots>v_{n-1}>u_n.
\]
Using common independent uniforms for the first \(n-1\) pairs \((u_i,v_i)\), with one extra independent \(u_n\)-Bernoulli, proves \(O-\frac12\le_{\mathrm{st}}E\). Using common uniforms for \((v_i,u_{i+1})\), with one extra independent \(u_1\)-Bernoulli, proves \(E\le_{\mathrm{st}}O+\frac12\). Together they give the stated distribution-function sandwich.

**4. One coupling realizes both bounds.** Put \(K=O-\frac12\). The stochastic inequalities read \(K\le_{\mathrm{st}}E\le_{\mathrm{st}}K+1\). Coupling \(E\) and \(K\) by the same uniform quantile variable gives \(0\le E-K\le1\) almost surely. Since both are integers, the difference is either \(0\) or \(1\), and therefore \(|E-(K+\frac12)|=\frac12\) surely. Every coupling of an integer-valued and half-integer-valued random variable incurs displacement at least \(\frac12\); hence the constructed coupling is simultaneously optimal for all Wasserstein orders, including \(\infty\).

**5. Boundary probabilities.** Replace each probability in every triple by \((p+\delta)/(1+3\delta)\) for \(\delta>0\). All triples become positive, so the sandwich holds. As \(\delta\downarrow0\), the two parity events retain positive limiting probabilities by assumption, and the two conditional distributions converge coefficientwise on their finite supports. The sandwich passes to the limit, and the quantile construction again gives the exact transport claim.

**6. Sharpness.** For \(n=1\), take \(\Pr(X_1=0)=\Pr(X_1=\frac12)=\frac12\) and \(\Pr(X_1=1)=0\). Then \(E\equiv0\) and \(O\equiv\frac12\), giving equality in the mean bound as well as in every transport identity.

## Verification
The standalone Python 3 script `verify.py` uses exact integer coefficient convolution. It exhausts all \(15^n\) choices of triples with denominator \(4\) for each \(n=1,2,3,4\), including zero-weight boundaries, and checks every CDF sandwich by integer cross-products. It also tests deterministic pseudorandom rational triples for \(n\le12\), and explicitly constructs the monotone quantile transport with rational masses. The script has no external dependencies. Run `python3 verify.py`; its baseline output is recorded in `VERIFICATION.md`. Finite checks are diagnostic; the infinite quantifiers are justified by the six analytic proof steps above.

## Relationship to prior work
Broadie and Petkova (2026) proved that the two parity-conditioned laws are Poisson-binomial and that each conditional mean differs from the unconditional mean by at most \(\frac12\), yielding an inter-parity mean bound of \(1\). They also studied modes and optimal matchups. Their full paper does not state a joint nearest-neighbor coupling or any Wasserstein distance. The proof here strengthens their distribution comparison to an explicit optimal coupling, using an oriented zero-interlacing argument and two Bernoulli stochastic orders. The Hermite–Biehler theory and Hurwitz-stability results underlying the algebra are classical; their existence is not presented as new. Earlier results on modal locations do not imply a coupling of the complete distributions, although the relevant polynomial machinery is shared.

## Limitations
Independence of the summands and the exact three-point support \(\{0,\frac12,1\}\) are essential assumptions. Both parity events must have positive probability. This theorem does not imply that arbitrary parity-conditioned distributions, or sums of dependent summands, have the same transport distance. The result does not classify optimal couplings uniquely.

## References
1. M. Broadie and I. Petkova, *On the structure of the Poisson trinomial distribution*, arXiv:2603.09019v1, first public March 9, 2026. https://arxiv.org/html/2603.09019v1
2. O. Holtz, *Hermite–Biehler, Routh–Hurwitz, and total positivity*, Linear Algebra and its Applications 372 (2003), 105–110. https://doi.org/10.1016/S0024-3795(03)00501-9
3. J. N. Darroch, *On the distribution of the number of successes in independent trials*, Annals of Mathematical Statistics 35 (1964), 1317–1321. https://doi.org/10.1214/aoms/1177703278
