# Convex fixed-point regression and stochastic incomparability of cyclic counts in random mappings

## Finding
Let \(f:[n]\to[n]\) be uniformly selected from the \(n^n\) self-maps, for an integer \(n\ge3\). Write \(K\) for the number of fixed points and \(C\) for the number of cyclic vertices. Here a vertex is cyclic when it belongs to a directed cycle, including a loop. Set \(q=n-1\), and write \((a)_{\underline j}=a(a-1)\cdots(a-j+1)\), with \((a)_{\underline0}=1\).

**Theorem.** The regression \(\mu_k=\mathbb E[C\mid K=k]\), for integer \(0\le k\le n\), satisfies
\[
\mu_k=k+\sum_{j=2}^{n-k}\frac{(n-k)_{\underline j}}{q^j}.
\]
Its successive differences \(\mu_{k+1}-\mu_k\), \(0\le k<n\), are strictly increasing. The unique minimizing condition is \(K=1\), with
\[
\mu_2-\mu_1=\frac1q,\qquad
\mu_0-\mu_1=\frac1q\sum_{t=1}^{q}\frac{(q)_{\underline t}}{q^t}
\sim\sqrt{\frac{\pi}{2n}}.
\]
For every \(1\le k\le n-2\), neither \(C\mid K=k\) nor \(C\mid K=k+1\) first-order stochastically dominates the other. The two strict opposite-sign tail differences are
\[
\begin{aligned}
&\Pr(C\ge k+1\mid K=k+1)-\Pr(C\ge k+1\mid K=k)
=\frac{k n^{n-k-1}}{q^{n-k}}>0,\\
&\Pr(C\ge k+2\mid K=k+1)-\Pr(C\ge k+2\mid K=k)
=\frac{n^{n-k-2}(k-q)}{q^{n-k}}<0.
\end{aligned}
\]
Nevertheless, the aggregate dependence cancels exactly:
\[
\operatorname{Cov}(K,C)=0.
\]
Thus the fixed-point count provides a nonlinear, nonmonotone conditional predictor of the cyclic-vertex count despite zero linear covariance.

## Assumptions and scope
All \(n^n\) maps are equally likely, equivalently their images are independent and uniformly distributed over \([n]\). Conditional events \(\{K=k\}\) have positive probability for every \(0\le k\le n\). At \(k=n\), the map is the identity and \(C=n\). At \(k=0\), there are no one-cycles and \(C\ge2\). First-order stochastic order compares all upper-tail probabilities at integer thresholds. The incomparability statement concerns \(1\le k\le n-2\) only. No stochastic-order assertion is made for \(k=0\) versus \(k=1\) or for \(k=n-1\) versus \(k=n\).

## Proof
**Conditional enumeration (established ingredients).** For a specified cyclic vertex set \(S\) of size \(c\), the directed forest rooted at \(S\) has \(c n^{n-c-1}\) choices, interpreted as one when \(c=n\). This follows from the rooted-forest matrix-tree determinant: the relevant principal minor of \(nI-J\) has eigenvalues \(c\) once and \(n\) with multiplicity \(n-c-1\). The map restricted to \(S\) is a permutation. The number of permutations of \(c\) labels with exactly \(k\) fixed points is \(\binom ck D_{c-k}\), where \(D_0=1\), \(D_1=0\), and \(D_j=(j-1)(D_{j-1}+D_{j-2})\) for \(j\ge2\). Hence
\[
\Pr(K=k,C=c)=\frac{\binom nc\binom ck D_{c-k}\,c n^{n-c-1}}{n^n}.
\]
The fixed-point indicators are independent Bernoulli variables of parameter \(1/n\), so \(K\sim\mathrm{Bin}(n,1/n)\). Division yields, with \(m=n-k\),
\[
\Pr(C=k+j\mid K=k)=\frac{\binom mj D_j (k+j)n^{m-j}}{n q^m},
\quad 0\le j\le m.
\]
In the displayed formula the factor \(n^{m-j}/n\) also covers the boundary \(j=m\) without negative exponents.

**Conditional mean and convexity.** Conditional on the identities of the \(k\) fixed points, each remaining vertex independently chooses one of the \(q\) vertices other than itself. A specified nonfixed vertex lies on an \(\ell\)-cycle, for \(2\le\ell\le m\), with probability \((m-1)_{\underline{\ell-1}}/q^\ell\). Summing over the \(m\) eligible vertices gives the formula for \(\mu_k\).

Put
\[
S_m=\sum_{j=2}^{m}\frac{j(m-1)_{\underline{j-1}}}{q^j},\qquad S_0=S_1=0.
\]
The falling-factorial subtraction identity
\((m)_{\underline j}-(m-1)_{\underline j}=j(m-1)_{\underline{j-1}}\)
shows
\[\mu_{k+1}-\mu_k=1-S_{n-k}.\]
Each term in \(S_m\) is nondecreasing with \(m\), and the \(j=2\) term increases strictly when \(m\ge2\). In addition, \(S_2>S_1\). Hence \(S_m\) is strictly increasing for \(m=1,2,\ldots,n\), and the successive differences of \(\mu_k\) strictly increase.

