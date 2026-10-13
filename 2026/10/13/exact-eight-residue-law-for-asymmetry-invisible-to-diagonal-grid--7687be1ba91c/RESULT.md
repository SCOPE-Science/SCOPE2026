# Exact eight-residue law for asymmetry invisible to diagonal-grid independence

## Finding
For each integer \(n\ge2\), let \(\mathcal P_n\) be the class of nonnegative \(n\times n\) arrays \(P=(p_{ab})\) satisfying
\[
 \sum_{b=1}^n p_{ab}=\sum_{a=1}^n p_{ab}=\frac1n,
 \qquad \sum_{a,b=1}^k p_{ab}=\frac{k^2}{n^2}\quad(0\le k\le n).
\]
Thus the two marginals are uniform on \(n\) bins and all *diagonal* grid cumulative probabilities agree exactly with independence. Let \(C_P(i/n,j/n)=\sum_{a\le i,b\le j}p_{ab}\), and define
\[
 A_n(P)=\max_{0\le i<j\le n}\left|C_P(i/n,j/n)-C_P(j/n,i/n)\right|.
\]
Write \(n=8q+r\) with \(0\le r<8\). Then the exact maximum is
\[
 \max_{P\in\mathcal P_n}A_n(P)=\frac{S_n}{n^2},\qquad
 S_n=15q^2+a_rq+b_r,
\]
where the pairs \((a_r,b_r)\), in order \(r=0,1,\ldots,7\), are
\[
 (0,0),(3,0),(6,0),(11,2),(14,3),(17,5),(22,8),(25,10).
\]
A single admissible array attains the *individual sharp oriented asymmetry bound at every grid pair* \(i<j\) simultaneously. Moreover,
\[
 \max_{P\in\mathcal P_n}A_n(P)=\frac{15}{64}\quad\Longleftrightarrow\quad 8\mid n,
 \qquad \lim_{n\to\infty}\max_{P\in\mathcal P_n}A_n(P)=\frac{15}{64}.
\]
For example the sharp values at grid sizes \(3,4,5,8,11\) are respectively \(2/9,3/16,1/5,15/64,28/121\).

## Assumptions and scope
Every array entry is a probability, including possible zeros; strict positivity or smoothness is *not* assumed. The statistic compares copula cumulative probabilities at grid points, not arbitrary interior points. Only the \(n+1\) diagonal knot values are constrained: no assertion is made that the checkerboard copula has the entire diagonal \(t\mapsto t^2\). Independent uniform marginals do not imply a symmetric joint law. Primary classification is MSC2020 62H05.

## Proof
**1. Universal finite-grid envelope.** Put \(h_k=k(n-k)\). Bilinear interpolation of the array defines a checkerboard copula \(C\), whose diagonal deficit \(h(t)=t-C(t,t)\) is 1-Lipschitz with \(h(k/n)=h_k/n^2\). For \(0\le i<j\le n\), set \(H_{ij}=\max_{i\le k\le j}h_k\). Proposition 3.1 of Kokol Bukovšek–Mojškerc–Stopar [1] bounds the upper-triangle value by
\[
 C(i/n,j/n)\le\min\left\{i/n,\;j/n-\frac{h(i/n)+h(j/n)+\operatorname{TV}_{[i/n,j/n]}h}{2}\right\}.
\]
The variation exceeds the sum of successive knot variations. The integer sequence \(h_k\) is unimodal, hence this sum is \((2H_{ij}-h_i-h_j)/n^2\). It follows that
\[
 C(i/n,j/n)\le\frac{1}{n^2}\min\{ni,nj-H_{ij}\}.
\]
The Bertino lower envelope [1, Theorem 2.6(ii)] is valid for any copula with its own diagonal. On this interval, the diagonal deficit has minimum no greater than \(\min(h_i,h_j)/n^2\); alternatively the elementary marginal/rectangle inequalities give
\[
 C(j/n,i/n)\ge\frac{ni-\min(h_i,h_j)}{n^2}.
\]
Combining yields the *exact pointwise candidate*
\[
 C(i/n,j/n)-C(j/n,i/n)\le\frac{F_{ij}}{n^2},\qquad
 F_{ij}=\min(h_i,h_j)-\max\{0,H_{ij}-n(j-i)\}.
\]
The same bound applies to the absolute difference after transposition.

