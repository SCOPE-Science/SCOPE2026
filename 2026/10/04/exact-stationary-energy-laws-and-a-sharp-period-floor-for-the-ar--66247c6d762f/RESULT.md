# Exact stationary energy laws and a sharp period floor for the Arneodo–Coullet–Tresser forced-oscillator class
## Finding
Consider the forced-oscillator jerk equation
\[
\dddot x+\beta\ddot x+\dot x=f(x),
\qquad \beta>0,
\]
where \(f:\mathbb R\to\mathbb R\) is locally Lipschitz. In phase variables
\[
y=\dot x,\qquad z=\ddot x,
\]
this is
\[
\dot x=y,\qquad
\dot y=z,\qquad
\dot z=f(x)-y-\beta z.
\]

Every compactly supported invariant probability measure \(\nu\) satisfies the two exact stationary identities
\[
\mathbb E_\nu[z^2]=\mathbb E_\nu[y^2]
\]
and
\[
\mathbb E_\nu[x f(x)]
=-\beta\,\mathbb E_\nu[y^2]
=-\beta\,\mathbb E_\nu[z^2].
\]
The second identity is zero exactly when \(\nu\) is supported on equilibria
\[
\{(r,0,0):f(r)=0\}.
\]

Every nonconstant periodic orbit has least period
\[
P\ge2\pi.
\]
The equality case is completely rigid: \(P=2\pi\) if and only if, after a time shift,
\[
x(t)=m+R\cos t,
\qquad R>0,
\]
and
\[
f(s)=-\beta(s-m)
\]
for every
\[
s\in[m-R,m+R].
\]
Thus the lower bound is universal across the whole forced-oscillator class, and it is attained only when the restoring graph is exactly affine with slope \(-\beta\) over the entire amplitude interval of the orbit.

For the symmetric piecewise-linear example studied by Arneodo, Coullet, and Tresser, let \(\alpha,\mu>0\) and
\[
f_{\alpha,\mu}(x)=
\begin{cases}
-\mu x-\mu-\alpha,&x\le-1,\\
\alpha x,&|x|\le1,\\
-\mu x+\mu+\alpha,&x\ge1.
\end{cases}
\]
Its three equilibria occur at
\[
x=0,\qquad x=\pm r_*,
\qquad
r_*=1+\frac{\alpha}{\mu}.
\]
Every compact invariant probability measure that is not a convex combination of these three equilibrium atoms gives positive mass to
\[
|x|>r_*.
\]
Every nonconstant periodic orbit crosses the boundary
\[
|x|=r_*
\]
at least twice in each least period.

For this piecewise model, the period floor is sharp in a stronger sense. Equality
\[
P=2\pi
\]
occurs exactly when
\[
\beta=\mu,
\]
and the periodic orbit belongs to one of the two harmonic families
\[
x(t)=r_*+R\cos(t-t_0)
\]
or
\[
x(t)=-r_*+R\cos(t-t_0),
\]
with
\[
0<R\le\frac{\alpha}{\mu}.
\]

## Assumptions and scope
The measure statements concern Borel probability measures invariant under the classical flow and supported on compact subsets of \(\mathbb R^3\). Local Lipschitz continuity of \(f\) ensures uniqueness of the flow, and compact support makes all test functions below integrable.

The 1979 forced-oscillator class is the historical starting point. A later full-text treatment explicitly records it as
\[
\dddot x+\beta\ddot x+\dot x=f_\mu(x),
\qquad \beta>0.
\]
The 1981 spiral-attractor paper then studies the same equation with the odd piecewise-linear choice displayed above. Its full text states the three branches and the numerical spiral-attractor parameters near
\[
\alpha=0.2171604,
\qquad
\mu=0.2061612.
\]

The earliest verified public-source date used here is 1979-07-23, the publication date of Physics Letters A volume 72, issues 4–5 containing the founding forced-oscillator article.

## Proof
Let \(L\) be the generator
\[
L
=
y\,\partial_x
+z\,\partial_y
+\bigl(f(x)-y-\beta z\bigr)\partial_z.
\]
For every continuously differentiable test function \(H\) on a neighborhood of the compact support,
\[
\int LH\,d\nu=0.
\]

