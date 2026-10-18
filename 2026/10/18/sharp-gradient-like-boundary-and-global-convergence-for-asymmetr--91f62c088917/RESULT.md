# Sharp gradient-like boundary and global convergence for asymmetric coupled sine maps

## Finding

For the two-dimensional coupled sine map of Soula, Taha, Fournier-Prunaret, and Hamri, every real initial condition converges to a fixed point whenever the parameters satisfy \(a>0\), \(b>0\), \(0\leq c<1\), and
\[
 a+(2-c)b\leq2.
\]
The closed threshold includes the neutral-flip endpoint. No nonconstant periodic orbit, invariant quasiperiodic set, or chaotic recurrent orbit is possible anywhere in this region. An explicitly constructed periodic potential is strictly increasing along every nonfixed orbit. The parameter bound is sharp **for this strict-potential property**: once \(a+(2-c)b>2\), the same potential decreases at points arbitrarily close to the diagonal half-integer fixed point. This is not a necessity claim for nonconvergent dynamics outside the region.

In every fundamental cell, the fixed-point set has exactly four or six points. In addition to the four points \((0,0)\), \((\tfrac12,0)\), \((0,\tfrac12)\), and \((\tfrac12,\tfrac12)\) modulo integers, there are precisely two additional fixed points if and only if
\[
 \frac{a}{2-c}<b<\frac{a}{c}
\]
when \(0<c<1\). When \(c=0\), the criterion is simply \(b>a/2\), with no upper bound. At equality in either finite threshold no additional *distinct* fixed points are present.

## Assumptions and scope

For any real \(x,y\), define
\[
\begin{aligned}
 x'&=x+\frac{a}{2\pi}\sin(2\pi x)+\frac{(1-c)b}{2\pi}\sin(2\pi(y-x)),\\
 y'&=y+\frac{a}{2\pi}\sin(2\pi y)+\frac{b}{2\pi}\sin(2\pi(x-y)).
\end{aligned}
\]
These are the map's actual unwrapped real-plane equations, not a separately rounded or discretized numerical map. The map commutes with integer translations and therefore induces a map on the two-torus. All convergence assertions hold for the original real-plane lift as well as modulo integer translations. Fix \(a,b>0\), \(0\leq c<1\), and put \(h=1-c\in(0,1]\), \(L=a+(1+h)b\).

## Proof

**1. Hidden weighted-gradient structure.** Define the integer-periodic analytic potential
\[
 V(x,y)=\frac{-a h^{-1}\cos(2\pi x)-a\cos(2\pi y)+b\cos(2\pi(y-x))}{4\pi^2}
\]
and \(D=\operatorname{diag}(h,1)\). Direct differentiation proves the **exact** identity \(T(X)=X+D\nabla V(X)\). In the coordinates \(z=D^{-1/2}X\), put \(W(z)=V(D^{1/2}z)\). The transformed map is the unit-step gradient ascent \(z\mapsto z+\nabla W(z)\).

**2. Global Hessian bound and strict ascent at equality.** With \(v=(\sqrt h,-1)^\mathsf T\), its Hessian is
\[
 \nabla^2W=a\begin{pmatrix}\cos(2\pi x)&0\\0&\cos(2\pi y)\end{pmatrix}-b\cos(2\pi(y-x))vv^\mathsf T.
\]
Since \(\|v\|^2=1+h\), every Hessian eigenvalue lies in \([-L,L]\). For \(g=\nabla W(z)\), Taylor's integral formula gives
\[
 W(z+g)-W(z)=\|g\|^2+\int_0^1(1-t)g^\mathsf T\nabla^2W(z+tg)g\,dt
 \geq(1-L/2)\|g\|^2.
\]
Thus ascent is strict when \(L<2\) and \(g\ne0\). At \(L=2\), equality in the initial Hessian lower bound in the nonzero direction \(g\) would require \(g\) parallel to \(v\), both individual cosines equal to \(-1\), and the difference cosine equal to \(+1\). These conditions put \((x,y)=(\tfrac12,\tfrac12)\) modulo integers, where \(g=0\), a contradiction. Hence, when \(L=2\) and \(g\ne0\), the Hessian quadratic form is **strictly above** \(-2\|g\|^2\) at the initial point and on a short positive segment; the integral inequality is therefore strict as well. Consequently \(V(TX)>V(X)\) for every nonfixed \(X\) throughout \(L\leq2\).

**3. Complete finite stationary set.** Since \(a+hb\leq L\leq2\) and \(a+b\leq L\), each coordinate displacement has absolute value at most \(1/\pi<1\); hence a fixed point modulo integers is precisely a real fixed point. Write \(u=2\pi x\), \(t=2\pi(y-x)\), and \(r=b/a\). The two zero-displacement equations are
\[
 \sin u=-hr\sin t,\qquad \sin(u+t)=r\sin t.
\]
If \(\sin t=0\), both coordinates have integral or half-integral values, yielding the four listed fixed points. Otherwise the sine-addition identity forces
\[
 \cos u=r(1+h\cos t),\qquad
 \cos t=C:=\frac{r^{-2}-1-h^2}{2h}.
\]
For \(-1<C<1\), exactly two possibilities \(t=\pm\arccos C\) modulo \(2\pi\) occur. For either one, the prescribed sine and cosine determine a unique \(u\) because \(r^2(1+h^2+2hC)=1\). Both equations are then satisfied. The strict inequality \(-1<C<1\) is equivalent to \(a/(1+h)<b<a/(1-h)\) for \(h<1\), and to \(b>a/2\) for \(h=1\). At \(C=\pm1\) the two branches merge into one of the four grid points. Outside the strict inequalities they do not exist. In particular there are finitely many fixed points on the torus for every allowed parameter triple.

