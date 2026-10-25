# Three even geodesic-distance moments reconstruct every flat circular cylinder

## Finding
For every positive circumference \(C\) and height \(H\), the first three consecutive even moments of the intrinsic distance between two independent uniform points on the *lateral surface* of the flat circular cylinder determine both parameters. The first two even moments are insufficient on a complete, explicit open range of normalized fourth moments. Thus three is the sharp cutoff for this natural sequence of global statistics.

Define \(M_{2j}=\mathbb E[D^{2j}]\), \(s=M_2>0\), and \(\rho=M_4/s^2\). The complete fiber cardinalities for given \((M_2,M_4)\) are
\[
\#\{(C,H):\text{these moments are attained}\}=
\begin{cases}
0,&\rho<83/55\ \text{or}\ \rho\ge12/5,\\
1,&\rho=83/55\ \text{or}\ 9/5\le\rho<12/5,\\
2,&83/55<\rho<9/5.
\end{cases}
\]
Here \(C,H\) must both be strictly positive, so limiting degenerate surfaces are excluded. The third even moment distinguishes every pair in the two-solution range.

As an exact collision, two cylinders whose squared half-circumference and squared height are respectively \((2,2)\) and \((20/11,26/11)\) both satisfy \(M_2=1\) and \(M_4=68/45\), but their sixth moments are \(58/21\) and \(77950/27951\), differing by \(752/27951\).

## Assumptions and scope
Let \(X_{C,H}=S^1(C)\times[0,H]\), where \(S^1(C)\) is a circle of circumference \(C>0\). Equip the product with its intrinsic Riemannian length metric \(ds^2=du^2+dv^2\), using the circle coordinate modulo \(C\), and normalized area measure. The boundary consists only of the two rim circles; the disks inside the rims are not part of the metric surface. The two sampled points are independent. A closed-form inverse reconstructs the positive geometric parameters, not merely a dimensionless shape ratio.

## Proof
**1. Exact probability model.** The shortest circular arc separation \(U\) of two independent uniform circle coordinates is uniform on \([0,a]\), where \(a=C/2\). The absolute difference \(V\) of two independent uniform height coordinates has density \(2(H-v)/H^2\) on \([0,H]\), and \(U,V\) are independent. Geodesics lift to straight segments in the Euclidean strip \(\mathbb R\times[0,H]\); the segment joining endpoints of a shortest angular lift stays inside the strip. Therefore
\[
D^2=U^2+V^2.
\]
Put \(x=a^2>0\) and \(y=H^2>0\). Direct integration gives, for every nonnegative integer \(j\),
\[
\mathbb E[U^{2j}]=\frac{x^j}{2j+1},\qquad
\mathbb E[V^{2j}]=\frac{y^j}{(j+1)(2j+1)}.
\]
Independence and the binomial theorem yield
\[
\begin{aligned}
M_2&=\frac{x}{3}+\frac{y}{6},\\
M_4&=\frac{x^2}{5}+\frac{xy}{9}+\frac{y^2}{15},\\
M_6&=\frac{x^3}{7}+\frac{x^2y}{10}+\frac{xy^2}{15}+\frac{y^3}{28}.
\end{aligned}
\]

