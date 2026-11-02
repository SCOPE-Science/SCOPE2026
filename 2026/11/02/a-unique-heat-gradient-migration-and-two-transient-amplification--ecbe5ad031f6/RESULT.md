# A unique heat-gradient migration and two transient amplification peaks on a weighted four-vertex path

## Finding

Consider a path with four vertices, unit edge lengths and positive heat conductances \(a,b,c\). On the open parameter cone
\[
 b>2a>0,\qquad c>3(b-a),
\]
the sharp graph-Lipschitz norm of its heat semigroup first selects the **middle edge**, then at a unique positive time selects the **left edge** forever. For the explicit conductances \((a,b,c)=(1,3,9)\), this sharp norm has **two strict local maxima separated by a strict cusp local minimum**. The cusp time lies in the rigorously certified rational interval \((5285/100000,5286/100000)\). The four-vertex path is the smallest positively weighted path on which the maximizing edge can migrate at positive time.

For every \(t\geq0\), put
\[
 B=\begin{pmatrix}-2a&b&0\\a&-2b&c\\0&b&-2c\end{pmatrix},\qquad
 u(t)=e^{tB}(1,1,1)^{\mathsf T}.
\]
There is exactly one \(t_*>0\) satisfying \(u_1(t_*)=u_2(t_*)\), and the exact, attained sharp norm is
\[
 \Lambda(t)=\begin{cases}u_2(t),&0\le t\le t_*,\\u_1(t),&t_*\le t<\infty.\end{cases}
\]
Moreover \(u_1(t)>u_3(t)\) for every \(t>0\); for every \(t>0\), all nonconstant real extremizers, modulo constants and nonzero scalar multiplication, are the affine vertex ramps \(f(v_j)=j\). In the specific example \((1,3,9)\), there are unique \(0<\tau_2<t_*<\tau_1\) such that \(\Lambda\) increases on \((0,\tau_2)\), decreases on \((\tau_2,t_*)\), increases on \((t_*,\tau_1)\), and decreases on \((\tau_1,\infty)\). These are exactly its two smooth strict local maxima and its strict cusp minimum, respectively. Numerical orientation only (not certification): \(\tau_2\approx0.03761756\), \(t_*\approx0.05285503\), \(\tau_1\approx0.20639384\); the maxima have norm approximately \(1.06453\) and \(1.13885\), respectively.

## Assumptions and scope

Vertices are \(v_0,v_1,v_2,v_3\) in their natural path order. Each graph-metric edge has length one regardless of its heat conductance. The positive symmetric generator is \(L_cf(v)=\sum_{w\sim v}c_{vw}(f(v)-f(w))\), with conductances \((a,b,c)\), and \(H_t=e^{-tL_c}\) on real-valued functions. The graph-Lipschitz seminorm is \(\operatorname{Lip}(f)=\max_{j=1,2,3}|f(v_j)-f(v_{j-1})|\). The operator norm is taken on functions modulo constants. All assertions about the open cone hold simultaneously for every positive parameter triple satisfying its inequalities and all indicated times. Nonzero extremizer means nonconstant function with positive Lipschitz seminorm.

## Proof

**1. Exact gradient intertwining and equality cases.** Let \((Df)_j=f(v_j)-f(v_{j-1})\). Direct expansion with \(Q=-L_c\) gives \(DQ=BD\). Exponentiating yields \(D H_t=e^{tB}D\). The tridiagonal \(B\) has nonnegative off-diagonals and is irreducible; thus \(e^{tB}\) is entrywise strictly positive for every \(t>0\). It follows, with \({\bf1}=(1,1,1)^{\mathsf T}\), that
\[
 \sup_{\operatorname{Lip}(f)\le1}\operatorname{Lip}(H_tf)
 =\|e^{tB}\|_{\infty\to\infty}=\max_j(e^{tB}{\bf1})_j.
\]
Equality is attained by ramps with every \((Df)_j=1\). Because every entry is strictly positive, equality in any row's triangle inequality with \(\|Df\|_\infty=1\) forces all three gradient entries to have common sign and magnitude one. Consequently the ramps and their affine rescalings comprise all nonconstant extremizers for \(t>0\).

**2. Suppression of the right edge.** Set \(h=u_1-u_3\). The differential system \(u'=Bu\) gives \(h'=-2ah+2(c-a)u_3\), with \(h(0)=0\). Because \(c>3(b-a)>3a>a\) and \(u_3(t)>0\), integration gives \(h(t)>0\) for every \(t>0\).

**3. Exactly one positive maximizing-edge switch.** Put \(g=u_2-u_1\). The initial derivative is \(g'(0)=c-3(b-a)>0\). Conjugating \(B\) as \(SBS^{-1}\) with \(S=\operatorname{diag}(\sqrt a,\sqrt b,\sqrt c)\) gives a real symmetric Jacobi matrix whose diagonal is \((-2a,-2b,-2c)\) and off-diagonals are \((\sqrt{ab},\sqrt{bc})\). Its eigenvalues are distinct; its negative is positive definite because its leading principal minors are \(2a,3ab,4abc\), all strictly positive. Write the largest eigenvalue as \(\lambda_1\), so \(-2a<\lambda_1<0\), the first strict inequality following from strict Perron coupling. The corresponding eigenvector \(v>0\) obeys \(b v_2=(\lambda_1+2a)v_1\). The cone assumption \(b>2a\) forces \(v_1>v_2\), hence by strictly positive Perron coefficient in \(e^{tB}{\bf1}\), one has \(g(t)<0\) for all sufficiently large \(t\).

By diagonalizability, \(g(t)\) is a linear combination of three exponentials with distinct real exponents. The elementary exponential zero-count lemma says such a nonzero combination has at most two real zeros, counted with multiplicities. To prove the lemma, divide by the exponential of the smallest exponent, differentiate, apply Rolle's theorem with multiplicities, and use that a sum of two distinct real exponentials has at most one zero. Since \(g(0)=0\), \(g'(0)>0\), and \(g(t)<0\) eventually, there exists at least one positive zero. If it had two or a multiple root, this together with the zero at zero would exceed the bound. There is therefore exactly one simple positive zero \(t_*\), with \(g>0\) before and \(g<0\) after. Together with step 2, this yields the asserted all-time norm formula.

