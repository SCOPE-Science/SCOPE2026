# An absolute movement floor for environmental invasion in a five-state wildlife metapopulation

## Finding

The five-state host–pathogen patch system of Park (2012), with no external reservoir spillover, has an exact, sharp **movement floor for local disease invasion that cannot be overcome by increasing environmental infection conversion arbitrarily**. It has a complete three-regime classification in movement and environmental conversion, and exactly one disease-invasion threshold as movement is increased.

Write the healthy-patch extinction rate as \(a>0\), excess infected-patch extinction rate as \(d>0\), environmental clearance rate as \(z>0\), environmental infection-conversion rate as \(\varepsilon>0\), direct infection probability as \(0\le\delta\le1\), and migration rate as \(m>a\). Define
\[
 b=m-a,\qquad q=a+z,\qquad T=b(b+q),\qquad
 b_0=\frac{\sqrt{q^2+4dz}-q}{2}>0.
\]
The positive disease-free equilibrium is locally exponentially stable when
\[
 H(b)=\varepsilon(T-dz)+z(b+q)(\delta b-d)<0,
\]
and linearly unstable when \(H(b)>0\). At \(H(b)=0\) its linearization has a simple zero eigenvalue; nonlinear stability at equality is not asserted. For every finite \(\varepsilon>0\), the classification is:

1. If \(0<b\le b_0\), then \(H(b)<0\), irrespective of \(\delta\) and \(\varepsilon\). In particular, no increase in environmental conversion can cause local invasion at these movement levels.
2. If \(b>b_0\) and \(\delta b<d\), there is exactly one positive conversion threshold,
\[
 \varepsilon_c(b,\delta)=\frac{z(b+q)(d-\delta b)}{b(b+q)-dz}.
\]
The disease-free equilibrium is stable below, unstable above, and nonhyperbolic at this threshold.
3. If \(\delta b\ge d\), then \(H(b)>0\) for every \(\varepsilon>0\).

Conversely, for each fixed \(\varepsilon>0\) and \(0\le\delta\le1\), there is exactly one movement threshold \(b_*>b_0\), the positive root of
\[
 (b_*+q)[(\varepsilon+\delta z)b_*-dz]=dz\varepsilon.
\]
It is strictly decreasing separately in \(\varepsilon\) and \(\delta\), and approaches \(b_0\) as \(\varepsilon\to\infty\), independently of \(\delta\). If direct transmission is absent (\(\delta=0\)), the weak-environmental-conversion singularity has the certified bound
\[
 \frac{dz}{\varepsilon}<b_*<\frac{dz}{\varepsilon}+\varepsilon.
\]
Thus the invasion movement threshold diverges as \(dz/\varepsilon\) when \(\varepsilon\downarrow0\), whereas even arbitrarily large \(\varepsilon\) cannot lower it below the strictly positive floor \(b_0\).

## Assumptions and scope

Let \(S,K,I,Z\) be proportions of patches that respectively have susceptible occupants without environmental contamination, susceptible occupants with contamination, infected occupants, and contamination without occupants. The unoccupied, uncontaminated fraction is \(E=1-S-K-I-Z\). The state evolves within the nonnegative simplex under the four equations
\[
\begin{aligned}
\dot S&=m(S+K)E+zK-aS-mSI,\\
\dot K&=m(S+K)Z-(a+z)K-m\delta KI+m(1-\delta)SI-\varepsilon K,\\
\dot I&=mIE-(a+d)I+m\delta I(S+K)+mIZ+\varepsilon K,\\
\dot Z&=(a+d)I+aK-zZ-mZ(S+K+I).
\end{aligned}
\]
These are the no-spillover equations of the cited five-state patch model after renaming rates. Require \(a,z,d,\varepsilon>0\), \(0\le\delta\le1\), and \(m>a\). The positive uninfected equilibrium is \((S,K,I,Z)=(b/m,0,0,0)\). 'Invasion' means a positive spectral bound of the infected-compartment linearization; this is a local deterministic criterion, not a finite-population outbreak probability or global endemic-persistence theorem.

