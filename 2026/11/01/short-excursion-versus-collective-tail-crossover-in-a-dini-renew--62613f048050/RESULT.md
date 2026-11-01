# Short-excursion versus collective-tail crossover in a Dini renewal pressure

## Finding
Fix \(c>0\) and \(p>1\). On the one-sided binary full shift let the potential at a sequence whose first \(1\) occurs after exactly \(k\) initial zeros be \(\phi(x)=-c(k+1)^{-p}\); set \(\phi(0^\infty)=0\). Denote the topological pressure of \(\beta\phi\) by \(P_\beta\), where \(\beta>0\). Put
\[
 S=c\zeta(p),\qquad b_\beta=e^{-\beta S},\qquad A_1=c(1+2^{-p}),\qquad T_p=c(p-1)\zeta(p).
\]
There is a unique \(p_*\in(1,2)\), determined by
\[
 (p_*-1)\zeta(p_*)=1+2^{-p_*},\qquad p_*\approx1.553201524280.
\]
Then the **sharp second correction** to the low-temperature pressure is
\[
\boxed{\frac{P_\beta}{b_\beta}-1-e^{-\beta c}\sim
 \begin{cases}
 \displaystyle\frac{c\Gamma(2-p)}{p-1}\,\beta e^{-\beta T_p},&1<p\le p_*,\\[5pt]
 e^{-\beta A_1},&p>p_*.
 \end{cases}}
\qquad(\beta\to\infty).
\]
Here \(f_\beta\sim g_\beta\) means \(f_\beta/g_\beta\to1\), and every coefficient displayed is positive. At the critical exponent the two competing activation exponents coincide, but the collective-tail term wins by a factor proportional to \(\beta\).

The leading relation \(P_\beta\sim e^{-\beta S}\), and the first relative correction \(e^{-\beta c}\), hold throughout \(p>1\). The new structural feature is the crossover: a *polynomially decaying, infinitely long memory* produces a collective second correction for \(p\le p_*\), whereas for \(p>p_*\) a single two-step excursion supplies it.

## Assumptions and scope
The shift \(\sigma\) acts on \(\Sigma=\{0,1\}^{\mathbb N_0}\) with its usual geometric metric. Define \(k(x)=\min\{j\ge0:x_j=1\}\) for \(x\ne0^\infty\). For a fixed \(c>0\) and \(p>1\), set \(\phi(x)=-c(k(x)+1)^{-p}\) and \(\phi(0^\infty)=0\). Its \(n\)-variation is at most \(c(n+1)^{-p}\), hence its variations are summable and its geometric-metric modulus is Dini. The only maximizing invariant probability for \(\phi\) is the fixed-point measure at \(0^\infty\).

Pressure is defined by the variational principle
\[
P_\beta=\sup_{\mu\in\mathcal M_\sigma}\bigl(h_\mu(\sigma)+\beta\int\phi\,d\mu\bigr).
\]
The statement includes all real \(\beta\to+\infty\), each fixed \(c>0\), and each fixed \(p>1\); it does not assert uniformity as \(p\) or \(c\) varies with \(\beta\).

