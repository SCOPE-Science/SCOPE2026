# Independent mathematical audit

## correctness

PASS

The exact source-form ternary rounding gives E Q(g)=g and E||Q(g)||²=||g||∞||g||1, hence E||Q(g)−g||²=M||g||1−||g||². Normalize one |g_i|=M=1; with S=sum other magnitudes and R=sum their squares ≥S²/(d−1), the ratio ≤(1+S)/(1+S²/(d−1)), maximized at S=√d−1 with all other magnitudes 1/(√d+1), giving sharp (√d+1)/2 and variance parameter ω*=(√d−1)/2. d=1 zero variance separately. For f=L||x||²/2 with h=ηL and only source-form TernGrad randomness, worst expected one-step factor exactly 1−2h+[(√d+1)/2]h². Thus descent iff 0<h<4/(√d+1), unique minimax h*=2/(√d+1), factor (√d−1)/(√d+1); h=1 neutral at d9 and adverse for d≥10 on equality direction. Independently checked extremizers numerically for several dimensions; all-dimensional assertion is analytic.

## originality

PASS

The original TernGrad paper fixes this quantizer but does not in its inspected analysis give the global sharp 1/2-improved compressor variance parameter. The later unbiased-compression comparison table explicitly lists sufficient ω=√d−1, not the minimum. This finding optimizes the same model and adds an exact quadratic one-step stability frontier; the earlier sufficient table alone does not imply sharpness.

## value

PASS

Optimal variance constants affect mathematically meaningful compressor guarantees; halving the conventional sufficient parameter and obtaining an attained dimension-dependent descent boundary provide quantitative design insight, even though the one-step quadratic model is deliberately limited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
