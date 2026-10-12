# Exact Kesten–Stigum boundary for nontrivial three-state Potts phases on the order-four Cayley tree

## Finding

Consider the ferromagnetic three-state Potts model on the Cayley tree of order \(k=4\), with \(\theta=e^{\beta J}>1\). Up to permutation of spin labels, every nontrivial translation-invariant splitting Gibbs measure has boundary law \((z,1,1)\), where \(z>0\), \(z\ne1\), satisfies
\[
z=\left(\frac{\theta z+2}{z+\theta+1}\right)^4.
\]
Put \(t=z^{1/4}\). Then every nontrivial solution is parameterized by
\[
\boxed{\theta(t)=\frac{t^4+t^3+t^2+t+2}{t(t^2+t+1)}},\qquad t>0,\ t\ne1.
\]
The two nontrivial eigenvalues of the corresponding three-state transition matrix are
\[
\lambda_a(t)=\frac{1}{(t+1)(t^2+1)},
\qquad
\lambda_b(t)=\frac{t^3(t+2)}{(t+1)(t^2+1)(t^4+2)}.
\]
Moreover,
\[
\lambda_b(t)-\lambda_a(t)
=
\frac{2(t-1)(t^2+t+1)}{(t+1)(t^2+1)(t^4+2)}.
\]
Hence the second eigenvalue in absolute value is \(\lambda_a\) for \(0<t<1\) and \(\lambda_b\) for \(t>1\).

Let \(\rho\in(0,1)\) be the unique root of
\[
\rho^3+\rho^2+\rho-1=0,
\]
so \(\rho=0.543689012692076\ldots\), and define
\[
\boxed{\theta_{\mathrm{KS}}=2(1+\rho)=3.087378025384152\ldots}.
\]
Then the Kesten–Stigum sufficient condition for non-extremality,
\[
4\lambda_*^2>1,
\]
holds for a nontrivial TISGM if and only if its parameter satisfies \(0<t<\rho\). Equivalently, on the \(z<1\) branch it holds exactly when
\[
\boxed{\theta>\theta_{\mathrm{KS}}}.
\]
For every nontrivial branch with \(t>1\), the Kesten–Stigum condition never holds.

This is an exact classification of what the Kesten–Stigum test certifies. Failure of that sufficient condition is not a proof of extremality.

## Assumptions and scope

The model is the homogeneous zero-field ferromagnetic three-state Potts model on the order-four Cayley tree. The boundary-law convention and tree order are those used in the cited Potts literature. By the standard classification, for \(q=3\) the nontrivial TISGM type is represented, up to relabeling, by one distinguished boundary-law coordinate, so it is enough to analyze \((z,1,1)\).

The statement concerns only the Kesten–Stigum sufficient non-extremality criterion. It does not determine the true reconstruction threshold and does not assert extremality when \(4\lambda_*^2\le1\).

## Proof

The boundary-law equation is
\[
z=\left(\frac{\theta z+2}{z+\theta+1}\right)^4.
\]
For \(t=z^{1/4}>0\), positivity allows taking the positive fourth root:
\[
t=\frac{\theta t^4+2}{t^4+\theta+1}.
\]
For \(t\ne1\), solving for \(\theta\) and cancelling the common factor \(t-1\) gives
\[
\theta(t)
=
\frac{t^5+t-2}{t^4-t}
=
\frac{t^4+t^3+t^2+t+2}{t(t^2+t+1)}.
\]
Also
\[
\theta(t)-1=\frac{t^4+2}{t(t^2+t+1)}>0,
\]
so the parameterization stays in the ferromagnetic region.

For boundary law \((z,1,1)\), the transition matrix is
\[
P=
\begin{pmatrix}
\dfrac{\theta z}{\theta z+2}&\dfrac{1}{\theta z+2}&\dfrac{1}{\theta z+2}\\[6pt]
\dfrac{z}{z+\theta+1}&\dfrac{\theta}{z+\theta+1}&\dfrac{1}{z+\theta+1}\\[6pt]
\dfrac{z}{z+\theta+1}&\dfrac{1}{z+\theta+1}&\dfrac{\theta}{z+\theta+1}
\end{pmatrix}.
\]
The vector \((0,1,-1)\) gives one eigenvalue
\[
\frac{\theta-1}{z+\theta+1}.
\]
The remaining nontrivial eigenvalue is the second eigenvalue of the lumped two-state chain separating spin \(1\) from spins \(2,3\). Using \(\theta z+2=t(z+\theta+1)\), it is
\[
\frac{z}{z+\theta+1}\left(\frac{\theta}{t}-1\right).
\]
Substitution of \(z=t^4\) and \(\theta(t)\) reduces these exactly to
\[
\lambda_a(t)=\frac{1}{(t+1)(t^2+1)},
\qquad
\lambda_b(t)=\frac{t^3(t+2)}{(t+1)(t^2+1)(t^4+2)}.
\]
Their difference has the factorization displayed above, so the larger absolute nontrivial eigenvalue switches only at \(t=1\).

