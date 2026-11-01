# Joint endpoint and deficit laws for near-diameter chords of round cylinders

## Finding

For each integer \(d\ge3\) and each \(R,H>0\), consider the Euclidean cylinder \(K=B_2^{d-1}(R)\times[-H/2,H/2]\). An affine line is sampled from Euclidean-motion-invariant measure, conditioned to intersect \(K\), and its intersection length is \(L\). Set \(k=d-2\), \(D=\sqrt{4R^2+H^2}\), \(\beta=(d+2)/2\), \(\kappa_m=\pi^{m/2}/\Gamma(1+m/2)\), and
\[
A_{d,R,H}=\frac{8(k+1)\kappa_k2^{k/2}}{(k+2)(k+4)\kappa_{k+1}[2R+(k+1)H]D^{k/2+1}},
\quad w_C=\frac{H}{2R},\quad w_S=\frac{2R}{H}.
\]
Classify each of the two chord endpoints as a planar end-**cap** (type \(C\)) or a curved **side** (type \(S\)), ignoring their common rim of measure zero. Distinguish top and bottom by their axial coordinate. For every ordered type pair \((i,j)\in\{C,S\}^2\),
\[
\Pr\{L>D-\varepsilon,\ \mathrm{top}=i,\ \mathrm{bottom}=j\}
=A_{d,R,H}w_iw_j\varepsilon^{\beta}+o(\varepsilon^{\beta}).\tag{1}
\]
In particular, \(\Pr\{L>D-\varepsilon\}\sim A_{d,R,H}(w_C+w_S)^2\varepsilon^\beta\). Conditional on the rare event, the top and bottom types converge to *independent* Bernoulli variables with cap probability
\[
p_C=\frac{w_C}{w_C+w_S}=\frac{H^2}{H^2+4R^2}=\frac{H^2}{D^2}.\tag{2}
\]
Thus the limiting cap fraction determines the height-to-diameter ratio \(H/(2R)=\sqrt{p_C/(1-p_C)}\).

There is a joint limiting law beyond endpoint types. Let \(s_+\) and \(s_-\) be the inward distance from the corresponding top and bottom rim, measured *radially* for a cap endpoint and *axially* for a side endpoint. Write \(a_C=2R/D\) and \(a_S=H/D\). Let \(\phi\in[0,\pi]\) be the angular distance between the horizontal directions at the top endpoint and the *negative* horizontal direction at the bottom endpoint. On the event with endpoint types \((i,j)\), put
\[
X=\frac{a_i s_+}{\varepsilon},\quad Y=\frac{a_j s_-}{\varepsilon},\quad
Z=\frac{R^2\phi^2}{2D\varepsilon},\quad T=1-X-Y-Z.
\]
Conditional on both \(L>D-\varepsilon\) and the fixed type pair \((i,j)\), \((X,Y,Z,T)\) converges in distribution to \(\mathrm{Dirichlet}(1,1,k/2,1)\), the *same* law for all four type pairs. The top/bottom type limit and the scaled deficit limit therefore decouple. All assertions hold separately for every fixed finite dimension and positive cylinder aspect ratio.

## Assumptions and scope

Here \(B_2^{d-1}(R)\) is the closed Euclidean radius-\(R\) ball in \(\mathbb R^{d-1}\). The directional measure is ordinary spherical area \(d\sigma(u)\) on \(S^{d-1}\), and the displacement measure is \((d-1)\)-dimensional Lebesgue \(dp\) in \(u^\perp\); normalizing their restriction to lines hitting \(K\) gives the invariant random-line law. For almost every line the two boundary endpoints lie on the relative interiors of smooth faces. A cylinder is smooth on those interiors but has a non-smooth rim, precisely where the diameter pairs live. The probability of chords with an endpoint exactly on the rim is zero. A "top" endpoint means the chord endpoint in the upper near-diametral neighborhood, not the endpoint with greater coordinate for arbitrary short chords; the event in (1) is sufficiently close to the diameter that this distinction is unambiguous. The asymptotics keep \(d,R,H\) fixed while \(\varepsilon\downarrow0\).

## Proof

