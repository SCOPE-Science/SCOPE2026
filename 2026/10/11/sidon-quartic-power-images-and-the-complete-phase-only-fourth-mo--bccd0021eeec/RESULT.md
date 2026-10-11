# Sidon quartic-power images and the complete phase-only fourth-moment equality groups

## Finding
For each prime \(p\ge5\), put \(H_p=\{t^4:t\in\mathbb F_p\}\). The set \(H_p\) has the Sidon property (each sum of two elements determines their unordered pair, including repeated elements) **if and only if** \(p\in\{5,13\}\).

For either of these two primes, fix \(\zeta_p=\exp(2\pi i/p)\), and define
\[
\mathcal E_p f(x,y)=p^{-1}\sum_{t\in\mathbb F_p}f(t)\zeta_p^{xt+yt^4},\qquad x,y\in\mathbb F_p.
\]
For every function \(f:\mathbb F_p\to\mathbb C\) satisfying \(|f(t)|=1\) at every point,
\[
\sum_{x,y\in\mathbb F_p}|\mathcal E_p f(x,y)|^4\le
\begin{cases}69/25,&p=5,\\445/169,&p=13.\end{cases}
\]
Both constants are attained. Equality holds **exactly** for
\[
 f(t)=\zeta_p^{At}u_{t^4},\qquad A\in\mathbb F_p,\quad (u_h)_{h\in H_p}\in\mathbb T^{H_p},\quad\mathbb T=\{z\in\mathbb C:|z|=1\}.
\]
The equality space has precisely \(p\) connected components, each a torus of real dimension \(|H_p|\): five two-tori for \(p=5\), and thirteen four-tori for \(p=13\). In particular, its phases need not be restrictions of additive characters of the two-coordinate quartic graph.

## Assumptions and scope
The theorem concerns prime fields of characteristic at least five, the graph \(\{(t,t^4):t\in\mathbb F_p\}\), counting measure on the output plane, and **unit-modulus inputs only**. The Sidon assertion concerns the distinct fourth-power values, including zero, rather than the parametrized graph itself. The sharp bound is not asserted to be the unrestricted \(L^2\)-to-\(L^4\) operator norm, and equality is not classified for primes outside \(\{5,13\}\).

## Proof
**1. Exactly two Sidon primes.** Let \(d=\gcd(4,p-1)\). Cyclicity of \(\mathbb F_p^\times\) gives \(|H_p|=1+(p-1)/d\). A Sidon subset \(H\subset\mathbb F_p\) of cardinality \(m\) has \(m(m+1)/2\) distinct unordered two-element sums, so \(m(m+1)/2\le p\). If \(p\equiv3\pmod4\), then \(d=2\), and this inequality forces \((p+1)(p+3)\le8p\), or \(p\le3\), a contradiction. If \(p\equiv1\pmod4\), then \(d=4\), and the inequality forces \((p+3)(p+7)\le32p\), equivalently \(p\le21\). The only candidate primes \(p\ge5\) are \(5,13,17\). The fourth-power images are \(H_5=\{0,1\}\), \(H_{13}=\{0,1,3,9\}\), and \(H_{17}=\{0,1,4,13,16\}\). The unordered sums in \(H_{13}\) are \(0,1,2,3,4,5,6,9,10,12\), all different; the three sums in \(H_5\) are \(0,1,2\). In \(H_{17}\), the three pairs \(\{0,0\},\{1,16\},\{4,13\}\) all sum to zero. This proves the claimed arithmetic criterion.

