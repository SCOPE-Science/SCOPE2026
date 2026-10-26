# The full first-order probability spectrum for bounded-multiplicity unlabelled permutations

## Finding
For every fixed integer \(r\ge1\), choose uniformly from the isomorphism classes of \(n\)-element permutations in which every cycle length appears at most \(r\) times. Then every first-order sentence in the directed successor relation has an effectively computable limiting probability. The complete set of such limits is
\[
\mathcal S_r=\mathbb Z[1/(r+1)]\cap[0,1].
\]
More precisely, for every fixed \(J\ge1\), cycle counts at lengths \(1,\ldots,J\) jointly converge to independent uniform variables on \(\{0,\ldots,r\}\). Thus the distinct-cycle-length model (\(r=1\)) has the dyadic spectrum, the at-most-two model (\(r=2\)) has the triadic spectrum, and every base \(r+1\) occurs.

## Assumptions and scope
The domain is a finite set of \(n\) elements with a bijection, in the language consisting of equality and one binary relation \(R(x,y)\), interpreted as \(f(x)=y\). The probability space has one equally weighted outcome per **isomorphism class**, not per labelled bijection. The fixed integer \(r\) does not grow with \(n\); each length \(j\) occurs \(m_j\) times with \(0\le m_j\le r\) and \(\sum_{j\ge1}j m_j=n\). For every positive \(n\) there is at least one admissible class, namely one \(n\)-cycle. The assertion is for sentences, without parameters or counting quantifiers, in this exact relation language.

## Proof
**Step 1: a small-cycle reduction.** A finite directed permutation is a disjoint union of directed simple cycles. Fix a sentence \(\varphi\). The effective bounded-degree Hanf locality theorem provides a computable neighborhood radius \(d\) and multiplicity threshold \(T\) such that \(\varphi\)'s truth depends solely on the rooted radius-\(d\) neighborhoods counted up to \(T\). A directed cycle of length at most \(2d+1\) gives a rooted neighborhood type different from that on every sufficiently long cycle. All cycles longer than \(2d+1\) give one common directed-path neighborhood type. (At radius zero, take \(d\ge1\) without loss.) With \(J=2d+1\), the number of vertices in short cycles is at most \(r\sum_{j=1}^J j\). For \(n>T+r\sum_{j=1}^J j\), the long-cycle neighborhood type is saturated above the threshold; the remaining neighborhood counts are functions only of \((m_1,\ldots,m_J)\). Consequently there is an effectively computable Boolean function
\[
B_\varphi:\{0,\ldots,r\}^J\longrightarrow\{0,1\}
\]
such that, for every sufficiently large \(n\), \(P\models\varphi\) if and only if \(B_\varphi(m_1,\ldots,m_J)=1\). To compute the truth table, for each admissible small-cycle vector take those short cycles together with one sufficiently long cycle and evaluate \(\varphi\) on that finite structure; all such truth values stabilize by Hanf locality. Thus this is an effective reduction, not merely an existence argument.

**Step 2: exact independent-coordinate conditioning.** For every \(t>0\), let \((M_j)_{j\ge1}\) be independent with
\[
\Pr_t(M_j=a)=\frac{e^{-tja}}{Z_j(t)},\qquad Z_j(t)=\sum_{b=0}^{r}e^{-tjb},\qquad 0\le a\le r.
\]
The random sum \(S_t=\sum_{j\ge1}jM_j\) is almost surely finite. Conditioning on \(S_t=n\) yields exactly the uniform law on all admissible bounded-multiplicity partitions of \(n\), because every admissible vector with total \(n\) has unconditioned probability \(e^{-tn}\prod_j Z_j(t)^{-1}\). The infinite product converges since \(\sum_j e^{-tj}<\infty\).

