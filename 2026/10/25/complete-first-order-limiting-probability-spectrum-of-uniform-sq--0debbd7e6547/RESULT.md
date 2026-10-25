# Complete first-order limiting-probability spectrum of uniform square permutations

## Finding

Let \(\mathcal Q_n\) consist of permutations of \([n]\) that admit a square root in the symmetric group, and choose \(\pi_n\) uniformly from \(\mathcal Q_n\). Regard \(\pi_n\) as a structure with equality and one binary successor relation \(R(x,y)\), true exactly when \(\pi_n(x)=y\). For each positive integer \(j\), write \(C_j\) for the number of directed cycles of length \(j\).

**Theorem.** For every fixed \(b\), the vector of counts \((C_1(\pi_n),\ldots,C_b(\pi_n))\) converges jointly to independent integer-valued random variables \((Z_1,\ldots,Z_b)\) with
\[
 \Pr(Z_j=t)=\begin{cases}
 e^{-1/j}(1/j)^t/t!,&j\text{ odd},\quad t\ge0,\\
 (1/j)^t/(t!\cosh(1/j)),&j\text{ even},\quad t\ge0\text{ even},\\
 0,&j\text{ even},\quad t\text{ odd}.
 \end{cases}
\]
Every first-order sentence \(\varphi\) in \(\{R,=\}\) has a limiting probability. Moreover, the **entire set** of first-order limiting probabilities is exactly
\[
 \mathcal S=\{\Pr(E):E\text{ is a finite Boolean combination of statements }Z_j\ge t,
 \ j\ge1,\ t\ge1\}.
\]
Here each Boolean combination uses only finitely many indices and thresholds. The set \(\mathcal S\) is dense in \([0,1]\), and for every individual \(s\in\mathcal S\) there exists a positive integer \(D\) such that \(s\in\mathbb Q(e^{1/D})\). Both a sentence's limiting value and a sentence realizing any specified finite Boolean combination can be obtained effectively.

For illustration, the limiting probability of having no directed \(2\)-cycle is \(1/\cosh(1/2)\), while that of having no fixed point is \(e^{-1}\). The even-length obstruction therefore remains first-order visible at every fixed even cycle length, even though arbitrary long cycles become locally indistinguishable.

## Assumptions and scope

The underlying probability measure is **uniform on permutations that possess a square root**, not the image distribution obtained by squaring a uniformly sampled permutation. Only positive sizes \(n\) are considered. The vocabulary has one binary relation representing the permutation graph; no external linear order, labels, counting quantifiers or second-order quantifiers are present. Parameters \(b,j,t\) and each logical sentence are fixed before \(n\) tends to infinity.

## Proof

**1. The admissible cycle multisets and generating series.** A cycle of odd length has a square root supported on the same set. A cycle of even length in a squared permutation always arises in a pair of equal-length cycles; conversely, each pair of equal-length even cycles can be interleaved into the square of one longer cycle. Hence \(\pi\in\mathcal Q_n\) exactly when \(C_j(\pi)\) is even for every even \(j\). Labelled permutation cycle counting gives the normalized generating series
\[
 F(z):=\sum_{n\ge0}\frac{|\mathcal Q_n|}{n!}z^n
 =A(z)H(z),\qquad A(z)=\exp\left(\sum_{j\text{ odd}}\frac{z^j}{j}\right)
 =\sqrt{\frac{1+z}{1-z}},\qquad
 H(z)=\prod_{j\text{ even}}\cosh\left(\frac{z^j}{j}\right).
\]
This enumerative identity is classical (Pouyanne, 2002, and earlier work); it is an input rather than a claim of novelty.

**2. Coefficient-ratio lemma.** The nonnegative coefficients \(a_n=[z^n]A(z)\) satisfy \(a_n\sim\sqrt{2/\pi}\,n^{-1/2}\); this follows from the dominant singularity at \(1\), because the singularity at \(-1\) has the weaker order \((1+z)^{1/2}\). Removing any *fixed finite* collection of odd-cycle factors changes this asymptotic only by multiplication by \(\exp(-\sum 1/j)\), where the sum ranges over the removed lengths.

