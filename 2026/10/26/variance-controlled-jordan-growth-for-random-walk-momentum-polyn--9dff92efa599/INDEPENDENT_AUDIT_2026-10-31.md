# Independent mathematical audit

## correctness

PASS

Define Y=1-j with probabilities p_j, E Y=0 and σ²=E Y²>0. Differentiating Σp_j P_(n+1-j)(z)=zP_n(z) at z=1 gives L D_(n,k)=k D_(n,k-1), where L=E shift by Y minus identity, D_(n,0)=1. The characteristic polynomial is G(s)-s=(s-1)²H(s) with H nonincreasing nonnegative coefficients; positivity and p0>0 exclude roots of H in |s|≤1, so all nonunit characteristic modes decay. For polynomial n^(2k), L has leading term k(2k-1)σ² n^(2k-2), so comparison of highest forcing coefficients gives c_k=c_(k-1)/((2k-1)σ²)=1/[σ^(2k)(2k-1)!!], and the lower polynomial/decaying modes contribute O(n^(2k-1)). The Jordan polynomial functional calculus P_n(I+N_q)=Σ D_(n,k)N_q^k/k! has leading n^(2q-2)N_q^(q-1) and ||N_q^(q-1)||2=1. Since -(m-1)≤Y≤1 and E Y=0, E[(1-Y)(Y+m-1)]≥0 gives σ²≤m-1, with equality only for the endpoint p0=(m-1)/m,pm=1/m. Independent exact rational jets for two higher-order admissible distributions and root/leading-ratio checks corroborated formulas at finite n, not infinite proof.

## originality

PASS

Cowal–Marshall–Pollock arXiv:2510.24608 establishes the same random-walk polynomial family and its boundedness/rapid exterior growth, but the inspected Theorem 1.2 and application assume diagonalizability with simple dominant eigenvalue; they do not quantify defective Jordan-block boundary amplification or all-order derivatives at 1. Miña-Díaz–Rubin–Wennman arXiv:2509.22588 studies geometric supremum norms of classical Chebyshev/Faber polynomials, not this recurrence derivative invariant. The deltoid special-case arXiv:2507.01885 primary PDF was inspected through Theorems 2–4 and §3.3 (the convergence theorem assumes an eigenvector basis), and restarted Lanczos arXiv:2511.05364 primary HTML was inspected through its matrix hypotheses and §2, which assumes symmetric or Hermitian matrices. Thus these inspected results also concern diagonalizable cases rather than defective Jordan growth. A hidden classical special-case derivative calculation remains a qualified priority risk. Published Resultary semantic search identified no theorem covering the exact σ-dependent coefficients. Originality is best-of-knowledge.

## value

PASS

Boundary defective Jordan blocks are a natural non-normal stress test for polynomial acceleration. The exact σ-dependent leading amplification for every fixed block size makes the stability cost measurable and the unique variance-maximizing endpoint law a genuine recurrence-design optimality statement, not merely a restatement of bounded scalar polynomials.

The dated certificate retains the supplied scientific assessment, sources and limitations.
