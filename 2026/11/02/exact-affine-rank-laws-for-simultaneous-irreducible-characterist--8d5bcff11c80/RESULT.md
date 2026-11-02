# Exact affine-rank laws for simultaneous irreducible characteristic-three cubics

## Finding

Let \(q=3^s\), where \(s\ge1\), and let \(H\) be any nonempty set of distinct elements of \(\mathbb F_q\). Define
\[
N_q(H)=\#\left\{(b,c)\in\mathbb F_q^2:\ X^3+bX+c+h\text{ is irreducible in }\mathbb F_q[X]\ \text{for every }h\in H\right\}.
\]
For every nonempty subset \(J\subseteq H\), choose any \(h_J\in J\), and write
\[
d(J)=\dim_{\mathbb F_3}\operatorname{span}_{\mathbb F_3}\{h-h_J:h\in J\}.
\]
This is independent of the chosen \(h_J\). The exact **affine-rank formula** is
\[
\boxed{N_q(H)=\frac q6\left(3q-2-q\sum_{\varnothing\ne J\subseteq H}(-1)^{|J|+1}3^{-d(J)}\right).}
\]
Equivalently, with \(V^*=\operatorname{Hom}_{\mathbb F_3}(\mathbb F_q,\mathbb F_3)\),
\[
\boxed{N_q(H)=\frac q6\sum_{0\ne\lambda\in V^*}\bigl(3-|\lambda(H)|\bigr).}
\]
In particular, \(N_q(H)\) depends only on the affine-rank function of the labeled offset configuration, not on its field multiplication table.

The exact **extremal criterion** is
\[
N_q(H)>0\quad\Longleftrightarrow\quad
H\text{ avoids an affine hyperplane in the }\mathbb F_3\text{-space }\mathbb F_q.
\]
Here ``avoids'' means \(H\) is disjoint from the hyperplane. Consequently \(|H|\le 2q/3\) whenever \(N_q(H)>0\). Equality is possible exactly for complements of affine hyperplanes, and every such extremal set has \(N_q(H)=q/3\).

For any three **distinct** offsets \(H=\{h_1,h_2,h_3\}\), the result specializes to
\[
\boxed{N_q(H)=\begin{cases}
q(q-3)/9,&h_1,h_2,h_3\text{ are collinear over }\mathbb F_3,\\
q(4q-9)/27,&\text{otherwise.}
\end{cases}}
\]
(The second case requires \(s\ge2\).) Thus a noncollinear triple has exactly \(q^2/27\) more simultaneous irreducible coefficient pairs than a collinear triple. For comparison, one offset has count \(q(q-1)/3\), and two distinct offsets have count \(q(2q-3)/9\).

## Assumptions and scope

The base field is exactly \(\mathbb F_{3^s}\), \(s\) an arbitrary positive integer. The polynomials are monic cubic trinomials with zero quadratic coefficient, and \((b,c)\) ranges over **all** \(q^2\) pairs, including zero coefficients. An irreducible cubic is equivalent to a cubic with no root in its coefficient field. Offsets comprise a nonempty set; repeated offsets are immaterial and are removed. The affine-rank formula and the extremal criterion are exact at every field size, with no asymptotic or genericity qualifications.

## Proof

**1. Identify the only coefficient stratum that can support irreducibility.** Fix \(b\in\mathbb F_q\), and consider the additive map \(L_b(x)=x^3+bx\). If \(L_b\) is bijective, then every cubic \(X^3+bX+c+h\) has a root and no pair is counted. A nonzero kernel element \(r\) must satisfy \(r^2=-b\). Conversely, if \(b=-r^2\) for some \(r\in\mathbb F_q^\times\), then the kernel is exactly \(\{0,r,-r\}\), and each such \(b\) has exactly two representing elements \(r\) and \(-r\). This includes all possibilities, since \(b=0\) gives the bijective Frobenius map.

For \(b=-r^2\), substitution \(x=ry\) gives
\[
L_b(ry)=r^3(y^3-y).
\]
The map \(y\mapsto y^3-y\) has kernel \(\mathbb F_3\) and image exactly the trace-zero hyperplane: the trace of its output vanishes, and both spaces have size \(q/3\). Therefore \(X^3-r^2X+c+h\) is irreducible if and only if
\[
\lambda_r(c+h)\ne0,\qquad \lambda_r(v)=\operatorname{Tr}_{\mathbb F_q/\mathbb F_3}(v/r^3).
\]
The field trace pairing is nondegenerate. Since the cubic Frobenius map permutes \(\mathbb F_q^\times\), the functionals \(\lambda_r\) range bijectively over the nonzero \(\mathbb F_3\)-linear functionals as \(r\) ranges over \(\mathbb F_q^\times\); replacing \(r\) by \(-r\) replaces \(\lambda_r\) by \(-\lambda_r\) but leaves \(b\) unchanged.

**2. Count the permissible constants for each functional.** For fixed \(0\ne\lambda\in V^*\), the condition \(\lambda(c+h)\ne0\) for all \(h\in H\) excludes the set \(-\lambda(H)\) of field-three values for \(\lambda(c)\). Each value of \(\lambda(c)\) has exactly \(q/3\) preimages. Hence the number of allowed \(c\) is \((q/3)(3-|\lambda(H)|)\). Each coefficient \(b\) is counted twice as \(\lambda\) and \(-\lambda\), proving
\[
N_q(H)=\frac q6\sum_{\lambda\ne0}\bigl(3-|\lambda(H)|\bigr).
\]
This also immediately proves nonnegativity and integrality.

