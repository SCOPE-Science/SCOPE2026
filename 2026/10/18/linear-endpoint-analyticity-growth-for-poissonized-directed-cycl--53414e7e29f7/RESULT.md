# Linear endpoint analyticity growth for Poissonized directed cycles

## Finding

Let \(n\ge2\), and let \(S_n\) be the cyclic translation \((S_nf)(k)=f(k+1\pmod n)\) on the real or complex spaces \(\ell^p(\mathbb Z/n\mathbb Z)\). Write \(L_n=I-S_n\), \(T_n(t)=\exp(-tL_n)\), and
\[
 M_n^{(p)}=\sup_{t>0}t\|L_nT_n(t)\|_{\ell^p\to\ell^p}.
\]
Then the two endpoint constants agree and obey the **sharp, dimension-linear asymptotic**
\[
 \lim_{n\to\infty}\frac{M_n^{(1)}}n
 =\lim_{n\to\infty}\frac{M_n^{(\infty)}}n
 =C_* =\frac4{\pi^2}u_*\sum_{j=0}^{\infty}e^{-(2j+1)^2u_*}
 =0.1491464853520236\ldots.
\]
Here \(u_*\) is the **unique** solution in \((3/5,1)\) of
\[
 \sum_{j=0}^{\infty}\bigl(1-(2j+1)^2u_*\bigr)
 e^{-(2j+1)^2u_*}=0,
 \qquad u_*=0.9972653787252169\ldots.
\]
Every maximizing time \(t_n\) (for either endpoint norm) satisfies
\[
 \lim_{n\to\infty}\frac{t_n}{n^2}
 =s_*:=\frac{u_*}{2\pi^2}=0.0505220542889816\ldots.
\]
For every finite \(n\) and \(t>0\) there is also an **exact kernel identity**:
\[
 \|L_nT_n(t)\|_{1\to1}=\|L_nT_n(t)\|_{\infty\to\infty}
 =\sum_{k=0}^{n-1}\bigl|p_{n,t}(k)-p_{n,t}(k-1)\bigr|,
\]
where \(p_{n,t}(k)=\sum_{m\ge0}\mathbf1_{\{m\equiv k\,({\rm mod}\ n)\}}e^{-t}t^m/m!\).
For contrast, the corresponding Hilbert-space constant is exactly
\[
 M_n^{(2)}=\frac1{e\sin(\pi/n)},\qquad
 \lim_{n\to\infty}\frac{M_n^{(2)}}n=\frac1{\pi e}.
\]
Consequently the endpoint-to-Hilbert growth-coefficient ratio is
\(\pi eC_*=1.273671345152158\ldots>1\).

## Assumptions and scope

The underlying group is the finite additive group \(\mathbb Z/n\mathbb Z\), \(n\) is an arbitrary integer at least two, and time is positive and real. The generator \(L_n\) is **nonsymmetric** for \(n\ge3\). No reversible-chain assumption or unspecified normalization of edge rates is used: the positive jump rate of the oriented cycle is precisely one. All norms are usual counting-measure \(\ell^p\) norms; normalizing counting measure to a probability does not change an operator norm on one \(\ell^p\) space. The limit concerns the endpoint \(p=1,\infty\) constants, while the stated Hilbert formula is an explicit comparison.

## Proof

**1. Exact finite-time norm.** The power series for \(T_n(t)=e^{-t}e^{tS_n}\) gives convolution by the probability vector \(p_{n,t}\). Thus \(L_nT_n(t)\) is convolution by \(p_{n,t}(k)-p_{n,t}(k-1)\), with a harmless change of orientation. A convolution matrix on a finite group has all absolute row sums and all absolute column sums equal to the \(\ell^1\) norm of its coefficient vector; these are precisely its induced \(\ell^\infty\) and \(\ell^1\) norms. The displayed identity follows, including norm attainment by a sign vector at \(p=\infty\) and by a point mass at \(p=1\).

**2. A uniform small-time bound.** Before wrapping, the Poisson mass function \(q_t(m)=e^{-t}t^m/m!\), \(m\ge0\), is unimodal. Hence
\[
 \sum_{m\ge0}|q_t(m)-q_t(m-1)|=2\max_{m\ge0}q_t(m)
 \le \frac{C}{\sqrt{1+t}},\qquad q_t(-1)=0,
\]
where the final inequality is the elementary Stirling bound (enlarging \(C\) for \(t\le1\)). Passing from integers to residues modulo \(n\) cannot increase this total variation. It follows that
\[
 \lim_{\varepsilon\downarrow0}\sup_{n\ge2}
 \sup_{0<t\le\varepsilon n^2}\frac{t}{n}\|L_nT_n(t)\|=0.
\]

