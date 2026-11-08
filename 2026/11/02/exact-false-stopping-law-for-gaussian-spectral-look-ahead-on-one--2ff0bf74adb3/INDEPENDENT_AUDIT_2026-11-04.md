# Independent mathematical audit

## correctness

PASS

PASS. For E=diag(1,d I_N), 1<=b<=N, q>=0, Gaussian independent Ω, the nonstationary spectral norm of Q^T E squared is d²+(1-d²)||P_range(Y)e1||² by rank-one eigenvalues. The singular-axis scaling D=diag(1,d^(2q+1)I_N) sends a Haar b-plane with S=||P_R e1||² to projection S/(S+d^(4q+2)(1-S)); exact Haar law S=Z/(Z+V), Z~chi²_b, V~chi²_(N+1-b) independent, yields the stated beta CDF including 0 at τ<=d and 1 at τ>=1, with full-block b=N+1 giving L=1. Chi-square LLNs give fixed-width critical alpha=1/(4q+2), chi-square critical law Z/(Z+1) and growing-width ratio beta=b/(N d^(4q+2)). Equality of threshold and limiting value is explicitly unclassified. The claim is for the indicator, not an entire randomized low-rank algorithm.

## originality

PASS

PASS, best-of-knowledge and qualified. The Haar projection beta law and one-spike singular geometry are classical, and published random-ellipsoid section-radius work shares the ingredient. The present final claim is the exact beta transfer through the powered look-ahead spectral estimator plus its conditional stopping probability and width/power phase transition; none of the material actually read establishes that complete statement. The source introducing the same stopping estimator (Smith–Do–Chen 2026) remains a material full-text-access limitation, and a hidden equivalent special-case formula is possible; not claimed as proven priority.

## value

PASS

PASS. Exact, finite-sample calibration of a naturally used spectral stop test is useful independently of general error bounds. The 0.9897679877478459 false-stop example with a separated spike demonstrates why a small tail singular value alone is insufficient when tail multiplicity is large. The sharp power/sketch-size transition quantifies the remedy. A one-spike flat-tail restriction is mathematically motivated, not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
