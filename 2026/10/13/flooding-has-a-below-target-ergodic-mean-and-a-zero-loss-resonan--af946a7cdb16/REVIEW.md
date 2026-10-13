# Review

## Correctness

PASS. The scalar Flooding update is exactly multiplicative by \(1+h\) below the flood radius and by \(1-h\) above it. For \(0<h<1\), taking log-radius turns the dynamics into two translations and, after a finite transient, a rigid circle rotation. Standard rotation theory and direct integration give the stated occupancy and mean-loss formulas. The \(h=1\) endpoint is a separate exact doubling/zeroing argument. The packaged checker replays the critical identities and resonances.

Scientific risk: the full classification is deterministic and one-dimensional, and exact boundary hits depend on the stated kink convention.

## Originality

PASS. The defining paper gives the ascent/descent threshold rule and an informal random-walk description. Later work proves a local two-step gradient-regularization effect and gives scalar-quadratic Flooding illustrations and stationarity bounds, but no exact global orbit or time-average classification was found. A checked Fromage result already uses a logarithmic circle rotation for another optimizer, so that device is treated as prior; the accepted contribution is the Flooding-specific below-target mean, occupancy law, resonances, and exact-solve zero-loss absorption.

Residual risk: an unindexed note may have solved the same piecewise map.

## Value

PASS. Flooding is explicitly intended to keep loss near a prescribed nonzero level. The exact theorem shows a systematic deterministic calibration bias below that level and a natural learning-rate endpoint that instead forces generic trajectories to zero loss. Those two facts directly test the method's defining design goals and provide sharp guidance about what the flood level and learning rate do in a solvable model.

Self-review: passed. Independent audit: not yet performed.
