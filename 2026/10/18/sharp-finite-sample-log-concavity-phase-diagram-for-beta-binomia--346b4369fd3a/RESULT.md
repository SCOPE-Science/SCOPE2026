# Sharp finite-sample log-concavity phase diagram for beta-binomial counts

## Finding

For \(n\ge2\) an integer, let \(X\) have the beta-binomial law
\[
 p_k=\Pr(X=k)=\binom nk\frac{B(k+\alpha,n-k+\beta)}{B(\alpha,\beta)},\qquad 0\le k\le n,
\]
where \(\alpha,\beta>0\), and \(B\) is Euler's beta function. Write \(LC\) for the property \(p_k^2\ge p_{k-1}p_{k+1}\) at each \(1\le k\le n-1\).

**Theorem (complete finite-sample classification).** The law has \(LC\) if and only if exactly one of the following parameter conditions holds:

1. \(\alpha\ge1\) and \(\beta\ge1\).
2. \(\alpha>1\), \(\dfrac{n-1}{n+1}<\beta<1\), and
\[
\alpha-1\ge\frac{n(n-1)(1-\beta)}{2-(n+1)(1-\beta)}.
\]
3. \(\beta>1\), \(\dfrac{n-1}{n+1}<\alpha<1\), and
\[
\beta-1\ge\frac{n(n-1)(1-\alpha)}{2-(n+1)(1-\alpha)}.
\]

In cases 2 and 3, equality in the displayed parameter boundary makes **exactly one** interior log-concavity inequality an equality (at the right edge or left edge respectively). In case 1, all interior inequalities are strict unless \(\alpha=\beta=1\), when the masses are uniform. If \(0<\alpha<1\) and \(0<\beta<1\), every interior log-concavity inequality reverses strictly.

**Finite-sample ceiling.** For fixed \(0<\beta<1\), no choice of \(\alpha>0\) yields \(LC\) when
\[
 n\ge\frac{1+\beta}{1-\beta}.
\]
Below this ceiling a sufficiently large \(\alpha\) does yield \(LC\), with the exact minimum given above. The symmetric statement holds with \(\alpha\) and \(\beta\) interchanged. The ceiling is strict: equality of trial count and the real bound does not permit rescue.

## Assumptions and scope

All beta-binomial masses are strictly positive, since \(n\ge2\) and \(\alpha,\beta>0\). There is no assumption that either beta shape exceeds one. Log-concavity refers to the sequence of **count probabilities** as a function of integer \(k\); it does not mean concavity of a beta density in its real argument, nor concavity of a regression log-likelihood as a function of model coefficients. The case \(n=1\) has no interior inequalities and is deliberately excluded.

## Proof

Define the adjacent ratio \(r_k=p_{k+1}/p_k\), for \(0\le k<n\). The beta-function recurrence gives
\[
 r_k=\frac{(n-k)(\alpha+k)}{(k+1)(\beta+n-k-1)}.
\]
Thus \(p_k^2\ge p_{k-1}p_{k+1}\) is equivalent to \(r_{k-1}\ge r_k\). Write \(u=\alpha-1\) and \(v=\beta-1\). Clearing only strictly positive factors yields the exact identity
\[
 r_{k-1}-r_k
 =\frac{F_k u+G_k v+(n+1)uv}{k(k+1)(\beta+n-k)(\beta+n-k-1)},
\]
where \(F_k=(n-k)(n-k+1)\), \(G_k=k(k+1)\), and \(1\le k<n\). Denote the numerator by \(N_k\). Therefore the global question reduces *without approximation* to simultaneous nonnegativity of the explicit \(N_k\).

When \(u,v\ge0\), all terms in \(N_k\) are nonnegative, and \(N_k>0\) except when \(u=v=0\). If one variable is zero and the other negative, the numerator is strictly negative at every interior index.

