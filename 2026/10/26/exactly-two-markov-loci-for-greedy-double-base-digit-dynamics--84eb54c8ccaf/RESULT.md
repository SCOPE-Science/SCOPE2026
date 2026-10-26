# Exactly two Markov loci for greedy double-base digit dynamics

## Finding
Let \(s>1\), \(1<q\le s/(s-1)\), and set \(c=1/s\), \(r=q/s\), \(M=1/(s-1)\). The stationary greedy binary digit sequence of the map
\[
G(x)=\begin{cases}qx,&0\le x<c,\\sx-1,&c\le x\le M\end{cases}
\]
is a time-homogeneous one-step Markov chain **if and only if**
\[
q=1+1/s\quad\text{or}\quad q=s/(s-1).
\]
On the first, strictly interior locus, its transition matrix and stationary law (state order \(0,1\)) are
\[
P=\begin{pmatrix}\frac{s}{s+1}&\frac1{s+1}\\1&0\end{pmatrix},\qquad
\pi=\left(\frac{s+1}{s+2},\frac1{s+2}\right).
\]
The binary digits are genuinely dependent, with exact lag covariance
\[
\operatorname{Cov}(D_0,D_n)=\frac{s+1}{(s+2)^2}\left(-\frac1{s+1}\right)^n\quad(n\ge0),
\]
and asymptotic centered partial-sum variance per digit
\[
\lim_{N\to\infty}\frac1N\operatorname{Var}\left(\sum_{n=0}^{N-1}D_n\right)
=\frac{s(s+1)}{(s+2)^3}.
\]
On the second, endpoint locus, the digits are independent and identically distributed, with \(\Pr(D_n=1)=1/s\).

## Assumptions and scope
For the parameter range above, \(G\) is the greedy two-base interval map on \([0,M]\). Write \(I_0=[0,c)\), \(I_1=[c,M]\), and \(J_0=[0,c)\), \(J_1=[c,r]\). Let \(\mu\) denote its unique absolutely continuous invariant probability measure; existence, uniqueness within the absolutely continuous class, and equivalence to Lebesgue measure on \([0,r)\) are established in Huang--Komornik--Zou (2026), Theorems 1.1--1.2. Thus \(D_n=\mathbf 1_{I_1}(G^n X)\), for \(X\sim\mu\), is stationary. One-step Markov means that for every finite word of positive probability, the conditional probability of the next digit depends only on its last digit. Endpoints have \(\mu\)-measure zero and do not affect statements. The result concerns this specific natural generating binary partition and this absolutely continuous stationary measure, not arbitrary invariant measures or finite-memory chains of higher order.

## Proof
**1. Support and admissible intervals.** Since \(r>c\) and \(r\le M\), both digits occur with positive probability. Moreover \(G(J_0)=[0,r]\) and \(G(J_1)=[0,q-1]\), up to endpoints. Therefore the adjacent words \(00\), \(01\), and \(10\) have strictly positive probability: their cylinder sets contain positive-length intervals in \([0,r)\), where \(\mu\) is equivalent to Lebesgue measure. The word \(11\) has positive probability exactly when \(q-1>c\), or \(q>1+1/s\).

**2. Necessity below the first locus.** Suppose \(1<q<1+1/s\). The word \(11\) is forbidden, but both \(01\) and \(10\) have positive probability. If the stationary digits formed a one-step Markov chain, any finite alternating word \(1010\cdots10\) would then have strictly positive probability. To show this is impossible, let \(F=G|_{J_0}\circ G|_{J_1}\), so \(F(x)=q(sx-1)\) along every allowable \(10\) pair. The affine map has slope \(sq>1\) and fixed point \(z=q/(sq-1)\). Under \(q<1+1/s\), \(z>r\). Thus for every starting point \(x\in J_1\subseteq[0,r]\), the formal iterate satisfies
\[
F^k(x)=z+(sq)^k(x-z)\le z-(sq)^k(z-r)\longrightarrow-\infty
\]
uniformly. For sufficiently large \(k\), this is incompatible with following \(k\) successive \(10\) pairs while remaining in \([0,r]\). Hence the required long alternating cylinder is empty, contradicting one-step Markovity.

**3. Necessity between the loci.** Suppose \(1+1/s<q<s/(s-1)\). Now \(11\) occurs with positive probability. Under a stationary one-step Markov law, arbitrarily long words \(11\cdots1\) would then have positive probability. On such a word, the right-branch affine map \(R(x)=sx-1\) is iterated. Its fixed point is \(M=1/(s-1)>r\); hence
\[
R^k(x)=M+s^k(x-M)\le M-s^k(M-r)\longrightarrow-\infty
\]
uniformly for \(x\le r\). Therefore sufficiently long all-one cylinders are empty, a contradiction. This excludes all parameters strictly between the two specified loci.

