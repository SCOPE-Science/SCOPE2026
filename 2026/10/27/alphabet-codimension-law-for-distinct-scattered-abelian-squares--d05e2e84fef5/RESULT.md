# Alphabet-codimension law for distinct scattered Abelian squares in random words

## Finding

Fix an alphabet \(\Sigma\) with \(q\ge2\) symbols. A word \(uv\), with \(|u|=|v|\ge1\), is an *Abelian square* when each symbol has the same multiplicity in \(u\) and \(v\). For a word \(w\), let \(A(w)\) be the number of **distinct** nonempty Abelian-square words occurring as scattered (not necessarily contiguous) subsequences of \(w\). Different positional embeddings of the same word count only once.

Generate \(W_n\) by sampling letters independently with fixed probabilities \(\pi_a>0\), \(\sum_{a\in\Sigma}\pi_a=1\), and put \(A_n=A(W_n)\). Define

\[
g_a(z)=\frac{\pi_a z}{1-(1-\pi_a)z},\qquad U(z)=\sum_{a\in\Sigma}g_a(z).
\]

Write \(d=q-1\), fix one final symbol with \(\theta_q=0\), and for \(\theta\in[-\pi,\pi]^d\) define

\[
\Phi(z,\theta)=\left(\sum_{a\in\Sigma}g_a(z)e^{i\theta_a}\right)
\left(\sum_{a\in\Sigma}g_a(z)e^{-i\theta_a}\right).
\]

**Exact identity.** As a power series at \(z=0\),

\[
\boxed{\sum_{n\ge0}\mathbb E[A_n]z^n
=\frac{1}{1-z}\frac1{(2\pi)^d}
\int_{[-\pi,\pi]^d}\frac{\Phi(z,\theta)}{1-\Phi(z,\theta)}\,d\theta.}
\]

There is exactly one \(r\in(0,1)\) with \(U(r)=1\). Define

\[
v_a=g_a(r),\qquad \mu=rU'(r)>0,\qquad \sum_a v_a=1.
\]

**Asymptotic theorem.** For every fixed full-support source distribution and fixed \(q\ge2\),

\[
\boxed{\mathbb E[A_n]\sim
\frac{r^{-n}}{2(1-r)\mu}
\left(\frac{\mu}{2\pi n}\right)^{(q-1)/2}
\frac1{\sqrt{\prod_{a\in\Sigma}v_a}}.}
\]

Thus each independent Parikh-balance constraint costs one square-root power of word length, but does not change the exponential growth base. If \(T_n\) is the number of all distinct nonempty scattered subsequences, then

\[
\boxed{\frac{\mathbb E[A_n]}{\mathbb E[T_n]}\sim
\frac12\left(\frac{\mu}{2\pi n}\right)^{(q-1)/2}
\frac1{\sqrt{\prod_a v_a}}.}
\]

In particular, the ratio compares **expectations**, not the expectation of an individual-word ratio.

For the uniform source on \(q\) symbols, the theorem specializes to

\[
\boxed{\mathbb E[A_n]\sim
\frac{q^{3/2}}{2(q-1)}
\left(\frac{2q-1}{2\pi}\right)^{(q-1)/2}
\frac{(2-1/q)^n}{n^{(q-1)/2}}.}
\]

For the binary source with masses \(p\) and \(1-p\), let \(s=\sqrt{p(1-p)}\), and let \(g_0,g_1\) be the two weight series. There is also the algebraic closed form

\[
\boxed{\sum_{n\ge0}\mathbb E[A_n]z^n
=\frac1{1-z}\left(
\frac1{\sqrt{(1-(g_0+g_1)^2)(1-(g_0-g_1)^2)}}-1\right).}
\]

It follows that

\[
\mathbb E[A_n]\sim
\frac{(1+2s)\sqrt{1+s}}{4\sqrt\pi\,s^{3/2}}
\frac{(1+s)^n}{\sqrt n},\qquad
\frac{\mathbb E[A_n]}{\mathbb E[T_n]}\sim
\frac12\sqrt{\frac{1+s}{\pi s n}}.
\]

For the fair binary source, \(\mathbb E[A_n]\sim\sqrt{3/\pi}\,(3/2)^n/\sqrt n\).

## Assumptions and scope

The alphabet size \(q\) is a fixed finite integer at least two. All letter masses \(\pi_a\) are strictly positive, fixed as \(n\) increases, and independent across positions. Scattered subsequences preserve order but may skip positions. The empty word is not counted, and the two halves of an Abelian square have positive common length. No claim is made for Markov sources, growing alphabets, vanishing letter probabilities, or contiguous factor counts.

