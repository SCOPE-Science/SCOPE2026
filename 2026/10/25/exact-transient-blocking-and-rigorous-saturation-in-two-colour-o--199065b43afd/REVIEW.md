# Independent mathematical audit

## correctness

PASS

For the infinite Z nearest-neighbor antagonistic Poisson adsorption process with independent proposals of each color at rate 1/2 per site and repeated attempts, freezing site 0 separates independent left/right half-line processes. With T the boundary occupation time, before next-site occupation the rate at boundary is 1, after it 1/2, giving Volterra equation h(t)=1−(1/2)∫_0^t e^{−s}h(s)ds, h=e^{t/2}g, and solution g(t)=exp[−t/2−(1−e^{−t})/2]. The weighted occupation M(t)=E[e^{−T/2}1(T≤t)]=(1−e^{−t})exp[−(1−e^{−t})/2]. Opposite cavity colors occur with probability 1/2, and conditional no successful deposition at 0 until both boundaries occupy has probability e^{−(T_+ + T_−)/2}; independence gives B(t)=M(t)²/2. At t→∞, every vacant site must be blocked (if side colors match, an attempt of that color eventually succeeds), so θ∞=1−1/(2e). Expanding around u=1 yields [1/(2e)−B(t)]∼e^{−t}/(2e). Finite-time independent integral/quadrature of cavity Volterra equation agreed at t=.01,.25,.5,1,2,4,8. The infinite graphical construction and monotone limit are justified by summable chronological ancestor-path bounds, not by simulation.

## originality

PASS

The exact repeated-attempt equal-rate model appears in Martins–Dickman–Ziff (2022), but its one-dimensional analysis uses a three-site approximation and simulations and conjectures an exact finite-cycle saturation law. They do not prove the exact all-time blocked-site probability, cavity survival function or sharp relaxation coefficient. The other 2023 one-dimensional paper uses a different single-proposal dynamics and does not imply repeated-attempt kinetics. The previously conjectured value 1−1/(2e) is acknowledged as antecedent, not advertised as newly discovered.

## value

PASS

A natural unresolved kinetic observable in a published antagonistic adsorption model is evaluated exactly at every t, replacing a low-order approximate closure with an analytic infinite-volume law. The cavity decomposition supplies a rigorous proof of a previously numerical saturation constant and the exact leading relaxation rate. This is substantive method and time-resolved probability, not simply reprinting the predicted final density, and creates a benchmark for simulation and closure approximation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
