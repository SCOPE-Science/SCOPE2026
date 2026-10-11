# Exact phase-volume law contradicts both published Lyapunov spectra of a five-dimensional Lorenz model

## Finding
Consider the five-dimensional Lorenz system
\[
\dot x_1=\sigma(x_2-x_1),\qquad
\dot x_2=-x_1x_3+r x_1-x_2,
\]
\[
\dot x_3=x_1x_2-x_1x_4-bx_3,\qquad
\dot x_4=x_1x_3-2x_1x_5-dx_4,
\]
\[
\dot x_5=2x_1x_4-4bx_5.
\]
Its divergence is the constant
\[
\nabla\!\cdot F=-\sigma-1-5b-d.
\]
Hence the tangent-flow determinant obeys
\[
\det D\phi_T=\exp\bigl[-(\sigma+1+5b+d)T\bigr].
\]
For the standard full finite-time Lyapunov exponents \(\lambda_1(T),\ldots,\lambda_5(T)\), defined from the singular values of \(D\phi_T\),
\[
\sum_{j=1}^5\lambda_j(T)=-(\sigma+1+5b+d)
\]
for every \(T>0\). The same identity holds for every full asymptotic Lyapunov spectrum whenever its limits exist.

At the source parameters
\[
\sigma=10,\qquad b=\frac83,\qquad d=\frac{19}{3},
\]
the required sum is
\[
-10-1-5\frac83-\frac{19}{3}=-\frac{92}{3}=-30.6666\ldots .
\]
The five values printed for \(r=43\),
\[
1.1281,\ 0.0073,\ -1.3786,\ -1.3774,\ -1.6688,
\]
sum exactly, as printed, to
\[
-3.2894=-\frac{16447}{5000},
\]
whereas the five values printed for \(r=25\),
\[
-0.5246,\ -0.5358,\ -6.9952,\ -2.0305,\ -4.1633,
\]
sum to
\[
-14.2494=-\frac{71247}{5000}.
\]
Their discrepancies from the exact phase-volume rate are respectively
\[
\frac{410659}{15000}=27.3772666\ldots
\]
and
\[
\frac{246259}{15000}=16.4172666\ldots .
\]
These are not rounding-scale errors. Neither printed five-number list can therefore be a correct full Lyapunov spectrum of the displayed ODE in its displayed time variable.

## Assumptions and scope
The conclusion concerns the continuous-time system exactly as printed in equation (2.8) of the primary source and the parameter values attached there to Figure 2. No assumption on \(r\) is needed for the phase-volume identity because \(r\) does not enter the divergence.

For a finite-time statement, “full Lyapunov spectrum” means the standard five singular-value growth rates of the tangent map over the same time interval. An accumulated orthonormalized tangent computation has the same determinant sum in exact arithmetic. For an asymptotic statement, the identity applies whenever the five Lyapunov limits exist.

The result does not identify the numerical implementation that produced the displayed curves. It also does not infer that the trajectory at \(r=43\) is non-chaotic merely because the reported full vector is inconsistent: a corrected computation could still have a positive largest exponent. Likewise, it does not independently prove convergence at \(r=25\).

## Proof
Let \(J(t)=DF(x(t))\) be the Jacobian along any solution and let \(Y(t)\) be a fundamental matrix for the variational equation \(\dot Y=J(t)Y\), with \(Y(0)=I\). The diagonal entries of \(DF\) are
\[
-\sigma,\qquad -1,\qquad -b,\qquad -d,\qquad -4b,
\]
so
\[
\operatorname{tr}J(t)=-(\sigma+1+5b+d)
\]
for every trajectory and every time for which the solution exists.

Jacobi's determinant identity gives
\[
\frac{d}{dt}\log|\det Y(t)|=\operatorname{tr}J(t),
\]
therefore
\[
|\det Y(T)|=\exp\bigl[-(\sigma+1+5b+d)T\bigr].
\]
If \(s_1(T),\ldots,s_5(T)\) are the singular values of \(Y(T)\), then \(\prod_j s_j(T)=|\det Y(T)|\). Thus
\[
\sum_{j=1}^5\frac1T\log s_j(T)
=\frac1T\log|\det Y(T)|
=-(\sigma+1+5b+d).
\]
Taking limits proves the asymptotic version. Substituting the source parameters gives \(-92/3\). The two decimal sums are exact arithmetic on the values printed in the source and differ from \(-92/3\), proving the claimed incompatibility.

## Verification
The accompanying `verify.py` uses only Python's standard-library exact rational arithmetic. It checks the divergence coefficient at the source parameters, both printed five-number sums, both exact discrepancies, and the time-\(500\) determinant exponents. Running the packaged file returns `VERIFY_OK`.

The proof itself is analytic; the checker is only an arithmetic replay. No numerical integration, finite sampling, or extrapolation is used to establish the contradiction.

## Relationship to prior work
The primary AIMS Mathematics article prints equation (2.8), fixes \(\sigma=10\), \(b=8/3\), and \(d=19/3\), and gives the two five-number Lyapunov lists at time \(500\) for \(r=43\) and \(r=25\). The same article decomposes the vector field into conservative/nonlinear and diagonal dissipative pieces, but it does not state the resulting full-spectrum phase-volume constraint or compare it with Figure 2.

The original five-dimensional Lorenz-model paper by Shen studies nonlinear feedback, stability, and Lyapunov exponents for the same model family. Zhang and Deng later analyze dynamical transitions and chaos for the same five-dimensional model. Both works predate the 2023 numerical tuples corrected here. The closest checked published research record for the same model concerns a logarithmic correction at the critical transition \(r=1\), not the Lyapunov spectrum at \(r=25\) or \(r=43\). A separate checked record applies the same phase-volume diagnostic to a different four-dimensional Sprott-C extension; it does not imply the present source-specific contradiction.

Targeted searches by DOI, exact exponent values, model aliases, divergence, phase volume, and Lyapunov-sum language did not locate a published record stating this comparison for the Mao–Feng–Al-Towailb–Saberi-Nik spectra.

## Limitations
The exact phase-volume identity is standard; originality is claimed only for applying it to, and obtaining the explicit contradiction with, these two published five-number spectra. A failed literature search is not a proof that no unindexed correction exists.

The source describes the plotted quantities as Lyapunov exponents “at 500th second” but does not, in the material inspected, specify enough numerical detail to diagnose the implementation. If the plotted quantities were intended as some nonstandard diagnostic rather than a full tangent spectrum, the paper's labeling would need that qualification. The present result does not reconstruct corrected exponent values and does not overturn qualitative chaos or steady-state conclusions supported independently of the inconsistent lists.

## References
1. X. Mao, H. Feng, M. A. Al-Towailb, and H. Saberi-Nik, “Dynamical analysis and boundedness for a generalized chaotic Lorenz model,” *AIMS Mathematics* 8 (2023), 19719–19742. DOI: 10.3934/math.20231005. Published 12 June 2023.
2. B.-W. Shen, “Nonlinear Feedback in a Five-Dimensional Lorenz Model,” *Journal of the Atmospheric Sciences* 71 (2014), 1701–1723. DOI: 10.1175/JAS-D-13-0223.1.
3. D. Zhang and D. Deng, “Dynamical transition and chaos for a five-dimensional Lorenz model,” *Mathematical Methods in the Applied Sciences* 45 (2022), 1612–1631. DOI: 10.1002/mma.7877. First published 3 November 2021.
