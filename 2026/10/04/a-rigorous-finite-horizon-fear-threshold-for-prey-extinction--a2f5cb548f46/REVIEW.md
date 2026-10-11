# Independent mathematical audit

## correctness

PASS

The comparison proof reconstructs from the frozen equations without using the saved verifier as proof. Before the first prey zero, v' >= -dv gives v(t) >= v0 exp(-dt), and 1+kv >= kv gives u' <= a exp(dt)u/(k v0) - c v0^m exp(-mdt)u^p. With w=u^(1-p), this becomes a linear differential inequality. The integrating factor exp(-Phi_k(t)) yields a contradiction to positivity through T whenever (1-p)c v0^m integral_0^T exp(-mds-Phi_k(s)) ds > u0^(1-p). Bounding Phi_k(s) by Phi_k(T) gives exactly R_T exp(-Phi_k(T))>1 and hence the displayed K(T). The iff statement about existence of a horizon is only for this certificate and follows from monotone convergence R_T upward to R_infinity. Independent high-precision replay gives R_infinity=1.6617980909507749..., R_1.5=1.1612741245896543..., K(1.5)=15.379188974865015..., and strict coarse/sharp margins 1.0058182537801465... and 1.1289939181497174... at k=16.

## originality

PASS

Best-of-knowledge originality survives a statement-level comparison with the exact motivating source. That paper claims qualitative fear-driven finite-time extinction and prints a large-k comparison argument, but its displayed comparison reaches a strictly positive upper bound and does not establish the present integrating-factor contradiction or the finite-horizon formula K(T). Remark 5 explicitly leaves quantitative control of the fear size open. Fresh Resultary searches found no earlier record implying this exact k-versus-T certificate. The novelty is therefore the valid explicit finite-horizon certificate for the exact two-dimensional model, not the general idea that sublinear predation can cause finite-time extinction.

## value

PASS

The source makes fear-driven finite-time extinction a central conclusion and itself identifies quantitative fear size as an open issue. A rigorous prescribed-horizon certificate separates a provable regime from the much smaller plotted simulation value and gives a reusable analytic bound on the exact model. This is a motivated quantitative repair/boundary result rather than a routine parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
