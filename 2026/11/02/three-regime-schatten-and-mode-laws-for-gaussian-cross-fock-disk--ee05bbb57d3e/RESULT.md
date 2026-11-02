# Three-regime Schatten and mode laws for Gaussian cross-Fock disk transfer

## Finding
For positive Gaussian parameters \(a,b\) and radius \(R\), disk truncation between one-variable analytic Fock spaces has an exact nuclear norm, strictly controlled modal transitions, and a sharp three-regime Schatten asymptotic. Put \(t=\sqrt{a/b}\) and \(x=bR^2\). For every integer \(n\geq0\), define \(p_n(x)=\mathbb P\{\operatorname{Pois}(x)\geq n+1\}\). The complete (not necessarily decreasingly ordered) singular-value family is
\[
 d_n=t^n p_n(x).
\]
The operator belongs to every \(\mathcal S_p\) with \(p>0\), and
\[
 \|C_R\|_{\mathcal S_1}=\begin{cases}(e^{(t-1)x}-1)/(t-1),&t\ne1,\\x,&t=1.\end{cases}
\]
For each fixed \(p>0\) and fixed \(a,b\), as \(R\to\infty\) (equivalently \(x\to\infty\)),
\[
\sum_{n\ge0}d_n^p\sim
\begin{cases}
 (1-t^p)^{-1},&0<t<1,\\
 x,&t=1,\\
 \dfrac{e^{p(t-1)x}}{(t-1)^p}\dfrac{(2\pi t x)^{(1-p)/2}}{\sqrt p},&t>1.
\end{cases}
\]
For \(t\le1\), the singular-value family is strictly decreasing in \(n\). For \(t>1\), it is strictly log-concave; the maximum is attained at one index or two adjacent indices, and the transition thresholds for successive modes are strictly increasing in \(x\). If \(t>1\), a maximizing index \(n_x\) obeys \(n_x/x\to t\), and
\[
\|C_R\|\sim\frac{e^{(t-1)x}}{(t-1)\sqrt{2\pi t x}}.
\]
More sharply, whenever \((n+1-tx)/\sqrt{tx}\to u\in\mathbb R\), one has \(d_n/\|C_R\|\to e^{-u^2/2}\). At \(t=1\), the Hilbert--Schmidt norm also has the exact formula
\[
\|C_R\|_{\mathcal S_2}^2=x\{1-e^{-2x}[I_0(2x)+I_1(2x)]\}=x-\sqrt{x/\pi}+O(x^{-1/2}),
\]
where \(I_j\) denotes a modified Bessel function.

## Assumptions and scope
For \(c>0\), let \(\mathcal F_c\) be the analytic Fock Hilbert space of entire \(f\) with
\[
 \|f\|_c^2=\frac c\pi\int_{\mathbb C}|f(z)|^2e^{-c|z|^2}\,dA(z).
\]
For every \(a,b,R>0\), the compact operator \(C_R:\mathcal F_a\to\mathcal F_b\) is defined unambiguously by
\[
 \langle C_R f,g\rangle_b=\frac b\pi\int_{|z|<R}f(z)\overline{g(z)}e^{-b|z|^2}\,dA(z).
\]
The right side is bounded because point evaluations on a fixed compact disk are bounded in both spaces. This is a specific disk-truncated, mismatched-Gaussian pairing; no identification with every squeezed-window cross-Toeplitz convention is asserted. All asymptotics hold with \(a,b\) fixed, and \(p\) fixed when Schatten powers are considered. The notation \(\|C_R\|_{\mathcal S_p}^p\) means the sum of the \(p\)-th powers of singular values even when \(0<p<1\).

