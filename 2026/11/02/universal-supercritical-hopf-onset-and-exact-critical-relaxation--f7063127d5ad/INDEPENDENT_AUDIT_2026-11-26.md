# Independent mathematical audit

## correctness

PASS

At both nonzero equilibria the characteristic polynomial is λ³+aλ²+bλ+2b. The Routh first column has all positive entries for a>2 and two sign changes for 0<a<2. At a=2 the factorization (λ+2)(λ²+b) gives one real stable mode and a simple center pair, with crossing derivative real part −b/[2(b+4)]. An independent exact symbolic reconstruction of the quadratic/cubic contraction in the q₁=1 normalization gives Re G=−2(b+1)/(b+4) and Im G=−(4b²+43b+72)/[3√b(b+4)]. The physical-time cubic is G/2, not ℓ₁=Re G/(2√b). The nonzero real cubic and crossing give locally unique stable cycles for δ=2−a>0, with reflection exchanging them. Removing nonresonant terms through degree four in a smooth parameter-dependent center normal form leaves a radial remainder O_b(r⁵); applying the radial equation at cycle extrema gives r²=bδ/[2(b+1)]+O_b(δ²) throughout the cycle. The leading x-amplitude is 2r+O_b(r²); the angular speed combines the linear frequency shift with Im G times r²/2 and has O_b(δ²) error. Its one-turn time gives the stated least-period law. At δ=0 the radial cubic is strictly negative, and (r⁻²)'=2(b+1)/(b+4)+O_b(r²); attraction and integration give the stated t⁻¹/² coefficient. The strong-stable foliation transfers the center asymptotic by exponential tracking, with its equilibrium fiber the one-dimensional exponentially decaying exception. The displayed displacement normalization is for the center coordinate, with an exponentially small extra transverse displacement along tracked trajectories; it does not purport to parametrize the entire three-dimensional neighborhood by u. Nonexponential stability follows also from the nondecaying linear center pair. All estimates fix b>0. Exact-computation replay: python3 /workspace/branches/1fab7724-9433-4d4b-ae41-75c4f7a0d02e/independent_hopf_check.py; recorded independent_hopf_check_output.txt in the same directory. The frozen SymPy script was read, not run.

## originality

PASS

The defining vector field, its equilibria and spectral framework are known. The supported model-specific content is the exact cubic contraction and its strict sign for every fixed b>0, with physical-time frequency/amplitude and critical relaxation constants. The primary model paper's inspected stability and bifurcation sections give samples and finite-parameter dynamics, not those coefficients. The general jerk theorem provides transversality criteria but explicitly requires a separate Lyapunov calculation. The closest indexed exact computations concern different vector fields, including a same-day sine model; no historical priority exclusion is inferred from dates or from a keyword miss.

## value

PASS

The paper introducing this family emphasizes periodic and chaotic behavior; the exact local onset answers a natural missing question about when attracting cycles first bifurcate at the nonzero equilibria. Uniform strict sign across the positive-b parameter range, a physical-time period coefficient, and the quantified critical slowing for all nearby initial conditions off the stable fiber make the result a useful nonnumerical benchmark. This is more than applying a linear stability test or claiming another sample cycle, and it implies neither global dynamics nor security properties.

The dated certificate retains the supplied scientific assessment, sources and limitations.
