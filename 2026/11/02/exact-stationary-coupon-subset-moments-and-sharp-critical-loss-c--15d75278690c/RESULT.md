# Exact stationary coupon-subset moments and sharp critical-loss completion exponent

## Finding

Consider a finite *post-loss careless coupon collector*: among \(n\ge 1\) labels, at each integer time choose one uniformly, add it to the currently retained set, and then independently delete each retained label with probability \(p\in(0,1)\). Let \(S_t\) be the post-loss set, \(q=1-p\), and \(\pi_{n,p}\) the unique stationary law.

**Exact all-subset theorem.** For every specified subset \(A\subseteq[n]\) with \(|A|=k\), the stationary inclusion probability is
\[
 m_k:=\Pr_{\pi_{n,p}}(A\subseteq S)
 =\prod_{j=1}^{k}\frac{j q^j}{n(1-q^j)+j q^j},\qquad k=0,1,\ldots,n,
\]
with the empty product equal to one. This determines the entire exchangeable invariant law through
\[
\Pr_{\pi_{n,p}}(|S|=j)
 =\binom nj\sum_{r=0}^{n-j}(-1)^r\binom{n-j}{r}m_{j+r},\qquad 0\le j\le n.
\]
In particular the probability of the post-loss **fully collected** state is exactly
\[
 \rho_{n,p}:=\pi_{n,p}(\{[n]\})
 =\prod_{k=1}^{n}\frac{k(1-p)^k}{n(1-(1-p)^k)+k(1-p)^k}.
\]

**Sharp critical-loss theorem.** Fix \(c>0\), take integers \(n>c\), and set \(p_n=c/n\). Define
\[
 I(c)=\int_0^1\log\left(1+\frac{e^{cx}-1}{x}\right)\,dx,
\]
where the integrand has continuous value \(\log(1+c)\) at zero, and
\[
 A(c)=\exp\left\{\frac{\log(1+c)-c}{2}
 -\frac{c^2}{2}\int_0^1\frac{x e^{cx}}{x+e^{cx}-1}\,dx\right\}.
\]
The second integrand has continuous value \(1/(1+c)\) at zero. Then
\[
 \rho_{n,c/n}=A(c)\exp[-nI(c)]\bigl(1+O_c(n^{-1})\bigr).
\]
Writing \(T_{n,p}=\min\{t\ge1:S_t=[n]\}\) for the first fully collected post-loss state when \(S_0=\varnothing\),
\[
 \boxed{\displaystyle\lim_{n\to\infty}\frac1n\log\mathbb E_\varnothing T_{n,c/n}=I(c).}
\]
Moreover \(\log(1+c)<I(c)<c\) strictly. Thus the usual one-label marginal approximation yields a **strictly smaller** exponential rate than the exact critical-loss completion rate.

## Assumptions and scope

The draws are independent uniform choices on \([n]\). Deletion coins are mutually independent across labels and rounds, independent of the draws, and applied **after** acquisition; the newly drawn coupon can therefore be deleted immediately. The exact formula holds for every integer \(n\ge1\) and every \(p\in(0,1)\). The asymptotic theorem holds for any *fixed* real \(c>0\), along all integers \(n>c\). The stopping time starts from the empty set and is defined on post-loss states. This is a finite-state discrete-time chain, not a selected-label-only refresh chain or a global-reset chain.

## Proof

**1. Existence, exchangeability and subset recurrence.** There is a positive one-step probability of an all-deletion transition to the empty state; from the empty state any specified finite collection can be reached in finitely many rounds with positive probability by repeatedly drawing its labels and keeping all of them. Consequently the finite chain is irreducible. It is aperiodic, since staying empty in one round has probability \(p>0\). Thus there is a unique stationary measure. All label permutations preserve its transition kernel, hence its invariant law is exchangeable.

Fix \(A\) with \(|A|=k\ge1\). Under a stationary state before the draw, the event that all of \(A\) are present after adding the newly drawn label but before deletion has probability
\[
\left(1-\frac{k}{n}\right)m_k+\frac{k}{n}m_{k-1}.
\]
Indeed, a draw outside \(A\) requires \(A\) already present; for a draw of a specified label of \(A\), the other \(k-1\) specified labels must already be present. Independence of the subsequent \(k\) survival coins gives the exact stationary identity
\[
m_k=q^k\left[\left(1-\frac{k}{n}\right)m_k+\frac{k}{n}m_{k-1}\right].
\]
Rearranging produces
\[
\frac{m_k}{m_{k-1}}=\frac{kq^k}{n(1-q^k)+kq^k}.
\]
With \(m_0=1\) iteration proves the finite product formula, and in particular \(m_n=\rho_{n,p}\). To recover the full invariant law, for a fixed \(j\)-element set \(A\), finite Boolean-lattice inclusion-exclusion yields
\[
\Pr(S=A)=\sum_{r=0}^{n-j}(-1)^r\binom{n-j}{r}m_{j+r}.
\]
Summing over the \(\binom nj\) equally likely candidate sets proves the cardinality formula. All identities are exact, without an independence assumption on label indicators.

