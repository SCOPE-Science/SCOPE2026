# Exact phase-count classification for the ferromagnetic Widom–Rowlinson boundary law

## Finding

Consider the ferromagnetic soft-core Widom–Rowlinson translation-invariant boundary-law system
\[
u=a\frac{1+u^k+\theta v^k}{1+u^k+v^k},\qquad
v=a\frac{1+\theta u^k+v^k}{1+u^k+v^k},
\qquad a=\lambda^{1/k},
\]
with integer \(k\ge4\), \(0<\theta<1\), and \(\lambda>0\). Define
\[
\theta_c(k)=\frac{k-1}{k+1}.
\]
If \(\theta\ge\theta_c(k)\), there is exactly one positive solution for every \(\lambda>0\), and it is symmetric.

If \(0<\theta<\theta_c(k)\), define
\[
\lambda_c(k,\theta)=
\frac{1}{k-1-(k+1)\theta}
\left(\frac{k+1}{k}\right)^k.
\]
Then there is exactly one positive solution for \(0<\lambda\le\lambda_c(k,\theta)\) and exactly three positive solutions for \(\lambda>\lambda_c(k,\theta)\). Thus Conjecture 1 of the motivating source is true in its previously unresolved range \(k\ge4\).

The nonsymmetric pair has an exact one-parameter representation. For \(t>0\), put
\[
D_{k,\theta}(t)=\sinh((k-1)t)-\theta\sinh((k+1)t).
\]
Whenever \(D_{k,\theta}(t)>0\), let
\[
q(t)=\left(\frac{\sinh t}{D_{k,\theta}(t)}\right)^{1/k},
\qquad
u(t)=e^tq(t),
\qquad
v(t)=e^{-t}q(t),
\]
and
\[
\Lambda_{k,\theta}(t)=
\left(\frac{\sinh((k+1)t)}{\sinh(kt)}\right)^k
\frac{\sinh t}{D_{k,\theta}(t)}.
\]
Every nonsymmetric positive solution is exactly \((u(t),v(t))\) or \((v(t),u(t))\) for one unique \(t\), with \(\lambda=\Lambda_{k,\theta}(t)\). The function \(\Lambda_{k,\theta}\) is strictly increasing from \(\lambda_c(k,\theta)\) to \(+\infty\) on its domain.

In the boundary-law correspondence used by the source, these positive solutions give the same exact count of translation-invariant splitting Gibbs measures.

## Assumptions and scope

The theorem uses the source normalization above, integer tree order \(k\ge4\), ferromagnetic soft-core parameter \(0<\theta<1\), and positive activity \(\lambda\). It counts positive translation-invariant boundary-law solutions, hence translation-invariant splitting Gibbs measures in the source correspondence. It does not count non-translation-invariant Gibbs measures, extremal decompositions, periodic measures, or dynamical Gibbs states.

The argument itself also works algebraically for lower orders, but the scientific claim here is the unresolved \(k\ge4\) regime identified by the source.

## Proof

