# Sharp all-orbit Lyapunov floor in a four-branch map without fixed points

## Finding

For \(0<r<1\), set \(H=1+r+r^2\) and suppose
\[
\frac{H}{r^2}<s<1+\frac{H}{r^3}.
\]
For the four-branch discontinuous piecewise-affine map \(T=T_{r,s}\) defined below, every branch-regular forward orbit satisfies the sharp finite-time estimate
\[
\left|(T^n)'(x)\right|\ge (sr^3)^{\lfloor n/4\rfloor}r^{n-4\lfloor n/4\rfloor},\qquad n\ge1.
\]
In particular,
\[
\inf_{x\text{ branch-regular}}\liminf_{n\to\infty}\frac{1}{n}\log\left|(T^n)'(x)\right|=\frac14\log(sr^3).
\]
A strict primitive eight-cycle realizes equality, so the lower bound is optimal even among periodic orbit exponents. Consequently, **uniform exponential derivative expansion along every branch-regular forward orbit holds if and only if \(sr^3>1\)** throughout this two-dimensional parameter chamber.

For the originally studied parameter choice \(r=4/5\), \(s=5\), the exact minimum Lyapunov exponent is \(\frac14\log(64/25)\approx0.235001814622868\); a minimizing cycle in the original, unnormalized coordinate is
\[
\frac1{89}(76,-1845,-1120,-540,-76,1845,1120,540),
\]
with return multiplier \(4096/625\).

## Assumptions and scope

Define \(T:[-s,s]\to[-s,s]\) by
\[
T(x)=\begin{cases}
r(x+1),&-s\le x\le-1,\\
s(x+1),&-1<x<0,\\
s(x-1),&0\le x<1,\\
r(x-1),&1\le x\le s.
\end{cases}
\]
The inner branches have slope \(s\), the outer branches slope \(r\). The state interval is forward invariant; every branch image lies in it. A **branch-regular forward orbit** means \(T^j(x)\notin\{-1,0,1\}\) for every \(j\ge0\), so each finite derivative is defined by the ordinary chain rule. The theorem concerns all such orbits, without genericity, invariant-measure, or typical-initial-condition assumptions. The parameters satisfy strict inequalities: \(0<r<1\) and \(H/r^2<s<1+H/r^3\). The discontinuity at zero and the nondifferentiable branch boundaries are excluded from differentiability claims.

The original physical map has inner slope \(m_2=s\), outer slope \(m_1=r\), scale \(a=b_1/r>0\), and state \(X=ax\), with \(b_2=sa\). Conjugacy by this scale leaves slopes and Lyapunov exponents unchanged.

## Proof

**1. The maximum outer run is three.** Write \(g(z)=r(z-1)\), for \(z\ge1\), and let \(K=r+r^2+r^3=rH\). On either outer branch, while successive states remain outer, their magnitudes evolve by \(g\), without sign reversal. Starting from any outer state of magnitude at most \(s\), four successive outer visits would force \(g^3(s)\ge1\). But
\[
g^3(s)=r^3s-K<r^3+H-K=1
\]
by the strict upper parameter inequality. Therefore every block of four consecutive regular states includes at least one inner state.

**2. Derivative-count bound.** For a regular trajectory of length \(n=4q+j\), \(0\le j\le3\), partition the first \(4q\) states into consecutive four-state blocks. At least \(q\) of the \(n\) factors are inner slope \(s\). If \(I_n\) is the number of inner steps, then \(I_n\ge q\); since \(s>r\),
\[
\left|(T^n)'(x)\right|=s^{I_n}r^{n-I_n}\ge s^q r^{3q+j}=(sr^3)^q r^j.
\]
Taking logarithms, dividing by \(n\), and passing to the lower limit proves the universal floor.

**3. Attaining periodic witness.** Put \(P=sr^3\) and \(u=(P-K)/(1+P)\). The lower inequality \(sr^2>H\) implies \(0<u<1\). Starting at \(u\), the next negative state has magnitude \(z_1=s(1-u)\); its second outer iterate is
\[
g^2(z_1)=r^2s\frac{1+K}{1+P}-r(1+r).
\]
The inequality \(g^2(z_1)>1\) simplifies exactly to \(sr^2>H\): multiply through by \(1+P\), use \(1+K-rH=1\), and cancel positive factors. Hence the first four branch labels are inner–outer–outer–outer, strictly away from branch boundaries. Their affine composition is
\[
T^4(u)=Pu+K-P=-u.
\]
The map is odd at all nonzero states in the relevant strict branches, so the next four steps retrace the sign-reversed branch sequence and \(T^8(u)=u\). Because \(T^4(u)=-u\ne u\), its least period is eight. Exactly two inner and six outer derivatives appear, giving
\[
(T^8)'(u)=(sr^3)^2=P^2,
\qquad \frac18\log|(T^8)'(u)|=\frac14\log P.
\]
This proves attainment and sharpness for the infinite-time all-orbit infimum.

