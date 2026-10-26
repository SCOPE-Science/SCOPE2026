# Sharp parity-separation profile and all optimal systematic linear encoders

## Finding
Let \(r\ge0\) be an integer. Define \(K(r)\) as the largest integer \(k\ge0\) for which a binary **systematic linear** encoding
\[E(u)=(u,uP):\mathbb F_2^k\longrightarrow\mathbb F_2^{k+r}\]
exists with two distance requirements:

1. For all distinct \(u,v\in\mathbb F_2^k\), \(d_H(E(u),E(v))\ge3\).
2. Whenever \(\sum_i u_i\ne\sum_i v_i\pmod2\), \(d_H(E(u),E(v))\ge4\).

For \(k=0\), these requirements are vacuous. Then the exact profile is
\[
\boxed{K(r)=\begin{cases}0,&0\le r\le2,\\1,&r=3,\\5,&r=4,\\2^{r-1}-r,&r\ge5.\end{cases}}
\]
Furthermore, all parity-check column **sets** attaining this maximum can be classified, with the \(r\) parity coordinates labeled and with arbitrary permutations of the \(k\) information coordinates identified. For \(r=3\), there is one maximizing column set, \(\{111\}\). For \(r=4\), there is one, consisting of every four-bit vector of weight at least three. For every \(r\ge5\), there are exactly \(r+1\) maximizing column sets. Writing
\[B_r=\{v\in\mathbb F_2^r:\operatorname{wt}(v)\ge3\},\]
they are
\[
B_r\cap\{v:v_j=1\}\quad(1\le j\le r),\qquad
B_r\cap\{v:\sum_{j=1}^r v_j=1\pmod2\}.
\]
The \(r\) coordinate-hyperplane constructions have minimum **data** distance exactly three and function-separation distance exactly four, and hence offer a *strict* one-unit separation. The remaining all-odd-weight construction has overall minimum distance four, so it does not have strict separation. The unique \(r=4\) maximizing construction is strict; the \(r=3\) one is not.

## Assumptions and scope
The alphabet is \(\mathbb F_2\) with ordinary Hamming distance. The function is the parity (modular sum) \(f(u)=\sum_i u_i\pmod2\), not the integer Hamming weight. The encoder is linear and systematic **in the stated message coordinates**; neither nonlinear maps nor free/non-systematic encoders are covered. Redundancy \(r\) means the number of appended transmitted parity symbols, not the rank of \(P\). The thresholds three and four are minimum separations, not claims of different integer-radius error-correction guarantees: both distances correct one Hamming error, whereas distance four detects an additional error. The classification counts unordered sets of distinct \(r\)-bit check columns, not ordered generator matrices.

## Proof
**1. Reduction to a restricted sum-free set.** Let the \(k\) rows of \(P\) be \(h_1,\ldots,h_k\in\mathbb F_2^r\). For a message difference with support \(T\subseteq\{1,\ldots,k\}\), its encoded weight is
\[
|T|+\operatorname{wt}\left(\sum_{i\in T}h_i\right).
\]
For \(|T|=1\), function separation four forces \(\operatorname{wt}(h_i)\ge3\). For \(|T|=2\), data distance three forces \(h_i\ne h_j\). For \(|T|=3\), function separation four forces \(h_i+h_j+h_\ell\ne0\). Conversely these three conditions suffice: differences of size at least four automatically have data distance at least four, and odd-sized differences of size at least five automatically have function separation at least five. Thus an admissible encoder is equivalent to a set \(S=\{h_1,\ldots,h_k\}\subseteq B_r\) with no distinct triple satisfying \(a+b=c\). Because zero is excluded, this is exactly the usual sum-free condition \((S+S)\cap S=\varnothing\) in characteristic two.

**2. A structural input.** We use the following known theorem of Davydov--Tombak (1989): if a sum-free set \(S\subseteq\mathbb F_2^r\), for \(r\ge4\), is not contained in an affine hyperplane, then \(|S|\le5\cdot2^{r-4}\). Its statement is quoted explicitly by Reiher (2025, Introduction). This external theorem, rather than finite computation, is the key non-elementary ingredient.

**3. The exact upper bound for \(r\ge5\).** Let \(M_r=2^{r-1}-r\). The set of odd-weight vectors of weight at least three is sum-free and has size \(M_r\), since exactly \(r\) odd-weight vectors have weight one. Thus \(K(r)\ge M_r\). For every \(r\ge5\), \(M_r>5\cdot2^{r-4}\); at \(r=5\) the gap is one and grows thereafter. Consequently any competing sum-free set of at least \(M_r\) vectors must be contained in an affine hyperplane. A sum-free set in a linear hyperplane through the origin has cardinality at most \(2^{r-2}\), below \(M_r\), so the hyperplane has the form
\[H_a=\{v:a\cdot v=1\},\quad a\in\mathbb F_2^r\setminus\{0\}.\]
If \(a\) has Hamming weight \(s\), the hyperplane contains exactly \(s\) weight-one vectors and \(s(r-s)\) weight-two vectors, leaving at most
\[
2^{r-1}-s(r-s+1)\le2^{r-1}-r=M_r,
\]
where \(s(r-s+1)-r=(s-1)(r-s)\ge0\). Therefore \(K(r)=M_r\).

