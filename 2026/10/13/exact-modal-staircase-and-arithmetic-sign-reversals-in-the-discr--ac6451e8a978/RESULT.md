# Exact modal staircase and arithmetic sign reversals in the discrete asymmetric double Lindley law

## Finding

For every fixed asymmetry parameter \(\tau>0\), the global modes of the two-parameter discrete asymmetric double Lindley (DADL) law admit an exact, strictly ordered, infinite staircase as its concentration parameter \(\theta>0\) varies. Define the distinct increasing sites
\[
0=s_0<s_1<s_2<\cdots,
\qquad \{s_i:i\ge0\}=\{\tau j:j\in\mathbb Z_{\ge0}\}\cup\{k/\tau:k\in\mathbb Z_{\ge1}\}.
\]
Associate each site with its set of integer labels
\[
L_i=\{j\in\mathbb Z_{\ge0}:\tau j=s_i\}
\cup\{-k:k\in\mathbb Z_{\ge1},\ k/\tau=s_i\}.
\]
For \(i\ge0\), put
\[
\beta_i=\frac{\log(1+s_{i+1})-\log(1+s_i)}{s_{i+1}-s_i},
\qquad \beta_{-1}=+\infty.
\]
Then \(\beta_0>\beta_1>\cdots>0\), and \(\beta_i\to0\). The complete mode set is exactly
\[
\operatorname{argmax}_{x\in\mathbb Z}\Pr_{\theta,\tau}(X=x)=
\begin{cases}
L_i,&\beta_i<\theta<\beta_{i-1},\\
L_i\cup L_{i+1},&\theta=\beta_i.
\end{cases}
\]
These cases partition all \(\theta>0\), with the first open interval interpreted as \(\theta>\beta_0\). Each site is optimal on a nonempty open parameter interval; a site may correspond to two tied signed integers when the two grids coincide.

There is a sharp arithmetic dichotomy. If \(\tau^2=a/b\) for coprime positive integers \(a,b\), site \(s=m/\sqrt{ab}\), \(m>0\), is available exactly when \(a\mid m\) or \(b\mid m\), and has a positive mode label precisely if \(a\mid m\) and a negative mode label precisely if \(b\mid m\). Thus both positive and negative *unique* global modes recur infinitely often as \(\theta\downarrow0\) exactly when \(a>1\) and \(b>1\); the same recurrence holds when \(\tau^2\) is irrational. When \(\tau^2\) is an integer there are no negative-only sites, and when its reciprocal is an integer there are no positive-only sites. In particular, for a fixed \(\tau\), the unique modal sign changes infinitely often near \(\theta=0\) if and only if neither \(\tau^2\) nor \(\tau^{-2}\) is a positive integer. This claim concerns unique-mode intervals, not the isolated transition values or the positive-length intervals where both grids share a site.

## Assumptions and scope

The source's DADL law is supported on all integers \(x\), with \(\theta>0\), \(\tau>0\), \(p=e^{-\theta/\tau}\), \(q=e^{-\theta\tau}\), and strictly positive normalizing constant \(C=C(\theta,\tau)\). It has point masses
\[
\Pr(X=x)=
\begin{cases}
C(\tau-x)p^{-x},&x=-1,-2,\ldots,\\
C\tau(1+\tau x)q^x,&x=0,1,\ldots.
\end{cases}
\]
The parameters may approach but do not include \(\theta=0\). Modal multiplicity counts distinct integer outcomes, not site multiplicity. No assumptions on rationality or numerical precision are needed for the proof.

## Proof

**1. A common one-dimensional score.** Divide every point mass by the positive factor \(C\tau\). For a nonnegative outcome \(x=j\), the quotient is \((1+\tau j)e^{-\theta\tau j}\); for a negative outcome \(x=-k\), \(k\ge1\), it is \((1+k/\tau)e^{-\theta k/\tau}\). Hence, writing \(t=\tau j\) or \(t=k/\tau\), both sides have the same score
\[
w_\theta(t)=(1+t)e^{-\theta t},\qquad
\log w_\theta(t)=g(t)-\theta t,\quad g(t)=\log(1+t).
\]
Coincident site values have exactly equal probabilities irrespective of \(\theta\).

**2. Strictly ordered crossover parameters.** The twice differentiable function \(g\) satisfies \(g''(t)=-(1+t)^{-2}<0\) for all \(t\ge0\). Secant slopes on successive disjoint ordered intervals therefore satisfy \(\beta_i>\beta_{i+1}\). The mean-value theorem gives \(0<\beta_i\le(1+s_i)^{-1}\), and \(s_i\to\infty\); thus \(\beta_i\to0\). For successive sites,
\[
\log w_\theta(s_{j+1})-\log w_\theta(s_j)
=(s_{j+1}-s_j)(\beta_j-\theta).
\]
If \(\beta_i<\theta<\beta_{i-1}\), the scores strictly increase up to \(s_i\) and strictly decrease afterward, giving precisely \(L_i\). If \(\theta=\beta_i\), the scores strictly increase up to \(s_i\), agree at \(s_i\) and \(s_{i+1}\), and strictly decrease after \(s_{i+1}\), giving precisely \(L_i\cup L_{i+1}\). Since the slopes are strictly decreasing from \(\beta_0\) to zero, these are all positive \(\theta\).

