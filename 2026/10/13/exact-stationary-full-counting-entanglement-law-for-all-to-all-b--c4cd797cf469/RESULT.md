# Exact stationary full-counting entanglement law for all-to-all Bell measurements

## Finding

Consider \(n\ge2\) qubits subjected at each step to a computational-basis measurement at a uniformly random site with probability \(0<p<1\), or a Bell-basis measurement of a uniformly random unordered pair with probability \(1-p\). Suppose the initial state is a product state in the computational basis. The measurement outcomes never influence the pairing pattern: the trajectory stays a tensor product of Bell states and unpaired computational-basis states [1].

Write \(z=(1-p)/(p(n-1))\). For \(m\ge0\), define the matching partition function
\[
Z_m(z)=\sum_{r=0}^{\lfloor m/2\rfloor} \frac{m!}{(m-2r)!\,2^r r!}z^r.
\]
For any matching \(M\) of the complete graph on \(n\) labeled vertices, its unique stationary probability is exactly
\[
\pi_n(M)=\frac{z^{|M|}}{Z_n(z)}.
\]
Fix a subset \(A\) of size \(k\) and let \(l=n-k\). Let \(C\) count Bell pairs crossing from \(A\) to its complement. Every Rényi entropy (including the von Neumann entropy) of the pure quantum trajectory, measured in bits, equals \(C\). Its exact finite-size probability-generating function is
\[
G_{n,k}(t)=\mathbb E[t^C]=\frac{1}{Z_n(z)}\sum_{j=0}^{\min(k,l)}\binom{k}{j}\binom{l}{j}j!\,(zt)^j Z_{k-j}(z)Z_{l-j}(z).
\]
For \(n\ge2\), set \(r_1=zZ_{n-2}(z)/Z_n(z)\); for \(n\ge4\), set \(r_2=z^2Z_{n-4}(z)/Z_n(z)\), and otherwise \(r_2=0\). Then
\[
\mathbb E[C]=klr_1,\qquad
\operatorname{Var}(C)=klr_1+k(k-1)l(l-1)r_2-(klr_1)^2.
\]
In addition to these exact finite-size results, there is an explicit thermodynamic variance. If \(p\in(0,1)\) is fixed and integers \(k_n\) satisfy \(k_n/n\to a\in(0,1)\), write \(u\in(0,1)\) for the unique solution of \(\frac{1-p}{p}u^2=1-u\) and \(A_0=a(1-a)\). Then
\[
\lim_{n\to\infty}\frac{\mathbb E[C]}{n}=A_0(1-u),
\]
\[
\boxed{\lim_{n\to\infty}\frac{\operatorname{Var}(C)}{n}=
A_0(1-u)\bigl[u+2A_0(1-2u)\bigr]
+A_0^2\frac{2u(1-u)}{2-u}.}
\]
The second summand isolates fluctuations in the total number of monomer (unpaired) sites. For \(p=2/5\) and a cut fraction \(a=2/5\), the variance limit is approximately \(0.0740358330350\) per qubit.

## Assumptions and scope

The quantum dynamics is the all-to-all case of [1]: every unordered pair is sampled with equal probability, every site is sampled with equal probability, measurements are projective, and the stated sampling probabilities are held fixed as \(n\) grows. Both sampling operations can include null updates when the sampled sites are already compatible with the measurement. No postselection or assumption on Bell outcomes is needed. Results apply to any fixed bipartition and all integer sizes \(n\ge2\); the displayed thermodynamic limit requires fixed strictly interior \(p\) and asymptotic cut fraction \(0<a<1\). This theorem is about entanglement of individual pure conditional trajectories, not the entropy of an outcome-averaged density operator.

## Proof

