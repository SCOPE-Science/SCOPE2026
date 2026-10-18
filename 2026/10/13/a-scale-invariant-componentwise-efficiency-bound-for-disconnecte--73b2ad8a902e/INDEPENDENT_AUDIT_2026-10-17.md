# Independent mathematical audit

## correctness

PASS

The ORIGINAL RESULT is NOT correct: it claims B_comp is the minimum across gauges of the first coefficient expression in source Corollary 4.8, but that printed expression takes the denominator minimum across ALL i<j, even across disconnected components. An exact counterexample has two disconnected interacting pairs each with balanced weights (1,10), λ_forward=10 and λ_backward=1. Then B_comp=11, while the ALL-pair expression G_all minimizes to 20: normalize scales (1,t), t>=1, global max 10t and min pair ≤t/(1+t), giving G_all≥10(t+1)≥20, attained at t=1. The corrected final RESULT and SLOGAN REMOVE this false assertion and prove instead: (a) InEff(φ^p)≤B_comp using separate component cost/potential comparisons m_k SC_k≤Φ_k≤M_k SC_k and product minimizers; (b) for at least one interacting edge, B_comp is the exact infimum over component gauges of G_E with denominator restricted to POSITIVE interacting edges. For each component G_E≥M_k/m_k, and scales c_k=1/M_k on nontrivial components plus small singleton scales attain equality. All-isolated graph gives InEff=1, and G_E is not defined there. Independent rational counterexample plus symbolic ratio reasoning check all boundary cases. These corrected claims are valid under exact detailed balance, nonnegative costs, and independent component policies; they do not optimize the literal all-pair formula.

## originality

PASS

The surviving CORRECTED claim is a motivated componentwise optimization of an edge-restricted coefficient certificate, distinct from the source all-pair Corollary 4.8 formula. Source Assumption 2 permits disconnection and Proposition 4.7 supplies nonnegative coefficient comparison; the full exact optimization over arbitrary component gauges was not stated in inspected sections. Distinguishing G_E from G_all is essential, and the uncorrected statement fails correctness.

## value

PASS

The source explicitly admits disconnected interaction groups, for which its global bound is gauge dependent even though chosen policies are not. The corrected theorem produces an intrinsic valid componentwise efficiency guarantee and exactly normalizes the mathematically meaningful interacting-edge certificate. A concrete two-component (1,10) example shows why the distinction from the printed all-pair formula is scientifically necessary; this is a substantive motivated correction, not a cosmetic relabeling or assertion of sharp actual inefficiency.

The dated certificate retains the supplied scientific assessment, sources and limitations.
