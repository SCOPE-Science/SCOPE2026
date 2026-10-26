# The critical strong-transience boundary for a nearest-neighbour birth–death chain

## Finding

Let \(X=(X_n)_{n\ge0}\) be an irreducible birth–death chain on \(\mathbb Z_{\ge0}\), with \(P(X_{n+1}=1\mid X_n=0)=1\), and with transitions \(P(x,x+1)=p_x\), \(P(x,x-1)=q_x=1-p_x\) for every \(x\ge1\), where \(p_x,q_x>0\). Write \(\mu(x)=p_x-q_x\). If
\[
\mu(x)=\frac{3}{2x}+o\!\left(\frac{1}{x(\log x)^2}\right)
\quad (x\to\infty),
\]
then \(X\) is transient but its first return time \(\tau_0=\inf\{n\ge1:X_n=0\}\) has infinite conditional mean:
\[
\mathbb E_0[\tau_0\mid \tau_0<\infty]=\infty.
\]
Thus this class is not strongly transient, despite lying on the first-moment critical boundary.

## Assumptions and scope

The state space is the nonnegative integers. From each positive state the chain moves exactly one step up or down, with strictly positive probabilities \(p_x,q_x\) summing to one; from zero it moves to one. The displayed drift condition is a deterministic asymptotic along integer states, and \(\log\) denotes the natural logarithm. The error assumption is stronger than \(o(1/(x\log x))\). No claim is made for chains with larger jumps, holding probabilities at positive states, weaker drift errors, or higher return-time moments.

For this chain the conditional second increment moment is \(1\). The Lamperti transience criterion applies with \(c=3/2\) and \(s^2=1\), since \(2c=3>s^2\). The critical strong-transience equality for moment order \(\beta=1\), namely \(2c=(2\beta+1)s^2\), is satisfied exactly.

## Proof

Put \(H_0=\inf\{n\ge0:X_n=0\}\) for a chain started from a positive state. Define
\[
r_0=1,\qquad r_n=\prod_{k=1}^{n}\frac{q_k}{p_k}.
\]
For large \(k\), \(\mu(k)=O(k^{-1})\), so
\[
\log\frac{q_k}{p_k}
=\log(1-\mu(k))-\log(1+\mu(k))
=-2\mu(k)+O(k^{-3})
=-\frac{3}{k}+o\!\left(\frac{1}{k(\log k)^2}\right)+O(k^{-3}).
\]
The error terms have convergent tails, and the tail of the little-\(o\) term is \(o(1/\log n)\). Using \(\sum_{k\le n}k^{-1}=\log n+C+O(n^{-1})\), there is a constant \(C_0>0\) such that
\[
r_n=C_0n^{-3}\left(1+o\!\left(\frac1{\log n}\right)\right).
\]
Consequently, for \(S_n=\sum_{k=n}^{\infty}r_k\),
\[
S_n=\frac{C_0}{2}n^{-2}\left(1+o\!\left(\frac1{\log n}\right)\right).
\]

The hitting probability is harmonic away from zero: \(p_n(h(n+1)-h(n))=q_n(h(n)-h(n-1))\). Thus its successive differences are proportional to the scale products \(r_n\); imposing \(h(0)=1\) and \(h(n)\to0\) gives the birth–death hitting-probability formula \(h(n)=P_n(H_0<\infty)=S_n/S_0\). It follows that
\[
\frac{h(n+1)}{h(n)}
=1-\frac{r_n}{S_n}
=1-\frac2n+o\!\left(\frac1{n\log n}\right),
\qquad
\frac{h(n-1)}{h(n)}
=1+\frac2n+o\!\left(\frac1{n\log n}\right).
\]
Use the Doob \(h\)-transform, which gives the chain conditioned to hit zero:
\[
\widetilde p_n=p_n\frac{h(n+1)}{h(n)},\qquad
\widetilde q_n=q_n\frac{h(n-1)}{h(n)}.
\]
Because \(p_n+q_n=1\), its drift satisfies
\[
\widetilde\mu(n)=\widetilde p_n-\widetilde q_n
=\mu(n)-\frac2n+o\!\left(\frac1{n\log n}\right)
=-\frac1{2n}+o\!\left(\frac1{n\log n}\right).
\]

