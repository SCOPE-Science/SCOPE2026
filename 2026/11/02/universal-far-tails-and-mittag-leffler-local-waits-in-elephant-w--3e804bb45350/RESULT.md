# Universal far tails and Mittag-Leffler local waits in elephant walks with stops

## Finding

Consider a full-memory elephant random walk with stops. Write \(X_t\in\{-1,0,1\}\) for its increments, assume \(|X_1|=1\), and put \(\alpha=p+q=1-r\in(0,1)\), with the transition rule specified below. Define the number of actual moves and the *forward waiting time* observed at a deterministic integer time \(n\ge1\) by
\[
K_n=\sum_{t=1}^n X_t^2,\qquad
W_n=\min\{j\ge1:X_{n+j}\ne0\}.
\]

**Theorem (finite-time tail and local-wait law).** For every such walk, independently of the relative probabilities of forward and reverse copying, the following statements hold.

1. For every integer \(n\ge1\), integer \(m\ge0\), and realized \(K_n=k\),
   \[
   \Pr(W_n>m\mid\mathcal F_n)
    =\prod_{j=0}^{m-1}\left(1-\frac{\alpha k}{n+j}\right)
    =\frac{\Gamma(n)\Gamma(n+m-\alpha k)}
            {\Gamma(n-\alpha k)\Gamma(n+m)}.
   \]
   The empty product is one. In particular, \(W_n\) is finite almost surely.

2. For every *fixed* integer \(n\ge1\), as integer \(m\to\infty\),
   \[
   \Pr(W_n>m)=\frac{m^{-\alpha}}{\Gamma(1-\alpha)}
       +c_{n,\alpha}m^{-2\alpha}+o(m^{-2\alpha}),
   \qquad
   c_{n,\alpha}=\frac{\alpha}{\Gamma(1-\alpha)}
       \sum_{j=1}^{n-1}\frac{\Gamma(j-\alpha)}
                                  {\Gamma(j+1-2\alpha)}.
   \]
   The sum is zero when \(n=1\) and strictly positive when \(n\ge2\). Remarkably, the leading Pareto coefficient is **independent of the observation time**. Moreover,
   \[
   \mathbb E[W_n^s]<\infty\quad\Longleftrightarrow\quad0<s<\alpha.
   \]
   Thus \(\mathbb E[W_n]=\infty\) for every finite observation time. The second coefficient itself obeys \(c_{n,\alpha}\sim n^\alpha/\Gamma(1-\alpha)\) as \(n\to\infty\); this coefficient asymptotic does *not* assert a uniform two-scale expansion.

3. Let \(M\) have the standard Mittag-Leffler distribution of parameter \(\alpha\), characterized by
   \[
   \mathbb E[e^{-tM}]=E_\alpha(-t),\qquad
   E_\alpha(z)=\sum_{j=0}^{\infty}\frac{z^j}{\Gamma(1+\alpha j)}.
   \]
   Let \(E\) be mean-one exponential and independent of \(M\). Then the *joint* local-wait limit is
   \[
   \left(\frac{K_n}{n^\alpha},\frac{W_n}{n^{1-\alpha}}\right)
      \ \Longrightarrow\ \left(M,\frac{E}{\alpha M}\right).
   \]
   Therefore, for every \(x\ge0\),
   \[
   \lim_{n\to\infty}\Pr\!\left(W_n>x n^{1-\alpha}\right)
     =E_\alpha(-\alpha x),
   \qquad
   E_\alpha(-\alpha x)\sim
      \frac{1}{\alpha\Gamma(1-\alpha)x}\quad(x\to\infty).
   \]
   The deterministic-time far tail has exponent \(\alpha\), whereas the macroscopic, first-\(n\)-then-large-\(x\) tail has exponent one. These are different orders of limits, not two approximations claimed to be uniform simultaneously.

## Assumptions and scope

Fix \(p,q,r\ge0\) with \(p+q+r=1\) and \(0<r<1\). The first step is either \(+1\) or \(-1\) (with any probability distribution). Given \(X_1,\ldots,X_t\), choose \(J_t\) uniformly from \(\{1,\ldots,t\}\), independently of the next copying choice, and set \(X_{t+1}=X_{J_t}\) with probability \(p\), \(X_{t+1}=-X_{J_t}\) with probability \(q\), and \(X_{t+1}=0\) with probability \(r\). Use the natural filtration \(\mathcal F_t=\sigma(X_1,\ldots,X_t)\). At an already-zero increment, either copying sign remains zero.

The theorem concerns waiting for the next *nonzero increment*, not waiting for return of the walk's position to the origin. The observation time \(n\) is deterministic, not the time of the \(k\)-th nonzero increment. Part 2 takes \(m\to\infty\) with \(n\) fixed; Part 3 lets \(n\to\infty\) on the scale \(n^{1-\alpha}\). All stated parameters are in their open specified ranges.

## Proof

