# Polylogarithmic star counts and the zero–one law for uniform finite retractions

## Finding
For every integer \(n\geq1\), choose uniformly one of all functions \(f:[n]\to[n]\) with \(f\circ f=f\). A *root* is a fixed point; a root has \(s\) leaves if precisely \(s\) other elements map to it. Let \(C_s(n)\) count roots with \(s\) leaves.

**Theorem.** For every fixed integer \(s\geq0\),
\[
\frac{C_s(n)}{(\log n)^{s+1}}\xrightarrow{\mathsf P}\frac{1}{s!}\qquad(n\to\infty).
\]
Convergence holds jointly for any fixed finite collection of \(s\). For the pure first-order language with the single unary function symbol \(f\), the sequence of uniform finite idempotent-function structures has a **zero–one law**. Its almost-sure complete theory \(T\) is axiomatized by \(f(f(x))=f(x)\), together with, for every \(s\geq0\) and \(q\geq1\), the sentence asserting at least \(q\) distinct roots having exactly \(s\) leaves. This complete theory has the finite model property but is **not \(\omega\)-categorical**.

The theorem also has a finite exact moment form: if \(I_n\) is the number of idempotent maps on \([n]\), then for integers \(s\geq0\), \(j\geq1\), and \(j(s+1)\le n\),
\[
I_n\,\mathbb E[(C_s(n))_j]=\frac{(n)_{j(s+1)}}{(s!)^j}I_{n-j(s+1)}.
\]
Here \((a)_j\) denotes the falling factorial and \(I_0=1\).

## Assumptions and scope
Uniformity means uniform over all *labelled* idempotent self-maps, not uniform over integer partitions, unlabelled star forests, or maps with a prescribed number of fixed points. All \(s,q\) in the asymptotic assertions are fixed as \(n\to\infty\). A leaf is a nonfixed preimage; every connected component is one star with its root and any number of leaves. We use natural logarithms. We make no assertion of a uniform estimate for \(s\) growing with \(n\).

## Proof
**1. Finite decomposition and factorial moments.** An idempotent map with \(k\ge1\) roots is specified by choosing its \(k\) fixed points and independently choosing, for each of the remaining \(n-k\) points, one of those \(k\) roots. Thus
\[
I_n=\sum_{k=1}^n\binom nk k^{n-k},\qquad I_0=1,
\]
and the exponential generating function is \(\sum_{n\ge0}I_n z^n/n!=\exp(ze^z)\). To count an *ordered* \(j\)-tuple of distinct components each having \(s+1\) points, choose disjoint labelled \((s+1)\)-element sets in order and designate one root in each; then give the complement any idempotent map. This contributes \((n)_{j(s+1)}I_{n-j(s+1)}/(s!)^j\), proving the stated factorial-moment identity.

**2. Concentration of the root count.** Let \(K_n\) be the number of roots. Put \(w_n(k)=\binom nk k^{n-k}\), so \(\Pr(K_n=k)=w_n(k)/I_n\). The exact adjacent ratio is
\[
R_n(k):=\frac{w_n(k+1)}{w_n(k)}=
\frac{n-k}{(k+1)^2}\left(1+\frac1k\right)^{n-k}
\quad(1\le k<n).
\]
Both \(\binom nk\) and \(k^{n-k}\) are log-concave in the integer variable \(k\): for the second factor, the continuous logarithm \((n-k)\log k\) has strictly negative second derivative \(-(n+k)/k^2\). Hence \(R_n(k)\) is decreasing in \(k\).

Let \(r_n>0\) solve \(r_n+2\log r_n=\log n+1\). It is unique, and \(r_n\sim\log n\). Uniformly for \(r=n/k=r_n+o(1)\), direct expansion of the exact ratio gives
\[
\log R_n(k)=r+2\log r-\log n-1+O(r^{-1}+r^2/n).
\]
In particular, at \(k_-=\lfloor n/(r_n+r_n^{-1/2})\rfloor\) and \(k_+=\lceil n/(r_n-r_n^{-1/2})\rceil\), the logarithms of the respective ratios have opposite signs and magnitudes asymptotic to \(r_n^{-1/2}\). Monotonicity bounds each exterior tail by a geometric series. Relative to the weight near \(k_0=\lfloor n/r_n\rfloor\), the logarithms of the exterior boundary weights are smaller by at least a constant times \(n/r_n^3\), since on an interior interval of length of order \(n/r_n^{5/2}\) the log-ratio has magnitude of order \(r_n^{-1/2}\). As \(n/r_n^3\to\infty\), both tails have probability tending to zero. Therefore
\[
\frac{n}{K_n}=r_n+o_{\mathsf P}(1).
\]
The statement follows directly even if the maximizing integer lies next to \(k_0\); the comparison uses only weights and log-concavity.

