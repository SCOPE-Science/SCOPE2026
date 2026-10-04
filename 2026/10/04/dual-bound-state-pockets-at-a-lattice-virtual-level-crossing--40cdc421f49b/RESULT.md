# Dual bound-state pockets at a lattice virtual-level crossing
## Finding
Consider the three-dimensional lattice generalized Friedrichs family of Rasulov and Dilmurodov, with
\[
w_0^{(\gamma)}(k)=\varepsilon(k)+\gamma,
\qquad
w_1(k,p)=\varepsilon(k)+\varepsilon\!\left(\frac{k+p}2\right)+\varepsilon(p),
\]
where \(\varepsilon(k)=\sum_{j=1}^3(1-\cos k_j)\). Fix the coupling \(\mu_0=\mu_l^0(6)=\mu_r^0(6)\) at the source's simultaneous lower- and upper-edge virtual-level point, and put \(\boldsymbol\pi=(\pi,\pi,\pi)\).

For \(\eta>0\), define \(\Omega^-_\eta\) as the set of quasi-momenta \(k\) for which the operator with \(\gamma=6-\eta\) has an eigenvalue \(z^-_\eta(k)<0\), and define \(\Omega^+_\eta\) as the set of quasi-momenta for which the operator with \(\gamma=6+\eta\) has an eigenvalue \(z^+_\eta(k)>18\). Then
\[
\Omega^+_\eta=\boldsymbol\pi+\Omega^-_\eta,
\qquad
z^+_\eta(k+\boldsymbol\pi)=18-z^-_\eta(k).
\]
Thus crossing the dual virtual-level parameter switches a bound-state pocket from the lower edge to the upper edge without changing its quasi-momentum geometry.

Let
\[
C=\frac{32\pi^2\mu_0^2}{5\sqrt5},
\qquad
R=\frac{\sqrt{5/6}}C
 =\frac{25}{32\pi^2\mu_0^2\sqrt6}.
\]
As \(\eta\downarrow0\), the closures of the rescaled pockets converge in Hausdorff distance to Euclidean balls:
\[
\overline{\eta^{-1}\Omega^-_\eta}\longrightarrow \overline{B_R(0)},
\qquad
\overline{\eta^{-1}(\Omega^+_\eta-\boldsymbol\pi)}\longrightarrow \overline{B_R(0)}.
\]
Their three-dimensional Lebesgue volumes satisfy
\[
|\Omega^-_\eta|=|\Omega^+_\eta|
=\frac{4\pi}3R^3\eta^3+o(\eta^3).
\]
Inside the pocket there is also a universal parabolic energy profile. Uniformly for \(q\) in every compact subset of \(|q|<R\),
\[
\frac{z^-_\eta(\eta q)}{\eta^2}
\longrightarrow
-\left(\frac1{2C^2}-\frac35|q|^2\right),
\]
and the upper-edge profile follows from the exact reflection formula.

## Assumptions and scope
The torus is identified with the principal cube \((-\pi,\pi]^3\), with addition understood modulo \(2\pi\). The coupling \(\mu_0\) is the source's critical value at \(\gamma=6\). The result concerns the one-parameter detuning \(\gamma=6\pm\eta\) at this fixed coupling and only eigenvalues below the global lower edge \(0\) or above the global upper edge \(18\). It does not claim a description of embedded spectrum or of detunings in \(\mu\).

## Proof
The source defines the Fredholm determinant
\[
\Delta_\gamma(k;z)=w_0^{(\gamma)}(k)-z-\mu_0^2 I(k;z),
\qquad
I(k;z)=\int_{\mathbb T^3}\frac{dt}{w_1(k,t)-z},
\]
and proves that zeros of \(\Delta_\gamma(k;\cdot)\) outside the essential spectrum are precisely the discrete eigenvalues. Since \(\gamma\) enters only through \(w_0\),
\[
\Delta_{6\pm\eta}(k;z)=\Delta_6(k;z)\pm\eta.
\]
For \(z<0\), direct differentiation gives
\[
\partial_z\Delta_\gamma(k;z)
=-1-\mu_0^2\int_{\mathbb T^3}\frac{dt}{(w_1(k,t)-z)^2}<0,
\]
and \(\Delta_\gamma(k;z)\to+\infty\) as \(z\to-\infty\). Hence a negative eigenvalue exists exactly when \(\Delta_\gamma(k;0)<0\). At \(\gamma=6\), Theorem 3.8 of the source shows that \(\Delta_6(k;0)\ge0\), with equality only at \(k=0\). Therefore
\[
\Omega^-_\eta=\{k:\Delta_6(k;0)<\eta\}.
\]
The corresponding upper-edge statement follows either from the same monotonicity argument above \(18\) or from the exact reflection below.

