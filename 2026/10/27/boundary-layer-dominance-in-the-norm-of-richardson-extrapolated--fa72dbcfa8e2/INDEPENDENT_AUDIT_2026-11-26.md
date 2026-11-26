# Independent mathematical audit

## correctness

PASS

At each x, the nested grid shares exactly the even knots. The mass at odd knots is nonnegative and the signed weights sum to 1, so total variation is one plus twice the sum of negative masses in absolute value. Interpolating the finitely many signs attains this value on the continuous-function unit ball. For nx bounded and convergent, the two binomial laws converge in ℓ¹ to the stated Poisson laws; restricting to even coordinates and taking positive parts are ℓ¹-continuous. For σ²=nx(1−x)→∞, both binomial expected cell counts diverge. On |k−nx|≤Aσ the relative changes in the counts are O(A/√(nx)) and O(A/√(n(1−x))); Stirling expansion gives the uniform local limits φ(y) and √2φ(√2y) after scaling by σ and 2σ, respectively. Chebyshev controls the discarded positive-part tail by A^−2. The Gaussian difference changes sign at |y|=√log 2, and the Poisson local limit with the same tail bound gives G(λ)→H. Independently checked the strict gap with exact rational arithmetic: take s=e^(−7/5) between its alternating Taylor sums of degrees 17 and 18. Q_0,Q_3<1<Q_1,Q_2 and Q_(k+1)/Q_k=(14/5)/(2k+1), so only k=1,2 have 2p_(2λ)(2k)>p_λ(k). Using the even Poisson mass sum gives the stated witness, enclosed between 1.395 and 1.396 by substituting the s bounds with the indicated signs in 1−2s⁴+(48608/1875)s²−(119/25)s. For H, 2(√2−1)√(log 2/π)<0.391 follows using √2<1.415, log 2<0.694 (the atanh series at 1/3) and π>3.14. Compactness now gives a finite maximizer for G, and comparison along x=λ/n supplies the liminf. After reflection x≤1/2, any subsequence of maximizing points either has a finite nx cluster point or has nx→∞, which would yield H and contradict the witness. Since G(0)=1 the scales are bounded away from zero and every cluster point maximizes G. No uniqueness follows or is claimed. In Step 4 the negative differences at k=1,2 are for p_λ−2p_(2λ), the reverse of the actual evaluation weights; the final formula uses the correct sign. The uploaded checker was inspected but not executed.

## originality

PASS

The meaningful distinct claim is the sharp C-to-C stability asymptotic for the nested two-degree combination, with a strict Poisson boundary advantage and localization of every maximizing sequence. The operator itself is classical, and its finite total-variation identity is routine. Available comparison passages do not contain or mechanically imply the boundary-versus-bulk result. This is a bounded best-of-knowledge assessment, not a priority certification.

## value

PASS

This sharp stability problem is motivated by a standard approximation acceleration. The limit and localization are useful beyond the finite norm formula or a triangle-inequality bound: Gaussian asymptotics at every genuinely interior sequence provably miss the worst bounded-input amplification. The strict analytic witness and the resulting boundary scale address a naturally occurring extremal regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
