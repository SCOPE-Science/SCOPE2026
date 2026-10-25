# A sharp positivity dichotomy for the fourth-order Gauss step on three-site weighted diffusion networks

## Finding

**Theorem.** Consider every connected undirected three-vertex network with nonnegative symmetric conductances \(a=w_{12}\), \(b=w_{13}\), and \(c=w_{23}\). Put \(s=a+b+c\) and \(\tau=ab+ac+bc>0\). For the combinatorial weighted Laplacian \(L\), the completed two-stage, fourth-order Gauss–Legendre (diagonal \([2/2]\) Padé) diffusion map is
\[
T(h)=(12I-6hL+h^2L^2)(12I+6hL+h^2L^2)^{-1},\qquad h\ge0.
\]
It is symmetric, positive definite, and doubly stochastic for all finite \(h\ge0\). For each distinct pair \(i,j\), writing \(w=w_{ij}\),
\[
T_{ij}(h)=\frac{4h[12w+6\tau h+\tau(2s-3w)h^2]}{48+48sh+(16s^2+12\tau)h^2+12s\tau h^3+3\tau^2h^4}.
\]
Consequently there is an exact dichotomy:

* If \(3w_{ij}\le2s\) for **all** three edges (including edges of zero conductance), \(T(h)\) is strictly entrywise positive for every \(h>0\). Thus positivity is unconditional.
* If an edge \(ij\) has \(\delta=3w_{ij}-2s>0\), it is the **unique** such edge and the sharp positivity horizon is
\[
H=\frac{3+\sqrt{9+12w_{ij}\delta/\tau}}{\delta}.
\]
Precisely \(T(h)\ge0\) entrywise for \(0\le h\le H\). At \(H\) only the critical off-diagonal pair \((i,j),(j,i)\) vanishes, while all other entries are strictly positive. For every \(h>H\), these two entries are strictly negative, so positivity never returns.

The distinction has an equivalent **Green-kernel criterion**: the preceding unconditional case holds exactly when all off-diagonal entries of the Moore–Penrose Laplacian pseudoinverse \(L^+\) are nonpositive. Indeed
\[
L^+_{ij}=\frac{3w_{ij}-2s}{9\tau}\quad(i\ne j),\qquad
T(h)=I-\frac{12}{h}L^++O(h^{-2})\quad(h\to\infty).
\]
For positive connected undirected networks with just two vertices this Gauss step is always positivity preserving for every \(h\ge0\). Therefore three vertices are the **minimal symmetric weighted-network dimension** admitting finite-step positivity loss despite unconditional spectral stability of the fourth-order method.

For a weighted three-vertex path having consecutive edge weights \(a>0\) and \(b>0\), unconditional positivity holds exactly when \(\max\{a,b\}\le2\min\{a,b\}\). At weights \(a=3,b=1\), the sharp threshold is \(H=3+\sqrt{21}\). Keeping the two weaker edge weights fixed with positive sum \(t\), and letting one edge weight \(a\to\infty\), the sharp finite horizon obeys \(H\sim\sqrt{12/(at)}\).

## Assumptions and scope

All statements use exact real arithmetic and the completed end-step matrix, not positivity of internal stages. The graph has vertices \(1,2,3\), symmetric conductances \(a,b,c\ge0\), and at least two positive conductances. This is precisely the condition \(\tau>0\) for connectivity. The weighted combinatorial Laplacian is
\[
L=\begin{pmatrix}
a+b&-a&-b\\
-a&a+c&-c\\
-b&-c&b+c
\end{pmatrix}.
\]
Time \(h\) is a real, nonnegative timestep. “Nonnegative” and “positive” mean entrywise for a matrix. Spectral stability uses the ordinary Euclidean operator norm. The positive spectrum is the pair of roots of \(\lambda^2-2s\lambda+3\tau=0\), counted with multiplicity; both roots are positive because \(s,\tau>0\) and \(s^2\ge3\tau\).

