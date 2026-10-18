# Limiting Bernoulli-parameter spectrum of antipersistent Markov occupation counts

## Finding
Let \(X_1,X_2,\ldots\) be a stationary two-state Markov chain with transition matrix
\[
P=\begin{pmatrix}1-a&a\\ b&1-b\end{pmatrix},\qquad 0<a,b<1,\quad a+b>1.
\]
For \(n\ge1\), define \(S_n=\sum_{j=1}^nX_j\) and its probability-generating polynomial \(F_n(z)=\mathbb E[z^{S_n}]\). The fact that \(F_n\) has \(n\) strictly negative, simple zeros in this regime is a consequence of the previously established real-zero argument of Dekking and Kong [1], and is **not claimed as new**. Write the zeros as \(-t_{n,1},\ldots,-t_{n,n}\), where every \(t_{n,j}>0\).

Set \(u=1-a\), \(v=1-b\), \(h=a+b-1\), and
\[
t_\pm=\frac{(\sqrt{ab}\pm\sqrt h)^2}{(1-b)^2},\qquad 0<t_-<t_+.
\]
**Claim:** As \(n\to\infty\), the empirical probability measures
\[
\nu_n=\frac1n\sum_{j=1}^n\delta_{t_{n,j}}
\]
converge weakly to the absolutely continuous probability measure with density
\[
\boxed{\rho_{a,b}(t)=\frac{u+vt}{2\pi t\sqrt{4ht-(u-vt)^2}}\,\mathbf 1_{(t_-,t_+)}(t).}
\]
Consequently the empirical success probabilities of the independent Bernoulli variables representing \(S_n\), namely \(p_{n,j}=1/(1+t_{n,j})\), converge weakly to the pushforward of \(\rho_{a,b}(t)\,dt\) under \(t\mapsto1/(1+t)\). The limiting parameter support is exactly \([1/(1+t_+),1/(1+t_-)]\).

In particular, for all \(t_-<r<s<t_+\),
\[
\lim_{n\to\infty}\frac1n\#\{j:r<t_{n,j}<s\}=\frac{\theta(s)-\theta(r)}\pi,
\quad \theta(t)=\arccos\!\left(\frac{u-vt}{2\sqrt{ht}}\right).
\]
This gives both a density and a cumulative spectral law for the independent-Bernoulli factors, rather than merely existence of a Poisson-binomial representation.

## Assumptions and scope
The transition parameters are fixed strictly inside the unit square with \(a+b>1\); the chain starts in its stationary distribution \(\Pr(X_1=1)=a/(a+b)\). The observation horizon \(n\) tends to infinity. No claim is made for parameters varying with \(n\), for \(a+b=1\), or for nonstationary transition matrices. Weak convergence permits finitely many zeros outside the limiting support; it does not assert finite-sample containment in the limiting interval.

## Proof
**Step 1: exact recurrence.** Cayley–Hamilton for the transfer matrix \(P\operatorname{diag}(1,z)\), together with the stationary initial law, yields
\[
F_0(z)=1,\qquad F_1(z)=\frac{b+az}{a+b},\qquad
F_{n+2}(z)=(u+vz)F_{n+1}(z)+hzF_n(z).
\]
Indeed, its trace is \(u+vz\), and determinant is \(-hz\). The recurrence also follows by directly conditioning on the last Markov state. Its constant and leading coefficients are positive, so \(\deg F_n=n\) and \(F_n(0)>0\).

**Step 2: real negative zeros and their number.** The general real-rootedness in this regime was established in [1, Proposition 4.2]. For completeness, the recurrence gives a strict interlacing proof. The unique zero of \(F_1\) is negative. If the zeros of \(F_{n-1}\) strictly interlace the \(n\) distinct negative zeros of \(F_n\), then at each zero \(r<0\) of \(F_n\),
\[
F_{n+1}(r)=hrF_{n-1}(r).
\]
These signs alternate; they force one zero between each consecutive pair of zeros of \(F_n\). Positivity of the leading coefficient and the sign at the smallest zero force a further zero to its left; \(F_{n+1}(0)>0\) and negativity at the largest zero force one more in the final interval before zero. Thus \(F_{n+1}\) has precisely \(n+1\) distinct negative zeros, strictly interlaced with those of \(F_n\).

