# Exact circular design for four-parameter Mogi-source monitoring

## Finding

For every integer \(n\geq3\), consider \(n\) three-component displacement stations constrained to a common surface circle of radius \(r>0\) around the nominal horizontal position of one buried Mogi pressure source of nominal depth \(d>0\) and nonzero source strength \(A\). Let the four locally estimated parameters be source strength, depth, and both horizontal coordinates, with independent equal-variance Gaussian errors in every Cartesian displacement component. Among **all** choices of radius and all angular positions on the chosen circle, the local Fisher-information determinant has a global maximum precisely when

\[
\sum_{j=1}^{n}e^{i\theta_j}=\sum_{j=1}^{n}e^{2i\theta_j}=0
\quad\text{and}\quad
\frac{r}{d}=\sqrt{\frac{\sqrt{561}-11}{110}}
=0.339591178874808\ldots.
\]

For fixed \(r\), these two vanishing angular moments are also **necessary and sufficient** for determinant optimality. Thus a regular \(n\)-gon is optimal for every \(n\geq3\), but equal spacing is not asserted to be necessary when \(n\) is larger. At an angularly optimal design, the exact determinant for noise variance \(\sigma^2\) per component is

\[
\det \mathcal I(r)=
\frac{n^4 A^6}{\sigma^8}
\frac{r^2(d^2+\tfrac52r^2)^2}{(r^2+d^2)^{14}}.
\]

These statements concern an **information-optimal design within the common-radius station class**, not optimality among unrestricted station radii, nor finite-sample estimator error in a misspecified physical model.

## Assumptions and scope

Choose a nominal parameter vector \(\eta=(A,d,X,Y)\) with \(A>0\), \(d>0\), and nominal \(X=Y=0\). The ideal Mogi surface displacement at a station with known horizontal coordinates \((x,y)\) is

\[
\boldsymbol\mu(x,y;\eta)=
\frac{A}{[(x-X)^2+(y-Y)^2+d^2]^{3/2}}
\begin{pmatrix}x-X\\y-Y\\d\end{pmatrix}.
\]

The constant elastic prefactor is absorbed into \(A\). For each of \(n\geq3\) stations at \((x_j,y_j)=(r\cos\theta_j,r\sin\theta_j)\), all three Cartesian displacement components are measured with independent zero-mean Gaussian errors of known common variance \(\sigma^2>0\). Errors are independent across stations. The nominal location and depth determine where the stations are designed; those source parameters are nevertheless **unknown in the inverse problem** and all four parameters are included in the Fisher determinant. The design is local in the nominal parameters. Repeated angles are allowed, although regular spacing is an optimum.

## Proof

Put \(R^2=r^2+d^2\), and for one station let \(p=(x,y,d)^\mathsf T\) and \(e_x,e_y,e_z\) be the Cartesian coordinate vectors. At the nominal source center the four Jacobian columns, ordered as \((A,d,X,Y)\), are

\[
J_A=\frac p{R^3},\quad
J_d=A\left(\frac{e_z}{R^3}-\frac{3dp}{R^5}\right),\quad
J_X=A\left(-\frac{e_x}{R^3}+\frac{3xp}{R^5}\right),\quad
J_Y=A\left(-\frac{e_y}{R^3}+\frac{3yp}{R^5}\right).
\]

The information matrix is \(\mathcal I=\sigma^{-2}\sum_j J_j^\mathsf T J_j\). Direct dot products give, before summing over stations,

\[
\begin{aligned}
J_A\cdot J_A&=R^{-4},&J_A\cdot J_d&=-2AdR^{-6},\\
J_d\cdot J_d&=A^2(r^2+4d^2)R^{-8},&
J_A\cdot J_X&=2AxR^{-6},\\
J_A\cdot J_Y&=2AyR^{-6},&J_d\cdot J_X&=-3A^2dxR^{-8},\\
J_d\cdot J_Y&=-3A^2dyR^{-8},&J_X\cdot J_Y&=3A^2xyR^{-8},\\
J_X\cdot J_X&=A^2(R^2+3x^2)R^{-8},&
J_Y\cdot J_Y&=A^2(R^2+3y^2)R^{-8}.
\end{aligned}
\]

**Angular optimum.** Rotating every station around the nominal source center by angle \(\phi\) conjugates its full information matrix by the orthogonal parameter rotation \(\operatorname{diag}(1,1,Q_\phi)\), where \(Q_\phi\) acts on \((X,Y)\). The determinant is invariant under this conjugation. Averaging an arbitrary fixed-radius information matrix over all rotations produces the same matrix \(\overline{\mathcal I}\), regardless of the original angular positions. Strict concavity of \(\log\det\) on positive definite matrices, or regularization by \(\varepsilon I\) for singular matrices, proves

\[
\det\mathcal I\leq\det\overline{\mathcal I}.
\]

