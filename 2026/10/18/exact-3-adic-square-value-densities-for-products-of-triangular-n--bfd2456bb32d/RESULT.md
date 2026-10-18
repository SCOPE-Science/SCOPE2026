# Exact \(3\)-adic square-value densities for products of triangular numbers

## Finding
Let \(T(a)=a(a+1)/2\) for \(a\in\mathbb Z_3\), and normalize Haar probability \(\mu(\mathbb Z_3)=1\). For every integer \(n\), the probability
\[
\delta_3(n)=\mu^2\{(a,b)\in\mathbb Z_3^2:T(a)T(b)+n\in\mathcal S_3\}
\]
(here \(\mathcal S_3=\{z^2:z\in\mathbb Z_3\}\) is the square-value set; the domain \(\mathbb Z_3^2\) is a Cartesian square) has the following exact evaluation:
\[
\delta_3(n)=\begin{cases}
8/9,&n\equiv1\pmod3,\\
0,&n\equiv2,5\pmod9,\\
Q((64n+1)/9)/9,&n\equiv8\pmod9,\\
1/6,&n\equiv3,6\pmod9,\\
1/6+4H(n/9)/9,&n\equiv0\pmod9.
\end{cases}
\]
Here the auxiliary rational functions \(Q\) and \(H\) are *fully explicit*, as specified below. In particular, \(\delta_3(n)=0\) if and only if \(n\equiv2,5\pmod9\). The infinite family of values is not constant even among admissible congruence classes: \(\delta_3(1)=8/9\), \(\delta_3(3)=1/6\), \(\delta_3(8)=4/81\), \(\delta_3(9)=23/54\), \(\delta_3(18)=5/18\), and \(\delta_3(0)=11/36\).

For each integer \(c\), set \(Q(c)=\mu^2\{(u,v):c-u^2-v^2\text{ is a square in }\mathbb Z_3\}\). Set \(Q(0)=1/2\). For \(c\ne0\), put \(k=v_3(c)\), and let \(\epsilon\in\{1,2\}\) be the reduction of \(c/3^k\) modulo \(3\). Then
\[
Q(c)=\begin{cases}
(1-3^{-(k+1)})/2,&k\text{ odd},\\
1/2-3^{-(k+1)},&k\text{ even and }\epsilon=1,\\
1/2,&k\text{ even and }\epsilon=2.
\end{cases}
\]
For each integer \(m\), set \(H(m)=\mu^2\{(u,v):uv+m\text{ is a square in }\mathbb Z_3\}\), and \(H(0)=5/16\). For \(m\ne0\), write \(k=v_3(m)\) and \(\epsilon\equiv m/3^k\pmod3\). Define
\[
w_j=\frac{4(j+1)}{9\cdot3^j},\qquad t_k=1-\sum_{j=0}^k w_j,
\]
and \(\beta_{k,\epsilon}=3/16\) for odd \(k\), while for even \(k\), \(\beta_{k,1}=1/16\) and \(\beta_{k,2}=9/16\). Then
\[
H(m)=\frac12\sum_{\substack{0\le j<k\\j\text{ even}}}w_j
+\mathbf1_{\{k\text{ even},\epsilon=1\}}\,t_k
+w_k\beta_{k,\epsilon}.
\]
Every displayed sum is finite, and every parameter value is therefore a rational number computed by a finite formula.

## Assumptions and scope
The parameter \(n\) is any ordinary integer (including \(0\) or negative integers). The independent variables \(a,b\) are Haar-uniform over the **\(3\)-adic integers**; positivity is not an intrinsic \(3\)-adic condition. The diagonal \(a=b\) is Haar-null, so excluding identical indices would not change the measure. The event records whether a square root exists in \(\mathbb Z_3\), *not* the number of square roots. The set \(\{z^2:z\in\mathbb Z_3\}\) contains zero. This is a local-density theorem and does **not** imply the existence or asymptotic abundance of pairs of positive integers \(a,b\) satisfying an integral square equation.

For each positive integer \(r\), let \(P_r(n)\) be the proportion of \((a,b)\bmod3^r\) for which \(T(a)T(b)+n\) is a square modulo \(3^r\). Then \(P_r(n)\) is decreasing in \(r\) and \(\lim_{r\to\infty}P_r(n)=\delta_3(n)\). Indeed, the preimages in \(\mathbb Z_3^2\) are nested clopen sets with intersection the event in the definition; compactness of \(\mathbb Z_3\) ensures that a compatible sequence of square roots exists. The congruences are well defined because \(2\) is a unit in \(\mathbb Z_3\).

