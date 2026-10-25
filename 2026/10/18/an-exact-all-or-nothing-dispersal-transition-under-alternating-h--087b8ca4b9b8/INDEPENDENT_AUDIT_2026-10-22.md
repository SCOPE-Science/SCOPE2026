# Independent mathematical audit

## correctness

PASS

With odd/even D1=diag(B,b), D2=diag(b,B) and migration matrix P(d)=[[1-d,cd],[cd,1-d]], the two-season transfer is (J P(d) D1)^2. Its one-season positive square root Perron root equals lambda_max of symmetric [[cdB,sqrt(Bb)(1-d)],[sqrt(Bb)(1-d),cdb]], giving Lambda(d)=[cd(B+b)+sqrt(c^2d^2(B-b)^2+4Bb(1-d)^2)]/2. The radicand is squared Euclidean norm of the affine vector (u*d,v*(1-d)) with u=c(B-b)>0,v=2sqrt(Bb)>0, which is strictly convex on [0,1]; hence every interior d loses to the endpoint chord. Endpoints are sqrt(Bb) and cB, giving exact c*=sqrt(b/B), with just endpoints tied at equality. Differentiating the norm twice gives g=u^2v^2/g^3 and the stated uniform strong-convexity penalty. Independently checked Decimal parameter examples (B,b)=(4,1), c=1/4,1/2,3/4: exact winners d=0,both endpoints,d=1; all sample interiors are inferior. Real-parameter universality rests on analytic strict convexity, not sampled values.

## originality

PASS

Best-of-knowledge statement-level comparison identifies no prior theorem implying the final claim at its actual hypotheses; known overlap and residual bibliographic risks are recorded, not erased.

## value

PASS

The precise migration-cost phase boundary and strict gap distinguish pure strategy switching from intermediate evolutionary optima in a concrete, commonly used alternating source/sink toy model. Complete analytic optimization over a real parameter family can benchmark cost-bearing dispersal models, though it is not an ESS or empirical prediction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
