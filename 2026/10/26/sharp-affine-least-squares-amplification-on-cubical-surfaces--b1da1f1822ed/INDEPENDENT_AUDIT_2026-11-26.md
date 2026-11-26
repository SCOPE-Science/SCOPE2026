# Independent mathematical audit

## correctness

PASS

Independent reconstruction: the facet mixture pins one coordinate to a fair sign, giving diagonal second moment (d+2)/(3d). The kernel row mass is convex and invariant under sign changes, so a vertex norms it; continuity and full surface support make this an essential supremum. The sign row realizes the norm and symmetry gives L1 duality. The row law is 1+c_d(S_{d-1}+epsilon); integrating the simplex inclusion-exclusion CDF for the sum of k uniform [0,1] variables gives H_k with the stated 4/(k+1)! factor and the two rational benchmarks. For standardized S_k, the characteristic function expands as exp(-u^2/2)(1-u^4/(20k)+O((u^6+u^8)/k^2)) on |u|<=k^0.1, with Gaussian decay there and exponentially small integrated tails outside by the sinc bound. The absolute-moment integral gives relative +1/(20k); density inversion gives the stated O(k^-3/2) local error uniformly over bounded shifts. The two facet shifts contribute +5/(3d) on top of -49/(20d), giving -47/(60d); the volume shift adds 1/(6d) to 1/(20d), giving +13/(60d) and the claimed O(d^-3/2) gap error. Replay: RESULT.md lines 33–84; verify.py and VERIFICATION.md describe 60 finite checks (including quadrature for d=2–10), not re-executed and not used as an all-d proof.

## originality

PASS

Credit is for the facet-area calculation with separate first correction and controlled remainder, not for the volume coefficient or the qualitative ordering. The exact boundary formula, the benchmarks, and the leading scaled gap have equivalent coverage in the inspected distinct later catalogue record; the dates provide no basis for claiming that the later record anticipates this frozen result, and it does not give the relative O(d^-2) surface expansion or O(d^-3/2) gap remainder. The same-day parallelepiped record covers the volume coefficient without establishing intra-day priority; the frozen record uses volume as a comparison.

## value

PASS

Facet sampling is a natural continuous alternative to cubical volume sampling. The exact endpoint stability constant for each dimension and the first nonzero quantitative loss from changing the sampling rule distinguish two laws with identical leading growth. The estimate provides a concrete comparison beyond a generic projection bound or a few evaluated norms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
