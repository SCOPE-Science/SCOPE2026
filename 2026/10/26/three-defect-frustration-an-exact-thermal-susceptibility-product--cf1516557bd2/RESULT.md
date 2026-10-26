# Three-defect frustration: an exact thermal susceptibility product and optimal spacing on Ising rings

## Finding
Consider the zero-field classical nearest-neighbor Ising ring with exactly three antiferromagnetic bonds, all bond magnitudes equal to \(J>0\). Their cyclic gaps are integers \(a,b,c\ge1\) satisfying \(a+b+c=n\). For every \(0<t=\tanh(\beta J)<1\), the temperature-rescaled magnetic susceptibility \(X_{a,b,c}(t)=\operatorname{Var}(M)/n\) obeys
\[
X_{a,b,c}(t)=B_n(t)-\frac{8t(1-t^a)(1-t^b)(1-t^c)}{n(1-t)^2(1-t^n)},
\quad B_n(t)=1+\frac{2}{n(1-t^n)}\sum_{d=1}^{n-1}(n-2d)t^d.
\]
At every fixed positive finite temperature, defect placement obeys a strict majorization law: making the three gaps more unequal strictly increases \(X\). Thus, up to permutations and ring symmetries, the maximum occurs only at \((1,1,n-2)\), while the minimum occurs only when the gaps differ by at most one. For \(n=3,4\) all feasible placements are symmetry-equivalent; the ordering is nontrivial for \(n\ge5\).

The zero-temperature limit exists and equals
\[
X_{a,b,c}(1)=\frac{n^2+2}{3n}-\frac{8abc}{n^2}.
\]
In particular, when \(3\mid n\), the optimally spaced configuration has \(X_{\min}(1)=n/27+2/(3n)\), whereas clustered defects have \(X_{\max}(1)=n/3-22/(3n)+16/n^2\). Their ratio tends to \(9\) along multiples of three. This is a macroscopic distinction between equally numerous frustrated bonds whose locations alone differ.

## Assumptions and scope
Let \(n\ge3\) be an integer, \(\sigma_i\in\{-1,1\}\) periodic spins, \(M=\sum_{i=0}^{n-1}\sigma_i\), and
\[
H(\sigma)=-J\sum_{i=0}^{n-1}\epsilon_i\sigma_i\sigma_{i+1},\qquad \sigma_n=\sigma_0,\quad J>0.
\]
Exactly three signs \(\epsilon_i\) equal \(-1\), all others \(+1\). The gaps \((a,b,c)\) count edges in the three cyclic arcs joining successive negative bonds, so each is at least one. The Gibbs law is proportional to \(\exp[-\beta H(\sigma)]\). Spin-flip symmetry gives \(\mathbb E M=0\). The observable \(X=\operatorname{Var}(M)/n\) is the usual susceptibility multiplied by temperature (in units with Boltzmann constant one); the result does not optimize the \(\beta\)-weighted physical susceptibility.

## Proof
First, for an arbitrary signed nearest-neighbor ring, let \(P_{ij}\) be the product of bond-sign-weight factors \(\epsilon_k t\) along the directed arc from site \(i\) to site \(j\), and let \(Q_{ij}\) be its complementary-arc product. High-temperature expansion of the two spin traces gives, with no approximation,
\[
\langle\sigma_i\sigma_j\rangle=\frac{P_{ij}+Q_{ij}}{1+\prod_{k=0}^{n-1}(\epsilon_k t)}.
\]
Exactly three negative bonds give total sign \(-1\), hence denominator \(1-t^n\). Apply a sitewise \(\pm1\) gauge transformation so the only negative bond is the closing edge and the physical spins differ from gauged spins by a signature \(q_i\) which is \(+1\) for \(a\) consecutive sites, \(-1\) for the next \(b\) sites, and \(+1\) for the last \(c\) sites. For \(0\le i<j<n\) and \(d=j-i\), the exact two-point correlation becomes
\[
\langle\sigma_i\sigma_j\rangle=q_iq_j\,\frac{t^d-t^{n-d}}{1-t^n}.
\]
Because \(X=1+(2/n)\sum_{i<j}\langle\sigma_i\sigma_j\rangle\), setting every \(q_i=1\) gives \(B_n(t)\): for each \(d\), there are \(n-d\) pairs, and pairing the two geometric sums leaves \(\sum_{d=1}^{n-1}(n-2d)t^d\).

