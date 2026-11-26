# Independent mathematical audit

## correctness

PASS

At stationarity the independent Poisson reset age is E/r with E unit exponential. Integration of the zero-state velocity equation and Brownian scaling give the claimed coupling with h(w)=Mr(1−e^(−w/(Mr))) and diffusing orientation U_r(z)=(cos(√(2/r)W_z),sin(√(2/r)W_z)). Independently split the active error into coefficient, orientation and kernel defects. The coefficient defect is bounded by |α_r−α| times the L² norm of E²/2, namely √6. Conditional on E=s, the orientation L² defect is at most α√(2/r)∫₀ˢ(s−z)√z dz=4α√(2/r)s^(5/2)/15; averaging gives 16√15 α/(15√r). Using 0≤w−h(w)≤w²/(2Mr) bounds the active kernel defect by αE³/(6Mr), of norm 2√5 α/(Mr). The two-dimensional thermal Itô isometry gives squared kernel error at most E[E⁵]/(5M²r²)=24/(M²r²). Their sum bounds W₂ for all r>0. Conditioning on the age gives mean αs²e₁/2 and covariance 2s³I₂/3; direct Gaussian mixing gives the stated characteristic function and density (possible divergence at the reset point). With A=E²/2, D=A−1 and v=2E³/3, the factorial identities give E[D³]=74 and E[Dv]=36; conditional centering then gives both third moments and the displayed covariance. Bounds by exponential-age moments give uniform integrability at every fixed order and Lᵖ convergence on the same coupling. For diverging α_r, division by α_r removes the thermal term and gives the strictly positive-magnitude age-square limit, so the original scale escapes in probability. This is a stationary one-time position law for complete resets to a fixed heading, not an assumption of constant orientation between resets or a statement on position-only resetting. The supplied finite checker was read, not run.

## originality

PASS

The supported distinction is the joint inertial high-rate/high-activity planar law with an explicit all-rate W₂ error, not the resetting model, exponential-age construction, known passive scale, or moment formulas. Earlier same-model scalar moments do not determine the law or the error, and the closest inspected indexed result has an equivalent limiting position family but is later and does not give the submitted bound.

## value

PASS

The result distinguishes three physically meaningful scales and gives a quantitative law for the regime where propulsion and thermal fluctuations have comparable size. A scalar second moment does not tell whether the position is Gaussian or whether the orthogonal fluctuation size depends on the longitudinal displacement. The common-age mixture, asymmetric moments and explicit rate supply that information and a finite-rate accuracy benchmark under the specified reset protocol.

The dated certificate retains the supplied scientific assessment, sources and limitations.