For \(t>1\), the inequality \(\lambda_b<1/2\) is equivalent to positivity of
\[
G(t)=(t+1)(t^2+1)(t^4+2)-2t^3(t+2).
\]
Writing \(s=t-1>0\) gives
\[
G(1+s)=s^7+8s^6+28s^5+54s^4+59s^3+36s^2+14s+6>0.
\]
Thus \(4\lambda_b^2<1\) on every \(t>1\) branch.

For \(0<t<1\), the Kesten–Stigum inequality is \(\lambda_a>1/2\), equivalently
\[
(t+1)(t^2+1)<2
\quad\Longleftrightarrow\quad
t^3+t^2+t-1<0.
\]
The cubic is strictly increasing for \(t>0\), is negative at \(0\), and positive at \(1\). It therefore has a unique root \(\rho\in(0,1)\), and the criterion holds exactly for \(0<t<\rho\).

It remains to translate this to temperature parameter \(\theta\). Differentiation gives
\[
\theta'(t)=
\frac{t^6+2t^5+3t^4-6t^2-4t-2}
{t^2(t^2+t+1)^2}.
\]
For \(0<t<1\), the numerator is less than
\[
6t^4-6t^2-4t-2<0,
\]
so \(\theta(t)\) is strictly decreasing on this branch. It decreases from \(+\infty\) to \(2\). At \(t=\rho\), the relation \(\rho^3+\rho^2+\rho=1\) implies
\[
\theta(\rho)=2(1+\rho).
\]
Therefore \(t<\rho\) is equivalent to \(\theta>\theta_{\mathrm{KS}}\), completing the classification.

## Verification

The accompanying `verification/verify.py` uses only the Python standard library. It checks the exact polynomial identities behind the parameterization, eigenvalue reduction, branch ordering, positive-coefficient proof for \(t>1\), derivative numerator, and the algebraic reduction \(\theta(\rho)=2(1+\rho)\). It also isolates \(\rho\) numerically for display. These calculations replay exact identities already proved above; the numerical root is not used as an infinite-domain certificate.

## Relationship to prior work

Rozikov's 2021 survey states the general scalar boundary-law equation for Potts TISGMs and explicitly remarks that for the three-state model, extremality had been studied at order \(k=3\), while the case \(k\ge4\) had not been considered because an explicit formula for nontrivial solutions was unavailable. The present order-four argument avoids solving \(z\) as a function of \(\theta\): it instead uses the positive root parameter \(t=z^{1/4}\), in which \(\theta\) and both nontrivial transition eigenvalues become rational functions.

Külske and Rozikov's earlier general extremality paper supplies the transition-matrix framework and Kesten–Stigum criterion, but its explicit Section 4 critical-parameter theorem is restricted to the order-two tree. The 2024 order-three paper of Makhammadaliev treats \(k=3\), explicitly notes bulky branch formulas, and works with estimates for part of its Kesten–Stigum analysis. Neither inspected statement implies the exact order-four threshold above.

Targeted searches for order-four, \(q=3\), Kesten–Stigum, the cubic \(t^3+t^2+t-1\), the decimal threshold, and the rational eigenvalue form did not locate a matching published result. A weakly indexed equivalent calculation under different boundary-law notation remains possible and is recorded as a residual risk.

## Limitations

The result is about the Kesten–Stigum sufficient condition only. In particular, \(4\lambda_*^2\le1\) does not imply extremality, and no claim is made about the exact reconstruction threshold. The result is specialized to \(q=3\) and tree order \(k=4\), although the root parameterization suggests related calculations for other orders.

The literature comparison is strongest for the cited general, survey, order-two, order-three, and exact-query sources. An equivalent unpublished or weakly indexed order-four calculation could exist under different notation.

## References

1. U. A. Rozikov, “Gibbs Measures of Potts Model on Cayley Trees: A Survey and Applications,” arXiv:2103.07391v1 (2021), especially equation (3.6) and Remark 4.1.
2. C. Külske and U. A. Rozikov, “Fuzzy transformations and extremality of Gibbs measures for the Potts model on a Cayley tree,” arXiv:1403.5775; *Random Structures & Algorithms* 50 (2017), 636–678, DOI:10.1002/rsa.20671.
3. M. T. Makhammadaliev, “Pure phases of the ferromagnetic Potts model with \(q\) states on the Cayley tree of order three,” *Vestnik Udmurtskogo Universiteta. Matematika. Mekhanika. Komp'yuternye Nauki* 34 (2024), 499–517, DOI:10.35634/VM240403.
