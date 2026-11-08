# Independent mathematical audit

## correctness

PASS

For the specified four-dimensional two-vertex exponential-comparison logistic Keller–Segel ODE, the (M,z,C,w) change gives exact equations and isolates eigenvalue -β. At a positive unequal equilibrium, t=z/M∈(0,t_max), M=K/(1+t²), z=Kt/(1+t²), w=αz/δ. The scalar equilibrium branch χ=δX(t)/(αK), X=(1+t²)atanh(h)/t with h=t[1+κ(1-t²)/(1+t²)], is strictly increasing because h=(t+v)/(1+tv) and both atanh(s)/s and relevant positive factors increase; its limit 1+κ supplies the threshold. The reduced 3×3 Jacobian J=[[-a,-b,0],[d,-e,F],[0,α,-δ]] has q=αF/δ=e(1-h²)atanh(h)/h with 0<q<e. The exact identity D=ae+bd-aq=-(rη/2)G_t>0 follows from branch derivative G_t<0. The cubic coefficients A=a+e+δ, B=T+δ(a+e-q), C0=δD and AB-C0=(a+e)T+δ(a+e+δ)(a+e-q)+δaq are all strictly positive, completing Routh–Hurwitz and hyperbolic attraction, independent of d sign. Independently symbolically checked D+(rη/2)G_t=0 and numerically evaluated five distinct positive-rate admissible equilibria (κ=0.2,0.5,1,2,4), all with negative real eigenvalues and strictly positive Hurwitz margins. Boundary χ=χ_c, zero rates and global basins not covered.

## originality

PASS

Best-of-knowledge PASS, with material primary-text priority risk: the exact 2026 model source arXiv:2610.31049 discusses homogeneous-state instability and nonlinear graphon patterns in its accessible abstract. The complete same-model paper could not be read, so noncoverage of its full contents is NOT asserted. The accessible earlier stationary branch census (as cited in the assigned package) does not imply four-dimensional Hurwitz stability; PDE-on-edge Keller–Segel results are different models. The present strict determinant/Hurwitz calculation adds a mathematically distinct assertion on every asymmetric equilibrium.

## value

PASS

For a natural two-patch finite metapopulation chemotaxis model, a complete all-positive-parameter stability certificate for both patterned branches rules out secondary local Hopf, steady-state, or other spectral destabilization as chemotactic sensitivity grows. Existence and monotonicity of equilibria alone cannot settle these stability questions; the strict cubic Hurwitz factorization supplies a nontrivial missing dynamical classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
