# Independent mathematical audit

## correctness

PASS

The frozen theorem statement survives, but the frozen proof's endpoint contribution at RESULT.md line 64 has the wrong sign: for finite W_infty it is +sum_{k>i}p_k/W_infty, not its negative. It is material when alpha<-1. The replacement under repairs/3 derives the innovation identity from the normalized weighted depth average, then telescopes at finite n: the main term is sum_{j=i+1}^n a_j(p_j-p_i)+(sum_{k=i+1}^n p_k)/W_n. The Cesàro term for summable weights contributes (1-sum_{k>=i}p_k)/W_infty, giving exactly the claimed (1-p_i)/W_infty when combined; for nonsummable weights both boundary terms vanish. Absolute convergence comes from telescoping a_j, and monotone decrease of p_j follows from the sum or layer-cake count. This gives all signs and the summable equivalent; power and harmonic sum estimates give the other two equivalents, and partial fractions recover the alpha=1 formula. Independent python3 /workspace/repairs/3/verify_limit.py passed 90 exact finite enumeration/telescoping checks and the rational constants for alpha=-2, where the root is negative and label 2 is positive. The repair also replaces the confusing propagation recurrence at frozen line 41 with the exact weighted-average recursion. The script does not establish the infinite limits; the corrected proof does.

## originality

PASS

The repaired proof establishes the same fixed-label theorem. The innovation representation and root-only overlaps are credited. The distinct supported contribution is the all-label mixed covariance, including the surviving summable-weight correction, sign reversal, and sharp large-label regimes.

## value

PASS

This mixed observable distinguishes early high-influence vertices from sufficiently late vertices in a regime where mass remains concentrated on early labels. The exact finite-weight boundary contribution explains reversal despite every summand of the difference series being negative. The quantitative asymptotics, including the harmonic critical correction, give information not captured by marginal path-length or degree results. No moving-label uniformity is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
