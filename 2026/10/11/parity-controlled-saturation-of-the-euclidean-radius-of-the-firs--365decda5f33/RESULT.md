# Parity-controlled saturation of the Euclidean radius of the first two Jordan powers

## Finding
For the nilpotent Jordan shift \(J_n\) and its square, the parameterized Euclidean numerical radius
\[
R_n(t)=\max_{\|x\|_2=1}\Bigl(|\langle J_nx,x\rangle|^2+t^2|\langle J_n^2x,x\rangle|^2\Bigr)^{1/2}
\]
has a parity-controlled saturation phenomenon. Set \(\beta_n=\cos(\pi/(\lceil n/2\rceil+1))=w(J_n^2)\). For every integer \(n\ge3\), if \(n\) is even then \(R_n(t)>t\beta_n\) for each finite \(t\ge0\). If \(n\) is odd, there exists a sharp \(\tau_n\in(0,\infty)\) such that \(R_n(t)>t\beta_n\) precisely when \(0\le t<\tau_n\), and \(R_n(t)=t\beta_n\) precisely when \(t\ge\tau_n\).

The first two thresholds and the complete three-dimensional profile are
\[
\tau_3=2,\qquad \tau_5=\sqrt{5+\frac{7\sqrt2}{2}},\qquad
R_3(t)=\begin{cases}2/\sqrt{8-t^2},&0\le t\le2,\\ t/2,&t\ge2.\end{cases}
\]
For odd dimensions, \(\tau_n=\Theta(n^{3/2})\); more precisely,
\[
\frac1{2\pi}\le\liminf_{n\to\infty,\ n\ \mathrm{odd}}\frac{\tau_n}{n^{3/2}}
\le\limsup_{n\to\infty,\ n\ \mathrm{odd}}\frac{\tau_n}{n^{3/2}}
\le\frac3{2\sqrt2\pi}.
\]

## Assumptions and scope
Work on \(\mathbb C^n\) with its standard Hilbert norm. The shift \(J_n\) has entries \((J_n)_{i,i+1}=1\), all others zero. The radius is the standard Euclidean numerical radius of the operator pair \((J_n,tJ_n^2)\), not the numerical radius of the single operator \(J_n+tJ_n^2\). All statements hold for the specified finite dimensions and all real \(t\ge0\); there is no assertion about arbitrary weighted shifts or noninteger dimension. Complex phases may be removed by taking absolute values of coordinates: both absolute inner products are bounded above by the corresponding sums for the nonnegative coordinate vector, preserving its norm.

Define symmetric real matrices \(C=(J_n+J_n^*)/2\) and \(D=(J_n^2+(J_n^*)^2)/2\). For nonnegative real unit vectors \(x\), write \(a=\langle Cx,x\rangle\ge0\), \(b=\langle Dx,x\rangle\ge0\). Therefore \(R_n(t)^2=\max_{x\ge0,\|x\|_2=1}(a^2+t^2b^2)\). The parity-indexed submatrices of \(D\) are half-adjacency matrices of paths of lengths \(\lceil n/2\rceil\) and \(\lfloor n/2\rfloor\); a path of length \(d\) has top eigenvalue \(\cos(\pi/(d+1))\).

## Proof
**Parity and the sharp threshold.** For even \(n=2m\), the two parity blocks of \(D\) have the same top eigenvalue \(\beta_n\). Let \(u,v\) be their positive normalized top eigenvectors, embedded in disjoint coordinate sets. The unit vector \(x=(u+v)/\sqrt2\) has \(b=\beta_n\) and \(a>0\), since \(C\) couples adjacent indices. Hence \(R_n(t)^2\ge a^2+t^2\beta_n^2>t^2\beta_n^2\), for all finite \(t\).

