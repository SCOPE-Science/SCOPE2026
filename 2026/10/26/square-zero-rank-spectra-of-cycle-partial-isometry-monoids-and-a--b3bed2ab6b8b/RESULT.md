# Square-zero rank spectra of cycle partial-isometry monoids and a parity-sensitive Gaussian law

## Finding

For every integer \(n\ge 3\), let \(C_n\) be the cycle with vertex set \(\mathbb Z/n\mathbb Z\), equipped with graph distance, and let \(\mathcal D_n=\operatorname{DP}(C_n)\) be the inverse monoid of all partial distance-preserving bijections. Its zero is the empty partial map. Define the square-zero rank polynomial
\[
F_n(z)=\sum_{\substack{f\in\mathcal D_n\\ f^2=0}}z^{|\operatorname{Dom}f|}.
\]
For positive integers \(d\), put
\[
J_1(z)=1,\qquad J_2(z)=1+2z,\qquad
J_d(z)=\sum_{k=0}^{\lfloor d/2\rfloor}\frac{d}{d-k}\binom{d-k}{k}z^k\quad(d\ge3).
\]
Then the following exact polynomial identity holds for every \(n\ge3\):
\[
\begin{aligned}
F_n(z)={}&\sum_{d\mid n}\varphi(d)J_d(z)^{n/d}+H_n(z)\\
&-(2n-1)-n(n-1)z-\mathbf1_{\{2\mid n\}}\frac{n(n-2)}2z^2,
\end{aligned}
\]
where \(\varphi\) is Euler's totient function and
\[
H_n(z)=\begin{cases}
n(1+2z)^{(n-1)/2},&n\text{ odd},\\
\frac n2\bigl((1+2z)^{n/2}+(1+2z)^{(n-2)/2}\bigr),&n\text{ even}.
\end{cases}
\]
In particular, the first coefficients are \([z^0]F_n(z)=1\), \([z^1]F_n(z)=n(n-1)\), and
\[
[z^2]F_n(z)=\begin{cases}
n(n-1)(n-3),&n\text{ odd},\\
\frac{n(n-2)(2n-5)}2,&n\text{ even}.
\end{cases}
\]

Writing \(s_n=F_n(1)\) and \(\beta=7^{1/4}<\sqrt3\), the square-zero counts satisfy
\[
s_n=\begin{cases}
n3^{(n-1)/2}+O(n\beta^n+n^2),&n\text{ odd},\\
(\frac{2n}{3}+1)3^{n/2}+O(n\beta^n+n^2),&n\text{ even}.
\end{cases}
\]
For an element chosen uniformly from all of \(\mathcal D_n\), the square-zero probability is asymptotic to
\[
\Pr(f^2=0)\sim\begin{cases}
\frac1{2\sqrt3}(\frac{\sqrt3}{2})^n,&n\text{ odd},\\
\frac13(\frac{\sqrt3}{2})^n,&n\text{ even}.
\end{cases}
\]
Finally, if \(R_n\) is the rank of a uniformly selected square-zero element, then
\[
\frac{R_n-n/3}{\sqrt n/3}\ \xrightarrow{\mathrm d}\ \mathcal N(0,1),
\qquad \frac{R_n}{n}\xrightarrow{\mathbb P}\frac13.
\]
This is a full finite-rank classification together with parity-dependent exponential rarity and a Gaussian support law.

## Assumptions and scope

A partial map \(f:A\to B\) is a partial isometry when it is distance preserving on its domain \(A\subseteq\mathbb Z/n\mathbb Z\). Such maps are injective. Composition is ordinary partial-map composition, and \(0\) is the empty map. The graph is a simple cycle, including \(n=3\). No restrictions on the parity or primality of \(n\) are imposed. The probability statement samples uniformly from individual partial maps, not from choices of global dihedral extensions. The index-two nilpotence event \(f^2=0\) is also understood to contain the zero map itself.

## Proof

**1. Reduction to disjoint support.** For any injective partial transformation \(f:A\to B\), the domain of \(f^2\) is \(\{a\in A:f(a)\in A\}\). Thus \(f^2=0\) if and only if \(A\cap B=\varnothing\). In particular, \(\operatorname{rank}(f)\le\lfloor n/2\rfloor\).

