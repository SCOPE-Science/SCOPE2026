# Scientific assessment: rarity ordering of terminal coupon types

## Correctness — PASS

Every probability in the theorem is well defined and strictly positive for each integer completion time \(t\ge mq\), since all required rates are positive. A direct final-draw multinomial decomposition gives the exact joint formula. The coefficient sequence of each truncated exponential is log-concave with interval support, including a point-mass factor for zero null rate; convolution preserves this property. The Toeplitz minors are therefore nonnegative. In the two-column Cauchy–Binet identity the specific indices \(r=n-h\) and \(s=r+1\) give a strictly positive summand \(a_h^2(c_rb_s-c_sb_r)\), proving strict ordering at **every** admissible time, including the boundary \(m=2,p_0=0\). The endpoint, independence, covariance-sign and late-time consequences follow by elementary conditional normalization. Independent truncated-state dynamic programming checked 5,416 exact rational assertions, multiple quota sizes and null-rate boundaries; finite tests were not used in place of the proof.

## Originality — PASS, with residual historical-priority risk

May's 2008 equations in Section 2 already decompose the quota completion time by terminal type and give the underlying generating functions. This counting identity is **not** a novelty claim. Shank and Yang (2013) study nonuniform coupon laws with random quotas; Anceaume, Busnel and Sericola (2014) establish completion-time and uniform-extremality properties, including a null category. The inspected texts did not assert the exact-time likelihood-ratio comparison for each pair of terminal types. The proposed statement is a strict ordering of two-dimensional slices of the joint law, not a marginal coupon-cover-time distribution and not the first-repeat statistic. Searching synonymous formulations and comparing the exact implications found no equivalent or stronger covering result in the accessible material. A general total-positivity theorem together with a known terminal-count formula could conceivably imply this statement, and some historical material was not accessible in full; priority is therefore qualified, not declared proven unique.

## Mathematical value — PASS

The theorem identifies a global, nonasymptotic structural dependence principle in the classical nonuniform coupon collector: how exact completion delay changes *which* coupon completes the collection. Its all-time, all-rate, common-quota likelihood-ratio ordering is stronger than a mean or covariance comparison and yields sharp independency and rarest-type concentration characterizations. This is a motivated refinement of quota-completion theory rather than an arbitrary parameter-specific calculation. The optional null category and arbitrary common quotas preserve the full qualitative law.

## Scope and relevant literature

The fixed joint counting formula, existing quota-completion theory, and classical log-concave convolutions are not claimed as new. Sources: Russell May, *Coupon Collecting with Quotas* (2008), Sections 2–3, DOI 10.37236/906; Shank and Yang, *Coupon Collector Problem for Non-Uniform Coupons and Random Quotas* (2013), DOI 10.37236/3348; Anceaume, Busnel and Sericola (2014), arXiv:1402.5245, Sections 2 and 5; Mahmoud and Smythe, *On the Joint Behavior of Types of Coupons in Generalized Coupon Collection*, DOI 10.1239/aap/1339878719 (full 23-page public primary PDF inspected, notably Sections 1–6 and 10; concerns occupancy-frequency joint fluctuations rather than the terminal coupon conditional on completion time). The remaining limitation is historical priority of the strict ordering, not a missing step in its stated mathematical proof.

Self-review: passed. Independent audit: not yet performed.
