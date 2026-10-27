# Two sharp rate contrasts for bimodality in parallel two- and three-reservoir hydrographs

## Finding

In an ideal linear rainfall-routing model with two parallel branches, let the first branch consist of two identical linear reservoirs of rate \(a>0\), and let the second consist of three identical linear reservoirs of rate \(b>0\). Both receive the same instantaneous unit input, apportioned with weights \(w\in(0,1)\) and \(1-w\). The resulting normalized instantaneous unit hydrograph is
\[
 H(t)=w a^2t e^{-at}+(1-w)\frac{b^3t^2}{2}e^{-bt},\qquad t>0.
\]
Put \(k=a/b\). Let \(k_-\) and \(k_+\) be the unique roots, respectively in \((0,1/2)\) and \((1,\infty)\), of
\[
 P(k)=5k^4-24k^3+36k^2-20k+2.
\]
Their numerical values are \(k_-=0.126398265529446\ldots\) and \(k_+=2.599249091139546\ldots\).

**Sharp modality theorem.** For every \(k\in[k_-,k_+]\), the hydrograph has exactly one strict local maximum for every \(0<w<1\). For \(k<k_-\) or \(k>k_+\), define
\[
 I_k=\bigl(\min\{1/k,2\},\max\{1/k,2\}\bigr),
 \quad N_k(x)=k(1-k)x^3+(2k^2-2k-1)x^2+(4-2k)x-2.
\]
The polynomial \(N_k\) has exactly two simple zeros \(x_1<x_2\) in \(I_k\). Define
\[
 Q_k(x)=\frac{e^{(k-1)x}x|2-x|}{2k^2|kx-1|},\qquad
 W_j=\frac{Q_k(x_j)}{1+Q_k(x_j)}\quad(j=1,2).
\]
Then \(H\) has exactly two strict local maxima if and only if
\[
 \min(W_1,W_2)<w<\max(W_1,W_2).
\]
For all remaining positive parameter choices, including equality at either mixing-weight boundary, it has exactly one strict local maximum. Thus two distinct rate-contrast regimes permit peak splitting, separated by a closed interval in which it is impossible at any mixing weight.

An explicit bimodal example is \(a=3,b=1,w=e^2/(36+e^2)\). It has a central stationary trough at dimensionless time \(x=1\), bracketed by two strict local maxima (numerically near \(x=0.548438407\) and \(x=1.705841528\)).

## Assumptions and scope

A linear reservoir with storage coefficient \(1/a\) has normalized impulse response \(a e^{-at}\); a series of \(n\) identical reservoirs produces an Erlang (gamma) response with shape \(n\) and rate \(a\). The two branches here each begin empty and are stimulated at the same time by an ideal impulse, with no travel-time translation, nonlinear routing, finite rainfall duration, reservoir interactions, or intermediate tributaries. We count distinct strict local maxima at \(t>0\), not stationary shoulders. Both branch contributions are strictly positive and integrate to their stated weights; the total hydrograph integrates to one. The result is a mathematical statement about this specified ideal model, not a field-runoff forecast.

## Proof

**1. Dimensionless reduction and where extrema can occur.** With \(x=bt\), the hydrograph per unit dimensionless time is
\[
 F(x)=w k^2x e^{-kx}+(1-w)\frac{x^2}{2}e^{-x},\quad
 F'(x)=w k^2e^{-kx}(1-kx)+(1-w)\frac{x}{2}e^{-x}(2-x).
\]
The individual branch modes are at \(1/k\) and \(2\). Both derivatives are positive before the earlier mode and negative after the later mode. Consequently every stationary point lies in the closed interval joining these modes. When \(k=1/2\), these modes coincide and \(F\) has a unique strict maximum at \(x=2\).