First,
\[
L\left(\frac12y^2\right)=yz,
\]
so
\[
\mathbb E[yz]=0.
\]
Let \(F\) be any antiderivative of \(f\). Then
\[
LF=f(x)y,
\]
so
\[
\mathbb E[f(x)y]=0.
\]
Now
\[
L(yz)
=z^2+f(x)y-y^2-\beta yz.
\]
Stationarity gives
\[
\mathbb E[z^2]=\mathbb E[y^2].
\]

Next,
\[
L\left(\frac12x^2\right)=xy,
\]
so
\[
\mathbb E[xy]=0.
\]
Also
\[
L(xy)=y^2+xz,
\]
whence
\[
\mathbb E[xz]=-\mathbb E[y^2].
\]
Finally,
\[
L(xz)
=yz+x f(x)-xy-\beta xz.
\]
Using the three preceding identities gives
\[
\mathbb E[x f(x)]
=-\beta\mathbb E[y^2].
\]

Because \(\beta>0\), the right side vanishes if and only if \(y=0\) almost surely. Invariance of the support then forces successively
\[
z=0
\]
and
\[
f(x)=0.
\]
Thus equality consists exactly of invariant probabilities supported on equilibria. Conversely, every such probability clearly realizes equality.

Now let \(x(t)\) be a nonconstant periodic solution with least period \(P\). Its normalized orbit measure gives
\[
\int_0^P z(t)^2\,dt
=
\int_0^P y(t)^2\,dt.
\]
Since
\[
y=x'
\]
is \(P\)-periodic with zero mean and is not identically zero, Wirtinger's inequality gives
\[
\int_0^P z^2\,dt
\ge
\left(\frac{2\pi}{P}\right)^2
\int_0^P y^2\,dt.
\]
Therefore
\[
P\ge2\pi.
\]

Equality in Wirtinger's inequality holds exactly when \(y\) is a nonzero first harmonic. If also \(P=2\pi\), then after a time shift
\[
x(t)=m+R\cos t,
\qquad R>0.
\]
Hence
\[
\dddot x+\dot x=0,
\qquad
\ddot x=-(x-m).
\]
Substitution into the jerk equation yields
\[
f(x(t))=-\beta(x(t)-m).
\]
The harmonic orbit sweeps the whole interval \([m-R,m+R]\), giving the stated affine condition there. Conversely, if this affine condition holds on that interval, the displayed harmonic function is an exact \(2\pi\)-periodic solution.

For the symmetric piecewise model, direct inspection gives
\[
x f_{\alpha,\mu}(x)<0
\quad\Longleftrightarrow\quad
|x|>r_*.
\]
A non-equilibrium invariant measure has
\[
-\mathbb E[x f_{\alpha,\mu}(x)]
=\beta\mathbb E[y^2]>0,
\]
so it must assign positive mass to \(|x|>r_*\).