Define positive birth–death weights by \(\pi_1=1\) and
\[
\pi_{n+1}=\pi_n\frac{\widetilde p_n}{\widetilde q_{n+1}}.
\]
Since \(\widetilde p_n=(1+\widetilde\mu(n))/2\) and \(\widetilde q_n=(1-\widetilde\mu(n))/2\),
\[
\log\frac{\widetilde p_n}{\widetilde q_{n+1}}
=\widetilde\mu(n)+\widetilde\mu(n+1)+O(n^{-2})
=-\frac1n+o\!\left(\frac1{n\log n}\right).
\]
Summing gives
\[
\pi_n=\frac1n\exp\!\bigl(o(\log\log n)\bigr).
\]
In particular, eventually \(\pi_n\ge c_1/[n(\log n)^{1/2}]\) for some \(c_1>0\), so \(\sum_{n\ge1}\pi_n=\infty\).

Let \(m_i=\widetilde{\mathbb E}_i H_0\). Suppose for contradiction that \(m_1<\infty\). Since the conditioned chain has positive probability to reach each \(i\) before zero, the Markov property implies that every \(m_i\) is finite. Also \(m_i\ge m_{i-1}\), because a nearest-neighbour path from \(i\) to zero must first hit \(i-1\). Set \(d_i=m_i-m_{i-1}\ge0\), with \(m_0=0\). The first-step equations yield
\[
\widetilde q_i d_i-\widetilde p_i d_{i+1}=1.
\]
Multiplying by \(\pi_i\), using \(\pi_i\widetilde p_i=\pi_{i+1}\widetilde q_{i+1}\), and summing from \(i=1\) to \(N\) gives
\[
\widetilde q_1m_1-\pi_{N+1}\widetilde q_{N+1}d_{N+1}
=\sum_{i=1}^{N}\pi_i.
\]
The second term on the left is nonnegative, so \(\widetilde q_1m_1\ge\sum_{i=1}^{N}\pi_i\) for every \(N\), contradicting divergence of the weights. Therefore \(\widetilde{\mathbb E}_1H_0=\infty\).

The Doob-transform conditioning identity gives
\[
\widetilde{\mathbb E}_1H_0
=\mathbb E_1[H_0\mid H_0<\infty].
\]
Since the original chain moves from zero to one in one step, \(\tau_0=1+H_0\) after that first step. Hence \(\mathbb E_0[\tau_0\mid\tau_0<\infty]=\infty\), as claimed.

## Verification

The proof is analytic and covers the full stated asymptotic class. The accompanying exact-rational script checks a representative chain with \(p_1=q_1=1/2\) and \(p_x=(2x+3)/(4x)\), \(q_x=(2x-3)/(4x)\) for \(x\ge2\). For that example, the scale products, hitting probabilities, transformed transition probabilities, and reversible weights have closed forms; the script checks their identities for indices \(2\) through \(1000\). These finite checks are consistency checks only and are not used as a proof of the infinite divergence or of the general theorem.

## Relationship to prior work

Lo, Menshikov, and Wade establish strict-inequality criteria for \(\beta\)-strong transience in the Lamperti regime. Their Theorem 3.1 excludes the equality case \(2c=(2\beta+1)s^2\); Remark 3.2(a) explicitly describes the boundary as unresolved and suggests that a stronger logarithmic error assumption may settle it. Remark 5.3(d) notes that nearest-neighbour chains permit a simpler hitting-probability ratio argument. The present theorem proves only the \(\beta=1\) boundary for birth–death chains under the stated log-squared error assumption. It does not settle the full boundary for arbitrary \(\beta\), the weaker error assumption, or bounded-jump chains.

## Limitations

The result is restricted to irreducible nearest-neighbour birth–death chains with the stated boundary transition and drift asymptotic. It does not imply that every chain satisfying only \(\mu(x)=3/(2x)+o(1/(x\log x))\) fails to be strongly transient. It also does not classify conditional moments of order \(\beta\ne1\). The finite exact-rational example is illustrative, not a substitute for the analytic proof.

## References

Chak Hei Lo, Mikhail V. Menshikov, and Andrew R. Wade, “Strong transience for one-dimensional Markov chains with asymptotically zero drifts,” *Stochastic Processes and their Applications* 170 (2024), article 104260. Earliest public preprint: arXiv:2208.12955, 27 August 2022. DOI: 10.1016/j.spa.2023.104260.