**2. Sharp invariant endpoint asymptotics.** Put \(\lambda_n=-n\log(1-c/n)\). Elementary Taylor expansion at fixed \(c\) gives
\[
\lambda_n=c+\frac{c^2}{2n}+O_c(n^{-2}).
\]
For \(\lambda>0\) and \(0<x\le1\), let
\[
f_\lambda(x)=-\log\left(1+\frac{e^{\lambda x}-1}{x}\right),\qquad f_\lambda(0)=-\log(1+\lambda).
\]
The quotient \((e^{\lambda x}-1)/x\) extends real-analytically to zero, locally uniformly in \(\lambda\); hence both \(f_\lambda\) and its first required derivatives have uniform boundedness on \([0,1]\) for \(\lambda\) in any compact positive interval. The product identity is equivalently
\[
\log\rho_{n,c/n}=\sum_{k=1}^n f_{\lambda_n}(k/n).
\]
One-term Euler–Maclaurin and uniform Taylor expansion in \(\lambda\) therefore imply
\[
\begin{split}
\log\rho_{n,c/n}
={}&n\int_0^1 f_c(x)\,dx
+\frac{c^2}{2}\int_0^1\partial_\lambda f_c(x)\,dx\\
&+\frac{f_c(1)-f_c(0)}2+O_c(n^{-1}).
\end{split}
\]
Here
\[
\partial_\lambda f_c(x)=-\frac{x e^{cx}}{x+e^{cx}-1},\quad
f_c(1)=-c,\quad f_c(0)=-\log(1+c).
\]
Substitution gives \(\log\rho=-nI(c)+\log A(c)+O_c(n^{-1})\), which exponentiates to the stated positive-prefactor asymptotic. The apparent removable singularity of \(\partial_\lambda f_c\) is assigned its continuous value \(-1/(1+c)\) at zero.

**3. From stationary mass to the mean hitting-time exponent.** Couple two versions of the chain using the same draw and the same independent per-label deletion coins. The update preserves set inclusion; discrepancies at any label can survive \(t\) rounds only if that label avoided deletion at every round, so the probability of any initial discrepancy remaining is at most \(nq^t\). Consequently, for every initial state \(x\),
\[
\left\|P_x^t-\pi_{n,p}\right\|_{\mathrm{TV}}\le nq^t.
\]
Coupling a chain started from \(\varnothing\) to one started in stationarity also maintains \(S_t^{\varnothing}\subseteq S_t^\pi\). Thus for every \(t\), \(\Pr_\varnothing(S_t=[n])\le\rho_{n,p}\). A union bound gives \(\Pr_\varnothing(T_{n,p}\le t)\le t\rho_{n,p}\); taking \(t=\lfloor(2\rho_{n,p})^{-1}\rfloor\) for small \(\rho\) yields \(\mathbb E_\varnothing T_{n,p}\ge \mathrm{const}/\rho_{n,p}\). For an explicit uniform formulation, the elementary sum of \(\Pr(T>t)\) for \(0\le t\le\lfloor(2\rho)^{-1}\rfloor\) implies \(\mathbb E_\varnothing T\ge (4\rho)^{-1}\) whenever \(\rho\le1/2\).

On the other hand, define
\[
h_n=\left\lceil\frac{\log(2n/\rho_{n,p})}{-\log q}\right\rceil.
\]
The mixing bound gives, **for every state** \(x\),
\[
\Pr_x(S_{h_n}=[n])\ge \rho_{n,p}-nq^{h_n}\ge\rho_{n,p}/2.
\]
Therefore \(\Pr_x(T_{n,p}\le h_n)\ge\rho_{n,p}/2\). Iterating over consecutive blocks using the Markov property bounds the first hitting time by a geometric number of blocks, whence
\[
\mathbb E_\varnothing T_{n,p}\le\frac{2h_n}{\rho_{n,p}}.
\]
For \(p=c/n\), the already proved asymptotic gives \(\log(1/\rho_{n,p})=nI(c)+O_c(1)\), while \(-\log q=\Theta_c(1/n)\); thus \(h_n=O_c(n^2)\). The two estimates sandwich \(\frac1n\log\mathbb ET\) between \(\frac1n\log(1/\rho)\) plus errors tending to zero. This proves the limiting exponent without assuming a rare-hitting exponential limit or equality of the mean hitting time and inverse stationary mass.