## Proof
**Exact diagonalization.** The functions \(e_n^{(c)}(z)=\sqrt{c^n/n!}\,z^n\) are orthonormal bases in \(\mathcal F_c\). Angular integration makes \(\langle C_R e_n^{(a)},e_m^{(b)}\rangle_b=0\) unless \(m=n\); when \(m=n\), the radial substitution \(y=br^2\) gives
\[
 \langle C_R e_n^{(a)},e_n^{(b)}\rangle_b=t^n\frac{1}{n!}\int_0^x y^ne^{-y}\,dy=t^np_n(x)>0.
\]
Thus the displayed family is precisely the singular-value multiset. For fixed \(x>0\), the elementary bound \(p_n(x)\le x^{n+1}/(n+1)!\) shows superexponential decrease after multiplication by any fixed \(t^n\), proving compactness and membership in every finite Schatten class.

**Nuclear trace.** If \(X\) has Poisson distribution of mean \(x\), Tonelli's theorem gives \(\sum_{n\ge0}t^n p_n(x)=\mathbb E[\sum_{n=0}^{X-1}t^n]\). For \(t\ne1\), this is \((\mathbb Et^X-1)/(t-1)=(e^{x(t-1)}-1)/(t-1)\). At \(t=1\), it equals \(\mathbb EX=x\). This is an exact trace-norm identity, not an asymptotic approximation.

**Mode transitions.** Write \(q_n(x)=p_{n+1}(x)/p_n(x)\). Let
\[
 A_n(x)=\sum_{j=0}^{\infty}\frac{x^j}{(n+2)(n+3)\cdots(n+j+1)},
\]
where the \(j=0\) denominator is \(1\). The Poisson tail written relative to its first mass gives \(q_n(x)=1-A_n(x)^{-1}\). Every \(A_n(x)>1\) is strictly increasing in \(x>0\) and strictly decreasing in \(n\). Consequently \(q_n(x)\) is strictly increasing in \(x\), strictly decreasing in \(n\), and ranges from \(0\) to \(1\) as \(x\) varies from zero to infinity for fixed \(n\). Since \(d_{n+1}/d_n=tq_n(x)\), the assertions about modes follow, with the unique \(n\)-to-\(n+1\) threshold characterized by \(tq_n(x)=1\). They are strictly increasing in \(n\). The thresholds can produce a single adjacent tie but cannot produce any nonadjacent tie for the maximum.

**Subcritical and critical Schatten laws.** If \(t<1\), then \(p_n(x)\to1\) at fixed \(n\), while \(t^{pn}p_n(x)^p\le t^{pn}\); dominated convergence gives the geometric sum. If \(t=1\), \(p_n(x)\to1\) uniformly for \(n\le(1-\delta)x\) and \(p_n(x)\to0\) exponentially uniformly for \(n\ge(1+\delta)x\) by standard Poisson Chernoff estimates. To control the infinite upper tail for arbitrary fixed \(p>0\), one may apply the bound \(p_n(x)\le e^{-\theta(n+1)+x(e^\theta-1)}\) with a fixed \(\theta>0\) beyond \((1+\delta)x\) and sum the geometric tail. Therefore \(x^{-1}\sum p_n(x)^p\to1\) by letting \(\delta\downarrow0\).

**Supercritical Gaussian window.** Fix \(t>1\), and put \(m=n+1\). For any \(\delta>0\), uniformly over \(m\ge(1+\delta)x\), the geometric comparison of the Poisson upper tail to its first mass yields
\[
 p_n(x)\le \frac{e^{-x}x^m/m!}{1-x/(m+1)}.
\]
Uniformly when \(|m-tx|\le M\sqrt{tx}\) for fixed \(M\), successive Poisson-mass ratios yield instead \(p_n(x)/(e^{-x}x^m/m!)\to t/(t-1)\). Hence, using \(\pi_m(tx)=e^{-tx}(tx)^m/m!\),
\[
 d_n=\frac{e^{(t-1)x}}{t-1}\,\pi_m(tx)(1+o(1))
\]
uniformly throughout every fixed central Gaussian window. The Poisson local central-limit theorem and Stirling's formula give the asserted pointwise Gaussian profile, maximizing index, and sharp operator-norm constant. To justify the global \(p\)-power sum, select \(\delta>0\) so small that \((1+\delta)\log t<t-1\), possible since \(\log t<t-1\). The indices \(m<(1+\delta)x\) contribute at most a polynomial times \(t^{p(1+\delta)x}\), exponentially smaller than the displayed principal scale. At all remaining indices the previous tail bound controls \(d_n\) by a constant times \(e^{(t-1)x}\pi_m(tx)\). Stirling bounds give tightness outside growing central windows and the discrete Gaussian integral
\[
 \sum_{m\ge0}\pi_m(tx)^p\sim(2\pi tx)^{(1-p)/2}p^{-1/2}.
\]
Together with the central uniform equivalence this proves the complete supercritical Schatten formula for every fixed \(p>0\). The same bounds rule out a larger maximum away from the central window.

