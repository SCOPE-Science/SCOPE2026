# Independent mathematical audit

## correctness

PASS

The exact same-model characteristic transform of Boyer–Majumdar is an explicit prior input. For z near 0, its slow Kummer branch has exponent a_-(z)=λ_-(z)/(r+λ_-(z)) and analytic amplitude c_- (r+λ_-)^{-a_-}/Γ(1-a_-). The second branch has a strictly greater positive real decay exponent near 0, so locally uniform Kummer asymptotics permit four derivatives by Cauchy formula. Writing x=(vz/γ)², expand -a_-(z)=x/(2p)+(2-p)x²/(8p²)+…, and the analytic log-amplitude to x². The fourth derivative yields coefficient 3(2-p)L/p² and constant (15p²−12γ_E p−24−2π²+24γ_E)/(4p²) in v⁴/γ⁴ units. At p=2 this is (18−π²)/8>0; variance is v²/γ²[(L+γ_E)/p−1/2]+o(1), giving the claimed normalized 1/log² law. Independent SymPy expansion checked the fourth coefficient and the residual. No finite-time sign statement or uniform p→2 joint limit is proved.

## originality

PASS

The 2023/24 Boyer–Majumdar primary paper gives the full exact characteristic function and hence implicitly determines every finite-time cumulant; this strong dependence is explicitly credited. Its inspected main results and appendix state variance and logarithmic large-deviation scaling, but not the evaluated fourth-order critical constant. Computing a finite residue after a leading exponent cancellation needs a fourth-order expansion of an analytic prefactor. Broader generic mod-Gaussian/cumulant theory could subsume it. Qualified best-of-knowledge PASS, not claim that the original transform itself is new.

## value

PASS

The exact cancellation of the logarithmic fourth-cumulant growth at an identifiable physical reset/flip rate gives a distinct and measurable log-squared Gaussianization speed and a positive finite part. The prefactor calculation is a motivated finer asymptotic, not a simple restatement of a variance or LDP theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