## Proof
**1. Square criterion and conditional distributions.** A nonzero \(z\in\mathbb Z_3\) is a square if and only if \(v_3(z)\) is even and \(3^{-v_3(z)}z\equiv1\pmod3\). This follows by Hensel lifting of a unit square root. Haar-uniform units have each of the reductions \(1,2\pmod3\) with probability \(1/2\). For Haar-uniform \(U\in\mathbb Z_3\), \(\Pr(v_3(U)=j)=2/3^{j+1}\). Consequently, a Haar-uniform variable of \(3\mathbb Z_3\) is square with probability \(1/8\): writing it as \(3U\), its valuation must be odd before multiplication by \(3\), and its terminal unit must be \(1\pmod3\). A Haar-uniform element of \(3\mathbb Z_3\) becomes a square after multiplication by \(3\) with probability \(3/8\). Zero has measure zero in all these distributions.

The map \(a\mapsto T(a)\) has two types of residue classes modulo \(3\). On the critical class \(a\equiv1\pmod3\), the substitution \(2a+1=3A\) gives \(T(a)=(9A^2-1)/8\), where \(A\) is Haar-uniform on \(\mathbb Z_3\), and \(T(a)\equiv1\pmod9\). On each of the two regular classes \(a\equiv0,-1\pmod3\), the derivative \((2a+1)/2\) is a \(3\)-adic unit and Hensel's lemma makes \(T\) a measure-preserving bijection from that class onto \(3\mathbb Z_3\). Conditional on being regular (probability \(2/3\)), \(T(a)=3U\) with \(U\) Haar-uniform. The critical class has probability \(1/3\).

**2. Main case division.** If \(n\equiv1\pmod3\), all pairs except the doubly critical pair of classes give a unit congruent to \(1\pmod3\), whereas the doubly critical branch gives \(2\pmod3\). The measure is therefore \(8/9\).

