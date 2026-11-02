# Optimal vertical two-coset exponential bases for a tent-roof double tile

## Finding

Consider the open planar domain (boundary choices are immaterial)
\[
D=\{(x,y):0<x<1,\ 0<y<1/4\}\ \cup\
\{(x,y):0<x<1,\ 1/4+u(x)<y<1/2+u(x)\},
\qquad u(x)=\min\{x,1-x\}.
\]
For real \(t\), let \(\mathcal E_t\) consist of the two families
\[
 e^{2\pi i(nx+4my)},\qquad e^{2\pi i(nx+(4m+t)y)},
 \qquad (n,m)\in\mathbb Z^2.
\]
Set
\[
 \rho(t)=\max_{a\in\{1,2,3\}}\left|\cos\frac{\pi at}{4}\right|.
\]
The exact (optimal) squared synthesis bounds, for the coefficient \(\ell^2\) norm and unnormalized Lebesgue measure on \(D\), are
\[
 A(t)=\frac{1-\rho(t)}2,\qquad B(t)=\frac{1+\rho(t)}2.
\]
Consequently \(\mathcal E_t\) is a Riesz basis of \(L^2(D)\) exactly when
\[
 t\not\equiv0,\ 4/3,\ 2,\ 8/3\pmod4.
\]
Among **all** real offsets \(t\) in this two-coset class, both maximal lower synthesis bound and minimal upper synthesis bound occur exactly at \(t\equiv1,3\pmod4\). The sharp optimal squared condition number is
\[
\min_{t:A(t)>0}\frac{B(t)}{A(t)}=3+2\sqrt2,
\]
so the optimal operator-norm condition number equals \(1+\sqrt2\). Common vertical shifts of both cosets do not change any of these quantities.

For a forbidden residue \(t_0\) and small real \(\varepsilon\), the exact leading loss is
\[
 A(t_0+\varepsilon)=\frac{\pi^2 a_0^2}{64}\varepsilon^2+O(\varepsilon^4),
\]
where \(a_0=1\) for \(t_0\equiv0\), \(a_0=2\) for \(t_0\equiv2\), and \(a_0=3\) for \(t_0\equiv4/3,8/3\pmod4\). In each case the remainder is local with \(t_0\) fixed.

## Assumptions and scope

The domain uses ordinary planar Lebesgue measure, and the definition of Riesz bounds is
\[
 A\sum_{j}|c_j|^2\le\left\|\sum_jc_je_j\right\|_{L^2(D)}^2
 \le B\sum_j|c_j|^2
\]
for finitely supported complex coefficients, with completeness also required for a basis. Frequencies have unrestricted horizontal integer component and the two vertical cosets \(4\mathbb Z\) and \(4\mathbb Z+t\). No optimality is asserted among more general spectral sets. An arbitrary common vertical shift multiplies every basis function by the same unimodular function and hence preserves all bounds.

## Proof

**1. Exact double-tiling and all three fiber displacements.** Let \(Q=(0,1)\times(0,1/4)\). Almost every \((x,s)\in Q\) has exactly two representatives in \(D\) under vertical translations by integer multiples of \(1/4\): \((x,s)\) and \((x,s+a(x,s)/4)\), for a unique integer \(a(x,s)\in\{1,2,3\}\). This follows since the second component of \(D\) is an interval of length \(1/4\) whose lower endpoint is \(1/4+u(x)\). Each index occurs on a positive-measure subset of \(Q\): \(a=1\) on \(0<x<1/4,\ x<s<1/4\); \(a=2\) on \(0<x<1/4,\ 0<s<x\); and \(a=3\) on \(1/4<x<1/2,\ 0<s<x-1/4\). Each is open and of positive area. Thus the unfolding
\[
 Uf(x,s)=\big(f(x,s),f(x,s+a(x,s)/4)\big)
\]
is unitary from \(L^2(D)\) onto \(L^2(Q;\mathbb C^2)\).

**2. Sharp fiber singular values.** For any finite coefficients, form the two Fourier polynomials \(F_0,F_1\) on \(Q\) with frequencies \((n,4m)\) and the respective two families of coefficients. The system \(\{e^{2\pi i(nx+4ms)}\}_{n,m\in\mathbb Z}\) is orthogonal on \(Q\), with squared norm \(|Q|=1/4\), so Parseval states
\[
 \int_Q(|F_0|^2+|F_1|^2)=\frac14\sum_j|c_j|^2.
\]
At a point where \(a(x,s)=a\), the two unfolded values of the synthesized function equal
\[
\begin{pmatrix}1&1\\1&e^{2\pi ita/4}\end{pmatrix}
\begin{pmatrix}F_0(x,s)\\e^{2\pi its}F_1(x,s)\end{pmatrix}.
\]
The last diagonal phase is unitary. The squared singular values of the matrix are
\[
2\pm\left|1+e^{2\pi ita/4}\right|=2\pm2\left|\cos\frac{\pi at}{4}\right|.
\]
Integration over \(Q\) therefore gives the stated global bounds \((1\mp\rho(t))/2\). They are **sharp**: each of the three displacement sets has positive measure, and any measurable unit eigenvector field for the appropriate smallest or largest eigenvalue can be approximated in \(L^2(Q;\mathbb C^2)\) by the two scalar Fourier series. The inverse unfolding and synthesis then achieve the bound as an infimum or supremum.

