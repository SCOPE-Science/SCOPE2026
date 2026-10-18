# Exponential range-hitting coupling and a joint Gaussian–geometric law for biased cycle coverage

## Finding

Let \(1/2<p<1\), \(q=1-p\), \(\mu=p-q>0\), and \(r=q/p\). For every integer \(n\ge3\), let \(T_n\) be the number of nearest-neighbour steps required to visit every vertex of the cycle \(C_n=\{0,\ldots,n-1\}\), starting from \(0\), with clockwise-step probability \(p\). Let \(L_n\in\{1,\ldots,n-1\}\) be the last newly visited vertex and \(D_n=n-1-L_n\).

On the common, unwrapped walk defined below, put \(K=-\inf_{t\ge0}Z_t\), \(H_m=\inf\{t\ge0:Z_t=m\}\) for integers \(m\ge0\), \(J_n=\min\{K,n-2\}\), and \(b_n=\lfloor(n-1)/2\rfloor\). Then \(K\) is a geometric random variable with
\[
\Pr(K=k)=(1-r)r^k,\qquad k=0,1,2,\ldots,
\]
and the following **finite-size, joint, pathwise coupling** holds:
\[
\boxed{\Pr\bigl((T_n,D_n)\ne(H_{n-1-J_n},J_n)\bigr)\le 2r^{b_n+1}.}
\]
In particular, the total variation distance between the two joint laws is at most \(2r^{b_n+1}\) (and, of course, at most \(1\)). The auxiliary hitting time and minimum on the right are deliberately dependent at finite \(n\); independence is an asymptotic result, not a finite-size assertion.

As \(n\to\infty\),
\[
\boxed{\left(D_n,\frac{T_n-(n-1)/\mu}{\sqrt n}\right)\ \Longrightarrow\ (K,G),}
\]
where \(K\) has the above geometric law, \(G\sim N(0,4pq/\mu^3)\), and **\(K\) and \(G\) are independent**. Equivalently, for every fixed integer \(k\ge0\) and every real \(x\),
\[
\lim_{n\to\infty}\Pr\left(D_n=k,\ \frac{T_n-(n-1)/\mu}{\sqrt n}\le x\right)
=(1-r)r^k\,\Phi\left(\frac{x}{\sqrt{4pq/\mu^3}}\right).
\]
Thus final-vertex offset and Gaussian-scale completion-time fluctuations asymptotically decouple, while the complete joint law admits an exponentially accurate coupling to one underlying drifted walk.

## Assumptions and scope

Take independent \(\xi_1,\xi_2,\ldots\) with \(\Pr(\xi_i=1)=p\), \(\Pr(\xi_i=-1)=q\), and define \(Z_0=0\), \(Z_t=\sum_{i=1}^t\xi_i\). The cycle walk is \(Z_t\pmod n\); no state-dependent or time-dependent bias is allowed. Define \(M_t=\max_{0\le s\le t}Z_s\), \(m_t=\min_{0\le s\le t}Z_s\). A nearest-neighbour integer walk visits exactly every integer between its running minimum and maximum. Therefore every residue modulo \(n\) has been visited precisely when \(M_t-m_t\ge n-1\), and
\[
T_n=\inf\{t\ge0:M_t-m_t=n-1\}.
\]
The almost-sure positive drift implies \(Z_t\to+\infty\), so its ultimate minimum is finite, attained at some finite random time, and all nonnegative hitting times \(H_m\) are finite. The convention \(H_0=0\) is not needed in the asserted coupling because \(n-1-J_n\ge1\). No claim is made at \(p=1/2\), under drift varying with \(n\), or for non-nearest-neighbour walks.

## Proof

**1. Geometric ultimate minimum.** Standard gambler's ruin, or optional stopping applied to the bounded-exit martingale \(r^{Z_t}\), gives for every integer \(k\ge0\)
\[
\Pr\bigl(\inf_{t\ge0}Z_t\le-k\bigr)=r^k.
\]
Indeed, for barriers \(-k\) and \(a\), use the harmonic equation \(f(i)=pf(i+1)+qf(i-1)\), then let \(a\to\infty\). Hence \(\Pr(K=k)=r^k-r^{k+1}=(1-r)r^k\).

