# Exact error constants and weak-signal crossover for asynchronous learning on stars

## Finding

Let \(S_m=K_{1,m}\) be a star with \(m\ge1\) leaves. Fix a signal-accuracy parameter \(p\in[1/2,1]\) and positive hub/leaf activation-rate ratio \(\rho\). Under the asynchronous, initially-unannounced, private-signal majority process specified below, the population almost surely reaches unanimous agreement, and the error probability of that consensus is exactly

\[
E_{m,\rho}(p)=\sum_{k=0}^{m}\rho\binom{m}{k}
 B(m-k+\rho,k+1)\,e_k(p),
\qquad e_k(p)=\Pr\{\operatorname{Bin}(k,p)<k/2\}
 +(1-p)\Pr\{\operatorname{Bin}(k,p)=k/2\}.
\]

Here \(B\) is the beta function, \(\operatorname{Bin}(0,p)=0\), and all terms are ordinary finite probabilities. In the homogeneous-rate case \(\rho=1\), the beta-binomial weights are \(1/(m+1)\). With \(b_j(p)=\Pr\{\operatorname{Bin}(2j+1,p)\le j\}\), they give the more explicit identity

\[
E_{m,1}(p)=\frac{2\sum_{j=0}^{\lfloor(m-1)/2\rfloor}b_j(p)
 +\mathbf1_{\{m\text{ even}\}}b_{m/2}(p)}{m+1}.
\]

For every fixed \(\rho>0\) and \(1/2<p<1\), the error has the sharp asymptotic

\[
\boxed{\displaystyle \lim_{m\to\infty}mE_{m,\rho}(p)=
 \frac{2\rho p(1-p)}{(2p-1)^2}.}
\]

The singularity as \(p\downarrow1/2\) corresponds to a genuine finite-population weak-signal crossover. For every fixed \(\rho>0\) and \(\alpha\ge0\), set \(p_m=1/2+\alpha/\sqrt m\), for sufficiently large \(m\). Then

\[
\boxed{\displaystyle E_{m,\rho}(p_m)\longrightarrow
 F_\rho(\alpha):=\rho\int_0^1(1-u)^{\rho-1}
 \Phi(-2\alpha\sqrt u)\,du.}
\]

For equal rates and \(\alpha>0\), writing \(z=2\alpha\),

\[
F_1(\alpha)=\Phi(-z)+\frac{\Phi(z)-1/2}{z^2}
 -\frac{\phi(z)}{z},\qquad F_1(0)=1/2.
\]

For any fixed \(\rho>0\), \(F_\rho(\alpha)\sim\rho/(8\alpha^2)\) as \(\alpha\to\infty\). For \(m\ge2\) and \(1/2<p<1\), \(E_{m,\rho}(p)\) is strictly increasing in \(\rho\): faster relative activation of the hub worsens the probability of a correct consensus. For \(m=1\), it equals \(1-p\) for every rate ratio.

## Assumptions and scope

Each vertex has an independent private bit that equals the correct answer with probability \(p\). Initially every public announcement is \(\perp\). An independent rate-\(\lambda>0\) Poisson clock activates the hub, and independent rate-\(\mu>0\) clocks activate each leaf. An activated vertex publishes the strict majority among the currently announced non-\(\perp\) neighbors, or its *own fixed private bit* when there is a tie, including zero announced neighbors. Activations continue indefinitely and \(\rho=\lambda/\mu\). An error means **unanimous convergence to the incorrect bit**, not a transient mistaken announcement or a finite-horizon count. No self-neighbor loops, initial public opinions, Bayesian inference, heterogeneous leaf signal accuracies, or simultaneous activations are assumed. The rate-one, uniform-at-each-tick process is \(\rho=1\), up to an irrelevant rescaling of time.

## Proof

**1. Irreversibility of the hub's first declaration.** Let \(T\) be the first activation time of the hub. Before \(T\), a leaf that activates announces its private bit: its only neighbor is still silent. At \(T\), the hub selects the majority of these revealed private bits, breaking any tie toward its own signal. Once the hub announces its selected bit, every subsequent leaf activation replaces that leaf's announcement by the hub's bit. The net count advantage of the hub's selected bit among its neighbors therefore cannot decrease, and a possible tie is still resolved in its favor. Hence all subsequent hub announcements retain the same bit and every leaf eventually copies it. This proves almost-sure unanimous convergence and identifies its outcome with the first hub declaration. This locking observation was established for homogeneous clocks in Feldman et al. (2014); it is repeated to fix exactly what is being quantified.

