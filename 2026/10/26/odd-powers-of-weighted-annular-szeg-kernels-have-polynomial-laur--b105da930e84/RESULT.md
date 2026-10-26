# Odd powers of weighted annular Szegő kernels have polynomial Laurent multipliers

## Finding
For every \(0<q<1\), every \(r>0\), and every **odd positive integer** \(L\), define
\[
\mathcal S_{q,r}(t)=\sum_{n\in\mathbb Z}\frac{t^n}{1+r q^{2n}},\qquad q^2<|t|<1.
\]
There is an explicitly computable **real polynomial** \(P_{L,q,r}\) of degree \(L-1\), with leading coefficient \(1/(L-1)!\), for which the following identity holds locally uniformly and absolutely throughout the annulus:
\[
\boxed{\mathcal S_{q,r}(t)^L=\sum_{n\in\mathbb Z}\frac{P_{L,q,r}(n)}{1+r^L q^{2n}}\,t^n.}
\]
Every coefficient on the right is strictly positive; consequently \(P_{L,q,r}(n)>0\) for every integer \(n\). Equivalently, with \(\mathcal D=t\,d/dt\), the odd-power kernel is \(P_{L,q,r}(\mathcal D)\mathcal S_{q,r^L}\).

The first previously unresolved exponent has a particularly simple specialization. At the conformally invariant Szegő weight \(r=q\), put
\[
E(q)=\sum_{k=0}^{\infty}\frac{(2k+1)q^{2k+1}}{1+q^{2k+1}}>0.
\]
Then
\[
\boxed{\mathcal S_{q,q}(t)^3=\sum_{n\in\mathbb Z}\frac{\binom{n+2}{2}+3E(q)}{1+q^{2n+3}}\,t^n,}
\qquad
\binom{n+2}{2}=\frac{(n+1)(n+2)}2.
\]
For \(q=e^{-h}\) with \(h\downarrow0\), the correction has the sharp thin-annulus scale
\[
\boxed{E(e^{-h})\sim\frac{\pi^2}{24h^2}.}
\]

## Assumptions and scope
All parameters are real with \(0<q<1\), \(r>0\), and \(L\in\{1,3,5,\ldots\}\). The variable \(t\) is complex and satisfies \(q^2<|t|<1\). Binomial expressions at integer arguments are interpreted as their defining polynomials; in particular \(\binom{n+2}{2}=(n+1)(n+2)/2\), even for negative integers.

For a point \(z\) in the geometric annulus \(q<|z|<1\), the covariance kernel \(\mathcal S_{q,r}(z\overline w)^L\) has an explicit i.i.d.-Gaussian Laurent realization
\[
X_{q,r}^{(L)}(z)=\sum_{n\in\mathbb Z}\zeta_n\sqrt{\frac{P_{L,q,r}(n)}{1+r^Lq^{2n}}}\,z^n,
\]
where the \(\zeta_n\) are independent standard circular complex Gaussian variables. Its series converges locally uniformly almost surely, as its nonnegative coefficient squared norms sum locally uniformly on the annulus. The construction concerns the covariance and explicit Laurent coefficients; it does not claim a new zero-point correlation formula or extend the polynomial representation to even exponents.

## Proof
**1. Global quasi-periodicity.** The theta-product representation of the weighted Szegő kernel, or the Jacobi triple product, meromorphically continues \(\mathcal S_{q,r}\) from the annulus to \(\mathbb C^{\times}\). Its poles lie at \(t=q^{2k}\), \(k\in\mathbb Z\), and are simple. The theta functional equation gives
\[
\mathcal S_{q,r}(q^2t)=-r^{-1}\mathcal S_{q,r}(t).
\]
The residue normalization at \(t=1\) is fixed by \(\mathcal S_{q,r}(t)=(1-t)^{-1}+O(1)\). Thus \(\mathcal S_{q,r}^L\) and every Euler derivative \(\mathcal D^j\mathcal S_{q,r^L}\) transform by the **same multiplier** \(-r^{-L}\) when \(L\) is odd. This parity condition is essential to the argument.