**Step 1: transition and survival.** Since only nonzero earlier increments can produce a nonzero next increment,
\[
\Pr(X_{t+1}\ne0\mid\mathcal F_t)=\frac{\alpha K_t}{t},\qquad
\Pr(K_{t+1}=K_t+1\mid\mathcal F_t)=\frac{\alpha K_t}{t}.
\]
On \(\{W_n>j\}\), the activity count remains equal to \(K_n=k\) at time \(n+j\). Multiplying the consequent conditional failure probabilities proves the product in Part 1 and its Euler-gamma expression. Because \(\alpha k>0\), gamma-ratio asymptotics show that the product tends to zero as \(m\to\infty\), proving almost-sure finiteness.

**Step 2: the rare activity classes.** As \(K_1=1\), the event \(\{K_n=1\}\) requires failure at every transition from times \(1\) through \(n-1\). Thus
\[
\Pr(K_n=1)=\prod_{t=1}^{n-1}\left(1-\frac\alpha t\right)
 =\frac{\Gamma(n-\alpha)}{\Gamma(n)\Gamma(1-\alpha)}.
\]
For \(n\ge2\), the event \(\{K_n=2\}\) has a unique first success, at the transition from time \(j\) to time \(j+1\), for some \(1\le j\le n-1\). After that success all remaining transitions fail. Summing over the disjoint success times yields
\[
\Pr(K_n=2)=\frac{\alpha\Gamma(n-2\alpha)}
 {\Gamma(1-\alpha)\Gamma(n)}
 \sum_{j=1}^{n-1}\frac{\Gamma(j-\alpha)}
                            {\Gamma(j+1-2\alpha)}.
\]
All gamma arguments in these formulas are positive for \(0<\alpha<1\).

**Step 3: the uniform-in-\(n\) leading coefficient, at fixed \(n\).** For each fixed \(n\) and attainable \(k\in\{1,\ldots,n\}\), the conditional survival in Step 1 has expansion
\[
\Pr(W_n>m\mid K_n=k)
 =\frac{\Gamma(n)}{\Gamma(n-\alpha k)}
    m^{-\alpha k}\bigl(1+O_{n,k,\alpha}(m^{-1})\bigr).
\]
The finite mixture over \(K_n\) therefore has its first coefficient \(\Pr(K_n=1)\Gamma(n)/\Gamma(n-\alpha)=1/\Gamma(1-\alpha)\), exactly independent of \(n\). Its second coefficient comes from \(K_n=2\) and equals the expression for \(c_{n,\alpha}\) in Part 2. The error from the first class is \(O(m^{-\alpha-1})=o(m^{-2\alpha})\), since \(\alpha<1\); the classes \(k\ge3\) are \(O(m^{-3\alpha})=o(m^{-2\alpha})\). This also covers \(n=1\), for which the second coefficient is zero. From the tail sum criterion for positive integer-valued random variables, \(\mathbb E[W_n^s]\) is finite exactly when \(s<\alpha\), proving the moment assertion. Finally, \(\Gamma(j-\alpha)/\Gamma(j+1-2\alpha)\sim j^{\alpha-1}\) and summation of this regularly varying sequence gives \(c_{n,\alpha}\sim n^\alpha/\Gamma(1-\alpha)\).

**Step 4: the local-wait limit.** The established activity-count theorem of Bercu [1, Lemma 2.1] gives
\[
K_n/n^\alpha\longrightarrow M>0\quad\text{almost surely},
\qquad \mathbb E[e^{-tM}]=E_\alpha(-t).
\]
Fix \(x>0\) and put \(m_n=\lfloor x n^{1-\alpha}\rfloor\). On the probability-one event of that convergence, \(K_n=O(n^\alpha)\). Expanding the logarithm of the conditional survival product from Step 1 gives
\[
\log\Pr(W_n>m_n\mid\mathcal F_n)
  =-\frac{\alpha K_n m_n}{n}
   +O\!\left(\frac{K_n m_n^2}{n^2}
         +\frac{K_n^2m_n}{n^2}\right)
  \longrightarrow-\alpha Mx.
\]
Both error terms tend to zero: their orders are \(n^{-\alpha}\) and \(n^{\alpha-1}\). The conditional survival consequently converges almost surely to \(e^{-\alpha Mx}\). Multiplying this convergence by an arbitrary bounded continuous function of \(K_n/n^\alpha\), taking expectations and applying dominated convergence proves joint convergence to the mixture whose conditional survival given \(M\) is \(e^{-\alpha Mx}\); equivalently its second coordinate is \(E/(\alpha M)\) with independent mean-one exponential \(E\). The result at \(x=0\) follows from the almost-sure positivity of \(M\).

