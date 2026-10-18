# Complete complex Turán faces and sharp stability for coordinate stars on finite tori

## Finding
Let \(d\ge1\), let \(n_1,\ldots,n_d\ge3\) be arbitrary integers, and put
\[
G=\prod_{j=1}^d\mathbb Z/n_j\mathbb Z,\qquad
\Omega=\{0\}\cup\{\pm e_j:1\le j\le d\}.
\]
For a complex positive-definite function \(f:G\to\mathbb C\), normalized by \(f(0)=1\) and supported in \(\Omega\), let \(\mathcal M(f)=\sum_{x\in G}f(x)\). If some order is odd, put \(m=\min\{n_j:n_j\text{ odd}\}\) and \(c=\cos(\pi/m)\); otherwise put \(c=1\). The exact extremum is
\[
\max_f\mathcal M(f)=1+\frac1c.
\]
The **entire complex optimizer face**, including its extreme points, is as follows.

* If an odd factor occurs, the maximizing functions are **exactly** those with \(f(e_j)=0\) unless \(n_j=m\), and with \(f(e_j)=u_j\ge0\) real for the remaining indices, where \(\sum_{n_j=m}u_j=1/(2c)\). Thus, if \(r\) factors have order \(m\), the face is an \((r-1)\)-simplex with \(r\) vertices. In particular a unique smallest odd factor yields a unique optimizer, independent of all even factors.
* If every factor is even, the maximizing functions are **exactly** those with \(f(e_j)=u_j+iv_j\),
\[
 u_j\ge0,\qquad \sum_j u_j=\tfrac12,\qquad
 |v_j|\le u_j\tan(\pi/n_j).
\]
This is a \((2d-1)\)-simplex whose \(2d\) vertices each occupy one coordinate and have \(f(e_j)=(1\pm i\tan(\pi/n_j))/2\). These vertices are genuinely nonreal.

The zero set of the Fourier transform of any optimizer is also explicit. Write \(J=\{j:f(e_j)\ne0\}\), and let \(N=|G|\). For an odd-factor optimizer, its Fourier-zero count is \(N(2/m)^{|J|}\): at each active coordinate, exactly the two residues \((m\pm1)/2\) are allowed, while inactive coordinates are unrestricted. For an all-even optimizer, the zero count is \(N\prod_{j\in J}(z_j/n_j)\), with \(z_j=1\) for \(|v_j|<u_j\tan(\pi/n_j)\) and \(z_j=2\) at equality. The zero residues are the corresponding antipodal residue \(n_j/2\), optionally together with the adjacent residue dictated by the sign of \(v_j\).

There is a quantitative rigidity statement whenever an odd factor exists. Define the deficit \(\Delta=(1+1/c)-\mathcal M(f)\), \(s=\sin(\pi/m)\), and for \(n_j\ne m\) put
\[
\kappa_j=
\begin{cases}
\cos(\pi/n_j)-c,&n_j\text{ odd},\\
(1-c)\cos(\pi/n_j),&n_j\text{ even}.
\end{cases}
\]
Every \(\kappa_j\) is strictly positive, and **every admissible function** satisfies
\[
\boxed{\displaystyle
\Delta\ \ge\ \frac2c\left(s\sum_{n_j=m}|\operatorname{Im}f(e_j)|
+\sum_{n_j\ne m}\kappa_j|f(e_j)|\right).}
\]
Every coefficient \(2s/c\) and \(2\kappa_j/c\) in this bound is individually sharp: for each named term there are admissible perturbations arbitrarily close to an optimizer with equality in the corresponding single-coordinate ratio and all other terms absent.

## Assumptions and scope
All coordinate orders are at least three, so \(+e_j\) and \(-e_j\) are distinct. Positive definiteness means \(\sum_{x,y\in G}c_x\overline{c_y}f(x-y)\ge0\) for every complex coefficient family. It implies \(f(-x)=\overline{f(x)}\). Fourier transform is the unnormalized convention \(\widehat f(k)=\sum_x f(x)\exp(2\pi i\sum_j k_jx_j/n_j)\). On finite abelian groups, positive definiteness is equivalent to \(\widehat f(k)\ge0\) at every character. Counting rather than probability-normalized Haar measure is used throughout.

## Proof
**1. Separation of the Fourier inequalities.** Write \(a_j=f(e_j)=u_j+iv_j\), \(\zeta_n=e^{2\pi i/n}\), and
\[
q_n(a)=-\min_{0\le k<n}\operatorname{Re}(a\zeta_n^k).
\]
Then
\[
\widehat f(k)=1+2\sum_j\operatorname{Re}(a_j\zeta_{n_j}^{k_j}),\qquad
\min_k\widehat f(k)=1-2\sum_jq_{n_j}(a_j).
\]
Thus admissibility is **equivalent** to \(\sum_j q_{n_j}(a_j)\le1/2\), not merely implied by it. Furthermore \(q_n(a)\ge0\), with equality only at \(a=0\), since the regular root polygon surrounds the origin.

**2. Exact one-coordinate inequalities.** If \(n\) is odd, the two roots nearest the negative real axis give, with \(c_n=\cos(\pi/n)\) and \(s_n=\sin(\pi/n)\),
\[
q_n(u+iv)\ge c_nu+s_n|v|.
\]
If \(n\) is even, the root \(-1\) gives \(q_n(u+iv)\ge u\). For even \(n\), equality holds **exactly** for \(u\ge0\) and \(|v|\le u\tan(\pi/n)\): geometrically the supporting normal lies in the normal cone of the antipodal root, whose two bounding angles are \(\pm\pi/n\). For odd \(n\), equality \(q_n(a)=c_n\operatorname{Re}a\) forces \(a\) to be nonnegative real, as the two displayed roots force \(v=0\), and any negative real \(a\) instead gives \(q_n(a)=-a>c_na\).

