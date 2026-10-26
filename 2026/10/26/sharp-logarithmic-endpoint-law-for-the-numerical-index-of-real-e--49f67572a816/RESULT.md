# Sharp logarithmic endpoint law for the numerical index of real \(\ell_p^2\)

## Finding
For the real Banach space \(X_p=\ell_p^2(\mathbb R)\), let \(n(X_p)\) denote its numerical index. Put \(L_p=\log(2p)\). As \(p\to+\infty\),
\[
 n(X_p)=1-\frac{L_p+1}{p}+\frac{L_p^2+1}{2p^2}
       +O\!\left(\frac{L_p^3}{p^3}\right).
\]
For \(p>2\), let \(t_p\in(0,1)\) be the maximizer in the scalar formula stated below. This maximizer is unique, and its endpoint scale is
\[
 t_p^p=\frac{1}{2p}+\frac{1-L_p}{2p^2}
      +O\!\left(\frac{L_p^2}{p^3}\right).
\]
In particular, \(\lim_{p\to\infty}\{p[1-n(X_p)]-\log p\}=1+\log 2\) and \(\lim_{p\to\infty}p\,t_p^p=1/2\). By finite-dimensional duality, the same numerical-index expansion applies to the real conjugate-exponent spaces \(\ell_q^2\) as \(q\downarrow1\), after substituting \(p=q/(q-1)\). These two expansions, including the singular optimizing scale, constitute one endpoint finding.

## Assumptions and scope
For a real Banach space \(X\), the numerical radius of a bounded operator \(T\) is
\[
 v(T)=\sup\{|x^*(Tx)|: \|x\|=\|x^*\|=x^*(x)=1\},
 \qquad n(X)=\inf_{\|T\|=1}v(T).
\]
The theorem concerns \(p\to\infty\) with \(p>2\), and has a big-\(O\) remainder with constants independent of sufficiently large \(p\). A recently established exact identity [1], not reproved here, identifies the real two-dimensional index with the rotation numerical radius:
\[
 n(\ell_p^2)=M_p=\max_{0<t<1}\frac{t-t^{p-1}}{1+t^p}, \qquad p>2.
\]
The scalar function, and earlier bounds comparing it to the numerical index, were studied in [2,3]. We prove new endpoint expansions of this established identity, not a new solution of the full-exponent numerical-index problem.

## Proof
**1. Unique scalar optimum.** Put \(\varepsilon=2/p\in(0,1)\), \(\eta=1-\varepsilon\), \(t=e^{-2z/p}\) with \(z>0\), and \(y=e^{-2z}=t^p\). Elementary rearrangement of the cited exact scalar formula gives
\[
 \frac{t-t^{p-1}}{1+t^p}=\frac{\sinh(\eta z)}{\cosh z}
 =\frac{y^{\varepsilon/2}(1-y^{1-\varepsilon})}{1+y}.
\]
The logarithmic derivative of the middle expression vanishes precisely when \(\tanh(\eta z)\tanh z=\eta\). The left side increases strictly from zero to one on \((0,\infty)\), so it has a unique solution. The scalar objective tends to zero at both ends when \(0<\eta<1\); this stationary point is therefore the unique global maximum. In \(y\), its exact equation is
\[
 \varepsilon(1+y^{2-\varepsilon})=(2-\varepsilon)
       (y+y^{1-\varepsilon}). \tag{1}
\]