**2. The exact two-moment fiber.** Set \(s=M_2\) and \(t=y/s\). Since \(x=3s-st/2>0\) and \(y=st>0\), admissibility is equivalent to \(s>0\) and \(0<t<6\). The fourth moment becomes
\[
Q_4(t):=\frac{M_4}{s^2}
=\frac{324-48t+11t^2}{180}
=\frac{83}{55}+\frac{11}{180}\left(t-\frac{24}{11}\right)^2.
\]
The parabola has its unique minimum at \(t_0=24/11\). The omitted endpoint values are \(Q_4(0)=9/5\) and \(Q_4(6)=12/5\), and the second intersection with level \(9/5\) is \(t=48/11\). A horizontal line therefore has exactly the stated numbers of roots in \((0,6)\). For every admissible root the inverse parameters are
\[
H=\sqrt{st},\qquad C=2\sqrt{s\left(3-t/2\right)}.
\]
The only possible distinct two-moment companion of \(t\) is \(t'=48/11-t\).

**3. Sixth-moment separation.** Substitution gives
\[
Q_6(t):=\frac{M_6}{s^3}
=\frac{1620-432t+93t^2+4t^3}{420}.
\]
The reflected difference factors *exactly* as
\[
Q_6(t)-Q_6(48/11-t)
=\frac{2(11t-24)(121t^2-528t+1512)}{139755}.
\]
The quadratic factor is \(121(t-24/11)^2+936>0\) for every real \(t\). Consequently equality of the sixth moment for the two quadratic roots forces \(t=24/11\), where the roots coincide. Hence \(M_2,M_4,M_6\) identify \(t\), then \(H,C\), uniquely on the entire positive parameter domain. The explicit collision in the Finding paragraph proves minimality of the first three moments in this consecutive even-moment sequence. This completes the proof.

## Verification
The supplied standard-library checker `verify_moments.py` uses exact rational arithmetic. It reconstructs each moment from the independent-variable binomial sum, verifies the normalized polynomial identities on 1,936 rational parameter choices, checks the two nonisometric alias examples and their unequal sixth moments, checks the exact reflected sixth-moment factorization on an admissible rational grid, and confirms uniqueness of all 1,089 triples in an independent positive parameter grid. The displayed factorization, positivity, and horizontal-line analysis—not those finite tests—prove the universal theorem. An independent symbolic double integration of \((u^2+v^2)^j\) against the product density for \(j=1,2,3\) gives the same coefficients.

## Relationship to prior work
Herman and Pakianathan (2014) study distance distributions and mean-distance/diameter inequalities in homogeneous compact metric spaces. Their principal symmetry and average-distance theorems do not address a circular product with boundary or truncated even-moment identifiability. Granata and Carnevale (2016) expressly use the lateral surface of a cylinder as a comparison shape for geodesic distance-distribution profiles (their Figure 3), but their dimension-estimation study does not state the exact three-moment inverse theorem or its sharp twofold alias interval. More general inverse-distance-distribution questions are investigated by Mémoli and Needham (preprint 2018), without a verified full-text claim comparison here.

A separate known cylinder/Möbius distance-CDF calculation reconstructs \(C,H\) from small-radius CDF coefficients. That does not imply that the first two *global even moments* have the precise two-to-one fibers above, or that the third even moment suffices. The present result concerns compression to three ordinary expectations rather than access to the complete distribution or to infinitesimal CDF coefficients.

## Limitations
Only exact population moments of intrinsic geodesic distances on an uncapped, unwarped, two-parameter flat circular cylinder are treated. No sample complexity or quantitative stability in noisy estimation is established. The result does not extend automatically to extrinsic straight-line chord distances, circular cylinders with filled endcaps, twisted bands, general product manifolds, or arbitrary Riemannian metrics. A highly relevant general inverse-distribution study was accessible at abstract level, not in complete primary text; exact historical priority remains subject to independent literature review. No independent scientific audit has been performed.

## References
1. M. Herman and J. Pakianathan, *On the distribution of distances in homogeneous compact metric spaces*, arXiv:1407.5607v1, first submitted 2014-07-21. https://arxiv.org/abs/1407.5607
2. D. Granata and V. Carnevale, *Accurate Estimation of the Intrinsic Dimension Using Graph Distances: Unraveling the Geometric Complexity of Datasets*, Scientific Reports 6, 31377 (published 2016-08-11), DOI 10.1038/srep31377. https://www.nature.com/articles/srep31377
3. F. Mémoli and T. Needham, *Distance distributions and inverse problems for metric measure spaces*, arXiv:1810.09646 (initially submitted 2018-10-23), later Studies in Applied Mathematics 149 (2022), 943–1001. https://arxiv.org/abs/1810.09646
