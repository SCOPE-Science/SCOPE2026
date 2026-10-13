# Strict entropy concavity for four positive weighted Bernoulli summands

## Finding
Let \(B_1,B_2,B_3,B_4\) be independent Bernoulli variables with a common parameter \(p\in[0,1]\), and let \(w_1,w_2,w_3,w_4\) be **arbitrary strictly positive real weights**. Write
\[
S_p=\sum_{i=1}^{4} w_i B_i,\qquad
H_w(p)=-\sum_{s\in\operatorname{supp}(S_p)}\Pr(S_p=s)\log\Pr(S_p=s).
\]
Then \(H_w\) is strictly concave on \([0,1]\), and \(H_w''(p)<0\) for every \(0<p<1\). This proves the complete four-summand case of the positive-weight common-parameter entropy-concavity question, including all subset-sum collision patterns. In particular, the fourth-stage distribution in the recursive-overlap Bernoulli construction has strictly concave entropy for **every** strictly increasing choice of embedding lengths.

## Assumptions and scope
Entropy is Shannon entropy in natural logarithms; zero masses contribute zero. The four Bernoulli variables are independent and identically parametrized, **not** necessarily identically weighted. Real weights are positive, without rationality or noncollision assumptions. No joint concavity in four *different* Bernoulli parameters is asserted; such a heterogeneous strengthening is false already with three variables.

## Proof
**1. The finite coefficient patterns.** For each distinct subset sum \(s\) put
\[
 c_{s,k}=\#\left\{A\subseteq\{1,2,3,4\}:|A|=k,\ \sum_{i\in A}w_i=s\right\},\quad
 q_s(p)=\sum_{k=0}^4 c_{s,k}p^k(1-p)^{4-k}.
\]
Thus the function \(H_w\) depends only on the multiset of the five-term coefficient vectors \((c_{s,0},\ldots,c_{s,4})\). Reordering the weights leaves this multiset unchanged. After ordering them, normalize their sum to one. The weight vector lies in the compact ordered simplex
\[P=\{0\le w_1\le w_2\le w_3\le w_4,\ \sum_iw_i=1\}.\]
A collision between two subset sums is equivalent to \(a\cdot w=0\) for some nonzero \(a\in\{-1,0,1\}^4\), considered up to global sign. There are exactly 40 such possible hyperplanes. For any positive weight vector, let \(L\) be the common kernel of all collision normals at that vector. Its codimension is at most three. It is consequently represented among the intersections of at most three of the 40 hyperplanes. The polytope \(L\cap P\) has vertices among intersections of three independent hyperplanes selected from the 40 collision hyperplanes together with the four ordered-simplex boundary hyperplanes. Exact rational determinant enumeration finds twelve possible vertices in the latter global arrangement.

For each of these finitely many intersections \(L\), a positive relative-interior point of \(L\cap P\) has exactly the collisions forced by \(L\). To select such a point without accidentally acquiring any extra collision, the supplied enumerator takes a lexicographically weighted sum of all its rational vertices with successive powers of \(10^{12}\), then normalizes. All global vertex coordinates have denominators dividing \(840\); after clearing denominators, coefficients of each collision-normal dot-product are integers of absolute value at most \(840\). Since \(10^{12}>841\), a nonzero such integer polynomial in \(10^{12}\) cannot vanish: its leading nonzero term dominates the sum of lower terms. Therefore the weighted sum is generic relative to every non-forced collision hyperplane. Cases with zero first weight are discarded. This procedure enumerates **exactly 23** distinct coefficient-multiset patterns; independently, every one has an integer representative with ordered weights in \(\{1,\ldots,8\}\). The exhaustive rational procedure and the independent small-representative comparison are implemented in `classify4.py`.

