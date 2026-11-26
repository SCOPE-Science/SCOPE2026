# Independent mathematical audit

## correctness

PASS

PASS for the corrected proof and checker in repairs/2, with the theorem unchanged. The frozen proof and checker incorrectly use 6 as an upper majorant for the left side of Gilmer's (B2). The primary theorem's hypothesis is sqrt(3μb)·σ ≤ b^(3m/8), with the σ outside the radical. For b=3, μ=5/3, σ²=26/9, the left side squared is 130/3, strictly between 36 and 49. Both corrected files use 7 and justify it exactly. Independent rational/integer checks of the actual B1, B2, B3 at m=136 and 224 also pass by squaring nonnegative sides, not by relying on the faulty bound. For ≥4 ternary digits S(n)≤4d<3^(d−1); the map preserves [1,26], so trajectories eventually enter a finite cycle. Exact recomputation by the multinomial sum over suffix counts of 1s and 2s, with direct trajectory classification, matches both printed shell totals and the strict ratios; literal enumeration gives 280 happy integers in the seven-digit shell as a regression. Leading digits 1 and 2 contribute 1 and 4, respectively. Each shell partitions into 2·3^(m/4−1) m-strict intervals, so by averaging a starting happy interval and a starting nonhappy interval have the requisite densities. Gilmer Definition 1.1 includes the digit rule (0,1,4); Definition 1.2 permits the complement union of positive cycles. Definition 3.1 and Theorem 4.1 then give lower bounds on upper densities, with the latter converting to an upper bound on the happy lower density by complementarity. Exact rational checks show the loss exponent magnitude is <10⁻⁶ at both m; multiplication by 1−10⁻⁶ preserves the two stated strict targets. The result does not follow from finite shell counts alone. No frozen executable was run.

## originality

PASS

The corrected proof makes the same specific ternary density claim. Gilmer's transfer framework and digit counting method are prior, but do not supply the contrasting exact ternary shell inputs. The inspected publications and indexed variants do not state or imply the specific density dichotomy without this new finite input. The closest survey was not accessible in full, and that limitation is not used as evidence.

## value

PASS

Existence of natural density for the ordinary square-digit rule is a natural asymptotic question already singled out by the surrounding literature. In base three, two exact, sharply contrasting shell inputs to the transfer theorem resolve it with a gap greater than 0.26176 between the limiting bounds. The choice of shells serves the asymptotic result, not an arbitrary isolated numerical census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