**3. Conditional small-component concentration.** Conditional on \(K_n=k\), put \(m=n-k\). Each of the \(m\) leaves independently chooses one of the \(k\) roots. For fixed \(s\), the exact first and second conditional factorial moments are
\[
\mathbb E[C_s\mid K_n=k]
=k\binom ms k^{-s}(1-1/k)^{m-s},
\]
\[
\mathbb E[(C_s)_2\mid K_n=k]
=(k)_2\frac{(m)_{2s}}{(s!)^2k^{2s}}(1-2/k)^{m-2s},
\]
where the second formula is used only when \(m\ge2s\). On the high-probability window from step 2, the elementary expansions are uniform. Writing \(r=n/k=r_n+o(1)\), they imply
\[
\mathbb E[C_s\mid K_n=k]
=\frac{k r^s}{s!}e^{-(r-1)}(1+o(1))
=\frac{r_n^{s+1}}{s!}(1+o(1)),
\]
since \(e^{-(r_n-1)}=r_n^2/n\). The second factorial moment divided by the square of the first is \(1+O(r_n^2/n)\). Hence, uniformly in that window,
\[
\frac{\operatorname{Var}(C_s\mid K_n=k)}{\mathbb E[C_s\mid K_n=k]^2}
=O(r_n^2/n)+O(r_n^{-(s+1)})=o(1).
\]
Conditional Chebyshev, followed by the concentration of \(K_n\), proves \(C_s(n)/r_n^{s+1}\to1/s!\) in probability. Since \(r_n\sim\log n\), the claimed normalizer follows. A finite union bound gives joint convergence for finitely many fixed indices.

**4. Complete first-order limit theory.** Let \(T\) be the idempotency axiom plus the above unlimited multiplicity axioms for each finite star size. It is consistent, witnessed by a countable disjoint union of infinitely many stars of each finite size. To see completeness, fix an Ehrenfeucht–Fraïssé game of \(q\) rounds between any two models of \(T\). Maintain a partial isomorphism respecting all selected roots and their selected leaves. When Spoiler chooses a point in an already represented component, Duplicator chooses an unused matching leaf if necessary. When Spoiler enters a new component, the strategy selects a new root: if that component has fewer than \(q\) leaves, match its exact finite leaf number, and otherwise select an unused root with exactly \(q\) leaves. There are infinitely many components of every prescribed finite size in both models, and at most \(q\) pebbles are ever placed, so choices are possible. This strategy is symmetric, preserves every atomic equality and application of \(f\), and establishes elementary equivalence of all models of \(T\). For any sentence \(\varphi\), completeness implies \(T\models\varphi\) or \(T\models\neg\varphi\). By compactness, a finite collection of multiplicity axioms entails the selected consequence, and each such finite collection holds in \(F_n\) with probability tending to one by step 3. Thus its probability tends to \(1\) or \(0\), respectively.

Every finite collection of the axioms has a finite star-union model, so every consequence of \(T\) has some finite model: \(T\) has the finite model property. Finally, the infinitely many distinct one-variable formulas saying “this root has exactly \(s\) leaves” define disjoint nonempty unary types, so \(T\) is not \(\omega\)-categorical (equivalently, it has infinitely many root 1-types).

## Verification
The accompanying `verify_idempotent.py` independently enumerates all maps on \(1\) through \(6\) labelled points, selects idempotents by direct evaluation, and compares both first and second factorial moments of every small-star count against the independent combinatorial formula. The totals are \(1,3,10,41,196,1057\). Successful executable output ends in `IDEMPOTENT_STAR_MOMENTS_OK`. These checks corroborate exact finite formulas; the tail and variance estimates and the EF argument above supply the proofs for arbitrary \(n\).

## Relationship to prior work
Koponen (2026), Example 2.2, identifies bounded-height, bounded-parent DAG classes and analyzes finite-model properties of \(\omega\)-categorical theories and possible convergence-law bases. The height-one, one-parent class (with edges oriented from root to leaf) is the present finite-star class, but that deterministic framework supplies neither the uniform labelled star-count normalizer nor the specified non-\(\omega\)-categorical almost-sure theory. Harris and Schoenfeld (1967) studied enumeration of idempotent transformations; the elementary total-count formula is not new. General work of Compton on component distributions and logical zero–one laws provides a relevant potential general route to portions of the conclusion. Random-mapping component-count results for unrestricted maps or permutations are not identical measures to uniform idempotent maps.

## Limitations
The asymptotic count is pointwise in each fixed leaf count \(s\), not uniform for \(s\to\infty\). No convergence rate for arbitrary first-order sentences is claimed. Independent mathematical audit and absolute historical-priority verification have not been performed. Accessible bibliographic evidence for Harris–Schoenfeld and Compton was compared, but their complete primary texts were not available; broader historical assembly theorems might subsume individual components of this statement.

## References
1. Vera Koponen, *A characterization of the finite model property for ω-categorical theories*, arXiv:2610.16163v1 (first public 2026-10-12), https://arxiv.org/html/2610.16163v1, especially §2, Example 2.2.
2. B. Harris and L. Schoenfeld, *The number of idempotent elements in symmetric semigroups*, Journal of Combinatorial Theory 3 (1967), 122–135, https://doi.org/10.1016/S0021-9800(67)80002-4.
3. K. J. Compton, *Some methods for computing component distribution probabilities in relational structures* (1987), https://deepblue.lib.umich.edu/handle/2027.42/26614.
4. A. N. Timashev, *Random Mappings of Finite Sets with a Known Number of Components*, https://doi.org/10.1137/S0040585X97980798 (for a distinct random-mapping measure).