**2. Moment bound and candidate phases.** For \(s,v\in\mathbb F_p\), write
\[
R_{s,v}=\{(a,b)\in\mathbb F_p^2:a+b=s,\ a^4+b^4=v\},\qquad r_{s,v}=|R_{s,v}|.
\]
Character orthogonality gives the exact identity
\[
\sum_{x,y}|\mathcal E_p f(x,y)|^4=p^{-2}\sum_{s,v}\Big|\sum_{(a,b)\in R_{s,v}}f(a)f(b)\Big|^2.
\]
For \(|f|=1\), the triangle inequality bounds the right side by \(p^{-2}\sum_{s,v}r_{s,v}^2\); equality holds precisely when \(f(a)f(b)\) is constant on every nonempty fiber. Direct integer counting of the two finite fields gives, respectively, the histograms \(\#\{(s,v):r_{s,v}=r\}\): for \(p=5\), \(r=1,2,3,4\) occurs \(1,4,4,1\) times; for \(p=13\), \(r=1,2,4\) occurs \(13,48,15\) times. Thus the respective numerator energies are \(69\) and \(445\). The counts can be independently reconstructed by the explicit double loop in `checker.py`.

For \(p\in\{5,13\}\), the Sidon property ensures that fixed \(v=a^4+b^4\) determines the unordered multiset \(\{a^4,b^4\}\). Hence every input \(f(t)=\zeta_p^{At}u_{t^4}\) has fiber product \(\zeta_p^{As}u_{a^4}u_{b^4}\), independent of the pair inside \(R_{s,v}\), and attains the upper bound.

**3. Exhaustion of equality phases.** All fibers and their pair products define an integer relation matrix \(M_p\): for each two unordered pairs \(\{a,b\}\) and \(\{c,d\}\) in the same fiber, add the row \(e_a+e_b-e_c-e_d\), omitting one redundant reference pair per fiber. Since a pair product is commutative, the phase-equality group is exactly the annihilator of the row lattice of \(M_p\) in \(\mathbb T^p\). For \(p=5\) there are five rows; for \(p=13\) there are fifteen.

The \(|H_p|\) integer vectors \(1_{\{t:t^4=h\}}\), one for each \(h\in H_p\), are linearly independent and annihilated by \(M_p\): this follows directly from the Sidon condition. Thus the rational rank of \(M_p\) is at most \(p-|H_p|\). Modulo \(p\), the vector with entry \(t\) at coordinate \(t\) is another null vector, because every relation preserves the first-coordinate sum. It is independent of the quartic-class indicators: the entries at \(t=1\) and \(t=-1\) differ. Consequently the rank of \(M_p\) modulo \(p\) is at most \(p-|H_p|-1\), and every maximal-size nonzero minor is divisible by \(p\).

For completeness, the following explicit minors establish the matching rational rank and the *exact* gcd of maximal-rank minors. Index columns by field elements \(0,\ldots,p-1\); for a displayed pair equality \((c,d)\sim(a,b)\), use the row \(e_a+e_b-e_c-e_d\). For \(p=5\), use the three rows \((1,1)\sim(3,4)\), \((1,2)\sim(4,4)\), \((1,3)\sim(2,2)\), restricted to columns \((1,2,3)\): their determinant is \(-5\). For \(p=13\), use the nine rows
\[
\begin{gathered}
(1,7)\sim(9,12),\ (1,10)\sim(3,8),\ (1,12)\sim(5,8),\\
(2,7)\sim(3,6),\ (2,8)\sim(11,12),\ (2,11)\sim(3,10),\\
(3,4)\sim(9,11),\ (4,9)\sim(6,7),\ (5,9)\sim(6,8),
\end{gathered}
\]
restricted to columns \((1,2,3,6,7,8,9,11,12)\): their determinant is \(-13\). Every displayed equality can be verified directly in \(\mathbb F_p^2\) by summing the two corresponding quartic-graph points.

Therefore the rational rank is exactly \(p-|H_p|\), while the gcd of the full-rank minors is exactly \(p\). The elementary integer Smith-normal-form theorem now identifies the phase-equality group as \(\mathbb T^{|H_p|}\times\mathbb Z/p\mathbb Z\). The displayed candidate family consists of \(p\) disjoint translates of the \(|H_p|\)-dimensional connected torus of functions constant on fourth-power classes: disjointness follows by comparing \(t=1\) and \(t=-1\), which share their fourth power. Since this contained family has the same connected dimension and number of components as the full equality group, it equals the full equality group. This completes the proof.

## Verification
Run `python3 checker.py` from the directory containing this file. This standard-library checker enumerates all ordered and unordered two-sum fibers, independently verifies the power-class sets and Sidon sums, recomputes the exact energy histograms, tests the claimed phase-preservation identities, constructs the full relation matrices, evaluates both displayed determinants using exact rational arithmetic, and computes their modular ranks. Expected final line: `CHECK_PASS`. The small finite enumerations and determinants are exhaustive certificates of the stated finite cases; the argument excluding all other primes and the equality-group deduction are mathematical proofs and do not rely on extrapolation.

## Relationship to prior work
González-Riquelme and Oliveira e Silva develop sharp Fourier extension theory on finite-field paraboloids, parabolas, hyperbolic paraboloids, and cones. Their finite-field extension framework motivates phase equality questions but does not treat the graph \((t,t^4)\). The public calculation *Exact additive energy of the finite-field quartic graph* supplies the exact constant-input fourth moment in all characteristics above three; the present statement agrees with its numerical values at \(p=5,13\), but goes further by determining the full **unimodular** maximizing phase group and characterizing exactly when fourth-power images are Sidon. Biswas and Stovall study monomial-curve restriction over the reals with affine arclength measure, rather than finite-field phase-only Fourier moments. The present theorem makes no claim about the unrestricted operator norm.

## Limitations
The result is specific to the two exceptional Sidon primes and to equal-magnitude coefficients, and it does not determine phase extrema over every prime. It does not identify maximizers with unrestricted coefficient magnitudes. Although the closest inspected work does not imply the phase classification, an older equivalent result in finite-group relation lattices, multiplicative-subgroup Sidon sets, or polyphase Fourier analysis could remain unindexed.

## References
1. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v1 (first posted 2024-05-26), especially §1 and the convolution/equality framework.
2. *Exact additive energy of the finite-field quartic graph*, publicly available published-finding corpus mathematical record (2026); exact two-sum energy formula and its limitation to constant input.
3. C. Biswas and B. Stovall, *Sharp Fourier restriction to monomial curves*, arXiv:2302.05317v1 (2023); Euclidean affine-arclength setting.
