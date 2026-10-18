# An exact Bernoulli factor and entropy discontinuity profile for the scaled modulo-tent map

## Finding

The scaled modulo-tent map used in an ideal real-arithmetic threshold-bit generator has an exact product-Bernoulli description, but its threshold output hides a parameter-dependent amount of dynamical entropy. Let \(\mu>2\) and \(\theta=\{\mu/2\}\in(0,1)\), and put \(k=\lfloor\mu/2\rfloor\), so \(\mu=2(k+\theta)\). The full map, initialized by Lebesgue probability on \([0,1]\), is measurably isomorphic (up to null endpoints) to the one-sided independent product of a fair binary shift and a \((k+1)\)-symbol Bernoulli shift with probabilities
\[
\Pr(J=j)=\begin{cases}(k+\theta)^{-1},&0\le j<k,\\ \theta(k+\theta)^{-1},&j=k.\end{cases}
\]
In particular, the paper's threshold bits \(B_n=\mathbf 1_{[1/2,1]}(T_\mu^n X)\), for Lebesgue-uniform \(X\), obey
\[
\Pr(B_0=b_0,\ldots,B_{n-1}=b_{n-1})=2^{-n}
\]
for all integers \(n\ge1\) and all binary words \((b_0,\ldots,b_{n-1})\). Consequently the pushforward law of the infinite threshold-bit process is identical for every admissible parameter: within this stationary uniform-seed model, the parameter is statistically unidentifiable from any finite or infinite bitstream distribution.

The Kolmogorov--Sinai entropy of this invariant probability is
\[
 h_\lambda(T_\mu)=\log\mu-\frac{2\theta}{\mu}\log\theta,
\]
whereas the entropy of the full branch-itinerary shift is \(\log(2k+2)\) and that of the threshold-bit factor is exactly \(\log2\). The strictly positive difference
\[
\Delta(\mu)=\log(2k+2)-\log\mu+\frac{2\theta}{\mu}\log\theta
\]
is the Kullback--Leibler divergence between the hidden radial-label law and the uniform law on \(k+1\) labels; it decreases strictly on each \(2k<\mu<2k+2\), from the one-sided limit \(\log((k+1)/k)\) to zero. At every even parameter \(2k\) with \(k\ge2\), the branch entropy has unequal limits \(\log(2k)\) and \(\log(2k+2)\), while the metric entropy has the same limit \(\log(2k)\) from either side. The original central-branch normalization is undefined at such even parameters; only the one-sided limits are asserted.

## Assumptions and scope

The dynamical system is a real-valued map on \([0,1]\). For \(y=\min\{x,1-x\}\) and \(c=k/\mu\), define, away from finitely many branch endpoints,
\[
T_\mu(x)=\begin{cases}
\{\mu y\},&0\le y<c,\\
\{\mu y\}/\theta,&c\le y\le1/2.
\end{cases}
\]
Here \(\{v\}=v-\lfloor v\rfloor\) is fractional part, \(\mu>2\), and \(0<\theta=\{\mu/2\}<1\). The central region is \([c,1-c]\), equivalent to the normalized central subinterval in the cited map. These hypotheses include odd integral \(\mu\), for which the mathematical map is defined, although the triggering paper's implementation excludes integral parameters. Different conventions at a finite set of cutting points have no bearing on the probability or entropy conclusions.

All probabilities are with respect to Lebesgue-random initial condition and exact real arithmetic. The branch-itinerary entropy is explicitly distinguished from a claim about the ordinary topological entropy of a discontinuous pointwise representative. No cryptographic unpredictability or finite-precision assertion is made.

## Proof

**Complete affine branches.** On each half of the interval there are \(k\) ordinary branches of length \(1/\mu\), indexed by \(j=0,\ldots,k-1\), and one terminal central branch of length \(\theta/\mu\), indexed by \(j=k\). The left intervals are \((j/\mu,(j+1)/\mu)\) for \(j<k\) and \((k/\mu,1/2)\) for \(j=k\); their right counterparts are reflections about \(1/2\). Their images under \(T_\mu\) are each \((0,1)\). On ordinary branches the signed slope has magnitude \(\mu\); on central branches it has magnitude \(\mu/\theta\). There are therefore exactly \(2(k+1)\) full monotone branches.

**Exact invariant measure and cylinders.** For any integrable observable \(\varphi\), affine change of variables on these branches gives
\[
 \int_0^1\varphi(T_\mu(x))\,dx
 =\left(\frac{2k}{\mu}+\frac{2\theta}{\mu}\right)
 \int_0^1\varphi(t)\,dt
 =\int_0^1\varphi(t)\,dt.
\]
Thus normalized Lebesgue measure \(\lambda\) is invariant. Let \(S\in\{0,1\}\) mark left/right and let \(J\in\{0,\ldots,k\}\) mark the branch index. A branch has probability \(1/\mu\) if \(J<k\), and \(\theta/\mu\) if \(J=k\). The inverse affine branch takes any measurable target set to one of these weights times its Lebesgue measure. Inductively the cylinder for any finite sequence of pair labels has probability equal to the product of its branch probabilities. In particular, the pairs \((S_n,J_n)\) are independent and identically distributed.