**Step 5: asymptotic of the limiting tail.** By the standard Mittag-Leffler Laplace representation, \(\mathbb E[e^{-\alpha xM}]=E_\alpha(-\alpha x)\). The classical Pollard/Feller asymptotic \(E_\alpha(-t)\sim1/[t\Gamma(1-\alpha)]\) for \(t\to\infty\) and \(0<\alpha<1\) proves the last display. This uses an established special-function fact, not a claim newly proved here. All other identities and asymptotics are obtained above.

## Verification

Run `python CHECK.py` using the Python standard library. It verifies the finite-time conditional product formula against independent full-path enumeration, total mass and the one-activity probability, strict decrease of survival, and the exact formulas for the two leading asymptotic coefficients at rational parameter values. The checker also tests the deterministic conditional exponential approximation for larger sample sizes. It passes 609 finite checks. Enumerations and numerical approximations do not establish the infinite-size assertions; their proofs are Steps 1–5, with the cited activity-count theorem and classical Mittag-Leffler asymptotic explicitly identified as external inputs.

## Relationship to prior work

Miyazaki and Takei [7, Section 2] earlier studied the *same binary activity-count process* as the laziest minimal elephant walk, and proved its factorial moments, positive Mittag-Leffler limit, and central-limit refinements. Bercu [1] develops the signed elephant walk with stops and proves the almost-sure Mittag-Leffler limit for its number of nonzero increments. The present result **takes that known activity limit as an input**; it concerns the forward *waiting-time* law and its two distinct tail limits, neither asserted in [1]. Gut and Stadtmüller [3,4] analyze delays and counts of zero increments for related elephant walks rather than the deterministic-time forward waiting observable.

Huillet and Möhle [2, Section 8], building on Möhle’s general restaurant process [6], give a three-parameter harmonic Bernoulli Markov model. Its success count contains precisely the present activity-count transition under the parameter substitution \(w_1=\alpha\), \(w_2=1-\alpha\), and reinforcement parameter \(\alpha\), after matching the first index. Their Section 4 derives waiting laws for their *independent* harmonic Bernoulli model, while Section 8 analyzes the reinforced count process and its asymptotic count distribution. Miyazaki and Takei [7] also use precisely this birth-chain transition, but their Results, proofs and appendices address count moments, fluctuations and tree-percolation cluster sizes rather than forward observation-time waits. Consequently, neither the count-process construction nor the Mittag-Leffler activity limit is claimed here as new. The compared material does not state the observation-time-invariant far-tail constant, the next-term coefficient, or the joint local-wait limit with its different Pareto exponent. Specializations of broader species-sampling results remain a possible historical-priority risk; the relevant 2021 restaurant-process paper [6] was only available at abstract level for the present comparison, so no whole-paper non-coverage claim is made about it.

## Limitations

The law assumes full uniform memory, a nonzero initial increment, a fixed stop probability strictly between zero and one, and an independent copying choice at every step. It does not cover partial-memory walks, time-varying stop probabilities, or the boundary cases \(r=0\) and \(r=1\). The two asymptotic regimes are separately quantified; no joint uniform approximation across arbitrary growing \(m\) and \(n\) is established. Activity waiting times are not claimed independent or renewal distributed. The exact local-wait conclusion depends on the prior Mittag-Leffler activity-count theorem; the large-argument constant uses classical special-function theory. Historical priority beyond the inspected literature and independent mathematical validation remain open.

## References

[1] Bernard Bercu, *On the elephant random walk with stops playing hide and seek with the Mittag-Leffler distribution*, arXiv:2203.04196, first posted 2022-03-08. https://arxiv.org/abs/2203.04196

[2] Thierry Huillet and Martin Möhle, *On Bernoulli trials with unequal harmonic success probabilities*, arXiv:2211.17044, first posted 2022-11-30. https://arxiv.org/abs/2211.17044 ; open manuscript https://www.math.uni-tuebingen.de/user/moehle/bernoulli.pdf

[3] Allan Gut and Ulrich Stadtmüller, *The number of zeroes in Elephant random walks with delays*, arXiv:2005.09517, first posted 2020-05-19. https://arxiv.org/abs/2005.09517

[4] Allan Gut and Ulrich Stadtmüller, *Elephant random walks with delays*, arXiv:1906.04930, first posted 2019-06-11. https://arxiv.org/abs/1906.04930

[5] Harry Pollard, *The completely monotonic character of the Mittag-Leffler function \(E_\alpha(-x)\)*, Bulletin of the American Mathematical Society, 1948. See also the Mittag-Leffler discussion and references in [1].

[6] Martin Möhle, *A restaurant process with cocktail bar and relations to the three-parameter Mittag-Leffler distribution*, Journal of Applied Probability 58(4), 978–1006, publicly posted by the publisher 2021-11-22. https://doi.org/10.1017/jpr.2021.10 (abstract inspected; full text not available for comparison).

[7] Tatsuya Miyazaki and Masato Takei, *Limit theorems for the “laziest” minimal random walk model of elephant type*, arXiv:2003.04441, first posted 2020-03-09. https://arxiv.org/abs/2003.04441 (full text inspected).
