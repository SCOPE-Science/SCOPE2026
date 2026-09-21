# Exact Fisher-information preservation at multiple locations under a fixed interval quantizer

## Setting

Let
\[
p_\theta(x)=f(x-\theta),\qquad \theta\in\mathbb R,
\]
be a one-dimensional location family. Assume that the parent density \(f\) is positive on \(\mathbb R\), locally absolutely continuous, tends to zero at both tails, and has finite nonzero Fisher information
\[
J=\int_{\mathbb R}\left(\frac{f'(z)}{f(z)}\right)^2 f(z)\,dz\in(0,\infty).
\]
Write the location score as
\[
s(z)=-\frac{f'(z)}{f(z)}
\]
for almost every \(z\).

Fix a deterministic interval quantizer with \(m\ge2\) cells and finite threshold set
\[
T=\{\tau_1<\cdots<\tau_{m-1}\}.
\]
Let \(J_Q(\theta)\) denote the Fisher information about \(\theta\) in the quantized observation.

A finite-step score has a unique minimal finite knot set
\[
K=\{c_1<\cdots<c_\kappa\}
\]
meaning that \(s\) is almost everywhere constant on the \(\kappa+1\) complementary intervals and adjacent constants are distinct. If no such finite set exists, call the score non-finite-step.

## Main theorem: translation-incidence characterization

For every \(\theta\),
\[
J-J_Q(\theta)
=\mathbb E_\theta\!\left[\operatorname{Var}_\theta\bigl(S_\theta(X)\mid Q(X)\bigr)\right]\ge0,
\]
where \(S_\theta(X)=s(X-\theta)\) is the full-data score. Consequently:

1. If the score is non-finite-step, then \(J_Q(\theta)<J\) for every \(\theta\).
2. If the score has minimal knot set \(K\), then
   \[
   \boxed{\ J_Q(\theta)=J\quad\Longleftrightarrow\quad K+\theta\subseteq T.\ }
   \]

Thus the complete lossless-location set of a fixed quantizer is
\[
\boxed{\ \Lambda(Q,f)=\{\theta\in\mathbb R:K+\theta\subseteq T\}\ }
\]
when the score is finite-step, and is empty otherwise.

Equivalently, exact Fisher-information preservation at even one location forces the parent density to be continuous piecewise exponential: on each interval between score knots, \(\log f\) is affine.

## Exact design law for several target locations

Let \(\Theta\subset\mathbb R\) be a nonempty finite set of target locations. A fixed interval quantizer is Fisher-lossless at every \(\theta\in\Theta\) if and only if
\[
T\supseteq K+\Theta:=\{c+\theta:c\in K,\ \theta\in\Theta\}.
\]
Hence the exact minimum number of cells required is
\[
\boxed{\ m_{\min}=|K+\Theta|+1.\ }
\]

Because finite nonempty subsets of \(\mathbb R\) satisfy
\[
|K+\Theta|\ge |K|+|\Theta|-1,
\]
any \(m\)-cell quantizer obeys the sharp bound
\[
\boxed{\ |\Lambda(Q,f)|\le m-\kappa.\ }
\]
The bound is sharp for every \(1\le\kappa\le m-1\). For example, take
\[
K=\{0,d,\ldots,(\kappa-1)d\},\qquad
T=\{0,d,\ldots,(m-2)d\}
\]
with \(d>0\), and choose any integrable continuous piecewise-exponential density whose score changes at every point of \(K\). Then
\[
\Lambda=\{0,d,\ldots,(m-\kappa-1)d\},
\]
so \(|\Lambda|=m-\kappa\).

One explicit parent density for the sharpness construction is obtained by taking the score constants on the \(\kappa+1\) consecutive intervals to be
\[
q_j=-1+\frac{2j}{\kappa},\qquad 0\le j\le\kappa,
\]
and defining
\[
f(z)=C\exp\!\left(-\int_0^z q(u)\,du\right),
\]
where \(q(u)=q_j\) on the \(j\)-th interval and \(C\) normalizes the density. The leftmost score is negative, the rightmost is positive, adjacent scores differ, and the Fisher information is finite.

## Universal extremizer: asymmetric Laplace

A positive integrable density on all of \(\mathbb R\) cannot have a globally constant score, so every finite-step score has \(\kappa\ge1\). Therefore every fixed \(m\)-cell interval quantizer satisfies
\[
\boxed{\ |\Lambda(Q,f)|\le m-1.\ }
\]
Moreover equality holds if and only if the parent density is asymmetric Laplace, up to translation and scale/rate parameters.

Indeed, equality forces \(\kappa=1\). If the unique knot is \(c\), integrability forces the two score values to be \(-a\) and \(b\) with \(a,b>0\), hence
\[
f(z)=\frac{ab}{a+b}
\begin{cases}
 e^{a(z-c)},&z<c,\\
 e^{-b(z-c)},&z\ge c.
\end{cases}
\]
Its full location Fisher information is \(J=ab\), and for every threshold set \(T\),
\[
\Lambda(Q,f)=T-c.
\]
Thus an \(m\)-cell fixed quantizer preserves all Fisher information at exactly its \(m-1\) threshold-aligned locations (after the knot translation), and at no other locations.

For the symmetric Laplace density this says simply: a fixed interval quantizer is Fisher-lossless exactly when the unknown location coincides with one of its finite thresholds.

## Proof

Let the quantizer cells be \(C_j=(\tau_{j-1},\tau_j]\), with \(\tau_0=-\infty\) and \(\tau_m=\infty\). Under \(X=\theta+Z\), \(Z\sim f\),
\[
p_j(\theta)=\Pr_\theta(Q(X)=j)
=\int_{\tau_{j-1}-\theta}^{\tau_j-\theta}f(z)\,dz.
\]
Differentiating gives
\[
p_j'(\theta)
=f(\tau_{j-1}-\theta)-f(\tau_j-\theta)
=\int_{\tau_{j-1}-\theta}^{\tau_j-\theta}s(z)f(z)\,dz.
\]
Therefore the quantized score in cell \(j\) is
\[
\frac{p_j'(\theta)}{p_j(\theta)}
=\mathbb E\bigl[s(Z)\mid Z\in C_j-\theta\bigr].
\]
Consequently
\[
J_Q(\theta)=\mathbb E\!\left[\mathbb E(S_\theta\mid Q)^2\right],
\]
and the conditional-variance decomposition gives
\[
J-J_Q(\theta)=\mathbb E\!\left[\operatorname{Var}(S_\theta\mid Q)\right].
\]
Because \(f>0\), equality holds exactly when \(s\) is Lebesgue-a.e. constant on every shifted cell \(C_j-\theta\). Thus equality at one \(\theta\) already makes \(s\) a finite-step function whose essential change points are contained in \(T-\theta\). For the minimal knot set \(K\), equality at a general \(\theta\) is therefore equivalent to \(K\subseteq T-\theta\), or \(K+\theta\subseteq T\).

If \(s\) is finite-step, \((\log f)'=-s\) almost everywhere, so \(\log f\) is affine between successive knots and \(f\) is piecewise exponential. The simultaneous-target statement follows by taking the union of the required translated knot sets. The sumset inequality follows by ordering \(K=\{c_1<\cdots<c_\kappa\}\) and \(\Theta=\{\theta_1<\cdots<\theta_L\}\):
\[
c_1+\theta_1<\cdots<c_\kappa+\theta_1<c_\kappa+\theta_2<\cdots<c_\kappa+\theta_L,
\]
which supplies \(\kappa+L-1\) distinct sums. Applying this with \(\Theta=\Lambda\) gives \(|\Lambda|\le m-\kappa\). The constructions above attain equality. Finally, \(\kappa=0\) would make \(f\) a single exponential on all of \(\mathbb R\), which is not integrable; hence \(\kappa\ge1\), and the universal \(m-1\) bound and asymmetric-Laplace equality classification follow.

## Relation to prior work

The one-parameter information-loss inequality and its equality condition are not claimed as new. Hobza, Molina and Vajda (2005, Theorem 3.1) give the corresponding equality criterion for interval quantizations of location families in their probability-coordinate formulation; their paper explicitly treats reduction and convergence of Fisher information under interval quantization. Cabral Farias and Brossier (2013) use the exact score-projection loss identity
\[
I_q=I_c-\mathbb E[(S_c-S_q)^2]
\]
and explicitly note that a binary central threshold preserves all location Fisher information for the Laplace distribution.

Pötzelberger and Felsenstein (1993) is especially close prior work: it studies Fisher-information loss for finite interval discretizations, particularly for location parameters, and includes double-exponential examples. Its available bibliographic record and abstract were checked, but its full theorem text was not accessible in this review. Mayoral, Morales, Morales and Vajda (2003) also study efficiency and Fisher-information decrease under finite quantization.

The contribution claimed here, to the best of our knowledge, is the fixed-quantizer **multi-location** rigidity and combinatorial design law: the exact translate-containment formula \(\Lambda=\{\theta:K+\theta\subseteq T\}\), the exact minimum \(1+|K+\Theta|\) cells for a prescribed finite location set, the sharp \(|\Lambda|\le m-\kappa\) bound, and the characterization of asymmetric Laplace as the unique full-support location family attaining the universal \(m-1\) lossless-location maximum.

## Limitations

The result concerns one-dimensional full-support location families, deterministic interval quantizers, and local Fisher information. It does not address vector parameters, non-interval or randomized quantizers, adaptive thresholds depending on data or parameter estimates, global sufficiency, exact likelihood preservation, finite-sample risk, or approximate information retention. The 1993 Pötzelberger--Felsenstein paper remains the principal residual originality risk because a complete theorem-by-theorem comparison was not possible from the accessible material.

## References

1. K. Pötzelberger and K. Felsenstein, “On the Fisher information of discretized data,” *Journal of Statistical Computation and Simulation* 46 (1993), 125–144. https://doi.org/10.1080/00949659308811499
2. A. M. Mayoral, D. Morales, J. Morales and I. Vajda, “On efficiency of estimation and testing with data quantized to fixed number of cells,” *Metrika* 57 (2003), 1–27. https://doi.org/10.1007/s001840100178
3. T. Hobza, I. Molina and I. Vajda, “On convergence of Fisher informations in continuous models with quantized observations,” *TEST* 14 (2005), 151–179. https://doi.org/10.1007/BF02595401
4. R. Cabral Farias and J.-M. Brossier, “Optimal Scalar Quantization for Parameter Estimation,” arXiv:1310.6945 (2013). https://arxiv.org/abs/1310.6945