**2. Dihedral extensions and multiplicities.** The finite-cycle partial-isometry theorem of Fernandes and Paulista identifies \(\mathcal D_n\) with all restrictions of the dihedral group \(D_{2n}\) acting by \(x\mapsto \epsilon x+b\pmod n\), where \(\epsilon\in\{1,-1\}\) and \(b\in\mathbb Z/n\mathbb Z\) [1, Lemma 1.1]. Two distinct dihedral permutations agree on at most two vertices. Indeed their quotient is a nonidentity rotation (with no fixed point) or reflection (with at most two fixed points); two fixed points occur only when \(n\) is even and the points are antipodal. It follows that every restriction of rank at least three has a unique extension. Every nonempty rank-one restriction has exactly two extensions, and a rank-two restriction has two extensions precisely when its domain is an antipodal pair in an even cycle; otherwise its extension is unique [1, Lemma 1.1]. The empty restriction has \(2n\) extensions.

Among square-zero restrictions, rank one contributes \(n(n-1)\) distinct maps, and all these maps are double-counted by global extensions. For even \(n\), an antipodal rank-two domain can be chosen in \(n/2\) ways. Its image must be a disjoint antipodal pair, available in \(n/2-1\) ways, and there are two bijections between the chosen pairs. Thus the number of doubled square-zero rank-two restrictions is \(2(n/2)(n/2-1)=n(n-2)/2\). These are the only duplication corrections.

**3. Counting independent domains for each extension.** Fix \(g\in D_{2n}\). A restriction \(g|_A\) has square zero exactly when \(A\cap g(A)=\varnothing\). On each orbit of \(g\), occupied vertices therefore form an independent set in the cyclic adjacency relation defined by the permutation. A fixed-point orbit contributes \(1\), a two-cycle contributes \(1+2z\), and an orbit of length \(d\ge3\) contributes the ordinary cycle independence polynomial \(J_d(z)\). To verify its displayed coefficients, select \(k\) nonadjacent vertices of a labelled \(d\)-cycle: their positive circular gaps have total \(d\) and each gap is at least two, giving \(\frac d{d-k}\binom{d-k}{k}\) possibilities.

For rotations of order \(d\mid n\), there are \(\varphi(d)\) permutations, each with \(n/d\) orbits of length \(d\). This gives the divisor sum. An odd cycle has \(n\) reflections, each with one fixed vertex and \((n-1)/2\) transpositions. An even cycle has \(n/2\) reflections with no fixed vertices and \(n/2\) reflections with two fixed vertices. These give \(H_n(z)\). Subtracting the duplicate restrictions counted in step 2 proves the exact formula. The first coefficients also follow directly by counting ordered distance-preserving maps between disjoint one- or two-element subsets.

**4. Exponential asymptotics.** Put \(\lambda=(1+\sqrt5)/2\). For a cycle of length \(d\ge3\), its independence-set count at \(z=1\) is the Lucas number \(L_d=\lambda^d+(-\lambda^{-1})^d\). For odd \(d\), this is less than \(\lambda^d\). For even \(d\ge4\), the quantity \((\lambda^d+\lambda^{-d})^{1/d}\) decreases with \(d\) (because \(\log(1+\lambda^{-2d})/d\) decreases), so its maximum is \(L_4^{1/4}=7^{1/4}=\beta\). Consequently all rotations except the identity and, when \(n\) is even, the unique half-turn contribute together at most \(n\beta^n\) restrictions. The identity contributes only the empty domain; the half-turn contributes \(3^{n/2}\). Reflections contribute exactly \(n3^{(n-1)/2}\) for odd \(n\) and \(\frac{2n}{3}3^{n/2}\) for even \(n\). The low-rank duplication corrections are \(O(n^2)\), giving the two asymptotic formulas.

The known cardinality of the underlying monoid is \(|\mathcal D_n|=n2^{n+1}-\frac{(-1)^n+5}{4}n^2-2n+1\) [1, Theorem 1.4]. Dividing the just-proved estimates for \(s_n\) by \(|\mathcal D_n|\sim 2n2^n\) gives the parity-sensitive probability constants.

