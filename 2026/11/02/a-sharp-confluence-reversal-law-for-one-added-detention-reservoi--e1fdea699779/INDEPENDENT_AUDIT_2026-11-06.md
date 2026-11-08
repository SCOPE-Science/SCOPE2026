# Independent mathematical audit

## correctness

PASS

Non-dimensionalize by x=at and r=b/a. Convolution of the original exponential with the serial exponential yields g_r(x)=r(exp(-x)-exp(-rx))/(r-1), with g_1(x)=x exp(-x). The original peak is beta+exp(-delta), since beta>=1. The derivative of e^x times post-arrival discharge has strictly negative derivative -r^2 exp(-(r-1)x), forcing a single post-arrival peak or an endpoint maximizer. The routed pulse g_r reaches its mode at m(r)=log r/(r-1), and g_r(delta)-exp(-delta) has the sign of delta-m. Below m, the envelope for the modified peak minus original is strictly increasing to zero, including interior-peak regime; above m both modified summands decrease from arrival, so the comparison is exact. Differentiating the excess proves unique maximum at delta=2m; writing r=exp(2u) yields 2u coth(u)>=2 with equality u=0. Independently evaluated the exact derivative and peak for bounded r,beta,delta cases. Model explicitly excludes wider rainfall and hydraulic effects.

## originality

PASS

Hydraulic literature already recognizes that delaying one tributary may increase or decrease the downstream peak, so the qualitative paradox is prior. Pattison et al. study flood simulations and sensitivity of multi-tributary timing; the narrower analytical statement adds a universal exact modal-time sign threshold, beta-independence, and sharp penalty a/e² for one added serial linear reservoir. McCuen and Błażejewski are plausible but partly unread predecessors, retained as risks.

## value

PASS

Simple linear routing is an interpretable benchmark for detention/timing design: the exact safe/harmful boundary and rigorous maximum penalty are directly useful calibration and structural facts, despite not predicting empirical flood stage. The all-rate sharpness is not mechanically supplied by the qualitative flood examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
