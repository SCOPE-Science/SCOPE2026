# Independent mathematical audit

## correctness

PASS

For the row generator the zero row sums give the stationary root, the negative trace is a+b+c+h, and the three principal 2×2 minors are ab, ac, and (b+h)c. Setting x=h+a+b−c gives the quadratic discriminant x²−4ab, so the complex band is (h_−,h_+) intersected with h≥0. It is nonempty exactly at c>c_0 and has a strictly positive onset exactly at c>(sqrt(a)+sqrt(b))². At equality in the latter condition there is a defective point at h=0 rather than a nonempty initial real phase. At a nonnegative double root λ<0, semisimplicity would imply Q=λ(I−1π), contradicting Q_02=0 and π_2>0. Flux balance sets bπ_1=cπ_2=aπ_0−hπ_1; normalizing yields J=abc/[ab+ac+c(b+h)] with strictly negative derivative. On the band ρ²=(4ab−x²)/(x+2c)² has derivative −4(cx+2ab)/(x+2c)³. Its only turning point is h_*=c−a−b−2ab/c. When positive, c>c_1>sqrt(ab) puts it strictly inside the band and substitution yields ρ²=ab/(c²−ab). When c_0<c≤c_1, h=0 lies in the band and is the unique maximum, including the stationary-derivative case at c=c_1; at c≤c_0 the zero-extension is identically zero. Starting at state 0 the complex transient has a nonzero cosine coefficient 1−π_0, hence infinitely many sign crossings, whereas an exponential times a constant plus one exponential or a linear term has at most one. The supplied verify_cycle.py and its verification notes report algebra and sampled checks; no supplied script was executed. The independent algebra covers boundary cases that sampling cannot certify.

## originality

PASS

Against the accessible comparisons, the supported distinct result is the fixed-forward, one-reverse-rate spectral phase diagram and sharp coherence optimization with steadily falling current. Neither ordinary three-state eigenvalue formulas nor the existence of oscillations in Markov cycles is credited as new. Close inaccessible literature limits priority claims but does not negate the statement-level distinctions established in the inspected materials.

## value

PASS

A controlled change to the single backtracking rate makes this a natural minimal test of whether steady circulation predicts the visibility of damped population oscillations. It demonstrates rigorously that coherence can first increase from zero and then disappear while steady current falls strictly. The full boundaries and optimizer quantify the distinction across all forward-rate choices; the result does not invoke thermodynamic constraints or claim sustained oscillation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
