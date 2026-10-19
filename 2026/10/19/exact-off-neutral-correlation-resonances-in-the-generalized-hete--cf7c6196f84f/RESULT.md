# Exact off-neutral correlation resonances in the generalized heterochaos baker map

## Finding

For the two-dimensional generalized heterochaos baker map with two contracting branches, the complete Lebesgue-stationary covariance generating function of the central coordinate is algebraic. It exhibits two **off-neutral pole–branch collisions**, at \(a=1/10\) and \(a=2/5\), separate from the known center-neutral parameter \(a=1/4\). The collisions change the dominant covariance prefactor from a pure exponential to an exponential times \(n^{-1/2}\); between them the prefactor is instead \(n^{-3/2}\), with a parity effect. The Green–Kubo variance is an explicit rational, piecewise smooth function with a unique cusp maximum at the neutral parameter.

Put \(q=1-2a\), \(0<a<1/2\), and
\[
 r_a(z)=\frac{1-\sqrt{1-8aqz^2}}{2qz},\qquad r_a(0)=0,
 \qquad H_a(w)=\frac{4(2a+qw^2)}{(2-w)(4a-qw)}.
\]
For normalized Lebesgue measure \(m\) on the unit square, let
\[
 C_n(a)=\int_{[0,1]^2}(y-1/2)\bigl(\pi_y F_a^n(x,y)-1/2\bigr)\,dm(x,y),
 \qquad c_n(a)=12C_n(a).
\]
Then for every \(n\ge0\), the Taylor coefficients at zero satisfy
\[
 \boxed{\sum_{n\ge0}c_n(a)z^n=H_a(r_a(z)).}
\]
All \(c_n(a)>0\). For the following asymptotics put \(\rho=\sqrt{8aq}\) and \(u=\sqrt{2a/q}\). For each **fixed** admissible \(a\), as \(n\to\infty\):
\[
 \begin{array}{ll}
 0<a<1/10:&c_n(a)\sim \dfrac{1-10a}{1-4a}\left(\dfrac{1+6a}{2}\right)^n,\\[6pt]
 a=1/10\text{ or }a=2/5:&c_n(a)\sim\dfrac{4\sqrt2}{3\sqrt\pi}\,(4/5)^n n^{-1/2},\\[6pt]
 1/10<a<2/5:&c_n(a)\sim \dfrac{u}{\sqrt{2\pi}}\bigl[H_a'(u)-(-1)^nH_a'(-u)\bigr] \rho^n n^{-3/2},\\[6pt]
 2/5<a<1/2:&c_n(a)\sim \dfrac{2(5a-2)}{4a-1}(2-3a)^n.
 \end{array}
\]
The parity-dependent constants in the third regime are strictly positive. The exponential factors are below one at all \(a\ne1/4\); at \(a=1/4\) the known neutral \(n^{-3/2}\) law is recovered as a special case, not claimed as a new neutral asymptotic.

The absolutely convergent Green–Kubo series and the asymptotic time-average variance are
\[
 \sum_{n\ge0}c_n(a)=
 \begin{cases}2/(1-3a),&0<a\le1/4,\\4/(6a-1),&1/4\le a<1/2,\end{cases}
\]
\[
 \boxed{\lim_{N\to\infty}\frac1N\operatorname{Var}_m\!\left(\sum_{t=0}^{N-1}\bigl(\pi_y F_a^t-1/2\bigr)\right)
 =\begin{cases}\dfrac{1+a}{4(1-3a)},&0<a\le1/4,\\[4pt]\dfrac{3-2a}{4(6a-1)},&1/4\le a<1/2.\end{cases}}
\]
This variance is maximized uniquely at \(a=1/4\), where it equals \(5/4\); its one-sided derivatives there are \(+16\) and \(-16\). No central-limit theorem is required or asserted.

## Assumptions and scope

