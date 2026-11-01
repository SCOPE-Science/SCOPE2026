# A universal square-root Hilbert–Schmidt cusp for power-damped Hankel moments

## Finding
Let \((\mu_j)_{j\geq0}\) be a complex moment-type sequence such that, for some \(c\in\mathbb C\), \(\delta>0\), and \(C<\infty\),
\[
\left|\mu_j-\frac{c}{j+1}\right|\leq C(j+1)^{-1-\delta}\qquad(j\geq0).
\]
On \(\ell^2(\mathbb N)\) define the Hankel operator \(H_\mu=(\mu_{m+n-2})_{m,n\geq1}\) and the power-damping diagonal \(D_\alpha e_m=m^{-\alpha}e_m\). Then \(H_\mu\) is bounded and every commutator \(K_\alpha=D_\alpha H_\mu-H_\mu D_\alpha\), \(\alpha>0\), belongs to the Hilbert–Schmidt class. As \(\alpha\downarrow0\),
\[
\boxed{\|K_\alpha\|_{\mathcal S_2}^2=\frac{\pi^2|c|^2}{6}\,\alpha+O_{c,C,\delta}(\alpha^2).}
\]
When \(c\neq0\), the Hilbert–Schmidt norm has the sharp square-root cusp \(\|K_\alpha\|_{\mathcal S_2}\sim\pi|c|\sqrt{\alpha/6}\). In particular, if \(\mu_j=\int_0^1t^jw(t)\,dt\) for a bounded complex density satisfying \(|w(t)-w(1)|\leq C(1-t)^\delta\) on \([0,1]\), then the leading constant depends only on \(w(1)\).

## Assumptions and scope
All operators act on complex \(\ell^2(\mathbb N)\), with indices \(m,n\geq1\). The remainder estimate holds uniformly for \(0<\alpha\leq1/2\), with a constant depending on the specified sequence bounds, not on \(\alpha\). The index shift in the Hankel kernel is \(m+n-2\); the classical Hilbert matrix is obtained when \(\mu_j=1/(j+1)\). No positivity of \(\mu_j\) or \(w\) is required.

## Proof
**1. Existence and Hilbert–Schmidt membership.** Write \(\mu_j=c/(j+1)+r_j\). Hilbert's inequality bounds \((1/(m+n-1))_{m,n\geq1}\) on \(\ell^2\). The Hankel remainder is Hilbert–Schmidt, since
\[
\sum_{m,n\geq1}|r_{m+n-2}|^2\leq C^2\sum_{s\geq2}(s-1)^{-1-2\delta}<\infty.
\]
Thus \(H_\mu\) is bounded. The commutator matrix is \((m^{-\alpha}-n^{-\alpha})\mu_{m+n-2}\). Its classical-Hilbert contribution is Hilbert–Schmidt because
\[
\sum_{m,n\geq1}\frac{|m^{-\alpha}-n^{-\alpha}|^2}{(m+n-1)^2}
\leq4\sum_{m\geq1}m^{-2\alpha}\sum_{n\geq1}(m+n-1)^{-2}<\infty
\]
for every \(\alpha>0\). The remainder contribution is Hilbert–Schmidt because \(D_\alpha\) is bounded and \((r_{m+n-2})\) is Hilbert–Schmidt.

**2. Removal of the moment remainder.** For \(x,y\geq1\), the inequality \(|x^{-\alpha}-y^{-\alpha}|\leq\alpha|\log(x/y)|\) holds. The elementary discrete estimate
\[
\sum_{m=1}^{s-1}\log^2\frac{m}{s-m}\leq C_0s\qquad(s\geq2)
\]
follows by separating \(m\leq s/2\), using \(\log((s-m)/m)\leq\log(s/m)\), and comparing the sum of \(\log^2(s/m)\) with the integrable function \(\log^2(1/u)\) on \((0,1/2]\). Consequently,
\[
\left|\|K_\alpha\|_{\mathcal S_2}^2-|c|^2F(\alpha)\right|
\leq C_1\alpha^2\sum_{s\geq2}s^{-1-\delta}=O(\alpha^2),
\]
where \(F(\alpha)=\sum_{m,n\geq1}(m^{-\alpha}-n^{-\alpha})^2/(m+n-1)^2\) is the classical Hilbert commutator's squared Hilbert–Schmidt norm.