For odd \(n=2m+1\), let \(u\) be the positive normalized top eigenvector of the larger (odd-indexed) block of \(D\), and put
\[
\beta=\cos\frac\pi{m+2},\quad\eta=\cos\frac\pi{m+1},\quad\gamma=\beta-\eta>0,\quad c=\|C\|=\cos\frac\pi{n+1}.
\]
The eigenvalue \(\beta\) is simple, and the second eigenvalue of \(D\) is \(\eta\): it dominates the second eigenvalue \(\cos(2\pi/(m+2))\) of the larger path. For a nonnegative unit vector \(x=s u+y\), with \(s\ge0\) and \(y\perp u\), one has \(\beta-b\ge\gamma\|y\|^2\), \(\langle Cu,u\rangle=0\), and
\[
a\le2c\|y\|+c\|y\|^2\le3c\|y\|,
\qquad \beta^2-b^2\ge\beta\gamma\|y\|^2.
\]
The last inequality uses \(0\le b\le\beta\). Thus the **sharp** finite positive number
\[
\tau_n:=\sup_{x\ge0,\ \|x\|=1,\ b<\beta}
\frac{a}{\sqrt{\beta^2-b^2}}
\]
satisfies \(\tau_n\le3c/\sqrt{\beta\gamma}\). It is positive because the Perron vector of \(C\) has \(a>0\) and cannot be a top eigenvector of \(D\). The equivalence
\[
a^2+t^2b^2\le t^2\beta^2\ \Longleftrightarrow\ t\ge a/\sqrt{\beta^2-b^2}\]
for \(b<\beta\), together with \(a=0\) whenever \(b=\beta\), gives exactly the claimed open/closed saturation intervals. No attainment of the defining supremum for \(\tau_n\) is required.

**Explicit three-dimensional formula.** The optimizing nonnegative vector can be chosen reflection-symmetric. Indeed, for each supporting direction \(\theta\in[0,\pi/2]\), the top eigenvector of \(\cos\theta\,C+t\sin\theta\,D\) can be chosen nonnegative and reflection-symmetric by Perron--Frobenius and averaging along the commuting reflection (with a limiting argument if the matrix is reducible). Write \(x=(a,b,a)\) with \(2a^2+b^2=1\), and set \(s=a^2\in[0,1/2]\). Then \(a_C=2a b\), \(b_D=a^2\), giving
\[
a_C^2+t^2b_D^2=4s+(t^2-8)s^2.
\]
Maximizing this quadratic on the indicated closed interval gives \(R_3(t)^2=4/(8-t^2)\) for \(0\le t\le2\), and \(R_3(t)^2=t^2/4\) thereafter.

**Exact five-dimensional threshold.** The same nonnegative Perron/reflection argument reduces the maximum to \(x=(a,b,c,b,a)\). If \(a>0\), write \(r=c/a\ge0\), \(u=b/a\ge0\), and \(N=2+2u^2+r^2\). Then
\[
a_C=\frac{2u(1+r)}N,\qquad b_D=\frac{2r+u^2}N,\qquad\beta^2=\frac12.
\]
Put \(k=5+7\sqrt2/2\). To prove \(a_C^2\le k(\beta^2-b_D^2)\), multiply by \(N^2\) and expand the difference as
\[
Q(r,u)=\frac k2(r^2-2)^2+B(r)u^2+ku^4,
\quad B(r)=(6+7\sqrt2)(r-\sqrt2)\left(r-\frac{25\sqrt2+14}{31}\right).
\]
For \(r\ge0\), when \(B(r)\ge0\), all three terms are nonnegative. When \(B(r)<0\), one has \(\sqrt2<r<(25\sqrt2+14)/31\). The discriminant of the quadratic \(Q(r,\sqrt z)\) in \(z=u^2\) is
\[
B(r)^2-2k^2(r^2-2)^2=(35+14\sqrt2)(r-\sqrt2)^2
(r-12-9\sqrt2)\left(r-\frac{5\sqrt2-4}{17}\right)\le0
\]
on precisely that interval. Hence \(Q\ge0\). If \(a=0\), then \(x=(0,b,c,b,0)\), \(b_D=b^2\le1/2\) and the same inequality follows directly from \(a_C=2bc\), \(2b^2+c^2=1\), and \(k>4\) (indeed, \(4b^2c^2\le4(1/2-b^4)\le k(1/2-b^4)\)). Thus \(\tau_5^2\le k\). Conversely, for the unit top eigenvectors \(u_*\) and \(v_*\) of the parity blocks of \(D\), with \(\langle u_*,Cv_*\rangle=(2+\sqrt2)/4\), the vectors \(\sqrt{1-\varepsilon^2}\,u_*+\varepsilon v_*\) show
\[
\tau_5^2\ge\frac{2\langle u_*,Cv_*\rangle^2}{\beta(\beta-\eta)}
=5+\frac{7\sqrt2}{2}=k.
\]
This proves the sharp threshold, including the boundary \(t=\tau_5\).