**Step 3: uniform lattice local central limit estimate.** Write \(\mu_t=\mathbb E_tS_t\) and \(\sigma_t^2=\operatorname{Var}_t(S_t)\). There is a unique \(t_n>0\) with \(\mu_{t_n}=n\): the mean is strictly decreasing and continuous, tends to infinity as \(t\downarrow0\), and to zero as \(t\uparrow\infty\). The contributions of indices \(j\le1/t\), for which the coordinate laws stay bounded away from concentration, and exponential tails for indices \(j>1/t\), give
\[
\mu_t=\Theta_r(t^{-2}),\quad \sigma_t^2=\Theta_r(t^{-3}),\quad \sum_{j\ge1}\mathbb E_t|jM_j-\mathbb E_t(jM_j)|^3=O_r(t^{-4}),
\]
so \(t_n=\Theta_r(n^{-1/2})\).

Here is a direct Fourier argument for the needed span-one local limit, including the suppression of noncentral frequencies. For \(j\le\lfloor1/t\rfloor\), both probabilities of \(M_j=0\) and \(M_j=1\) are bounded below by a constant depending only on \(r\). Hence the modulus of each coordinate characteristic function is at most \(\exp[-c_r(1-\cos(j\theta))]\). For \(N=\lfloor1/t\rfloor\) and \(|\theta|\le\pi\), an elementary trigonometric estimate yields
\[
\sum_{j=1}^{N}(1-\cos(j\theta))\ge c\min\{N^3\theta^2,N\}.
\]
For \(|\theta|\le1/N\), sum \(1-\cos(j\theta)\ge c(j\theta)^2\) over \(j\le N\). For \(1/N<|\theta|\le4/N\), sum the same estimate over \(j\le N/8\); for \(4/N<|\theta|\le\pi\), apply the geometric-series bound \(|\sum_{j=1}^N e^{ij\theta}|\le 1/|\sin(\theta/2)|\le\pi/|\theta|\), enlarging the harmless numeric threshold as necessary and covering the remaining bounded transition interval by the preceding lower-bound method. Thus, uniformly in the full Fourier interval,
\[
|\mathbb E_te^{i\theta S_t}|\le\exp[-c_r\min\{t^{-3}\theta^2,t^{-1}\}].
\]
After centering, Taylor expansion on \(|\theta|\le t^{3/2}\log(1/t)\) gives the Gaussian characteristic function with vanishing relative error: the total cubic remainder is at most \(O_r(t^{1/2}\log^3(1/t))=o(1)\). On the complement the displayed exponential bound makes the Fourier inversion integral \(o(1/\sigma_t)\). Therefore, for every fixed integer \(h\),
\[
\Pr_{t_n}(S_{t_n}=n+h)=\frac{1+o(1)}{\sqrt{2\pi}\,\sigma_{t_n}}.
\]
The same proof holds with any fixed first \(J\) coordinates omitted: its variance remains asymptotic to \(\sigma_{t_n}^2\), its mean differs from \(n\) by a bounded amount, and the Fourier bounds persist after deleting finitely many terms. In particular, for any fixed \(w\),
\[
\frac{\Pr_{t_n}(\sum_{j>J}jM_j=n-w)}{\Pr_{t_n}(S_{t_n}=n)}\longrightarrow1.
\]

**Step 4: joint asymptotic uniformity.** For a fixed vector \(a=(a_1,\ldots,a_J)\in\{0,\ldots,r\}^J\) of weight \(w=\sum_{j=1}^Jja_j\), conditioning and independence show exactly that
\[
\Pr(m_1=a_1,\ldots,m_J=a_J)=\prod_{j=1}^J\frac{e^{-t_nja_j}}{Z_j(t_n)}\;\frac{\Pr_{t_n}(\sum_{j>J}jM_j=n-w)}{\Pr_{t_n}(S_{t_n}=n)}\longrightarrow(r+1)^{-J}.
\]
The convergence holds for every fixed finite \(J\) and all its finitely many vectors, without a parity restriction on \(n\).