**2. Explicit regular Taylor coefficients.** Set
\[
u_k=\frac{r q^{2k}}{1+r q^{2k}},\qquad
v_k=\frac{q^{2k+2}}{r+q^{2k+2}}\quad(k\ge0).
\]
Rearranging absolutely convergent Laurent series on \(q^2<|t|<1\) yields
\[
\mathcal S_{q,r}(t)=\frac1{1-t}+\sum_{k=0}^{\infty}\left(v_kt^{-k-1}-u_kt^k\right).
\]
Both tails converge normally in a neighborhood of \(t=1\). With \(\delta=1-t\), write
\[
\mathcal S_{q,r}(1-\delta)=\delta^{-1}+\sum_{h\ge0}c_h\delta^h,
\quad
c_h=\sum_{k\ge0}\left[v_k\binom{k+h}{h}-(-1)^hu_k\binom{k}{h}\right].
\]
The last sum converges absolutely, since its summands are bounded by a polynomial in \(k\) times \(q^{2k}\). The convention is \(\binom{k}{h}=0\) when \(k<h\).

**3. Finite constructive recursion.** For the given odd \(L\), form the truncated polynomial
\[
B_L(\delta)=1+\sum_{h=0}^{L-2}c_h\delta^{h+1},
\]
with an empty sum when \(L=1\). The principal part of \(\mathcal S_{q,r}(1-\delta)^L\) is precisely the negative-power part of \(\delta^{-L}B_L(\delta)^L\). For each \(j\ge0\), the principal part of \(\mathcal D^j\mathcal S_{q,r^L}\) equals that of \(\mathcal D^j\delta^{-1}\), whose highest pole is \(j!\delta^{-j-1}\). The principal parts for \(j=0,\ldots,L-1\) are therefore a triangular basis. Match powers \(\delta^{-L},\ldots,\delta^{-1}\) successively to obtain unique real scalars \(a_{L-1},\ldots,a_0\), with \(a_{L-1}=1/(L-1)!\). Define
\[
P_{L,q,r}(x)=\sum_{j=0}^{L-1}a_jx^j.
\]
Only \(c_0,\ldots,c_{L-2}\), explicitly summed above, are needed; this is an algorithm for each fixed odd \(L\), not an existence argument hiding an infinite linear system.

**4. Cancellation at every pole and uniqueness.** Let
\[
F(t)=\mathcal S_{q,r}(t)^L-P_{L,q,r}(\mathcal D)\mathcal S_{q,r^L}(t).
\]
Its principal part at \(t=1\) vanishes by construction. Quasi-periodicity and commutation of \(\mathcal D\) with dilation transfer that cancellation to each \(q^{2k}\); the theta product shows there are no other poles. Hence \(F\) is holomorphic on \(\mathbb C^{\times}\) and obeys \(F(q^2t)=-r^{-L}F(t)\). Write the global Laurent expansion \(F(t)=\sum_{n\in\mathbb Z}b_nt^n\). Coefficient comparison gives
\[
(q^{2n}+r^{-L})b_n=0\qquad(n\in\mathbb Z).
\]
Every parenthesis is positive, so \(b_n=0\) for all integers, proving the exact differential and Laurent identities. Termwise differentiation of \(\mathcal S_{q,r^L}\) is justified by local normal convergence.

**5. Strict positivity and Gaussian realization.** Every Laurent coefficient of \(\mathcal S_{q,r}\) is strictly positive. The coefficient of \(t^n\) in the integer \(L\)-fold Cauchy product is an absolutely convergent sum of positive terms (with at least one term), hence positive. Our identity identifies that coefficient with \(P_{L,q,r}(n)/(1+r^Lq^{2n})\). The denominator is positive. The stated Gaussian series then has exactly the required covariance; standard Gaussian-series compact convergence follows from the locally bounded sum of variances.

