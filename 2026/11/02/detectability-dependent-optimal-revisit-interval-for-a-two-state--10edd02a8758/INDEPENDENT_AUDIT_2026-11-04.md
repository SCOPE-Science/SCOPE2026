# Independent mathematical audit

## correctness

PASS

For two detections P(11),P(10),P(01),P(00)=(a²+c,a(1−a)−c,a(1−a)−c,(1−a)²+c) with a=pq,c=p²q(1−q) exp(-γΔ), compute Fisher J_{qq},J_{qr},J_{rr}; at q=1/2 Schur complement is exactly p²/[(2-p)²+4(1-p)²r−p²r²]. Chain-rule derivative dr/dγ=−Δr yields formula. For x=γΔ the log-score has sign opposite g=x(2A+Br)−2(A+Br−Cr²), A=(2-p)²,B=4(1-p)²,C=p². Prove g<0 through log2, g strictly increases beyond log2 and tends positive; score therefore has one global maximizer. Differentiating score w.r.t p gives strict negative at all maximizing roots (r<1/2), hence x*(p) decreases. Substitute x=1 gives threshold p_c. Independently recomputed exact symbolic Schur complement and threshold 0.6998478812491185 from multinomial cells; checked actual source check.py, no finite test claimed to prove all-p uniqueness.

## originality

PASS

Best-of-knowledge originality survives the actual implication comparisons; cited antecedents cover the foundations or narrower/different objects but none of the accessible material establishes this exact completed statement. Uninspected plausible literature is explicitly treated as residual priority risk, not a proven absence.

## value

PASS

Imperfect detection materially changes optimal temporal design. Explicit nuisance-adjusted Fisher information, all-p monotonicity, and exact one-switching-time crossover are natural and actionable mathematical distinctions beyond the known perfect-detection endpoint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