**3. Evaluate the rank dependence.** Inclusion-exclusion on the three possible values of \(\lambda(H)\) yields
\[
|\lambda(H)|=\sum_{\varnothing\ne J\subseteq H}(-1)^{|J|+1}
\mathbf1_{\{\lambda\text{ is constant on }J\}}.
\]
The condition in the indicator says that \(\lambda\) annihilates the \(d(J)\)-dimensional difference space. There are \(3^{s-d(J)}-1=q3^{-d(J)}-1\) **nonzero** such functionals. Thus, setting \(S(H)=\sum_{\varnothing\ne J\subseteq H}(-1)^{|J|+1}3^{-d(J)}\), one obtains
\[
\sum_{\lambda\ne0}|\lambda(H)|=qS(H)-1.
\]
The constant \(-1\) follows because the sum of the alternating coefficients over all nonempty subsets of \(H\) is one. Substitution in step 2 gives the stated affine-rank formula.

**4. Classify existence and the maximum.** Every term \(3-|\lambda(H)|\) is a nonnegative integer. Some term is positive exactly when a nonzero functional \(\lambda\) misses at least one value \(a\in\mathbb F_3\) on \(H\), equivalently when \(H\) avoids the affine hyperplane \(\lambda^{-1}(a)\). Such a hyperplane has \(q/3\) elements, so \(|H|\le2q/3\). If equality holds and there is a witness functional, \(H\) is the entire complement of that hyperplane. For this \(H\), exactly the two nonzero scalar multiples \(\pm\lambda\) omit a value: any other functional is independent of \(\lambda\) and is surjective on each full \(\lambda\)-fiber. (When \(s=1\), no other functional exists.) Thus \(N_q(H)=(q/6)(1+1)=q/3\).

**5. The three-offset dichotomy.** For three distinct elements, each singleton has rank zero and each pair rank one. If all three lie on one affine \(\mathbb F_3\)-line, their triple rank is one; otherwise it is two. Consequently
\[
S(H)=3-3/3+3^{-d(H)}=2+3^{-d(H)}.
\]
Putting \(d(H)=1\) or \(2\) in the formula from step 3 gives exactly the two displayed counts. Their difference is \(q^2/27\). The same calculation for one and two offsets yields the auxiliary counts stated in the finding.

## Verification

The standalone file `verify_artin_schreier.py` builds three explicit finite fields of orders \(3,9,27\) independently from irreducible defining polynomials. It independently enumerates cubic roots for each coefficient pair and compares the resulting simultaneous-irreducibility count with both the affine-rank formula and the functional-projection formula. For \(q=3\) and \(q=9\), it checks **every nonempty set of distinct offsets**, including all maximal-cardinality cases; for \(q=27\), it checks fourteen selected configurations including both affine-rank types of triples and maximum-size sets. It also checks the three-offset dichotomy and the extremal size criterion. Successful output is `VERIFY_OK checked_offset_sets=532 triple_classifications=89 independent_direct_polynomial_root_tests=True`. These tests are finite corroboration, not the universal proof supplied above.

Run `python verify_artin_schreier.py` using Python 3 and no third-party dependencies.

## Relationship to prior work

Pollack's 2008 *Simultaneous prime specializations of polynomials over finite fields* proves an asymptotic for general polynomial compositions under a coprimality hypothesis; its Theorem 2 assumes \(\gcd(q,2n)=1\), which excludes degree three in characteristic three, and it does not evaluate the present fixed-coefficient family. Bary-Soroker's 2012 *Hardy-Littlewood tuple conjecture over large finite field* proves the broad asymptotic \(q^n/n^r+O_{n,r}(q^{n-1/2})\) for all monic polynomials; it does not determine the exact counts on the \(q^2\)-member family with vanishing quadratic coefficient. Bary-Soroker and Stix's 2017 *Cubic twin prime polynomials are counted by a modular form* gives exact **pair** counts over the full space of monic cubics, including characteristic three; summing over all quadratic coefficients does not determine the present coefficient-stratified values or its general offset-rank dependence and extremal classification. The Artin--Schreier trace criterion and linear-algebra inclusion-exclusion are standard ingredients and are not claimed as new.

The specific mathematical contribution assessed here is the complete exact classification of the simultaneous constant-translate irreducibility count on the characteristic-three cubic Artin--Schreier coefficient stratum, including the affine-rank formula, three-point geometry and extremal admissible offset sets. Searches did not find an equivalent published statement, but this does not prove historical priority; a specialized source deriving the same formula remains a genuine risk.

## Limitations

The classification applies to a two-parameter monic cubic family in characteristic three; it does **not** count all monic cubics or higher-degree polynomials, and it is not a new theorem about general Artin--Schreier maps or hyperplane arrangements. For an arbitrary large set \(H\), the inclusion-exclusion expression can require exponentially many subsets; no polynomial-time evaluation algorithm is asserted. Independence and historical-priority certification are not asserted.

## References

- P. Pollack, *Simultaneous prime specializations of polynomials over finite fields*, Proc. London Math. Soc. 97 (2008), 545--567. DOI: 10.1112/plms/pdn013. Author's full manuscript: https://www.pollack-math.net/twinsl.pdf. First verified public journal date: 2008-03-28.
- L. Bary-Soroker, *Hardy-Littlewood tuple conjecture over large finite field*, arXiv:1206.3930 (first posted 2012-06-18), later Int. Math. Res. Not. 2014(2), 568--575.
- L. Bary-Soroker and J. Stix, *Cubic twin prime polynomials are counted by a modular form*, arXiv:1711.05564 (first posted 2017-11-15), later Canad. J. Math. 71 (2019), 1323--1350.