**6. Cubic identity and thin-annulus constant.** At \(r=q\), \(u_k=v_k=q^{2k+1}/(1+q^{2k+1})\); therefore \(c_0=0\) and
\[
c_1=\sum_{k\ge0}(2k+1)\frac{q^{2k+1}}{1+q^{2k+1}}=E(q).
\]
Thus \(\mathcal S_{q,q}^3=\delta^{-3}+3E(q)\delta^{-1}+O(1)\). Since
\[
\mathcal D\delta^{-1}=\delta^{-2}-\delta^{-1},\qquad
\mathcal D^2\delta^{-1}=2\delta^{-3}-3\delta^{-2}+\delta^{-1},
\]
the unique matching operator is \(\tfrac12\mathcal D^2+\tfrac32\mathcal D+(1+3E(q))\), giving the displayed cubic coefficients. Finally, with \(q=e^{-h}\),
\[
E(q)=h^{-1}\sum_{k\ge0}\frac{(2k+1)h}{e^{(2k+1)h}+1}
\sim \frac1{2h^2}\int_0^\infty\frac{x}{e^x+1}\,dx
=\frac{\pi^2}{24h^2}.
\]
The Riemann-sum step is justified by exponential tail domination, and the integral is \(\pi^2/12\) by its alternating exponential series.

## Verification
The standalone script `verification/check_odd_powers.py` recomputes the triangular recursion from the regular-coefficient sums at 80-digit precision. It tests \(L=1,3,5,7\), three self-dual and three non-self-dual weights, two complex arguments per parameter, the exact cubic correction at 25 positive/negative integer indices in each of three cases, and positivity of coefficient samples. It passed 123 kernel-power/cubic comparisons in addition to 24 leading-term and 600 positivity assertions; it also prints the independently computed thin-annulus normalized correction at three widths. These are consistency tests, not substitutes for the preceding proof of the universal theorem.

To reproduce with Python 3 and `mpmath`, run `python verification/check_odd_powers.py` after extracting the file from the same package.

## Relationship to prior work
Katori and Shirai (arXiv:2008.04177v1, Remark 1 following Proposition 1.1, and Appendix C) introduce the higher-power annular Gaussian analytic functions and explicitly report no known explicit Gaussian Laurent series for exponents \(L\ge3\); they give the exponent-two Bergman series. Their theta expression for \(\mathcal S_{q,r}\) and the older annular Szegő-kernel functional identities supply the foundational quasiperiodicity used here. The new result is the **single Laurent sum with an exact degree-\(L-1\) polynomial numerator for every odd exponent**, and particularly the explicit cubic coefficient sequence. It is not merely the known, unevaluated multiple convolution.

McCullough and Shen (1994) study the annular kernel's theta identities and extremal problems. Gafai, Murid, and Wahid (arXiv:2202.09114v1, Sections 3 and 5) derive product and bilateral representations of the weighted Szegő kernel itself. The inspected statements do not present the above all-odd differential reduction, cubic Laurent coefficients or thin-annulus correction. No assertion of absolute priority is possible from a bounded literature check; classical elliptic-function derivative identities might yield equivalent formulas in other notation.

## Limitations
The polynomial representation is proved for **odd positive integer powers** and arbitrary positive weight; no result for even powers \(L\ge4\) is claimed. The thin-annulus asymptotic concerns the cubic self-dual correction only. Positivity is proved for integer arguments of the polynomial, not every real argument. The i.i.d. Gaussian representation determines covariance but does not by itself establish novel zero-point correlation laws. Numerical verification samples finitely many parameters and cannot certify every \(q,r,L\). Historical-priority uncertainty remains, especially under equivalent theta/Fay/Kronecker derivative formulations.

## References
1. M. Katori and T. Shirai, *Zeros of the i.i.d. Gaussian Laurent series on an annulus: weighted Szegő kernels and permanental-determinantal point processes*, arXiv:2008.04177v1 (first posted 2020-08-10), especially Remark 1, formula (1.6), Appendix C. https://arxiv.org/abs/2008.04177
2. S. McCullough and L.-C. Shen, *On the Szegő kernel of an annulus*, Proceedings of the American Mathematical Society **121** (1994), 1111–1121, DOI: 10.1090/S0002-9939-1994-1189748-9.
3. N. S. Gafai, A. H. M. Murid, and N. H. A. A. Wahid, *Infinite product representation for the Szegő kernel for an annulus*, arXiv:2202.09114v1 (2022-02-18), especially Sections 3 and 5. https://arxiv.org/abs/2202.09114
