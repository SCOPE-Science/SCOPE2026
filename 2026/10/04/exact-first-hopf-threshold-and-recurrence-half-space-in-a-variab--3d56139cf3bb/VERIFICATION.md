---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The exact source vector field is x_dot=-a*x+y*z, y_dot=a*x-x*z, z_dot=-a*z+x^2+a with a>0. Solve -ax+yz=0, x(a-z)=0, x^2=a(z-1), giving E0=(0,0,1) and E±=(±sqrt(a(a-1)),±sqrt(a(a-1)),a) for a≥1 (coincident at a=1). E0 linearization has characteristic (λ+a)[λ²+aλ+1-a], hence stable for 0<a<1, real saddle for a>1; at a=3 its three eigenvalues are real, contradicting the source's saddle-focus label. At E±, compute λ³+2aλ²+a(2-a)λ+2a²(a-1); its cubic Routh determinant is 2a²(3-2a), giving stability 1<a<3/2 and instability after 3/2. At a=3/2 the spectrum is -3,±i sqrt(3)/2. Independent exact SymPy reconstruction from the actual ODE gave the nondegenerate first Lyapunov coefficient l1=-2sqrt(3)/3 using normalized adjoint eigenvectors, and the crossing derivative 6/13 from the characteristic polynomial; therefore a supercritical local Hopf on each symmetric branch, not just numerical oscillations. From z_dot+a(z-1)=x², every bounded complete solution satisfies z(t)-1=∫_0∞exp(-as)x(t-s)² ds ≥0; non-equilibrium complete orbits have strict z(t)>1. Initial transients for merely forward trajectories are explicitly excluded. No assertion that cycles extend globally to a=3 or that chaos is rigorously established.

## originality

PASS

Best-of-knowledge PASS for the exact parameter a=3/2 local Hopf, exact l1, lower-parameter equilibrium partition and complete-trajectory half-space on this exact Yan–Jie–Zhang polynomial ODE. Full introducing 2022 Scientific Reports article read, including original equations, stated equilibria, a=3 eigenvalues and numerical parameter scan. Its results do not state the lower parameter Hopf or memory constraint. Broader generic Hopf theorems do not supply coefficients without calculation.

## value

PASS

A precise supercritical Hopf and stable-equilibrium interval supply the missing transition below the source's high-parameter numerical chaos regime, while the backward filter excludes z≤1 for every nontrivial bounded complete orbit and corrects the published eigenvalue classification at a=3. These are source-specific structural dynamical constraints, not routine substitution alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
