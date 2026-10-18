# A large-index phase profile for monomial perturbations of Euler's partition product

## Finding

Let \(P(z)=\prod_{m\ge1}(1-z^m)\) and \(Q(z)=1/P(z)=\sum_{n\ge0}p(n)z^n\), where \(p(n)\) counts unrestricted integer partitions. For real \(a>0\) and integer \(j\ge1\), write
\[
C_{a,j}(z)=\frac{1}{P(z)-az^j}=\sum_{n\ge0}c_{a,j}(n)z^n.
\]
There is a unique \(\rho_{a,j}\in(0,1)\) satisfying \(P(\rho_{a,j})=a\rho_{a,j}^{j}\). Put \(t_{a,j}=-\log\rho_{a,j}\) and
\[
E(t)=\sum_{m\ge1}\frac{m}{e^{mt}-1},\qquad
V(t)=\sum_{m\ge1}\frac{m^2e^{-mt}}{(1-e^{-mt})^2},\qquad
L_{a,j}=j+E(t_{a,j}).
\]
For each **fixed** \((a,j)\), as \(n\to\infty\),
\[
c_{a,j}(n)=\frac{e^{jt_{a,j}}}{aL_{a,j}}e^{nt_{a,j}}\bigl(1+O_{a,j}(\delta_{a,j}^{n})\bigr),
\qquad 0<\delta_{a,j}<1.
\tag{1}
\]
In particular, the coefficients are positive and have a sharp exponential asymptotic, including a leading constant.

An equivalent positive weighted model consists of \(k+1\) ordered integer partitions separated by \(k\) marked tokens, each contributing weight \(a\) and size \(j\). Its total-size-\(n\) weight is \(c_{a,j}(n)\). Let \(K_{n;a,j}\) be its number of marked tokens, sampled with weights proportional to \(a^k\). For each fixed \((a,j)\), with \(t=t_{a,j}\) and \(L=j+E(t)\),
\[
\mathbb E K_{n;a,j}=\frac{n}{L}+O_{a,j}(1),\qquad
\operatorname{Var}(K_{n;a,j})=\frac{V(t)}{L^3}n+O_{a,j}(1),
\tag{2}
\]
\[
\frac{K_{n;a,j}-n/L}{\sqrt{nV(t)/L^3}}\ \xrightarrow{\mathrm d}\ N(0,1).
\tag{3}
\]
These fixed-parameter conclusions instantiate established supercritical-sequence theory; the **new focus is the following coupled large-index limit**.

Let \(A=\pi^2/6\). Fix any real \(\gamma\), and for each \(j\ge1\) set \(a_j=\exp(\gamma\sqrt j)\). Define
\[
s_{\gamma}=\frac{\gamma+\sqrt{\gamma^2+4A}}2,
\qquad \Theta(\gamma)=\frac{s_{\gamma}^2}{s_{\gamma}^2+A},
\qquad \Xi(\gamma)=\frac{2As_{\gamma}^3}{(s_{\gamma}^2+A)^3}.
\]
Then, with \(t_j=t_{a_j,j}\), the **exponential growth rate, mean marked-size fraction, and scaled fluctuation coefficient** satisfy
\[
\boxed{\lim_{j\to\infty}\sqrt j\,t_j=s_\gamma,}\qquad
\boxed{\lim_{j\to\infty}\frac{j}{j+E(t_j)}=\Theta(\gamma),}\qquad
\boxed{\lim_{j\to\infty}\frac{j^{3/2}V(t_j)}{(j+E(t_j))^3}=\Xi(\gamma).}
\tag{4}
\]
The phase profiles satisfy the exact duality \(\Theta(-\gamma)=1-\Theta(\gamma)\) and \(\Xi(-\gamma)=\Xi(\gamma)\). The fluctuation profile has its unique maximum at the balanced point \(\gamma=0\), where \(\Xi(0)=\sqrt6/(4\pi)\). Indeed \(s_\gamma s_{-\gamma}=A\), and differentiation of \(2As^3/(s^2+A)^3\) shows the maximum occurs at \(s^2=A\).

In the iterated limit \(n\to\infty\) **before** \(j\to\infty\), the second assertion describes the fraction \(jK_{n;a_j,j}/n\) of total size attributable to marked tokens. Its limiting value is \(\Theta(\gamma)\), ranging continuously from zero to one as \(\gamma\) runs from negative to positive infinity. In particular \(\Theta(0)=1/2\): a fixed positive perturbation weight, placed sufficiently far out, yields asymptotically equal marked and unmarked contributions after the large-size limit.

For every **fixed** real \(a>0\), there is also a second-order large-\(j\) expansion
\[
\boxed{t_{a,j}=\frac{\pi}{\sqrt{6j}}-\frac{\log j}{8j}
+\frac{2\log a-\log(2\sqrt6)}{4j}
+O_a\!\left(\frac{(\log j)^2}{j^{3/2}}\right).}
\tag{5}
\]
If \(B_{a,j}=e^{jt_{a,j}}/(aL_{a,j})\) is the coefficient constant in (1), then
\[
\boxed{B_{a,j}\sim\frac{\exp(\pi\sqrt{j/6})}{2\sqrt a\,(2\sqrt6)^{1/4}j^{9/8}}.}
\tag{6}
\]
The limits in (4) concern parameters \(j\to\infty\) after the fixed-parameter coefficient or probability asymptotics; no claim of uniformity in a simultaneous \(n,j\to\infty\) regime is made.