If \(n\equiv2\pmod3\), at least one regular class makes the sum congruent \(2\pmod3\), so only the doubly critical branch can contribute. In that branch
\[
T(a)T(b)+n=\frac9{64}\{C-A^2-B^2+9A^2B^2\},\qquad C=\frac{64n+1}9,
\]
provided \(n\equiv8\pmod9\). For \(n\equiv2,5\pmod9\), instead, the doubly critical value has valuation exactly one and cannot be a square; the density is zero. For \(n\equiv8\pmod9\), the unit \(1-9A^2\) has a square root in \(\mathbb Z_3^\times\), and the change \(B'=B\sqrt{1-9A^2}\) preserves conditional Haar measure for each \(A\). Since \(9/64=(3/8)^2\), this branch contributes \(Q(C)/9\).

If \(3\mid n\), the doubly critical branch (measure \(1/9\)) is always square. The exactly-one-critical branch (measure \(4/9\)) has conditional law \(n+3U\), Haar-uniform on \(3\mathbb Z_3\), so contributes \((4/9)(1/8)=1/18\). The sum is \(1/6\). The doubly regular branch (measure \(4/9\)) has conditional law \(9UV+n\). It contributes zero when \(9\nmid n\), and \((4/9)H(n/9)\) when \(9\mid n\). This proves the displayed expression for \(\delta_3\), conditional on the two auxiliary evaluations.

**3. Evaluation of \(Q\).** Classify \(u,v\pmod3\) as zero or nonzero. If \(c\equiv1\pmod3\), the configurations with both zero contribute \(1/9\); the configurations with exactly one nonzero contribute \((4/9)(1/8)\) by the unit-derivative change of variables on that nonzero coordinate. Thus \(Q(c)=1/6\). If \(c\equiv2\pmod3\), the exactly-one-nonzero configurations contribute \(4/9\), and both nonzero contribute \((4/9)(1/8)\); thus \(Q(c)=1/2\). If \(3\mid c\) but \(9\nmid c\), exactly the both-nonzero configurations contribute, and \(Q(c)=4/9\). If \(9\mid c\), the both-nonzero branch contributes \(4/9\), and the both-zero branch reduces after division by \(9\) to the same problem, giving
\[
Q(c)=4/9+Q(c/9)/9.
\]
Iterating this recurrence to valuation zero or one yields the formula for every nonzero \(c\). For \(c=0\) it gives \(Q(0)=4/9+Q(0)/9=1/2\).

**4. Evaluation of \(H\).** Independence of \(u,v\) gives
\[
\Pr(v_3(uv)=j)=\sum_{i=0}^j\frac{2}{3^{i+1}}\frac{2}{3^{j-i+1}}=w_j.
\]
Conditionally on \(v_3(uv)=j\), the unit part of \(uv\) is Haar-uniform in \(\mathbb Z_3^\times\). Let \(k=v_3(m)\) for nonzero \(m\). If \(j<k\), squareness has probability \(1/2\) when \(j\) is even and zero otherwise. If \(j>k\), squareness holds surely exactly when \(k\) is even and the unit of \(m\) is \(1\pmod3\). When \(j=k\), the two unit parts cancel modulo \(3\) with probability \(1/2\), leaving a conditionally uniform element of \(3\mathbb Z_3\); the other half is a unit with residue fixed by the sign of \(m\). For odd \(k\), cancellation gives squareness with conditional probability \((1/2)(3/8)=3/16\). For even \(k\), cancellation contributes \((1/2)(1/8)=1/16\), and the noncancelling half contributes \(1/2\) exactly when the unit of \(m\) is \(2\pmod3\). Summing valuation shells yields \(H(m)\). For \(m=0\), a square requires even valuation of \(uv\) and a unit square, so
\[
H(0)=\frac12\sum_{j\ge0,\ j\text{ even}}w_j
=\frac29\sum_{\ell\ge0}(2\ell+1)9^{-\ell}=5/16.
\]
This completes the proof. All denominators and formulas follow from exact Haar-mass identities, not an extrapolation from computation.

## Verification
The standalone standard-library program `check_density.py` performs exact rational evaluation of \(Q,H,\delta_3\), checks nine named reference values, and compares predictions with exhaustive congruence counts for 81 parameters from \(-40\) through \(40\), for all exponents from one through five. It tests monotonic containment and agreement to within a \(1/10\) tolerance at the largest sampled modulus. It is finite supporting evidence; the proof above establishes the infinite statement. Run `python3 check_density.py`; an authentic check output is included in `certificate.txt`.

## Relationship to prior work
Bagchi and Zhou-Zheng (first publicly released August 27, 2026, arXiv:2608.27697v1) prove that integer triangular-number \(D(n)\) pairs do not exist when \(n\equiv2,5\pmod9\) and analyze solvability over local fields. Their accessible primary text does not state an all-parameter Haar density formula or the rational functions \(Q,H\). Bliznac Trebješanin (first released March 31, 2026, arXiv:2603.29565) gives a related congruence obstruction and global Pell arguments, not these densities. Gurvich and Naumova (August 8, 2025, arXiv:2508.06598v1) classify constructions with zero shift, not the \(3\)-adic distribution of square-shift values. Classical local density and \(p\)-adic integration methods are conceptual antecedents. This result refines the known local obstruction to an explicit quantitative distribution but is not asserted to be independent of all general \(p\)-adic counting theories.

## Limitations
The density counts two free \(3\)-adic indices whose product-shift **admits** a square root; it does not count triples of variables \((a,b,z)\) with equal weight and is not an unweighted ternary quadratic-form representation density. No estimates for positive integer solutions, no local-global principle, no density at primes other than three, and no uniform asymptotic count of distinct positive triangular-number pairs are claimed. Computational congruence counts do not replace the Haar-measure proof. An equivalent implicit instance of general \(p\)-adic integration formulas remains an originality risk.

## References
1. S. Bagchi and C. Zhou-Zheng, *Diophantine m-tuples of Triangular Numbers*, arXiv:2608.27697v1 (first posted August 27, 2026), https://arxiv.org/html/2608.27697v1.
2. M. Bliznac Trebješanin, *On Diophantine pairs and triples of triangular numbers*, arXiv:2603.29565 (first posted March 31, 2026), https://arxiv.org/pdf/2603.29565.
3. V. Gurvich and M. Naumova, *On pairs of triangular numbers whose product is a perfect square and pairs of intervals of successive integers with equal sums of squares*, arXiv:2508.06598v1 (first posted August 8, 2025), https://arxiv.org/html/2508.06598v1.
4. T. Yang, *An Explicit Formula for Local Densities of Quadratic Forms*, preprint (1997), https://archive.mpim-bonn.mpg.de/id/eprint/938/ (general comparison; the published statement concerns quadratic-form representation densities).