**1. Unique reversible matching equilibrium.** Encode each Bell pair as an unordered edge and each unpaired qubit as a monomer. A computational-basis measurement on either end of an edge removes it; a Bell measurement of two monomers inserts their edge; a Bell measurement of a monomer and a paired site moves one endpoint; a Bell measurement of sites in distinct edges reconnects both edges. These update rules are obtained from Bell-basis projection identities in [1, main text and Supplemental Material I]. For a specified edge insertion, the forward transition probability is \((1-p)/\binom{n}{2}\), while deletion by either endpoint has probability \(2p/n\); their ratio is exactly \(z\). Endpoint sliding and two-edge reconnection have equal reverse and forward total probabilities because the same number of unordered measured pairs implement both directions (one and two, respectively). Hence \(z^{|M|}\) satisfies detailed balance for every off-diagonal transition. Since \(p>0\) deletes every edge and \(1-p>0\) inserts any chosen edge, all matchings communicate through the empty matching. Finiteness gives a unique stationary distribution, normalized by \(Z_n(z)\). The coefficient in \(Z_n\) counts ways of selecting and pairing \(2r\) of the \(n\) labeled sites.

**2. Full entropy distribution.** A matching with exactly \(j\) crossing edges chooses \(j\) endpoints in \(A\) and \(j\) outside, pairs them bijectively in \(j!\) ways, and independently chooses internal matchings on the remaining \(k-j\) and \(l-j\) sites. The crossed edges contribute \(z^j\) and internal choices contribute \(Z_{k-j}(z)Z_{l-j}(z)\). Divide by \(Z_n(z)\) and mark each crossing edge by \(t\) to obtain \(G_{n,k}(t)\). Each cross-cut Bell pair gives one maximally mixed qubit in the reduced state, while wholly contained Bell pairs and unpaired sites contribute pure tensor factors. Thus the reduced density matrix has exactly \(2^C\) identical nonzero eigenvalues \(2^{-C}\), proving the asserted Rényi entropy identity. Differentiating the generating function, or counting the chance of one or two specified disjoint edges, gives \(\mathbb EC=klr_1\), \(\mathbb E[C(C-1)]=k(k-1)l(l-1)r_2\), hence the exact variance.

**3. Thermodynamic fluctuations.** Let \(m\) be the number of monomers. It has the exact parity-constrained mass function
\[
\Pr(m)=\frac{n!}{Z_n(z)\,m!\,2^{(n-m)/2}((n-m)/2)!}z^{(n-m)/2},
\qquad m\in\{n\bmod2,n\bmod2+2,\ldots,n\}.
\]
For \(z=\theta/(n-1)\) where \(\theta=(1-p)/p\), successive unnormalized probabilities satisfy
\[
\frac{w_{m+2}}{w_m}=\frac{n-m}{z(m+1)(m+2)}.
\]
Applying Stirling's formula at \(m=sn\) gives a strictly concave logarithmic profile (up to an additive constant),
\[
\phi(s)=-s\log s-\frac{1-s}{2}\log(1-s)+\frac{1-s}{2}\log\theta-\frac{1-s}{2},
\]
with unique interior maximum at \(s=u\), where \(\theta u^2=1-u\), and curvature
\[
\phi''(u)=-\frac{2-u}{2u(1-u)}.
\]
Uniform Stirling estimates around the maximum, the strictly decreasing adjacent mass ratio, and exponentially small tails outside any fixed neighborhood justify the discrete Laplace expansion and its second-moment convergence (the lattice spacing is two). In particular,
\[
\frac{m}{n}\to u\quad\text{in probability},\qquad
\frac{\operatorname{Var}(m)}{n}\to\sigma^2=\frac{2u(1-u)}{2-u}.
\]
Conditionally on \(m\), uniform matching among exactly \(n-m\) occupied vertices gives
\[
\mathbb E(C\mid m)=\frac{kl(n-m)}{n(n-1)},
\]
\[
\mathbb E(C(C-1)\mid m)=\frac{k(k-1)l(l-1)(n-m)(n-m-2)}{n(n-1)(n-2)(n-3)}
\]
for \(n\ge4\) (for smaller \(n\), the second factorial moment vanishes). Expanding these exact rational expressions with \(k/n\to a\), and using the concentration and moments above, yields
\[
\lim\frac{\mathbb E[\operatorname{Var}(C\mid m)]}{n}=A_0(1-u)[u+2A_0(1-2u)],
\qquad
\lim\frac{\operatorname{Var}(\mathbb E(C\mid m))}{n}=A_0^2\sigma^2.
\]
The law of total variance establishes the boxed formula. Because the conditional variance is a polynomial-rational function of \(m\) of degree at most two, concentration plus the explicit second-moment limit suffice; no assumption about higher cumulants is needed.