## Proof

**Exact rational reduction.** The Laplacian eigenvalues are \(0\) and the roots of \(\lambda^2-2s\lambda+3\tau=0\). The Cayley–Hamilton identity therefore reads
\[
L^3-2sL^2+3\tau L=0.
\]
Define
\[
\begin{aligned}
D&=48+48sh+(16s^2+12\tau)h^2+12s\tau h^3+3\tau^2h^4,\\
U&=-48h-48sh^2+(12\tau-16s^2)h^3,\\
V&=24h^2+8sh^3.
\end{aligned}
\]
Direct polynomial multiplication, reduced using the displayed Cayley–Hamilton relation, establishes
\[
(DI+UL+VL^2)(12I+6hL+h^2L^2)=D(12I-6hL+h^2L^2).
\]
All coefficients in \(D\) are positive apart from the positive constant, so \(D(h)>0\) for every \(h\ge0\). Moreover \(12I+6hL+h^2L^2\) is positive definite and invertible: at each Laplacian eigenvalue \(\lambda\ge0\) its scalar eigenvalue equals \(12+6h\lambda+h^2\lambda^2>0\). Hence
\[
T(h)=I+\frac UD L+\frac VD L^2.
\]
A direct Laplacian multiplication gives \((L^2)_{ij}=\tau-2s w_{ij}\) for distinct \(i,j\). As \(L_{ij}=-w_{ij}\), the off-diagonal expression in the theorem follows exactly from \(-Uw_{ij}+V(\tau-2sw_{ij})\), after collecting coefficients.

**Diagonal and mass properties.** Define the scalar stability rational function
\[
r(z)=\frac{z^2-6z+12}{z^2+6z+12}.
\]
For every \(z\ge0\), its numerator equals \((z-3)^2+3>0\), and the denominator exceeds or equals the numerator by \(12z\). Thus \(0<r(z)\le1\), including \(r(0)=1\). The spectral theorem yields \(0<T(h)\le I\) in the positive-definite order. In particular all diagonal entries are strictly positive and \(\|T(h)\|_2=1\). Since \(L\mathbf1=0\) and \(T(h)\) is symmetric, \(T(h)\mathbf1=\mathbf1\) and \(\mathbf1^{\mathsf T}T(h)=\mathbf1^{\mathsf T}\).

**Complete off-diagonal sign classification.** For each possible edge conductance \(w\ge0\), the sign of \(T_{ij}(h)\) at \(h>0\) is the sign of
\[
q_w(h)=12w+6\tau h+\tau(2s-3w)h^2.
\]
If \(3w\le2s\), all terms are nonnegative and the middle term is strictly positive; hence \(q_w(h)>0\) for every \(h>0\), even if \(w=0\). If \(\delta=3w-2s>0\), then \(w>0\) and \(q_w(h)=12w+6\tau h-\tau\delta h^2\) has exactly one positive root: the quadratic has negative leading coefficient, a positive intercept, and one negative root. The positive quadratic root is the claimed \(H\). The sign is strictly positive below \(H\), zero at \(H\), and strictly negative thereafter. At most one edge can satisfy \(3w>2s\), since two such weights would have sum greater than \(4s/3>s\), an impossibility. Combining all entry types with positive diagonals gives the exact iff and no-reentry conclusions.

**Green-kernel interpretation and two-site minimality.** Set \(J=\mathbf1\mathbf1^{\mathsf T}\). An exact pseudoinverse is
\[
L^+=\frac{2s(I-J/3)-L}{3\tau},
\]
verified by \(LL^+=I-J/3\) and \(L^+\mathbf1=0\). Its off-diagonals are \((3w-2s)/(9\tau)\), proving the Green-kernel criterion. For positive eigenvalues, \(r(h\lambda)=1-12/(h\lambda)+O(h^{-2})\); the zero-eigenvalue projector stays fixed, yielding the asymptotic matrix formula. For two vertices joined by positive conductance \(w\), the nontrivial Laplacian eigenvalue is \(2w\), and the only off-diagonal step entry is \((1-r(2wh))/2>0\) for each finite \(h>0\). For a three-site path with weights \(a,b,0\), the exceptional condition reduces to \(\max\{a,b\}>2\min\{a,b\}\). Substituting \(a=3,b=1\) gives \(q_a(h)=-3(h^2-6h-12)\) and \(H=3+\sqrt{21}\). Finally writing \(w=a\), \(s=a+t\), and \(\tau=at+u\) for fixed \(t>0,u\ge0\), the positive-root formula yields \(H\sim\sqrt{12/(at)}\) as \(a\to\infty\).

