# Correct first-order averaging for the positive-radius zero-Hopf branch
## Finding
Consider the four-dimensional flow
\[
\dot x=a(y-x),\qquad
\dot y=bx-y-xz+u,\qquad
\dot z=-cz+xy,\qquad
\dot u=-du-jx+exz,
\]
with the perturbation used by Yang, Wei, and Moroz,
\[
a=-1+\varepsilon a_1,\qquad c=\varepsilon c_1,\qquad
j=\varepsilon j_1,\qquad d=\varepsilon d_1,
\]
where \(b>1\), \(e\ne0\), and \(\varepsilon>0\) is small. Put \(\omega=\sqrt{b-1}\). Reconstructing the first-order angular average directly from the printed differential equations and the paper's own linear change gives
\[
\bar f_r=\frac{r(eU-j_1-a_1\omega^2)}{2\omega^3},\qquad
\bar f_Z=\frac{Z(j_1-eU-d_1\omega^2)}{\omega^3},
\]
\[
\bar f_U=\frac{-2c_1U+2Z^2/\omega^4+r^2/(1+\omega^2)}{2\omega}.
\]
These are not the first two averaged functions printed in the source: the signs of the \(a_1\omega^2\) and \(eU\) contributions to the radial equation, and the sign of the \(eU\) contribution to the \(Z\)-equation, differ.

For a simple averaged zero with \(r>0\), one necessarily has
\[
U_*=\frac{a_1\omega^2+j_1}{e},\qquad Z_*=0,
\qquad
r_*^2=\frac{2c_1(1+\omega^2)(a_1\omega^2+j_1)}{e}.
\]
Consequently this positive-radius branch exists and is nondegenerate exactly when
\[
\frac{c_1(a_1\omega^2+j_1)}{e}>0,
\qquad a_1+d_1\ne0.
\]
Its first-order averaged Jacobian is Hurwitz exactly when
\[
a_1+d_1>0,\qquad c_1>0,\qquad a_1\omega^2+j_1<0.
\]
Under these strict conditions the standard first-order averaging theorem used by the source yields an asymptotically stable small periodic orbit for all sufficiently small positive \(\varepsilon\).

The discrepancy is substantive even at \(b=2\), where the later typographical distinction between \(b-1\) and \((b-1)^2\) disappears. For
\[
(b,a_1,d_1,c_1,j_1,e)=(2,1,2,1,-2,-1),
\]
the corrected zero is \((r_*,Z_*,U_*)=(2,0,1)\), its determinant is \(-3\), and its averaged eigenvalues are \(-3\) together with the roots of \(\lambda^2+\lambda+1\); hence the branch is asymptotically stable. The source's printed positive-radius existence expression has the opposite sign and excludes this parameter point. If only \(e\) is changed to \(+1\), the source's printed existence condition is satisfied, but the corrected formula gives \(r_*^2=-4\), so the reconstructed first-order average has no real positive-radius zero there. This does not prove that the full ODE has no periodic orbit at that second parameter choice; it proves that the source's stated first-order argument does not certify the claimed positive-radius branch.

## Assumptions and scope
The claim concerns the perturbative family just displayed, with \(b>1\), \(e\ne0\), and sufficiently small \(\varepsilon>0\). The parameters \(a_1,c_1,j_1,d_1\) are real; the source assumes them nonzero, and the same restriction may be imposed here. The result concerns only the simple averaged zero with positive polar radius. It does not assess the source's two zero-radius averaged labels, does not exclude periodic solutions arising by another mechanism, and does not classify global dynamics.

The primary classification is MSC2020 \(37\mathrm{G}15\), bifurcations of limit cycles and periodic orbits.

## Proof
After the source's amplitude rescaling, the printed system is
\[
\dot x=x-y+\varepsilon a_1(y-x),\qquad
\dot y=(1+\omega^2)x-y+u-\varepsilon xz,
\]
\[
\dot z=\varepsilon(-c_1z+xy),\qquad
\dot u=\varepsilon(-j_1x-d_1u+exz).
\]
Use exactly the linear change printed in the source,
\[
x=-\frac{Z}{\omega^2}+\frac{\omega X+Y}{1+\omega^2},\qquad
y=Y-\frac{Z}{\omega^2},\qquad z=U,\qquad u=Z.
\]
Its inverse relations needed for differentiation are
\[
X=\frac{(1+\omega^2)x-y+u}{\omega},\qquad
Y=y+\frac{u}{\omega^2},\qquad Z=u,\qquad U=z.
\]
At \(\varepsilon=0\), these variables satisfy \(\dot X=-\omega Y\), \(\dot Y=\omega X\), and \(\dot Z=\dot U=0\). Write \(X=r\cos\theta\) and \(Y=r\sin\theta\). Then \(\dot\theta=\omega+O(\varepsilon)\), so to first order the angular average is obtained by dividing the \(O(\varepsilon)\) variations of \(r,Z,U\) by \(\omega\).

