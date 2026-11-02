# Independent mathematical audit

## correctness

PASS

Recast λ2 maximizing over nonnegative weights Σw=B as the maximum-variance unit-edge-length embedding dual. Symmetrize peripheral clique leaves and parameterize axial variance by scalar d and peripheral angular variance t≤(k−1)/(2k). The exact scalar derivative gives d=1, t=0 for k≤3 and d=sqrt((k+1)/(2k)) for k≥4; the explicit rates a=3(d+1)/((k+3)d), c=0 or (kd−3)/(k(k+3)d), b=(2kd+3(k+1))/(k+3), e=(kd+2k+3)/(k+3) attain λ2=1 with edge-budget V_k. The remaining quotient 3×3 block is PSD by the displayed sum-of-squares certificate. Complementary slackness at each edge/vertex and equality conditions enforce uniqueness, and the peripheral eigenspace gives multiplicity 1 for k=2 and k for k≥3. Independent numerical Laplacian eigenvalue checks at k=2,3,4,5,20 recovered budget, exact gap, edge activation and multiplicities; these are not the all-k proof.

## originality

PASS

Best-of-knowledge: Sun–Boyd–Xiao–Diaconis 2006 establishes the same general continuous-time uniform-stationary total-rate-budget SDP and dual variance embedding, not this all-k clique-plus-two-tail optimum, its uniqueness and k=4 activation. Richter–Rocha treat double-broom trees, not additional peripheral clique edges. Jafarizadeh computes discrete-time reversible-chain SLEM on lollipops with row-stochastic constraints, a different feasible region and objective. Li–Guo–Shiu treat fixed unweighted kite graph topology. Kirkland–Pati 2002 is plausibly more general but only its abstract was obtained; authorized Oxford request reported disconnected VPN. Qualified PASS, not a priority certificate.

## value

PASS

The bottleneck-plus-clique network is a natural mixing-design graph. The optimal complete rate allocation exhibits an exact all-size structural edge-activation transition at k=4 and identifies a unique optimizer plus spectral degeneracies; no numerical optimization or unmotivated slice is substituted for the exact theorem. It answers which dense-community edges should receive zero physical rate under a global budget.

The dated certificate retains the supplied scientific assessment, sources and limitations.
