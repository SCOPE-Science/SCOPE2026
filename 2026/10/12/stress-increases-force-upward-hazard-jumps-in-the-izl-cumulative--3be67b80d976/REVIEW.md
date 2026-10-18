# Independent mathematical audit

## correctness

PASS

Reconstructed exact quantile equation p=(1+x/(2b))e^(−x), b=1+α>1, x=α/Qp(α)>0. Differentiating yields x_b=−x/[b(2b+x−1)]. The logarithmic derivative of quantile hazard is −N/[b(b−1)(2b+x−1)^2], N=4b³+4b²x−2b²+bx²−2b−2x+1. Independent SymPy algebra confirms this identity and N(1,x)=(x+1)^2, ∂_bN(1,x)=x²+8x+6, ∂²_bN=24b+8x−4>0, proving strict sign for all parameters. Equal CDF means equal survival so density shares hazard-jump sign. Numeric before/after hazards at (α1,α2,p)=(1.5,0.7,0.4) are about 0.46481 and 1.11772, corroborative only.

## originality

PASS

The parent step-stress reference introduces CDF-equivalent age and the jump formula; published source abstracts emphasize likelihood and estimation, not the uniform fixed-quantile parameter derivative. The earlier IZL distribution result gives agewise shape and Lambert-W quantiles separately. Best-of-knowledge PASS, recognizing a dynamic publisher page did not expose the full primary body in this run.

## value

PASS

The 2026 step-stress CEM explicitly interprets α1>α2 as higher stress but its displayed boundary difference has no inherent sign from continuity alone; this all-α, all-p theorem supplies the missing physical-direction guarantee despite the agewise upside-down-bathtub hazard. It is a motivated exact model-specific monotonicity law, not a generic scaling or a finite plot.

The dated certificate retains the supplied scientific assessment, sources and limitations.