Let the perturbation pieces of the rescaled equations be
\[
P_x=a_1(y-x),\qquad P_y=-xU,\qquad
P_u=-j_1x-d_1Z+exU,\qquad P_z=-c_1U+xy.
\]
Differentiating the inverse linear change gives
\[
P_X=\frac{(1+\omega^2)P_x-P_y+P_u}{\omega},\qquad
P_Y=P_y+\frac{P_u}{\omega^2},\qquad P_Z=P_u,\qquad P_U=P_z.
\]
The radial perturbation is \(\cos\theta\,P_X+\sin\theta\,P_Y\). Using
\[
\langle\cos\theta\rangle=\langle\sin\theta\rangle=
\langle\sin\theta\cos\theta\rangle=0,
\qquad
\langle\cos^2\theta\rangle=\langle\sin^2\theta\rangle=\frac12,
\]
and the displayed expressions for \(x\) and \(y\), direct averaging yields
\[
\bar f_r=\frac{r(eU-j_1-a_1\omega^2)}{2\omega^3}.
\]
Likewise \(\langle x\rangle=-Z/\omega^2\), so
\[
\bar f_Z=\frac{\langle P_u\rangle}{\omega}
=\frac{Z(j_1-eU-d_1\omega^2)}{\omega^3}.
\]
Finally,
\[
\langle xy\rangle=\frac{Z^2}{\omega^4}+rac{r^2}{2(1+\omega^2)},
\]
which gives the stated formula for \(\bar f_U\).

For \(r>0\), the equation \(\bar f_r=0\) forces
\[
U=\frac{a_1\omega^2+j_1}{e}.
\]
At this value the coefficient multiplying \(Z\) in \(\bar f_Z\) is \(-(a_1+d_1)/\omega\). Thus, at a simple zero with \(a_1+d_1\ne0\), necessarily \(Z=0\). The remaining equation \(\bar f_U=0\) gives the formula for \(r_*^2\).

At \((r_*,0,U_*)\), the Jacobian of the averaged vector field is
\[
\begin{pmatrix}
0&0&er_*/(2\omega^3)\\
0&-(a_1+d_1)/\omega&0\\
r_*/(\omega(1+\omega^2))&0&-c_1/\omega
\end{pmatrix}.
\]
Its determinant is
\[
\frac{c_1(a_1\omega^2+j_1)(a_1+d_1)}{\omega^5}.
\]
One eigenvalue is \(-(a_1+d_1)/\omega\). The other two are the roots of
\[
\lambda^2+\frac{c_1}{\omega}\lambda
-\frac{c_1(a_1\omega^2+j_1)}{\omega^4}=0.
\]
Because \(\omega>0\), both roots have negative real part exactly when their coefficient of \(\lambda\) and constant term are positive, namely when \(c_1>0\) and \(a_1\omega^2+j_1<0\). Combining this with the first eigenvalue proves the stability criterion. Under the existence condition these inequalities also force \(e<0\), consistently with \(r_*^2>0\).

Since \(r_*>0\), a sufficiently small neighborhood of the averaged zero remains inside the regular polar chart, and \(\dot\theta\) stays bounded away from zero for sufficiently small \(\varepsilon\). Thus the ordinary first-order averaging theorem applies to this branch without a polar-axis singularity.

## Verification
The reconstruction was checked in two independent ways. First, the averaged equations above were derived directly from the printed rescaled ODE and inverse linear change, rather than from the source's displayed averaged functions. Second, the bundled exact-rational checker verifies the two parameter witnesses, the corrected determinant, and the quadratic stability polynomial. Its recorded output is `VERIFY_OK`.

For the stable witness \((2,1,2,1,-2,-1)\), the checker verifies \(r_*^2=4\), \(U_*=1\), determinant \(-3\), and the stable quadratic \(\lambda^2+\lambda+1\). With only \(e\) changed to \(+1\), it verifies that the source's printed positive-radius condition is positive while the corrected value is \(r_*^2=-4\).

## Relationship to prior work
Yang, Wei, and Moroz introduced the specific perturbative calculation considered here. Their paper correctly sets \(\omega^2=b-1\) and prints the rescaled ODE and linear change used above, but its displayed first-order radial and \(Z\) averages have sign discrepancies relative to those equations. Its Theorem 2(i) then gives a positive-radius branch in terms of \(a_1\omega^2-j_1\), followed by additional conditions containing \((b-1)^2\). The present result reconstructs the average one step earlier, so the correction is not obtained by merely changing \((b-1)^2\) to \(b-1\).

Llibre and Tian later gave a substantially broader study of zero-Hopf equilibria for the same four-dimensional system. Their main origin theorem perturbs \(b,c,d,j\) around a zero-Hopf family while holding \(a\) fixed. The perturbation treated here instead holds \(b\) fixed and perturbs \(a,c,d,j\), so their theorem does not state this corrected averaged vector field or imply the displayed positive-radius criterion without an additional reparameterization or conjugacy. The checked full text describes the 2020 result as partial but does not supply this correction.

Searches by exact title, DOI, the corrected combination \(a_1\omega^2+j_1\), and the sign pattern of the corrected radial average did not locate a published correction or an equivalent statement. A semantically close published finding about polar-boundary zeros concerns a different Rössler unfolding and does not imply this algebraic reconstruction for the present vector field.

## Limitations
This is a local first-order averaging result. It establishes the correct simple positive-radius averaged branch and its first-order stability classification for the printed perturbative family. It does not prove that a periodic orbit is absent when the corrected positive-radius zero is absent; higher-order or different local mechanisms may still produce periodic orbits. It does not assess the source's zero-radius averaged labels, global hyperchaos, basin structure, or parameter regimes outside the small-\(\varepsilon\) setting.

## References
1. J. Yang, Z. Wei, I. Moroz, “Periodic solutions for a four-dimensional hyperchaotic system,” *Advances in Difference Equations* 2020, 198 (2020). DOI: 10.1186/s13662-020-02647-4. First published 2020-05-06.
2. J. Llibre, Y. Tian, “The zero-Hopf bifurcations of a four-dimensional hyperchaotic system,” *Journal of Mathematical Physics* 62, 052703 (2021). DOI: 10.1063/5.0023155.
3. MSC2020, \(37\mathrm{G}15\): bifurcations of limit cycles and periodic orbits.