At each time, \(\Pr(S=0,J=j)=\Pr(S=1,J=j)=1/\mu\) for \(j<k\), or \(\theta/\mu\) for \(j=k\). Since \(\mu=2(k+\theta)\), the law factors into \(\Pr(S=s)=1/2\) and the displayed law for \(J\). Hence the entire sequences \((S_n)\) and \((J_n)\) are independent of each other and i.i.d. in time. The \(S_n\) are precisely the stated threshold bits, up to null ties. Their path-space law is the fair Bernoulli product independently of \(\mu\), proving the stated output-law nonidentifiability for the stationary uniform-seed ensemble.

Every inverse branch contracts by at most \(1/\mu<1/2\), so a nested sequence of affine-cylinder intervals has diameter at most \(\mu^{-n}\). Consequently the full branch coding separates points except for the null set of branch-boundary preimages. It is thus a measure-theoretic isomorphism to the indicated one-sided product Bernoulli shift, not merely a factor assertion.

**Entropies and one-sided limits.** Because the branch partition is generating, its Bernoulli Shannon entropy equals the metric entropy:
\[
 h_\lambda(T_\mu)
 =-\frac{2k}{\mu}\log\frac1\mu
   -\frac{2\theta}{\mu}\log\frac\theta\mu
 =\log\mu-\frac{2\theta}{\mu}\log\theta.
\]
Its full sequence of branch itineraries has every word on \(2k+2\) labels admissible, so the associated full symbolic shift has entropy \(\log(2k+2)\). The binary shift factor has entropy \(\log2\). Differentiating within a fixed \(k\)-strip gives
\[
\frac{d}{d\theta}h_\lambda(T_\mu)
 =\frac{k\log(1/\theta)}{(k+\theta)^2}>0.
\]
The branch entropy is constant on that strip; hence the gap decreases strictly. Because the joint-label distribution factors, the difference \(\Delta=\log(k+1)-H(J)=D(\Pr(J=\cdot)\|\operatorname{Uniform}_{k+1})\) is positive for every \(0<\theta<1\): its radial distribution is not uniform. Using \(\theta\log\theta\to0\) as \(\theta\downarrow0\), and \(\log\theta\to0\) as \(\theta\uparrow1\), gives the claimed limits. On approaching an even parameter \(2k\) from below, one uses the preceding strip indexed by \(k-1\); from above, the strip indexed by \(k\). This proves continuity of the one-sided metric-entropy limits and the stated branch-symbolic jump.

## Verification

The standalone exact-rational checker `verification/check_rctm.py` constructs every affine inverse branch from the parameter, compares inverse images against the source's modulo/scaling map at interior rational test points, and enumerates all branch-label cylinders through specified finite lengths. It verifies that each binary word has measure \(2^{-n}\) exactly, without floating-point probability arithmetic. It passed 4,004 exact-rational branch-word contributions, 156 exact inverse-map identities, and numerical consistency checks for the entropy inequalities across seven rational parameters. The general theorem uses the analytical inverse-branch induction, not the finite checks.

## Relationship to prior work

The modulo/scaling map, its enlarged parameter region, and qualitative uniform orbit-distribution behavior belong to Khan and Jeoti (2015), extending an earlier 2013 conference study. The threshold-bit construction and its numerical NIST/ENT/TestU01 tests belong to Irfan and Khan (2024). Neither accessible full primary account states the exact independent product decomposition, the complete finite-bit cylinder law, or the stripwise metric-versus-branch entropy discontinuity profile in the form proved here. The proof uses the classical fact that a generating full-branch affine partition has independent labels; it does not claim that general principle as new. This is a specific exact dynamical analysis of the published construction, not a claim that it is cryptographically secure.

## Limitations

The conclusion describes a probability distribution over an ideal continuum of uniformly chosen seeds; it is not a randomness theorem for any single prescribed seed. Finite precision, parameter truncation, pseudorandom initialization, key-size accounting, computational indistinguishability, and adversarial unpredictability are not covered. The normalization is undefined when \(\mu\) is an even integer. The 2013 conference predecessor's full text was not obtained, and an equivalent prior parameter-specific derivation could remain undiscovered. General full-branch Bernoulli theory underlies the argument; the claimed contribution is its exact model-specific factorization and parameter singularity.

## References

1. M. Irfan and M. A. Khan, *Cryptographically Secure Pseudo-Random Number Generation (CS-PRNG) Design using Robust Chaotic Tent Map (RCTM)*, arXiv:2408.05580, version 1 publicly posted 2024-08-10; especially Sections III--V and Algorithms 1--2. https://arxiv.org/abs/2408.05580
2. M. A. Khan and V. Jeoti, *On the Enlargement of Robust Region of Chaotic Tent Map for the Use in Key Based Substitution-Box (S-Box)*, Journal of Computer Science 11 (2015), 517--525, DOI:10.3844/jcssp.2015.517.525; especially the complete map equations and discussions on pp. 518--524. https://thescipub.com/pdf/jcssp.2015.517.525.pdf
3. M. A. Khan and V. Jeoti, *Modified chaotic tent map with improved robust region*, conference paper (2013), DOI:10.1109/MICC.2013.6805880. Full text not inspected.
