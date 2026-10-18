# Unique offset and second-order gain for diagonal cube-section pyramids

## Finding

For every integer \(n\geq3\), consider the unit cube \(Q_n=[0,1]^n\) and its diagonal hyperplane sections
\[
H_t=\{x\in\mathbb R^n:\ \sum_{i=1}^n x_i=n/2+t\},\qquad -n/2<t<n/2.
\]
Let \(D_n\) be the largest volume of a pyramid contained in \(Q_n\), with base \(Q_n\cap H_t\) for some \(t\), and with unrestricted apex in \(Q_n\). Let \(c_n\) denote the largest volume for this same diagonal family when \(t=0\).

Write \(f_n\) for the probability density of a sum of \(n\) independent uniform random variables on \([-1/2,1/2]\). Then
\[
D_n=\max_{0\leq t<n/2}\frac{n/2+t}{n}\,f_n(t),\qquad c_n=\frac12f_n(0).
\]
The maximum is attained at exactly one offset \(t_n>0\) (apart from the symmetric reflection \(t\mapsto-t\)); the apex is the opposite cube vertex. As \(n\to\infty\),
\[
\boxed{t_n=\frac16+\frac{2}{45n}+O(n^{-2})},\qquad
\boxed{\frac{D_n}{c_n}=1+\frac1{6n}+\frac7{120n^2}+O(n^{-3})}.
\]
Equivalently,
\[
\boxed{D_n=\sqrt{\frac3{2\pi n}}\left(1+\frac1{60n}+\frac{73}{3360n^2}+O(n^{-3})\right)}.
\]
The \(O\)-constants are absolute. In dimension three,
\[
t_3=\frac{\sqrt2-1}{2},\qquad D_3=\frac{1+\sqrt2}{6},
\]
which coincides with the already-known *unrestricted* cube-pyramid maximum in dimension three. The general unrestricted maximum \(M_n\) therefore satisfies \(M_n\ge D_n\), giving an explicit second-order high-dimensional lower benchmark rather than only the known strict inequality \(M_n>c_n\).

## Assumptions and scope

All volumes are ordinary \(n\)-dimensional Euclidean volumes. A pyramid means the convex hull of its entire hyperplane-section base and one apex in the cube. The hyperplane direction is constrained to a main diagonal, but its offset and the apex are not prescribed. The exact and asymptotic assertions hold for every integer \(n\ge3\); the latter concern \(n\to\infty\). Symmetry permits taking \(t\ge0\). No claim is made that \(D_n=M_n\) for \(n\ge4\).

The density has the finite exact form, for \(|t|<n/2\),
\[
f_n(t)=\frac1{(n-1)!}\sum_{k=0}^{\lfloor n/2+t\rfloor}(-1)^k\binom nk\,(n/2+t-k)^{n-1}.
\]
At an integer endpoint the zero-power ambiguity is interpreted by continuity; this expression is a polynomial on each open chamber.

## Proof

**Geometric reduction.** Apply the coarea formula to the linear map \(x\mapsto\sum_i x_i\). The section area is \(\sqrt n\,f_n(t)\). For \(t\ge0\), the maximal perpendicular distance of a point of the cube to \(H_t\) is \((n/2+t)/\sqrt n\), attained at the all-zero vertex. The pyramid volume is one \(n\)-th of base area times height. The optimum over apices for fixed \(t\ge0\) is therefore exactly \((n/2+t)f_n(t)/n\). Reflection takes negative offsets to positive offsets with the same best volume.