## Proof
**1. Exact induced pressure.** Put \(a_j=c(j+1)^{-p}\), \(A_k=\sum_{j=0}^k a_j\), and \(S=\sum_{j\ge0}a_j\). A successive marker pair \(1,0^k,1\) has return length \(L=k+1\) and accumulated potential \(-A_k\): when moving toward the next marker the individual costs appear in reverse order. The induced map on the cylinder \([1]\) is the full shift over return-length symbols. For an invariant measure with positive marker frequency, Kac's formula, the induced entropy formula, and Shannon's entropy bound show that the variational pressure is at most the supremum of
\[
\frac{H(\pi)-\beta\sum_{k\ge0}\pi_k A_k}{\sum_{k\ge0}\pi_k(k+1)}
\]
over gap distributions with finite mean. Equality is attained by an independent gap process. For each \(\beta\), the unique positive \(P\) satisfying
\[
\boxed{\sum_{k=0}^\infty e^{-\beta A_k-P(k+1)}=1}\tag{1}
\]
exists because the left side decreases from infinity to zero: \(A_k\to S<\infty\). Relative entropy with respect to \(\pi_k=e^{-\beta A_k-P(k+1)}\) gives \(H(\pi')-\beta\mathbb E_{\pi'}A\le P\mathbb E_{\pi'}L\) for any competitor. The zero-marker measure has pressure zero, whereas the root is positive. Hence \(P=P_\beta\), and the stationary renewal measure with gaps \(\pi\) is the unique equilibrium state.

**2. Uniform first scale.** Write \(b=e^{-\beta S}\) and
\[
R_\beta(P)=\sum_{k\ge0}(e^{-\beta A_k}-b)e^{-P(k+1)}\ge0.
\]
Equation (1) is exactly
\[
1=\frac{b}{e^P-1}+R_\beta(P).\tag{2}
\]
For any \(q>1/(p-1)\) let \(K=\lceil\beta^q\rceil\). The contribution to \(R_\beta(P)\) from \(k<K\) is at most \(K e^{-\beta c}=o(1)\), uniformly in \(P\ge0\). The tail satisfies \(0\le S-A_k\le c(k+1)^{1-p}/(p-1)\) and therefore \(e^{-\beta A_k}/b=1+o(1)\) uniformly for \(k\ge K\). Comparing (1) at \(P=b/2\) and \(P=2b\) shows that its root lies between those values for all large \(\beta\); equation (2) then gives \(R_\beta(P_\beta)=o(1)\) and
\[
P_\beta/b\longrightarrow1.\tag{3}
\]

**3. Tail versus local excursions.** The \(k=0\) contribution to \(R_\beta(P_\beta)\) is \(e^{-\beta c}-b+o(e^{-\beta c})\), and the \(k=1\) contribution is \(e^{-\beta A_1}(1+o(1))\). More precisely, replacing their factors \(e^{-P(k+1)}\) by one incurs \(O(b e^{-\beta c})\). The sum over \(2\le k<K\) is \(O(K e^{-\beta A_2})\), where \(A_2>A_1\).

For the tail \(k\ge K\), put \(\delta_k=S-A_k\). The integral comparison gives
\[
\delta_k\sim\frac{c}{p-1}k^{1-p},
\qquad\beta\delta_K\longrightarrow0.
\]
Uniformly on the tail,
\[
e^{-\beta A_k}-b=b(e^{\beta\delta_k}-1)=b\beta\delta_k(1+o(1)).\tag{4}
\]
When \(1<p<2\), the Riemann-sum/Mellin estimate (using \(PK\to0\)) is
\[
\sum_{k\ge K}k^{1-p}e^{-P(k+1)}\sim\Gamma(2-p)P^{p-2}.
\]
Combining (3) and (4) gives the **sharp collective-tail term**
\[
\sum_{k\ge K}(e^{-\beta A_k}-b)e^{-P_\beta(k+1)}
\sim \frac{c\Gamma(2-p)}{p-1}\,\beta b^{p-1}.\tag{5}
\]
For \(p=2\), this tail is \(O(\beta b\log(1/P_\beta))=O(\beta^2b)\); for \(p>2\), it is \(O(\beta b)\). Both are negligible compared with \(e^{-\beta A_1}\), since \(S>A_1\).

For \(1<p<2\), the competitor exponents are \(T_p=(p-1)S\) from (5), and \(A_1\) from the single \(k=1\) term. Their smaller value determines the second correction. The \(k\ge2\) short terms are exponentially smaller than \(e^{-\beta A_1}\), and the \(k=0\) remainder \(O(b+b e^{-\beta c})\) is negligible compared with either second scale, because \(S>A_1\) and \(S>T_p\) for \(p<2\).

Finally, (2) gives the exact identity
\[
\frac{P_\beta}{b}=\frac{\log(1+b/(1-R_\beta(P_\beta)))}{b}
=1+R_\beta(P_\beta)+O\bigl(R_\beta(P_\beta)^2+b\bigr).
\]
Here \(R_\beta(P_\beta)\sim e^{-\beta c}\) and \(R_\beta^2=O(e^{-2\beta c})\), negligible against the second scale because \(\min\{T_p,A_1\}<2c\) for \(p<2\), while \(A_1<2c\) for \(p\ge2\). This proves the stated pressure asymptotic.

**4. Uniqueness of the crossover.** Write \(G(p)=(p-1)\zeta(p)\). For \(X_p\) gamma-distributed with shape \(p-1\) and rate one, the classical zeta integral gives
\[
G(p)=\mathbb E\left[\frac{X_p}{1-e^{-X_p}}\right].
\]
The integrand is strictly increasing on positive arguments, and gamma laws strictly increase in stochastic order as their shape increases (by adding an independent gamma variable). Thus \(G(p)\) is strictly increasing for \(p>1\). Meanwhile \(1+2^{-p}\) strictly decreases, \(G(p)\to1<3/2\) as \(p\downarrow1\), and \(G(2)=\zeta(2)>5/4\). Exactly one equality occurs in \((1,2)\), defining \(p_*\). At equality, the collective-tail contribution has an additional factor \(\beta\) and hence dominates the local term. This completes the proof.

## Verification
Run `python3 verification/check_pressure.py` from the package root. It uses only the Python standard library. The executed program approximates the crossover exponent by Euler–Maclaurin zeta evaluation, brackets finite-temperature pressure through explicit upper and lower bounds on the uncomputed branch tail, and checks finite Gibbs entropy identities. It completed 37 finite assertions. Its floating-point enclosures are numerical diagnostics rather than formal interval certification. The infinite asymptotics and uniqueness are established by the preceding analytic argument, not by finite tests.

## Relationship to prior work
Jiang–Li–Sun (2026, arXiv:2610.31327v1) establishes general regularity and low-temperature facts for Dini potentials but does not derive a power-tail renewal pressure's sharp second activation scale. Leplaideur–Mengue (2024, arXiv:2404.02182v1) treats exponential pressure rates for Lipschitz potentials with finite-type Aubry sets; that theory does not identify the present \(p\)-dependent tail-versus-local crossover. Cioletti–Lopes (2014, arXiv:1408.5342v1) develops renewal methods for Hofbauer-type potentials and positive-temperature transitions, not this low-temperature second-correction classification. Walters-type zero-temperature selection models have related background (Baraviera–Lopes–Mengue, 2011, arXiv:1106.5379v1).

An earlier geometric-tail renewal-pressure calculation treats a different sequence \(a_k\propto\theta^k\): it has a short-excursion correction hierarchy, and its rare-marker Poisson limit is not claimed as new here. The genuinely different result is that for the non-geometric Dini sequence \(a_k\propto(k+1)^{-p}\), the combined contribution of exponentially many long excursions overtakes the next short excursion below a uniquely determined exponent.

## Limitations
The proof applies to this explicit two-symbol renewal potential with fixed \(c>0\), fixed \(p>1\), and inverse temperature tending to infinity. No result is claimed for arbitrary Dini potentials, varying \(p\) in a critical scaling window, or a general thermodynamic system. The coefficient at the crossover comes from the exact power tail; a different regularly varying sequence may have a different correction. The priority assessment does not eliminate the possibility of uncatalogued renewal-pressure asymptotics or stronger general theorems. Independent external validation has not been performed.

## References
- Y. Jiang, Z. Li, Y. Sun, *Typical periodic optimization and freezing phase transition: Dini potentials and beyond*, arXiv:2610.31327v1, first submitted 2026-10-22. https://arxiv.org/abs/2610.31327
- R. Leplaideur and J. K. Mengue, *On the selection of subaction and measure for perturbed potentials*, arXiv:2404.02182v1, 2024. https://arxiv.org/abs/2404.02182
- L. M. Cioletti and A. O. Lopes, *Phase Transitions in One-dimensional Translation Invariant Systems: a Ruelle Operator Approach*, arXiv:1408.5342v1, 2014. https://arxiv.org/abs/1408.5342
- A. T. Baraviera, A. O. Lopes, J. K. Mengue, *On the selection of subaction and measure for a subclass of potentials defined by P. Walters*, arXiv:1106.5379v1, 2011. https://arxiv.org/abs/1106.5379