The map \(F_a\colon[0,1]^2\to[0,1]^2\), defined up to negligible partition boundaries, is
\[
 F_a(x,y)=\begin{cases}
 (x/a,\,y/2),&0\le x<a,\\
 ((x-a)/a,\,(y+1)/2),&a\le x<2a,\\
 ((x-2a)/q,\,2y\bmod1),&2a\le x\le1.
 \end{cases}
\]
The final branch is split at \(y=1/2\) into two affine pieces. The theorem concerns exactly \(M=2\), every real \(a\in(0,1/2)\), and Lebesgue-stationary covariance of the centered second coordinate. Nothing is asserted about arbitrary observables, nonstationary initial distributions, or the full transfer-operator spectrum. Lebesgue invariance follows by the inverse-branch densities: the first two strips together contribute \(2a\), and the expanding strip contributes \(q\), totaling one. The source's maps also have a three-dimensional invertible extension, but the present statement needs only its two-dimensional factor.

## Proof

**1. Exact observable closure.** Under normalized Lebesgue measure the base-map branch itinerary is i.i.d., with probabilities \(a,a,q\), and is independent of the initial fiber coordinate. Define for every integer \(k\ge0\)
\[
 f_k(y)=\{2^ky\}-1/2,
\]
with \(\{\cdot\}\) the fractional part (endpoint conventions have measure zero). Average one step of the central dynamics conditional on \(y\):
\[
 Pf_0=af_0+qf_1,\qquad Pf_k=2af_{k-1}+qf_{k+1}\quad(k\ge1).
\]
Here the coefficient deficit in the first identity is genuine: the two half-affine branches combine to \(af_0\), not \(2af_0\). Direct dyadic integration gives
\[
 12\int_0^1 f_0(y)f_k(y)\,dy=2^{-k}.
\]
Therefore \(c_n=12\langle f_0,P^nf_0\rangle\). All coefficients in the displayed operator closure and all dyadic inner products are strictly nonnegative, while a positive coefficient survives every iterate, proving \(c_n>0\).

**2. Resolvent.** For \(|z|\) small define \(g_k(z)=12\sum_{n\ge0}z^n\langle f_0,P^nf_k\rangle\). Then
\[
 g_0=1+z(ag_0+qg_1),\qquad
 g_k=2^{-k}+z(2ag_{k-1}+qg_{k+1})\quad(k\ge1).
\]
The root analytic at the origin of \(r=z(2a+qr^2)\) is \(r=r_a(z)\). The bounded resolvent solution has the form
\[
 g_k=A2^{-k}+Br^k,\quad
 A=\bigl(1-z(4a+q/2)\bigr)^{-1},\quad
 B=-\frac{3azA}{1-z(a+qr)}.
\]
It is the unique solution near \(z=0\) by the Neumann-series inversion of the bounded averaging operator. Substituting the boundary equation gives
\[
 g_0=A\frac{1-z(4a+qr)}{1-z(a+qr)}=H_a(r).
\]
As \(g_0=\sum c_nz^n\), this proves the exact generating function, including its normalization \(c_0=1\).

**3. Singularity and parity classification.** The square-root branch points lie at \(z=\pm\rho^{-1}\). The potentially singular denominators of \(H_a\) are \(w=4a/q\) and \(w=2\), each at a positive real \(w\); along the principal root \(r_a(z)\) a positive pole precedes the branch point precisely for \(a<1/10\) and \(a>2/5\), respectively. Their locations in \(z\) are \(2/(1+6a)\) and \(1/(2-3a)\); their coefficients are the strictly positive residues given in the theorem. At \(a=1/10\) and \(a=2/5\), the unique positive pole coalesces with the branch endpoint. Since
\[
 r_a(z)=u\bigl(1-\sqrt{2(1-\rho z)}+O(1-\rho z)\bigr)
\]
near the positive branch point, the local leading singularity at either collision is \(\frac{4\sqrt2}{3}(1-4z/5)^{-1/2}\). The transfer coefficient is thus \(\frac{4\sqrt2}{3\sqrt\pi}(4/5)^n n^{-1/2}\).

In the intermediate open interval the singularities at both \(+\rho^{-1}\) and \(-\rho^{-1}\) contribute. Their nonanalytic leading terms are respectively \(-u\sqrt2H_a'(u)\sqrt{1-\rho z}\) and \(+u\sqrt2H_a'(-u)\sqrt{1+\rho z}\). The elementary square-root coefficient formula yields exactly the displayed alternating \(n^{-3/2}\) amplitudes. To verify noncancellation, differentiating \(H_a\) and substituting \(w=\pm u\) reduces its numerator to \(48aqw\), with a strictly positive squared denominator; hence \(H_a'(u)>0>H_a'(-u)\). Also \(H_a'(u)>-H_a'(-u)\) because both factors in its positive-root denominator are strictly smaller in magnitude than at the negative root, so both parity constants are positive. No other singularity of equal or smaller modulus is present on the principal algebraic branch, proving the asymptotic equivalents. At \(a=1/4\), \(\rho=1\), but absolute summability follows from the same square-root estimate.