When \(u>0>v\), \(F_k\) strictly decreases with \(k\) and \(G_k\) strictly increases. Hence \(N_k\) strictly decreases with \(k\), so checking all indices is equivalent to checking only \(k=n-1\). At that index
\[
 N_{n-1}=u[2+(n+1)v]+n(n-1)v.
\]
Because \(u>0\) and \(v<0\), this can be nonnegative only if \(2+(n+1)v>0\), and in that regime it is equivalent to
\[
 u\ge\frac{n(n-1)(-v)}{2+(n+1)v}.
\]
Substituting the shapes gives case 2 exactly. At equality \(N_{n-1}=0\), and strict decrease gives \(N_k>0\) for all earlier indices. Moreover, when the condition fails, \(N_k<0\) occurs in precisely a (possibly empty when condition passes) right-end consecutive segment. Interchanging success and failure counts replaces \(X\) by \(n-X\) and exchanges \(\alpha\) with \(\beta\); this proves case 3 and the mirrored claims.

When \(u,v<0\), put \(a=-u\) and \(b=-v\), so \(0<a,b<1\). Then
\[
 N_k=-aF_k-bG_k+(n+1)ab
 \le -ab[F_k+G_k-(n+1)]<0.
\]
Indeed \(F_k+G_k=n(n+1)-2k(n-k)>n+1\) for \(n\ge2\) and \(1\le k<n\): since \(2k(n-k)\le n^2/2\), the difference from \(n+1\) is at least \(n^2/2-1>0\). This proves strict log-convexity and exhausts all shape ranges.

Finally, in case 2 the positivity \(2-(n+1)(1-\beta)>0\) is exactly \(n<(1+\beta)/(1-\beta)\). Conversely, whenever this strict inequality holds, taking \(\alpha\) sufficiently large satisfies the sharp bound. The reflected argument proves the other ceiling. ∎

## Verification

The accompanying `verify.py` is standalone Python requiring only the standard library. Run `python verify.py`. It calculates exact rational beta-binomial probabilities via rising factorials, checks the ratio numerator identity, checks the three-region classification, and checks every interior curvature inequality on a specified finite rational grid; its deterministic examples also exhibit equality and finite-trial failure.

For \(n=3\), \(\alpha=5/2\), and \(\beta=3/4\), the probabilities are \((11,30,60,120)/221\), so the right interior inequality is an equality. At \(n=4\) with the same shapes, that right inequality fails. The verifier confirms both examples exactly. Finite checks are supplementary; the proof above covers every allowed real parameter.

## Relationship to prior work

Martin, Witten, and Willis (2019) introduce beta-binomial regression for overdispersed count observations; their Appendix B concerns nonconcavity of regression likelihood **in its coefficient parameters**, a different question from the \(LC\) classification of the probability mass sequence. Johnson, Kontoyiannis, and Madiman discuss log-concavity of discrete compound laws and mention Pólya–Eggenberger laws among standard examples; they do not state the finite-\(n\), subunit-shape necessity-and-sufficiency inequalities above. Bobkov, Marsiglietti, and Melbourne study entropy and concentration within the class of log-concave integer laws; only their abstract was inspected, so no claim is made about the contents of their full paper. The preceding two-point binomial-mixture results address a different latent mixing distribution and do not imply this beta-mixing classification.

## Limitations

An earlier equivalent criterion under Pólya–Eggenberger, urn, or generalized-hypergeometric terminology is possible; no claim of an exhaustive world-literature search is made. The classification is for ordinary log-concavity of a beta-binomial mass function only. It does not classify arbitrary binomial mixing measures, Dirichlet-multinomial vectors, or posterior likelihood concavity in regression coefficients. Nothing here shows that a numerical algorithm for which log-concavity is useful remains exact outside the proved regimes. The arithmetic verifier cannot establish results for untested real parameters by itself.

## References

1. B. D. Martin, D. Witten, and A. D. Willis, *Modeling microbial abundances and dysbiosis with beta-binomial regression*, arXiv:1902.02776v1 (2019), especially Section 3 and Appendix B. https://arxiv.org/html/1902.02776v1
2. S. G. Bobkov, A. Marsiglietti, and J. Melbourne, *Concentration functions and entropy bounds for discrete log-concave distributions*, arXiv:2007.11030v1 (2020). https://arxiv.org/abs/2007.11030
3. O. Johnson, I. Kontoyiannis, and M. Madiman, *Log-concavity, ultra-log-concavity, and a maximum entropy property of discrete compound Poisson measures*, arXiv:0912.0581v2 (2011), especially Sections 2 and 5. https://arxiv.org/html/0912.0581v2
