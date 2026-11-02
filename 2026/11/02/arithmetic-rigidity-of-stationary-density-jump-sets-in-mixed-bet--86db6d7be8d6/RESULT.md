# Arithmetic rigidity of stationary-density jump sets in mixed beta maps

## Finding

**Theorem (infinite-step rigidity and quantitative jump-count bounds).** Fix an integer \(b\ge2\), a noninteger slope \(1<\beta<2\), and \(0<p<1\). Independently at each step apply \(B_b(x)=\{bx\}\) with probability \(1-p\), or \(B_\beta(x)=\{\beta x\}\) with probability \(p\), on \([0,1)\). Let \(h\) be the unique stationary probability density, represented by its decreasing right-continuous version on \((0,1)\). Then:

1. \(h\) has **infinitely many distinct strictly positive downward jumps**, for *every* such parameter triple; in particular, it is never a finite-step density.
2. Set \(r=(1-p)/b\), \(s=p/\beta\), and \(q=r+s<1\). If \(\beta\) is irrational, the jump at \(t_j=\{b^j(\beta-1)\}\), \(j\ge0\), has magnitude at least \((1-q)sr^j\), and the \(t_j\) are distinct. If \(\beta=c/d\) in lowest terms with \(d\ge2\), the jumps at \(t_j=B_\beta^{j}(1)\), \(j\ge1\), are distinct, have magnitude at least \((1-q)s^j\), and each has reduced denominator \(d^j\).
3. Let \(J(\varepsilon)\) be the number of distinct jumps whose magnitude is strictly larger than \(\varepsilon>0\). Then
\[
\liminf_{\varepsilon\downarrow0}\frac{J(\varepsilon)}{\log(1/\varepsilon)}\ge
\begin{cases}
1/\log(b/(1-p)),&\beta\notin\mathbb Q,\\
1/\log(\beta/p),&\beta\in\mathbb Q.
\end{cases}
\]
For Lebesgue-almost every \(\beta\in(1,2)\), the jumps are dense in \((0,1)\) for **every** \(0<p<1\). The stationary density remains of bounded variation and has only countably many jump locations.

In particular, for \(b=2\) and the golden-ratio slope \(\beta=(1+\sqrt5)/2\), both deterministic component maps have finite-step stationary densities, while **every nontrivial Bernoulli mixture has infinitely many jumps**.

## Assumptions and scope

The dynamics is independent and identically distributed with the two positive probabilities fixed across steps. Fractional part is \(\{u\}=u-\lfloor u\rfloor\). The density is unique in the absolutely continuous stationary class, as established for these expanding random beta transformations in Suzuki's 2023 theorem. All jump assertions concern one-sided limits strictly inside \((0,1)\), and are unaffected by choices on null sets. The statement makes no claim that the stationary *measure* is atomic: the measure is absolutely continuous, while its density has jumps.

For any finite word \(w=(\lambda_1,\ldots,\lambda_n)\) with letters in \(\{b,\beta\}\), define \(t_w=B_{\lambda_n}\circ\cdots\circ B_{\lambda_1}(1)\) and \(a_w=\prod_{i=1}^n p_{\lambda_i}/\lambda_i\), with \(p_b=1-p\), \(p_\beta=p\). For the empty word set \(t_\varnothing=1\), \(a_\varnothing=1\).

## Proof

**Step 1: exact positive endpoint expansion.** For \(\lambda>1\), \(0\le t\le1\), and a.e. \(y\in[0,1)\), the Lebesgue transfer operator satisfies
\[
\mathcal L_\lambda\mathbf1_{[0,t)}(y)=
\frac{\lfloor\lambda t\rfloor}{\lambda}
+\frac{1}{\lambda}\mathbf1_{[0,\{\lambda t\})}(y).
\]
This follows by counting the inverse branches \((y+k)/\lambda\) that lie in \([0,t)\). Define
\[
H(x)=\sum_{n=0}^\infty\sum_{|w|=n}a_w\mathbf1_{[0,t_w)}(x),\qquad
Z=\int_0^1H(x)\,dx=\sum_w a_w t_w.
\]
Because \(r+s=q<1\), the length-\(n\) total coefficient is \(q^n\), giving uniform convergence, \(H\in BV\), and \(1\le Z\le(1-q)^{-1}\). Applying the transfer identity term-by-term to \(\mathcal L=(1-p)\mathcal L_b+p\mathcal L_\beta\) gives \(\mathcal LH=H+C-1\), where \(C\) is a constant: all nonconstant terms correspond bijectively to words extended by one letter. Integration preservation forces \(C=1\). Thus \(h=H/Z\) is stationary; uniqueness follows from the established expanding random-beta-map result.

**Step 2: no jump cancellation.** Each summand is nonincreasing in \(x\) and has nonnegative coefficient. Uniform absolute convergence permits termwise one-sided limits. At each \(t\in(0,1)\), the exact downward jump is
\[
\Delta h(t)=\frac1Z\sum_{w:t_w=t}a_w.
\]
Therefore \(\Delta h(t)>0\) at **every** endpoint reached by a positive-weight word, with no cancellation. There are no discontinuities outside the countable endpoint set because a uniformly convergent sum of step functions is continuous wherever each summand is continuous. The bounded-variation estimate follows from \(\sum_w a_w\le(1-q)^{-1}\).