**2. The complete distribution of the informative sample.** Let \(K\) denote the number of *distinct* leaves that activate at least once before \(T\). The first-activation times of leaves are independent rate-\(\mu\) exponentials and \(T\) is an independent rate-\(\lambda\) exponential. Given \(T=t\), each leaf is observed with probability \(1-e^{-\mu t}\), independently. Integration gives

\[
\Pr(K=k)=\lambda\binom mk\int_0^\infty e^{-\lambda t}
 (1-e^{-\mu t})^k e^{-\mu t(m-k)}\,dt
 =\rho\binom mkB(m-k+\rho,k+1).
\]

The randomly revealed private signals and the hub's signal are independent of \(K\). If \(k\) leaves were revealed, the hub errs if strictly more than half are incorrect or if there is a tie and its prior signal is incorrect. This is exactly \(e_k(p)\) and proves the finite formula. At \(\rho=1\), cancellation of factorials makes \(K\) uniform on \(\{0,\dots,m\}\). For every \(j\ge0\), adding the hub tie-breaking bit to an even sample and using binomial symmetry shows \(e_{2j}(p)=e_{2j+1}(p)=b_j(p)\), proving the parity formula (with the final even term treated separately).

**3. Exact fixed-bias leading constant.** For fixed \(k\ge0\) and \(\rho>0\), the displayed beta-binomial probability obeys \(m\Pr(K=k)\to\rho\). Furthermore, for all sufficiently large \(m\), \(\Pr(K=k)\le C_\rho/m\) on \(k\le m/2\). One way to verify this is to use the exact adjacent-weight ratio

\[
\frac{\Pr(K=k+1)}{\Pr(K=k)}=
 \frac{m-k}{m-k-1+\rho},\qquad
 \Pr(K=0)=\frac\rho{m+\rho},
\]

whose product is bounded by a constant depending only on \(\rho\) for \(k\le m/2\). For \(p>1/2\), Hoeffding's bound gives \(e_k(p)\le\exp(-c_p k)\) for \(k\ge1\), for some \(c_p>0\) (the tie case is bounded by the same left-tail event). Contributions from \(k>m/2\), even multiplied by \(m\), vanish exponentially. Dominated truncation therefore yields

\[
\lim_{m\to\infty}mE_{m,\rho}(p)=\rho\sum_{k=0}^\infty e_k(p)
 =2\rho\sum_{j=0}^\infty b_j(p).
\]

For an independent random walk with \(+1\) probability \(p>q=1-p\) and \(-1\) probability \(q\), the sum \(\sum_{j\ge0}b_j(p)\) is the expected total number of visits to negative odd positions, since its \((2j+1)\)-step position is negative exactly when the binomial success count is at most \(j\). The expected total number of visits to any fixed integer \(-r\), \(r\ge1\), is \((q/p)^r/(p-q)\): the hitting probability is \((q/p)^r\), and the expected visits after a hit are \(1/(p-q)\). Summing over \(r=1,3,5,\ldots\) gives

\[
\sum_{j=0}^\infty b_j(p)=\frac1{p-q}
 \sum_{a=0}^\infty\left(\frac qp\right)^{2a+1}
 =\frac{pq}{(p-q)^2},
\]

which proves the leading constant.

