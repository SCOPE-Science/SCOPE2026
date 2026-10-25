# Independent mathematical audit

## correctness

PASS

Four RK4 stage derivatives of diag(w1 J,w2 J), 0<w1<w2, have determinant (h^6/32)*w1^3*w2^3*(w2^2-w1^2)^2||z1||^2||z2||^2; nonzero on full-excitation open set. Thus one-invariant quasi-orthogonal projection becomes radial normalization z+=(||z||/||R(hA)z||)R(hA)z. Q(x)=|R(ix)|^2=1+x^6(x^2-8)/576>0 gives exact modal action ratio E2(n)/E1(n)=(E2(0)/E1(0))*(Q(w2 h)/Q(w1 h))^n. Difference Q2-Q1 is an h^6 positive factor times h²-h*² with h*²=8(w2^6-w1^6)/(w2^8-w1^8). For unequal Q modes, action-angle Jacobian determinant at equal actions equals 4Q1Q2/(Q1+Q2)^2<1 and map cannot be symplectic; at equal Q it is a constant block rotation and symplectic. The switch lies strictly below h²=8/w2²; independently simplified the exact symbolic factor and evaluated w1=1,w2=2 to h*²=168/85. No finite check extrapolated to arbitrary timesteps.

## originality

PASS

Najafian–Vermeire 2024 introduced quasi-orthogonal RK projection and explicitly observed stage-space saturation reduction to normal projection. Jiang–Gong–Wang 2020 earlier normalized energy projection, so neither the radial correction nor total-energy preservation is novel. However inspected methods do not imply a two-frequency exact h* where projected classical RK4 is symplectic iff, nor the all-n energy-ratio asymptotic phase reversal. Distinct projected oscillator methods may carry equivalent amplification analysis; risk noted.

## value

PASS

Energy-conserving numerical integration can strongly misrepresent distribution of separate physical actions. The exact two-mode linear benchmark identifies an interior RK4-stability window where all energy eventually concentrates into one mode, and a single positive timestep where projected RK4 unexpectedly recovers both actions and symplecticity. This precise reliability boundary is a motivated test for conserving schemes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
