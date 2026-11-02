# Sharp covariance extremizers for coupled finite-field polynomial value sets

## Finding

For a uniformly random polynomial function and any fixed additive polynomial perturbation, the covariance of their value-set sizes is determined exactly by the **fiber profile of the perturbation**. The covariance is strictly Schur-convex in that profile. Every permutation polynomial gives the same strictly negative minimum, while every constant perturbation gives the same strictly positive maximum. The closest non-extremal profiles and their exact gaps are also classified.

Write \(V(g)=\#\{g(x):x\in\mathbb F_q\}\). Put \(a=(q-1)/q\) and \(b=(q-2)/q\), and let \(r_c=\#\{x:h(x)=c\}\). Then

\[
\operatorname{Cov}(V(f),V(f+h))
=q\sum_{c\in\mathbb F_q}a^{r_c}b^{q-r_c}-q^2a^{2q}.
\]

In particular, the sharp lower and upper bounds are

\[
C_{\min}=q^2ab^{q-1}-q^2a^{2q}<0,
\qquad
C_{\max}=qa^q+q(q-1)b^q-q^2a^{2q}>0.
\]

Equality in the lower bound holds **exactly when** \(h\) permutes \(\mathbb F_q\); equality in the upper bound holds **exactly when** \(h\) is constant as a function on \(\mathbb F_q\).

For \(q\ge3\), the smallest covariance among nonpermutation perturbations is \(C_{\min}+b^{q-2}/q\), achieved precisely at fiber profiles with one fiber of size two, one empty fiber, and all remaining fibers singletons. The largest covariance among nonconstant perturbations is \(C_{\max}-(a^{q-1}-b^{q-1})\), achieved precisely at fiber profiles with two occupied fibers of sizes \(q-1\) and \(1\).

## Assumptions and scope

Let \(q\ge2\) be any prime power. Let \(f\) be uniform on the set of polynomials \(\mathbb F_q[X]\) of degree at most \(q-1\); let \(h\) be a fixed polynomial in \(\mathbb F_q[X]\) of arbitrary degree. All random variables and covariances concern the common random \(f\); the polynomial \(h\) is not random. Polynomial functions are evaluated at the \(q\) elements of \(\mathbb F_q\). By Lagrange interpolation, evaluation is a bijection from polynomials of degree less than \(q\) onto all maps \(\mathbb F_q\to\mathbb F_q\). Consequently the values \(f(x)\) are independent and uniformly distributed.

Define \(r_c=\#h^{-1}(c)\), so \(r_c\ge0\) and \(\sum_c r_c=q\). The convention \(0^0=1\) is used when \(q=2\). The profiles in the extremal statements are multisets of \(q\) fiber sizes, including zero fibers. A permutation polynomial means a polynomial inducing a bijection of \(\mathbb F_q\); a constant perturbation means a constant polynomial *function*, even if its written representative has larger degree.

## Proof

**Joint exclusion probability.** For each \(u\in\mathbb F_q\), let \(I_u\) indicate that \(u\notin f(\mathbb F_q)\); for each \(v\in\mathbb F_q\), let \(J_v\) indicate that \(v\notin(f+h)(\mathbb F_q)\). At a point \(x\), the simultaneous requirements are \(f(x)\ne u\) and \(f(x)\ne v-h(x)\). The two forbidden values coincide exactly if \(h(x)=v-u\), in which case their joint exclusion probability is \(a\); otherwise the two values differ and it is \(b\). Independence across inputs gives

\[
\mathbb E[I_uJ_v]=a^{r_{v-u}}b^{q-r_{v-u}},
\qquad \mathbb E[I_u]=\mathbb E[J_v]=a^q.
\]

Write \(M_f=\sum_u I_u=q-V(f)\) and \(M_{f+h}=\sum_v J_v=q-V(f+h)\). There are exactly \(q\) pairs \((u,v)\) for every fixed difference \(v-u=c\). Expanding the covariance of these missing-value counts therefore gives the displayed identity.

**Strict convexity and sharp extremizers.** For integer \(t\in\{0,\ldots,q\}\), set \(\Phi(t)=a^t b^{q-t}\). If \(q\ge3\), then \(b>0\), and

\[
\Phi(t+2)-2\Phi(t+1)+\Phi(t)
=(a-b)^2a^t b^{q-t-2}>0
\qquad(0\le t\le q-2).
\]

For \(q=2\), its values are \(\Phi(0)=\Phi(1)=0\), \(\Phi(2)=1/4\), again strictly convex. Thus a balancing move from a fiber of size at least two more than another fiber strictly decreases \(\sum_c\Phi(r_c)\); the reverse transfer strictly increases it. With \(q\) nonnegative integer entries summing to \(q\), the unique minimum profile is \((1,\ldots,1)\), and the unique maximum profile is \((q,0,\ldots,0)\). Every profile is realizable by a finite-field polynomial function via interpolation. Substitution yields \(C_{\min}\) and \(C_{\max}\). This proves strict Schur-convexity on profiles, including all equality classifications.

The maximum is the variance of \(V(f)\), because a constant \(h\) only translates the value set. This variance is strictly positive: both constant and bijective maps \(f\) occur with positive probability. To see strict negativity of the minimum for \(q\ge3\), put \(z=q-1\ge2\). Then

\[
\frac{ab^{q-1}}{a^{2q}}=
\left(1-z^{-2}\right)^z\left(1+z^{-1}\right)<1,
\]

because the natural logarithm of the right-hand side is less than \(-1/z+1/z=0\). For \(q=2\), direct substitution gives \(C_{\min}=-1/4\).

**Sharp gaps from the extremizers.** Every nonpermutation fiber profile majorizes the profile \((2,1,\ldots,1,0)\). By strict convexity the smallest nonminimal covariance occurs precisely at that profile, with gap

\[
q\bigl(\Phi(2)+\Phi(0)-2\Phi(1)\bigr)
=q(a-b)^2b^{q-2}=\frac{b^{q-2}}q.
\]

Likewise, the profile \((q-1,1,0,\ldots,0)\) majorizes every other nonconstant fiber profile. It is therefore the unique second-maximum profile, and the drop from the maximum equals

\[
q\bigl(\Phi(q)+\Phi(0)-\Phi(q-1)-\Phi(1)\bigr)
=q(a-b)(a^{q-1}-b^{q-1})=a^{q-1}-b^{q-1}.
\]

The two second-extremal statements are restricted to \(q\ge3\); no intermediate fiber profile exists when \(q=2\).

## Verification

The accompanying \(\texttt{verify.py}\) reconstructs all polynomial functions as evaluation vectors and computes covariances independently by direct enumeration. It uses exact rational arithmetic and checks the formula, signs, equality characterizations, and second-extremal gaps. It exhaustively tests all perturbations for fields of orders \(2,3,4\), and representative profiles over the prime field of order \(5\). The order-four field uses bitwise exclusive-or as addition in its additive group. Reproduce with \(\texttt{python3 verify.py}\); no external Python packages are needed.

Direct enumeration checks finite fields only, while the algebraic argument proves the statement for **every prime power**. In particular, finite enumeration is not used as an infinite proof or an exhaustive historical-priority test.

## Relationship to prior work

Mullen, Wan and Wang study deterministic polynomial value-set cardinalities over finite fields, including restrictions for nonpermutation maps [1]. Gao and Wang establish the exact **marginal** distribution of the value-set size of one uniformly random degree-less-than-\(q\) polynomial and its limiting normal behavior [2]. These are the principal motivations: the joint distribution of the value-set sizes of \(f\) and its *shared-sample perturbation* \(f+h\) is not determined by two marginal laws. The present statement derives their covariance for every perturbation and proves the sharp fiber-profile extremizers, including first nontrivial gaps.

The related literature on intersections of value sets with affine lines for fixed low-degree polynomials [3] concerns different objects and does not imply this all-degree coupled random-polynomial covariance. Standard independent-occupancy identities can recover the constant-perturbation variance, but do not by themselves classify the joint dependence for arbitrary prescribed differences \(h(x)\).

The proofs rely on elementary exclusion and discrete convexity; these techniques are not claimed to be new. Unlocated work on correlated occupancy or joint random-function images might contain equivalent formulations.

## Limitations

The conclusion requires the unrestricted uniform distribution over all polynomial functions, not a random low-degree subfamily or independently sampled \(f\) and \(f+h\). It quantifies covariance, not the entire bivariate distribution. A fixed perturbation can have arbitrary degree, but only its induced finite-field function matters. Historical priority remains subject to an independent specialist literature review; independent mathematical auditing has not been performed.

## References

1. G. L. Mullen, D. Wan and Q. Wang, *Value Sets of Polynomial Maps over Finite Fields*, Quarterly Journal of Mathematics 64 (2013), 1191–1196, DOI 10.1093/qmath/has026; preprint arXiv:1210.8119 (first arXiv version 2012-10-30).
2. Z. Gao and Q. Wang, *A Probabilistic Approach to Value Sets of Polynomials over Finite Fields*, Finite Fields and Their Applications 33 (2015), 160–174, DOI 10.1016/j.ffa.2014.12.003; preprint arXiv:1407.5884 (2014-07-22).
3. G. M. Kyureghyan, M. Li and A. Pott, *On the Intersection Distribution of Degree Three Polynomials and Related Topics*, 2021, DOI 10.37236/9456.
