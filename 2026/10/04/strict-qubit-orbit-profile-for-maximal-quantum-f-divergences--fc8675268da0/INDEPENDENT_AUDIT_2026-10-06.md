# Independent mathematical audit

## correctness

PASS

For faithful nondegenerate qubits, the squared-overlap matrix is necessarily the two-by-two bistochastic matrix with entries \(q,1-q\), so \(t=\operatorname{Tr}(\rho\sigma_U^{-1})=t_{\min}+\Delta(1-q)\) with \(\Delta>0\). The determinant of \(A=\sigma_U^{-1/2}\rho\sigma_U^{-1/2}\) is orbit-independent. Cayley--Hamilton gives the claimed resolvent reduction and \(\operatorname{Tr}[\sigma_U(A-I)^2]=t-\delta-1\). Substitution into the standard operator-convex representation yields the displayed scalar profile. Its derivative is a nonnegative quadratic coefficient plus an integral whose kernel is strictly positive for every \(a\ge0\); non-affinity means at least one of these two positive components is nonzero. Hence the profile is strictly increasing in \(t\), therefore strictly decreasing in \(q\). The phase-quotiented endpoint and level-set claims follow, and \(q=\cos^2\theta\) gives the stated quadratic coefficient. I independently replayed the rational kernel derivative and orbit-slope identities; the inspected package verifier checks the same algebra on representative exact spectra without being used as an infinite proof.

## originality

PASS

The exact same-object Nguyen--Nguyen--Le preprint was materially inspected at its operator-convex representation and unitary-orbit optimization results. It determines the minimum, maximum and closed interval image for arbitrary finite dimension, but the inspected theorem and surrounding text do not state a strict qubit parametrization by the single transition probability, uniqueness of every intermediate level modulo phases, or the local quadratic coefficient. Those conclusions do not follow from endpoint extrema plus continuity alone. Targeted Resultary search and comparison with the older Zhang--Fei orbit paper found no stronger result covering the general maximal operator-convex \(f\) qubit profile.

## value

PASS

The source leaves the full unitary orbit between two sharp endpoints. In dimension two, identifying the entire landscape, proving there are no interior repeated levels after the natural phase quotient, and giving the exact local curvature is a natural structural refinement of the same optimization problem. It is not merely a re-evaluation of endpoint values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
