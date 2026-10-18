# Independent mathematical audit

## correctness

PASS

Direct inspection of the actual Su–Long manuscript shows λ in mean−variance payoff and the intermediate media Eq (18), but no λ in final governing drift equations (19)–(24) or the discrete updates (42)–(44). For identical other parameters, initial states and noise, identical maps produce identical iterates, and well-posed ODE/SDE models have the same trajectories/laws under standard uniqueness assumptions. On admissible y=0 face the ambiguous media payoff has two outcomes separated by (1−z)(F_m−F_m prime) with probabilities x,1−x, giving variance x(1−x)(1−z)^2(F−F prime)^2 and payoff-correct replicator sensitivity x(1−x)z(1−z)^3(F−F prime)^2. Exact fractions with x=z=1/2, fines 7/2 and 4/5 give 729/6400; source Eq18 gives 729/3200; final equations zero. Checked source verification/verify.py arithmetic and independently multiplied fractions. No inference about actual unpublished simulator is made.

## originality

PASS

General identifiability observations and a different published stochastic-coalition error are known, but the demonstrated absence of risk coefficient lambda from Su–Long 2026 final Eqs 19–24/42–44, contrasted with the nonzero exact payoff sensitivity, is a specific source contradiction not found covered by prior targeted searches; no assertion about private code.

## value

PASS

Identifies a consequential within-paper contradiction between promised sensitivity to media risk preferences and the only published evolution and numerical laws; zero Fisher information under defined likelihood and exact observational equivalence make the policy/interpretation limit explicit. Not just a cheap normalization check: it invalidates inference about λ from the stated model and contrasts with an independently computed nonzero payoff-level response.

The dated certificate retains the supplied scientific assessment, sources and limitations.