## Assumptions and scope

An integer partition may be empty, with \(p(0)=1\). Each marked separator is distinguishable by its position among the ordered partition blocks. Real weights \(a>0\) are used as positive statistical weights; integer weights are not required. Every statement (1)--(3) holds separately for each fixed \(a>0\) and \(j\ge1\). In (4), \(\gamma\in\mathbb R\) is fixed and \(a_j=\exp(\gamma\sqrt j)\). In (5)--(6), \(a>0\) is fixed independent of \(j\). The stated asymptotic notations have constants with exactly those indicated dependencies.

## Proof

**1. Unique pole and the weighted model.** For \(|z|<1\), \(Q(z)\) is analytic and has strictly positive coefficients \(p(n)\), including \(p(0)=p(1)=1\). Set \(H(z)=az^jQ(z)\). Its positive real value increases strictly from zero to infinity on \((0,1)\), hence has exactly one positive solution \(H(\rho)=1\). For \(|z|<\rho\), \(|H(z)|\le H(|z|)<1\). On \(|z|=\rho\), equality \(H(z)=1\) can occur only at \(z=\rho\): the positive coefficients at exponents \(j\) and \(j+1\) force their phases to agree and both to equal \(1\). The pole at \(\rho\) is simple because \(H'(\rho)>0\). Analyticity in \(|z|<1\) and discreteness of zeros permit a circle of radius \(R\in(\rho,1)\) containing no other pole. Since
\[
C_{a,j}(z)=\frac{Q(z)}{1-H(z)}
=\sum_{k\ge0}a^kz^{jk}Q(z)^{k+1},
\tag{7}
\]
(7) gives the stated block model and nonnegative coefficients. The residue of the unique leading pole gives
\[
[z^n]C_{a,j}(z)=\frac{Q(\rho)}{\rho H'(\rho)}\rho^{-n}+O(R^{-n}).
\]
Now \(\rho Q'(\rho)/Q(\rho)=E(-\log\rho)\) by logarithmic differentiation of the Euler product, and \(\rho H'(\rho)=j+E(-\log\rho)\). Also \(Q(\rho)=e^{jt}/a\) from \(H(\rho)=1\). This proves (1).

**2. Marked-block moments.** Marking the count of separators gives the bivariate generating function
\[
C_{a,j}(z,u)=\frac{Q(z)}{1-uH(z)}.
\]
For complex \(u\) near \(1\), the simple dominant pole \(\rho(u)\), defined by \(uH(\rho(u))=1\), varies analytically, and the coefficient asymptotic is uniform in a neighborhood of \(u=1\). Write \(u=e^v\), \(w(v)=\log\rho(e^v)\), and \(h(w)=\log H(e^w)\). Then \(v+h(w(v))=0\). At \(v=0\),
\[
h'(w(0))=L=j+E(t),\qquad h''(w(0))=V(t),
\]
so \(w'(0)=-1/L\) and \(w''(0)=-V(t)/L^3\). Thus the logarithmic moment generating function of \(K_{n;a,j}\) equals
\[
n\bigl(w(0)-w(v)\bigr)+O_{a,j}(1),
\]
with first and second derivatives \(n/L+O(1)\) and \(nV(t)/L^3+O(1)\). Its third and higher derivatives are \(O_{a,j}(n)\), and rescaling \(v\) by \(n^{-1/2}\) yields Gaussian convergence (3), since \(V(t)>0\). This proves (2)--(3) without invoking a stronger unproved probabilistic approximation.

**3. Modular asymptotics.** Let \(t>0\), \(A=\pi^2/6\). The Dedekind eta transformation yields the **exact identity**
\[
Q(e^{-t})=\sqrt{\frac{t}{2\pi}}\exp\!\left(\frac A t-\frac t{24}\right)
\frac{1}{P(e^{-4\pi^2/t})}.
\tag{8}
\]
For \(t\downarrow0\), logarithms and derivatives of (8) give
\[
\log Q(e^{-t})=\frac A t+\frac12\log\frac{t}{2\pi}-\frac t{24}
+O(e^{-4\pi^2/t}),
\]
\[
E(t)=\frac A{t^2}-\frac1{2t}+\frac1{24}+O(t^{-2}e^{-4\pi^2/t}),
\qquad
V(t)=\frac{2A}{t^3}-\frac1{2t^2}+O(t^{-4}e^{-4\pi^2/t}).
\tag{9}
\]
The error terms absorb polynomial factors into the exponentially small remainders if necessary; the displayed derivative orders are valid for sufficiently small \(t\).

**4. Coupled phase limit.** The defining root equation, equivalently \(H(e^{-t})=1\), is
\[
j t=\log a+\log Q(e^{-t}).
\tag{10}
\]
For \(a=a_j=e^{\gamma\sqrt j}\), set \(s=t\sqrt j\). By (8), uniformly on any compact subinterval of \((0,\infty)\), equation (10) divided by \(\sqrt j\) tends to \(s=\gamma+A/s\). Its right-minus-left side is strictly decreasing as a function of \(s\), with a unique positive root \(s_\gamma\). Comparison on either side of this root proves \(t_j\sqrt j\to s_\gamma\). Substituting into (9) gives \(E(t_j)/j\to A/s_\gamma^2\) and \(V(t_j)/j^{3/2}\to2A/s_\gamma^3\), which prove every limit in (4). The stated profile dualities follow from \(s_\gamma s_{-\gamma}=A\); differentiating \(\Xi\) as a function of \(s>0\) gives a single maximum at \(s=\sqrt A\), corresponding to \(\gamma=0\).

**5. Sharper fixed-weight expansion.** Fix \(a>0\), let \(t_0=\sqrt{A/j}\), and define \(G_j(t)=jt-\log a-\log Q(e^{-t})\). Equation (10) is \(G_j(t)=0\), and \(G_j'(t)=j+E(t)>0\). By (8)--(9), \(G_j(t_0)=-\log a-\tfrac12\log(t_0/(2\pi))+O(j^{-1/2})\) and \(G_j'(t_0)=2j+O(\sqrt j)\). Taylor's theorem around \(t_0\), with \(G_j''(t)=O(j^{3/2})\) on a fixed relative neighborhood, gives
\[
t_{a,j}=t_0+\frac{\log a+\frac12\log(t_0/(2\pi))}{2j}
+O_a\!\left(\frac{(\log j)^2}{j^{3/2}}\right).
\]
Using \(t_0/(2\pi)=1/(2\sqrt{6j})\) yields (5). Finally \(E(t_{a,j})/j\to1\) and \(B_{a,j}=e^{jt_{a,j}}/[a(j+E(t_{a,j}))]\). Exponentiating (5) gives (6).

## Verification

The standalone standard-library script `check.py` performs 975 exact coefficient equalities. One method inverts the perturbed Euler pentagonal series; the other independently sums marked-block weights using ordinary partition dynamic programming. It additionally checks 36 numerical root/profile quantities at \(j=100,400,1600\) for \(\gamma=-1,0,1\), and eight fixed-weight asymptotic comparisons, printing `CHECKS_PASS`. These are finite regression checks, **not** replacements for the analytic proof. Run from the directory containing this document using `python check.py`; it requires Python 3 and no additional packages.

## Relationship to prior work

Keith, Schneider, and Sills explicitly conjectured exponential growth for \(1/(P(z)-az^j)\) at all fixed positive \(a\) and positive integer \(j\). The fixed-parameter exponential asymptotic (1) resolves that formulation, but it is itself an application of Flajolet--Sedgewick's pre-existing supercritical-sequence asymptotic theorem and is **not claimed independently new**. Similarly, fixed-parameter Gaussian component counts lie in the established analytic-combinatorics framework.

The central contribution claimed here is instead the *coupled large-index dependence* (4), including its explicit continuous marked-mass and fluctuation phase profiles, and the precise logarithmic correction and amplitude (5)--(6). These involve the Dedekind eta modular transformation and parameter-dependent root analysis absent from the cited fixed-schema statement. Keith's subsequent treatment of false-theta reciprocals concerns different generating functions, not this monomial-index crossover. The possibility of an earlier general perturbative theorem subsuming the coupled limit remains an originality risk.

## Limitations

The order of limits is explicit: fixed \(j\) first, then \(j\to\infty\). No simultaneous \(n,j\) asymptotic, uniform error estimate in \(j\), or assertion for nonpositive \(a\) follows. The ordinary fixed-parameter singularity and Gaussian mechanisms are established methods; originality is limited to the specified large-index phase calculations. The numerical script is illustrative, not an infinite certificate. No independently audited priority or proof status is asserted.

## References

1. W. J. Keith, R. Schneider, A. V. Sills, *Composition-Theoretic Series and False Theta Functions*, INTEGERS 24A (2024), A11, published May 27, 2024, DOI: 10.5281/zenodo.11352821; accessible article: https://math.colgate.edu/~integers/a11Proc23/a11Proc23.pdf. Conjecture 1 on page 12.
2. P. Flajolet, R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press (2009), Section V.2 on supercritical sequences. Freely available author's version: https://algo.inria.fr/flajolet/Publications/book.pdf. Earlier lecture version: https://algo.inria.fr/flajolet/Teach/fascII.pdf, Section V.3, Theorem V.3.
3. Z.-Y. Kong, L.-P. Teo, *An Elementary Proof of the Transformation Formula for the Dedekind Eta Function*, arXiv:2302.03280 (2023); https://arxiv.org/abs/2302.03280.
4. W. J. Keith, *Reciprocals of False Theta Functions*, arXiv:2412.19998 (first public December 2024; consulted version January 2025), https://arxiv.org/abs/2412.19998.