The dispersion obeys \(\varepsilon(k+\boldsymbol\pi)=6-\varepsilon(k)\). Consequently,
\[
w_1(k+\boldsymbol\pi,p+\boldsymbol\pi)=18-w_1(k,p),
\qquad
w_0^{(6+\eta)}(k+\boldsymbol\pi)=18-w_0^{(6-\eta)}(k).
\]
Changing variables \(p\mapsto p+\boldsymbol\pi\) in the integral gives
\[
I(k+\boldsymbol\pi;18-z)=-I(k;z),
\]
so
\[
\Delta_{6+\eta}(k+\boldsymbol\pi;18-z)
=-\Delta_{6-\eta}(k;z).
\]
The exact pocket translation and eigenvalue reflection follow from the determinant criterion and uniqueness of an exterior zero.

Theorem 3.9 of the source gives, at the lower threshold,
\[
\Delta_6(k;z)
=C\sqrt{\frac65|k|^2-2z}+O(|k|^2)+O(|z|)
\]
as \(k\to0\) and \(z\uparrow0\). Setting \(z=0\) yields
\[
\Delta_6(k;0)=C\sqrt{\frac65}|k|+O(|k|^2)=\frac{|k|}{R}+O(|k|^2).
\]
Thus, for every \(\delta>0\), all sufficiently small \(\eta\) satisfy
\[
B_{(R-\delta)\eta}(0)\subset\Omega^-_\eta
\subset B_{(R+\delta)\eta}(0).
\]
The source's strict global minimum at \(0\) supplies the uniform positive margin away from a fixed neighborhood of the origin. The ball sandwich proves the Hausdorff limit and, after taking volumes and then \(\delta\downarrow0\), the cubic volume law.

Finally fix a compact set \(K\subset\{q:|q|<R}\). Write the negative eigenvalue as \(z^-_\eta(\eta q)=-\eta^2E_\eta(q)\). Substitution in the threshold expansion gives
\[
1=C\sqrt{\frac65|q|^2+2E_\eta(q)}+O(\eta)
\]
uniformly for \(q\in K\), after bracketing the unique zero between two fixed positive values of \(E\). Therefore
\[
E_\eta(q)\longrightarrow \frac1{2C^2}-\frac35|q|^2
\]
uniformly on \(K\). The reflected upper-edge profile is exact.

## Verification
The critical inputs were checked directly against the primary source: the operator and determinant definitions, the global absence of exterior eigenvalues at \((\gamma,\mu)=(6,\mu_0)\), uniqueness of the lower minimum and upper maximum of the threshold determinant, and the square-root threshold expansion with coefficient \(C=32\pi^2\mu_0^2/(5\sqrt5)\). The algebraic identity \(C\sqrt{6/5}=32\pi^2\mu_0^2\sqrt6/25=R^{-1}\) gives the stated radius \(R\). The proof of the pocket and energy laws is analytic; no finite sampling is used to infer an infinite-domain statement.

## Relationship to prior work
Rasulov and Dilmurodov establish the dual virtual levels, the absence of exterior eigenvalues at the critical point, and the threshold determinant expansions. The present statement extracts the detuning geometry that follows when \(\gamma\) crosses the dual point at fixed \(\mu_0\): exact lower/upper pocket duality, the limiting ball, the cubic quasi-momentum volume law, and the parabolic eigenvalue profile.

Albeverio, Lakaev, and Djumanova studied a different rank-one Friedrichs family and obtained low-energy quasi-momentum expansions and eigenvalue existence near a lower threshold. That work supplies important context for the linear quasi-momentum cusp but does not contain the \(\gamma\)-detuned two-edge pocket theorem above. Lakaev and collaborators later obtained convergent coupling-threshold eigenvalue expansions for a two-dimensional rank-one generalized Friedrichs model; that result concerns a different operator, dimension, and perturbation parameter.

## Limitations
The theorem is local in the detuning \(\eta\) for its asymptotic statements, although the exact determinant reflection holds whenever both detuned operators are defined. The energy profile is asserted uniformly only on compact subsets strictly inside the limiting ball; no boundary-layer expansion at \(|q|=R\) is claimed. The result does not determine spectral behavior inside the essential band. A residual literature risk is an equivalent pocket-volume consequence stated under different threshold-bifurcation terminology outside the inspected sources.

## References
1. T. H. Rasulov and E. B. Dilmurodov, *Eigenvalues and virtual levels of a family of \(2\times2\) operator matrices*, Methods of Functional Analysis and Topology 25 (2019), 273--281; arXiv:1911.04918v1.
2. S. Albeverio, S. N. Lakaev, and R. Kh. Djumanova, *Low energy effects for a family of Friedrichs models under rank one perturbations*, arXiv:math/0604282v1.
3. S. N. Lakaev, Sh. Kh. Kurbanov, and Sh. U. Alladustov, *Convergent expansions of eigenvalues of the generalized Friedrichs model with a rank-one perturbation*, Complex Analysis and Operator Theory 15 (2021), Article 121; arXiv:2004.08815.
