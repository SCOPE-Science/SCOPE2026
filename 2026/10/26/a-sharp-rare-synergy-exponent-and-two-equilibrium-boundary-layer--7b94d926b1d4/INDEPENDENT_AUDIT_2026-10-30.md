# Independent mathematical audit

## correctness

PASS

The source payoff equation after fixing r/G=κ gives F_n(x)=κ[c((1+δx)/L)^n+(1−cL^(-n))(1−δx)^n]−1. For n≥2 its second derivative is strictly positive on [0,1], while F_n(0)=κ−1>0 and any fixed y in (0,min((L−1)/δ,1)) has F_n(y)→−1, so there is exactly one low crossing and at most one upper crossing, controlled by sign F_n(1). Endpoint: L<1+δ gives +∞, L>1+δ gives −1, equality gives κc−1, except c=1/κ where remaining κ(1−p_n)(1−δ)^n>0. Uniform compact-rescaled limits F_n(u/n)→κe^(−δu)−1 and F_n(x_L+z/n)→κc e^(δz/L)−1 yield low and macroscopic roots. At L=1+δ,c>1/κ, F_n(1−z/n)→κc e^(−δ z/(1+δ))−1; at exact c=1/κ, F_n(1−C(1−δ)^n/n)/(1−δ)^n→κ−δC/(1+δ), giving the finer C*=κ(1+δ)/δ by sign bracketing. The vector field x(1−x)tanh(sF_n/2) has the asserted stability signs. Independent exact-Fraction checks for n=96 δ=2/5 κ=3/2 verified the lower root between 0.01053 and 0.01055 and upper between 0.48735 and 0.48736, along with subcritical/supercritical/critical endpoint signs. Finite tests are illustrative; the limit proof is analytic.

## originality

PASS

Existing exact Zhu et al. 2024 equations provide the finite-n model and endpoint criterion, and Peña–Nöldeke cover general group-size shifts; neither inspected primary source supplies exponentially rare synergy p_n=cL^(−n) with exact L=1+δ phase transition and two distinct critical upper-root scales. Their recognized finite-n results are not claimed new.

## value

PASS

This model directly asks whether cooperation can persist when synergistic group interactions become exponentially rare as group size grows. The exact rarity exponent L=1+δ, nonzero limiting full-cooperation basin for L below threshold, and two sharply different vanishing boundary layers at threshold characterize a meaningful singular phase transition beyond fixed-n bistability. The critical amplitude layer is not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