**Uniqueness at every dimension.** The uniform density on an interval is log-concave, and convolution preserves log-concavity, so \(f_n\) is positive and log-concave in \((-n/2,n/2)\). Since \(t\mapsto\log(n/2+t)\) is strictly concave there, the product \((n/2+t)f_n(t)\) is strictly log-concave. It vanishes at both endpoints and hence has one unique maximizer. For \(n\ge3\), differentiability and symmetry give \(f_n'(0)=0\), while the derivative of the product at zero is \(f_n(0)>0\). Thus its unique maximum has \(t_n>0\). Its exact characterization is
\[
\frac{f'_n(t_n)}{f_n(t_n)}=-\frac1{n/2+t_n}.
\]
For \(n=3\) the central piece is \(f_3(t)=3/4-t^2\), \(0\le t\le1/2\). Differentiating \((3/2+t)f_3(t)\) yields \(t_3=(\sqrt2-1)/2\); strict log-concavity ensures this is the global restricted maximizer. Direct substitution gives \(D_3=(1+\sqrt2)/6\).

**Uniform Fourier expansion.** Write \(\phi(s)=\sin(s/2)/(s/2)\). For large \(n\) the Fourier inversion formula (valid with the derivatives used here) gives
\[
f_n(t)=\frac1{2\pi\sqrt n}\int_{\mathbb R}\exp(-itu/\sqrt n)\,\phi(u/\sqrt n)^n\,du.
\]
The analytic logarithm at zero satisfies
\[
\log\phi(s)=-\frac{s^2}{24}-\frac{s^4}{2880}-\frac{s^6}{181440}+O(s^8).
\]
Fix \(T>0\). For \(|t|\le T\), expand after restricting to \(|u|\le n^{1/12}\), using \(\phi(u/\sqrt n)^n=e^{-u^2/24}(1-u^4/(2880n)+(u^8/(2\cdot2880^2)-u^6/181440)/n^2+O(n^{-3}p(u)))\) with an integrable Gaussian-weighted polynomial \(p\). On \(n^{1/12}<|u|<\delta\sqrt n\), a Gaussian bound \(|\phi(u/\sqrt n)|^n\le e^{-cu^2}\) makes the contribution smaller than any fixed power of \(n^{-1}\). On \(|u|\ge\delta\sqrt n\), the strict bound \(|\phi(s)|<1\) away from zero and the \(O(|s|^{-1})\) decay make the tail exponentially small. The same estimates justify differentiating once in \(t\). All remainders below are uniform, including one \(t\)-derivative, on fixed compact \(t\)-intervals.

Using Gaussian moments \(\mathbb Eu^2=12\), \(\mathbb Eu^4=432\), \(\mathbb Eu^6=25920\), \(\mathbb Eu^8=2177280\) for \(u\sim N(0,12)\), termwise integration gives
\[
 f_n(t)=\sqrt{\frac6{\pi n}}\left[1-\frac{3/20+6t^2}{n}+\frac{-13/1120+(9/2)t^2+18t^4}{n^2}+O_T(n^{-3})\right],
\]
and the derivative expansion gives
\[
\frac{f_n'(t)}{f_n(t)}=-\frac{12t}{n}+\frac{36t}{5n^2}+O_T(n^{-3}).
\]
Consequently, uniformly for bounded \(t\),
\[
\frac d{dt}\log[(n/2+t)f_n(t)]
=\frac{2-12t}{n}+\frac{16t}{5n^2}+O_T(n^{-3}).
\]
For any fixed \(a<1/6<b\), this derivative is positive at \(a\) and negative at \(b\) for all sufficiently large \(n\). Strict log-concavity puts \(t_n\) in \((a,b)\), and substitution into the derivative expansion first shows \(t_n=1/6+O(n^{-1})\), then shows \(t_n=1/6+2/(45n)+O(n^{-2})\).

**Optimized volume.** Division of the uniform density expansion at \(t\) by that at zero yields
\[
\frac{f_n(t)}{f_n(0)}=1-\frac{6t^2}{n}+\frac{(18/5)t^2+18t^4}{n^2}+O_T(n^{-3}).
\]
Multiplying by \(1+2t/n\) gives
\[
\frac{(n/2+t)f_n(t)/n}{c_n}=1+\frac{2t-6t^2}{n}+\frac{(18/5)t^2-12t^3+18t^4}{n^2}+O_T(n^{-3}).
\]
The first correction is stationary at \(t=1/6\), so replacing \(t=1/6\) by \(t=t_n=1/6+O(n^{-1})\) changes only the \(O(n^{-3})\) remainder. Evaluation gives \(D_n/c_n=1+1/(6n)+7/(120n^2)+O(n^{-3})\). Finally the central density expansion yields
\[
c_n=\sqrt{\frac3{2\pi n}}\left(1-\frac3{20n}-\frac{13}{1120n^2}+O(n^{-3})\right),
\]
so multiplication gives the displayed absolute expansion with coefficient \(73/3360\).

## Verification

The accompanying standalone `verify_diagonal_pyramid.py` checks exact Gaussian moment arithmetic and all displayed second-order coefficient identities using rational numbers. It checks the three-dimensional closed form algebraically and independently integrates the characteristic-function formula for several larger dimensions to test the offset and volume asymptotics. The checker is corroborative only: strict uniqueness and uniform error estimates follow from the analytical arguments above, not finite numerical tests.

## Relationship to prior work

Nikolov (2026, arXiv:2610.14047v1, Theorem 4 and Propositions 1–3) determines the optimal *central* pyramid \(c_n\), proves \(nM_n<(n+1)c_{n+1}\), establishes \(M_n>c_n\), and gives \(M_3=(1+\sqrt2)/6\). The present result neither reproves those as novel nor determines unrestricted \(M_n\) in higher dimensions. Its new invariant is the globally optimized **offset along the fixed main-diagonal direction** and its explicit sharp second-order asymptotics.

Ambrus and Gárgyán (2025) give central Laplace–Pólya asymptotics and discrete ratio estimates, but not the off-center pyramid optimizer. Bartha–Fodor–González Merino (2020) study central main-diagonal section volumes. Pournin (2023 preprint) studies local extremality of noncentral **section area over directions at fixed distance**, rather than maximizing section area times apex height over the offset. These statements do not imply the optimized off-center volume expansion without the present analysis.

## Limitations

The theorem optimizes offsets within the main-diagonal normal family only. It does not prove that a diagonal direction maximizes a noncentral pyramid among all normals for \(n\ge4\); it does not establish the unrestricted second-order asymptotic of \(M_n\); and it does not provide a finite-\(n\) elementary formula for \(t_n\) in general. The \(O\)-terms are asymptotic rather than claimed explicit universal numerical bounds. Published priority beyond the inspected material is not independently certified.

## References

1. N. Nikolov, *Maximal volumes of pyramids in the unit cube*, arXiv:2610.14047v1 (first submitted 2026-10-04), https://arxiv.org/html/2610.14047v1.
2. G. Ambrus and B. Gárgyán, *Estimates on the decay of the Laplace–Pólya integral*, Bulletin of the London Mathematical Society 57 (2025), 3360–3379, https://doi.org/10.1112/blms.70157; arXiv:2412.12835.
3. F. Bartha, F. Fodor, and B. González Merino, *Central diagonal sections of the \(n\)-cube*, arXiv:2005.08292 (2020), https://arxiv.org/abs/2005.08292.
4. L. Pournin, *Local extrema for hypercube sections*, arXiv:2203.15054v2 (2023), https://arxiv.org/pdf/2203.15054.