**Step 5: limiting spectrum and effectivity.** By Step 1, \(\varphi\) is eventually equivalent to \(B_\varphi(m_1,\ldots,m_J)=1\). Hence Steps 1 and 4 yield
\[
\lim_{n\to\infty}\Pr(P_{n,r}\models\varphi)=\frac{\#\{a\in\{0,\ldots,r\}^J:B_\varphi(a)=1\}}{(r+1)^J}.
\]
The numerator is computable from a finite truth table. Conversely, for each fixed \(j\) and \(0\le a\le r\), the statement “there are exactly \(a\) cycles of length \(j\)” is first-order: use a formula defining a cycle of length \(j\), existentially quantify exactly \(a\) distinct representatives not on the same cycle, and universally require every length-\(j\) cycle to meet a chosen representative (with the obvious zero case). For any fixed \(J\), conjunctions specify each full vector \(a\in\{0,\ldots,r\}^J\). Disjoining exactly \(m\) such mutually exclusive conjunctions realizes limiting probability \(m/(r+1)^J\) for every \(0\le m\le(r+1)^J\). Taking all \(J\) proves the claimed complete spectrum.

## Verification
A standalone integer-arithmetic checker, `bounded_cycles_check.py`, uses exact dynamic programming for \(\prod_{j\ge1}(1+z^j+\cdots+z^{rj})\). It compares coefficient counts with direct partition enumeration at small orders, and checks, for three caps \(r=1,2,3\), the exact finite-block identity
\[
p_r(n)=\sum_{a_1,\ldots,a_J=0}^{r}p_r^{(>J)}(n-\sum_{j=1}^Jja_j),
\]
with out-of-range coefficients interpreted as zero. It also computes exact rational joint distribution errors at \(n=480\). Its output was `BOUNDED_CYCLE_PARTITIONS_EXACT_OK 1134 finite_checks [(1, 49, 0.0151278302148033), (2, 57, 0.016065698823015284), (3, 61, 0.014859501214983098)]`. These finite checks are not a proof of the infinite asymptotic, which follows from Steps 2–4.

## Relationship to prior work
The unrestricted uniformly random unlabelled-permutation model (uniform *all* integer partitions) has a known first-order zero-one law; the bounded model gives nontrivial \((r+1)\)-adic spectra and is not a corollary of that unrestricted law, because conditioning on bounded multiplicities changes the limiting small-cycle distribution. Albert–Bouvel–Féray explain the distinction between the unary-bijection language and the two-order language for permutations. Koponen discusses conditions for first-order convergence under random expansions; Markström–Räty study permutation classes encoded by regular languages. Neither directly treats uniform isomorphism classes with bounded cycle multiplicity. Debruyne–Tenenbaum investigate general restricted-part partition asymptotics; the conditioning/local-limit argument above supplies the specific joint small-part law needed here. Corteel–Pittel–Savage–Wilf study multiplicity phenomena in unrestricted random integer partitions, a different distribution.

## Limitations
The cap \(r\) must remain fixed, and the distribution must weight isomorphism classes equally. The theorem does not concern a uniformly labelled permutation, a uniformly chosen permutation within selected conjugacy classes, growing caps, first-order logic with numerical order, or monadic second-order logic. No finite-size error rate beyond convergence is asserted. The completeness and novelty assessment is limited by the possibility that an older more general restricted-part limit theorem implies the stated joint-coordinate asymptotic, or an earlier model-theoretic classification implies the full first-order spectrum. The computational checks are finite and are not independent scientific validation.

## References
1. V. Koponen, *A characterization of the finite model property for \(\omega\)-categorical theories*, arXiv:2610.16163v1 (first public 2026-10-12).
2. K. Markström and E. Räty, *Logical isomorphism and logical limit laws for small permutation classes and regular languages*, arXiv:2610.22218v1 (first public 2026-10-15).
3. M. Albert, M. Bouvel, and V. Féray, *Two first-order logics of permutations*, arXiv:1808.05459 (2018).
4. G. Debruyne and G. Tenenbaum, *The saddle-point method for general partition functions*, arXiv:2004.05227 (2020).
5. S. Corteel, B. Pittel, C. D. Savage, and H. S. Wilf, *On the multiplicity of parts in a random partition*, Random Structures & Algorithms 14 (1999), 185–197.