**Diameter localization.** For any \(x=(x_h,z_x)\), \(y=(y_h,z_y)\) in \(K\), \(\|x-y\|^2\le(2R)^2+H^2\). Equality holds if and only if \(x=(R\omega,H/2)\) and \(y=(-R\omega,-H/2)\), or the reverse, for \(\omega\in S^{d-2}\). By compactness, every sequence of chords with length tending to \(D\) has both endpoints approaching one of these diametral pairs, uniformly in the choice of direction. After exchanging the two endpoint labels and orienting the line toward the top end, all sufficiently long chords thus lie near the indicated top/bottom rim manifold.

**Four local face charts.** Fix a type pair \((i,j)\). Choose \(\omega_+,\omega_-\in S^k\) with \(\omega_-\) close to \(-\omega_+\), define the angular gap \(\phi=\arccos(-\omega_+\cdot\omega_-)\), and introduce nonnegative inward parameters \(s,t\). For a top cap endpoint take \(x=((R-s)\omega_+,H/2)\); for top side take \(x=(R\omega_+,H/2-s)\). For the bottom cap use \(y=((R-t)\omega_-,-H/2)\); for bottom side use \(y=(R\omega_-,-H/2+t)\). All these charts parametrize disjoint patches except boundaries of zero area. Direct expansion of the exact Euclidean distance gives, uniformly over the compact rim manifold,
\[
D-\|x-y\|=a_i s+a_jt+\frac{R^2}{2D}\phi^2
 +O\bigl(s^2+t^2+(s+t)\phi^2+\phi^4\bigr).\tag{3}
\]
More intrinsically, the exact squared distance decomposes into a nonnegative axial shortage, nonnegative radial shortage, and \(2r_xr_y(1-\cos\phi)\), so sufficiently small length deficit forces \(s,t=O(\varepsilon)\) and \(\phi=O(\sqrt\varepsilon)\). This provides both an absolute dominating neighborhood and a uniform scaled error \(o(\varepsilon)\) in (3); it avoids assuming any Taylor approximation for far-away boundary points.

**Invariant-line Jacobian.** For smooth boundary points of any convex body, the oriented boundary-pair Blaschke–Petkantschin change of variables reads
\[
d\sigma(u)\,dp=\frac{|n_x\cdot u|\,|n_y\cdot u|}{\|x-y\|^{d-1}}\,dS(x)dS(y),\quad u=\frac{x-y}{\|x-y\|}.\tag{4}
\]
This follows directly by differentiating the impact parameter map \(p=x-(x\cdot u)u\) in the two transversal boundary coordinates; for each directed chord, the projection of the boundary area element onto \(u^\perp\) produces \(|n\cdot u|\) at either endpoint, and differentiating the outgoing ray direction gives the inverse \(\|x-y\|^{d-1}\) factor. Equation (4) holds on the cap and cylindrical side charts; the rim itself has zero measure. At a diametral pair, these flux factors tend to \(q_C=H/D\) for a cap and \(q_S=2R/D\) for a side, so
\[
\frac{q_i}{a_i}=w_i\quad(i\in\{C,S\}).\tag{5}
\]
Each boundary chart has local surface measure \((R+O(s))^k ds\,d\sigma_k(\omega_+)\) at a cap and \(R^k ds\,d\sigma_k(\omega_+)\) at a side. Around \(-\omega_+\), replace \(\omega_-\) by the exponential tangent coordinate \(v\in\mathbb R^k\); then \(\phi=\|v\|\), with Jacobian \(1+O(\|v\|^2)\). The two line orientations contribute a factor \(2\).