For every finite cutoff \(b\), the even-cycle tail \(H_{>b}(z)=\prod_{j>b,\ j\text{ even}}\cosh(z^j/j)\) has nonnegative coefficients \(h_m\) with \(H_{>b}(1)<\infty\). More strongly, for every \(\alpha\in(1/2,1)\), \(\sum_m m^\alpha h_m<\infty\): after normalizing each factor at \(1\), treat its cycle mass as the nonnegative random variable \(jT_j\), where \(T_j\) has the even-supported distribution proportional to \(1/(j^t t!)\). Its \(\alpha\)-moment is \(O(j^{\alpha-2})\), summable over even \(j\); subadditivity of \(u^\alpha\) controls the sum over factors. If \(a^{(b)}_n\) denotes the coefficients of the odd-factor tail, then \(a_n^{(b)}\sim c_b n^{-1/2}\) and is bounded. Split \([z^n]A_{>b}H_{>b}\) at even-tail mass \(m=n/2\). For \(m\le n/2\), dominated convergence applies to \(a^{(b)}_{n-m}/a_n^{(b)}\), which is uniformly bounded and tends to one for fixed \(m\). For \(m>n/2\), boundedness of \(a^{(b)}_{n-m}\) and the fractional-moment tail give \(o(n^{-\alpha})=o(n^{-1/2})\). Thus
\[
 [z^n]A_{>b}(z)H_{>b}(z)
 \sim \sqrt{\frac{2}{\pi n}}\exp\left(-\sum_{\substack{j\le b\\j\text{ odd}}}\frac1j\right)
 \prod_{\substack{j>b\\j\text{ even}}}\cosh(1/j).
\]
In particular \([z^n]F(z)\sim\sqrt{2/(\pi n)}H(1)\), and the ratio for the omitted finite factors tends to the reciprocal of \(\prod_{j\le b,\ j\text{ odd}}e^{1/j}\prod_{j\le b,\ j\text{ even}}\cosh(1/j)\).

**3. Joint short-cycle limit.** Fix \(b\) and permitted counts \(t_1,\ldots,t_b\). Extracting the exact cycle factors gives
\[
 \Pr(C_j(\pi_n)=t_j\ (1\le j\le b))
 =\frac{[z^{n-\sum_{j\le b}jt_j}]A_{>b}(z)H_{>b}(z)}{[z^n]F(z)}
 \prod_{j=1}^b\frac{1}{j^{t_j}t_j!}.
\]
The coefficient-ratio lemma proves convergence to the stated product distribution. The limiting probabilities sum to one (each odd Poisson and each even conditional Poisson distribution is normalized), so joint weak convergence follows, not merely pointwise convergence of selected mass functions.

**4. Complete logical limit classification.** The undirected Gaifman graph of \(R\) is a disjoint union of directed cycles and has maximum degree two. For any first-order sentence \(\varphi\), the effective bounded-degree Hanf theorem provides a radius \(r\) and threshold \(T\) such that its truth depends only on counts of rooted radius-\(r\) neighborhood types truncated at \(T\). For a permutation, every cycle longer than \(2r+1\) gives precisely the same rooted radius-\(r\) directed-path type. Every shorter cycle contributes one distinguishable rooted type, its count being \(jC_j\). By step 3, the total number of vertices on shorter cycles is tight; therefore the number of vertices of the long-path type tends to infinity in probability. Hence the limiting truth of \(\varphi\) is a Boolean function of finitely many truncated short-cycle counts. This yields existence and the upper inclusion in \(\mathcal S\). Conversely, each condition \(C_j\ge t\) is definable by requiring \(t\) distinct disjoint directed \(j\)-cycles, so every finite Boolean combination is realized by a first-order sentence. The effective enumeration of finite neighborhood types and of truncated vectors yields an algorithm for each probability.

**5. Arithmetic restriction and density.** For finitely many \(j\), probabilities of truncated \(Z_j\) are built from rational numbers, \(e^{-1/j}\) for odd \(j\), and \(1/\cosh(1/j)=2e^{-1/j}/(1+e^{-2/j})\) for even \(j\). Choosing \(D\) divisible by the finitely many indices places every Boolean combination probability in \(\mathbb Q(e^{1/D})\). For density, use only distinct odd lengths \(j\ge3\). The indicators \(\mathbf1_{\{Z_j\ge1\}}\) are independent Bernoulli variables with parameter \(1-e^{-1/j}<1/2\). For a growing finite set of such odd lengths the largest atom has probability \(\exp(-\sum_j 1/j)\to0\), because the harmonic series over odd integers diverges. Ordering these finitely many atoms and taking partial unions approximates any given value in \([0,1]\) to within the largest atom. Each such union is definable, proving density.