**3. Lattice-to-continuum estimate.** Replacing \((m+n-1)^{-2}\) by \((m+n)^{-2}\) changes \(F(\alpha)\) by at most
\[
C_2\alpha^2\sum_{m,n\geq1}\frac{\log^2(m/n)}{(m+n)^3}=O(\alpha^2).
\]
Put \(G_\alpha(x,y)=(x^{-\alpha}-y^{-\alpha})^2/(x+y)^2\), for \(x,y\geq1\). Its partial derivatives satisfy
\[
|\partial_xG_\alpha|\leq2\alpha^2\left(\frac{|\log(x/y)|}{x(x+y)^2}+\frac{\log^2(x/y)}{(x+y)^3}\right),
\]
and the analogous estimate holds for \(\partial_yG_\alpha\). On each cell \([m,m+1]\times[n,n+1]\), replace the logarithm by \(|\log(m/n)|+\log2\), and both denominators by their values at \((m,n)\). The resulting bounds have a finite double sum, since
\[
\sum_{m,n\geq1}\frac{1+|\log(m/n)|}{m(m+n)^2}<\infty,
\quad
\sum_{m,n\geq1}\frac{1+\log^2(m/n)}{(m+n)^3}<\infty.
\]
The cell mean-value estimate therefore yields
\[
F(\alpha)=\int_1^\infty\!\int_1^\infty G_\alpha(x,y)\,dx\,dy+O(\alpha^2).
\]
All constants in this step are uniform for \(0<\alpha\leq1/2\).

**4. Exact continuum reduction and leading coefficient.** Set \(s=x+y\) and \(t=x/(x+y)\). Integrate first in \(s\) over \([1/\min(t,1-t),\infty)\), use symmetry about \(t=1/2\), and put \(u=t/(1-t)\). This gives the exact identity
\[
\int_1^\infty\!\int_1^\infty G_\alpha(x,y)\,dx\,dy
=\frac1\alpha\int_0^1\frac{(1-u^\alpha)^2}{(1+u)^2}\,du.
\]
The inequality \(|(1-e^{-z})^2-z^2|\leq C_3z^3\) for \(z\geq0\), followed by integration against \((1+u)^{-2}du\), gives
\[
\frac1\alpha\int_0^1\frac{(1-u^\alpha)^2}{(1+u)^2}\,du
=\alpha\int_0^1\frac{\log^2u}{(1+u)^2}\,du+O(\alpha^2).
\]
Integration by parts and the alternating Basel series evaluate the integral as \(2\sum_{k\geq1}(-1)^{k-1}/k^2=\pi^2/6\). Combining steps 2–4 proves the claimed estimate, including the sharp coefficient.

**5. Moment-density specialization.** If \(|w(t)-w(1)|\leq C(1-t)^\delta\), then
\[
\left|\mu_j-\frac{w(1)}{j+1}\right|
\leq C\int_0^1 t^j(1-t)^\delta\,dt
\leq C' (j+1)^{-1-\delta},
\]
by the beta-integral estimate. Hence the preceding result applies with \(c=w(1)\).

## Verification
The standalone `check.py` performs exact-fraction finite-section commutator and moment tests and independent numerical quadrature diagnostics for the continuum coefficient. Run with `python3 check.py` using the Python standard library. Such finite diagnostics are not an infinite-dimensional proof; the proof is the estimates and exact integral above.

## Relationship to prior work
The classical Hilbert matrix and its generalized moment Hankel matrices are well-established. Chatzifountas, Girela and Peláez (2013, arXiv:1309.6125) characterize boundedness and Schatten membership of the Hankel matrices themselves. Xu and Ye (2023, DOI 10.3934/math.2023466) study derivative-Hilbert operators between analytic function spaces. Frank, Sukochev and Zanin (2024, arXiv:2405.10652) prove endpoint Schatten properties for commutators with powers of the Laplacian on Euclidean spaces. The present calculation concerns a different operator family and a small-parameter Hilbert–Schmidt norm coefficient; none of these stated results determines that coefficient.

## Limitations
The asymptotic requires a polynomially decaying remainder in the moment sequence and is asserted only as \(\alpha\downarrow0\). For \(c=0\), the theorem yields an \(O(\alpha^2)\) upper bound for the squared norm, not a universal next coefficient. No trace-class, spectral-distribution, or general \(\ell^p\) assertion is made. Prior results under a different Mellin/Hankel commutator formulation may exist; independent verification and a definitive literature-wide priority assessment have not been performed.

## References
1. C. Chatzifountas, D. Girela and J. Á. Peláez, *A generalized Hilbert matrix acting on Hardy spaces*, arXiv:1309.6125 (first version 2013-09-24), especially the introductory operator definition and Theorem 5. https://arxiv.org/abs/1309.6125
2. Y. Xu and S. Ye, *A Derivative Hilbert operator acting from Bergman spaces to Hardy spaces*, AIMS Mathematics 8 (2023), 9290–9302, DOI 10.3934/math.2023466 (published 2023-02-15), especially Sections 3–4. https://www.aimspress.com/aimspress-data/math/2023/4/PDF/math-08-04-466.pdf
3. R. L. Frank, F. Sukochev and D. Zanin, *Endpoint Schatten class properties of commutators*, arXiv:2405.10652 (first version 2024-05-17), especially Theorems 1.1–1.2. https://arxiv.org/abs/2405.10652