A regular \(n\)-gon for \(n\geq3\) produces exactly this rotational average, because its first and second angular Fourier moments vanish; thus the bound is achievable. For positive-definite designs, equality in strict Jensen requires rotational invariance of \(\mathcal I\). Conversely invariance suffices. The entries \(\mathcal I_{A,X}\), \(\mathcal I_{A,Y}\) are nonzero constant multiples of the cosine and sine first-moment sums, and \(\mathcal I_{X,X}-\mathcal I_{Y,Y}\), \(\mathcal I_{X,Y}\) are nonzero multiples of the cosine and sine second-moment sums. Thus rotational invariance is equivalent to the displayed two angular-moment conditions, with no exceptional positive-radius case. The rotationally averaged matrix is positive definite for every \(r>0\) and \(A>0\), so singular designs cannot give equality.

**Information determinant.** Under these moment conditions the matrix has the two-by-two block and two equal scalar blocks

\[
\mathcal I=\frac n{\sigma^2}
\begin{pmatrix}
R^{-4}&-2AdR^{-6}&0&0\\
-2AdR^{-6}&A^2(r^2+4d^2)R^{-8}&0&0\\
0&0&A^2(d^2+\tfrac52 r^2)R^{-8}&0\\
0&0&0&A^2(d^2+\tfrac52 r^2)R^{-8}
\end{pmatrix}.
\]

The first block has determinant \(A^2r^2R^{-12}\). Multiplication by both location blocks yields the determinant formula in the Finding section.

**Unique radius.** Set \(z=r^2/d^2>0\). With all positive constants omitted, maximizing the determinant is maximizing

\[
g(z)=\frac{z(1+\tfrac52z)^2}{(1+z)^{14}}.
\]

Its derivative has the exact factorization

\[
g'(z)=-\frac{(5z+2)(55z^2+11z-2)}{4(1+z)^{15}}.
\]

The quadratic has one positive root \(z_*=(\sqrt{561}-11)/110\). It is negative below that root and positive above; hence \(g\) rises strictly to \(z_*\) and decreases strictly after it. Moreover \(g(z)\to0\) at both endpoints of the positive half-line. This proves the unique global radius and characterizes every complete maximizer.

## Verification

The accompanying `check.py` constructs the full three-component nonlinear Mogi mean, differentiates with respect to all four unknown parameters, and independently reconstructs Fisher matrices for a square and an equilateral triangle. Exact symbolic equalities verify the displayed balanced matrix and determinant. An exact-rational deliberately angularly unbalanced network has strictly smaller determinant. The program checks the derivative factorization and its unique positive root algebraically. It ran successfully with SymPy. The infinite family of angular configurations is established by the rotational symmetrization proof, **not** by the finite examples in this program.

## Relationship to prior work

Mogi's original 1958 elastic point-source model supplies the forward displacement law; the pressure-source physics is not new. Masterlark (2007) studies how violations of homogeneous elastic assumptions affect forward and inverse volcanic deformation, and makes clear why an ideal-model optimum is not automatically a field recommendation. Fournier, Freymueller and Cervelli (2009) use three-component GPS measurements, a four-parameter Mogi source, nonlinear uncertainty estimation and bootstrap simulations for a real monitoring network. These works concern estimation and model error rather than the exact common-radius D-optimal angular and radial classification proved here. A 2008 USGS network report describes Monte Carlo station-count and placement studies, but its complete PDF was not accessible for a full theorem-by-theorem comparison. A separate result on superposed Mogi sources and radial horizontal-displacement peak splitting concerns a different observable and optimization objective, not the information determinant of four-parameter inversion.

The proposed novelty is restricted to the exact formula and complete optimizer characterization under the explicit local idealization. General symmetry-based optimal-design results could furnish an alternative derivation, and an unlocated geophysical specialization could anticipate this statement.

## Limitations

The design assumes all stations share one freely chosen radius, an approximately correct nominal source center and depth, additive independent isotropic displacement errors, and an ideal homogeneous elastic half-space. Vertical and horizontal GNSS errors often have unequal variances and common modes; environmental and elastic heterogeneity can dominate instrumental noise. Correlated errors, unequal station costs, topography, missing displacement components, mixed radii, additional nuisance parameters and Bayesian robustness are not covered. D-optimality concerns the local information ellipsoid, not a guarantee of global nonlinear inverse identifiability or operational volcanic safety. Historical priority needs broader human verification, especially against inaccessible specialized network-design literature.

## References

1. Mogi, K. (1958). Relations between the eruptions of various volcanoes and the deformations of the ground surfaces around them. *Bulletin of the Earthquake Research Institute*, 36, 99–134.
2. Masterlark, T. (2007). Magma intrusion and deformation predictions: Sensitivities to the Mogi assumptions. *Journal of Geophysical Research: Solid Earth* 112, B06419. DOI: 10.1029/2006JB004860. First publicly posted June 26, 2007.
3. Fournier, T., Freymueller, J., and Cervelli, P. (2009). Tracking magma volume recovery at Okmok volcano using GPS and an unscented Kalman filter. *Journal of Geophysical Research: Solid Earth* 114, B02405. DOI: 10.1029/2008JB005837. First published February 27, 2009.
4. U.S. Geological Survey (2008). *National Volcano Early Warning System* related station-placement and sensitivity report, Scientific Investigations Report 2008-5114, https://pubs.usgs.gov/sir/2008/5114/ (complete PDF inaccessible during comparison).
