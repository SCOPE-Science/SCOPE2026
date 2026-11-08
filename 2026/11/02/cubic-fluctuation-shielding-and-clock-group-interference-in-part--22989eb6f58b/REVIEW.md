# Independent mathematical audit

## correctness

PASS

For a connected finite weighted graph, nonempty reset S and unreset U, strictly positive grounded Laplacian H, and independent rate-r group clocks, the synchronous squared-distance Lyapunov generator  -2d^T A d-r d^T P d gives uniqueness and second moments. The first moment depends only on reset projection P, not the grouping: (A+rP)mu=omega. Reconstructed exact covariance equation AC+CA+r sum_g(C-R_g C R_g)=r sum_g P_g mu mu^T P_g. With t=1/r and C_SS=t^2 D_t, C_US=t^3 X_t, C_UU=t^3 Y_t, limiting block equations uniquely yield D=sum_g b_g b_g^T, X=-BD, HY+YH=2BDB^T. SPD H makes the Sylvester operator invertible; integral Gramian Q PSD and nonzero iff at least one Bb_g nonzero. Independent symbolic solution of the star full stationary covariance system gives Var(center)=nu^2/[(r+1)(r^2+5r+5)] for independent opposite-sign leaves, whereas common-clock symmetry forces exactly zero. The asymptotic r^-3 is per fixed graph; it can vanish.

## originality

PASS

The 2026 partial reset Kuramoto work establishes the fast-reset grounded-Laplacian pinned limit, and general linear PDMP work already gives exact moment closure. The present finite-dimensional theorem additionally identifies the order r^-3 unreset covariance Gramian for arbitrary clock partitions, its vanishing criterion, exact stationary star cancellation and reversal of any proposed clock-group ordering. Those are not stated in inspected primary results. As a specialization of general linear jump-moment theory, an unlocated theorem may in principle imply it; best-of-knowledge PASS is qualified.

## value

PASS

Grouping reset clocks while holding each node reset rate and every stationary mean fixed isolates a genuine stochastic-correlation intervention. The exact cubic shielded covariance, its PSD forcing and an explicit example showing no universal ordering are motivated, structurally useful facts in network stochastic dynamics; the value is not merely existence of linear moment equations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
