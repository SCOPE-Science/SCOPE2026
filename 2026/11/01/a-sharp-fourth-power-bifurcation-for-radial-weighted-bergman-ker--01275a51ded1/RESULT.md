# A sharp fourth-power bifurcation for radial weighted Bergman kernels

## Finding

For real \(m\geq0\) and integer \(q\in\{0,1,2,3,4\}\), let \(A^2_{m,q}(\mathbb D)\) be the holomorphic Hilbert space on the open unit disk with unnormalized area weight
\[
\omega_{m,q}(z)=|z|^{2m}(1-|z|^2)^q.
\]
Write \(K_{m,q}(z,w)=\mathcal K_{m,q}(z\overline w)\) for its reproducing kernel. The exact number of distinct scalar roots of \(\mathcal K_{m,q}\) in \(\mathbb D\), counted with multiplicity, is
\[
\boxed{N(m,q)=\begin{cases}2,&q=4\text{ and }m>1,\\0,&\text{otherwise}.\end{cases}}
\]
For \(q=4\) and \(m>1\), the two roots are nonreal, conjugate, and simple. At the sharp transition \((m,q)=(1,4)\), the numerator has exactly two simple roots on the unit circle, at \(1-e^{\pm\pi i/3}\), and no root inside. The result is a complete Lu Qi-Keng zero-fibre classification for these five lowest integral boundary exponents, **uniform over every real interior-defect exponent** \(m\ge0\); it makes no claim for \(q\ge5\).

## Assumptions and scope

The weight is positive almost everywhere, and \(m\ge0\) ensures all monomials belong to the weighted Hilbert space. Area measure is the ordinary planar \(dA\), not normalized by \(\pi\). A scalar root \(t\) with \(|t|<1\) corresponds to a genuine off-diagonal kernel zero because \(z\overline w=t\) is solvable with \(z,w\in\mathbb D\). Conversely all such kernel zeros arise from scalar roots. Root multiplicity is the analytic multiplicity in \(t\); the kernel on the bidisk has infinitely many point pairs over each scalar root.

## Proof

**1. Exact moment reduction.** Radial orthogonality of monomials and the beta integral yield, for each integer \(n\ge0\),
\[
\|z^n\|_{m,q}^2=\pi B(n+m+1,q+1)
=\frac{\pi q!}{\prod_{h=1}^{q+1}(n+m+h)}.
\]
Consequently the scalar kernel is
\[
\mathcal K_{m,q}(t)=\frac{1}{\pi q!}\sum_{n=0}^\infty
\left(\prod_{h=1}^{q+1}(n+m+h)\right)t^n,
\qquad |t|<1.
\]
Set \(d=q+1\). As the coefficient is a polynomial in \(n\) of degree \(d\), its \((d+1)\)-st finite difference vanishes. Therefore
\[
\pi q!(1-t)^{d+1}\mathcal K_{m,q}(t)=P_{m,q}(t),
\]
where \(P_{m,q}\) is the explicit degree-at-most-\(d\) polynomial
\[
P_{m,q}(t)=\sum_{j=0}^{d}t^j\sum_{k=0}^{j}(-1)^{j-k}
\binom{d+1}{j-k}\prod_{h=1}^{d}(m+k+h).
\]
The prefactor has no zero or pole in the disk, so the kernel zeros are exactly the disk zeros of this polynomial.

**2. Transfer disk root counts to a half-plane.** Introduce the Cayley variable
\[
t=\frac{s-1}{s+1},\qquad
Q_{m,q}(s)=(s+1)^dP_{m,q}\!\left(\frac{s-1}{s+1}\right).
\]
Then \(|t|<1\) if and only if \(\operatorname{Re}s>0\). Thus the root count is the number of right-half-plane roots of the real polynomial \(Q_{m,q}\). Multiplicities are preserved. All assertions below are exact polynomial identities in the **real** variable \(m\), so no integer-only specialization is used.

For \(q=0,1\), the Cayley polynomials have degrees one and two, respectively, with strictly positive coefficients for every \(m\ge0\), hence all roots have strictly negative real part. For \(q=2\), the cubic Routh first column, from highest to lowest degree, is
\[
6,\quad6(2m+3),\quad8(m+1)(m+2),\quad
2(2m+3)(2m^2+6m+1),
\]
all strictly positive. For \(q=3\), the corresponding quartic first column is
\[
24,\quad48(m+2),\quad8(2m+3)(2m+5),
\quad\frac{32(m+1)(m+2)(m+3)(m^2+4m+6)}{(2m+3)(2m+5)},
\quad8(2m^4+16m^3+40m^2+32m+3),
\]
again strictly positive. The elementary Routh-Hurwitz criterion excludes roots on or to the right of the imaginary axis in all four cases.

