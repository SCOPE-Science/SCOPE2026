# Sharp log-concavity and curvature phase diagram for symmetric three-normal mixtures

## Finding

Consider three normal components with common variance and symmetric locations: a central component and two equally weighted satellites. Their mixture has an **exact global upper bound on log-density curvature**, with a switch between the center and two off-center maximizers, and an **exact sharp log-concavity threshold** expressed using the principal Lambert function. In particular, log-concavity can fail even when the mixture has a unique mode.

For \(0<\theta<1\), \(a>0\), and \(\sigma>0\), let
\[
f(x)=\theta\varphi_\sigma(x)+\frac{1-\theta}{2}\{\varphi_\sigma(x-a)+\varphi_\sigma(x+a)\},\qquad x\in\mathbb R,
\]
where \(\varphi_\sigma\) is the centered normal density of variance \(\sigma^2\). Set
\[
r=\frac{1-\theta}{\theta},\qquad b=\frac{a^2}{\sigma^2},\qquad k=re^{-b/2},
\]
and define the continuous increasing function
\[
Q(k)=\begin{cases}\dfrac{1}{4(1-k^2)},&0<k\le\tfrac12,\\[3pt]\dfrac{k}{1+k},&k\ge\tfrac12.\end{cases}
\]
Then the **optimal global curvature constant** is
\[
\boxed{\sup_{x\in\mathbb R}(\log f)''(x)=\frac{bQ(k)-1}{\sigma^2}.}
\]
For \(k\ge\tfrac12\) the supremum is attained at \(x=0\). For \(0<k<\tfrac12\), it is attained precisely at the two nonzero points
\[
x=\pm\frac{\sigma^2}{a}\operatorname{arcosh}\!\left(\frac{1-2k^2}{k}\right).
\]
Consequently \(f\) is log-concave precisely when \(bQ(re^{-b/2})\le1\), and strongly log-concave precisely when the inequality is strict. The largest strong-log-concavity modulus is \((1-bQ(k))/\sigma^2\) whenever positive.

More explicitly, put \(r_*=e^{3/2}/2\) and let \(W_0\) denote the principal real branch of the Lambert \(W\) function, satisfying \(W_0(z)e^{W_0(z)}=z\). There is a **unique** sharp transition \(B(r)\) given by
\[
\boxed{
B(r)=\begin{cases}
4+W_0(-4r^2e^{-4}),&0<r\le r_*,\\[3pt]
1-2W_0\!\left(-\dfrac{e^{1/2}}{2r}\right),&r\ge r_*.
\end{cases}}
\]
The branches agree at \(r=r_*\), where \(B(r_*)=3\). In all cases
\[
\boxed{f\text{ is log-concave}\ \Longleftrightarrow\ b\le B(r).}
\]
The function \(B(r)\) decreases strictly from \(4\) to \(1\) as \(r\) increases from zero to infinity. For equal mixture weights, \(r=2\), the threshold is \(B(2)=3.532109317947512\ldots\); for weights \((1/4,1/2,1/4)\), the threshold is \(B(1)=3.920690394872886\ldots\).

The latter weight profile provides a transparent separation between shape notions: for \(r=1\), \(b=4\), the mixture has exactly one strict mode, at zero, yet is **not** log-concave; its maximal log curvature equals \(\{(1-e^{-4})^{-1}-1\}/\sigma^2>0\).

## Assumptions and scope

The mixture has exactly three positive component weights, two symmetric satellite means and one central mean, and a shared strictly positive variance. No limiting, asymptotic, large-separation, or genericity assumption is imposed. All curvature claims are pointwise on the entire real line. The Lambert formulas use the principal real branch, which is well-defined for the displayed parameter ranges. The endpoints \(\theta=0,1\) are excluded from the phase diagram and may be treated separately by direct limiting arguments.

The formulas extend without changing \(B(r)\) to a \(d\)-dimensional spherical-covariance mixture, \(d\ge1\), with means \(-av,0,av\) for a fixed unit vector \(v\). The log Hessian equals \(-I_d/\sigma^2\) in directions orthogonal to \(v\); its largest eigenvalue is the one-dimensional curvature stated above. Thus the same threshold and optimal strong-concavity modulus hold in every finite dimension. General asymmetric weights, noncollinear means, and unequal covariances are outside this result.

## Proof