For odd \(m\) and \(c=c_m\), more is true: whenever \(n\ne m\),
\[
q_n(a)-c\operatorname{Re}a\ge \kappa_n|a|,
\quad \kappa_n=\begin{cases}c_n-c,&n\text{ odd},\\(1-c)c_n,&n\text{ even}.
\end{cases}
\]
To verify **the sharp constants**, let \(P_n\) be the convex hull in \(\mathbb R^2\) of \(\{-\zeta_n^k\}\). The left side is the support function of \(P_n-(c,0)\) at the vector corresponding to \(a\). The largest centered Euclidean disk in this translated polygon has radius equal to the minimum distance of \((c,0)\) to a side of \(P_n\). Each side has unit outward normal with support value \(c_n\). If \(n\) is odd, a side normal is horizontal to the right and the nearest distance is \(c_n-c\). If \(n\) is even, the closest side normals make angles \(\pm\pi/n\) with the positive real direction, giving distance \(c_n(1-c)\). Taking the direction of a nearest normal attains each constant. Since every odd \(n>m\) has \(c_n>c\), these values are positive.

**3. Global equality face.** Let \(Q=\sum_j q_{n_j}(a_j)\) and \(M=1+2\sum_j u_j\). Direct algebra gives the exact deficit identity
\[
\left(1+\frac1c\right)-M
=\frac{1-2Q}{c}+\frac2c\sum_j\bigl(q_{n_j}(a_j)-cu_j\bigr).
\]
Each summand is nonnegative. If an odd factor exists, the equality case must have \(a_j=0\) for \(n_j\ne m\), real nonnegative \(a_j\) at the remaining coordinates, and \(Q=1/2\); these are exactly the first stated simplex. In the all-even case \(c=1\), the equality conditions from step 2 instead give the displayed wedges and \(\sum u_j=1/2\). Each wedge is generated by its two boundary rays, and after fixing the sum of all real parts, the whole feasible equality set is the simplex spanned by the \(2d\) stated single-coordinate vertices. The vertices are affinely independent: in any convex combination, the real and imaginary coordinates recover uniquely the two endpoint weights in each axis.

**4. Fourier zeros and stability.** The separated formula for \(\widehat f\) shows it vanishes exactly when **every active** coordinate reaches its individual minimum. An odd optimal real coefficient has two minimizing roots; an even optimal coefficient has one except on the boundary of its wedge, where it has two. Multiplying the independent residue counts proves the zero formulas. Substituting the one-coordinate inequalities in the exact deficit identity proves the quantitative bound. For sharpness of an inactive coefficient, perturb just that coefficient in a nearest-side-normal direction with magnitude \(t>0\), and reduce a fixed positive active odd real coefficient so that \(Q=1/2\). For all sufficiently small \(t\), admissibility holds and the deficit-to-\(t\) ratio is exactly \(2\kappa_j/c\). For the imaginary coefficient, perturb a single active odd coefficient by \(iv\) and reduce its real part to \((1/2-s|v|)/c\); for sufficiently small \(|v|\), its two original minimizing roots stay minimizing, giving deficit exactly \(2s|v|/c\). These are genuine admissible perturbations, not merely tangent formal calculations. This completes the proof.

## Verification
The standalone `verify.py` computes finite-group character spectra directly with standard-library complex arithmetic. Its deterministic checks cover twelve product groups, explicit extreme points, convex mixtures of optimizing vertices, feasibility and sharp objectives, and random feasible perturbations tested against the quantitative inequality. Its finite checks corroborate the theorem but the unrestricted statements above follow from the polygon-support argument. Run using `python verify.py`; no external package or data is needed.

## Relationship to prior work
Turán constants on locally compact and finite abelian groups, including packing/spectral bounds, were developed by Kolountzakis and Révész (2003/2006). Gorbachev and Manoshina (2002/2004) studied the even periodic one-dimensional interval problem using finite linear programming. DeCorte, de Laat, and Vallentin (2013/2014) recast Cayley-graph Lovász theta problems in finite Fourier variables. These works explain the governing optimization framework and, in dimension one, many scalar optima. The claim here is specifically the mixed-order **complete complex optimizer face**, the associated positional Fourier-zero patterns, and the explicit sharp coefficientwise stability law. General Fourier linear-program formulations or one-dimensional even formulas by themselves do not furnish these equality and stability classifications.

## Limitations
The statement concerns the **coordinate star** only, not a radius-two ball, an arbitrary sparse support, or nonabelian groups. The numerical checker is corroborative; it is not an exhaustive test of all dimensions or of all complex feasible kernels. The scalar mass alone is elementary from the separated Fourier constraints and is not presented as the sole contribution. Equivalent complete equality/stability descriptions could exist in graph-theta or positive-definite-kernel literature under different terminology; no claim of independent external validation is made.

## References
1. D. V. Gorbachev and A. S. Manoshina, *Turan Extremum Problem for Periodic Function with Small Support*, arXiv:math/0211291, public 19 November 2002; later *Mathematical Notes* 76 (2004).
2. M. N. Kolountzakis and S. Gy. Révész, *Turán's extremal problem for positive definite functions on groups*, arXiv:math/0312218, public 10 December 2003; later *J. London Math. Soc.* 74 (2006), 475–496.
3. E. DeCorte, D. de Laat, and F. Vallentin, *Fourier analysis on finite groups and the Lovász theta-number of Cayley graphs*, arXiv:1307.5703, public 22 July 2013; later *Experimental Mathematics* 23 (2014), 146–152.