When \(k\ne1/2\), on \(I_k\) the two branch derivatives have opposite signs. The equation \(F'(x)=0\) is equivalent to
\[
 \frac{w}{1-w}=Q_k(x)
 =\frac{e^{(k-1)x}x|2-x|}{2k^2|kx-1|}.
\]
The positive function \(Q_k\) is continuous on \(I_k\). If \(k>1/2\), its endpoint limits are \(+\infty\) and \(0\), in that order; if \(k<1/2\), they are \(0\) and \(+\infty\). Therefore every positive odds level is attained, and \(F\) has at least one maximum.

**2. The cubic governing changes of modality.** Direct logarithmic differentiation gives
\[
 (\log Q_k)'=(k-1)-\frac1{x(kx-1)}-\frac1{2-x}
 =\frac{N_k(x)}{x(kx-1)(2-x)}.
\]
The denominator is strictly positive on \(I_k\) in both possible orderings of the component modes. Expanding the numerator gives exactly
\[
 N_k(x)=k(1-k)x^3+(2k^2-2k-1)x^2+(4-2k)x-2.
\]
Its cubic discriminant factors as
\[
 \operatorname{disc}_xN_k=4(2k-1)^2P(k),\qquad
 P(k)=5k^4-24k^3+36k^2-20k+2.
\]
This identity also follows by inserting the displayed cubic coefficients into the standard cubic discriminant formula, and is checked by exact rational arithmetic in the accompanying program.

**3. Exactly two positive critical contrasts.** On \(0<k<1/2\), substitute \(k=z/[2(1+z)]\) with \(z>0\). Then
\[
 16(1+z)^4P(k)=32-32z-144z^2-112z^3-27z^4.
\]
The coefficients have one sign change and the polynomial goes from positive to negative on the positive half-line; Descartes' rule and continuity show exactly one root \(k_-\) here. On \(1/2<k<1\), put \(k=(1+z)/(2+z)\), giving
\[
 (2+z)^4P(k)=-(z^4+8z^3+30z^2+52z+27)<0.
\]
On \(k>1\), put \(k=1+z\), obtaining \(P(k)=5z^4-4z^3-6z^2-1\). Again there is exactly one positive root, \(k_+\). Hence \(P>0\) exactly for \(k<k_-\) or \(k>k_+\), and \(P\le0\) between the roots.

**4. Locating all physically relevant cubic roots.** For \(0<k<k_-<1/2\), the discriminant is positive, so the cubic has three distinct real zeros. Its coefficients show \(N_k(x)<0\) for \(x\le0\). On \([0,2]\),
\[
 N_k'(2)=2k(1-2k)>0,\qquad N_k''(2)=-2(2k-1)^2<0.
\]
As \(N_k''\) increases with \(x\) in this regime, \(N_k''<0\) throughout \([0,2]\), and \(N_k'\ge N_k'(2)>0\) there. Thus exactly one cubic zero lies in \((0,2)\). For \(x\ge1/k\), \(N_k(1/k)=1/k-2>0\), \(N_k'(1/k)=(k-1)(2k-1)/k>0\), and \(N_k''(1/k)=2(k-2)(2k-1)>0\); the second derivative is increasing thereafter. Hence no zero lies at or above \(1/k\). The other two real zeros must lie in \((2,1/k)=I_k\).

For \(k>k_+>2\), the cubic leading coefficient is negative. It has a negative zero because \(N_k(-\infty)>0>N_k(0)\). On \([0,1/k]\), the second derivative is positive (it decreases with \(x\) and remains positive at \(1/k\)), so the cubic is convex, and its endpoint values \(N_k(0)=-2\), \(N_k(1/k)=1/k-2\) are both negative. Therefore it is negative throughout this interval. On \([2,\infty)\), the second derivative and \(N_k'(2)=-2k(2k-1)\) are negative, so the cubic remains negative. Consequently its two other real zeros lie in \((1/k,2)=I_k\). These location arguments cover the full extreme-contrast regimes without numerical root isolation.

If \(k_-<k<k_+\) and \(k\ne1/2\), the discriminant is negative and the cubic has only one real root. Since \(N_k\) has equal, nonzero signs at both endpoints of \(I_k\), it has no zero in the interval, and \(Q_k\) is strictly monotone. At either critical \(k=k_-\) or \(k=k_+\), the cubic has a double zero within \(I_k\); it touches rather than crosses zero, and \(Q_k\) remains strictly monotone. The special cases \(k=1/2\) and \(k=1\) are directly covered by the branch-mode argument and the logarithmic derivative, respectively.

**5. Counting maxima and the exact mixing-weight window.** For \(k<k_-\), \(Q_k\) increases, then decreases, then increases across its two turning points \(x_1,x_2\). For \(k>k_+\), it decreases, then increases, then decreases. Horizontal levels strictly between its two turning-point heights therefore meet it three times; levels outside meet it once, and either boundary height produces one transverse intersection plus a tangent one. The sign of \(F'\) starts positive and ends negative. Hence three simple intersections give two strict maxima separated by a strict minimum, whereas one intersection gives one strict maximum. At a tangent intersection no additional extremum is created. Converting odds to mixing weights by \(w=Q/(1+Q)\) gives the stated exact necessary-and-sufficient interval, including all its boundaries.

**6. An exact two-peak witness.** For \(k=3\), direct substitution yields
\[
 Q_3(2/3)=\frac{4e^{4/3}}{81},\quad
 Q_3(1)=\frac{e^2}{36},\quad
 Q_3(3/2)=\frac{e^3}{84}.
\]
Since \(e^{2/3}>16/9\) and \(e>7/3\), the middle value is strictly between the other two. Choosing \(w/(1-w)=e^2/36\) produces a stationary point at \(x=1\) in the increasing portion of \(Q_3\), and two additional simple stationary points on its other branches. The middle is a minimum and the outer two are maxima. The inequalities follow, for example, from the first three positive terms of the exponential series.

## Verification

Run `python3 verify.py` in the directory containing the accompanying source. It has no external dependencies. The program checks the cubic-discriminant identity exactly over more distinct rational parameter values than its total polynomial degree permits; reproduces both critical ratios by bisection; verifies the logarithmic-derivative numerator at 1,000 deterministic random interior points; numerically compares the directly differentiated hydrograph against the predicted one-mode or two-mode outcomes for rate ratios on both sides and inside the two thresholds; and checks the exact \(k=3\) witness. All these checks passed. The finite grid comparisons are safeguards against algebraic or implementation mistakes, not a proof for all real parameters. The universal classification is established by the analytical argument above.

## Relationship to prior work

The Nash linear-reservoir cascade and its gamma response are classical. Diskin, Oben-Nyarko and Ince introduced parallel cascades for urban catchments; Parmentier, Dooge and Bruen studied parallel fast/slow runoff elements. These support the hydrograph object, not a claimed new physical mechanism. Došlá (2009), Proposition 6, gives an explicit modality criterion for two gamma components with a **common shape** and different rates, while Proposition 7 treats a **common rate** and different shapes; the general unequal-shape/unequal-rate case is explicitly left untreated in that paper. Its general ratio-of-derivatives characterization motivates the method but does not calculate the present \((2,3)\) two-threshold polynomial or its exact parameter windows. Evin, Merleau and Perreault (2011) fit two-gamma hydrological mixture distributions through Bayesian model comparison, without giving the specified parallel-cascade peak-count diagram in the inspected complete HTML article. The result is therefore an exact specialization of a natural previously unclassified parameter slice, not a claim of novelty for the gamma model or the generic mixture criterion. Possible broader mixture-modality results and inaccessible historical cascade materials leave residual priority risk.

## Limitations

Only a simultaneous impulse with precisely two branches, of integer reservoir depths two and three, is classified. The theorem does not directly imply any classification for unequal within-branch storage coefficients, additional parallel branches, delayed inputs, finite-width storms, nonlinear reservoir relations, flow thresholds, or real rainfall records. Boundary shoulders are stationary points but not additional strict maxima. The polynomial-root values are numerical approximations to algebraically defined constants, not independent exact definitions. Self-review is not independent validation; historical originality has not been independently certified.

## References

1. Nash, J. E., “Systematic determination of unit hydrograph parameters,” *Journal of Geophysical Research* **64** (1959), 111–115. DOI: 10.1029/JZ064i001p00111.
2. Diskin, M. H., Oben-Nyarko, K., and Ince, S., “Parallel Cascades Model for Urban Watersheds,” *Journal of the Hydraulics Division* **104** (1978), 261–276. DOI: 10.1061/JYCEAJ.0004936.
3. Parmentier, B., Dooge, J., and Bruen, M., “Root selection methods in flood analysis,” *Hydrology and Earth System Sciences* **7** (2003), 151–161; public article dated 2003-04-30. DOI: 10.5194/hess-7-151-2003.
4. Došlá, Š., “Conditions for bimodality and multimodality of a mixture of two unimodal densities,” *Kybernetika* **45** (2009), 279–292, especially Propositions 6–7. Persistent identifier: https://dml.cz/handle/10338.dmlcz/140075.
5. Evin, G., Merleau, J., and Perreault, L., “Two-component mixtures of normal, gamma, and Gumbel distributions for hydrological applications,” *Water Resources Research* **47** (2011); public article dated 2011-08-23. DOI: 10.1029/2010WR010266.
6. Yan, B. et al., “The Heterogeneous Discrete Generalized Nash Model for Flood Routing,” *Hydrology and Earth System Sciences Discussions* preprint (2020), DOI: 10.5194/hess-2020-17.
