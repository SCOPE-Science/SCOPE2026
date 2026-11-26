# Independent mathematical audit

## correctness

PASS

Conditioning on the first Poisson refresh of the uniform momentum gives the Bessel renewal equation with initial Fourier mass one. In the shifted Laplace variable u=s+λ, rationalization splits the credited kernel into 2λ/(u²−(λ²−κ²)) and 1/(sqrt(u²+κ²)+λ). Independently checked the inverse of the latter: Laplace-transform the proposed truncated sine integral and then remove the truncation (the decreasing 1/y tail gives a uniform bound by splitting at y=1/t). Substituting x=sqrt(y²−κ²) yields (2/π) times the integral of x²/[(x²+λ²)(x²+u²+κ²)] over x>0, which is exactly 1/(λ+sqrt(u²+κ²)) for real u>0. At the lower edge the amplitude equals (sqrt(2κ)/λ²) z^(1/2) plus a term z^(3/2) times a locally smooth factor. The endpoint Fourier expansion has phase 3π/4 and Γ(3/2); retaining the z^(3/2) term gives an O(t^(-5/2)) correction and the remaining endpoint term may be integrated three times, since its third derivative is locally integrable. Away from the edge, the amplitude tends to zero and all positive-order derivatives are integrable, uniformly on compact positive κ sets, so repeated integrations produce no competing term. The t^(-2) window fixes the entire-function argument exactly and division by t gives the uniform t^(-5/2) error. The root terms refer to the analytic continuation in the scalar Fourier response, not a claim that both are isolated eigenvalues of the kinetic generator. At κ=0 mass is conserved; errors remain absolute at oscillation zeros. The original script was inspected, not run. Independent angular evolution and direct oscillatory quadrature agree in 18 split tests to a maximum scaled discrepancy of 1.55e−12, with separate finite critical-window and phase-controlled edge checks.

## originality

PASS

The transform and its renewal interpretation are prior, and the elementary root threshold is already algebraically encoded by that transform. The supported distinct result is the explicit cut-edge amplitude and phase with compact-uniform control, used together with the exact split to give the signed, time-tuned critical profile and error. The record does not claim a new kernel or the general kinetic phenomenon of a pole/cut crossover.

## value

PASS

The fixed-frequency late-time Fourier observable makes a natural distinction invisible in a spatial diffusion limit. The result quantifies the transition from real decay to damped oscillation, controls when the oscillatory leading term vanishes, and supplies an explicit signed crossover with an error estimate valid on both sides of the threshold. The branch coefficient and uniform estimate add information beyond reading the two algebraic roots from the known kernel; no statement of validity for the microscopic chain is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