**2. The optimizer's singular scale.** Since \(0<y<1\), equation (1) implies
\[
 \left[\frac{\varepsilon}{2(2-\varepsilon)}\right]^{1/(1-\varepsilon)}
 \le y\le \frac{\varepsilon}{2-\varepsilon}.
\]
Consequently \(y=\Theta(\varepsilon)\) and \(\log y=\log\varepsilon+O(1)\); in particular \(\varepsilon|\log y|\to0\). Expand the right side of (1) using \(y^{1-\varepsilon}=y\exp(-\varepsilon\log y)\), and note that \(\varepsilon y^{2-\varepsilon}=O(\varepsilon^3)\). Uniformly for the maximizing solution,
\[
 \varepsilon=4y-2\varepsilon y(1+\log y)
            +O\!\left(\varepsilon^3\log^2(1/\varepsilon)\right).
\]
It follows successively that
\[
 y=\frac{\varepsilon}{4}
   +\frac{\varepsilon^2}{8}\left[1+\log\left(\frac{\varepsilon}{4}\right)\right]
   +O\!\left(\varepsilon^3\log^2(1/\varepsilon)\right),\tag{2}
\]
and
\[
 \log y=\log\left(\frac{\varepsilon}{4}\right)
 +\frac{\varepsilon}{2}\left[1+\log\left(\frac{\varepsilon}{4}\right)\right]
 +O\!\left(\varepsilon^2\log^2(1/\varepsilon)\right).\tag{3}
\]
The estimates are uniform because \(y=\Theta(\varepsilon)\) and the exponential Taylor remainder is bounded by a constant times its first omitted power.

**3. Value expansion, including cancellation.** For \(y=\Theta(\varepsilon)\), expand the exact scalar objective \(y^{\varepsilon/2}(1-y^{1-\varepsilon})/(1+y)\) to second order. The mixed terms \(+\varepsilon y\log y\) and \(-\varepsilon y\log y\) cancel, leaving
\[
 M_p=1+\frac{\varepsilon\log y}{2}-2y
  +\frac{\varepsilon^2\log^2 y}{8}+2y^2
  +O\!\left(\varepsilon^3\log^3(1/\varepsilon)\right).\tag{4}
\]
Substituting (2) and (3) into (4) yields
\[
 M_p=1+\frac{\varepsilon}{2}\log\left(\frac{\varepsilon}{4}\right)
 -\frac{\varepsilon}{2}
 +\frac{\varepsilon^2}{8}\left[\log^2\left(\frac{\varepsilon}{4}\right)+1\right]
 +O\!\left(\varepsilon^3\log^3(1/\varepsilon)\right).
\]
Since \(\varepsilon=2/p\) and \(\log(\varepsilon/4)=-\log(2p)\), this is exactly the claimed expansion for \(n(X_p)=M_p\). Formula (2) gives the announced expansion of \(t_p^p=y\). The conjugate-exponent conclusion uses the standard equality of numerical indices of finite-dimensional spaces and their duals (equivalently the adjoint identification of spatial numerical radii). This completes the proof.

## Verification
The accompanying standalone Python standard-library script `verify.py` independently locates the unique stationary point and separately maximizes the original scalar expression; it also checks the predicted asymptotic errors for several increasing values of \(p\). Run `python verify.py` from the folder containing this document. The finite checks are supplementary: the analytic estimates (1)–(4), coupled with the cited full-exponent identity, are the infinite-parameter proof.

## Relationship to prior work
[1] proves the exact equality of the real planar numerical index and the rotation numerical radius for all exponents. Its hyperbolic optimality equation matches the starting point of the present derivation; it does not state the logarithmic second-order endpoint expansion or the corresponding optimizer boundary layer. [2] and [3] study the scalar numerical radius and estimates for the numerical index without determining the latter's present sharp large-exponent expansion. Thus the result refines a newly completed exact invariant; it is not a claim that the scalar maximization or its stationary equation was previously unknown.

## Limitations
This is an endpoint expansion in real two-dimensional spaces; it does not give finite-exponent closed forms, higher-dimensional indices, or independent proof of the identity imported from [1]. The first-public date records the source's initial arXiv submission rather than the date of this derivation. Literature indexing is not exhaustive: an equivalent endpoint expansion in older, unindexed numerical-radius work remains a priority risk. No independent validation has been performed.

## References
[1] Rafael Chiclana, *The Numerical Index of Two-Dimensional Real ℓp Spaces*, arXiv:2606.01675v1 (first submitted June 1, 2026), https://arxiv.org/abs/2606.01675.

[2] M. Martín and J. Merí, *A note on the numerical index of the Lp space of dimension two*, Linear and Multilinear Algebra, DOI:10.1080/03081080701650739, https://doi.org/10.1080/03081080701650739.

[3] J. Merí and J. Quero, *On the numerical index of the real two-dimensional Lp space*, arXiv:2205.08807, https://arxiv.org/abs/2205.08807.
