# The one-switch and saturation geometry of nested uniform-spacing exceedance counts

## Finding

Let \(m\ge2\) and let \((X_1,\ldots,X_m)\) be uniformly distributed on the probability simplex (equivalently, the \(m\) gaps produced by \(m-1\) independent uniform points in \([0,1]\)). Write \(N_m(u)=\sum_{i=1}^m\mathbf1\{X_i>u\}\). For all \(0<s\le t<1\), the covariance is

\[
\operatorname{Cov}(N_m(s),N_m(t))
=m(1-t)^{m-1} B_m(s,t),\qquad
B_m(s,t)=1-m(1-s)^{m-1}+(m-1)
\left(\frac{(1-s-t)_+}{1-t}\right)^{m-1}.
\]

Here \(x_+=\max(x,0)\). The **complete sign classification** is:

1. If \(m=2\) and \(t=1/2\), this covariance is zero for every \(0<s\le t\), because \(N_2(1/2)=1\) almost surely.
2. Otherwise, if \(0<t\le 1/m\), the covariance is strictly positive at every \(0<s\le t\).
3. For every \(t>1/m\), there exists exactly one \(s_m(t)\in(0,t)\), with negative covariance for \(0<s<s_m(t)\), zero covariance at \(s=s_m(t)\), and positive covariance for \(s_m(t)<s\le t\).

Define \(t_m^\star=m^{-1/(m-1)}\) and \(s_m^\star=1-t_m^\star\). For \(m\ge3\), the zero curve \(s_m(t)\) is strictly increasing for \(1/m<t<t_m^\star\), and is exactly constant,

\[
s_m(t)=s_m^\star \qquad(t_m^\star\le t<1).
\]

For \(m=2\), the zero curve is already constant: \(s_2(t)=1/2\) for all \(t>1/2\). For fixed \(a>1\), the fine-scale transition obeys

\[
\lim_{m\to\infty} m s_m(a/m)=b(a),
\qquad e^{b(a)}=1+a b(a),\quad 0<b(a)<a,
\]

where \(b(a)\) is the unique strictly positive solution. In particular, two counts built from nested threshold events can have strictly negative covariance: \(\operatorname{Cov}(N_3(1/5),N_3(1/2))=-3/20\); the corresponding zero occurs at the exact lower threshold \(s_3(1/2)=2/5\).

## Assumptions and scope

All spacings are **positive**, exchangeable, and sum exactly to one, with joint Dirichlet distribution \(\operatorname{Dirichlet}(1,\ldots,1)\). The result is finite-sample and exact for each integer \(m\ge2\), with both thresholds strictly between zero and one and \(s\le t\). The probability of equality with a nontrivial threshold is zero. The limiting assertion fixes \(a>1\) as \(m\to\infty\), with \(m>a\). No corresponding claim is made for general Dirichlet parameters, dependent nonequiprobable breakpoints, or nonuniform underlying sampling.

## Proof

**1. Exact covariance.** Translation of the uniform-simplex density gives, for distinct indices \(i\ne j\),

\[
\Pr(X_i>u)=(1-u)^{m-1},\qquad
\Pr(X_i>s,X_j>t)=(1-s-t)_+^{m-1}.
\]

Since \(s\le t\), the same-index joint event is \(\{X_i>t\}\). Expanding \(\mathbb E[N_m(s)N_m(t)]-\mathbb E[N_m(s)]\mathbb E[N_m(t)]\) into the \(m\) diagonal and \(m(m-1)\) off-diagonal pairs proves the boxed covariance identity above, with no independence assumption on the gaps.

**2. Shape of the zero set.** For fixed \(t\), let \(B(s)=B_m(s,t)\), extended continuously to \(s=0\). Then \(B(0)=0\). On \(0<s<\min(t,1-t)\), direct differentiation gives

\[
B'(s)=(m-1)(1-s)^{m-2}\left[m-\frac{m-1}{1-t}
\left(\frac{1-s-t}{(1-t)(1-s)}\right)^{m-2}\right].
\]