**4. Two peaks for \((1,3,9)\).** Here
\[
 B=\begin{pmatrix}-2&3&0\\1&-6&9\\0&3&-18\end{pmatrix},\qquad
 \det(zI-B)=z^3+26z^2+126z+108.
\]
An exact rational Taylor certificate described below places \(t_*\) in \((5285/100000,5286/100000)\) and establishes \(u_2'(t_*)<0\). In addition \(u_2'(0)=4>0\). Since \(u_2'\) is another three-real-exponential combination, it has at most two zeros on the full real line. It is negative for all sufficiently large times, because its dominant Perron coefficient is \(\lambda_1 v_2<0\). Therefore its sign changes once on \((0,t_*)\), at a unique simple \(\tau_2\), from positive to negative. On \((0,t_*]\), \(u_1'=(-2u_1+3u_2)>u_1>0\). At the switch, \(u_1'(t_*)=u_1(t_*)>0\), while \(u_2'(t_*)<0\). The same exponential-zero-count reasoning applied to \(u_1'\), whose sign is eventually negative, shows it changes sign exactly once after \(t_*\), at \(\tau_1\). Thus the piecewise-analytic sharp norm has precisely the stated two strict maxima separated by a strict cusp minimum. In particular \(\Lambda(0)=1\), \(\Lambda(t)>1\) for all \(0<t\le\tau_1\), and \(\Lambda(t)\to0\) as \(t\to\infty\).

**5. Minimality of four vertices for moving maximizers.** A weighted two-edge path has a two-by-two strictly Metzler gradient matrix \(B_2\). The difference between its two row-sum trajectories is a combination of two distinct real exponentials and vanishes at \(t=0\). A nonzero such difference has at most one real zero, so its sign cannot change at any positive time. The one-edge path has only one candidate edge. The four-vertex example consequently has the smallest vertex count possible for positive-time migration.

## Verification

Run `python verify_weighted_path.py` with Python 3 (only the standard library is required). The checker independently expands the intertwining identity on four rational test conductance triples and calculates the displayed characteristic polynomial. Most importantly, for \(t_-=5285/100000\), \(t_+=5286/100000\), it evaluates the rational polynomial \(S_{26}(t)=\sum_{k=0}^{26}(tB)^k{\bf1}/k!\) exactly. Since \(\|B\|_\infty=21\), \(t_+<53/1000\) and \(e^{6/5}<8\), each coordinate of the exponential remainder has absolute value bounded by
\[
 \varepsilon=8\frac{(6/5)^{27}}{27!}<10^{-20}.
\]
The code checks \(S_{26,2}(t_-)-S_{26,1}(t_-)>2\varepsilon\) and \(S_{26,2}(t_+)-S_{26,1}(t_+)<-2\varepsilon\). It also bounds \(u_2'(t_*)\) from above by the rational inequality
\[
 (B S_{26}(t_-))_2+21\varepsilon+21^2\cdot8\,(t_+-t_-)<0,
\]
using \(\|u''(t)\|_\infty\le21^2e^{21t}<21^2\cdot8\) throughout the interval. All tests are exact Fraction comparisons. The numerical peak locations in the Finding section merely illustrate the rigorously proved three-turning-point structure.

## Relationship to prior work

The general commutation/intertwining approach to birth-death heat processes and sharp Lipschitz operator norms appears in Chafaï and Joulin (2010), especially their general birth-death intertwining and Feynman–Kac treatment. It does not, in the inspected text, identify the present open parameter cone, unique switching edge, or double-peaked four-site sharp norm. Ollivier (2007) sets out the transport contraction framework, and Münch and Wojciechowski (2017) develop curvature/gradient equivalences for general graph Laplacians; neither inspected work computes the exact present switching and two-peak profile. Our contribution is the all-time optimizing-edge migration and, for concrete integer conductances, the *nonunimodal* sharp seminorm despite self-adjoint Markov heat flow. Related exact norm calculations on other finite graphs and total-variation contractions do not imply the weighted-path Lipschitz two-peak statement.

## Limitations

The branch-switch proof assumes the strict open cone \(b>2a>0\), \(c>3(b-a)\). The two-peak claim is established for conductances \((1,3,9)\), not for every triple in the cone. Conductances determine heat rates, not metric edge lengths. No analogous result for longer paths, nonlinear maximal operators, other function-space norms, or weighted metric distances is asserted. Numerical sample values are not proof; strict rational enclosures, the analytic sign arguments, and the exponential zero-count bound provide certification. Published coverage outside inspected accessible sources may remain unindexed.

## References

1. Y. Ollivier, *Ricci curvature of Markov chains on metric spaces*, arXiv:math/0701886 (first public 2007-01-30), https://arxiv.org/abs/math/0701886.
2. D. Chafaï and A. Joulin, *Intertwining and commutation relations for birth-death processes*, arXiv:1011.2331 (first public 2010-11-10), https://arxiv.org/abs/1011.2331.
3. F. Münch and R. K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: heat equation, Laplacian comparison, non-explosion*, arXiv:1712.00875 (first public 2017-12-04), https://arxiv.org/abs/1712.00875.
