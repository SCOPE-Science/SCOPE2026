# Independent mathematical audit

## correctness

PASS

Direct periodic Fourier integration gives the positive product symbol 2Q_b. The sharp worst-horizon ratio is the continuum ratio because as delta tends to zero the same grid delta times the positive integers can approximate both extremizers (including zero by k=1 and infinity by delta*k growing). To enforce the minimum 1/6 requires b at least sup F(s)=1/(6a(s))-1/s². The sinc Taylor bound on (0,pi], the nonpositive-sine lobes, and the decreasing U(s)=s/[6(s−1)]−s⁻² on [4pi,infinity) leave only (2pi,3pi); F(5pi/2) exceeds those exclusions. I checked the derivative numerator N, its positive lower bound until 5pi/2, its strictly negative derivative after 5pi/2 up to 3pi and the endpoint signs. Hence t_* is unique. For b≤b_* the tail Q bound lies strictly below Q_b(pi); for b<b_* every minimizer is beyond 2pi by comparing Q_b(s)/Q_b(t_*), decreasing in b for s<t_*. Comparing a maximizer and minimizer at the larger b proves strict decrease of the extreme ratio up to b_*. For b≥b_* the fixed minimum and strictly increasing maximum give the other side, proving uniqueness. Independent high-precision numerical evaluation (/tmp/opencode/scope-review-analytic.py 4) gave t_*=7.87451945091259722, b_*=0.174777992381291262, peak s≈3.75263938870502440, K≈1.70020056456180867 and 6Q_{1/2}(4)≈4.01355210541606446. I also verified the strict improvement factor without using unvalidated extrema samples: rational Taylor remainder bounds give N(7.87)>0 and b_*≤U(7.87); on [1,6.284] use spacing 1/250, Taylor bounds at the grid points and |Q''|<15 (a=integral_0^1 (1−cos(us)) du) with interpolation error ≤15(1/250)²/8. For s≤1 use a(s)≤s²/6. These give K<1.7005, while 6Q_{1/2}(4)>4.0135, implying the claimed factor >2.36. Frozen checker was inspected, not executed.

## originality

PASS

The retained claim is the sharp periodic continuum minimax over all positive masses and horizons, not the additive preconditioner, the mass-normalized choice, sinc symbol or the existence of uniform bounds. The closest published scalar benchmark and originating analytical preconditioning paper cover different quantifiers or only a fixed parameter.

## value

PASS

The all-horizon comparison is a natural robustness design problem for an existing preconditioner, not an arbitrary slice: the equality at the low-frequency limit and a competing oscillatory lobe selects a distinct unique tuning. A certified >2.36 gap relative to the conventional mass coefficient gives a meaningful continuum benchmark, not merely a tiny numerical improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
