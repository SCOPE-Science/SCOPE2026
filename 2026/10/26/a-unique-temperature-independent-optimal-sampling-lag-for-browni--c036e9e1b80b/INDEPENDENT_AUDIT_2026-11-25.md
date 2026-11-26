# Independent mathematical audit

## correctness

PASS

The drift eigenvalues −1±u are negative, and the stationary Lyapunov equations give a−b=Tₓ−Tᵧ and c=u(Tₓ+Tᵧ)/(2(1−u²)), hence the stated positive determinant d. With C=Σ exp(Aᵀt), the cross-entry difference is (Tₓ−Tᵧ)e⁻ᵗsinh(ut) and det C=d e⁻²ᵗ. Pairing the four variables in the two squared wedge terms and their product, then subtracting the mean square, leaves 2d−2C₁₁C₂₂+C₁₂²+C₂₁²=2(d−det C)+(C₁₂−C₂₁)². This makes the squared SNR a strictly increasing function of sinh²(vt)/(e²ᵗ−1), independently of temperatures for the argmax. The sign of its derivative is that of G_v−1 with G_v=v coth(vt)(1−e⁻²ᵗ). The derivative of G_v has the sign of sinh(2vt)−v(e²ᵗ−1)<0 by convexity and sinh(2t)<e²ᵗ−1; endpoints give 2 and v<1. Its partial derivative in v is positive because sinh(2vt)>2vt. The v→0 limit follows by bracketing the level-one root of (1−e⁻²ᵗ)/t; independently evaluating the positive root gives 0.79681213002002004616. The v→1 roots diverge since G₁=1+e⁻²ᵗ; for ε=1−v and q=e⁻²ᵗ*, the exact equation ε=(1+v)qᵛ−vq−vqᵛ⁺¹ bounds q above by 2ε and below by (ε/(1+v))^(1/v) eventually. Thus ε|log q|→0 and the equation divided by q yields q/ε→1. The unnormalized absolute expected Q_t peaks at artanh(v)/v; strict monotonicity of v coth(vt) and the optimum equation give the strict ordering and the two nonzero limiting gaps. Mean L_t=Q_t/t is not the unnormalized signal comparison. When u=0 or the temperatures agree the informative maximum disappears; |u|=1 is not stationary. Analytic replay with a bounded scalar root check; frozen checker read but not executed.

## originality

PASS

The supported distinct result is the unique lag maximizing the single-chord SNR for exact observations, including temperature independence of the argmax, strict coupling monotonicity, and asymptotic laws. The Gaussian moment method and finite-step angular-momentum observable are antecedents; an optimal discretization idea was already raised by Viot et al. Neither that regime nor the inspected nearby exact two-observation quantities gives the asserted optimal lag.

## value

PASS

Prior gyrator fluctuation work raises an intermediate sampling-interval question. For the experimentally interpretable design of one exact stationary position pair, the result supplies the unique best lag, independent of the unknown or varying bath-temperature pair, and a coupling-dependent slowdown near the stability boundary. The nonvanishing gap from the lag maximizing mean wedge explains why larger mean signal need not give better standardized signal. The value is this exact design benchmark, not a claim about the most efficient use of a full experimental time series.

The dated certificate retains the supplied scientific assessment, sources and limitations.