**Critical Hilbert--Schmidt identity.** For independent Poisson variables \(X,Y\) of mean \(x\), \(\sum_n p_n(x)^2=\mathbb E\min(X,Y)=x-\frac12\mathbb E|X-Y|\). The Skellam probability law gives \(\mathbb P(X-Y=j)=e^{-2x}I_{|j|}(2x)\), and the recurrence \(jI_j(z)=\frac z2(I_{j-1}(z)-I_{j+1}(z))\) telescopes to \(\mathbb E|X-Y|=2xe^{-2x}[I_0(2x)+I_1(2x)]\). The stated exact formula follows; the remainder follows from the standard large-argument Bessel expansion.

## Verification
The standard-library checker in `checks/verify.py` independently evaluates truncated Poisson tails, radial Fock matrix coefficients by Simpson quadrature, nuclear trace identities, strict ratio monotonicity, critical second moments and selected large-radius asymptotic constants. In its packaged form it passed 2,442 finite assertions. These finite checks support normalization and constants, but the infinite statements are proved analytically above.

## Relationship to prior work
Kisil's 2021 preprint (subsequently published in 2023) develops cross-Toeplitz operators between different Fock--Segal--Bargmann realizations using two-sided Heisenberg convolution, but does not establish the present disk-truncated two-Gaussian modal or Schatten profile. Dewage and Ólafsson's 2021 preprint (2022 publication) derives eigenvalue integrals for same-weight quasi-radial Fock Toeplitz operators; the familiar Poisson tails at equal weights are an ingredient, not a newly claimed fact. Esmeral and Maximenko (2015 preprint) study radial Fock Toeplitz eigenvalue-sequence algebras. The additional results here concern the unequal Gaussian pairing, unique mode transitions, full Schatten phase diagram with constants, and exact nuclear trace. This comparison is specific to the cited statements and inspected material, not a proof of historical priority.

## Limitations
The operator is one-dimensional and disk-truncated, with fixed strictly positive input and output Gaussian parameters. The result gives singular-value information, not eigenvalues of a non-square-space transfer, and is not asserted to cover all definitions of cross-Toeplitz operators associated with squeezed Gaussian windows. The three regimes are pointwise in fixed \(t\), not uniform near \(t=1\). No claim is made about nonradial symbols or arbitrary growing regions, and independent mathematical validation has not been performed.

## References
- V. V. Kisil, *Cross-Toeplitz Operators on the Fock--Segal--Bargmann Spaces and Two-Sided Convolutions on the Heisenberg Group*, arXiv:2108.13710, first posted 2021-08-31; Annals of Functional Analysis 14 (2023), article 38, DOI 10.1007/s43034-022-00249-7.
- V. Dewage and G. Ólafsson, *Toeplitz Operators on the Fock Space with Quasi-Radial Symbols*, arXiv:2107.01465, first posted 2021-07-03; Complex Analysis and Operator Theory 16 (2022), article 61, DOI 10.1007/s11785-022-01208-9.
- K. Esmeral and E. A. Maximenko, *Radial Toeplitz Operators on the Fock Space and Square-Root-Slowly Oscillating Sequences*, arXiv:1505.07906, first posted 2015-05-29; Complex Analysis and Operator Theory 10 (2016), 1655--1677.
