# Exact efficacy thresholds for two treatment sites on a uniformly loaded chain

## Finding

For \(n\ge2\) unit-loading sites, place two identical partial filters at distinct indices \(1\le a<b\le n\). Each filter removes fraction \(\eta\in(0,1]\) of the load after that site's contribution. The objective is the sum of the postsite loads. Every minimizing placement is determined by the following strictly increasing threshold list for the gap \(d=b-a\). Set \(N=n+1\), and for \(1\le d\le n-2\) define
\[
\tau_d=\begin{cases}
2(d+1)/(N-d),&d\equiv N\pmod2,\\
2d/(N-d-1),&d\not\equiv N\pmod2.
\end{cases}
\]
The optimal gap is \(d_*=1+\#\{j:\tau_j<\eta\}\), with the additional gap \(d_*+1\) exactly when \(\eta=\tau_{d_*}\) and that threshold exists. At each optimal gap \(d\), take \(s=a+b=N\) when \(s\equiv d\pmod2\) permits it, and both \(s=N-1,N+1\) otherwise. These sums give all optima by \((a,b)=((s-d)/2,(s+d)/2)\). This includes exact ties at full efficacy and the single placement for \(n=2\).

## Assumptions and scope

The model is a one-dimensional chain with a unit input at each site, no inlet load, and no loss except at the two treatment sites. In symbols, \(c_0=0\), \(c_i=(c_{i-1}+1)(1-\eta\,\mathbf1_{\{i=a\text{ or }i=b\}})\), and the objective is \(E(a,b)=\sum_{i=1}^n c_i\). The objective is mass load under fixed-flow normalization. The grid is part of the model, not a sampling prescription for a continuous objective. No treatment number, removal fraction, nonlinear rates or hydrodynamics are optimized.

## Proof of the discrete classification

Without treatment, the postsite objective is \(E_0=nN/2\). The first treatment removes \(\eta a\), reducing the total load by \(\eta a(N-a)\) before the second treatment is accounted for. The load immediately before filtering at the second site is \(b-\eta a\); its removal reduces the objective by a further \(\eta(b-\eta a)(N-b)\). Thus
\[
E_0-E(a,b)=\eta\,[a(N-a)+b(N-b)-\eta a(N-b)].
\]
For \(s=a+b\) and \(d=b-a\), the bracket, up to an additive constant independent of \((a,b)\), is \(-Q(s,d)/4\), where
\[
Q(s,d)=(2-\eta)(s-N)^2+(2+\eta)\left(d-\frac{\eta N}{2+\eta}\right)^2.
\]
To see this, substitute \(a=(s-d)/2\) and \(b=(s+d)/2\). The coefficients of \(s^2,d^2,s,d\) in the bracket are respectively \(-(2-\eta)/4,-(2+\eta)/4,(2-\eta)N/2,\eta N/2\), with no mixed term. Since \(\eta>0\), minimizing \(E\) is therefore equivalent to minimizing \(Q\).

The feasibility conditions are \(1\le d\le n-1\), \(s\equiv d\pmod2\), and \(d+2\le s\le2n-d\). The interval is centered at \(N\) and has half-length \(n-1-d\). When parity disagrees, \(d<n-1\) (because \(n-1\equiv N\pmod2\)), so both nearest allowed sums \(N\pm1\) are feasible. Since \(2-\eta>0\), these nearest sums, or just \(N\) for agreeing parity, are exactly the fixed-gap optimizers. Write \(\varepsilon_d=0\) for agreeing parity and \(1\) otherwise. The corresponding score is
\[
Q_d=(2+\eta)\left(d-\frac{\eta N}{2+\eta}\right)^2+(2-\eta)\varepsilon_d.
\]
Subtracting adjacent scores gives
\[
Q_{d+1}-Q_d=\begin{cases}
2[2(d+1)-\eta(N-d)],&d\equiv N\pmod2,\\
2[2d-\eta(N-d-1)],&d\not\equiv N\pmod2.
\end{cases}
\]
In either case the sign is the sign of \(\tau_d-\eta\), with positive denominators. When \(d\equiv N\pmod2\), the numerator of the next threshold stays fixed while the denominator decreases by two; when the parity disagrees, the numerator increases by four and the denominator stays fixed. Thus the thresholds increase strictly. The score decreases for the initial consecutive gaps with \(\tau_d<\eta\), is flat at at most one adjacent pair, and increases thereafter. This gives exactly the claimed gap and all the listed pairs, including when all increments are positive, all are negative, or there are no increments.

**Example.** For \(n=6\), the thresholds in \((0,1]\) are \(2/3\) and \(1\). For \(0<\eta<2/3\), only \((3,4)\) is optimal. At \(\eta=2/3\), the placements \((2,4)\) and \((3,5)\) join it. For \(2/3<\eta<1\), only these last two placements are optimal, and at \(\eta=1\), \((2,5)\) joins them. The three-way placement ties come from two adjacent winning gaps, one with a single exact center and one with two parity-shifted centers.

## Continuous benchmark from a classical covariance matrix

For comparison, let \(k\ge1\) point filters with common removal fraction \(\eta\in(0,1]\) lie strictly inside a continuous segment of length \(L>0\). Suppose the inlet load is zero, the load has derivative 1 between filters, and each filter multiplies it by \(\rho=1-\eta\). If \(\ell_0,\ldots,\ell_k\) are the positive gaps with sum \(L\), then the integral of the load is exactly \(\tfrac12\ell^T K\ell\), where \(K_{ij}=\rho^{|i-j|}\). Indeed, within a gap the distributed source contributes \(\ell_i^2/2\) to the integral; material generated in gap \(i\) contributes \(\ell_i\ell_j\rho^{j-i}\) in a later gap \(j\).

The inverse of this classical Kac–Murdock–Szegő matrix is tridiagonal; see [1, Theorem 2.1(i), equation (2.1)]. Its row sums are \(1/(1+\rho)\) at the ends and \((1-\rho)/(1+\rho)\) in the interior. It is positive definite for \(0\le\rho<1\), as is also seen from the strictly diagonally dominant symmetric inverse with positive diagonal. The unique minimizer of the quadratic form under the sum constraint is \(\ell=L K^{-1}\mathbf1/(\mathbf1^T K^{-1}\mathbf1)\); these gaps are positive, so the minimizer is admissible. Therefore with \(D=2+(k-1)\eta\) the end gaps equal \(L/D\), the internal gaps equal \(\eta L/D\), the positions are \(L[1+(j-1)\eta]/D\), and the minimum is \(L^2(2-\eta)/(2D)\). This exact continuous solution is an application of the classical covariance formula, not the contribution here. Its real-valued optimizer does not classify the parity-constrained grid optima or their ties.

## Verification and limitations

The standalone standard-library program `verify.py` evaluates the finite-site load directly from the recurrence, checking the reduction identity, square-completed score, center condition, gap thresholds and exact ties at sampled rational efficacies for \(2\le n\le13\). It also tests the continuous benchmark at rational parameters. Run `python3 verify.py`; the expected output is `PASS 7193 exact-rational assertions`. The continuous and discrete statements for all admissible parameters follow from the preceding arguments, not from the finite checks.

This is an exact benchmark for the specified homogeneous chain and postsite objective; there is no claim for more than two integer filters, different treatment timing, unequal loading, longitudinal loss, measured field concentration, or actual placement in a river. The literature comparison does not establish absolute priority.

## Related work

WorldQual [2] includes distributed loading and in-stream transport under more general water-quality assumptions; its distributed-source passage is not an optimization of this two-filter chain. Brand and Ostfeld [3] study placement in a regional wastewater system. Their network design setting is related; no claim about the contents of the inaccessible full text is needed for the discrete proof. The continuum covariance comparison [1] already implies all of the continuous formulas above, while the discrete result requires minimization on a bounded parity sublattice rather than on the affine hyperplane.

## References

1. G. Fikioris, *Spectral properties of Kac–Murdock–Szegő matrices with a complex parameter*, arXiv:1804.08140, Theorem 2.1(i), equation (2.1). https://arxiv.org/abs/1804.08140
2. A. Voß et al. (2012), *Continental scale modelling of in-stream river water quality: a report on methodology, test runs, and scenario application*, Hydrological Processes 26, 2370–2384. https://nora.nerc.ac.uk/id/eprint/18635/1/N018635PP.pdf
3. N. Brand and A. Ostfeld (2011), *Optimal Design of Regional Wastewater Pipelines and Treatment Plant Systems*, Water Environment Research. https://doi.org/10.2175/106143010X12780288628219
