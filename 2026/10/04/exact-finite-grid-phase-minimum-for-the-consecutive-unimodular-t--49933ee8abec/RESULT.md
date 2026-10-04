# Exact finite-grid phase minimum for the consecutive unimodular trinomial

## Finding
For every integer \(N\ge 3\), let \(\zeta_N=e^{2\pi i/N}\) and define
\[
P_N=\min_{|u|=|v|=1}\max_{k\in\mathbb Z_N}\left|1+u\zeta_N^k+v\zeta_N^{2k}\right|^2.
\]
Then
\[
P_N=\begin{cases}
1+4\cos(\pi/N),&N\text{ odd},\\
3+2\cos(2\pi/N)=1+4\cos^2(\pi/N),&N\text{ even}.
\end{cases}
\]
For odd \(N\), one may take \(v=1\) and any unimodular \(u\) satisfying \(\operatorname{Re}u=\cos(\pi/N)-1\). For even \(N\), one may take
\[
v=e^{2\pi i/N},\qquad u=e^{i(\pi/2+\pi/N)}.
\]
Thus the sampled phase minimum tends to the continuous squared minimum \(5\), but with a parity-dependent second-order deficit:
\[
5-P_N=\frac{2\pi^2}{N^2}+O(N^{-4})\quad(N\text{ odd}),
\qquad
5-P_N=\frac{4\pi^2}{N^2}+O(N^{-4})\quad(N\text{ even}).
\]

## Assumptions and scope
The coefficients all have modulus one, the spectrum is the consecutive three-point set \(\{0,1,2\}\), and the norm is sampled on the complete \(N\)-th-root grid. The theorem concerns every integer \(N\ge3\). It does not claim an optimum when coefficient moduli are allowed to vary, nor for nonconsecutive three-point spectra.

## Proof
Write \(u=e^{i\alpha}\), \(v=e^{i\beta}\), set \(\theta=\beta/2\), and put
\[
c=\cos(\alpha-\beta/2),\qquad y_k=\theta+\frac{2\pi k}N.
\]
A direct expansion gives
\[
\left|1+u\zeta_N^k+v\zeta_N^{2k}\right|^2
=1+4c\cos y_k+4\cos^2y_k.
\]
For a fixed rotation \(\theta\), define
\[
p=\max_k\cos y_k,\qquad -r=\min_k\cos y_k.
\]
For \(N\ge3\), both \(p\) and \(r\) are positive. Let
\[
F_c(x)=1+4cx+4x^2.
\]
Since \(F_c\) is convex, its maximum over the sampled cosine values is bounded by the larger of its values at the two extreme sampled cosines \(p\) and \(-r\); for the balancing choice \(c=r-p\), those endpoint values coincide. Indeed,
\[
F_{r-p}(p)=F_{r-p}(-r)=1+4pr.
\]
Conversely, for any \(c\), the sample maximum is at least \(\max\{F_c(p),F_c(-r)\}\), and the first of these endpoint values increases with \(c\) while the second decreases. Hence their minimum possible maximum occurs exactly at \(c=r-p\). Because \(|r-p|\le1\), this value of \(c\) is realized by a unimodular \(u\). Therefore
\[
P_N=1+4\min_\theta p(\theta)r(\theta).
\]

It remains to solve a regular-polygon geometry problem. Let \(a\in[0,\pi/N]\) be the angular distance from \(0\) to the nearest point of the rotated \(N\)-grid.

If \(N\) is even, the grid is antipodally symmetric, so
\[
p=r=\cos a.
\]
The minimum occurs at the half-step rotation \(a=\pi/N\), giving
\[
\min_\theta pr=\cos^2(\pi/N).
\]
Taking \(\theta=\pi/N\) and \(c=0\) gives the displayed even extremizer.

If \(N\) is odd, antipodes fall halfway between grid points. The nearest distances to the two axes \(0\) and \(\pi\) are therefore \(a\) and \(\pi/N-a\). Thus
\[
pr=\cos a\,\cos(\pi/N-a)
=\frac{\cos(\pi/N)+\cos(2a-\pi/N)}2.
\]
Since \(|2a-\pi/N|\le\pi/N\),
\[
pr\ge\cos(\pi/N),
\]
with equality when \(a=0\) or \(a=\pi/N\). At \(a=0\), one has \(v=1\), \(p=1\), \(r=\cos(\pi/N)\), and the balancing condition becomes \(c=\cos(\pi/N)-1\), yielding the displayed odd extremizer.

Substitution gives the two exact formulas. The asymptotic expansions follow from the Taylor series of cosine at the origin.

## Verification
The proof is analytic and covers all \(N\ge3\). The accompanying standard-library program `verify.py` is only a finite corroboration: it reconstructs the explicit extremizers, checks their sampled peaks against the formulas for \(3\le N\le1200\), and independently tests the endpoint-balancing reduction on deterministic rotated grids. It is not used to infer the infinite theorem.

## Relationship to prior work
Neuwirth's trigonometric-trinomial work formulates the continuous complex Mandel'shtam phase problem for prescribed coefficient moduli and proves monotonicity with respect to the phase parameter. For the consecutive equal-modulus trinomial, that continuous problem has squared optimum \(5\). The theorem here instead samples only the complete \(N\)-th-root grid and determines the exact finite-grid optimum for every \(N\), including the parity-dependent correction and explicit extremizers.

Graham and Ramsey study Sidon constants of finite sets and classify the exceptional three-element extremal cases arising from \(\mathbb Z_3\) and \(\{0,1,2\}\subset\mathbb Z_4\). That result addresses a different optimization in which coefficient magnitudes vary; it neither states nor implies the fixed-equal-modulus all-\(N\) formulas above.

## Limitations
The result is restricted to three consecutive characters with equal coefficient moduli. It does not classify all minimizing phase pairs, and it does not address arbitrary three-frequency supports. The closest identified literature uses different objectives or the continuous circle; unindexed sequence-design or communications literature using crest-factor terminology remains a residual originality risk.

## References
1. S. Neuwirth, *The maximum modulus of a trigonometric trinomial*, arXiv:math/0703236, first public version 2007-03-08; DOI: 10.1007/s11854-008-0028-2.
2. R. L. Graham and L. T. Ramsey, *Sidon Sets with Extremal Sidon Constants*, Proc. Amer. Math. Soc. 83 (1981), DOI: 10.1090/S0002-9939-1981-0627683-3.