## Proof

**1. Greedy waiting times.** Fix a nonempty word \(u=a_1\cdots a_\ell\). In an i.i.d. infinite input, greedily match its letters from left to right. The successive waiting times are independent geometric variables on positive integers, with success parameters \(\pi_{a_j}\). The first \(n\) input symbols contain \(u\) as a scattered subsequence exactly when their waiting-time sum is at most \(n\). Consequently,

\[
\sum_{n\ge0}\Pr(u\preceq W_n)z^n
=\frac{1}{1-z}\prod_{j=1}^{\ell}g_{a_j}(z).
\]

This is an equality of absolutely convergent series for sufficiently small \(|z|\), or equivalently of formal power series.

**2. Parikh-balance Fourier filter.** Write an Abelian square uniquely as \(uv\) with \(|u|=|v|=m\ge1\). Expand \(\Phi(z,\theta)^m\). Its angular constant term retains exactly those pairs \((u,v)\) whose first \(q-1\) symbol counts agree; equality for the omitted final symbol follows because the halves have the same length. Summing over \(m\ge1\) and using step 1 gives the claimed exact torus integral.

**3. The unique dominant saddle.** Since \(g_a(0)=0\), \(g_a(1)=1\), and each \(g_a\) has strictly positive derivative on \((0,1)\), \(U(0)=0\) and \(U(1)=q>1\) give the unique \(r\in(0,1)\). Put \(t=z/r\) and \(F(t,\theta)=\Phi(rt,\theta)\). Then

\[
F(1,0)=1,\qquad \partial_tF(1,0)=2\mu.
\]

With \(v=(v_1,\ldots,v_{q-1})^\mathsf T\), define the positive-definite matrix

\[
\Sigma=\operatorname{diag}(v_1,\ldots,v_{q-1})-vv^\mathsf T.
\]

This is the covariance of the first \(q-1\) indicator coordinates of one letter with distribution \((v_a)_a\). Directly expanding the characteristic function of the difference of two independent such indicators gives

\[
F(1,\theta)=\left|\sum_a v_a e^{i\theta_a}\right|^2
=1-\theta^\mathsf T\Sigma\theta+O(\|\theta\|^4).
\]

The matrix determinant lemma yields

\[
\det\Sigma=\left(\prod_{a<q}v_a\right)
\left(1-\sum_{a<q}v_a\right)=\prod_{a\in\Sigma}v_a>0.
\]

By the analytic implicit-function theorem, the equation \(F(t,\theta)=1\) has, for \(\theta\) near zero, one simple root near \(t=1\), satisfying

\[
t(\theta)=1+\frac{\theta^\mathsf T\Sigma\theta}{2\mu}
+O(\|\theta\|^4).
\]

No other singularity competes on the unit circle: for \(|t|\le1\),

\[
\left|\sum_a g_a(rt)e^{i\theta_a}\right|
\le\sum_a g_a(r|t|)\le U(r)=1.
\]

All coefficients of every \(g_a\) at positive degree are strictly positive. Equality in the inequalities and their counterparts with negative phases is possible on \(|t|=1\) only for \(t=1\) and for all angular phases equal. The convention \(\theta_q=0\) makes this precisely \(\theta=0\). The poles of all \(g_a(rt)\) lie outside the closed unit disc. Compactness provides uniform annular continuation away from the one simple pole. Thus the standard residue contour for the coefficient of \(F/(1-F)\) is uniform in a small angular neighborhood; outside it coefficients are exponentially smaller.

**4. Gaussian integration and exact constant.** Near \(\theta=0\), the residue of \(F(t,\theta)/(1-F(t,\theta))\) at \(t=t(\theta)\) contributes

\[
\frac{t(\theta)^{-n-1}}{\partial_tF(t(\theta),\theta)}
=\frac{1+o(1)}{2\mu}
\exp\left(-\frac{n}{2\mu}\theta^\mathsf T\Sigma\theta\right)
\]

uniformly after rescaling \(\theta=O(n^{-1/2})\). Positive definiteness yields Gaussian decay outside that scale, and the nonzero-angular region contributes exponentially little. The Gaussian integral therefore gives, writing \(H(z)\) for the angular integral of \(\Phi/(1-\Phi)\),

\[
r^n[z^n]H(z)\sim
\frac{1}{2\mu}\frac{1}{(2\pi)^{q-1}}
\int_{\mathbb R^{q-1}}
\exp\left(-\frac{n}{2\mu}\theta^\mathsf T\Sigma\theta\right)d\theta
=\frac1{2\mu}\left(\frac{\mu}{2\pi n}\right)^{(q-1)/2}
\frac1{\sqrt{\det\Sigma}}.
\]

