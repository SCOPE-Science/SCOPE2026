# A one-parameter family of asymmetric blind alternatives for the \(\mathcal X_{1,3}\) extropy contrast
## Finding
Alshathri and Kayid define the population differential-extropy contrast
\[
\mathcal X_{r,n}=\frac12\int_0^1\left(\rho_{n-r\mid n:F}(u)^2-\rho_{n-r\mid n:G}(u)^2\right)f(F^{-1}(u))\,du
\]
and implement their symmetry test with the fixed minimal choice \((r,n)=(1,3)\). There is a whole one-parameter family of smooth asymmetric distributions for which this implemented population contrast is exactly zero.

Let \(z=2u-1\) and define
\[
h(u)=z^3-\frac{15}{28}z,
\qquad
d_\varepsilon(u)=1+\varepsilon h(u),
\qquad 0<|\varepsilon|<\frac{28}{13}.
\]
Set
\[
Q_\varepsilon(u)=\int_0^u\frac{dv}{d_\varepsilon(v)},\qquad 0\le u\le1,
\]
and let \(F_\varepsilon\) be the inverse of \(Q_\varepsilon\) on \([0,Q_\varepsilon(1)]\). Then the associated density satisfies
\[
f_\varepsilon(Q_\varepsilon(u))=d_\varepsilon(u).
\]
For every allowed nonzero \(\varepsilon\), this distribution is asymmetric but
\[
\mathcal X_{1,3}(F_\varepsilon)=0.
\]
The blindness is specific to the implemented contrast: the next admissible member of the same family gives
\[
\mathcal X_{1,4}(F_\varepsilon)=\frac{\varepsilon}{35}.
\]
Thus a single \((1,3)\) extropy contrast is not a characterization of symmetry over all absolutely continuous finite-variance laws, even though the collection of contrasts across system sizes can retain identifying information.

## Assumptions and scope
The construction uses \(0<|\varepsilon|<28/13\). The support is the finite interval \([0,Q_\varepsilon(1)]\). The density is strictly positive and real analytic on the interior of its support, and the variance is finite automatically because the support is bounded.

The conclusion concerns the population functional underlying the fixed \((r,n)=(1,3)\) statistic chosen in Section 5 of Alshathri and Kayid. It does not assert a formula for the test's limiting rejection probability. It also does not contradict their all-\(n\) characterization, because the same constructed family is detected already at \((r,n)=(1,4)\).

## Proof
For \((r,n)=(1,3)\), the source formulas give \(a_{1,3}=4\) and \(b_{1,3}=3\), hence
\[
\rho_{2\mid3:F}(u)=4u-3u^2,
\qquad
\rho_{2\mid3:G}(u)=4(1-u)-3(1-u)^2=1+2u-3u^2.
\]
Therefore, with \(z=2u-1\),
\[
W_3(u):=\rho_{2\mid3:F}(u)^2-\rho_{2\mid3:G}(u)^2
=\frac12 z(5-3z^2).
\]
The constant part of \(d_\varepsilon\) contributes zero because \(W_3\) is odd in \(z\):
\[
\int_0^1W_3(u)\,du=0.
\]
For the perturbation, using \(du=dz/2\),
\[
\begin{aligned}
\int_0^1W_3(u)h(u)\,du
&=\frac14\int_{-1}^1 z(5-3z^2)\left(z^3-\frac{15}{28}z\right)\,dz\\
&=\frac14\left(\frac87-\frac{15}{28}\frac{32}{15}\right)=0.
\end{aligned}
\]
Consequently
\[
\mathcal X_{1,3}(F_\varepsilon)
=\frac12\int_0^1W_3(u)d_\varepsilon(u)\,du=0.
\]

It remains to verify that this is a genuine asymmetric probability model. The cubic \(h(z)=z^3-15z/28\) has critical points at \(z=\pm\sqrt{5/28}\). At the endpoints its values are \(\pm13/28\), while the interior critical values have smaller absolute magnitude. Hence
\[
|h(u)|\le\frac{13}{28}
\]
for \(0\le u\le1\). The stated range of \(\varepsilon\) therefore gives \(d_\varepsilon(u)>0\) everywhere. Thus \(Q_\varepsilon\) is a strictly increasing real-analytic diffeomorphism from \((0,1)\) onto the interior of a finite interval, and its inverse defines a strictly positive real-analytic density there.

