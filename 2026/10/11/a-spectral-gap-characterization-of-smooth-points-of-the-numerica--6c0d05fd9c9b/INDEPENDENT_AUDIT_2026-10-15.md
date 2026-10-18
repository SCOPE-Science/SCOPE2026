# Independent mathematical audit

## correctness

PASS

For nonzero bounded weights |a_n|→b>0, the diagonal phase gauge identifies w(T_a) with the top of the selfadjoint Jacobi spectrum with links |a_n|/2. The difference from constant-b Jacobi is compact, so the top r>b is an isolated eigenvalue; the nonzero off-diagonal recurrence forces simplicity and its absolute-value Rayleigh maximizer is strictly positive. A bounded spectral gap and uniformly positive inf_n|a_n| give a quadratic operator-norm expansion and a real-Fréchet derivative ∑u_n u_{n+1} Re(conj(a_n)h_n/|a_n|) on the full ℓ∞. At r=b the bounded alternating-long-block direction h_n=a_n s_n/|a_n| has both signs of perturbation attain b+ε as a spectral lower bound and the norm inequality makes the bound sharp, preventing two-sided Gâteaux differentiability. For (t,1,1,...) the tail recurrence gives r=1 up to t=√2 and the explicit larger radius thereafter. Independence: SciPy eigh_tridiagonal on 501×501 sections gave 1.1547005383792515 at t=2 (exact 2/√3), and errors below 4e−8 for t=1.42; these finite checks are not the infinite proof.

## originality

PASS

Best-of-knowledge original characterization of smooth points of a natural infinite-dimensional norm. Sharif (arXiv:2303.00876) defines this weighted-shift numerical-radius norm and quotes its classical one-defect numerical-radius formula but its inspected analysis concerns numerical-radius bounds and Banach limits, not smoothness in full ℓ∞. The finite-defect paper Undrakh et al. 2015 and Roy–Sain numerical-radius smoothness address distinct parameter and operator settings. The published Resultary binary-weight shift characterization concerns sequences with zero weights and longest runs, so does not imply the positive nonzero-tail case. The 2/√3 one-defect value is acknowledged prior art; the analytic smoothness transition is distinct.

## value

PASS

The exact necessary-and-sufficient norm-smoothness locus at a natural essential-spectrum boundary, the full Banach-space derivative, and the long-tail obstruction are structural geometry of a published equivalent norm on ℓ∞; not merely another evaluation of the classical one-defect numerical radius.

The dated certificate retains the supplied scientific assessment, sources and limitations.