**3. A uniform large-time bound.** With \(\theta_j=2\pi j/n\), Fourier diagonalization gives
\[
 p_{n,t}(k)=\frac1n\sum_{j=0}^{n-1}
 e^{t(e^{i\theta_j}-1)}e^{-ik\theta_j}.
\]
Putting \(r_j=\min(j,n-j)\), one has
\(1-\cos\theta_j\ge8r_j^2/n^2\) and
\(|1-e^{i\theta_j}|\le2\pi r_j/n\). Therefore, with \(v=t/n^2\ge1\),
\[
 \|L_nT_n(t)\|\le\sum_{j=1}^{n-1}
 |1-e^{i\theta_j}|e^{-t(1-\cos\theta_j)}
 \le\frac{4\pi}{n}\sum_{r\ge1}r e^{-8vr^2}
 \le\frac{C}{n}e^{-8v}.
\]
Consequently
\[
 \lim_{R\to\infty}\sup_{n\ge2}
 \sup_{t\ge Rn^2}\frac{t}{n}\|L_nT_n(t)\|=0.
\]
These two tail estimates also imply that each \(M_n^{(1)}=M_n^{(\infty)}\) is attained at some positive time.

**4. Diffusive window and circular Gaussian limit.** For fixed \(0<a<b<\infty\), put \(t=sn^2\) with \(s\in[a,b]\), and let
\[
 h_s(x)=\sum_{m\in\mathbb Z}e^{-2\pi^2m^2s}e^{2\pi imx}
 =\sum_{m\in\mathbb Z}\frac1{\sqrt{2\pi s}}
 e^{-(x+m)^2/(2s)}.
\]
This is the periodic Gaussian density of variance \(s\). Representing the Fourier indices in \([-n/2,n/2]\), expansion of \(e^{2\pi i j/n}\) yields
\[
 n^2\bigl(p_{n,sn^2}(k)-p_{n,sn^2}(k-1)\bigr)
 =-h_s'\bigl((sn^2-k)/n\bigr)+o(1)
\]
uniformly in \(s\in[a,b]\) and \(k\). Indeed, the exponent's cubic Taylor remainder is \(O(j^3/n)\), while the summands after multiplying by \(n^2\) are dominated by \(C|j|e^{-8aj^2}\); dominated convergence, first on bounded \(j\) and then on Gaussian tails, is uniform. Uniform shifted Riemann sums of the smooth periodic function \(|h_s'|\) then give
\[
 \sup_{s\in[a,b]}
 \left|\frac{sn^2}{n}\|L_nT_n(sn^2)\|
 -s\int_0^1|h_s'(x)|\,dx\right|\longrightarrow0.
\]
Together with steps 2–3, this yields the full maximized limit, provided the continuum variational constant is identified.

**5. Exact limiting profile.** The Jacobi triple-product formula for
\(q=e^{-2\pi^2s}\in(0,1)\) reads
\[
 h_s(x)=\prod_{m=1}^{\infty}(1-q^{2m})
 \bigl(1+2q^{2m-1}\cos(2\pi x)+q^{4m-2}\bigr).
\]
Every positive factor depending on \(x\) is strictly decreasing on \((0,1/2)\), so \(h_s\) is even and strictly decreasing between its maximum at zero and its minimum at one-half. It follows that
\[
 \int_0^1|h_s'(x)|\,dx
 =2\bigl(h_s(0)-h_s(1/2)\bigr)
 =8\sum_{j\ge0}e^{-2\pi^2(2j+1)^2s}.
\]
Writing \(u=2\pi^2s\), the variational constant becomes
\[
 C_* =\frac4{\pi^2}\max_{u>0}G(u),\qquad
 G(u)=u\sum_{j\ge0}e^{-(2j+1)^2u}.
\]