**1. Exact reduction to one scalar.** Gaussian completion of the square gives
\[
f(x)=\theta\varphi_\sigma(x)\{1+k\cosh z\},\qquad z=\frac{ax}{\sigma^2},\quad k=re^{-b/2}.
\]
Put \(u=k\cosh z\). Then \(u\in[k,\infty)\), and differentiation yields
\[
\sigma^2(\log f)''(x)=-1+b\frac{u+k^2}{(1+u)^2}.
\]
Indeed, the second derivative of \(\log(1+k\cosh z)\) is \((k\cosh z+k^2)/(1+k\cosh z)^2\). This identity is valid for every \(x\) and all admitted parameters, including at the branch transition.

**2. Global optimization and location of maximum curvature.** For \(F_k(u)=(u+k^2)/(1+u)^2\),
\[
F_k'(u)=\frac{1-u-2k^2}{(1+u)^3}.
\]
If \(k\ge1/2\), the critical point \(1-2k^2\) lies at or below the admissible left endpoint \(u=k\); hence \(F_k\) strictly decreases for \(u>k\), and its maximum is \(F_k(k)=k/(1+k)\). If \(0<k<1/2\), the single maximizer is \(u=1-2k^2>k\), and substitution gives \(F_k(u)=1/[4(1-k^2)]\). Because \(\cosh z=1\) exactly at zero and is strictly increasing for \(z>0\), this proves the stated maximizing locations, including uniqueness up to reflection. The pieces agree at \(k=1/2\), since both equal \(1/3\).

**3. Exact log-concavity boundary and absence of re-entry.** The curvature identity proves that log-concavity is equivalent to \(bQ(re^{-b/2})\le1\). As \(b\downarrow0\), the left-hand side tends to zero. At \(b=4\), it is strictly greater than one because \(Q(k)>1/4\) for all \(k>0\). To identify all possible roots of \(bQ(re^{-b/2})=1\), distinguish the optimizer branches:

* On \(k\ge1/2\), equality gives \(b=1+1/k\), so \(1<b\le3\), and
  \[
  r=\frac{e^{b/2}}{b-1}.
  \]
  This right-hand side decreases strictly from infinity to \(r_*=e^{3/2}/2\) as \(b\) increases from \(1\) to \(3\), because its logarithmic derivative is \((b-3)/[2(b-1)]<0\) before \(3\). Writing \(w=(1-b)/2\) gives \(we^w=-e^{1/2}/(2r)\), with \(-1\le w<0\), and therefore \(b=1-2W_0(-e^{1/2}/(2r))\).

* On \(0<k\le1/2\), equality gives \(b=4(1-k^2)\), so \(3\le b<4\), and
  \[
  r=e^{b/2}\sqrt{1-b/4}.
  \]
  Its logarithmic derivative is \((3-b)/[2(4-b)]<0\) for \(b>3\), so it decreases strictly from \(r_*\) to zero. Writing \(w=b-4\) yields \(we^w=-4r^2e^{-4}\), with \(-1\le w<0\); hence \(b=4+W_0(-4r^2e^{-4})\).

Each fixed \(r>0\) therefore has **exactly one** root \(B(r)\). Continuity, the strict inequality near zero, and the strict reverse inequality at \(4\) establish that \(bQ(re^{-b/2})<1\) below the root and is \(>1\) above it. The displayed root functions also show strict decrease of \(B\), with limits \(4\) and \(1\). At equality the log-density has zero second derivative somewhere, so it is log-concave but not strongly log-concave with a positive modulus. In the strict region its sharp positive modulus follows from Step 2.

**4. A unimodal but non-log-concave member.** Choose \(r=1\), \(b=4\). The maximum-curvature formula is positive because \(k=e^{-2}<1/2\) and
\[
 bQ(k)=\frac1{1-e^{-4}}>1.
\]
To establish unimodality independently rather than infer it from curvature, differentiate the factorized log density with respect to \(z>0\):
\[
\frac{d}{dz}\log f\!\left(\frac{\sigma^2z}{a}\right)
=-\frac z4+\frac{e^{-2}\sinh z}{1+e^{-2}\cosh z}.
\]
It is negative exactly when \(e^{-2}h(z)<1\), where \(h(z)=4\sinh z/z-\cosh z\). The everywhere-convergent Maclaurin series is
\[
h(z)=3+\frac{z^2}{6}-\frac{z^4}{120}
+\sum_{j=3}^{\infty}\frac{4/(2j+1)-1}{(2j)!}\,z^{2j}.
\]
Every coefficient in this tail is negative, so for all \(z>0\),
\[
h(z)\le3+\frac{z^2}{6}-\frac{z^4}{120}\le\frac{23}{6}<e^2.
\]
The quadratic bound reaches its maximum at \(z^2=10\). Thus \(f'(x)<0\) for all \(x>0\). Symmetry gives \(f'(x)>0\) for all \(x<0\), and zero is the unique strict mode.