**3. Exact lattice-collision classification.** An intersection \(\tau j=k/\tau>0\) exists exactly when \(\tau^2=k/j\) is rational. If \(\tau^2=a/b\) in lowest terms, then \(\tau=a/\sqrt{ab}\), \(\tau^{-1}=b/\sqrt{ab}\). The positive and negative sites are respectively \(aj/\sqrt{ab}\), \(j\ge1\), and \(bk/\sqrt{ab}\), \(k\ge1\). A positive-only site exists whenever \(m=aj\) is not divisible by \(b\); such sites recur infinitely often exactly if \(b>1\), by coprimality. A negative-only site exists whenever \(m=bk\) is not divisible by \(a\); such sites recur infinitely often exactly if \(a>1\). For \(ab\mid m\), both signs have equal score. If \(\tau^2\notin\mathbb Q\), no sites collide and each sign has infinitely many sites.

**4. Repeated sign reversals.** Every positive-only or negative-only site has an open \(\theta\)-interval where its single label is uniquely globally modal. Both site sequences are unbounded; hence arbitrarily far along the sorted list there are sites of both signs in the cases stated above. Because \(\beta_i\downarrow0\), those open parameter intervals approach zero and modal sign must reverse infinitely many times. Conversely, if the positive lattice contains the negative one, no negative-only site exists and a uniquely negative mode is impossible; the reciprocal inclusion similarly excludes uniquely positive modes. This proves the if-and-only-if statement, including both integer and reciprocal-integer exceptions.

## Verification

A standalone standard-library Python checker, `verify_modes.py`, reconstructs the source's normalizing constant, compares direct point masses against the common score, verifies finite consecutive slopes, tests the predicted maximizing outcome sets on a finite grid, verifies transition ties, and checks normalization numerically. Running `python3 verify_modes.py` prints `normalized weights, transition ties, and direct mode scans: PASS`. These checks illustrate the theorem; strict concavity and exact divisibility provide its all-parameter proof.

For \(\tau=\sqrt{3/2}\), the first positive site labels in order are \(-1,+1,-2,\{+2,-3\},-4,+3,-5\), after the zero site. The first four transition values are approximately \(0.731062082058\), \(0.496591311684\), \(0.412687677703\), and \(0.330809757632\); sample interior parameters successively give unique modes \(-1,+1,-2\). The grid intersection at \(\{+2,-3\}\) is a persistent two-way tie across its own open parameter interval.

## Relationship to prior work

Salinas et al. (2026), Section 2.4.6, prove only half-line unimodality and direct practitioners to compare a short list of modal candidates. Their paper does not state a global parameter-to-mode staircase, strict neighboring transition sequence, or the arithmetic recurrence of sign changes. The present finding uses their exact published probability mass function; it does not change the model or assert that their candidate-comparison procedure is wrong.

The symmetric integer-line sign-magnitude family of Alyami et al. (2025) concerns distributions constrained to symmetric modal behavior and therefore does not imply the two-grid asymmetric phase diagram. The skew discrete Laplace law of Kozubowski and Inusah (2006) has purely geometric tails rather than these linear-geometric Lindley kernels; its mode classification cannot give the DADL staircase or the grid-collision criterion. Strict concavity of the logarithm and arithmetic divisibility are standard ingredients, not separately claimed as novel.

## Limitations

The result describes population modes and their exact multiplicities for fixed \(\tau\); it does not characterize means, skewness signs, maximum-likelihood estimates, or finite-sample mode-estimation variability. Rational versus irrational assertions concern exact real parameters, and a floating-point approximation to \(\tau\) cannot establish the rationality of \(\tau^2\). The checker is finite and illustrative, not a proof of the infinite sign-reversal assertion. Priority remains subject to independently inspecting any unindexed equivalent result.

## References

1. H. S. Salinas, H. S. Bakouch, S. R. Bapat, A. F. Daghestani, and A. S. Aloufi, *Discrete Asymmetric Double Lindley Distribution on Z: Theory, Likelihood Inference, and Applications*, Symmetry 18 (2026), article 533, DOI: 10.3390/sym18030533 (published 20 March 2026; Sections 2.1 and 2.4.6).
2. L. Alyami, H. S. Salinas, H. S. Bakouch, M. Kachour, A. F. Daghestani, and S. R. Bapat, *Symmetric Discrete Distributions on the Integer Line: A Versatile Family and Applications*, Symmetry 17 (2025), article 2148, DOI: 10.3390/sym17122148.
3. T. J. Kozubowski and S. Inusah, *A skew Laplace distribution on integers*, Annals of the Institute of Statistical Mathematics 58 (2006), 555–571, DOI: 10.1007/s10463-005-0029-1.