**Growth in odd dimension.** With \(n=2m+1\), embed the parity-block Perron vectors as \(u,v\). Let \(A_m=\langle u,Cv\rangle>0\); explicitly their coordinate entries in their respective blocks are \(\sqrt{2/(m+2)}\sin(j\pi/(m+2))\) and \(\sqrt{2/(m+1)}\sin(j\pi/(m+1))\). Testing \(x=\sqrt{1-\varepsilon^2}\,u+\varepsilon v\), sending \(\varepsilon\downarrow0\), and combining with the preceding global gap estimate gives
\[
\sqrt{\frac{2A_m^2}{\beta\gamma}}\le\tau_{2m+1}\le\frac{3c}{\sqrt{\beta\gamma}}.
\]
Direct Riemann-sum comparison of the positive sine profiles gives \(A_m\to1\). Taylor expansion gives \(\beta\to1\), \(c\to1\), and \(\gamma=\pi^2m^{-3}+O(m^{-4})\). Substituting \(n=2m+1\) yields the two explicit liminf/limsup bounds and \(\Theta(n^{3/2})\).

## Verification
The accompanying standalone script `verify.py` checks the polynomial identity and discriminant factorization in the five-dimensional certificate exactly in the quadratic field \(\mathbb Q(\sqrt2)\), checks the lower-limit equality there, and performs numerical matrix comparisons for small odd and even dimensions. It prints `JORDAN_PAIR_SATURATION_CERTIFICATE_OK` upon success. Matrix sampling is a regression check only. The universal and asymptotic assertions follow from the analytic arguments above, not from finite sampling.

## Relationship to prior work
The standard joint/Euclidean numerical-radius invariant is studied in Bhunia--Majeed (arXiv:2603.03962, first public March 4, 2026), including bounds involving Euclidean operator radii. Jana--Bhunia--Paul (arXiv:2204.05150) and Moslehian--Sattari--Shebrawi (2017) prove general inequalities for two-operator radii. Stanković (2026) identifies the joint numerical radius with the Euclidean radius and studies inequalities for spherical transforms of tuples. The present result concerns an exact nonlinear saturation transition for the particular pair of first and second powers of the canonical nilpotent Jordan shift; none of the inspected bounds logically fixes that transition or its dimension parity. Gau--Wu (arXiv:1304.0295) studies numerical ranges of KMS matrices, whose matrices combine all powers of a shift into a single operator. Knowledge of the numerical range of that single sum does not fix the joint Euclidean radius of the two separate powers. These comparisons establish absence of coverage in the inspected statements, not a proof of universal novelty.

## Limitations
No exact values of \(\tau_n\) for odd \(n\ge7\), and no exact coefficient in the asymptotic \(\tau_n/n^{3/2}\), are established. The lower/upper limit bounds need not be sharp. This is a finite-dimensional complex-Hilbert-space theorem, with nonnegative real parameter only. Prior-work searching cannot exclude an unindexed, differently phrased equivalent theorem.

## References
1. P. Bhunia and R. Majeed, *Refined numerical radius estimates and Euclidean operator radius*, arXiv:2603.03962 (2026), https://arxiv.org/pdf/2603.03962.
2. S. Jana, P. Bhunia, and K. Paul, *Euclidean operator radius inequalities of a pair of bounded linear operators and their applications*, arXiv:2204.05150 (2022), https://arxiv.org/pdf/2204.05150.
3. M. S. Moslehian, M. Sattari, and K. Shebrawi, *Extensions of Euclidean operator radius inequalities*, Math. Scand. 120 (2017), 129–144, DOI:10.7146/math.scand.a-25509, https://journals.msp.org/mscand/article/download/328/327/359.
4. H.-L. Gau and P. Y. Wu, *Numerical Ranges of KMS Matrices*, arXiv:1304.0295 (2013), https://arxiv.org/pdf/1304.0295.
5. H. Stanković, *Spherical Heinz transform of operator tuples*, Z. Anal. Anwend. 45 (2026), 139–163, DOI:10.4171/ZAA/1787, https://ems.press/content/serial-article-files/52403.