**2. The entropy curvature.** For \(0<p<1\), each \(q_s(p)>0\). Twice differentiating gives
\[
 H_w''(p)=-\sum_s\left(q_s''(p)\log q_s(p)+\frac{q_s'(p)^2}{q_s(p)}\right).
\]
The exact coefficient vectors, hence these expressions, are determined by the 23 patterns just classified. The reflection \(S_p\stackrel d=\sum_iw_i-S_{1-p}\) shows \(H_w(p)=H_w(1-p)\), so it suffices to show negative curvature for \(0<p\le1/2\).

**3. The uniform small-parameter range.** Because every subset-event mass \(p^k(1-p)^{4-k}\) is at least \(p^4\) for \(0<p\le1/2\), every nonzero \(q_s(p)\ge p^4\). The elementary second-derivative formula for \(p^k(1-p)^{4-k}\) implies its absolute second derivative is at most 12; summing over 16 binary configurations gives \(\sum_s|q_s''(p)|\le192\). Hence
\[\left|\sum_s q_s''(p)\log q_s(p)\right|\le768\log(1/p).\]
All weights are positive, so \(S_p=0\) if and only if all four Bernoulli variables vanish. Cauchy–Schwarz applied to the two events \(S_p=0\) and \(S_p>0\) gives the information lower bound
\[
\sum_s\frac{q_s'(p)^2}{q_s(p)}
\ge\frac{16(1-p)^2}{1-(1-p)^4}
\ge\frac{4(1-p)^2}{p}.
\]
It follows that
\[
 H_w''(p)\le768\log(1/p)-\frac{4(1-p)^2}{p}<0
 \quad(0<p\le10^{-4}),
\]
since \(768p\log(1/p)\le768\cdot10^{-4}\log(10^4)<0.708<4(1-10^{-4})^2\).

**4. Complete rigorous interval certification on the compact range.** The accompanying `curvature4.py` checks the remaining closed interval \([10^{-4},1/2]\) for **all 23** coefficient patterns. It uses the outward-rounded `mpmath.iv` interval arithmetic of mpmath 1.3.0, 28 decimal digits, exact integer polynomial coefficients and rational Bernstein expressions. The interval for each probability is computed from nonnegative Bernstein terms, its first two derivatives from exactly differentiated integer polynomials, and the logarithm and reciprocal from interval operations. A binary subdivision is accepted **only** if the computed upper endpoint of the enclosing interval for the entire displayed curvature expression is strictly negative. An undecidable box is bisected rather than assumed valid. All boxes terminate with strict negative upper bounds: 1,129 visited nodes across the 23 patterns, with maximal subdivision depth five. The executable also checks the 23 distinct integer representatives. The interval proof covers a real continuum; the assertions are not sampling at finitely many parameter values.

Together with the uniform small-parameter estimate and reflection, this proves \(H_w''(p)<0\) on \((0,1)\). Since entropy is continuous at \(p=0,1\), strict concavity holds throughout \([0,1]\).

## Verification
Run `python classify4.py` and `python curvature4.py` using Python 3.13 or compatible Python 3 and mpmath 1.3.0. The former must report `CLASSIFICATION VERIFIED: 23 patterns represented by weights <=8`; the latter must report `GLOBAL PASS: 23 patterns 1129 subinterval nodes` (elapsed seconds vary). The rational classification makes no numerical assumptions. The curvature checker makes interval comparisons, never midpoint tests. Both programs are embedded in full.

## Relationship to prior work
Neunhäuserer (2026) introduced the recursive-overlap family and conjectured entropy concavity, proving the two extremal regimes. A public MathOverflow discussion originating on 28 August 2026 gives its equivalent positive integer weighted-Bernoulli representation and proves the three-weight case. The discussion explicitly identifies 23 four-weight collision patterns and reports numerical tests for all 23, but analytic proofs for only seven as of its 15 September 2026 revision. The present four-weight **uniform strict proof** includes the remaining patterns; unlike the earlier numerical tests, the new finite interval enclosure controls every real parameter in every case. The classical Hillion–Johnson Shepp–Olkin theorem concerns unit-weight Bernoulli sums, and does not directly cover arbitrary unequal positive weights.

## Limitations
The result is only for four summands and a common Bernoulli parameter; no arbitrary-length conclusion or heterogeneous-parameter concavity is established. Rigorous interval arithmetic is part of the proof for the compact interior range, rather than replaced by an elementary closed-form inequality for each pattern. The complete lead preprint text could not be accessed, although its abstract and the author's substantive public discussion were checked; an unlocated equivalent proof remains a priority risk. Independent scientific review has not been carried out.

## References
1. J. Neunhäuserer, *Recursive overlap Bernoulli distributions and an entropy concavity conjecture*, arXiv:2609.05546, posted 2 September 2026, https://arxiv.org/abs/2609.05546.
2. J. Neunhäuserer, MathOverflow question 514729, *A recursive overlap construction of finite Bernoulli-sum laws and an entropy-concavity conjecture*, asked 28 August 2026; and Amir's answer, updated 15 September 2026, https://mathoverflow.net/questions/514729/.
3. E. Hillion and O. Johnson, *A proof of the Shepp–Olkin entropy concavity conjecture*, Bernoulli 23 (2017), 3638–3649, DOI:10.3150/16-BEJ860.