**Elementary integral.** Set \(b=R^2/(2D)\). For every type pair the leading unnormalized directed-line mass equals
\[
2|S^k|R^{2k}D^{-(k+1)}q_iq_j
\int_{s,t\ge0,\,v\in\mathbb R^k}
\mathbf1\{a_is+a_jt+b\|v\|^2<\varepsilon\}\,ds\,dt\,dv.\tag{6}
\]
Integrating first over \((s,t)\) and then over the tangent ball gives the exact identity
\[
\int\mathbf1\{a_is+a_jt+b\|v\|^2<\varepsilon\}\,ds\,dt\,dv
=\frac{4\kappa_k}{(k+2)(k+4)}\frac{b^{-k/2}}{a_ia_j}
\varepsilon^{2+k/2}.\tag{7}
\]
The error from (3) and all Jacobian factors is lower order, by the compactness domination above and the rescaling \((s,t,v)=(\varepsilon s',\varepsilon t',\sqrt\varepsilon v')\).

**Probability normalization.** Cauchy's projection identity gives the total invariant-line mass \(\int_{S^{d-1}}\operatorname{vol}_{d-1}(K|u^\perp)d\sigma(u)=\kappa_{d-1}S(K)\). The cylinder surface area is \(S(K)=\kappa_{k+1}R^k[2R+(k+1)H]\), and \(|S^k|=(k+1)\kappa_{k+1}\). Divide (6)–(7) by \(\kappa_{k+1}S(K)\), substitute (5), and simplify to obtain exactly \(A_{d,R,H}w_iw_j\) in (1). Summing the four ordered type pairs proves (2) and the independent Bernoulli limit.

**Scaled joint distribution.** Let \(r=a_is/\varepsilon\), \(r'=a_jt/\varepsilon\), \(z=b\|v\|^2/\varepsilon\). The limiting scaled region is the simplex \(\{r,r',z\ge0:\ r+r'+z<1\}\), and integration over tangent angular directions gives measure proportional to \(z^{k/2-1}dr\,dr'\,dz\). Adding the slack \(T=1-r-r'-z\) identifies the four Dirichlet parameters as \((1,1,k/2,1)\). All type-specific factors are multiplicative constants, hence cancel under conditional normalization. This proves the final joint assertion.

## Verification

The accompanying Python program `verification/verify_cylinder.py` computes the claimed four type-pair coefficients directly and compares them with finite-\(\varepsilon\) boundary integrals using the **exact endpoint separation**, surface Jacobians and fluxes, not the quadratic approximation. It uses reproducible scrambled Sobol quadrature and checks dimensions \(3,4,5\), two aspect ratios and two deficit scales. It reports `PASS` for all cases. At \(d=4,R=1,H=2\), summing the four ordered pair coefficients gives the exact rational leading coefficient \(3/32\); the program separately checks this identity. These computations validate constants and geometry numerically, not the infinite-limit theorem; the proof above supplies that limit.

## Relationship to prior work

Kellerer's 1971 full-text paper established the complete *univariate* chord-length distribution of ordinary three-dimensional cylinders by reducing to the planar-section chord law (especially equations (47), (50), (53) and (56)). Consequently the present **unconditioned three-dimensional scalar tail is not asserted to be independent of, or logically beyond, that prior distribution**. Mäder's 1980 paper also treats univariate random chord lengths for circular cylinders. The actual claim here is the geometric *joint* extreme event: its four top/bottom boundary-type masses, the asymptotic independence and explicit cap fraction, and the type-independent conditional Dirichlet law in every dimension \(d\ge3\). A one-dimensional length distribution does not determine the boundary-type marked law, although classical invariant-line techniques make the joint calculations possible. Vlasov's signed-chord paper is consulted for the distinction between random-line sampling conventions, not for a new cylinder-specific theorem.

## Limitations

The asymptotics are for fixed \(d\ge3\) and fixed positive \(R,H\), not uniform when \(R/H\) vanishes or diverges or as dimension grows. The statement uses the invariant-line convention exclusively, and the cap and side labels are defined only off the measure-zero seams. No independent expert audit has been performed. Mäder's 1980 full text could not be inspected through lawful access; historical-priority uncertainty therefore remains for possibly implicit marked endpoint distributions. Older univariate laws have not been renamed as original results. The exact dates of the original 1971 and 1980 articles' first public appearance were not established; the recorded date 2007-11-29 refers to the exactly dated methodological arXiv v1 source, not the inception of cylinder chord studies.

## References

1. A. M. Kellerer, *Considerations on the Random Traversal of Convex Bodies and Solutions for General Cylinders*, Radiation Research **47** (1971), 359–376, DOI:10.2307/3573243. Full text inspected: https://websites.umich.edu/~nersb590/CourseLibrary/Kellerer.pdf (especially equations (47), (50), (53), (56)).
2. U. Mäder, *Chord Length Distributions for Circular Cylinders*, Radiation Research **82** (1980), 454–466, DOI:10.2307/3575312. Bibliographic record and abstract inspected; full text unavailable.
3. A. Yu. Vlasov, *Signed Chord Length Distribution. I*, arXiv:0711.4734v1, publicly posted 2007-11-29, https://arxiv.org/abs/0711.4734. Public HTML/full text inspected; different signed distribution and sampling focus.
