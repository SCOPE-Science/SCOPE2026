# Rate-universal square-root coexistence in two-type infection on \(K_{2,n}\)

## Finding

Let \(K_{2,n}\) have two core vertices and \(n\ge2\) peripheral vertices. Initially one peripheral vertex has permanent infection type 1 and a different peripheral vertex has permanent type 2. Each type-\(i\) infected vertex independently attempts to infect every susceptible neighbor at exponential rate \(\lambda_i>0\), with type retained forever after the first successful infection. Let \(N_{i,n}\) be the final type-\(i\) vertex count, \(L_n=\min(N_{1,n},N_{2,n})\), and \(S_n\) be the event that the two core vertices receive different types. Put \(q=\lambda_1/(\lambda_1+\lambda_2)\).

For all \(n\ge2\), define
\[
I_n(\alpha,\beta)
=\beta\int_0^\infty e^{-(\alpha+\beta)t}
 \bigl[e^{-\alpha t}(1+\alpha t)\bigr]^{n-2}\,dt
=\beta\sum_{k=0}^{n-2}
\frac{(n-2)!}{(n-2-k)!}
\frac{\alpha^k}{((n-1)\alpha+\beta)^{k+1}}.
\]
Then the exact probability of core-type coexistence and the exact probability of complete winner-takes-all-but-one are
\[
\Pr(S_n)=q I_n(\lambda_1,\lambda_2)
 +(1-q)I_n(\lambda_2,\lambda_1),
\qquad
\Pr(L_n=1)=1-\Pr(S_n).
\]
The first probability is strictly decreasing in \(n\) at every fixed positive rate pair. As \(n\to\infty\),
\[
\boxed{\Pr(S_n)=\sqrt{\frac{\pi}{2n}}
-\frac{\lambda_1/\lambda_2+\lambda_2/\lambda_1-2/3}{n}
+O_{\lambda_1,\lambda_2}(n^{-3/2}).}
\]
In particular, **the leading square-root coefficient is independent of both infection rates**, although its second-order correction is not.

Conditionally on \(S_n\), both types occupy macroscopic proportions:
\[
\frac{N_{1,n}}{n}\xrightarrow{\Pr(\cdot\mid S_n)}q,
\qquad
\frac{L_n}{n}\xrightarrow{\Pr(\cdot\mid S_n)}m,
\qquad m=\min(q,1-q)>0.
\]
Consequently, for every fixed real \(r\ge1\),
\[
\boxed{\mathbb E[L_n^r]
\sim\sqrt{\frac{\pi}{2}}\,m^r n^{r-1/2}.}
\]
In particular \(L_n\to1\) in probability but \(\mathbb E L_n\sim m\sqrt{\pi n/2}\) diverges, and
\(\operatorname{Var}(L_n)\sim m^2\sqrt{\pi/2}\,n^{3/2}\).
The first core infection has type 1 with probability \(q\); surprisingly, conditional on the rare event \(S_n\), this probability instead tends to \(1-q\).

## Assumptions and scope

The graph is the simple, undirected, deterministic complete bipartite graph \(K_{2,n}\). The two seeds are distinct peripheral vertices, one of each permanent type. All remaining vertices are susceptible. Clocks across directed infected-to-susceptible incidences, vertices, and infection types are independent; when a vertex of type \(i\) acquires a susceptible neighbor, it transmits to that neighbor after a fresh \(\operatorname{Exp}(\lambda_i)\) waiting time. An already infected vertex never changes type. Only two competing types are present. The rates \(\lambda_1,\lambda_2\) are fixed strictly positive constants as \(n\) grows. There is no recovery and no time horizon cutoff.

Both core vertices and all peripheral vertices are eventually infected almost surely, because the graph is finite, connected, and all rates are positive. In this result, "coexistence" means both colors occupy core vertices; equivalently both colors have final population larger than one. The event is *not* asserted to persist with nonzero probability in the large-graph limit.

## Proof