**Step 3: the oscillatory band.** For \(z=-t\), the scalar recurrence has characteristic equation
\[
\lambda^2-(u-vt)\lambda+ht=0.
\]
Its discriminant is negative precisely for \(t_-<t<t_+\). To check the displayed endpoints, solve \((u-vt)^2=4ht\); the roots in \(\sqrt t\) are \((\sqrt{ab}\pm\sqrt h)/v\), using \(uv+h=ab\). The characteristic roots within the band are \(\sqrt{ht}\,e^{\pm i\theta(t)}\), with
\[
\theta(t)=\arccos\left(\frac{u-vt}{2\sqrt{ht}}\right),\qquad
\theta'(t)=\frac{u+vt}{2t\sqrt{4ht-(u-vt)^2}}>0.
\]
The angle increases continuously from \(0\) to \(\pi\) across this interval.

**Step 4: count finite zeros in every interior subinterval.** The real initial conditions in Step 1 give the exact identity
\[
F_n(-t)=(ht)^{n/2}\bigl[\cos(n\theta(t))+K(t)\sin(n\theta(t))\bigr],
\qquad
K(t)=\frac{F_1(-t)/\sqrt{ht}-\cos\theta(t)}{\sin\theta(t)}.
\]
On any compact subinterval \([r,s]\subset(t_-,t_+)\), the real function \(K\) is smooth. Set \(\varphi=\arctan K\). The bracket has the same zeros as \(\cos(n\theta-\varphi)\), since its positive prefactor is \(\sqrt{1+K^2}\). For sufficiently large \(n\), \(n\theta'-\varphi'>0\) on \([r,s]\); the number of zeros in \((r,s)\), counted once, is therefore
\[
\frac n\pi(\theta(s)-\theta(r))+O_{r,s}(1).
\]
Strict real-rootedness from Step 2 guarantees these are distinct zeros of \(F_n\); their total count cannot exceed \(n\).

**Step 5: tightness and limit.** For \(0<\varepsilon<(t_+-t_-)/2\), Step 4 counts asymptotically the proportion \((\theta(t_+-\varepsilon)-\theta(t_-+\varepsilon))/\pi\) of all \(n\) zeros. This tends to \(1\) as \(\varepsilon\downarrow0\), since \(\theta(t_-)=0\) and \(\theta(t_+)=\pi\). Thus the remaining mass outside any expanding family of interior intervals tends to zero; the empirical measures converge weakly to the law with cumulative distribution \(\theta(t)/\pi\) on \([t_-,t_+]\). Differentiating gives the displayed density, automatically integrating to one. Continuous mapping proves the Bernoulli-parameter statement: every negative zero \(-t\) corresponds to a factor proportional to \(1-p+pz\) with \(p=1/(1+t)\) [2, Theorem 4.1].

## Verification
A standalone exact-rational and floating-point checker is included as `verify.py`. It enumerates finite-state paths, reconstructs the probability-generating polynomials independently, checks the Cayley–Hamilton recurrence with rational arithmetic, locates negative zeros by sign changes and bisection, and compares empirical proportions with the proven limiting cumulative \(\theta/\pi\). Its finite examples test the formulas; they are not the proof of weak convergence, which is Steps 3–5.

## Relationship to prior work
Dekking and Kong [1, Proposition 4.2] already derived all-real zeros of the Markov-binomial polynomial when the two transition probabilities sum to at least one, using an earlier polynomial-root criterion; in particular **the existence of an independent-Bernoulli representation is prior theory**, not a new finding. Tang and Tang [2, Theorem 4.1] review the equivalence between real negative zeros and Poisson-binomial laws. Xia and Zhang [3] study approximation and moments of stationary Markov-binomial laws. The present claim identifies the exact weak empirical *distribution of the distinct Bernoulli parameters* as the observation horizon grows, with explicit support and density; these statements are not asserted by the inspected passages of [1]–[3]. Standard two-term spectral-recursion asymptotics underlie the derivation and are not claimed as new methods.

## Limitations
This is a deterministic root-parameter asymptotic, not an assertion that the dependent observations become independent. No claim of finite-sample root localization exactly in the limiting spectral band, convergence rates at its endpoints, or uniformity in transition parameters is made. The originality comparison relies on accessible primary texts and targeted searches; equivalent specializations of general polynomial-zero asymptotic theorems may exist under different terminology. The result has received no independent audit.

## References
[1] M. Dekking and D. Kong, *Multimodality of the Markov Binomial Distribution*, arXiv:1102.3613 (2011), especially Proposition 4.2 and its generating-function recurrence. https://arxiv.org/abs/1102.3613

[2] W. Tang and F. Tang, *The Poisson binomial distribution—Old & New*, arXiv:1908.10024 (first posted 2019-08-27), especially Theorem 4.1. https://arxiv.org/abs/1908.10024

[3] A. Xia and M. Zhang, *On approximation of Markov binomial distributions*, *Bernoulli* 15 (2009), 1335–1350; freely available at arXiv:1001.2144. https://arxiv.org/abs/1001.2144
