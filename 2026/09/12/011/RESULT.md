# Refutation of the 8% binomial-versus-Gaussian Fourier envelope at ML-KEM-768

## Context

Dual-distinguishing analyses of lattice key encapsulation routinely compute
advantage exponents under an idealized Gaussian error heuristic, while the
deployed CRYSTALS-Kyber / ML-KEM samples errors from a centered binomial law.
The admitted target asked for a proved quantitative transfer: that replacing
the idealized rounded Gaussian by the deployed Kyber eta=2 centered binomial
changes the modular characteristic-function (Fourier) factor by at most 8%,
uniformly over the distinguishing-relevant dual-frequency range at q=3329 for
ML-KEM-768. Admission preflight pinned the exact error law and variance,
confirmed the range reaches the moderate-frequency regime where second-order
and tail terms matter, and ruled out type, vacuity, and first-coefficient
trivial defeats, so both a proof and a rigorous disproof were audit-worthy.

## Definitions

Let q=3329. Let B be the Kyber eta=2 centered-binomial law:
P(B=k)=binomial(4,k+2)/16 for k in {-2,-1,0,1,2}, i.e. weights
(1,4,6,4,1)/16, with E[B]=0 and Var(B)=1.
Let Z~N(0,1) and R_s=round(s Z) be the rounded Gaussian with scale s>0,
P(R_s=k)=Phi((k+1/2)/s)-Phi((k-1/2)/s), V(s)=E[R_s^2].
Let s* be the unique variance-matched parameter with V(s*)=1.
Put phi_B(t)=E[exp(2 pi i t B/q)] and phi_G(t)=E[exp(2 pi i t R_{s*}/q)].
The target envelope asserted |phi_B(t)/phi_G(t)-1|<=0.08 uniformly for scaled
dual arguments in [0,T_768] with T_768=768.

## Result

The 8% uniform envelope is FALSE. At the in-range frequency t=768,

  phi_B(768)/phi_G(768) < 0.92,  |phi_B/phi_G - 1| > 0.08,

with certified ratio below 0.9059 (float true value approximately 0.8996,
i.e. deviation approximately -0.1004). Hence uniformity over [0,768] fails.
The float cross-check locates violation onset near t approximately 727
(-0.086 at 740, -0.091 at 750, -0.096 at 760). The continuous-Gaussian
reading with sigma^2=1 is violated too (-0.1018 at 768).

## Proof / evidence

Closed form: B=X_1+X_2 with X_j in {-1,0,1} of law (1/4,1/2,1/4), so
phi_{X_j}(t)=(1+cos(2 pi t/q))/2=cos^2(pi t/q) and phi_B(t)=cos^4(pi t/q),
Var(B)=2*1/2=1. For the rounded Gaussian,
phi_{G,s}(t)=sum_k P(R_s=k) cos(2 pi t k/q) by symmetry.

Variance bracket: V is continuous and strictly increasing on (0,infinity) by
the layer-cake identity V(s)=sum_{m>=1}(2m-1) 2(1-Phi((m-1/2)/s)) with
strictly positive normal density, uniform tails on compact s-intervals via
Mills-ratio domination (dominated convergence with round(x)^2<=2x^2+1/2 also
gives continuity). With truncation K=6 the exact-rational script certifies
V(0.955)<=0.99536<1 and V(0.96)>=1.00493>1, the upper bound adding the
certified second-moment tail E[R^2 1_{|R|>K}], the lower bound dropping it.
Hence the unique s* lies in (0.955,0.96), with s1=191/200, s2=24/25.

Binomial upper bound: X=768 pi/3329; certified Machin-Leibniz pi enclosure
pi in [3.1415926535,3.1415926536] gives X in an interval inside (0,1) where
cos decreases, so cos(X)<=cos(X_lo); the alternating Taylor even sum S_10 at
x_c=X_lo plus next-term magnitude gives phi_B(768)<=B^U=0.3141429023.

Gaussian uniform lower bound: for each |k|<=6 bound P(R_s=k) uniformly over
[s1,s2] via monotone Phi enclosures, and cos(2 pi 768 k/q) via a certified
cosine-interval routine (midpoint Taylor plus Lipschitz and Leibniz
remainders); the bilinear product minimum over each rectangle is a corner
value; summing corner minima and subtracting the Mills-ratio tail
P(|R_{s2}|>6) with cos>=-1 gives phi_{G,s}(768)>=G^L=0.3467821448 for all
s in [s1,s2]. Primitives proved from scratch: arctan Leibniz remainder with
verified term decrease, decreasing g(k)=(2k+1)/((2k+2)(2k+3)), integrated
T-series normal CDF with Leibniz bound, Mills ratio 1-Phi(y)<=phi(y)/y,
and E[Z^2 1_{Z>y}]=y phi(y)+(1-Phi(y)) transferred to R_s.

Violation: exact Fraction check 100*B^U<92*G^L (31.41429<31.90395), i.e.
B^U/G^L<0.9059<0.92, so phi_B(768)/phi_G(768)<0.92 and |ratio-1|>0.094>0.08.

## Limitations

The certificate refutes uniformity via one in-range frequency (t=768); it
does not supply a full violation map over all frequencies nor a corrected
tight envelope constant, which would need further remainder-controlled
analysis. It treats the one-dimensional modular characteristic-function
ratio for the variance-matched rounded Gaussian, not a full dual-advantage
exponent with lattice summation.

## Reproducibility

Run `python3 output/artifacts/verify_counterexample.py` (stdlib only, exact
Fraction verified path). It prints the variance bracket, the two one-sided
bounds, the exact 100*B^U<92*G^L check with CERTIFIED line, then a labeled
float cross-check. Interval widths are ~1e-10 against a violation margin
~1e-2. No floats enter the verified path.

## References

- NIST FIPS 203 / CRYSTALS-Kyber specification and supporting documentation
  (eta=2 centered-binomial choice, heuristic Gaussian closeness, q=3329).
- pq-crystals Kyber centered-binomial-distribution documentation.
- NewHope supporting analysis Appendix B and Bai-Galbraith et al. on concrete
  LWE hardness (Renyi-divergence comparisons of error laws, a distinct global
  measure not implying the pointwise envelope).
- Cryptography StackExchange discussions on centred binomial versus
  discretised Gaussian security effects.