## Proof

**1. Exact infected linearization.** At the positive disease-free equilibrium, the full Jacobian is upper block triangular with a healthy-patch eigenvalue \(-b<0\). In the coordinate order \((K,I,Z)\), its infection block is
\[
 B=\begin{pmatrix}
 -(a+z+\varepsilon)&(1-\delta)b&b\\
 \varepsilon&-d+\delta b&0\\
 a&a+d&-(z+b)
\end{pmatrix}.
\]
All three compartments communicate through strictly positive links because \(b,\varepsilon,a+d>0\); thus \(B\) is an irreducible Metzler matrix.

**2. A positive test vector fixes the spectral sign.** Define the positive determinant
\[
 C=(a+z+\varepsilon)(z+b)-ab=z(a+z+\varepsilon)+b(z+\varepsilon)>0
\]
and quantities
\[
 k=\frac{b[(1-\delta)(z+b)+a+d]}{C}>0,
 \qquad v=\frac{ak+a+d}{z+b}>0.
\]
Direct substitution shows
\[
 B(k,1,v)^\mathsf T=(0,\,\varepsilon k+\delta b-d,\,0)^\mathsf T.
\]
For an irreducible Metzler matrix, there exists a strictly positive left eigenvector \(\ell\) at its real spectral bound \(s(B)\). Taking a left product gives
\[
 s(B)\,\ell^\mathsf T(k,1,v)
   =\ell_I(\varepsilon k+\delta b-d).
\]
Every factor except the indicated scalar is positive, so \(s(B)\) has exactly the sign of \(\varepsilon k+\delta b-d\); equality yields a simple Perron eigenvalue zero. Multiplication by \(C\) gives
\[
 C(\varepsilon k+\delta b-d)
 =\varepsilon b[(1-\delta)(z+b)+a+d]+(\delta b-d)C
 = H(b).
\]
Expanding and collecting terms proves
\[
 H(b)=(\varepsilon+\delta z)b(b+a+z)-dz(b+a+z+\varepsilon)
 =\varepsilon[T-dz]+z(b+q)(\delta b-d).
\]
Therefore the displayed sign criterion is necessary and sufficient; it does not rely on a numerical eigenvalue approximation.

**3. An absolute environmental-conversion floor.** The function \(T=b(b+q)\) is strictly increasing for \(b>0\), and has the unique positive solution \(T=dz\) at \(b_0\). Since
\[
 b_0=\frac{dz}{b_0+q}<d,
\]
all \(0<b\le b_0\) obey \(T\le dz\) and \(\delta b<d\). Both summands in the final expression for \(H\) are nonpositive and the second is strictly negative. For \(b>b_0\), the coefficient of \(\varepsilon\) is strictly positive. If \(\delta b<d\), solving the single affine equality \(H=0\) yields the positive threshold \(\varepsilon_c\) in the finding. If \(\delta b\ge d\), both terms are nonnegative and the first is strictly positive. This proves all three regimes and equality statements.

**4. Unique movement threshold and its limits.** For fixed \(\varepsilon>0\) and \(\delta\), the polynomial
\[
 H(b)=(\varepsilon+\delta z)b^2+
 [(\varepsilon+\delta z)q-dz]b-dz(q+\varepsilon)
\]
has positive leading coefficient and negative constant, hence exactly one positive root \(b_*\), at which it crosses from negative to positive. Because \(H(b_0)<0\), that root satisfies \(b_*>b_0\). At the positive root \(\partial_bH>0\). Further,
\[
 \partial_\delta H=zT>0,
 \qquad \partial_\varepsilon H=T-dz>0
 \quad\text{at }b=b_*,
\]
so implicit differentiation proves the two strict monotonicity statements. For any fixed \(b>b_0\), \(H(b)>0\) for sufficiently large \(\varepsilon\), so the decreasing roots tend to \(b_0\).