**1. First hub and two-stage competing race.** The first infection of a core vertex is produced by one of four independent exponential clocks from the two peripheral seeds. It is type 1 with probability \(q\). Conditional on the first hub being type \(i\), write \(\alpha=\lambda_i\) and \(\beta=\lambda_j\) for the other type. By exponential memorylessness, all unused clocks may be restarted at this instant. The type-\(j\) seed's transmission to the remaining hub is an independent \(\operatorname{Exp}(\beta)\) variable \(T\), while the type-\(i\) seed's transmission is independent \(\operatorname{Exp}(\alpha)\). Each of the \(n-2\) initially susceptible peripheral vertices can transmit type \(i\) to the second hub only after first receiving it from the first hub, so its two-step delay is an independent sum of two \(\operatorname{Exp}(\alpha)\) variables. Such a sum exceeds \(t\) with probability \(e^{-\alpha t}(1+\alpha t)\).

The second hub acquires type \(j\) precisely when \(T\) beats the type-\(i\) seed clock and all of these two-step delays. Integrating its density gives \(I_n(\alpha,\beta)\). Expanding \((1+\alpha t)^{n-2}\) and integrating the exponential monomials gives the finite sum. Averaging over the type of the first hub establishes the exact coexistence formula. When both hubs acquire the same type, every initially susceptible peripheral vertex eventually acquires that type, so the other type retains only its original seed. If the hubs split, both types have a seed and a hub. This proves \(\{L_n=1\}=S_n^c\). The factor \(e^{-\alpha t}(1+\alpha t)\) lies strictly between zero and one for \(t>0\), so both integrals, hence the coexistence probability, decrease strictly with \(n\).

**2. Laplace asymptotics.** In \(I_n(\alpha,\beta)\) substitute \(t=s/(\alpha\sqrt n)\) and expand the logarithm. For bounded \(s\), its exponential has the expansion
\[
 e^{-s^2/2}\left[1+n^{-1/2}\left(\frac{s^3}{3}
-(1+\beta/\alpha)s\right)
+O_{\alpha,\beta}(n^{-1}(s^2+s^4+s^6))\right].
\]
The remainder is integrable uniformly after splitting the integral at \(s=n^{1/12}\): Taylor's theorem controls the first interval, and \(\log(1+u)-u\le-c u^2\) for bounded positive \(u\), combined with direct exponential decay for large \(u\), controls the second. Since
\(\int_0^\infty e^{-s^2/2}\,ds=\sqrt{\pi/2}\),
\(\int_0^\infty s e^{-s^2/2}\,ds=1\), and
\(\int_0^\infty s^3e^{-s^2/2}\,ds=2\), we obtain
\[
I_n(\alpha,\beta)
=\frac{\beta}{\alpha}\sqrt{\frac{\pi}{2n}}
-\frac{\beta}{\alpha}\left(\frac13+\frac{\beta}{\alpha}\right)\frac1n
+O_{\alpha,\beta}(n^{-3/2}).
\]
Weighting this expansion by \(q\) and \(1-q\) cancels the rate ratios in the leading term. The next coefficient simplifies to \(\lambda_1/\lambda_2+\lambda_2/\lambda_1-2/3\), proving the stated asymptotic formula. The same calculation gives
\(\Pr(\text{first hub type 1}\mid S_n)\to1-q\).

**3. Conditional macroscopic coexistence.** Conditional on the first hub's type \(i\), on \(S_n\), and on the elapsed time \(T=t\) until the second hub becomes type \(j\), the conditional density of \(T\) is proportional to the integrand defining \(I_n(\alpha,\beta)\). The substitution in Step 2 shows that \(\alpha\sqrt n\,T\) converges conditionally to the positive half-normal distribution with density \(\sqrt{2/\pi}e^{-s^2/2}\) for \(s>0\). For each originally susceptible peripheral vertex, conditional on not transmitting type \(i\) via the two-step path before \(T=t\), the probability it was already infected is exactly \(\alpha t/(1+\alpha t)\). Thus the number \(K\) infected before the second hub has the conditional law
\[
K\mid(T=t,S_n,\text{first type }i)
\sim\operatorname{Bin}\left(n-2,\frac{\alpha t}{1+\alpha t}\right).
\]
Therefore \(K/n\to0\) conditionally in probability. After the second hub is infected, each of the remaining \(n-2-K\) peripheral vertices independently sees fresh competing exponential clocks of rates \(\lambda_1\) and \(\lambda_2\); its probability of receiving type 1 is \(q\). Conditional binomial concentration yields \(N_{1,n}/n\to q\) and \(L_n/n\to m\) in probability given \(S_n\), regardless of which type occupied the first hub.

