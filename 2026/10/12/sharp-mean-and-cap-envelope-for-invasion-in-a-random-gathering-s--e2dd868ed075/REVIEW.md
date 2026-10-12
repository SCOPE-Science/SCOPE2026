# Self-review

## Correctness

PASS. The source gives
\[
\mathcal R_0=C\,\mathbb E[\Theta(\Theta-1)].
\]
The exact lower bound follows from
\[
(n-k)(n-k-1)\ge0
\]
on integer gathering sizes, and the exact upper bound follows from
\[
n(K-n)\ge0.
\]
The stated adjacent-support and endpoint distributions attain the two bounds, and their convex mixtures attain every intermediate value. The no-cap family has exact factorial moment \(m(L-1)\), proving unboundedness.

## Originality

PASS. Cortez derives the factorial-moment formula and several named distribution examples, but does not give the fixed-mean, fixed-cap extremal interval. Boyer et al. give closely related policy motivation and show that the distribution of gathering sizes matters, but use a different expected-incidence model and do not state this envelope. Searches by source identifier, variance, factorial moment, cap, and sharp-bound aliases found no equivalent statement.

## Value

PASS. The result converts an intervention-motivated reproduction formula into an exact robust-policy theorem. Mean and cap can be insufficient even for the sign of \(\mathcal R_0-1\); the theorem gives the sharp regime in which all compatible laws are safe, all are supercritical, or the answer depends on distribution shape. It also shows that without a cap, fixed mean alone gives no finite worst-case invasion bound.

## Closest literature and limitations

Boyer, Rumpler, Kissler, and Lipsitch independently demonstrate that gathering-size distributions and heavy tails strongly affect gathering restrictions, which supports the importance of the question. Their model and target quantity differ from the source-specific reproduction-number problem solved here.

The upper extremizer uses size-zero gatherings, which the motivating model explicitly allows. A stricter application requiring every gathering to be nonempty has a different upper envelope. The theorem addresses invasion threshold, not full nonlinear epidemic burden or welfare-optimal policy.

Self-review: passed. Independent audit: not yet performed.