To identify the minimizer, let \(u_j=(q-1)_{\underline{j-1}}/q^{j-1}\) for \(1\le j\le q+1\). Then \(j u_j/q=u_j-u_{j+1}\) and \(S_q=1-1/q\). On the other hand, with \(v_j=(q)_{\underline{j-1}}/q^{j-1}\) we have \((j-1)v_j/q=v_j-v_{j+1}\). Therefore
\[S_{q+1}=1+\frac1q\sum_{t=1}^{q}\frac{(q)_{\underline t}}{q^t}>1.\]
Thus \(\mu_1-\mu_0=1-S_{q+1}<0\) while \(\mu_2-\mu_1=1-S_q=1/q>0\); strict convexity finishes the unique-minimum assertion.

For the asymptotic, set \(a_{q,t}=(q)_{\underline t}/q^t=\prod_{s=0}^{t-1}(1-s/q)\). Uniformly for \(t=O(\sqrt q)\), \(\log a_{q,t}=-t(t-1)/(2q)+O(t^3/q^2)\). The bound \(a_{q,t}\le\exp(-t(t-1)/(2q))\) controls the Gaussian tail beyond \(O(\sqrt q)\). The associated Riemann sum yields \(\sum_{t=1}^q a_{q,t}\sim\sqrt{\pi q/2}\), proving the displayed result since \(q=n-1\).

**Stochastic incomparability.** For \(1\le k\le n-2\), the conditional law at \(K=k\) has positive mass at \(C=k\), namely \(k n^{m-1}/q^m\), and no mass at \(C=k+1\) because \(D_1=0\). The conditional law at \(K=k+1\) has minimum \(C=k+1\) and mass \((k+1)n^{m-2}/q^{m-1}\) there. Subtracting upper tails at thresholds \(k+1\) and \(k+2\) proves both displayed inequalities. Opposite strict signs prohibit stochastic dominance in either direction.

**Zero covariance.** Fix a vertex \(i\) and write \(I_i=\mathbf1_{\{f(i)=i\}}\). The expected number of cyclic vertices in the unconditional mapping is
\[\mathbb E[C]=\sum_{\ell=1}^n\frac{(n)_{\underline\ell}}{n^\ell}.\]
Conditional on \(I_i=1\), the vertex \(i\) is cyclic and every other vertex remains an independent uniform chooser, giving
\[\mathbb E[C\mid I_i=1]=1+\sum_{\ell=1}^{n-1}\frac{(n-1)_{\underline\ell}}{n^\ell}.\]
Their difference is \(\sum_{\ell=1}^n \ell(n-1)_{\underline{\ell-1}}/n^\ell-1=0\): the terms telescope because, for \(b_\ell=(n-1)_{\underline{\ell-1}}/n^{\ell-1}\), \(b_\ell-b_{\ell+1}=\ell b_\ell/n\), \(b_1=1\), \(b_{n+1}=0\). Therefore \(\operatorname{Cov}(I_i,C)=0\) for every \(i\), and \(K=\sum_i I_i\) gives \(\operatorname{Cov}(K,C)=0\).

## Verification
The accompanying standalone file `verify_mapping.py` enumerates every self-map for \(3\le n\le7\), computes each cyclic set independently, and compares the conditional law, means, strict-convexity inequalities, adjacent upper-tail witnesses and zero covariance using exact rational arithmetic. It additionally tests the formulae and inequalities for \(8\le n\le70\) using exact integer coefficients. It reports 10,059 passed assertions. Those finite tests are reproducibility and error-detection checks; the all-size results rest on the proofs above. No Monte Carlo sampling or numerical extrapolation is used as proof.

## Relationship to prior work
Pitman's forest-volume identity (2001) and Hansen–Jaworski's general cyclic-point enumeration (2006) supply established counting foundations; neither that enumeration nor the displayed joint law is claimed as new. Hansen–Jaworski (2010) analyzes mapping components conditional on the cyclic-vertex count, a different direction of conditioning. The assessed result is the qualitative structure of \(\mathbb E[C\mid K=k]\), its sharp unique minimum, the adjacent stochastic-incomparability classification and its coexistence with exact zero global covariance. All are algebraically derivable from enumeration, so an older unpublished or unlocated inequality treatment could have priority.

## Limitations
The theorem concerns uniform independent-image mappings, not arbitrary weighted mapping models. The stochastic-order classification is explicitly restricted to successive positive fixed-point counts through \(n-2\). It does not give the exact joint shape of all nonadjacent conditional comparisons, concentration bounds, or an asymptotic joint limit theorem. Exact covariance zero does not assert independence. Some older mapping literature was available only at bibliographic or abstract level, leaving a genuine historical-priority risk; no claim of independent certification is made.

## References
1. Jim Pitman, *Forest volume decompositions and Abel–Cayley–Hurwitz multinomial expansions*, Berkeley Statistics Technical Report 591 (publicly dated April 1, 2001), https://live-statistics.pantheon.berkeley.edu/tech-reports/591 .
2. Jennie C. Hansen and Jerzy Jaworski, *A new random mapping model*, arXiv:math/0603529 (first submitted March 22, 2006), https://arxiv.org/abs/math/0603529 .
3. Jennie C. Hansen and Jerzy Jaworski, *Random mappings with a given number of cyclical points*, *Ars Combinatoria* 94 (2010), 341–359, https://combinatorialpress.com/ars-articles/volume-094-ars-articles/random-mappings-with-a-given-number-of-cyclical-points/ .