Relative to this baseline, only pairs with \(q_iq_j=-1\) change sign. Those pairs belong to the two interfaces between the central negative block and its positive neighbors. For blocks of lengths \(u,v\) adjacent in the positive orientation and an intervening opposite block of length \(w=n-u-v\), direct summation over the corresponding \(uv\) pairs gives
\[
\sum_{i\in I_u,j\in I_v}(t^{j-i}-t^{n-j+i})
=\frac{t(1-t^u)(1-t^v)(1-t^w)}{(1-t)^2}.
\]
Both relevant interfaces give the same product with \(u,v,w\) a permutation of \(a,b,c\). The flip of each pair-correlation sign multiplies its contribution by \(-2\). Together with the \(2/n\) prefactor, the total correction is exactly \(-8t(1-t^a)(1-t^b)(1-t^c)/[n(1-t)^2(1-t^n)]\), proving the displayed formula.

For fixed \(t\in(0,1)\), the map \(u\mapsto\log(1-t^u)\) has second derivative \(-h^2e^{hu}/(e^{hu}-1)^2<0\), where \(h=-\log t>0\). Therefore the product \(\prod_{u\in\{a,b,c\}}(1-t^u)\) is strictly Schur-concave for triples with fixed sum. As its coefficient in \(X\) is strictly negative, \(X\) is strictly Schur-convex. Integer balancing and anti-balancing yield the unique extremizer types stated above. This does not assert a total order for triples incomparable under majorization.

As \(t\uparrow1\), the correlation \((t^d-t^{n-d})/(1-t^n)\) tends to \((n-2d)/n\), giving \(B_n(1)=(n^2+2)/(3n)\). Moreover \((1-t^a)(1-t^b)(1-t^c)/(1-t)^3\to abc\), while \((1-t)/(1-t^n)\to1/n\). This proves the zero-temperature formula and preserves the strict extremizers because maximizing or minimizing \(abc\) under positive integer fixed-sum constraints has the same extremal types. For \(n=3m\), substitute \((m,m,m)\) and \((1,1,n-2)\) and divide their leading terms to obtain the limiting ratio \(9\).

## Verification
The standalone `verify_three_frustrated_ising.py` performs independent exact rational full-spin Gibbs enumerations for every positive triple summing to \(n=3,\ldots,9\) at \(t\in\{1/5,1/2,4/5\}\), and independently enumerates every zero-temperature ground-state spin configuration. The script checks the finite-temperature formula, the ground-state degeneracy \(2n\), the ground-state susceptibility, and extremizing gap triples. The executed run reported 252 finite-temperature equality checks, 84 zero-temperature checks and seven placement classifications. These finitely many tests are corroboration; the above exact identities and concavity argument establish the arbitrary-size theorem.

## Relationship to prior work
Ismail (2003) studies the Glauber dynamic specific heat and relaxation spectra of six-site Ising rings with random bond energies; its model motivates frustration and response observables but its investigated dynamical quantities and random-magnitude couplings do not give the present arbitrary-size equal-magnitude static susceptibility placement theorem. Turban (2016, first arXiv version May 17) obtains partition functions and correlations of finite Ising chains with homogeneous multispin interactions, but does not classify arbitrary placements of three negative nearest-neighbor bonds. Standard one-dimensional bond-gauge and transfer-matrix identities are acknowledged prerequisites and are not claimed as new. Earlier even-frustration results for exactly two negative bonds give a different positive bond-sign product and do not imply the odd-frustration product law or its three-gap extrema. Searches of relevant literature and research records did not locate a dominating theorem, but cannot rule one out.

## Limitations
Only equal-magnitude nearest-neighbor \(\pm J\) bonds, exactly three negative bonds, zero applied magnetic field, and equilibrium magnetization variance are treated. The placement theorem holds at strictly positive finite temperature and in the zero-temperature limit; at exactly infinite temperature \(t=0\), all placements give \(X=1\). The result makes no statement about unequal bond magnitudes, more defects, dynamics, or physical susceptibility with its additional inverse-temperature factor. Historical originality assessment remains non-exhaustive and there has been no independent scientific review.

## References
1. G. Ismail, "Dynamic specific heat of frustrated Ising spin rings", *Revista Mexicana de Física* **49** (2003), 194–202. https://rmf.smf.mx/ojs/index.php/rmf/article/download/3151/3119/5638
2. L. Turban, "One-dimensional Ising model with multispin interactions", arXiv:1605.05199v1 (May 17, 2016). https://arxiv.org/abs/1605.05199
