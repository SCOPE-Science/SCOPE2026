# Independent mathematical audit

## correctness

PASS

With x=cos(theta), the height difference factors as (1−x)[−1+2a(1+x)+b(2x+1)²]. The coefficient vector is nonnegative on the entire cycle, so the Euclidean support-function maximum is exactly F_E(x)=E G(x)−(1−x). Independently, for x=−u, 0≤u≤1, the components whose norm is G(−u) are 2(1−u²) and (1+u)(1−2u)²=1−3u+4u³. Up to u=√3/2 the latter is at most 1 and the former at most 2; above that point they are bounded by 2 and 1/2 respectively in the opposite order. Thus G(−u)≤√5 and F_E(−u)≤F_E(0). Polynomial differentiation gives R G'=3+4x−8x²−48x³−48x⁴ and −R³ G''/4 with ascending coefficients 1,33,264,816,1392,1584,1152,384. On [0,1] this proves strict concavity for E>0, and F_E'(0)>0 while F_E'(1)=1−E√97. The cases E=0 and E=1/√97 yield zero excess, with every allocation optimal in excess value, not a unique allocation. Above threshold there is a unique interior x_E; equality in the Euclidean norm bound forces the stated positive allocation and exactly two phases modulo the cycle. Positive excess requires 4a+9b>1, hence positive central curvature. The relation G'(x_E)=−1/E and strict concavity give strict decrease in x_E and the unique quartic limit (independent numerical check: 0.371708101121). As E approaches onset the amplitude direction tends to (4,9)/√97. The frozen symbolic/grid script was inspected but not executed; the result does not rely on its grids.

## originality

PASS

The distinct claim is the full-period, fixed squared-amplitude frontier with a unique mixed optimizer and monotone separation above onset. Individual harmonic thresholds, previously observed cooperation of harmonics, and the Euclidean norm reduction alone are not original here. The inspected primary and indexed results do not supply the complete constrained frontier or a stronger theorem implying it. The closest combined-overtide primary source could not be read in full independently, so this distinction is bounded by the obtained evidence.

## value

PASS

Rather than just identifying a local curvature threshold, this solves the full-cycle allocation problem and rules out a competing, remote high-water maximum. It gives a unique allocation above onset and a monotone crest-spacing prediction through the whole mathematical energy range. That is useful as a sharp benchmark within the phase-locked harmonic model, not a claim about real tidal forcing or attainable ocean energies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