**4. Convergence of every orbit.** On the compact torus the periodic function \(V\) is bounded. Along every orbit it is nondecreasing and strictly increases at nonfixed states, so its values converge. The one-step increase tends to zero. Any torus accumulation point must therefore be fixed, because the one-step increase is continuous and strictly positive otherwise. It follows, again by compactness, that the one-step displacement on the torus tends to zero. The omega-limit set of a sequence in a compact metric space whose consecutive distances tend to zero is connected: separated closed components would force infinitely many transition points with an additional accumulation point outside their separated neighborhoods. The omega-limit set here is a connected subset of a finite fixed-point set, hence one point. The torus orbit converges to it. Since the lift's actual coordinate increments tend to zero and different integer translates of a sufficiently small neighborhood of that limit are separated, the real-plane orbit is eventually contained in one such translated neighborhood and converges to its unique fixed-point lift. Strict ascent also forbids every nonconstant periodic orbit directly.

**5. Exact sharpness for this potential.** At \((x,y)=(\tfrac12,\tfrac12)\) the transformed Hessian has eigenvalues \(-a\) and \(-a-(1+h)b=-L\). In an eigenvector direction for \(-L\), the map's linearization multiplies displacements by \(1-L\). A second-order Taylor expansion of the potential change has leading term \(\tfrac12L^2(2-L)\varepsilon^2\|v\|^2\), which is strictly negative when \(L>2\). Thus this specific \(V\) cannot be a nondecreasing potential outside the closed stated region. No claim about necessity of \(L\leq2\) for point convergence is made.

## Verification

The standalone `verification.py` evaluates the weighted-gradient identity, Hessian representation, and half-integer Jacobian characteristic polynomial by symbolic simplification. It also executes 7,656 finite, seeded numerical diagnostics, including quantitative ascent checks, endpoint tests, explicit nontrivial fixed points, and descent beyond the boundary. It returns `symbolic identities: 3; finite diagnostics: 7656 PASS` in the tested environment. The universal conclusions come from the proof above, not from finite numerical samples.

## Relationship to prior work

Soula, Taha, Fournier-Prunaret, and Hamri (2022), equations (4)–(10), introduce the three-parameter map; their sections 3–5 analyze local fixed-point/period-two bifurcations, parameter diagrams, and synchronization. They do not state the closed global all-orbit convergence region or the strict weighted-gradient potential. Hamri and Soula (2010) treat the symmetric predecessor by critical curves and numerical basin analysis. Maistrenko, Maistrenko, and Mosekilde (2005) investigate synchronization and antisynchronization of coupled sine maps; their detailed complete text was not available for this comparison. The analytical descent-lemma method itself is standard and is not claimed as new. The contribution is the model-specific hidden mobility-gradient identity, the globally sharp potential-ascent boundary including the neutral endpoint, and the resulting all-orbit theorem with the fixed-set census.

## Limitations

The result assumes strictly positive \(a,b\) and \(c<1\); the unidirectional endpoint \(c=1\), negative couplings, and other parameter regimes are not covered. The sharpness statement is only for the displayed potential, not for global convergence itself. The theorem supplies convergence but does not calculate attraction-basin measures or all rates. The 2005 same-family predecessor was available only as an abstract/indexed preview, so earlier implicit or explicit coverage remains a priority risk. The primary publication's author-upload page carries a June 15, 2020 public-upload record; the journal version is dated February 18, 2022. The earlier date is used as the earliest observed public-source date, not as the journal publication date.

## References

1. Y. Soula, A. K. Taha, D. Fournier-Prunaret, N.-E. Hamri, *Bifurcations and Dynamical Behavior of 2D Coupled Chaotic Sine Maps*, Applied and Computational Mathematics 11 (2022), 18–30, DOI: 10.11648/j.acm.20221101.12. Full accessible author-upload text and date record: https://www.researchgate.net/publication/342184443_Bifurcations_and_dynamical_behavior_of_2D_coupled_chaotic_sine_maps.
2. N.-E. Hamri, Y. Soula, *Basins and Critical Curves Generated by A Family of Two-Dimensional Sine Maps*, Electronic Journal of Theoretical Physics 7 (2010), 139–150. Accessible author-upload text: https://www.researchgate.net/publication/228686600_Basins_and_Critical_Curves_Generated_by_A_Family_of_Two-Dimensional_Sine_Maps.
3. V. L. Maistrenko, Yu. L. Maistrenko, E. Mosekilde, *Chaotic Synchronization and Antisynchronization in Coupled Sine Maps*, International Journal of Bifurcation and Chaos 15 (2005), 2161–2177, DOI: 10.1142/S0218127405013320. Abstract/publisher preview only inspected.