**6. The unique maximizing diffusion scale.** Let \(k\) run through positive odd integers. For \(u\ge1\),
\(G'(u)=\sum_k(1-k^2u)e^{-k^2u}<0\).
For \(u\le3/5\), periodization cannot increase the \(L^1\) norm of the derivative of the unwrapped Gaussian, so
\[
 \frac4{\pi^2}G(u)
 \le\sqrt{\frac{u}{\pi^3}}
 \le\sqrt{\frac3{5\pi^3}}
 <\frac4{e\pi^2}
 <\frac4{\pi^2}G(1).
\]
Thus every maximizer belongs to \((3/5,1)\). On the closed interval \([3/5,1]\),
\[
 G''(u)=-(2-u)e^{-u}
 +\sum_{k=3,5,\ldots}k^2(k^2u-2)e^{-k^2u}.
\]
For each \(k\ge3\), divide the corresponding positive summand by \((2-u)e^{-u}\) and call the ratio \(R_k(u)\). Its logarithmic derivative satisfies
\[
 \frac{d}{du}\log R_k(u)
 =\frac{k^2}{k^2u-2}+\frac1{2-u}-(k^2-1)
 \le\frac{45}{17}+1-8<0.
\]
Consequently \(\sum_{k\ge3}R_k(u)\le\sum_{k\ge3}R_k(3/5)<0.21<1\). For a direct tail bound, the \(k=3\) term is \((153/7)e^{-24/5}<0.2\); for odd \(k\ge5\), it is at most \((3/7)k^4e^{-(3/5)(k^2-1)}\), whose sum is less than \(0.001\) by comparison of successive terms. Hence \(G''(u)<0\) throughout \([3/5,1]\). Moreover \(G'(3/5)>0\) and \(G'(1)<0\), as follows directly by bounding the same exponentially decaying tails. Therefore there is precisely one root \(u_*\in(3/5,1)\) of \(G'\), and it is the unique global maximum.

**7. Maximizing times and Hilbert comparison.** The uniform compact-window convergence in step 4, the uniform tail bounds, and uniqueness in step 6 imply by a maximizing-subsequence argument that every exact endpoint maximizer satisfies \(t_n/n^2\to u_*/(2\pi^2)\). On \(\ell^2\), the Fourier multipliers of \(L_n\) are \(1-e^{2\pi ij/n}\). Optimizing \(t|1-e^{2\pi ij/n}|e^{-t(1-\cos(2\pi j/n))}\) gives \(1/(e|\sin(\pi j/n)|)\). The largest value for \(j\ne0\) is attained at \(j=1\) or \(j=n-1\), yielding the stated exact Hilbert formula.

## Verification

The accompanying `check.py` uses two independent finite calculations: a directly accumulated wrapped-Poisson mass and the diagonal Fourier representation of its time derivative. It checks their kernel differences and endpoint norms on several finite cycles, compares finite diffusive-window values with the theta-series constant, tests strict concavity of the limiting profile at selected points, and independently reproduces the exact Hilbert spectral optimizer. Its assertions are finite consistency checks, **not** replacements for steps 2–7 of the proof. The limits and global uniqueness follow from the analytical estimates above. The infinite series used in the defining equations converges exponentially at every positive argument.

## Relationship to prior work

The group-convolution representation and continuous-time Poissonization are standard; Saloff-Coste's survey *Random Walks on Finite Groups*, section 2.2 (equation (2.10)), states the continuous-time convolution formula explicitly. Gerencsér's *Mixing times of Markov chains on a cycle with additional long range connections* (arXiv:1401.1692, first posted 2014-01-08) studies reversible and nonreversible cyclic walks and their mixing-time bounds, rather than endpoint time-derivative norms or their exact asymptotic constants. Xu's *\(H^\infty\) functional calculus and maximal inequalities for semigroups of contractions on vector-valued \(L_p\)-spaces* (arXiv:1402.2344, first posted 2014-02-11) treats vector-valued maximal inequalities and functional calculus for \(1<p<\infty\); it does not give an endpoint norm for the oriented cyclic shift, a theta-function sharp coefficient, or maximizer localization. The present contribution is the quantitative **endpoint growth coefficient and unique diffusive optimizing scale** for this concrete nonreversible positive semigroup, not Poissonization or the Fourier formula alone.

## Limitations

The theorem establishes a leading limit and convergence of maximizing times, **not** an error rate in \(n\), an all-dimension exact optimization formula, or a claim for arbitrary nonreversible chains. The numerical decimal digits are evaluations of an analytically defined constant, not independent certified enclosures. A logically equivalent earlier result might be presented in wrapped-Poisson total variation or cyclic Markov-semigroup terminology; a complete historical-priority certification has not been performed.

## References

1. Laurent Saloff-Coste, *Random Walks on Finite Groups*, especially §2.2 and (2.10), accessible manuscript: https://pi.math.cornell.edu/~lsc/papers/chap5.pdf .
2. Balázs Gerencsér, *Mixing times of Markov chains on a cycle with additional long range connections*, arXiv:1401.1692 (initial public submission 2014-01-08), https://arxiv.org/abs/1401.1692 .
3. Quanhua Xu, *\(H^\infty\) functional calculus and maximal inequalities for semigroups of contractions on vector-valued \(L_p\)-spaces*, arXiv:1402.2344 (initial public submission 2014-02-11), https://arxiv.org/abs/1402.2344 .
4. Jacobi's triple-product formula for the periodic Gaussian/theta function; the specific product identity required here is displayed in step 5.
