# Three omitted mixed equilibria in a triple-helix replicator model
## Finding
For the tripartite replicator system printed as Eq. (3.13) in Liu, Meng, Ji and Wang, introduce
\[
A=E_c-L_c,\qquad D=E_u-L_u,\qquad B=G_c+F_c,\qquad E=G_u+F_u,\qquad F=F_c+F_u.
\]
The system is
\[
\begin{aligned}
\dot x&=x(1-x)(Ay+Bz-C_c),\\
\dot y&=y(1-y)(Dx+Ez-C_u),\\
\dot z&=z(1-z)(F-Bx-Ey).
\end{aligned}
\]
The source lists only the eight cube corners as equilibria. At its own baseline parameters there are exactly three additional equilibria in \([0,1]^3\):
\[
H_9=\left(\frac{34}{37},\frac{40}{41},0\right),\qquad
H_{10}=\left(\frac{6}{37},\frac{8}{41},1\right),\qquad
H_{11}=\left(\frac{517}{1248},\frac{71}{156},\frac{3329}{4992}\right).
\]
The two face equilibria are hyperbolic saddles with one unstable direction, and the fully mixed equilibrium is a hyperbolic saddle with two unstable directions.

More generally, if \(B>0\), \(E>0\), and \(A+D>0\), then the affine indifference equations have at most one fully mixed solution, namely
\[
x_* = \frac{AF+BC_u-C_cE}{B(A+D)},\qquad
y_* = \frac{-BC_u+C_cE+DF}{E(A+D)},\qquad
z_* = \frac{ABC_u-ADF+C_cDE}{BE(A+D)}.
\]
Whenever all three coordinates belong to \((0,1)\), this equilibrium has unstable dimension two.

## Assumptions and scope
The result concerns exactly the deterministic three-population, two-strategy replicator system printed as Eq. (3.13) of the cited 2026 article. The baseline calibration is the source's stated choice
\[
C_c=40,\ C_u=34,\ E_c=42,\ E_u=38,\ G_c=18,\ G_u=16,\ F_c=14,\ F_u=12,\ L_c=L_u=1.
\]
Thus \(A=41\), \(D=37\), \(B=32\), \(E=28\), and \(F=26\). No claim is made about payoff specifications other than the printed system, about finite-population stochastic evolutionary models, or about global basin geometry beyond the local stable/unstable dimensions proved here.

## Proof
An equilibrium coordinate can be a boundary value, where its logistic prefactor vanishes, or an interior value, where the corresponding affine payoff difference must vanish.

For \(z=0\), the interior conditions for \(x\) and \(y\) reduce to
\[
41y-40=0,\qquad 37x-34=0.
\]
Hence, besides the four corners of the lower face, the only noncorner equilibrium on that face is
\[
\left(\frac{34}{37},\frac{40}{41},0\right).
\]
A single interior coordinate cannot occur there: if \(x\) is interior then \(y=40/41\) is forced, and if \(y\) is interior then \(x=34/37\) is forced.

For \(z=1\), the corresponding equations are
\[
41y-8=0,\qquad 37x-6=0,
\]
so the only noncorner equilibrium on the upper face is
\[
\left(\frac{6}{37},\frac{8}{41},1\right).
\]

Now suppose \(0<z<1\). Then the third affine factor must vanish:
\[
32x+28y=26.
\]
If \(x=0\), this forces \(y=13/14\), while the interior \(y\)-equation requires \(z=17/14\), outside the cube. If \(y=0\), then \(x=13/16\), while the interior \(x\)-equation requires \(z=5/4\), again outside the cube. The alternatives \(x=1\) or \(y=1\) are immediately incompatible with \(32x+28y=26\). Therefore any equilibrium with interior \(z\) must have all three coordinates interior. Solving
\[
41y+32z=40,\qquad 37x+28z=34,\qquad 32x+28y=26
\]
gives uniquely
\[
\left(\frac{517}{1248},\frac{71}{156},\frac{3329}{4992}\right),
\]
whose coordinates are all strictly between zero and one. This proves that the baseline cube contains exactly eleven equilibria.

For the general interior calculation, solve
\[
Ay+Bz=C_c,\qquad Dx+Ez=C_u,\qquad Bx+Ey=F.
\]
The determinant of this linear system is \(BE(A+D)\), so under \(B>0\), \(E>0\), and \(A+D>0\) the solution is unique and equals the displayed formula.

