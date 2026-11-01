# Independent mathematical audit

## correctness

PASS

The one-coordinate orthogonal projection to mean-zero functions has normalized integral kernel u(a,b)=q·1_{a=b}−1. Summing u_i u_j over pairs yields the displayed second Krawtchouk polynomial K(d)=[((q−1)n−qd)^2−(q−2)((q−1)n−qd)−n(q−1)]/2. The q^{-n} matrix has equal absolute row/column sums E|K(D)|, D~Bin(n,(q−1)/q), hence both endpoint operator norms. E K(D)=0 and K(0)>0, so an integer negative value exists; convex quadratic gives a unique strict negativity interval, with zero roots properly excluded. Conditioning on two mismatches gives signed second difference E[u1u2 1_{D≤t}]=p²[b(t)−b(t−1)], proving the four-boundary formula with out-of-range masses zero. For n/q→∞, standardized matching count has Lyapunov third-moment bound O(√(q/n)), vanishing linear correction and uniformly bounded fourth moments; this establishes Gaussian convergence plus L1 uniform integrability and √(2/(πe)) limit. For q→∞ with n/q→λ>0, Binomial matching counts converge to Poisson, factorial moment bounds imply fourth-moment UI, and the polynomial tends to second Charlier; k=1 is the sole negative term for 0<λ<2−√2, while k=2 changes sign transversally at λ*=2−√2. Differentiating uniformly summable Poisson tails gives positive derivative jump √2 λ*exp(−λ*). Finally λ↓0 and λ→∞ asymptotics follow first terms and Poisson CLT with UI. Independently coded exact rational checks of 1659 (n,q) pairs and 25 entire row enumerations, plus cusp numerical check, corroborate finite algebra only; no finite data are used to prove limits.

## originality

PASS

Best of knowledge for the COMPLETE q≥3 finite-n endpoint theorem and nonconstant q→∞, n/q→λ Poisson–Charlier crossover with first cusp: Hamming harmonic decomposition, fixed-binary exact projection constants and classical Krawtchouk identities are known input, but the inspected independent published statements do not establish the combined varying-alphabet assertion. An important inaccessible classical polynomial-summation paper may cover the finite four-mass reduction, so the finite formula is not claimed independently novel in isolation. This is not absolute priority certification.

## value

PASS

The absolute ℓ¹/ℓ∞ amplification of a canonical degree-two Hamming harmonic projection is a natural operator invariant for product alphabets, not an arbitrary slice. The exact two-parameter reduction to four binomial masses enables sharp finite evaluation, while the q-growing regime produces a nontrivial Charlier limit that fixed-alphabet Boolean calculations cannot even parametrize. The first cusp at 2−√2 identifies an exact threshold where the minimizing sign support changes. This is an independently useful exact asymptotic invariant without needing a downstream general theorem. If the finite boundary identity is classical, the joint scaling/cusp remains the mathematically motivated distinction; routine classical inputs are acknowledged.

The dated certificate retains the supplied scientific assessment, sources and limitations.