## Verification

The accompanying standalone `artifacts/verify_gauss_three.py` checks the cubic Laplacian identity, the exact matrix quotient and all pairwise numerator formulas symbolically; independently computes \(L^+\); and compares 672 exact-rational direct matrix inversions with the closed forms across 112 connected conductance triples and six timesteps. It also checks stochasticity, symmetry, diagonal positivity, the weighted-path threshold, and nearby signs. Running the file with Python and the pinned SymPy dependency prints a deterministic `VERIFY_OK` confirmation. These finite tests only corroborate the exact symbolic identities and proof; they are not used to infer the result for all conductances or all timesteps.

## Relationship to prior work

The strong-stability-preserving theory of Gottlieb, Shu and Tadmor (2001) provides the historical numerical-integration motivation, but is concerned with method-wide stability/positivity under prescribed timestep restrictions, rather than the completed Gauss map on every weighted three-site diffusion network. Horváth (1998) treats general Runge–Kutta positivity and absolute-monotonicity radii over broad positive ODE classes; its broad order-barrier statements do not give this fixed-graph exact-weight threshold. Zappavigna, Colaneri, Kirkland and Shorten (2012) establish failure mechanisms for Padé approximants on larger Metzler systems and present general sufficient step-size conditions, but not this sharp symmetric three-site Green-kernel characterization. An accessible published eight-state Markov-chain result proves arbitrary-small-step failure is first possible at eight states for general (possibly directed) generators, whereas the present three-state symmetric construction concerns **some finite** step and its full positivity interval; the statements are logically compatible and do not imply each other. Existing unconditional unweighted complete-multipartite special cases do not determine the unequal-conductance threshold.

## Limitations

This classification concerns exactly three sites, nonnegative symmetric edge weights and the completed two-stage Gauss–Legendre step; it makes no assertion about arbitrary graph sizes, directed or nonlinear systems, positivity of stage values, rounding error, spatial discretization error, or improved accuracy. The finite-step failure on three sites does not contradict the published minimum of eight states for failure at **arbitrarily small** steps. The cited primary literature and public mathematical-search records did not reveal an equivalent classification, but a specialized unindexed or inaccessible source could exist; absence from those searches is not a proof of novelty. Independent external mathematical review has not been performed.

## References

1. S. Gottlieb, C.-W. Shu, and E. Tadmor, “Strong Stability-Preserving High-Order Time Discretization Methods,” *SIAM Review* **43** (2001), 89–112; electronic first appearance 2001-02-02. https://doi.org/10.1137/S003614450036757X
2. Z. Horváth, “Positivity of Runge-Kutta and diagonally split Runge-Kutta methods,” *Applied Numerical Mathematics* **28** (1998), 309–326. https://doi.org/10.1016/S0168-9274(98)00050-6
3. A. Zappavigna, P. Colaneri, S. Kirkland, and R. Shorten, “Essentially negative news about positive systems,” *Linear Algebra and its Applications* **436** (2012), 3425–3442. https://doi.org/10.1016/j.laa.2011.12.021
4. L. Lóczi and D. I. Ketcheson, “Rational functions with maximal radius of absolute monotonicity,” *LMS Journal of Computation and Mathematics* **17** (2014), 159–205. https://doi.org/10.1112/S1461157013000326
