# Independent mathematical audit

## correctness

PASS

The Paley–Wiener model carries T_b to A_b f(s)=a^-1 exp(-bs/a)f(s/a) on L2(p_n ds), with p_n=sum_{j<=n}s^{2j}. Change of variables gives norm^2=a^-m sup exp(-2bs(1-a^-m)/(a-1))p_n(s)/p_n(a^-m s). At b=0, upper/inverse radii are a^{n-1/2} and a^-1/2; adjoint eigenfamily g=t^gamma/p_n(t) for -1/2<Re gamma<n-1/2, multiplied by log-periodic independent functions, fills infinite-multiplicity essential annulus. At b>0, f=t^gamma exp(-bt/(a-1)) (Re gamma>-1/2) fills punctured essential disk; bounded powers give radius a^-1/2. Tail uniformity validates sup-limit K, and K=1 iff b>=(a-1)/2 max_{s>0}log p_n(s)/s. Small-b Laplace scaling gives (n(a-1)/(e b))^n, and exact norm nonconvergence follows as s->infty. Independently optimized b_* for (n,a)=(1,2),(3,1.7), finding K(b*/2)>1 and K(b*),K(2b*)=1. These finite tests do not prove spectral statements.

## originality

PASS

Liang–Li–Qian 2026 Theorem 4.1 provides the underlying polynomial Fourier weight, while their inspected Section 5 studies multiplier spectra and weighted-composition boundedness, not this T_b full Fredholm spectrum and sharp K threshold. Chalendar–Partington 2023 Section 3.3 has a qualitatively analogous annulus/disk phenomenon for Hardy–Bergman intersection using a *decreasing* Laplace weight 1+1/t; its actual norm/radii differ and do not imply the Sobolev growth exponent n or b_*. General Zen-space spectral method is credited, but its admissible measure-generated weights are not this strictly increasing polynomial. Semantic Resultary query returned no matching theorem among inspected hits. Broad generalized weighted shifts may imply some parts, remaining a residual risk.

## value

PASS

A natural operator on derivative Hardy–Sobolev spaces displays a dimension/order-dependent annulus collapsed by arbitrarily small positive vertical translation, with a sharp quantified power threshold and singular amplification. These are structural spectral and quantitative phenomena, not mere renamings; the method is motivated by the same-family Fourier representation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