**2. A pathwise event on which coverage is a shifted hitting time.** Set \(b=b_n\) and let \(E_n\) be the event that (i) \(K\le b\) and (ii) the minimum achieved by time \(H_b\) equals the ultimate minimum:
\[
E_n=\{K\le b,\ m_{H_b}=-K\}.
\]
Since \(\Pr(K>b)=r^{b+1}\), only the possibility of a new minimum after \(H_b\) remains to be controlled. At \(H_b\), the walk is at \(b\), and its current minimum is \(m_{H_b}\le0\). Conditionally on its trajectory through \(H_b\), the strong Markov property and gambler's ruin give
\[
\Pr\{\inf_{t>H_b}Z_t<m_{H_b}\mid\mathcal F_{H_b}\}
=r^{b-m_{H_b}+1}\le r^{b+1}.
\]
Therefore, by the union bound,
\[
\Pr(E_n^c)\le2r^{b+1}.
\]
On \(E_n\), the ultimate minimum \(-K\) has already occurred by \(H_b\), and the integer \(h=n-1-K\) satisfies \(h\ge b\). Prior to \(H_h\), the running maximum is at most \(h-1\) and the running minimum is at least \(-K\), so the range is at most \(n-2\); coverage has not occurred. At \(H_h\), the running minimum equals \(-K\) and the maximum equals \(h\), so the range is exactly \(n-1\); coverage occurs at that instant. Thus
\[
T_n=H_{n-1-K},\qquad L_n=n-1-K,\qquad D_n=K\quad\text{on }E_n.
\]
Because \(K\le b\le n-2\) on this event, \(J_n=K\), establishing the joint coupling probability. The total-variation bound follows by the ordinary coupling inequality. Notice that the proof makes no assertion about paths outside \(E_n\).

**3. Centered passage-time fluctuations.** For \(j\ge1\), let \(\tau_j=H_j-H_{j-1}\). Spatial homogeneity and the strong Markov property make the \(\tau_j\) independent, identically distributed copies of \(\tau=H_1\). The positive drift makes \(\tau\) exponentially integrable in a neighborhood of zero: \(\{\tau>t\}\subseteq\{Z_t\le0\}\), whose probability decreases exponentially by a Chernoff bound. First-step analysis from \(0\) gives the distributional recursion
\[
\tau\overset d=\begin{cases}1,&\text{with probability }p,\\1+\tau'+\tau'',&\text{with probability }q,\end{cases}
\]
where the copies in the second branch are independent and have the law of \(\tau\). Taking first and second moments yields
\[
\mathbb E\tau=\frac1\mu,\qquad \operatorname{Var}(\tau)=\frac{4pq}{\mu^3}.
\]
The classical i.i.d. central limit theorem therefore shows
\[
\frac{H_{n-1}-(n-1)/\mu}{\sqrt n}\Longrightarrow N\left(0,\frac{4pq}{\mu^3}\right).
\]
The difference \(H_{n-1}-T_n\) is tight. To see this, fix an integer \(c\ge0\). For sufficiently large \(n\), on \(E_n\cap\{K\le c\}\),
\[
0\le H_{n-1}-T_n\le H_{n-1}-H_{n-1-c}.
\]
By the strong Markov property the upper bound has the fixed law of \(H_c\), independently of \(n\). The complement has probability at most \(r^{c+1}+2r^{b_n+1}\), and the first term can be made arbitrarily small by choosing \(c\) large. Consequently \(H_{n-1}-T_n=O_{\Pr}(1)\), and the Gaussian limit also holds with \(T_n\) replacing \(H_{n-1}\).

**4. Independence of the limit and the final location.** Write \(K^{(s)}=-\min_{0\le t\le s}Z_t\). Positive drift implies \(K^{(s)}\to K\) almost surely as \(s\to\infty\). Fix \(s\). The variable \(K^{(s)}\) is measurable with respect to \(\mathcal F_s\). For \(n-1>s\), the walk cannot have hit level \(n-1\) before time \(s\), and conditional on \(\mathcal F_s\), the strong Markov property gives
\[
H_{n-1}\overset d=s+H'_{n-1-Z_s},
\]
where the primed passage process uses fresh steps independent of \(\mathcal F_s\). Since \(|Z_s|\le s\), the independent-summand central limit theorem applies uniformly over the finitely many possible values of \(Z_s\). The conditional limit of the normalized passage time is therefore the same Gaussian law for every \(\mathcal F_s\) event. It follows that the Gaussian limit is asymptotically independent of \(K^{(s)}\). Letting \(s\to\infty\), and using \(\Pr(K^{(s)}\ne K)\to0\), proves asymptotic independence of the normalized \(H_{n-1}\) and \(K\).

