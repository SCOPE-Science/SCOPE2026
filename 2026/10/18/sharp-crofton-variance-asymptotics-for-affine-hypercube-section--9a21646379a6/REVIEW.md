# Independent mathematical audit

## correctness

PASS

Under invariant affine-hyperplane measure conditioned on meeting the cube, the correct law is Gaussian width-weighted: E_aff F=(2nmu)^-1 E_G ∫[-L,L]F(G,t)dt, L=Σ|G_i|, mu=sqrt(2/pi). Every section vertex corresponds a.s. to one edge interval; integrating single intervals gives known EV_n=2^(n-1). Summing pairwise overlap lengths yields the exact second moment. Same-direction pairs have probability 1/n and are O(1/n) in overlap. For distinct directions the center difference is Z+σA+τB, with Z|H~N(0,4H) and H~Bin(n-2,1/2). The normalized Gaussian density at bounded offsets tends 1/sqrt(4πn); ∫intersection_length(x)dx=4AB. Chernoff on H<n/4 plus integrable Gaussian density envelope proves sqrt(n)Eoverlap→2mu²/sqrt(pi). Combining prefactors gives Var V_n/(4^n sqrt(n))→1/(2sqrt2 pi) after subtracting the mean square. For typical-to-mean separation, the offset |U|L is order n away from |U|<delta and all random signed edge centers have subgaussian O(sqrt n) tails, yielding V_n/2^(n-1)→0 in probability. Independently derived the coefficient exactly as sqrt(2)/(4pi); no claim that finite simulations prove the asymptotic.

## originality

PASS

Swan proves expectation 2^(n-1) for affine hyperplanes with a different presentation; that known component is explicitly excluded. Lonke studies central Haar sections with zero offset rather than the width-biased affine Crofton measure. Published combinatorial finite cube slicing and central-4-cube face laws cannot determine the stated invariant affine variance scaling. No returned Resultary hit or inspected primary theorem covered the 4^n sqrt(n) asymptotic constant. The distinction is in probability measure, dimension regime and second rather than first moment; a similar title is not sufficient.

## value

PASS

This identifies a natural high-dimensional random section statistic where the classical exact expectation is exponentially larger than the typical count, and quantifies its rare-event dominated variance with sharp constant. The affine Crofton law and normalization are canonical and the finding is a nonroutine stochastic-geometric asymptotic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
