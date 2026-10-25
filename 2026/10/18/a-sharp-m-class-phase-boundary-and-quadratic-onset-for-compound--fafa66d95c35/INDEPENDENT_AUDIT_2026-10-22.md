# Independent mathematical audit

## correctness

PASS

Re-derived Poisson K_X(t)=lambda(Ee^(tJ)-1-tEJ), V=lambda EJ^2. Exact second-order remainder factorization K_X=Vt²/2 Ee^(tR) uses independent U~Beta(1,2), size-biased Y/L~Beta(alpha+2,beta), R=UY. The coefficients A_n=2(a)_n/((n+2)!(b)_n), a=alpha+2,b=a+beta, have A_{n+1}/A_n=(a+n)/((b+n)(n+3)) and difference from m0=a/(3b) equal n[b(3-a)-a(n+3)]/[3b(b+n)(n+3)]. Thus A_n<=m0^n all n iff b(3-a)<=4a, equivalent to alpha>=1 or beta<=a(a+1)/(1-alpha) when alpha<1; coefficientwise geometric majorant proves c*=Lm0. Otherwise A2>A1², local positive derivative of Psi=(1-1/F)/s implies c*>Lm0 with finite positive maximizer since Psi(s)->0 at infinity. Independently symbolically verified at b0=4a/(3-a): u=0,u_prime=(3-a)^4/[1728a(a+1)],v=-(3-a)^4/[8640(a+3)]<0, giving unique near-critical optimizer and exact stated quadratic gain via IFT and uniform-away-from-zero global gap. The local checks of rational coefficients are diagnostic, not a substitute for the entire coefficientwise proof.

## originality

PASS

Chen 2026 establishes the **general** compound Poisson canonical transform and c* variational formula, Klar--Müller earlier M-class MGF criterion, and Chen--Wang its signed extension, all fully credited. None of the inspected Gamma/two-point/Skellam examples evaluates the two-shape continuous Beta-jump coefficient ratio, the iff alpha/beta boundary, or quadratic onset. Querying Beta concentration records shows a direct Beta tail threshold for a single Beta random variable, not Beta-jump compound sum. Best-of-knowledge PASS with an unlocated general stochastic-order theorem possible.

## value

PASS

The phase diagram decides when the best variance-matched Bernstein pole is already determined locally by the third cumulant versus forced by a global transform obstruction. The explicit smooth codimension-one threshold and quadratic onset for naturally parameterized bounded Beta jumps and L/4 uniform-jump benchmark are useful sharp concentration invariants, not merely application of an existing formula without new work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
