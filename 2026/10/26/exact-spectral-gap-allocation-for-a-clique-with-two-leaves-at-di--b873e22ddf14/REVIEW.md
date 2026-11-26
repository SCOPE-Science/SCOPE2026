# Independent mathematical audit

## correctness

PASS

With t=sqrt(1-u^2) and s=sqrt((k+2)/k)/2 the scalar equation is (ks-2t)/(k+4)=t/(2sqrt(1-t^2)); the difference is strictly decreasing from positive to minus infinity, so there is exactly one admissible root. All edges of the displayed embedding have squared length one, including when k=1 and the peripheral simplex is a single point. Applied to its centered coordinates the Rayleigh bound gives lambda_2 V<=B for every feasible allocation. Substitution into the rates gives LQ=lambda Q_c in the odd, even and simplex directions using mu/s=-k/H and mu=-t/(2u). There are 1+1+(k-1) such independent modes; the two block traces are 2w_AB+k w_AC+2w_AX and (k+2)w_AC+2w_AX, both strictly greater than 2lambda, so the two other nonzero eigenvalues strictly exceed lambda. Summing weights gives lambda V_k, and tracing the embedding identity also gives lambda V, proving equality and the optimal B/V_k. The root gives u->1/sqrt(2); division in the stated budget expression yields k/2+7/2+2u+1/u+O(1/k), giving the claimed asymptotic.

## originality

PASS

Maximum-variance unfolding is an established exact dual framework for this optimization. Neither the inspected general theorem nor the strongest matching graph or optimization records evaluate this family with two leaves at distinct core vertices. The explicit root, rates, multiplicity and asymptotic are the supported distinct contribution.

## value

PASS

The family isolates the competition between a dense core and two bottlenecks on distinct hubs. The exact evaluation specifies how to allocate a finite budget across all existing edge classes, shows that none need be dropped, and gives a sharp spectral benchmark with the Fiedler multiplicity and asymptotic scale. This is substantive graph-specific information not obtained merely by restating the SDP.

The dated certificate retains the supplied scientific assessment, sources and limitations.