**4. Uniform expansion threshold.** If \(P>1\), put \(\rho=P^{1/4}>1\). As \(\rho>r\), step 2 gives for all \(n=4q+j\) and every branch-regular orbit
\[
\left|(T^n)'(x)\right|\ge\rho^n(r/\rho)^j\ge (r/\rho)^3\rho^n.
\]
Conversely, if \(P\le1\), the period-eight orbit of step 3 has eight-step multiplier at most one, contradicting any globally uniform exponential lower bound \(C\rho^n\), \(C>0\), \(\rho>1\). Thus the criterion is necessary and sufficient.

**5. Exact published-parameter example.** For \(r=4/5,s=5\), one has \(H/r^2=61/16<5<369/64=1+H/r^3\), \(P=64/25\), and \(u=76/445\). Iterating in the normalized coordinate and multiplying by \(a=b_1/r=5\) gives the eight physical coordinates in the finding, which are strictly inside the appropriate branches. Their exact return multiplier is \(P^2=4096/625\).

## Verification

The accompanying `verify.py` checks the map and all branch inequalities with rational arithmetic at six rational parameter pairs, reconstructs the exact eight-cycle and its multiplier for each, samples 150 distinct points in an analytically known neutral interval at \(r=2/5,s=125/8\), and checks the published numerical-coordinate witness. It also checks the four-block frequency restriction on rational trajectories. Run `python3 verify.py` using Python's standard library. The universal theorem follows from the displayed inequalities and affine compositions, not from these finite trials.

For example, at \(r=2/5\), the choices \(s=12\), \(s=125/8\), and \(s=20\) lie in the chamber and give \(P=96/125<1\), \(P=1\), and \(P=32/25>1\), respectively. The periodic witness is attracting, neutral, or repelling accordingly. On the neutral line, the already-known interval of neutral period-eight points is \((0,47/125)\); it is not asserted as a novel finding here.

## Relationship to prior work

García-Grimaldo and Campos-Cantón introduced the fixed-point-free piecewise-linear class and analyzed positivity of Lyapunov exponents and one Devaney-chaotic parameter choice (2021). García-Grimaldo et al. implemented the particular \(r=4/5,s=5\) example and displayed finite-trajectory Lyapunov estimates and numerical bifurcation diagrams (2023). The complete published 2023 article was examined, including its defining piecewise map and its Lyapunov section. It does not give an all-initial-condition sharp exponential derivative bound, an optimal minimizing exponent over all regular trajectories, or this exact global expansion threshold. Earlier explicit one-inner/three-outer periodic itinerary calculations already establish the cycle witness and, at criticality, neutral periodic intervals; **those periodic-orbit existence statements are not claimed as new**. The distinct contribution here is the all-orbit frequency obstruction coupled with matching sharpness and the resulting necessary-and-sufficient uniform expansion classification. The 2021 article's complete text could not be inspected; its abstract and first-page preview are available and leave publication-priority uncertainty.

## Limitations

All derivative assertions exclude orbits visiting \(-1,0,1\), where the ordinary derivative is not defined. This is a sharp bound for a specified open chamber, not a complete parameter-plane classification. Positive derivative growth is not a claim of cryptographic security, topological mixing, or a particular invariant density. The periodic witness and its neutral interval may be covered by prior itinerary classifications; only the universal lower bound and global-in-chamber criterion are proposed as the new mathematical result. The earliest verified public map-family date is October 26, 2021. Originality remains subject to a full-text check of the 2021 paper and other unindexed sources; no independent external mathematical audit was performed.

## References

1. C. García-Grimaldo and E. Campos-Cantón, *Chaotic Features of a Class of Discrete Maps without Fixed Points*, International Journal of Bifurcation and Chaos **31** (2021), 2150200, DOI: `10.1142/S021812742150200X` (public date 2021-10-26).
2. C. García-Grimaldo, C. F. Bermudez-Marquez, E. Tlelo-Cuautle, and E. Campos-Cantón, *FPGA Implementation of a Chaotic Map with No Fixed Point*, Electronics **12** (2023), 444, DOI: `10.3390/electronics12020444` (published 2023-01-14).