**4. Exact integrated correlation and variance cusp.** On \(z=1\) the selected root solves \(qr^2-r+2a=0\), so
\[
 r_a(1)=\begin{cases}2a/q,&a\le1/4,\\1,&a\ge1/4.\end{cases}
\]
Substitution into \(H_a\) yields the stated Green–Kubo series. Stationarity and absolute summability give
\[
 \lim_{N\to\infty}N^{-1}\operatorname{Var}(\sum_{t<N}(Y_t-1/2))=C_0+2\sum_{n\ge1}C_n=(2G_a(1)-1)/12.
\]
Simplification yields the two rational branches. Their derivatives are \((1-3a)^{-2}>0\) on the left and \(-4(6a-1)^{-2}<0\) on the right, with one-sided values \(+16\), \(-16\) at \(a=1/4\), proving the unique cusp maximum.

## Verification

The accompanying `verify.py` checks 699 exact-arithmetic tests and finite numerical diagnostics, including rational Taylor coefficients, direct dyadic integral enumeration, symbolic residues, pole–branch constants, positivity and large-lag asymptotic comparisons. Its exact direct integrations use explicit branch words and the derivative on each dyadic cell, independently of the symbolic resolvent. Execute `python verify.py` in an environment with Python 3 and SymPy. Computational evidence checks only finite cases; it is not substituted for the all-parameter singularity and Green–Kubo proofs above.

## Relationship to prior work

Takahasi–Yamamoto introduced the generalized maps and their Dyck-shift structure [1]. Takahasi proved mixing and off-neutral exponential mixing [2] and, via time-reversal symmetry, correlation invariance under \(a\leftrightarrow1/2-a\); those results and this symmetry are prior work, not new contributions. Saiki–Takahasi–Yamamoto–Yorke [3, Sec. 2.7 and Fig. 5] directly investigated numerically the same central-coordinate autocorrelation, including \(a=1/3\), and recorded its exponential or polynomial behavior, but did not provide the exact off-neutral generating function, the two resonant pole thresholds, or the integrated-variance cusp. Takahasi–Tsujii [4] subsequently established optimal \(n^{-3/2}\) mixing for neutral maps; the neutral exponent and parameter themselves are not claimed new. The new scope is the full parameter-dependent **exact central-coordinate series and off-neutral resonance structure**; the neutral special case is included only for uniformity. General-purpose singularity analysis is used as a mathematical tool, not claimed as new.

## Limitations

This is a single-observable Lebesgue-stationary result, not a spectral theorem for all smooth functions. The off-neutral asymptotics are pointwise for fixed \(a\); no uniform double-scaling law is proved as \(a\) approaches a resonance. This theorem establishes an asymptotic variance but does not prove a central limit theorem. At the neutral parameter it recovers previously studied algebraic decay; the originality claim concerns the off-neutral exact description and resonance/cusp classification. Earlier results expressing the same formulas through an equivalent operator could exist despite the source comparisons; independent historical and mathematical review is outstanding.

## References

[1] H. Takahasi and K. Yamamoto, *Heterochaos baker maps and the Dyck system: maximal entropy measures and a mechanism for the breakdown of entropy approachability*, arXiv:2209.04905, first posted 11 September 2022, https://arxiv.org/abs/2209.04905.

[2] H. Takahasi, *Exponential mixing for heterochaos baker maps and the Dyck system*, arXiv:2307.08119, 2023, https://arxiv.org/html/2307.08119v1.

[3] Y. Saiki, H. Takahasi, K. Yamamoto and J. A. Yorke, *The dynamics of the heterochaos baker maps*, arXiv:2401.00836, 2024, https://arxiv.org/abs/2401.00836.

[4] H. Takahasi and M. Tsujii, *Polynomial rate of mixing for the heterochaos baker maps with mostly neutral center*, arXiv:2408.16618, first posted 29 August 2024, https://arxiv.org/abs/2408.16618.
