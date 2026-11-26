# Independent mathematical audit

## correctness

PASS

The primary Eqs. (2.1)–(2.4) and §3.2 give the stated density on [0,2π), α,β>0, and the stationary point in Eq. (3.3), but do not check admissibility. Put x=2παβ and r(x)=x/(exp(x)−1). Up to its positive prefactor the derivative has sign 1−α−r(x)−αβθ, a strictly decreasing affine function of θ. It is negative everywhere when α≥1. For 0<α<1, r(x) is strictly decreasing from 1 to 0 (its derivative numerator is exp(x)(1−x)−1<0), so r(x)=1−α has exactly one positive solution. Setting c=1−α turns the equation into −(x+c) exp(−x−c)=−c exp(−c); W_0 gives x=0 for the rearranged equation, while W_{−1} gives the unique positive root and β_c after division by 2πα. The sign at θ=2π is strictly negative because x+r(x)=x/(1−exp(−x))>1. Hence every positive stationary point is interior; at equality only the right derivative at the seam vanishes and the density is strictly decreasing thereafter. In each seam case the specified pointwise wrapped version is maximized at 0, not at an unavailable point near 2π. Indeed the jump g(0)−g(2π−)=C(1−exp(−x))>0. The positive prefactor and normalization also follow from the geometric wrapping of a normalized LE parent. Independent high-precision root solving, numerical integration and evaluation reproduced β_c(1/2)=0.399934475015558622…, θ0(1/2,1/5)=−2.185249661340380482…, θ0(1/2,1/2)=0.351076603008782184… and θ0(2,1)=−0.500021911694667218…, with unit integrated mass in those examples. The global result follows from the analytic inequalities, not a derivative grid. The verdict is for the mode of the stated density version, not for arbitrary changes of a density at a point.

## originality

PASS

The supported distinct result is the exact joint two-parameter domain of an interior WRLE mode and the seam classification, not the density, the derivative, the algebraic stationary point or the standard Lambert W inversion alone. No exact classification was identified in the inspected sources. Qualify the frozen literature wording: classical wrapped Lindley and wrapped new-XLindley are distinct one-parameter models as families, but they are exact slices of WRLE, not disjoint families. The uncertain literature priority of those slices is not attributed to the frozen finding.

## value

PASS

The stationary point reported as a mode can be outside the angular support even at ordinary plotted parameter values. The corrected criterion resolves an entire change in shape within the fitted model: it distinguishes monotone decay from a unique interior peak and gives the exact regime where the peak or seam must be reported. The value is the joint boundary classification and correction to interpretation, not routine differentiation or merely producing a negative stationary point. It does not change the WRLE density or any fitted analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