A symmetric absolutely continuous distribution must satisfy the density-quantile identity
\[
f(F^{-1}(u))=f(F^{-1}(1-u)).
\]
Here \(h(1-u)=-h(u)\), so
\[
d_\varepsilon(1-u)=1-\varepsilon h(u),
\]
which differs from \(d_\varepsilon(u)\) on a set of positive measure whenever \(\varepsilon\ne0\). Therefore \(F_\varepsilon\) is not symmetric.

Finally, for \((r,n)=(1,4)\),
\[
\rho_{3\mid4:F}(u)=6u^2-4u^3,
\]
and direct polynomial expansion gives
\[
\rho_{3\mid4:F}(u)^2-\rho_{3\mid4:G}(u)^2
=-4(2u-1)(2u^2-2u-1).
\]
Its integral against the constant part of \(d_\varepsilon\) vanishes by reflection, while
\[
\int_0^1\left(\rho_{3\mid4:F}(u)^2-\rho_{3\mid4:G}(u)^2\right)h(u)\,du=\frac{2}{35}.
\]
Hence
\[
\mathcal X_{1,4}(F_\varepsilon)=\frac{\varepsilon}{35}.
\]
This also shows explicitly why the construction does not defeat the source's use of a family of system sizes for characterization.

## Verification
All algebraic identities are exact. The accompanying `verify.py` recomputes the polynomial weights, the two vanishing moments for \((1,3)\), the nonzero \((1,4)\) moment, and the sharp endpoint bound used for positivity using rational arithmetic only.

The source defines the transformed consecutive-system densities and differential extropies in equations (11)--(14), defines \(\mathcal X_{r,n}\) in equation (24), proves convergence of the estimator to \(\mathcal X_{r,n}\) in Theorem 5.1, and then explicitly chooses \((r,n)=(1,3)\) for the implemented test. Its scale standardization does not remove this blind family: under a positive affine rescaling, a zero population contrast remains zero.

## Relationship to prior work
Alshathri and Kayid's all-system-size characterization uses equality across all admissible \(n\) for a fixed \(r\); the present construction instead isolates the loss of information caused by collapsing that family to the single \((1,3)\) contrast used in the test. The exact identity \(\mathcal X_{1,4}=\varepsilon/35\) demonstrates that distinction directly.

Sathar and Sathar study extropy for consecutive \(k\)-out-of-\(n\):G systems and state a characterization based on equality across all admissible system configurations. That collection-level result does not imply that one fixed polynomial-weighted contrast separates all asymmetric density-quantile profiles.

Earlier symmetry tests based on extropy of order statistics or record values use different system weights and different statistics. Their accessible descriptions do not contain the polynomial null family above or imply it for the consecutive-system \((1,3)\) contrast.

## Limitations
The result is a population-level blind-family construction. It does not derive the limiting distribution of the spacing estimator under these alternatives, so it does not claim a particular limiting power or size. It does not analyze cumulative residual or cumulative past extropy versions. It does not claim that combining \((1,3)\) with \((1,4)\) is itself omnibus-consistent; \((1,4)\) is used only to show that the all-system-size information is not annihilated by this family.

A remaining originality risk is that an equivalent orthogonality construction may exist in nonindexed notes or in inaccessible full text on other extropy-based symmetry tests under different notation.

## References
1. T. Alshathri and M. Kayid, “Extropy-based characterization and nonparametric testing of symmetry in continuous distributions via consecutive systems,” *AIMS Mathematics* 11(4), 10638--10667 (2026), DOI 10.3934/math.2026438. Published 20 April 2026.
2. E. I. Abdul Sathar and S. Sathar, “Extropy Properties of Consecutive \(k\)-Out-of-\(n\):G Systems Under the Condition \(2k\ge n\),” *Symmetry* 18(7), 1114 (2026), DOI 10.3390/sym18071114.
3. P. Xiong, W. Zhuang, and G. Qiu, “Testing symmetry based on the extropy of record values,” *Journal of Nonparametric Statistics* 33(1), 134--155 (2021), DOI 10.1080/10485252.2021.1914338.
4. H. Alizadeh Noughabi and J. Jarrahiferiz, “Extropy of order statistics applied to testing symmetry,” *Communications in Statistics - Simulation and Computation* 51(6), 3389--3399 (2022), DOI 10.1080/03610918.2020.1714660.