**Step 3: irrational slope.** The one-letter word \((\beta)\) reaches \(\beta-1\), and extending by \(j\) letters \(b\) reaches \(t_j=\{b^j(\beta-1)\}\), with coefficient \(sr^j\). If two such points coincided, \((b^j-b^k)(\beta-1)\in\mathbb Z\) for distinct \(j,k\), forcing \(\beta\) rational. Hence all points are distinct for irrational \(\beta\), and \(1/Z\ge1-q\) proves the jump bound.

**Step 4: rational slope.** Write \(\beta=c/d\) in lowest terms, where \(d\ge2\). Inductively \(B_\beta^j(1)=u_j/d^j\) in lowest terms, since multiplying \(u_j/d^j\) by \(c/d\) and reducing modulo \(1\) preserves coprimality of the numerator with \(d\). Different denominators show all \(t_j\) distinct. The word of \(j\) consecutive \(\beta\)'s has coefficient \(s^j\), yielding its lower bound.

**Step 5: counting and generic density.** For irrational \(\beta\), the \(j\)-th distinguished jump exceeds \((1-q)sr^j\); consequently at least \(\log(1/\varepsilon)/\log(1/r)+O_{b,\beta,p}(1)\) jumps exceed \(\varepsilon\). The rational case similarly gives \(\log(1/\varepsilon)/\log(1/s)+O(1)\). Finally, multiplication by integer \(b\) modulo \(1\) is Lebesgue ergodic; for a.e. starting point \(a\in(0,1)\), its orbit meets every interval. Applying this to \(a=\beta-1\) gives the dense-jump assertion for a.e. slope and simultaneously for all \(p\in(0,1)\).

**Step 6: two finite-step components.** The integer map \(B_2\) has uniform invariant density \(1\). If \(\beta=(1+\sqrt5)/2\), then \(B_\beta(1)=\beta-1=\beta^{-1}\) and \(B_\beta^2(1)=0\); the deterministic Parry density is the two-level function
\[
\frac{1+\beta^{-1}\mathbf1_{[0,\beta^{-1})}(x)}{1+\beta^{-2}}.
\]
The irrational-slope conclusion proves that mixing these two finite-step systems generates an infinite jump hierarchy for every nontrivial probability.

## Verification

The attached standard-library script `check.py` independently enumerates all words through length eight for three rational slope/probability triples, evaluates the transfer-operator action on rational step functions, checks the exact finite-depth residual bound \(\|\mathcal LH_N-H_N\|_\infty\le q^{N+1}\) on a rational sample grid, and verifies every asserted rational-orbit jump lower bound through that depth. It passed all 24 finite-depth cases. The mathematical proof above, not finite tests, establishes the infinite statements. The finite-depth residual bound itself follows exactly: the transfer of \(H_N\) contains its lower-depth steps plus a constant and the length-\(N+1\) tail; mass preservation makes the constant the negative tail integral, whose oscillation and supremum are at most \(q^{N+1}\).

## Relationship to prior work

Suzuki (2023, arXiv:2303.17521, Theorem 3.1) proves the crucial general positive endpoint-series representation and uniqueness of the stationary density, and Theorem 4.2 establishes linear response; these are **prior results**. The present statement does not re-claim those formulas. Its additional conclusion is the all-parameter infinite-step rigidity, the split arithmetic witnesses, explicit finite-threshold jump-count bounds, and a.e. dense discontinuities for an integer/noninteger two-slope mixture. Kalle–Maggioni (2018) provides a more general construction for random piecewise-linear invariant densities. Dajani–Kalle–Maggioni (2020) develops random matching criteria yielding finite-step densities for other random interval-map families. Bahsoun–Ruziboev–Saussol (2017) provides general random linear-response theory. The precise implication risk from Suzuki's strong formula is acknowledged below.

## Limitations

This is a structural characterization of jump sets, **not** an independent reconstruction of a previously unknown stationary density. The bounds on the number of jumps are lower bounds; exact asymptotics and the structure of orbit collisions remain open here. Dense jumps are asserted only for almost every slope, not every irrational slope. The transfer-series expansion from Suzuki is strong enough that this theorem may be viewed as a derived consequence; priority for the *arithmetic rigidity and quantitative complexity* assertions requires independent literature checking. No independent mathematical audit has been performed.

## References

1. S. Suzuki, *Absolutely continuous invariant measures for random dynamical systems of beta-transformations*, arXiv:2303.17521 (first posted 2023-03-30), especially Theorems 3.1 and 4.2, https://arxiv.org/abs/2303.17521.
2. C. Kalle and M. Maggioni, *Invariant densities for random systems of the interval*, arXiv:1805.11430 (first posted 2018-05-29), https://arxiv.org/abs/1805.11430.
3. W. Bahsoun, M. Ruziboev, B. Saussol, *Linear response for random dynamical systems*, arXiv:1710.03706 (2017), https://arxiv.org/abs/1710.03706.
4. K. Dajani, C. Kalle, M. Maggioni, *Matching for random systems with an application to minimal weight expansions*, arXiv:2008.04398 (2020), https://arxiv.org/abs/2008.04398.
