# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The multinomial mode is Jefferson/D'Hondt apportionment, and rational linear independence excludes all quotient ties. Janson's joint Jefferson seat-excess theorem is exactly a Cesàro weak-limit theorem when the house size is uniform on the initial integers. The deterministic divisor-method bounds make the modal displacement uniformly bounded, so every polynomial moment converges and the polynomial transfer law follows.

The joint transform was checked directly by conditioning on J: given J=j, the exponent is a sum of independent uniform variables with coefficients p·z-z_i. The all-order logarithmic coefficient formula then needs only Janson's one-coordinate marginal law. Multiplication of its centered-uniform moment generating function by the Bernoulli-polynomial exponential generating function simplifies exactly to
\[
e^{np_i z/2}\left(\frac{\sinh(p_i z/2)}{p_i z/2}\right)^{n-2}.
\]
Coefficient extraction gives E B_m(T_i+1)=p_i^m b_{m,n}; the p_i^{-k} weights in c_k then collapse against sum_i p_i=1. This verifies the claimed universality for every fixed k.

The Q2 calculation was independently expanded from the conditional uniform representation. The resulting variance identity
\[
\operatorname{Var}(c_1)=\frac{2A_2+4A_1-5n^2+21n-22}{1440}
\]
combined with Q2=c2+c1^2/2 reproduces the displayed closed form. A direct highest-averages enumeration for the generic three-category example through N=300000 agrees with the predicted means of c1, c2, and Q2 to the expected empirical accuracy. Boundary checks at n=2 also agree with the irrational-binomial Jefferson mode law.

## Originality

**PASS, to the best of our knowledge.** Elezović (arXiv:2609.20229) was inspected in full where relevant. Section 6 deliberately averages a floor reference that is generally not on the multinomial slice and explicitly states that whether those averages survive passage to an on-slice reference such as the actual mode is open. The paper also notes that modal rounding destroys the single-bin structure used in its floor-reference argument.

Janson (arXiv:1110.6369; Annals of Operations Research 2014) was inspected at the theorem level. Theorem 3.7 already gives the joint and marginal limiting Jefferson seat-excess distributions for fixed rationally independent proportions and random large house size. That theorem is essential prior art; this record does not claim the seat-excess law, its mean, or its variance.

Older apportionment literature is a material originality risk. Schwingenschlögl--Drton (2004, 2006) studies seat allocation distributions, biases, and variances, while Heinrich--Pukelsheim--Schwingenschlögl (2005) studies stationary multiplier methods and the limiting Sainte-Laguë divergence. The 2005 paper was inspected in accessible full text; the 2004 and 2006 articles were checked through bibliographic records and abstracts, but their complete texts were not inspected. These works make it plausible that additional polynomial seat-excess moments exist in the literature. However, targeted searches for Bernoulli-polynomial seat-excess identities, the specific hyperbolic-sine generating function, modal multinomial Cesàro coefficients, and the connection between Janson's law and Elezović's expansion did not locate the all-order c_k formula or the Q2 formula reported here.

The originality claim is therefore narrow: the bridge to the multinomial modal expansion, the probability-vector-independent all-order Cesàro means of the logarithmic coefficients, the explicit first non-universal multiplicative coefficient, and the normalized modal-mass consequence. It is not a claim that the underlying apportionment limit law or general moment methods are new.

## Value

**PASS.** The result resolves, under the standard generic arithmetic condition, an on-slice averaging question explicitly left open in the recent multinomial-mode paper. The all-order cancellation is structurally stronger than a first-coefficient calculation and identifies a sharp distinction between logarithmic and multiplicative expansions: universality persists for every c_k but already fails for Q2. The joint transform also turns all polynomial modal averages into finite differentiation or cube integration problems.

## Scientific limitations

The result does not cover rational or arithmetically nongeneric probability vectors, where quotient ties and periodic effects can change the averaging law. It proves Cesàro limits rather than pointwise limits or convergence rates. The explicit multiplicative calculation is carried only through Q2, although the joint transform in principle determines higher orders. Older apportionment literature was not exhaustively checked, and the inaccessible full texts of the 2004 and 2006 seat-allocation papers remain the principal residual originality uncertainty.