**4. Strict bounds on the exponent.** For \(x>0\), the function \((e^{cx}-1)/x\) is strictly increasing: its derivative has numerator \(e^{cx}(cx-1)+1>0\), as is seen by differentiating that numerator in \(cx\). It rises from \(c\) to \(e^c-1\) on \([0,1]\). The integrand defining \(I(c)\) therefore lies strictly between \(\log(1+c)\) and \(c\) on \((0,1)\), giving the stated strict inequalities.

## Verification

The accompanying standalone Python 3 standard-library script `VERIFY.py` independently builds exact cardinality transition matrices, solves their stationary equations by rational Gaussian elimination, verifies the subset moments and inclusion-exclusion inversion for the complete ranges \(1\le n\le8\) and \(p\in\{1/2,1/3,2/5\}\), and performs finite numerical checks of the stated first-order asymptotic for several \(c\) and \(n\). It completed **688 assertions**. Run `python3 VERIFY.py` from the extracted folder. The analytical recurrence, Euler–Maclaurin remainder and mixing/hitting inequalities—not these finite tests—prove the infinite assertions. Representative values are \(I(1)\approx0.836727862260\) and \(A(1)\approx0.595917718227\).

## Relationship to prior work

Cruciani and Dudeja (2026, arXiv:2602.20705v1) introduce exactly this post-loss chain, prove a metastable phase for \(p=c/n\), and analyze the mean under mean-field and unconditional bounds. Their one-label marginal is correct, but treating all labels as independently retained predicts the smaller exponent \(\log(1+c)\). They provide neither the full finite invariant subset product nor the sharp critical-loss completion exponent displayed here.

Long (2026, arXiv:2605.14511v1), particularly Section 5, studies the same post-loss process, establishes fixed-\(p\) stationary high-tail asymptotics and a fixed-\(p\) exponential hitting law. Those conclusions assume \(p\) does not shrink with \(n\); they do not yield the \(p=c/n\) rate by substitution, since their tail constants and \((1-p)^n\) change regimes. This theorem does not claim novelty for the fixed-\(p\) high-tail or stationary-entry results. Attrill and Garoni (2026, arXiv:2605.14206v1) examine a selected-label refresh chain rather than independent simultaneous post-draw deletion; it is a different model.

A published mathematical-record search and targeted searches using alternate descriptions (stationary factorial moments, subset-inclusion recursions, critical per-label deletion, sharp coupon completion rate) revealed no directly covering assertion in the accessible inspected sources. This is evidence of noncoverage by those sources, not a proof of absolute historical novelty; generic immigration–thinning identities and unindexed loss-chain papers are residual priority risks.

## Limitations

The asymptotic and hitting-time exponent are only for fixed \(c>0\) and \(n\to\infty\) with \(p_n=c/n\). The exact invariant formula holds at every finite \(n\) and \(0<p<1\), but no uniform expansion as \(c\) varies with \(n\) is asserted. The stationary probability prefactor \(A(c)\) is **not** asserted to be the expected hitting-time prefactor. No sharp mean prefactor, distributional exponential hitting limit, quasi-stationary law, optimal sampling policy, or nonuniform-coupon extension is proved. Numerical experiments were finite and are not substitutes for the argument. The mathematical priority comparison is self-review and accessible-source based; comprehensive independent historical adjudication is not claimed.

## References

1. E. Cruciani and A. Dudeja, *The Careless Coupon Collector's Problem*, arXiv:2602.20705v1 (24 February 2026), https://arxiv.org/html/2602.20705v1 .
2. C. D. Long, *Clumsy and Careless: Stationary-Entry Flux in Non-monotone Coupon Collectors*, arXiv:2605.14511v1 (14 May 2026), https://arxiv.org/html/2605.14511v1 .
3. L. J. Attrill and T. M. Garoni, *The clumsy coupon collector's problem*, arXiv:2605.14206v1 (14 May 2026), https://arxiv.org/abs/2605.14206 .