First, the symmetric branch is unique. Setting \(u=v=x\) gives
\[
a=\phi(x):=x\frac{1+2x^k}{1+(1+\theta)x^k}.
\]
Its logarithmic derivative satisfies
\[
\frac{x\phi'(x)}{\phi(x)}
=1+k\frac{(1-\theta)x^k}
{(1+2x^k)(1+(1+\theta)x^k)}>0,
\]
so \(\phi\) is strictly increasing from \(0\) to \(+\infty\). Thus exactly one positive symmetric solution exists for each \(a>0\).

Now suppose \(u\ne v\), and by swapping coordinates assume \(u>v\). Set \(r=u/v>1\) and
\[
S_r=1+r+\cdots+r^{k-1},\quad
B_r=r+r^2+\cdots+r^{k-1},\quad
C_r=1+r+\cdots+r^k.
\]
Subtracting the two boundary-law equations and then adding them eliminates \(a\) and gives the exact identity
\[
v^k(B_r-\theta C_r)=1.
\]
Conversely, this identity together with
\[
a=v\frac{C_r}{S_r}
\]
reconstructs both original equations, so no nonsymmetric solutions have been lost or added.

Write \(r=e^{2t}\), \(t>0\). The geometric sums become hyperbolic sines, and the preceding identities give exactly
\[
u=e^tq(t),\qquad v=e^{-t}q(t),\qquad
\lambda=\Lambda_{k,\theta}(t),
\]
with \(q\), \(D_{k,\theta}\), and \(\Lambda_{k,\theta}\) as stated above. Hence nonsymmetric solutions exist precisely when
\[
\theta<\frac{\sinh((k-1)t)}{\sinh((k+1)t)}.
\]
For fixed \(t>0\), the function \(s\mapsto s\coth(st)\) is strictly increasing, so the ratio on the right is strictly decreasing in \(t\), starts at \((k-1)/(k+1)\), and tends to \(0\). Therefore no nonsymmetric solution exists when \(\theta\ge\theta_c(k)\). If \(0<\theta<\theta_c(k)\), the admissible \(t\)-domain is one interval beginning at \(0\).

It remains to prove that \(\Lambda_{k,\theta}\) is strictly increasing. Define
\[
Q_n(t)=\frac{\sinh(nt)}{n\sinh t},
\qquad
g_n(t)=\frac{d}{dt}\log Q_n(t)=n\coth(nt)-\coth t,
\]
and put
\[
\eta=\frac{(k+1)\theta}{k-1}.
\]
Then
\[
\frac{\Lambda_{k,\theta}(t)}{\lambda_c(k,\theta)}
=(1-\eta)
\frac{(Q_{k+1}/Q_k)^k}{Q_{k-1}-\eta Q_{k+1}}.
\]
For fixed \(t>0\), extend \(g_n\) to a real variable \(s\ge1\) by
\[
g_s=s\coth(st)-\coth t.
\]
Direct differentiation gives
\[
\partial_s g_s=\coth(st)-st\,\operatorname{csch}^2(st)>0,
\]
and
\[
\partial_s^2g_s=2t\,\operatorname{csch}^2(st)
\bigl(st\coth(st)-1\bigr)>0.
\]
Thus \(g_s\) is strictly increasing and strictly convex. If \(\Delta_j=g_{j+1}-g_j\), then \(\Delta_j\) is positive and strictly increasing, while \(g_1=0\). Consequently
\[
k(g_{k+1}-g_k)>g_{k-1}.
\]

After multiplying the logarithmic derivative of \(\Lambda_{k,\theta}\) by the positive denominator \(Q_{k-1}-\eta Q_{k+1}\), its sign is the sign of an affine function of \(\eta\):
\[
N(\eta)=k(g_{k+1}-g_k)(Q_{k-1}-\eta Q_{k+1})
-(Q'_{k-1}-\eta Q'_{k+1}).
\]
At \(\eta=0\), the preceding inequality gives \(N(0)>0\). At the other endpoint \(\eta=Q_{k-1}/Q_{k+1}\),
\[
N(\eta)=Q_{k-1}(g_{k+1}-g_{k-1})>0.
\]
The admissible domain has \(0\le\eta<Q_{k-1}/Q_{k+1}\), so affinity implies \(N(\eta)>0\) throughout. Hence \(\Lambda_{k,\theta}'(t)>0\).

Finally,
\[
\lim_{t\downarrow0}\Lambda_{k,\theta}(t)
=\frac{1}{k-1-(k+1)\theta}
\left(\frac{k+1}{k}\right)^k
=\lambda_c(k,\theta),
\]
and \(\Lambda_{k,\theta}(t)\to+\infty\) at the other endpoint of its domain. Therefore each \(\lambda>\lambda_c\) has exactly one nonsymmetric parameter \(t\), producing exactly one swap-pair, while \(\lambda\le\lambda_c\) has none. Together with the unique symmetric branch, this proves the stated one-versus-three classification.

## Verification

The proof is exact and does not infer an infinite statement from finite experimentation. The accompanying `verify.py` independently reconstructs the hyperbolic parameterization for representative orders and parameters, substitutes it into both original boundary-law equations, checks strict numerical increase of \(\Lambda_{k,\theta}\) on sampled points, and checks the critical limit. Replay produced `VERIFY_OK cases=112 max_residual=1.998e-15`.

The computation is corroborative only. The decisive steps are the reversible elimination, the hyperbolic parameterization, the exact domain inequality, and the convexity argument for the logarithmic derivative.

## Relationship to prior work

Kissel, Külske, and Rozikov derive the same two-variable boundary-law system and the threshold
\[
\theta_c(k)=\frac{k-1}{k+1},
\qquad
\lambda_c(k,\theta)=
\frac{1}{k-1-(k+1)\theta}
\left(\frac{k+1}{k}\right)^k.
\]
For \(k\ge4\), however, their theorem proves only partial phase-count statements and then states Conjecture 1 asserting that the counts should be exactly one and exactly three in the complementary parameter regimes. Their subsequent reduction identifies a constrained minimization as the remaining obstacle and reports computer checks only for finitely many orders. The present theorem supplies a different reversible parameterization and a monotonicity proof that closes that gap for every \(k\ge4\).

A later paper on dynamical Gibbs–non-Gibbs transitions for Widom–Rowlinson models on trees cites the static result in the weaker form that the non-uniqueness region has at least three translation-invariant splitting Gibbs measures. It does not supply the exact global phase count proved here.

Targeted database searches using the model name, source identifier, threshold formula, Conjecture 1 language, translation-invariant splitting Gibbs measure aliases, and the hyperbolic parameterization did not locate a published statement implying this theorem.

## Limitations

The theorem is confined to the translation-invariant boundary-law sector of the ferromagnetic soft-core model. It does not classify all Gibbs measures, periodic or weakly periodic boundary laws, extremality, reconstruction, free-energy dominance, or dynamical Gibbs properties. It does not claim that a literature search proves absolute novelty; an equivalent argument hidden in weakly indexed material remains a residual risk.

## References

1. S. Kissel, C. Külske, and U. A. Rozikov, *Hard-Core and Soft-Core Widom–Rowlinson Models on Cayley Trees*, arXiv:1901.09258v1, first public 2019-01-26; Journal of Statistical Mechanics: Theory and Experiment (2019) 043204, DOI 10.1088/1742-5468/ab081e.
2. F. Henning, C. Külske, A. Le Ny, and U. A. Rozikov, *Dynamical Gibbs-non-Gibbs transitions in Widom–Rowlinson models on trees*, arXiv:2012.09718v1.
