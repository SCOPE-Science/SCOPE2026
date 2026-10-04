# Fixed points of the generalized equilibrium transform are signed exponentials
## Finding
Let \(X\) be a nondegenerate real-valued random variable with \(0<\mathbb{E}|X|<\infty\), distribution function \(F\), and generalized equilibrium transform \(X^e\) defined by
\[
f^e(t)=\begin{cases}
F(t)/\mathbb{E}|X|,&t<0,\\
(1-F(t))/\mathbb{E}|X|,&t\ge0.
\end{cases}
\]
Then \(X^e\stackrel{d}{=}X\) if and only if there exist \(a>0\) and \(p\in[0,1]\) such that
\[
F(x)=\begin{cases}
p e^{x/a},&x<0,\\
1-(1-p)e^{-x/a},&x\ge0.
\end{cases}
\]
Equivalently, \(X\stackrel{d}{=}SE\), where \(E\) is exponential with mean \(a\), \(S\in\{-1,+1\}\) is independent of \(E\), and \(\mathbb{P}(S=-1)=p\). Thus the magnitude is necessarily memoryless with one common scale, while the sign bias is arbitrary. The endpoint cases \(p=0\) and \(p=1\) are the positive and negative exponential laws, and \(p=1/2\) is the centered Laplace law.

## Assumptions and scope
The transform is the generalized equilibrium distribution introduced for random variables with general real support by Capaldo, Di Crescenzo, and Navarro. The only assumptions used are nondegeneracy and \(0<\mathbb{E}|X|<\infty\). No second moment, smooth baseline density, symmetry, or sign-balance assumption is imposed. The result classifies distributional fixed points only; it does not assert convergence of iterates, attraction, rates, or absence of nontrivial periodic points.

## Proof
Assume first that \(X^e\stackrel{d}{=}X\), and set \(a=\mathbb{E}|X|\). Since \(X^e\) has a Lebesgue density, the fixed-point identity implies that \(X\) is absolutely continuous. Hence \(F\) is absolutely continuous and, for almost every \(x<0\), equality of the two densities gives
\[
F'(x)=\frac{F(x)}{a}.
\]
Therefore the absolutely continuous function \(e^{-x/a}F(x)\) has derivative zero almost everywhere on every bounded subinterval of \(( -\infty,0)\). It is constant there, so for some \(p\in[0,1]\),
\[
F(x)=p e^{x/a},\qquad x<0.
\]
Likewise, for almost every \(x>0\),
\[
F'(x)=\frac{1-F(x)}{a}.
\]
Thus \(e^{x/a}(1-F(x))\) has derivative zero almost everywhere, and continuity of the absolutely continuous CDF at zero forces
\[
1-F(x)=(1-p)e^{-x/a},\qquad x\ge0.
\]
The fixed point has no atom at zero because it is absolutely continuous. This proves necessity, including the boundary cases \(p=0\) and \(p=1\).

Conversely, suppose \(F\) has the displayed form. Its density is
\[
f(x)=\begin{cases}
(p/a)e^{x/a},&x<0,\\
((1-p)/a)e^{-x/a},&x>0,
\end{cases}
\]
and \(\mathbb{E}|X|=a\). Substituting the CDF and survival function into the defining generalized equilibrium density gives exactly the same \(f\) on both half-lines. Hence \(X^e\stackrel{d}{=}X\).

Finally, the same CDF is obtained by taking an exponential magnitude \(E\) of mean \(a\) and an independent sign \(S\) with \(\mathbb{P}(S=-1)=p\). This establishes the equivalent independent-sign representation.

## Verification
The proof was checked in both directions. The forward direction uses only the fact that the transform has a density, the resulting almost-everywhere first-order equations, and absolute continuity to integrate those equations. The converse was checked by direct substitution and by the identity \(\mathbb{E}|SE|=\mathbb{E}E=a\). The behavior at zero is covered because a fixed point is absolutely continuous and therefore has no atom there.

A further normalization check shows why the two exponential decay rates cannot differ: the same normalizing constant \(a=\mathbb{E}|X|\) appears in both half-line differential equations. The sign probability remains free because neither equation couples the two side masses beyond continuity and total mass one.

## Relationship to prior work
Capaldo, Di Crescenzo, and Navarro define the general-support equilibrium density used here and develop its mixture representation, stochastic-order properties, aging properties, and risk-theory applications. Their article does not state a fixed-point classification. The classical nonnegative equilibrium transform is known to have the exponential distribution as its only fixed point; Shevtsova and Tselishchev explicitly summarize that characterization, and Di Crescenzo and Meoli prove the analogous exponential characterization for a fractional nonnegative equilibrium transform.

The present classification is not a relabeling of the classical one-sided result. Allowing both signs produces a full sign-bias family: the magnitude must still be exponential, but the transform preserves an arbitrary negative-side mass \(p\) once both half-lines share the same scale. In particular, only the balanced member \(p=1/2\) is the centered Laplace distribution.

## Limitations
This theorem concerns exactly the generalized equilibrium transform defined above. Other objects also called generalized, stationary-renewal, or asymmetric equilibrium transforms can use different normalizations or Stein identities and therefore have different fixed-point sets. No claim is made that the fixed-point family is attractive under iteration, that iterates exist under weaker moment assumptions, or that no nontrivial cycles exist. The literature comparison is necessarily limited by indexing and terminology; an equivalent fixed-point statement in older or differently named renewal-transform literature remains a residual originality risk.

## References
1. M. Capaldo, A. Di Crescenzo, and J. Navarro, “Generalized equilibrium distributions,” *Probability in the Engineering and Informational Sciences*. DOI:10.1017/S0269964825100041. First published online 31 July 2025.
2. I. Shevtsova and M. Tselishchev, “A Generalized Equilibrium Transform with Application to Error Bounds in the Rényi Theorem with No Support Constraints,” *Mathematics* 8 (2020), 577. DOI:10.3390/math8040577.
3. A. Di Crescenzo and A. Meoli, “On the fractional probabilistic Taylor’s and mean value theorems,” arXiv:1611.01686.
