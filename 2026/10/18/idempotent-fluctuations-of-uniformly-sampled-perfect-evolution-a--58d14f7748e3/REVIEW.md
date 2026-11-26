# Independent mathematical audit

## correctness

PASS

Transitivity on nonzero vectors gives mean one. Ordered simultaneous nonzero idempotents cannot be distinct collinear vectors (t²=t forces t=1). For the D=(q^n−1)(q^n−q) ordered independent pairs, prescribing the images of both squared vectors has probability 1/D when those squares are independent and zero otherwise. In odd characteristic, for fixed x of support s, y with proportional squares has the same support and is a nonzero scalar times a coordinatewise sign change; this gives (q−1)2^{s−1} distinct y, of which q−1 are collinear. Summing the remainder against binomial(n,s)(q−1)^s gives exactly B=(q−1)((2q−1)^n−2q^n+1)/2. Since the mean is one, 1−B/D is the variance. B>0 from s=2; the correction (not the variance) tends to zero in both stated regimes, and for n=2 it equals (q−1)/(q(q+1)). In characteristic two Frobenius preserves independence, and a binary-independent list of fixed vectors is field-independent: applying T to a first relation over the extension makes its unique coefficients Frobenius-fixed. Thus R≤n, expected counts of ordered fixed k-frames are exactly one, and E[{R choose k}_2]=1/|GL_k(F₂)|. The proposed inverse follows from {k choose r}_2{j choose k}_2={j choose r}_2{j−r choose k−r}_2 and the binary binomial product ∏_{i=0}^{j−r−1}(1−2^i), which vanishes when j>r. This proves the full law and extension independence. Audited the frozen checker without executing it. Independent replay: python3 -I /workspace/independent_reproductions.py enumerates matrices with a direct kernel test and counts point solutions for (2,2), (4,2), (3,2), (3,3). Variances 1,1,5/6,23/26; the F₂ and F₄ dimension-two normalized histograms agree exactly. These are bounded cross-checks, not the proof.

## originality

PASS

The supported distinct contribution as of the frozen finding is the exact all-dimension odd-characteristic finite-q variance defect. The mean was explicitly known; the binary distribution is a consequence of established semilinear descent and binary fixed-space counting, albeit with a self-contained proof here. Two separate later catalogue findings overlap exactly with these components; they are not independent evidence of pre-finding priority. No inspected earlier source gives or implies the odd-characteristic defect.

## value

PASS

The exact, strictly positive odd-characteristic defect answers a natural second-moment question left open by the known normalization and large-field motivation. Its dimension and field dependence is essential: it quantifies the finite ensemble’s difference from characteristic two and identifies the projective square-collision obstruction. This is an all-parameter refinement, not a single field/dimension census; no full odd-characteristic law is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
