# Independent mathematical audit

## correctness

PASS

For z=(Re Z,Im Z), Jacobian J has unit columns (−sinθ_i,cosθ_i) and θ+=θ−hJᵀz; G=JJᵀ has eigenvalues in [0,N]. Odd N: for any unit direction approximate cos φ_i by s_i=sign cos φ_i; |∑s_i|≥1 and ∑(1−|cosφ_i|)≤∑sin²φ_i, so λ_min(G)≥1−|Z|. Complex-exponential remainder gives z+=(I−hG)z+R, |R|≤Nh²|Z|²/2, implying |Z+|≤(1−h/4)|Z| throughout |Z|≤1/2, h<1/N, and summable phase increments yield the ≤4|Z_n| tail. For even N=2m, θ=(u,−u,0^(m−2),π^m) is exactly invariant; Z=2(cos u−1) and u+=u−2h sin u(1−cos u) ∈(0,u). Taylor: u+=u−hu³+(h/4)u⁵+O_h(u⁷) hence y=u^-2 satisfies y+−y=2h+(3h²−h/2)/y+O(y^-2). As y~2hn, remainder after subtracting 2hn+(3h/2−1/4)log n is summable (O(log n/n²)), giving finite constant +o(1). Direct independent symbolic coefficient check and numerics at N=4,h=.2 gave stabilized corrected residual about 2.666 at n=10k,25k,50k; bounded simulations not infinity proof. h=1/6 admissible only N=4, matching exact cancellation.

## originality

PASS

The earlier explicit same-map Buescu–Oliveira (2025) studies exactly three clocks and Morse–Smale sinks. Sclosa (2022) covers prior geometry of odd/even balanced states, explicitly credited; neither gives an all-size finite-step exponential contraction with uniform |Z|≤1/2 domain and a separate even exact slow manifold carrying (3h/2−1/4) logarithmic correction. A closely named 2025 discrete Kuramoto article could only be assessed at abstract/preview level; this is substantial priority residual risk but not independent evidence of coverage or scientific failure.

## value

PASS

A quantitatively sharp geometric odd/even dynamical dichotomy for a natural complete graph coupled map, including a proved common odd-size attraction domain, exact invariant even slow orbit and logarithmic correction/cancellation, is substantive. It is not merely renaming the known continuous-time equilibrium parity observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
