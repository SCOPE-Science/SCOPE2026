# Local return asymptotics at a logarithmic Lamperti boundary

## Finding

For every \(\beta>0\), \(d\in\mathbb R\), and irreducible nearest-neighbour birth–death chain \(X\) on \(\mathbb Z_{\ge0}\) with \(P(0,1)=1\) and drift \(\mu_x=p_x-q_x=\frac{\beta+\frac12}{x}+\frac{d}{x\log x}+o\!\left(\frac{1}{x(\log x)^2}\right)\), the chain is transient and there is a constant \(C\in(0,\infty)\) such that \(P_0(X_{2n}=0)\sim C n^{-\beta-1}(\log n)^{-2d}\); consequently, \(\mathbb E_0[\tau_0^\beta\mid\tau_0<\infty]\) is finite exactly when \(d>\frac12\).

Here \(p_x=P(x,x+1)\), \(q_x=P(x,x-1)=1-p_x\) for \(x\ge1\), and \(\tau_0=\inf\{n\ge1:X_n=0\}\). The asymptotic statement is along integer \(n\to\infty\); odd-time return probabilities vanish by parity.

## Assumptions and scope

The state space is \(\mathbb Z_{\ge0}\). The chain is irreducible, has nearest-neighbour steps, and leaves zero for one with probability one. For all sufficiently large \(x\), its upward-minus-downward drift has the displayed expansion, with fixed \(\beta>0\), fixed \(d\in\mathbb R\), and a remainder whose ratio to \(1/[x(\log x)^2]\) tends to zero. All finite-state transition probabilities are strictly positive, so the chain is uniformly elliptic after combining the asymptotic condition with the finite prefix. No claim is made for jumps larger than one or for a weaker, nonsummable remainder.

## Proof

Put \(\rho_0=1\) and \(\rho_x=\prod_{j=1}^{x}q_j/p_j\). Since \(\log(q_x/p_x)=-2\mu_x+O(\mu_x^3)\), summation gives
\[
\rho_x\sim K x^{-2\beta-1}(\log x)^{-2d},\qquad K>0.
\]
Thus \(\sum_{x\ge0}\rho_x<\infty\), so the birth–death chain is transient. Its hitting probability \(h(x)=P_x(\tau_0<\infty)\) has the exact scale-function representation
\[
h(x)=\frac{\sum_{k=x}^{\infty}\rho_k}{\sum_{k=0}^{\infty}\rho_k}.
\]
Regular-variation summation and the local ratio of consecutive scale terms yield
\[
\frac{h(x+1)}{h(x)}=1-\frac{2\beta}{x}-\frac{2d}{x\log x}+O\!\left(\frac{1}{x(\log x)^2}\right).
\]
The Doob \(h\)-transform conditions the excursion after its first step on eventual return to zero. For \(x\ge1\), its transitions are \(p_x^h=p_xh(x+1)/h(x)\) and \(q_x^h=q_xh(x-1)/h(x)\); at zero it steps to one. Consequently its drift is
\[
\mu_x^h=p_x^h-q_x^h=\frac{\frac12-\beta}{x}-\frac{d}{x\log x}+O\!\left(\frac{1}{x(\log x)^2}\right).
\]
This transformed reflecting chain is uniformly elliptic and is in the Bessel-like regime of Alexander's first-return theorem. In that theorem's notation, \(\delta=2\beta-1>-1\) and \(\kappa=(1+\delta)/2=\beta\). The scale-product slowly varying factor is \(L(x)\sim K' (\log x)^{-2d}\), with \(K'>0\): the \(1/(x\log x)\) term contributes \(-2d\log\log x\) to the log of the scale product, while the \(O(1/(x\log^2 x))\) remainder has a convergent sum. Alexander's theorem therefore gives, for the transformed first-return mass along even times,
\[
P_0^h(\tau_0=2n)\sim K'' n^{-\beta-1}(\log n)^{-2d},\qquad K''>0.
\]
This is exactly the conditional first-return mass of the original chain. Write \(f_n=P_0(\tau_0=2n)\) and \(r=P_0(\tau_0<\infty)\in(0,1)\). Then \(f_n\sim rK''n^{-\beta-1}(\log n)^{-2d}\). The sequence is regularly varying with exponent \(-\beta-1<-1\), hence locally subexponential. The defective renewal equation for \(u_n=P_0(X_{2n}=0)\), \(u_0=1\), is \(u_n=\sum_{j=1}^{n}f_j u_{n-j}\); the local defective-renewal asymptotic gives \(u_n\sim f_n/(1-r)^2\). Absorbing positive constants proves the stated return-probability asymptotic.

Finally, the conditional moment is proportional to
\[
\sum_{n\ge1} n^\beta P_0^h(\tau_0=2n)\asymp\sum_{n\ge2}\frac{1}{n(\log n)^{2d}}.
\]
The integral test gives convergence exactly when \(2d>1\). This proves the threshold, including divergence at \(d=1/2\).

## Verification

The proof uses four analytic steps: the exact birth–death scale formula; the adjacent-ratio expansion under the stated logarithmic remainder; the Doob-transform drift calculation; and the first-return/local defective-renewal asymptotics. The parameter map is \(\delta=2\beta-1\), so Alexander's condition \(\delta>-1\) holds for every allowed \(\beta>0\). The return-mass exponent is \(\beta+1\), and the logarithmic factor is \((\log n)^{-2d}\); the moment test is therefore the ordinary series \(\sum 1/[n(\log n)^{2d}]\). No finite computation is used as a substitute for the asymptotic proof. The positive constant is not simplified into a closed expression in the full transition sequence.

## Relationship to prior work

Lo, Menshikov, and Wade's 2022 paper classifies conditional return-time moments away from the critical equality and explicitly notes that the boundary and a transient-chain local-limit estimate are not covered by their theorem. Alexander's 2009 theorem supplies first-return asymptotics for recurrent reflecting Bessel-like walks. The present argument applies that result after conditioning a transient birth–death excursion to return, then transfers the regularly varying first-return mass through the defective renewal equation. Neither inspected source states the resulting logarithmic local-return asymptotic in the original transient-chain parameters. The result is limited to nearest-neighbour chains and the displayed second-order drift expansion.

## Limitations

The coefficient threshold depends on the logarithmic correction and does not follow from the leading \((\beta+1/2)/x\) term alone. The summable remainder assumption is material: a weaker remainder can introduce an additional slowly varying factor and alter the boundary test. The local renewal step uses the standard local-subexponential theorem for regularly varying sequences with total mass below one. This is a mathematical derivation from existing tools, not a claim of independent priority certification; independent audit has not been performed.

## References

1. C. H. Lo, M. V. Menshikov, and A. R. Wade, “Strong transience for one-dimensional Markov chains with asymptotically zero drifts,” arXiv:2208.12955v1, first posted 27 August 2022; Theorem 3.1 and Remarks 3.2, 5.3.
2. K. S. Alexander, “Excursions and local limit theorems for Bessel-like random walks,” arXiv:0912.4550v1, first posted 23 December 2009; Theorem 2.1.
3. K. Wang and Y. Wang, “Equivalent conditions of local asymptotics for the solutions of defective renewal equations, with applications,” *Acta Mathematicae Applicatae Sinica* 26 (2010), 503–512, DOI 10.1007/s10255-010-0019-9.
4. S. Foss, D. Korshunov, and S. Zachary, *An Introduction to Heavy-Tailed and Subexponential Distributions*, 2nd ed., Springer, 2013, Chapter 5.
