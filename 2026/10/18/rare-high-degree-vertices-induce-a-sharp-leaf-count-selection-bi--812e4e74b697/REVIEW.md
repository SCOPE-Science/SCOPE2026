# Independent mathematical audit

## correctness

PASS

The scope in RESULT.md lines 29–37 and 165 is subsequential: take integer pairs (n,k) with n→∞ and n/k!→eλ, for example n=floor(eλ k!) along k→∞. The positive finite intensity is generally impossible along every integer n because the successive intensity levels have diverging ratios. Prüfer multiplicities are multinomial on m=n-2 draws, and the degree threshold is k+1. For fixed r, n^r times the probability that r specified loads all equal k tends to λ^r, and the ratio on raising any coordinate is at most 2/(k+1); summing over excess compositions controls the first and second moments of the excess J-rk, with J the selected total load. Conditional empty-box expectation equals f(n-r,m-J), where f(b,t)=b(1-1/b)^t. At (n,m) its first derivatives in b,t are 2/e+O(1/n), -1/e+O(1/n); on b≥n/2 and 0≤t≤m its second derivatives are O(1/n). Thus for fixed r, the conditional shift is (rk-2r)/e+o(k), yielding rλ^r/e for the scaled mixed factorial moment. For all r with rk≤m, bounded first derivatives give C(J+r). Multiplying the event indicator bound by J uses x(x)_k=(x)_(k+1)+k(x)_k, giving the displayed uniform bound Cr(k+2)(n/k!)^r; r with rk>m contribute zero. Dividing by k r! gives a summable bound, so the alternating sum gives -λe^(-λ)/e for the no-hub indicator and the opposite sign for A_n. The ordinary factorial moments likewise give the Poisson law and its no-hub mass; dividing by the limiting event probabilities gives both conditional means. The frozen verifier was inspected, not run. An independent exact finite check enumerated partitions of n-2 with at most n parts, padded with zeros; for multiplicities c_j of load j, weight each profile by n!(n-2)!/∏_j(c_j!(j!)^c_j). For (n,k)=(11,3),(15,4),(24,4),(38,5), total weight and leaf total matched n^(n-2) and n(n-1)^(n-2), and the covariances were positive. This finite check does not certify the limit.

## originality

PASS

The accepted contribution is the mixed critical-event coefficient and resulting leaf-mean shifts, not the Poisson count or the critical maximum marginal. The inspected allocation and fixed-mark results do not supply the uniform mixed calculation needed for the global union of rare events.

## value

PASS

The natural rare-extreme threshold produces a quantitatively diverging leaf selection bias, smaller than the standard sqrt(n) fluctuations. The exact mixed coefficient and separate event-conditioned means capture dependence that marginal extrema and ordinary central-limit laws miss. The subsequential lattice restriction is necessary rather than an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