For \(\delta=0\), the positive-root equation becomes
\[
 (b_*+q)(\varepsilon b_*-dz)=dz\varepsilon,
 \qquad b_*=\frac{dz}{\varepsilon}+\frac{dz}{b_*+q}.
\]
Its second term lies strictly between zero and \(\varepsilon\), since \(b_*>dz/\varepsilon\). This proves the sharp stated reciprocal-scale bracket.

## Verification

The independent, standard-library-only program `verify.py` computes the determinant of the explicit \(3\times3\) infected block and the positive-vector residuals in exact rational arithmetic. It passed 729 parameter tuples spanning positive rates, three direct-infection probabilities, and two exact threshold witnesses. It separately checks the pure-environmental formula and limiting floor with floating-point sanity checks. These tests are finite corroboration only: the all-parameter result follows from the preceding algebra and Perron sign argument.

For example, when \(a=d=z=1\), \(\delta=0\), and \(\varepsilon=1/2\), the movement threshold is exactly \(b_*=\sqrt5\), or \(m_*=1+\sqrt5\). With \(a=d=z=b=1\) and \(\delta=1/2\), the exact conversion threshold is \(\varepsilon_c=3/4\).

## Relationship to prior work

Park (2012) supplies the five-state transition system and numerical comparisons of equilibrium patch occupancy as movement, environmental clearance and transmission vary. The present result is restricted to the linear disease-invasion threshold at the positive disease-free equilibrium, not the endemic occupancy plots. Its exact transmission-independent hard floor, complete conversion/movement classification, and sharp zero-environment asymptotic were not identified in the inspected model, results and discussion sections of that source.

Hess (1996) and Gog, Woodroffe and Swinton (2002) analyze metapopulation disease and movement in models without the same contaminated-but-unoccupied and reoccupied patch route. North and Godfray (2017) analyze spatial dispersal range and approximated establishment thresholds for a different three-class model. These foundations motivate but do not visibly imply the stated five-state formula. The Perron–Frobenius/Metzler method is standard and is not claimed as new; historical priority remains provisional.

## Limitations

The result is **local** at the disease-free equilibrium and applies to an idealized homogeneous deterministic patch ensemble. It does not prove that nonlinear endemic equilibria are unique, that infection goes extinct globally below the threshold, or that outbreaks occur with high probability in a finite metapopulation. The boundary \(H=0\) is nonhyperbolic; its nonlinear behavior is not determined. The strict assumptions \(z>0\), \(\varepsilon>0\), \(d>0\), \(m>a\), and absence of exogenous spillover are essential to the stated classification; permanently persistent contamination and external infection introduce different boundary questions. Historical priority beyond the inspected literature is not certified.

## References

1. Park, A. W. (2012). *Infectious disease in animal metapopulations: the importance of environmental transmission.* Ecology and Evolution **2**, 1398–1407. DOI: 10.1002/ece3.257. Author-uploaded accessible full text: https://www.researchgate.net/publication/230812328_Infectious_disease_in_animal_metapopulations_The_importance_of_environmental_transmission. Public release date recorded as 2012-06-08 at https://openalex.org/W1885265509.
2. Hess, G. (1996). *Disease in Metapopulation Models: Implications for Conservation.* Ecology **77**, 1617–1632. DOI: 10.2307/2265556.
3. Gog, J., Woodroffe, R., and Swinton, J. (2002). *Disease in endangered metapopulations: the importance of alternative hosts.* Proceedings of the Royal Society B **269**, 671–676. DOI: 10.1098/rspb.2001.1667.
4. North, A. R., and Godfray, H. C. J. (2017). *The dynamics of disease in a metapopulation: The role of dispersal range.* Journal of Theoretical Biology **418**, 57–65. DOI: 10.1016/j.jtbi.2017.01.037. Open full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC5360276/.