At a fully mixed equilibrium, let
\[
s_x=x_*(1-x_*),\qquad s_y=y_*(1-y_*),\qquad s_z=z_*(1-z_*).
\]
The Jacobian is
\[
J_*=\begin{pmatrix}
0&s_xA&s_xB\\
s_yD&0&s_yE\\
-s_zB&-s_zE&0
\end{pmatrix}.
\]
Thus
\[
\operatorname{tr}J_*=0,
\qquad
\det J_*=-BE(A+D)s_xs_ys_z<0.
\]
The characteristic polynomial has the form
\[
\lambda^3+q\lambda+r,
\qquad r=BE(A+D)s_xs_ys_z>0.
\]
It has a negative real root because its value at \(0\) is positive and it tends to \(-\infty\) as \(\lambda\to-\infty\). If all three roots are real, the negative determinant and zero trace force exactly one negative root and two positive roots. If the remaining two roots are complex conjugates, their common real part is half the negative of the real root and is therefore positive. Hence every admissible fully mixed equilibrium is hyperbolic with unstable dimension two.

At each baseline face equilibrium, the tangent \((x,y)\) block has zero trace and negative determinant, hence one positive and one negative eigenvalue. The remaining transverse eigenvalue equals \(-46606/1517<0\) at \(H_9\) and \(-23282/1517<0\) at \(H_{10}\). Each face equilibrium therefore has exactly one unstable direction.

## Verification
The bundled `verify.py` reconstructs Eq. (3.13), enumerates all equilibrium status patterns in the baseline cube, checks that the only solutions are the eight corners and the three displayed mixed points, verifies the general fully mixed formula by exact symbolic substitution, and confirms the Jacobian determinant identity. All arithmetic is exact rational or symbolic arithmetic.

A direct numerical spectrum check, used only as a diagnostic after the exact proof, gives approximately
\[
\operatorname{spec}(J(H_{11}))=\{-9.53356,\ 4.76678\pm 8.67608i\},
\]
consistent with the exact unstable-dimension-two argument.

## Relationship to prior work
The motivating article explicitly writes Eq. (3.13), then states that solving the stationarity equations yields eight equilibrium points, all cube corners, and bases its local stability table on those eight points. Its baseline simulation parameters are also stated explicitly. The calculation above therefore corrects the equilibrium census of that precise published system rather than modifying the model.

A closely related earlier collaborative-innovation paper by Su, Shi, Zhu and Xin (2021) explicitly retains mixed equilibria when reducing a three-party game to two active strategy variables under a fixed government strategy. That precedent shows that mixed states are standard objects in this literature, but it neither uses the 2026 payoff system nor implies the three omitted equilibria, their exact coordinates, or the universal unstable-index-two property proved here.

Peng, Wang and Zhao (2025) analyze another tripartite evolutionary game and study equilibrium strategies and asymptotic stability, but the accessible article material concerns a different industrial-internet payoff structure. It does not imply the source-specific affine system, the baseline eleven-point census, or the determinant/trace argument above.

## Limitations
The equilibrium classification is exact for the stated baseline parameters and the general fully mixed formula is exact under \(B>0\), \(E>0\), and \(A+D>0\). The result does not classify every possible boundary degeneracy for arbitrary parameters. It also does not establish a global basin partition or claim that the stable manifolds of the omitted saddles are the unique global separatrices. The literature search cannot prove absolute novelty; the originality assessment is limited to the source article, directly relevant earlier collaborative-innovation models, published-record semantic searches and exact-form web searches described in the review materials.

## References
1. Y. Liu, J.-H. Meng, F. Ji, J. Wang, “How to enhance collaborative innovation resilience? A game-theoretic analysis of triple-helix synergies in high-tech sectors,” *Journal of Industrial and Management Optimization* 22 (2026), 1539–1570. DOI: 10.3934/jimo.2026057.
2. N. Su, Z. Shi, X. Zhu, Y. Xin, “An Evolutionary Game Model of Collaborative Innovation Between Enterprises and Colleges Under Government Participation of China,” *SAGE Open* 11 (2021). DOI: 10.1177/2158244021994854.
3. X. Peng, S. Wang, C. Zhao, “Government Subsidy Policies for Industrial Internet Adoption: A Tripartite Evolutionary Game Analysis,” *Managerial and Decision Economics* 46 (2025), 1392–1404. DOI: 10.1002/mde.4440.