**5. Higher-dimensional extension.** Write each \(x\in\mathbb R^d\) as \(x=sv+y\) with \(y\perp v\). The density factors into the one-dimensional mixture in \(s\) and the \((d-1)\)-dimensional centered Gaussian density in \(y\). The log Hessian is block diagonal with one eigenvalue \((\log f_1)''(s)\) and \(d-1\) copies of \(-1/\sigma^2\). Since \(bQ(k)>0\), its largest global eigenvalue equals the one-dimensional maximum. This proves the dimensional claim.

## Verification

The accompanying standalone `verification.py` evaluates the critical derivative and branch formulas symbolically with SymPy, verifies both principal Lambert-branch equations with high-precision arithmetic, checks branch location and strict neighboring regimes over a range of weight ratios, and numerically checks attainment of the analytic curvature maximum. It also checks the strictly positive curvature and decreasing-density inequalities for the one-mode counterexample. Executed with Python, SymPy, and mpmath, it produced `verification_output.txt` reporting **283 passed assertions**. The symbolic checks are exact; the numerical cases sample finite parameters. The analytical proof above, not the computational tests, establishes the global and all-dimensional claims.

## Relationship to prior work

Okahara and Kobayashi, *Three Homoscedastic Gaussian Components Have at Most Four Modes* (arXiv:2610.15369v1; publicly posted October 11, 2026), prove the maximum number of density modes is four in arbitrary dimension and three for collinear component means. The present result does **not** claim a new modal-count upper bound. Instead it computes a global log-density curvature, the exact two-parameter log-concavity region, its optimizer bifurcation, and a one-mode non-log-concave example. Their free-energy and mode-count theorem, including its curvature appendix concerning branch derivatives, does not state this phase diagram.

Okuno and Kabata, *On Mixtures of Three Homoscedastic Gaussian Densities: An Unconditional Sharper Bound on the Number of Modes* (arXiv:2607.17506v1), establish an earlier unconditional eight-mode bound. Ray and Lindsay, *The topography of multivariate normal mixtures* (Annals of Statistics 33, 2005; arXiv:math/0602238), give a Gaussian-mixture ridgeline framework and modal-curvature analysis. These general frameworks explain why derivatives and conditional component moments are natural tools; the posterior-variance identity alone is not claimed new. Neither compared result gives the explicit sharp Lambert phase boundary above.

## Limitations

This is an exact analytic classification for a **symmetric, three-component, common-variance** subfamily only. It does not classify the modal phase diagram of arbitrary three-normal mixtures or the log-concavity region for asymmetric weights, irregular means, or unequal variances. The monotonicity of the sharp boundary refers to the satellite-to-center weight ratio, not to the maximum-curvature expression as a function of separation at all parameter values. The numerical checker supplies corroborating finite evaluations and cannot certify infinite quantifiers. Historical priority is qualified: a more general, not-yet-identified Gaussian-mixture log-concavity theorem could imply parts of the result; independent expert assessment has not been performed.

## References

1. R. Okahara and K. Kobayashi, *Three Homoscedastic Gaussian Components Have at Most Four Modes*, arXiv:2610.15369v1, October 11, 2026. https://arxiv.org/html/2610.15369v1
2. A. Okuno and Y. Kabata, *On Mixtures of Three Homoscedastic Gaussian Densities: An Unconditional Sharper Bound on the Number of Modes*, arXiv:2607.17506v1, July 20, 2026. https://arxiv.org/abs/2607.17506
3. S. Ray and B. G. Lindsay, *The topography of multivariate normal mixtures*, *Annals of Statistics* 33 (2005), arXiv:math/0602238. https://arxiv.org/abs/math/0602238
