# Independent mathematical audit

## correctness

PASS

The maximum of two independent iid copies has mass b_k=F(k)^2-F(k-1)^2, so its PGF is Poisson-binomial iff all zeros are real nonpositive. For heterogeneous two-trial X=B_p+B_r, polynomial quadratic discriminant equals A(A+4(1-p)(1-r)) with A=(p-r)^2+2pr(1-p)(1-r)>=0; positive coefficients force nonpositive real roots, including degenerate boundaries. For every m>=3, homogeneous binomial small-p rescaling yields G_{m,p}(u/p)->2(1+u)^m-1 with simple nonreal roots; root continuity makes nonreal PGF roots persist for sufficiently small p. For m=3 the exact cubic discriminant is 108p^6(1-p)^12R(p) with R=4p^6+8p^3+3p^2+6p-1, strictly increasing for p>=0, with unique p*~0.1507324653; sign criterion plus positivity gives PB iff p>=p* in 0<p<1, with p=0,1 degenerate PB. Independently verified both factorizations symbolically in SymPy; finite test cannot replace nonreal-root continuity for every m.

## originality

PASS

Existing work shows closure of ultra-log-concavity under discrete order statistics; PF-infinity or real-rooted generating polynomials characterize the stronger Poisson-binomial property and need not be preserved. The explicit two-trial closure, small-p nonclosure at every m>=3, and sharp m=3 algebraic parameter boundary are not consequences of the cited weaker ULC closure theorem. Tang-Tang survey covers distributions/real-rooted criterion but not an inspected exact max-of-iid phase classification. Resultary semantic search found only different Poisson-binomial cumulant/dispersion and order-statistic correlation results, no same statement. PASS best knowledge with aliases/Pólya-frequency risk.

## value

PASS

The closure problem for an analytically natural nonlinear transformation of the Poisson-binomial family (two-sample maxima) has a sharp smallest failure size and a nontrivial exact critical probability. It delineates PF-infinity versus ULC preservation and supplies a minimal counterexample with useful parameter phase transition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
