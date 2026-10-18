# Independent mathematical audit

## correctness

PASS

For a 4-cycle with rates (q,a,r,b), cost tq+a+r+b=1 and Laplacian spectral gap lambda2, the test vectors u=(1,1,-1,-1), v=(sqrt(t),-sqrt(t),-1,1) are orthogonal to constants. For t<=9, the nonnegative Rayleigh multipliers alpha=(3-sqrt(t))(1+sqrt(t))/16 and beta=1/4 sum their edge energies exactly to the total budget, giving lambda2<=4/(t+2sqrt(t)+5). The proposed interior rates meet this bound with double lambda2 and larger final eigenvalue; alpha,beta>0 for t<9 force the unique equality weights. For t>=9, v3=(3,-3,-1,1) gives lambda2<=1/5-(t-9)q/5. Its equality conditions give unique path rates (0,3/10,2/5,3/10) above 9 and complete segment 0<=q<=1/15 at 9, with eigenvalues 0,1/5,3/5-6q,6/5-10q. Independent Laplacian eigensolutions confirmed interior, transition and exterior, but exact Rayleigh equality arguments establish globality.

## originality

PASS

PASS best of knowledge. Sun–Boyd–Xiao–Diaconis (2006) give the general continuous-time fastest-mixing SDP, arbitrary-cost path solution, equal-cost cycle optimum, and 2D optimal cycle embedding. Their §5.3 explicitly calls arbitrary edge-cost cycles more complicated and does not give this single-heterogeneous-price 4-cycle t=9 transition or complete nonunique optimum segment; the t=1 point is prior. Shakeri et al. interlayer algebraic-connectivity allocations and randomized-gossip cost models optimize different variables.

## value

PASS

The four-cycle is the smallest natural connected ring with a single removable edge leaving a spanning path. The exact resource-allocation phase boundary between using and deleting the shortcut, the jump in spectral multiplicity, and the full critical optimizer continuum form a motivated complete finite parametric classification not reducible to a known fixed numerical table. It provides a sharp benchmark for spectral SDP sensitivity and active-set changes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