For a nonconstant periodic orbit, this gives a time at which \(|x|>r_*\). Integrating the third equation over a period gives
\[
\int_0^P f_{\alpha,\mu}(x(t))\,dt=0,
\]
because the period averages of \(y\), \(z\), and \(z'\) vanish. If \(|x(t)|\ge r_*\) for all \(t\), continuity would confine the orbit to one outer half-line, where \(f_{\alpha,\mu}\) has one sign except at the equilibrium; the zero-average identity would then force a constant equilibrium. Hence a nonconstant orbit also has a time with \(|x|<r_*\). Periodicity and continuity force at least two crossings of \(|x|=r_*\).

Finally, if the piecewise model attains \(P=2\pi\), the general equality classification says its range must lie in an interval on which \(f_{\alpha,\mu}\) has slope \(-\beta\). The central slope is \(\alpha>0\), so the range must lie wholly in one outer branch, where the slope is \(-\mu\). Thus \(\beta=\mu\). Matching the affine intercept centers the harmonic orbit at \(r_*\) or \(-r_*\), and staying in the same outer branch requires
\[
R\le r_*-1=\frac{\alpha}{\mu}.
\]
The converse follows by direct substitution.

## Verification
The accompanying checker uses exact sparse-polynomial arithmetic over rational coefficients. It treats \(q\) as a formal symbol for \(f(x)\) in identities whose test polynomials do not differentiate \(q\).

It verifies
\[
L\left(\frac12y^2\right)=yz,
\]
\[
L\left(\frac12x^2\right)=xy,
\]
\[
L(yz)=z^2+qy-y^2-\beta yz,
\]
\[
L(xy)=y^2+xz,
\]
and
\[
L(xz)=yz+xq-xy-\beta xz.
\]
It also checks the piecewise branch continuity, the three zeros \(0,\pm(1+\alpha/\mu)\) on exact rational test parameters, and the harmonic equality substitution when \(\beta=\mu\).

The stored checker output is `VERIFY_OK`. The invariant-measure conclusions additionally use the generator stationarity relation, and the period statement uses the classical equality case of Wirtinger's inequality.

## Relationship to prior work
Coullet, Tresser, and Arneodo introduced the forced-oscillator jerk class in 1979 as a route to stochastic behavior. A later full-text mathematical treatment explicitly identifies that paper as the starting point for
\[
\dddot x+\beta\ddot x+\dot x=f_\mu(x).
\]

Arneodo, Coullet, and Tresser's 1981 full text develops the Shilnikov spiral-attractor mechanism and gives the exact symmetric piecewise-linear function used in the specialization above. It studies homoclinic orbits, the Poincaré return map, and the numerically observed spiral attractor. The inspected text does not state the two stationary energy identities or the universal least-period theorem.

The 1982 continuation focuses on chaotic oscillators and the Shilnikov theorem. Modern work on this jerk family studies symmetry, local bifurcations, integrable deformations, and piecewise chaotic examples. Separate invariant-measure literature has numerically approximated an Arneodo–Coullet attractor for a later polynomial model, but that is not the same piecewise forced-oscillator statement and does not supply the exact identities proved here.

Targeted database and web searches for the exact derivative-energy law, the weighted defect \(-\mathbb E[x f(x)]\), the \(2\pi\) period floor, and the outer-equilibrium amplitude barrier found no statement implying the final theorem. The closest indexed exact-balance results concern different jerk or polynomial flows such as Genesio and Moore–Spiegel.

## Limitations
The general theorem concerns compactly supported invariant probability measures and periodic orbits. It does not prove that a nontrivial compact recurrent set exists for a given nonlinearity \(f\).

The piecewise specialization proves that every non-equilibrium compact invariant measure assigns positive mass outside the outer-equilibrium amplitude, but it does not classify all such measures.

The 1979 founding article itself was not available as complete lawful full text in the inspected sources. Its equation lineage is independently stated in the 2022 full text, and the exact 1981 piecewise model was inspected in a full author-uploaded rendering. The inaccessible 1979 full text remains a bibliographic risk for originality, though no accessible abstract, later summary, or exact search exposed the stationary identities proved here.

## References
1. P. H. Coullet, C. Tresser, and A. Arneodo, “Transition to stochasticity for a class of forced oscillators,” Physics Letters A 72(4–5), 268–270 (1979), DOI 10.1016/0375-9601(79)90464-X.
2. A. Arneodo, P. Coullet, and C. Tresser, “Possible new strange attractors with spiral structure,” Communications in Mathematical Physics 79(4), 573–579 (1981), DOI 10.1007/BF01209312.
3. A. Arneodo, P. Coullet, and C. Tresser, “Oscillators with chaotic behavior: An illustration of a theorem by Shil'nikov,” Journal of Statistical Physics 27, 171–182 (1982), DOI 10.1007/BF01011745.
4. C. Lăzureanu, “Dynamical Properties, Deformations, and Chaos in a Class of Inversion Invariant Jerk Equations,” Symmetry 14, 1318 (2022), DOI 10.3390/sym14071318.
5. V. Magron, M. Forets, and D. Henrion, “Semidefinite approximations of invariant measures for polynomial systems,” Discrete and Continuous Dynamical Systems B 24, 6745–6770 (2019), DOI 10.3934/dcdsb.2019165.