Since the full expectation generating function is \(H(z)/(1-z)\), its coefficients are cumulative sums of those of \(H\). With \(r<1\) and a polynomially varying positive prefactor, the last terms dominate the sum geometrically with factor \((1-r)^{-1}\). This gives the stated expected Abelian-square count.

**5. All distinct subsequences and specializations.** Summing the greedy identity over all nonempty patterns yields

\[
\sum_{n\ge0}\mathbb E[T_n]z^n
=\frac1{1-z}\frac{U(z)}{1-U(z)},
\qquad
\mathbb E[T_n]\sim\frac{r^{-n}}{(1-r)\mu}.
\]

Dividing proves the ratio of means. If all \(\pi_a=1/q\), then \(r=q/(2q-1)\), \(\mu=(2q-1)/q\), and \(v_a=1/q\), producing the displayed constant. For \(q=2\), the elementary integral identity \((2\pi)^{-1}\int_0^{2\pi}(A-B\cos\theta)^{-1}d\theta=(A^2-B^2)^{-1/2}\), valid first for \(A>|B|\), gives the algebraic formula. Finally, with \(s=\sqrt{p(1-p)}\), \(r=(1+s)^{-1}\), \(v_0v_1=s/(1+2s)\), and \(\mu=2(1+s)/(1+2s)\). Substitution gives the binary constants.

## Verification

Run `python3 verification.py` with Python 3 and no external dependencies. It compares a direct construction of all distinct scattered subsequence sets against an independently computed exact multinomial-weight generating series for seven positive rational source distributions on alphabets of sizes two through five. The exhaustive total is 39,286 source words. Three binary distributions are also checked against an independent algebraic-square-root differential recurrence. Uniform alphabet sizes two, three, and four are checked numerically at length 100 against the theorem's asymptotic constant using exact coefficient arithmetic before decimal comparison. These finite checks are supplementary, not a substitute for the analytic proof.

## Relationship to prior work

Richmond and Shallit [1] counted the number of Abelian-square *patterns* of a fixed length and supplied the multinomial-square formula; that identity is established prior mathematics and is used here. Fici, Mignosi and Shallit [2] investigated Abelian-square *contiguous factors* and factor-rich infinite words; their random-word factor scale differs fundamentally from scattered-subsequence occurrence. Biers-Ariel, Godbole and Kelley [3] studied expected total distinct subsequences in biased random words and did not impose the Parikh-equality constraint on two halves. Their unrestricted generating-function singularity is compatible with, but does not determine, the additional \(n^{-(q-1)/2}\) penalty and its full-support bias constant. Sequence tables for unweighted Abelian-square patterns [4] likewise do not enumerate distinct scattered Abelian-square subsequences of random source words.

The contribution claimed here is the exact probability-weighted scattered-pattern Fourier generating function **together with** the general alphabet-dependent local singularity theorem and explicit bias-sensitive constant, not the fixed-length pattern counts, the greedy subsequence method, the multinomial identity, or the unrestricted mean. No claim of independent external validation is made.

## Limitations

The result is about expectation, not typical values, concentration, variance, or the expected ratio of two random counts. Constants are not uniform as any \(\pi_a\) tends to zero or as \(q\) grows with \(n\). Finite experiments cannot prove the asymptotic theorem. Closely related unindexed or differently named results on weighted Abelian-pattern languages may exist; the checked primary literature does not conclusively exclude all such formulations.

## References

[1] L. B. Richmond and J. Shallit, *Counting Abelian Squares*, first public arXiv version July 31, 2008, https://arxiv.org/abs/0807.5028. Fixed-length unweighted pattern counts and multinomial enumeration.

[2] G. Fici, F. Mignosi and J. Shallit, *Abelian-Square-Rich Words*, first public arXiv version January 4, 2017, https://arxiv.org/abs/1701.00948. Contiguous-factor theory and random-factor comparison.

[3] Y. Biers-Ariel, A. Godbole and E. Kelley, *Expected Number of Distinct Subsequences in Randomly Generated Binary Strings*, first public arXiv version April 27, 2017, https://arxiv.org/abs/1704.08661. Bias-dependent unrestricted subsequences.

[4] OEIS A000984, A002893 and A002895, https://oeis.org/A000984, https://oeis.org/A002893 and https://oeis.org/A002895. Unweighted Abelian-square pattern counts for alphabet sizes two through four.
