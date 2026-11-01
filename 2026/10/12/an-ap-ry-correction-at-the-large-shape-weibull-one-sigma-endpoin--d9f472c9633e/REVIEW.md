# Independent mathematical audit

## correctness

PASS

With r=1/k and unit scale, write X=e^{rY}, Y=log E, E~Exp(1). The cumulant generating function of Y is logΓ(1+t). Its cubic expansion gives μ=-γ, v=ζ(2)=a² and κ3=-2ζ(3). Hence m_r=1+μr+(μ²+v)r²/2+O(r³), s_r²=vr²+(2μv+κ3)r³+O(r⁴), and s_r=ar+a(μ−ζ(3)/v)r²+O(r³). Thus r^{-1}log(m_r−s_r)=μ−a+(ζ(3)/a)r+O(r²) and r^{-1}log(m_r+s_r)=μ+a−(ζ(3)/a)r+O(r²). Smooth Taylor expansion of F_Y(y)=1−exp(−exp y) at these two endpoints yields C_k=Cinf−A/k+O(k^{-2}), with strictly positive A. Because Cinf exceeds erf(1/sqrt2), eventual recovery above the Gaussian one-sigma benchmark follows. The lower endpoint m_r−s_r is positive for sufficiently small r. No global monotonicity, minimal K or exact finite crossing is claimed.

## originality

PASS

Best-of-knowledge originality PASS for the signed first-order large-shape expansion of the already-named Weibull one-sigma central mass. The 2023/2024 source determines the Gumbel limiting constant and plots the Weibull functional through shape 10 but does not give the large-k signed 1/k coefficient in the arXiv v2 sections read. A directly relevant published small-shape Weibull anti-concentration law is for shape tending to zero, not infinity. Classical log-Gamma and Weibull formulas are ingredients; no checked covering statement for the exact signed coefficient was established.

## value

PASS

The same one-sigma functional previously fails its Gaussian comparison for the non-infinitely-divisible shape k=3 and is evaluated only numerically for shape up to 10. The large-shape boundary is a mathematically natural question: the theorem identifies the reflected-Gumbel endpoint, the positive exact Apéry correction determining its approach from below, and eventual recovery above the Gaussian benchmark. This quantifies a motivated signed endpoint law and gives a precise asymptotic benchmark for subsequent finite-shape investigations; it is not a claim of a global phase diagram or an arbitrary parameter slice. Although elementary Gamma expansions are proof ingredients, the prior source does not specify their combination at the standardized moving one-sigma endpoints.

The dated certificate retains the supplied scientific assessment, sources and limitations.