If no fiber matrix is singular, its inverse has uniformly bounded operator norm (only three values of \(a\) occur), so the synthesis map extends onto all of \(L^2(Q;\mathbb C^2)\) and the system is a Riesz basis. If some fiber matrix is singular, functions supported in its positive-measure region give nonzero vectors orthogonal to the synthesis range; the system is neither complete nor a Riesz basis. Fiber singularity is precisely \(at/4\in\mathbb Z\), giving the four forbidden residue classes.

**3. Unique minimax staggering.** Write \(\theta=\pi t/4\) modulo \(\pi\), and use reflection to assume \(0\le\theta\le\pi/2\). For \(\theta<\pi/4\), \(|\cos\theta|>1/\sqrt2\). For \(\pi/4<\theta<3\pi/8\), \(|\cos3\theta|>1/\sqrt2\). For \(3\pi/8\le\theta\le\pi/2\), \(|\cos2\theta|\ge1/\sqrt2\), with equality at the left endpoint where \(|\cos3\theta|>1/\sqrt2\). At \(\theta=\pi/4\), \(\rho=1/\sqrt2\). Thus this is the unique minimizing angle after the symmetry reduction, i.e. precisely \(t\equiv1,3\pmod4\). Substitution proves both optimum bounds and condition numbers.

**4. Quadratic stability loss at every collision.** At \(t_0\equiv4/3,2,8/3\) modulo four, just one of the three absolute cosines equals one, with index \(a_0=3,2,3\), respectively. All others are strictly below one at that point, so the same term uniquely maximizes nearby. At \(t_0\equiv0\), all three equal one, but for sufficiently small nonzero \(\varepsilon\), the index \(a_0=1\) has the largest absolute cosine. Expanding \(\left|\cos(\pi a_0\varepsilon/4)\right|=1-\pi^2 a_0^2\varepsilon^2/32+O(\varepsilon^4)\) proves the stated coefficients.

## Verification

The accompanying `verify.py` checks the exact scalar fiber matrix formula at rational and irrational parameter samples; enumerates the three displacement indices on a finite mesh; verifies the optimum, the forbidden residue classes and the quadratic coefficients numerically. These tests provide finite consistency checks, not a substitute for the analytical proof.

## Relationship to prior work

Asipchuk and De Carli, *Methods of construction of exponential bases on planar domains* (arXiv:2505.00870, first submitted May 2025; journal 2026), develop multi-tiling techniques for this nonconvex domain. Their subsequent note *Methods of Construction of Exponential Bases on Planar Domains Revised* (arXiv:2610.18751, October 2026) replaces the frequency construction in their proof. Their construction supplies a distinguished basis and the bounds \((2\pm\sqrt2)/4\). The present theorem treats **all** vertical two-coset offsets as one parameter, proves exact rather than merely admissible constants for each, finds the complete nonbasis set, proves the globally optimal offsets, and quantifies each of four distinct degenerations. General lattice-multitiling and finite Vandermonde theorems provide context and the matrix reduction, but do not state this fully optimized offset classification for the present geometry. The optimal offset \(t=1\) recovers the familiar displayed constants.

## Limitations

The optimality claim is confined to vertically separated two-coset bases with full horizontal frequencies \(\mathbb Z\), not to arbitrary nonuniform or oblique frequency sets. Earlier general fiber criteria may imply parts of the proof after specialization; historical priority for the complete optimized phase diagram is not independently established. The verification program samples finitely many parameters and cannot prove global optimization by itself. This analytical result has not undergone independent validation.

## References

1. O. Asipchuk and L. De Carli, *Methods of construction of exponential bases on planar domains*, arXiv:2505.00870 (first public 2025-05-05), journal version *Bull. Malays. Math. Sci. Soc.* **49** (2026), article 133, DOI:10.1007/s40840-026-02112-7.
2. O. Asipchuk and L. De Carli, *Methods of Construction of Exponential Bases on Planar Domains Revised*, arXiv:2610.18751v1 (2026-10-13).
3. M. N. Kolountzakis, *Multiple lattice tiles and Riesz bases of exponentials*, *Proc. Amer. Math. Soc.* **143** (2015), 741–747.
4. C. Cabrelli and D. Carbajal, *Riesz bases of exponentials on unbounded multi-tiles*, *Proc. Amer. Math. Soc.* **146** (2018), 1991–2004.