For \(m\ge3\) the ratio inside the inner power decreases strictly with \(s\); for \(m=2\) it is identically one wherever defined. Once \(s+t\ge1\), \(B'(s)=m(m-1)(1-s)^{m-2}>0\). Thus \(B\) is nondecreasing throughout if \(t\le1/m\); when \(m\ge3\), the derivative is strictly positive on \(s>0\) even at \(t=1/m\). If \(t>1/m\), then

\[
B'(0)=\frac{(m-1)(1-mt)}{1-t}<0,
\]

and the derivative changes sign at most once, from negative to positive. The endpoint is positive because \(B(t)=\operatorname{Var}(N_m(t))/[m(1-t)^{m-1}]>0\) whenever \(N_m(t)\) is nonconstant. The sole exceptional deterministic case is \(m=2,t=1/2\), when the two spacings sum to one and exactly one exceeds one-half almost surely. For this case \(B(s)=0\) on the entire allowed interval. For \(m=2,t<1/2\), direct substitution gives \(B(s)=s(1-2t)/(1-t)>0\). These observations prove strict positivity for all other \(t\le1/m\), and existence and uniqueness of the negative-to-positive crossing for every \(t>1/m\).

**3. Exact plateau and strict pre-plateau increase.** Put \(t_m^\star=m^{-1/(m-1)}\) and \(s_m^\star=1-t_m^\star\), for which \(0<s_m^\star\le t_m^\star\). Whenever \(t\ge t_m^\star\), one has \(s_m^\star+t\ge1\), and therefore \(B_m(s_m^\star,t)=1-m(1-s_m^\star)^{m-1}=0\). Uniqueness identifies the root. For \(1/m<t<t_m^\star\) and \(m\ge3\), the root lies strictly in \(s+t<1\): if the cutoff \(1-t\) lies in the allowed interval, \(B_m(1-t,t)=1-mt^{m-1}>0\), whereas \(B_m\) is initially negative. At such a root \(\partial_sB_m>0\), while

\[
\partial_tB_m(s,t)
=-(m-1)^2\frac{s}{(1-t)^2}
\left(\frac{1-s-t}{1-t}\right)^{m-2}<0.
\]

Implicit differentiation yields \(s_m'(t)=-\partial_tB_m/\partial_sB_m>0\). For \(m=2\), the increasing interval is empty and the plateau begins immediately beyond one-half.

**4. Microscopic transition.** Fix positive \(a\) and \(b\le a\). Substituting \(t=a/m\), \(s=b/m\) into the exact formula and expanding logarithms gives

\[
\frac1m\operatorname{Cov}\bigl(N_m(b/m),N_m(a/m)\bigr)
\longrightarrow e^{-a}\{1-(1+ab)e^{-b}\}.
\]

For \(a>1\), the function \(e^b-1-ab\) starts with negative derivative at zero, is strictly convex, and is positive at \(b=a\) (because \(e^a>1+a^2\) for \(a\ge1\)). Hence there is exactly one positive zero \(b(a)\in(0,a)\). Uniform convergence of the displayed finite formulas on each compact positive \(b\)-interval, together with the unique finite-sample crossing, traps \(m s_m(a/m)\) between any two points on opposite sides of \(b(a)\). This proves convergence. The inequality \(e^a>1+a^2\) follows by differentiation on \(a\ge1\): \(e^1>2\), and the derivative \(e^a-2a\) is positive there.

## Verification

A standalone standard-library checker, `verify_nested_spacings.py`, tests the independent diagonal/off-diagonal covariance expansion against the compact bracket identity using exact rational arithmetic for \(20{,}800\) finite parameter triples with \(2\le m\le14\); it checks the mean-threshold and deterministic two-spacing exceptions, plateau signs, and convergence of the large-size covariance kernel. Run `python3 verify_nested_spacings.py` from the package directory. All programmed checks passed on the packaged script. Numerical experiments do not prove uniqueness, the derivative assertions, or convergence; those are established analytically above.

## Relationship to prior work

Uniform-spacing and normalized-exponential representations are classical. Weiss (1962) gives a central limit theorem for linear spacing statistics, while Shorack and Wellner (1986, Chapter 21) organize finite-sample and asymptotic uniform-spacing empirical-process theory; their accessible chapter excerpt confirms that scope but not the full results of the chapter. Pyke (1965) surveys general spacing distributions, and Holst (1980) studies random-stick pieces and related length questions. The elementary two-coordinate simplex-tail formula is not claimed as new. The contribution assessed here is the complete **finite-sample covariance sign geometry** for nested exceedance-count levels: the exact mean-spacing boundary, the exceptional deterministic case, uniqueness of the zero contour, its monotone-to-constant transition, and the scaled-root limit. An earlier equivalent statement might still be present in the uninspected portions of the comprehensive spacing literature.

## Limitations

The theorem applies specifically to symmetric Dirichlet spacings and ordered thresholds. Its originality assessment is literature-dependent, not a proof of historical priority: relevant classic survey/book full texts could not all be inspected. The asymptotic covariance kernel is consistent with classical spacing empirical-process theory and is not independently claimed as a new kernel. No independent scientific audit or independent proof certification is asserted.

## References

- L. Weiss, “On the Distribution of Linear Functions of Spacings from a Uniform Distribution,” *Mathematica Scandinavica* 11 (1962), 149–150, DOI 10.7146/math.scand.a-10660. Full two-page text inspected.
- G. R. Shorack and J. A. Wellner, *Empirical Processes with Applications to Statistics*, Wiley, 1986, Chapter 21, “Spacings,” pp. 720–742. ISBN 047186725X; accessible SIAM edition DOI 10.1137/1.9780898719017.ch21. Only the chapter excerpt was accessible.
- R. Pyke, “Spacings,” *Journal of the Royal Statistical Society, Series B* 27 (1965), 395–436, DOI 10.1111/j.2517-6161.1965.tb00602.x. Abstract and publication metadata inspected.
- L. Holst, “On the lengths of the pieces of a stick broken at random,” *Journal of Applied Probability* 17 (1980), 623–634, DOI 10.2307/3212970. Abstract and metadata inspected.