**4. Weak-signal limit and crossover.** Write \(U_m=K/m\). Coupling all leaves through the same \(T\) shows, conditional on \(T\), that \(U_m\to U=1-e^{-\mu T}\) almost surely. The distribution of \(U\) is \(\Pr(U\le u)=1-(1-u)^\rho\), so it has beta density \(\rho(1-u)^{\rho-1}\) on \((0,1)\). At any sequence \(k_m/m\to u>0\), the binomial central-limit theorem (with the hub's single tie-breaking vote, whose effect vanishes) gives

\[
e_{k_m}(1/2+\alpha/\sqrt m)\to \Phi(-2\alpha\sqrt u).
\]

The probability of \(U=0\) is zero, and the errors are bounded in \([0,1]\). Conditioning and bounded convergence prove the claimed integral. For \(\rho=1\), substituting \(u=t^2\) and integrating by parts yields the stated expression in \(\Phi\) and \(\phi\). To obtain its large-\(\alpha\) analogue for every \(\rho>0\), use \(v=4\alpha^2u\) and dominated convergence on a growing initial interval, noting that \(\int_0^\infty\Phi(-\sqrt v)\,dv=1/2\); the exponentially small Gaussian tail controls the remainder near \(u=1\), including integrable \((1-u)^{\rho-1}\) singularities. This gives \(F_\rho(\alpha)\sim\rho/(8\alpha^2)\).

**5. Rate monotonicity.** A larger hub activation rate (with the leaf clocks coupled unchanged) makes its first announcement earlier and therefore stochastically reduces \(K\). For \(p>1/2\), the sequence \(e_k(p)\) is nonincreasing, and \(e_{2j+1}(p)>e_{2j+2}(p)\), because

\[
b_j(p)-b_{j+1}(p)=(2p-1)\binom{2j+1}{j}
 [p(1-p)]^{j+1}>0.
\]

When \(m\ge2\), the coupling changes the probability of \(K\ge2\) strictly, so the total expected error increases strictly with \(\rho\). When \(m=1\), both \(e_0(p)\) and \(e_1(p)\) equal \(1-p\), giving the exceptional equality.

## Verification

The accompanying `verify_star.py` uses exact rational arithmetic to compare the closed-form beta-binomial sum with an independently constructed first-activation Markov recurrence for \(m=1,\ldots,16\), five rational signal accuracies and six rational clock ratios; it also checks the equal-rate binomial-tail reduction. An independent full enumeration of private-signal patterns and first-activation orders checks \(m=1,\ldots,6\). Standard-library floating evaluations test the fixed-bias constant and weak-signal limiting function at specified finite sizes. These finite calculations do not prove the asymptotic statements; the preceding random-walk and central-limit arguments do. Run with `python3 verify_star.py` using the Python standard library.

## Relationship to prior work

Feldman, Immorlica, Lucier and Weinberg (2014, Section 3, Claim 1 and the star example) already prove the first-hub-announcement locking mechanism and eventual correct consensus with high probability, obtaining a logarithmic-over-linear error upper bound via a Chernoff argument. These facts are *not* claimed as new. Bahrani et al. (2019) study the same asynchronous private-signal mechanism on preferential-attachment and balanced trees. Mohan and Pralat (first released September 9, 2023) investigate its qualitative behavior on binomial random graphs and mention the star benchmark. The present statement instead specifies the **exact finite erroneous-consensus probability with arbitrary positive hub/leaf clock-rate ratio, its sharp fixed-bias constant, and its critical weak-signal limiting profile**. No cited result supplies these latter formulas, nor do its qualitative conclusions determine their constants. Mueller-Frank and Neri (2021) treat distinct quasi-Bayesian and axiomatic updating rules, not this first-announcement private-tie majority process.

## Limitations

Only stars with homogeneous independent leaf signal accuracy and leaf rate, one hub rate, binary signals, and initially silent public reports are covered. The weak-signal limit holds for fixed \(\rho\) and fixed \(\alpha\), not arbitrary rate or signal sequences; the fixed-bias constant requires \(p>1/2\). Some finite-size expressions can be obtained from classical binomial random-walk identities; the novelty claim is confined to the combined sharp probabilistic characterization of this social-learning process, not to those classical identities. External publication priority is subject to unindexed or differently described specialist literature. Independent review has not been performed.

## References

1. M. Feldman, N. Immorlica, B. Lucier and S. M. Weinberg, *Reaching Consensus via non-Bayesian Asynchronous Learning in Social Networks*, 2014, arXiv:1408.5192, https://arxiv.org/abs/1408.5192 (especially Section 3, star example).
2. M. Bahrani, N. Immorlica, D. Mohan and S. M. Weinberg, *Asynchronous Majority Dynamics in Preferential Attachment Trees*, first public July 12, 2019, arXiv:1907.05823, https://arxiv.org/abs/1907.05823.
3. D. Mohan and P. Prałat, *Asynchronous Majority Dynamics on Binomial Random Graphs*, first public September 9, 2023, arXiv:2309.04691, https://arxiv.org/abs/2309.04691.
4. M. Mueller-Frank and C. Neri, *A general analysis of boundedly rational learning in social networks*, Theoretical Economics 16 (2021), 317–357, https://doi.org/10.3982/TE2974.