## Verification

Run the included standalone program with `python3 square_permutation_check.py`. It enumerates each permutation through size eight and tests square-root admissibility by its even cycle multiplicities. An entirely separate exact-rational coefficient construction multiplies the cycle factors. For every size one through eight, the two methods agree on the total count, on absence of fixed points, on absence of two-cycles, and on the joint event of exactly one fixed point and no two-cycle. Successful execution reports `SQUARE_PERM_EXACT_OK 8 16517 4x8_coeff_checks 14280`. These finite checks corroborate the decomposition and generating function; they do not establish coefficient asymptotics, infinite limits or FO equivalence. Those rely on the arguments above.

## Relationship to prior work

Pouyanne, *On the Number of Permutations Admitting an m-th Root* (2002), supplies the exact cycle-admissibility criterion, product generating functions, and enumeration asymptotics for powers of permutations. Bóna, McLennan and White, *Permutations with roots* (2000), study root-existence probabilities. These enumerative conclusions are not claimed as new. Compton's first-order convergence result for uniformly random permutations, described explicitly in Müller, Skerman and Verstraaten, *Logical limit laws for Mallows random permutations* (arXiv:2302.10148), concerns the unconditioned permutation law; the cited Mallows theorems concern inversion-biased measures, not uniform sampling on square-permutation classes. Burris, Compton, Odlyzko and Richmond (1997) provide abstract admissible-class logical limit-law tools whose general conclusions may apply to the class studied here. The current contribution is the **explicit complete family of all attainable first-order limiting probabilities**, including the parity-conditioned short-cycle distributions and arithmetic/density consequences, not the classical counting theorem or generic existence of a limit law.

The recent convergence-law program of Adam-Day, Benedikt and Larrauri (arXiv:2504.14270, first version 19 April 2025) and Koponen (arXiv:2610.16163, first version 12 October 2026) motivates studying which restricted finite structure classes have fully computable logical limiting statistics; neither addresses square permutations. Their published statements are not used as premises for the enumeration or coefficient estimates.

## Limitations

Only first-order sentences in the one-relation permutation language are covered; no assertion is made for two-order permutation logic, counting extensions, monadic second-order logic, or a uniformly sampled *square of* a permutation. The work uses standard singularity analysis and bounded-degree locality. Generic logical convergence may be subsumed by existing abstract theorems; the explicitly determined limiting-probability spectrum is the object of the new claim. A possible unlocated specialized theorem on FO spectra of root-admitting permutations remains a historical-priority risk. Numerical checks are strictly finite.

## References

1. N. Pouyanne, *On the Number of Permutations Admitting an m-th Root*, Electronic Journal of Combinatorics 9 (2002), R3, https://doi.org/10.37236/1620 (full text https://www.combinatorics.org/ojs/index.php/eljc/article/download/v9i1r3/pdf/).
2. M. Bóna, A. McLennan, D. White, *Permutations with Roots*, Random Structures & Algorithms 17 (2000), 157–167, https://doi.org/10.1002/1098-2418(200009)17:2%3C157::AID-RSA4%3E3.0.CO;2-2.
3. T. Müller, F. Skerman, T. W. Verstraaten, *Logical limit laws for Mallows random permutations*, arXiv:2302.10148, https://arxiv.org/abs/2302.10148.
4. S. Burris, K. Compton, A. Odlyzko, B. Richmond, *Fine Spectra and Limit Laws, II: First-Order 0–1 Laws*, Canadian Journal of Mathematics 49 (1997), 641–652, https://doi.org/10.4153/CJM-1997-030-6.
5. S. Adam-Day, M. Benedikt, A. Larrauri, *Convergence Laws for Extensions of First-Order Logic with Averaging*, arXiv:2504.14270v1, https://arxiv.org/abs/2504.14270.
6. V. Koponen, *A characterization of the finite model property for \(\omega\)-categorical theories*, arXiv:2610.16163v1, https://arxiv.org/abs/2610.16163.