**2. Simultaneous attainment under only the knot constraints.** Let \(\delta_n\) linearly interpolate \(\delta_n(k/n)=(k/n)^2\) between neighboring knots. Its slopes are \((2k+1)/n\), lie in \([0,2]\), and \(\delta_n(t)\le t\), so the standard diagonal characterization [1, Proposition 2.3] makes \(\delta_n\) an admissible full diagonal. Its deficit \(t-\delta_n(t)\) is unimodal and linear between knots. Thus the total-variation bound in step 1 is exact at every grid pair, and the deficit minimum is an endpoint value. The maximal upper-triangle copula with diagonal \(\delta_n\), spliced below the diagonal to the Bertino lower copula, is itself a copula by [1, Theorem 3.6 and Proposition 4.3]. It realizes the upper and lower envelopes simultaneously at every pair. Assign its mass on each of the \(n^2\) grid cells to an entry of \(P^*\). Uniform marginals, the stipulated diagonal prefixes, and
\[
 C_{P^*}(i/n,j/n)-C_{P^*}(j/n,i/n)=F_{ij}/n^2\qquad(i<j)
\]
all follow. No gridwise construction depends on a choice of \((i,j)\).

**3. Optimize all grid pairs.** Fix the spacing \(d=j-i\). By symmetry of \(h_k\) about \(n/2\), moving an interval contained on one side of the center toward the center cannot decrease \(F_{ij}\): on the increasing side it is exactly \(\min\{h_i,d(i+j)\}\). When the interval straddles the center, \(H_{ij}=H_n=\lfloor n^2/4\rfloor\), independent of its placement. Centering the endpoints maximizes \(\min(h_i,h_j)\) and hence \(F_{ij}\). Therefore the best integer value at each spacing is
\[
 G_n(d)=\frac{n^2-L_{n,d}^2}{4}-\max\{0,H_n-nd\},\qquad
 L_{n,d}=d+((n-d)\bmod2),
\]
where \(1\le d\le n-1\), and the first term is an integer because \(L_{n,d}\) has the parity of \(n\). For \(d\le H_n/n\) the penalty is active and consecutive values of \(G_n(d)\) increase: the first term falls by either zero or \(d+1<n\), while the negative penalty improves by \(n\). For \(d\ge H_n/n\) the penalty vanishes and the first term is nonincreasing. Thus only the nearest admissible integers to \(H_n/n\) can maximize \(G_n\). Direct substitution for \(n\bmod8\), comparing those at most two candidates, gives the eight pairs displayed in the finding. (When the lower candidate is zero, only spacing one is admissible.) These expressions are strictly smaller than \(15n^2/64\) in all nonzero residue classes, equal to it when \(8\mid n\), and have leading coefficient \(15/64\). This proves the theorem. \(\square\)

## Verification
The self-contained file `verify.py` uses integer arithmetic exclusively for the decisive checks. It validates complete grid-pair envelopes and the residue law for each \(2\le n\le95\), the closed centered-spacing expression for several larger \(n\), and literal nonnegative feasible integer matrices at \(n=3\) and \(n=8\) after scaling every entry by \(n^2\). It checks their row/column sums, every diagonal prefix, and actual attained asymmetry. These finite checks are diagnostics; the universal result follows from the preceding analytic envelope, attainment theorem, and integer maximization.

## Relationship to prior work
Kokol Bukovšek, Mojškerc and Stopar [1] solve the *fully specified continuous diagonal* extremal-copula problem and give \(15/64\) for the exact independence diagonal \(\delta(t)=t^2\) (Example 4.11). The present finite-grid law concerns **strictly weaker information** (only the diagonal knots), gives an integer-size-dependent sharp objective, establishes the eight-residue oscillation and a simultaneous finite-matrix extremizer. Its proof explicitly uses [1]'s upper envelope and diagonal splice, rather than claiming those general tools as new. Perrone, Solus and Uhler [2] describe discrete-copula polytopes, while Sukeda and Sei [3] study checkerboard copulas under Kendall-concordance constraints; neither identified result states this finite diagonal-knot asymmetry law.

## Limitations
This is a theorem for nonnegative arrays and grid-point asymmetry. The attaining array can have zero cells, and the continuous copula used for attainment can be singular before binning. It does not give an optimum for strictly positive arrays or the exact supremum of off-grid asymmetry of a checkerboard interpolation. The derivation depends on previously established full-diagonal extremal-copula theorems. An earlier equivalent finite-grid formula under another terminology cannot be excluded by the literature inspection.

## References
[1] D. Kokol Bukovšek, B. Mojškerc, N. Stopar, *Exact upper bound for copulas with a given diagonal section*, arXiv:2308.02220 (first posted 2023-08-04), especially Proposition 3.1, Theorem 3.6, Proposition 4.3, Example 4.11; https://arxiv.org/html/2308.02220v2 .

[2] E. Perrone, L. Solus, C. Uhler, *Geometry of Discrete Copulas*, arXiv:1802.06969 (2018); https://arxiv.org/html/1802.06969v2 .

[3] I. Sukeda, T. Sei, *On the minimum information checkerboard copulas under fixed Kendall's rank correlation*, arXiv:2306.01604 (first posted 2023-06-02); https://arxiv.org/html/2306.01604v2 .
