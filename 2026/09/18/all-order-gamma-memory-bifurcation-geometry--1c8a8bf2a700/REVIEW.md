# Same-model review

## Correctness

**PASS.**

For a nonzero Neumann mode, the Erlang chain linearization is
\[
\dot U=-XU-d_2\lambda V_0,\qquad
\dot V_j=-BV_j+\tau^{-1}V_{j+1},\qquad
\dot V_k=-BV_k+\tau^{-1}A,\qquad
\dot A=\rho U-MA.
\]
Direct elimination gives
\[
P_k(z)=(z+X)(z+M)(z+B)^{k+1}+d_2\rho\lambda\tau^{-(k+1)}.
\]
The phase derivative on \(z=i\omega\) is strictly positive, so every admissible odd- or even-\(\pi\) phase level has exactly one frequency. The modulus is also strictly increasing. The crossing derivative
\[
dz/dC=1/(C L(i\omega))
\]
has nonzero real part because \(\operatorname{Re}L(i\omega)>0\), proving simplicity and transversality. The stationary threshold has modulus \(R_k(0)\), strictly smaller than every negative-side oscillatory threshold, which establishes the claimed primary stability interval.

The fixed-mean limit follows from
\[
\left(1+\frac{T}{r}(z+d_1\lambda)\right)^r\to e^{T(z+d_1\lambda)}
\]
locally uniformly for \(r=k+1\to\infty\). The resulting limiting phase and modulus equations agree with the characteristic equation for a discrete temporal delay filtered by spatial heat propagation.

Adversarial checks included sign reversal of the memory-driven flux, the zero spatial mode, the first negative-side crossing, and the possibility of multiple phase levels. The theorem is stated in terms of the signed coupling \(C\), so it remains valid regardless of the sign of \(\rho\).

## Originality

**PASS, to the best of our knowledge.**

The 2026 source introduces the integer Gamma family but its abstract explicitly states that the stability and bifurcation analysis is carried out for the exponentially decaying weak kernel and the peak-type strong kernel. Detailed indexed mathematical summaries likewise present only the \(k=0\) cubic and \(k=1\) quartic analyses.

Searches using the exact title and arXiv identifier, and combinations of `cognitive map`, `Gamma memory`, `Erlang`, `higher-order kernel`, `reaction-diffusion`, `Hopf`, `phase condition`, and `linear chain`, found no prior source giving the all-order characteristic factorization, crossing count, or fixed-mean phase limit for this model. Generic Erlang linear-chain theory is well established and is not claimed as new. Literature on Erlang approximations and fixed-delay limits was treated as methodological background rather than evidence of source-specific priority.

The exact source article's full text was not independently inspected. Its abstract and detailed indexed mathematical summaries were inspected. Therefore an unindexed appendix or remark containing an all-order result remains the principal residual originality risk.

## Value

**PASS.**

The result turns a sequence of increasingly high-degree Routh-Hurwitz calculations into a closed-form theorem for every integer Gamma order. It shows that the weak and strong kernels capture only the first part of a larger phase ladder: a new negative-signed secondary oscillatory crossing appears first at \(k=2\), a second positive-signed crossing at \(k=4\), and the total number of modal oscillatory thresholds grows as \(\lfloor(k+2)/2\rfloor\).

The result also separates first instability from secondary spectral restructuring: every negative-signed Hopf crossing lies beyond the stationary loss, whereas the positive \(j=0\) Hopf threshold is the first positive-side loss. The fixed-mean limit explains how these finite ladders converge to the countably infinite phase sequence of a discrete-delay problem.

## Limitations checked

The record does not claim global stability, nonlinear branch direction, exclusion of simultaneous modal resonances, or a Hopf theorem without the standard nonlinear nondegeneracy conditions. It does not cover noninteger Gamma shape parameters. The fixed-delay result is spectral rather than a nonlinear PDE convergence theorem.

**Same-model review: passed. Cross-model review: not yet performed.**
