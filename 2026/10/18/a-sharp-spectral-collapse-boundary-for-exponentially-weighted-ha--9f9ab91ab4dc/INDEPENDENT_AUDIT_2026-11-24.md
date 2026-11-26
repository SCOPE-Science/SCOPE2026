# Independent mathematical audit

## correctness

PASS

Plancherel with the stated pi^(-1) norm gives 2 * integral_0^infinity x^alpha exp(-2xt) dx = Gamma(alpha+1)/[2^alpha t^(alpha+1)], as required by weighted Paley–Wiener. In the Laplace model one step shifts t to t+b with input amplitude exp(-at). Iteration sums t,t+b,...,t+(n-1)b and gives amplitude exp(-ant-abn(n-1)/2). The shifted density contributes (t/(t+nb))^eta to the norm ratio. Its continuous essential supremum is one on either axis; in the open quadrant the log derivative -an+eta*nb/[t(t+nb)] has a unique zero, giving the stated rationalized root. The expansion t_n=eta/(an)+O(n^-3) gives ant_n=eta+O(n^-2) and t_n/(t_n+nb)=eta/(ab n^2)*(1+O(n^-2)), so both the prefactor and relative error follow. For each power, an infinite orthonormal sequence supported on a bounded near-maximizer interval is weakly null; compact operators kill its norm in the limit. This supplies both the finite-rank and essential-norm lower bound for all j and noncompactness. The interior radii vanish by the power norm and the quotient norm bound; the identity and the b=0 multiplier give the first two spectral rows. If a=0<b, the fibers t=r+kb, 0<r<b, carry normalized shifts with weights ((r+kb)/(r+(k+1)b))^eta. For |lambda|<1, their adjoints have eigenvectors lambda^k ((r+kb)/r)^eta times arbitrary L^2 base data on b/2<r<b, uniformly summable there. Infinite-dimensional adjoint kernel gives non-Fredholmness for the conjugate parameter; closure and norm one give both disks. For fixed n and a,b>0, evaluating the ratio at t=sqrt(b/a) lower-bounds it by exp(-abn(n-1)/2-n sqrt(ab))/(1+n sqrt(ab))^eta, confirming convergence to one as ab->0 from the quadrant. The 1158 checks in the frozen audit and inspected CHECK.py are finite corroboration, not a fresh run or proof of the spectrum.

## originality

PASS

The unweighted translation axis, including both spectra and the flat approximation numbers, follows from published results and is expressly excluded from the novelty credited here. The supported distinct claim is the mixed-quadrant Bergman calculation: the noncompact quasinilpotent regime paired with the exact weighted all-power profile, its sharp alpha-dependent asymptotic and finite-rank distances. No earlier equivalent or dominating calculation was established in the compared material.

## value

PASS

This is an explicit analytic-function family in which combining two natural norm-one boundary operations collapses both radii without compactness, while finite-rank approximation distances remain as large as the norm at each power. The sharp Gaussian-in-n scale and polynomial prefactor quantify the effect. The mixed family and its quantitative behavior, not the individual known axis facts, have the scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