**4. Classification of equality.** To attain \(M_r\), equality forces \((s-1)(r-s)=0\), hence \(s=1\) or \(s=r\), and the set must include *every* weight-at-least-three vector of its affine hyperplane. These are the \(r\) coordinate sets and the single all-odd-weight set displayed above. They are all sum-free as subsets of affine hyperplanes avoiding the origin. Since \(M_r>2^{r-2}\) and two distinct affine hyperplanes intersect in at most \(2^{r-2}\) points, these \(r+1\) sets are distinct and exhaustive. For any coordinate-hyperplane family and \(r\ge5\), two allowed check columns can be chosen of weights three and four, differing in one coordinate, which creates an input difference of size two and codeword weight three. The all-odd-weight family produces no codeword of weight below four: weight-one information words have parity part of weight at least three, while any nonzero xor of two odd-weight distinct columns has even weight at least two; inputs of information weight at least three satisfy the remaining bound. In either family a weight-three column gives function-separation weight four. Thus the strict/non-strict distinction is exact.

**5. Small dimensions.** For \(r\le2\), \(B_r\) is empty. For \(r=3\), \(B_r=\{111\}\), giving \(K(3)=1\) and overall distance four. For \(r=4\), \(B_r\) has the four vectors of weight three plus the all-ones vector, all pairwise distinct. The xor of any two distinct weight-three vectors has weight two, and the xor of a weight-three vector with the all-ones vector has weight one, so no two sum to a member of \(B_r\). Thus all five columns are feasible, proving \(K(4)=5\), uniqueness, and distance exactly three.

## Verification
Run `python3 verify.py` with the Python standard library. It exhaustively enumerates all candidate column subsets in dimensions three through five, checks the predicted optimum and number of maximizers, checks all distinct constructions for dimensions five through nine, and checks every nonzero encoded message difference for the maximizing constructions in dimensions three through five. The included `verify_output.txt` ends in `VERIFY_OK`. Exhaustion in finitely many dimensions is **not** used to justify the all-dimensional bound, which follows from the stated structural theorem and the proof above.

## Relationship to prior work
Rajput--Rajan--Freij-Hollanti--Hollanti (2025 preprint, 2026 journal article) introduced linear function-correcting codes with data protection and their coset-distance formulation, but did not give this fixed-redundancy parity-function profile or the maximizing column families. Verma--Singh (2026) treated the modular-sum function in the Lee-metric data-protection framework, which specializes to Hamming distance over binary symbols, giving general bounds rather than the exact linear classification here. Ho (2026) determined systematic linear function-separation redundancy for separation thresholds at most three; the present function-distance-four problem, with an additional data-distance-three constraint, is not a specialization of those exact low-threshold results. The 2026 study of optimal generator encodings for fixed codes addresses a different optimization variable, not the maximum message dimension at fixed physical redundancy. The Davydov--Tombak sum-free-set bound is a **published key lemma**, not a novelty claim; the new conclusion identifies the restricted column-geometry optimum and its complete strict/non-strict classification. See references.

## Limitations
All proofs assume systematic *linear* encodings and exact parity-of-data function, with the specified two distance thresholds; no optimality for nonlinear or nonsystematic encodings follows. The structural bound quoted from Davydov--Tombak is used as a known theorem, not independently reproved. The equivalence of this restricted sum-free extremal problem to a previously indexed coding invariant cannot be wholly excluded; in particular, more exhaustive primary-text comparison of very recent systematicity papers would be appropriate for independent validation. The result does not claim a two-error function-correction guarantee, because separation distance four corresponds to one-error correction plus enhanced detection, not radius-two correction.

## References
1. C. Rajput, B. S. Rajan, R. Freij-Hollanti, C. Hollanti, *Function-Correcting Codes With Data Protection*, arXiv:2511.18420v1 (first submitted 2025-11-23); IEEE Transactions on Information Theory **72** (2026), 4860--4880, DOI 10.1109/TIT.2026.3692458. Full text: https://www.researchgate.net/publication/404792787_Function-Correcting_Codes_With_Data_Protection
2. G. K. Verma and A. K. Singh, *On Function-Correcting Lee Metric Codes with Data Protection*, arXiv:2610.12217v1 (2026-10-08), especially Section 4.3. https://arxiv.org/html/2610.12217v1
3. A. A. Davydov and L. M. Tombak, *Quasi-perfect linear binary codes with distance 4 and complete caps in projective geometry*, Problems of Information Transmission **25** (1989). Structural sum-free bound as stated in Reference 4.
4. C. Reiher, *On Lev's periodicity conjecture*, Bulletin of the London Mathematical Society **57** (2025), 1496--1511, Introduction. https://doi.org/10.1112/blms.70043
5. D. Ho, *On systematicity of linear function-correcting codes*, arXiv:2608.29389 (2026-08-29).
6. C. Rajput, K. L. Jagatti, B. S. Rajan, *On Optimal Encodings and Systematicity in Function-Correcting Codes*, arXiv:2610.09011 (2026-10-06).
7. C. Rajput et al., *Existence and Constructions of Strict Function-Correcting Codes with Data Protection*, arXiv:2604.26397 (2026-04-29).