**4. Sufficiency on the interior locus.** Let \(q=1+1/s\). Then \(r=(s+1)/s^2\), \(G(J_0)=[0,r]\), and \(G(J_1)=[0,c]\). In particular, each allowed transition \(i\to j\) restricts \(G\) to a bijection of its transition subinterval onto the whole partition atom \(J_j\), with constant slope. Direct substitution in the Perron--Frobenius equation gives the probability density
\[
h(x)=\frac{s(s+1)}{s+2}\mathbf 1_{J_0}(x)+\frac{s^2}{s+2}\mathbf 1_{J_1}(x).
\]
The total integral is one, and the equations on \(J_0\) and \(J_1\) are respectively \(h_0=h_0/q+h_1/s\) and \(h_1=h_0/q\). Uniqueness of the absolutely continuous invariant probability identifies this density with \(d\mu/dx\). For every positive-probability cylinder \((D_0,\ldots,D_n)=(d_0,\ldots,d_n)\), the composition \(G^n\) is affine and maps the cylinder bijectively onto \(J_{d_n}\). The initial density is constant on the initial partition atom, so the conditional distribution of \(G^nX\) given that entire word is uniform on \(J_{d_n}\). Consequently the next digit depends only on \(d_n\). From the ratios of transition-preimage lengths we obtain
\[
P_{00}=1/q=\frac{s}{s+1},\quad P_{01}=\frac1{s+1},\quad P_{10}=1,\quad P_{11}=0.
\]
Integrating \(h\) gives \(\pi_1=1/(s+2)\). The nontrivial eigenvalue is \(\lambda=-1/(s+1)\), so the standard two-state covariance calculation gives \(\operatorname{Cov}(D_0,D_n)=\pi_1(1-\pi_1)\lambda^n\). Summing the absolutely convergent covariance series yields the stated asymptotic variance.

**5. Sufficiency on the endpoint locus.** Let \(q=s/(s-1)\). Then \(r=M\) and **both** digit branches map their full atoms onto \([0,M]\). The normalized Lebesgue density \(h=1/M=s-1\) is invariant, because \(1/q+1/s=1\). Every inverse cylinder maps the full interval onto a subinterval with length ratio \(q^{-N_0}s^{-N_1}\), so under normalized Lebesgue the digits are independent, with digit probabilities \(1/q=(s-1)/s\) and \(1/s\). These two loci exhaust the admissible parameter set by steps 2--3.

## Verification
All algebraic identities in the proof are exact. A standalone Python 3 script `CHECKER.py` uses rational arithmetic to enumerate cylinder intervals and compare their probabilities with the claimed Markov-product law for all binary words of lengths one through seven on both loci at \(s\in\{3/2,2,5/3,5\}\). It also exhibits forbidden long alternating or all-one words for two interior off-locus rational parameters. The script has been executed and returned all checks passing. These finite tests are corroboration only; the repelling-fixed-point argument proves the all-length exclusions, and the affine-cylinder argument proves the all-length Markov identities.

## Relationship to prior work
Huang, Komornik, and Zou (arXiv:2605.08641v1) introduce the two-slope greedy map and determine the unique absolutely continuous invariant probability, its support, and jump-density formulas (Theorems 1.1--1.3). Their full manuscript was inspected, including the map, main theorems, transfer-operator formula, and examples; these do not state the present necessary-and-sufficient **stationary one-step digit Markov** classification. Their endpoint constant-density example corresponds to the second locus, so that density fact is prior input, not asserted as a novel result. Classical \(\beta\)-shift/Markov partition theory treats the equal-slope specialization, and results on finite-type intermediate \(\beta\)-shifts concern different parameter families. The classification above handles all admissible unequal-slope pairs and includes the strictly interior Markov locus and a necessity argument from forbidden long words.

## Limitations
Novelty is assessed against accessible literature and relevant existing mathematical records, not exhaustively against every possible equivalent formulation. In particular, full texts of some older papers on intermediate \(\beta\)-shifts and double-base univoque expansions were not accessible in this run, and a hidden stronger symbolic classification might imply the result. The independent scientific audit has not been performed. The theorem does not classify higher-order Markov digit processes, all invariant measures, lazy expansions, or other choices of state partition.

## References
1. W. Huang, V. Komornik, and Y. Zou, *Invariant measure for double base expansions*, arXiv:2605.08641v1 (first public 2026-05-09), Sections 1--4, Theorems 1.1--1.3, Example 4.1. https://arxiv.org/abs/2605.08641
2. B. Li, T. Sahlsten, and T. Samuel, *Intermediate \(\beta\)-shifts of finite type*, arXiv:1401.7027 (related equal-slope finite-type question; abstract inspected). https://arxiv.org/abs/1401.7027
3. V. Komornik, W. Steiner, and Y. Zou, *Unique double base expansions*, arXiv:2209.02373 (different uniqueness-of-expansions question; abstract inspected). https://arxiv.org/abs/2209.02373