**3. The fifth-degree onset.** For \(q=4\), the exact Cayley polynomial, in descending powers of \(s\), has coefficients
\[
\begin{aligned}
&120,\quad120(2m+5),\quad240(m^2+5m+5),\\
&80(2m+5)(m^2+5m+3),\\
&40(2m^4+20m^3+64m^2+70m+15),\\
&8(2m+5)(2m^4+20m^3+60m^2+50m+3).
\end{aligned}
\]
Its Routh first column, from the degree-five row to the constant row, is
\[
\begin{aligned}
&120,\quad120(2m+5),\quad160(m+2)(m+3),\\
&8(2m+3)(2m+5)(2m+7),\\
&-\frac{64(m-1)(m+1)(m+2)(m+3)(m+4)(m+6)}{(2m+3)(2m+7)},\\
&8(2m+5)(2m^4+20m^3+60m^2+50m+3).
\end{aligned}
\]
All entries apart from the penultimate one are strictly positive for \(m\ge0\). When \(0\le m<1\), the remaining entry is positive, so there is no right-half-plane root. When \(m>1\), the sign pattern is \(+,+,+,+,-,+\), with exactly **two** sign changes. The Routh root-count theorem gives exactly two right-half-plane roots, counting multiplicity. A positive real \(s\) cannot be a zero because every displayed coefficient is positive, so these two roots are a nonreal conjugate pair. They are necessarily simple.

At \(m=1\), the exceptional factorization is
\[
Q_{1,4}(s)=120(s+3)(s^2+3)(s^2+4s+7).
\]
Only the factor \(s^2+3\) has roots on the imaginary axis; those roots are simple. Its Cayley images are \(t=1-e^{\pm\pi i/3}\) on \(|t|=1\). The other three roots lie strictly outside \(|t|\le1\). This covers the unique Routh transition without applying a strict-sign criterion at a zero row, and proves the stated classification.

## Verification

The companion standard-library Python program `verify.py` expands the beta-moment numerator, performs the Cayley substitution using exact polynomial arithmetic in \(m\), checks the cubic, quartic and quintic Routh identities by polynomial multiplication, and verifies the \(m=1\) factorization. It prints `BERGMAN_ROUTH_EXACT_POLYNOMIAL_IDENTITIES_OK` on success. Finite numerical root checks can illustrate the transition, but no finite sampling is used to establish the theorem for all real \(m\).

## Relationship to prior work

The classical weighted Bergman monomial expansion is used throughout the subject. Zeytuncu, *Weighted Bergman Projections and Kernels: Lp Regularity and Zeros* (arXiv:1009.2806, 2010), studies existence of zeros for radial disk weights comparable to one, not this sharp two-parameter phase boundary. Jacobson, *Weighted Bergman Kernel Functions and the Lu Qi-Keng Problem* (Texas A&M dissertation, 2012), develops general meromorphic-factor weighted-kernel formulas and explicitly treats the \(|z|^{2p}\) family on the unweighted disk. Those formulas provide background for special integral cases, but do not state the uniform continuous-\(m\), first-five-boundary-exponents classification or the precise Routh bifurcation. Park, *The Zeros of the Bergman Kernel for Some Reinhardt Domains* (2016), uses Routh-Hurwitz in a different family of Reinhardt domains. Perälä, *Vanishing Bergman kernels on the disk* (arXiv:1703.05976, 2017), treats finite zero counts abstractly and constructs other radial weights with zeros. No novelty is claimed for the beta integral, Cayley transform, or Routh-Hurwitz method themselves.

## Limitations

Only integer boundary exponents \(q=0,1,2,3,4\) and real interior exponents \(m\ge0\) are addressed. The general case of nonintegral \(q\) and higher integral exponents is not settled. The count concerns scalar roots in the unit disk, not the global topology of the zero variety in the bidisk. The statement is an independently reproducible mathematical argument, but independent mathematical validation has not been performed. A broader, equivalent prior classification in less searchable weighted-kernel literature remains possible.

## References

1. Y. E. Zeytuncu, *Weighted Bergman Projections and Kernels: Lp Regularity and Zeros*, arXiv:1009.2806 (first public 2010-09-14). https://arxiv.org/abs/1009.2806
2. R. L. Jacobson, *Weighted Bergman Kernel Functions and the Lu Qi-keng Problem*, dissertation, Texas A&M University (repository record 2012-07-16). https://oaktrust.library.tamu.edu/items/b6a215a2-ccf5-45ff-887c-153dcf11237b
3. J. Park, *The Zeros of the Bergman Kernel for Some Reinhardt Domains*, *Journal of Function Spaces* (2016), doi:10.1155/2016/3856096. https://doi.org/10.1155/2016/3856096
4. A. Perälä, *Vanishing Bergman kernels on the disk*, arXiv:1703.05976 (first public 2017-03-17). https://arxiv.org/abs/1703.05976