**5. Gaussian rank law.** The number of non-reflection extension pairs yielding square-zero elements is negligible compared with the reflection contribution, since \(\beta<\sqrt3\); the even half-turn is also smaller than the reflection contribution by a factor of order \(n^{-1}\). Low-rank multiplicity corrections are negligible for the same reason. Conditional on a fixed reflection with \(t\) transposition orbits, the square-zero rank of its restriction is exactly \(\operatorname{Binomial}(t,2/3)\): for each orbit choose neither point (weight \(1\)) or either one point (weight \(2z\)). For odd \(n\), \(t=(n-1)/2\). For even \(n\), \(t\) equals \(n/2\) or \((n-2)/2\), with weights proportional to \(3^t\). In both cases \(2t/3=n/3+O(1)\) and \(2t/9=n/9+O(1)\), and the classical binomial central limit theorem gives the displayed normal law. Total-variation comparison with the exact finite population is justified by the vanishing proportion of all non-reflection and multiply represented restrictions.

## Verification

The independently implemented checker `cycle_square_zero_checker.py` enumerates all disjoint-domain/image partial bijections directly, retaining only those preserving the graph-geodesic distance. It does not assume that every partial isometry extends to a dihedral permutation. For every \(3\le n\le12\), it compares all coefficients of this direct count with the separate closed-form polynomial implementation; the tests cover \(4{,}447{,}144\) candidate maps. The rank coefficients for \(n=8\) are \((1,56,264,288,96)\), summing to \(705\). The checker also evaluates selected larger cases as numerical consistency checks for the asymptotic formulas. Run with `python3 cycle_square_zero_checker.py`; no third-party packages are needed. Finite verification is not used as a substitute for the general proof.

## Relationship to prior work

Fernandes and Paulista [1] prove the dihedral restriction theorem, the extension multiplicities, and the total cardinality and generators of \(\mathcal D_n\); these foundational results are explicitly credited. The present theorem additionally imposes the algebraic zero-square constraint, classifies its full rank distribution, and derives a parity-sensitive rarity law and a Gaussian limit. Their complete accessible article was examined, including Lemma 1.1, Theorems 1.4 and 1.5, and the presentation section; it does not state these square-zero statistics.

Gomes and Howie [2] study nilpotent elements in the full symmetric inverse semigroup and prove a decomposition into nilpotent paths. The cycle-isometry submonoid is a proper constrained family: the counts above require a dihedral-orbit independence analysis and a correction for multiple global extensions. Cain, Malheiro and Paulista [3] study maximal commutative nilpotent subsemigroups of full transformation semigroups, not the elementwise square-zero rank distribution of cycle partial isometries. Dimitrova, Fernandes, Koppitz and Quinteiro [4] investigate three orientation/order-constrained submonoids of the dihedral inverse monoid, including their cardinalities and Green's relations, but not the asserted zero-square polynomial. Independence polynomials, Lucas numbers and the binomial central limit theorem are established tools and are not claimed as discoveries.

## Limitations

The count concerns exactly the equation \(f^2=0\); it does not classify higher nilpotency indices or square-zero subsemigroups. The probability is uniform over elements of \(\mathcal D_n\), and the asymptotics take \(n\to\infty\) along either parity. The first formula is exact for all \(n\ge3\), but the Gaussian theorem is asymptotic only. The available searches and inspected principal literature do not establish a prior equivalent theorem; this is not a proof of global historical priority. The full dissertation *Partial Isometries of Some Simple Connected Graphs* (2022) was not accessible, leaving an identifiable residual priority risk. Independent expert validation has not been performed.

## References

[1] V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a cycle graph*, arXiv:2205.02196, first posted 2022-05-04; Turkish Journal of Mathematics 47 (2023), 1746–1760. https://arxiv.org/abs/2205.02196

[2] G. M. S. Gomes and J. M. Howie, *Nilpotents in finite symmetric inverse semigroups*, Proceedings of the Edinburgh Mathematical Society 30 (1987), 383–395. https://doi.org/10.1017/S0013091500026778

[3] A. J. Cain, A. Malheiro and T. Paulista, *Commutative nilpotent transformation semigroups*, arXiv:2310.08481, first posted 2023-10-12; Semigroup Forum 109 (2024), 60–75. https://arxiv.org/abs/2310.08481

[4] I. Dimitrova, V. H. Fernandes, J. Koppitz and T. M. Quinteiro, *On three submonoids of the dihedral inverse monoid on a finite set*, arXiv:2301.01519, first posted 2023-01-04. https://arxiv.org/pdf/2301.01519