## Verification

Run `python3 verify_bell.py` using only the Python standard library. The verifier enumerates all matchings for \(2\le n\le8\) and three rational choices of \(p\), checks complete transition matrices and detailed balance using rational arithmetic, checks the proposed generating function coefficient by coefficient for every nontrivial bipartition, and independently checks both moments. It reports `VERIFY_OK: 21 exact weighted matching chains; 3342 state instances; 70788 transition pairs; generating distributions and first two moments for every bipartition; 9 thermodynamic variance checks`. Nine additional stable numerical evaluations at \(n=4000\), three values of \(p\), and three cut fractions check the asymptotic coefficient to tolerance \(10^{-3}\). These are corroborations rather than an exhaustive proof for all sizes; the proof above supplies that step.

## Relationship to prior work

Holdhusen, McAmis, and Rahmani [1, main text Eqs. (3)–(7), pp. 2–3] establish the exact Bell-matching automaton and the leading mean-field entanglement scaling for uniform Bell sampling. Their Supplemental Material II, pp. 7–8, derives conditional combinatorial pairing counts and an averaged entropy expression based on an asymptotic monomer-density approximation. Those foundational matching identities are credited and not claimed to be new. The contribution here is an exact finite-size **stationary** reversible law, the resulting **unconditional all-moment cut-entropy distribution**, and the explicit fluctuation coefficient including the otherwise missed global monomer-count fluctuations. The full first-version paper including its supplement was inspected, not merely the abstract.

The general monomer-dimer Gibbs representation and complete-graph mean-field density are established mathematical background [2–4]. They do not by themselves state the particular quantum-measurement chain's detailed balance, cross-cut entropy generating function, or its explicit variance coefficient. The latter requires both two-edge matching correlations and the monomer fluctuation curvature. The new statement is scoped to that combined quantum-statistical observable and does not claim a general new monomer-dimer principle.

## Limitations

All-to-all uniform Bell sampling is essential to the reversible Gibbs law; no claim is made for power-law biased pair selection or finite-range measurements. The result is stationary, not a mixing-time bound. The thermodynamic variance constant is established only with fixed \(p\in(0,1)\) and macroscopic \(a\in(0,1)\). No quantum advantage or multipartite entanglement is asserted. An unindexed equivalent specialization of standard monomer-dimer fluctuation identities remains possible and requires independent priority review.

## References

[1] W. Holdhusen, B. M. McAmis, and A. Rahmani, "Classical Cellular Automaton for Measurement-Only Entanglement Transitions," arXiv:2609.28743v1 (first public version 2026-09-23), especially main text pp. 2–3 and Supplemental Material II pp. 7–8. https://arxiv.org/pdf/2609.28743

[2] D. Alberici, P. Contucci, and E. Mingione, "A Mean-Field Monomer–Dimer Model with Randomness: Exact Solution and Rigorous Results," Journal of Statistical Physics 160 (2015), 1721–1732, DOI:10.1007/s10955-015-1306-x.

[3] W.-K. Lam and A. Sen, "Central limit theorem in disordered Monomer-Dimer model," Random Structures & Algorithms 66 (2025), e21256; first online 2024-08-07, DOI:10.1002/rsa.21256.

[4] O. J. Heilmann and E. H. Lieb, "Theory of monomer-dimer systems," Communications in Mathematical Physics 25 (1972), 190–232, DOI:10.1007/BF01877590.
