# Independent mathematical audit

## correctness

PASS

The exact four affine branches induce the stated depth/side kernel on dyadic cells for absolutely continuous shell-cell-constant laws: tau2 flips side and adds 2; tau1 subtracts 1 for k>=1 and from k=0 sends uniform mass to a geometric 2^{-j-1} same-side reset. For p>2/3 the stationary recurrence w_k=p w_{k+1}+q 1_{k>=2}w_{k-2}+p w0 2^{-k-1} yields W_p(z)=(3p-2)/((2-z)(p-qz-qz²)), W(1)=1, w0=(3p-2)/(2p)>0 and W'(1)=1/(3p-2). Factor positivity and irreducible side/depth Markov chain prove existence and uniqueness within the stated shell-cell-constant class; no global uniqueness claim is inferred. Positive quadratic pole r solves q(r²+r)=p and simple-pole asymptotics show density power divergence for p in (2/3,6/7), a p=6/7 double pole gives w_k=(k/5+7/25)2^{-k}+(4/75)(-1/3)^k and density 2k/5+14/25+(8/75)(-2/3)^k, and p>6/7 gives limiting density (3p-2)/(7p-6). At critical approach epsilon=3p-2, W(exp(-epsilon t)) tends to 1/(1+t), giving the mean-one exponential limit. For p<2/3, K_n is bounded below by a +2/-1 i.i.d. walk with drift 2-3p>0; hence eventual positive depth, finitely many k=0 resets and strong-law K_n/n=2-3p a.s., giving exponential endpoint proximity. The side flips on infinitely many tau2 selections so no individual endpoint trajectory convergence; annealed spatial weak convergence to half delta0+half delta1 follows from symmetric parity mixing. Invariant AC probabilities cannot converge weakly to singular endpoint mixture, hence no such interior stationary law for p<2/3. Branch boundaries and p=2/3 are properly excluded or ascribed to prior critical work. The independent symbolic/rational checker verified 1032 stationarity equations, 130 p=6/7 coefficients, 920 affine rational itineraries, 90-digit pole checks and 12 finite Laplace evaluations. Those checks corroborate, not prove, the all-p analysis. Exact frozen tree reconstructed from 7 Git blobs.

## originality

PASS

Best-of-knowledge comparison of mathematical statements: the exact same mBGI map and shell transitions and critical p=2/3 infinite invariant law are due to Hata–Yano; the present complete off-critical stationary depth generating function, the distinct p=6/7 boundedness/logarithmic threshold, the critical-approach Exp(1) scaling and the p<2/3 escape speed are not included in their inspected theorem or Section 4. Other primary articles give parallel phenomena for a different one-ended Pelikan map or under critical-intermittency assumptions not met by these branches. The older Boyarsky–Góra–Islam primary full text was inaccessible due to an authorized institutional VPN disconnect; its content remains a named historical-priority risk and was not treated as a blanket originality failure. No source-independent absolute novelty certificate is claimed.

## value

PASS

The critical mBGI model is a natural random-interval-map example from Hata–Yano, with two distinct attracting endpoints and a Markov shell structure. The parameter-wide exact stationary PGF, normalization boundary p=2/3, independent bounded-density boundary p=6/7, logarithmic crossover, critical-approach exponential scaling, and complementary almost-sure escape rate answer motivated ergodic and density-regularity questions and make the family quantitatively tractable. This is not a named-constant substitution, arbitrary finite slice, or known-table recomputation. The narrower class-uniqueness limitation and exclusion of full quenched convergence are recognized; no broader classification or global AC uniqueness is advertised.

The dated certificate retains the supplied scientific assessment, sources and limitations.