On \(S_n^c\), \(L_n=1\). On \(S_n\), the random variable \(L_n/n\) is bounded and converges in conditional probability to \(m\), so its conditional moments of every fixed positive order converge to \(m^r\). Multiplication by \(\Pr(S_n)\sim\sqrt{\pi/(2n)}\) proves the moment asymptotics. Finally \((\mathbb E L_n)^2=O(n)\) is lower order than \(\mathbb E L_n^2\asymp n^{3/2}\), giving the variance formula.

## Verification

The companion `checker.py` is a standalone Python 3 standard-library program. Run `python3 checker.py` from the directory containing this document. It evaluates the integral formula as a finite rational sum, constructs the full terminal distribution by an independent acyclic continuous-time Markov-chain recurrence on all four infection counts/core types, and compares it to a second exact description conditioned on the first hub type. All finite-case comparisons use `fractions.Fraction`. It also checks finite examples, rate-swapping symmetry, strict size monotonicity, and numerical convergence toward the analytically derived two-term expansion. Its expected final status is `PASS: 687 exact-rational assertions and asymptotic diagnostics`.

These finite computations verify sample cases and independent characterizations; they do not prove the asymptotic theorem. The all-order proof is the exponential race, integral identity, and dominated Laplace analysis above.

## Relationship to prior work

Deijfen, van der Hofstad, and Sfragara (2022 preprint; 2024 journal publication) establish a winner-takes-all-but-one law for **random configuration-model graphs with infinite-mean power-law degrees**, not for the deterministic fixed-two-hub graph \(K_{2,n}\). Their limit theorem neither provides a finite-\(n\) core-split formula nor the \(n^{-1/2}\) rare-event coefficient, its rate cancellation, its second-order correction, or divergent minority moments. Ahlberg, Deijfen, and Janson (2017 preprint) study competing growth under a finite-variance-degree configuration-model hypothesis; its square-integrability assumptions do not describe the two degree-\(n\) hubs of \(K_{2,n}\). Deijfen and van der Hofstad (2013 preprint, 2016 journal) analyze an earlier heavy-tailed configuration model and show a different all-but-finite form of competitive exclusion. The model of exponential competing growth and the general winner-takes-all phenomenon are established prior literature, not claims of invention here.

## Limitations

The exact formulas require two peripheral seeds of different types, a fixed two-vertex core, independent exponential edge-contact clocks, irreversible infections, and fixed positive transmission rates. Varying rates with graph size, recovery, random graph topology, multiple cores, and initial core seeds are not covered. The constant independent of rates is only the *leading* asymptotic coefficient, not the exact finite-size coexistence probability. The conditional half-normal statement is about the time between first and second core infections on the rare core-split event. Neither historical priority nor independent mathematical certification is established by the accompanying reproducible checks.

## References

1. M. Deijfen, R. van der Hofstad, and M. Sfragara, *The winner takes it all but one*, arXiv:2204.04125, first submitted 8 April 2022, https://arxiv.org/abs/2204.04125 ; *Journal of Applied Probability* 61 (2024), 137–152, DOI:10.1017/jpr.2023.23.
2. D. Ahlberg, M. Deijfen, and S. Janson, *Competing first passage percolation on random graphs with finite variance degrees*, arXiv:1711.02902, first submitted 8 November 2017, https://arxiv.org/abs/1711.02902 ; *Random Structures & Algorithms* 55 (2019), 545–559.
3. M. Deijfen and R. van der Hofstad, *The winner takes it all*, arXiv:1306.6467, first submitted 27 June 2013, https://arxiv.org/abs/1306.6467 ; *Annals of Applied Probability* 26 (2016), 2419–2453.