Finally, Step 2 implies \(\Pr(D_n\ne K)\le2r^{b_n+1}\), while Step 3 gives \((T_n-H_{n-1})/\sqrt n\to0\) in probability. Slutsky's theorem for joint random variables yields the asserted independent Gaussian–geometric limit. The fixed-\(k\) formula follows because the geometric coordinate takes integer values and Gaussian cumulative distribution functions are continuous. This completes the proof.

## Verification

The standalone `verify.py` uses only the Python standard library. Execute `python verify.py` to check exactly, with rational arithmetic, the passage-time moment recursion and the gambler's-ruin harmonic identities for four rational biases. It also exhaustively checks finite nearest-neighbour paths through twelve steps on cycles of sizes three through eight, including the range/coverage equivalence and the finite-path counterpart of the hitting-time coupling on qualifying histories. Its deterministic checks are supplementary; the exponential probability bound, all infinite-horizon statements, and asymptotic independence are justified by Steps 1–4 above, not finite experiments.

## Relationship to prior work

Idnani and Salem (2026, arXiv:2610.15115) obtain an exact *marginal* last-coverage-vertex distribution for a homogeneous biased nearest-neighbour walk on a cycle and an expansion-sequence representation. That known one-dimensional geometric-looking marginal is not claimed as new here. The present claim concerns a *joint*, exponentially controlled coupling of **coverage time and terminal vertex** to a single infinite lifted path and the resulting asymptotic independence of its Gaussian and geometric components. The motivating paper examines coverage locations but does not derive this coupling or joint time-location limit in its main results, proofs, or open-problem section.

Buchanan, Horn and Rombach (2022/2023, arXiv:2209.08079) characterize directed graphs with uniform last-visited-vertex laws under their simple-random-walk convention. Their graph-classification result does not imply the present joint limit or biased-walk hitting-time coupling. Levin and Peres, *Markov Chains and Mixing Times*, treat the symmetric cycle's cover time; gambler's ruin, strong Markov arguments, and renewal passage-time central limit theorems are standard ingredients, not originality claims. The value of the present statement is their explicit joint, finite-size assembly for the drifted coverage model.

## Limitations

The bias \(p\) is fixed strictly above \(1/2\); the proof does not give uniform estimates as \(p\downarrow1/2\) or in the diffusive crossover regime. It also does not address time-varying bias, multiple walkers, higher-dimensional tori, or general holding-time distributions. The finite-size coupling compares the actual terminal pair with a *dependent*, walk-indexed auxiliary pair; it does not assert finite-size independence or a quantitative Gaussian approximation rate. The stated joint theorem has not been independently audited. Literature searches cannot rule out an unindexed earlier joint limit or a general result implying the exact coupling. The standard passage-time and ruin identities are not represented as new results.

## References

1. Kiyan Idnani and Jad Salem, *Last-Coverage Probabilities of Random Walks on Cycle Graphs for Symmetric, Biased, and Time-Dependent Walks*, arXiv:2610.15115, first submitted 2026-10-10. https://arxiv.org/abs/2610.15115
2. Calum Buchanan, Paul Horn and Puck Rombach, *On the Last New Vertex Visited by a Random Walk in a Directed Graph*, arXiv:2209.08079, first submitted 2022-09-16; published 2023. https://arxiv.org/abs/2209.08079
3. David A. Levin and Yuval Peres, *Markov Chains and Mixing Times*, 2nd ed., American Mathematical Society, 2017, Chapter 11, cycle cover times. https://pages.uoregon.edu/dlevin/MARKOV/markovmixing.pdf
4. David J. Aldous and James A. Fill, *Reversible Markov Chains and Random Walks on Graphs*, unfinished monograph, Chapter 6, cover times of cycles. https://www.stat.berkeley.edu/~aldous/RWG/book.pdf
