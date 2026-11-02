# Five Hasse–Weil spectra for marked genus-three Howe curves over \(\mathbb F_9\)

## Finding
Let \(k=\mathbb F_9=\mathbb F_3(i)\), where \(i^2=2\). For every ordered \((A,B)\in k^2\) with \(A,B\notin\{1,-1\}\) and \(A\ne B\), let \(C_{A,B}\) be the smooth projective model of
\[
 y^2=(x^4-Ax^2+1)(x^4-Bx^2+1).
\]
These are all \(42\) smooth ordered pairs in this fixed coefficient model. If \(L_{A,B}(T)\) is the numerator of the Hasse–Weil zeta function and \(P_t(T)=1-tT+9T^2\), then the *complete* distribution is:

| Elliptic Frobenius traces \((t_1,t_2,t_3)\), sorted | \(L_{A,B}(T)\) | Ordered pairs | \(\#C_{A,B}(k)\) |
| --- | --- | ---: | ---: |
| \((-6,-2,-2)\) | \(P_{-6}(T)P_{-2}(T)^2\) | 6 | 20 |
| \((-6,2,2)\) | \(P_{-6}(T)P_2(T)^2\) | 4 | 12 |
| \((-2,-2,2)\) | \(P_{-2}(T)^2P_2(T)\) | 12 | 12 |
| \((-2,-2,6)\) | \(P_{-2}(T)^2P_6(T)\) | 8 | 8 |
| \((-2,2,2)\) | \(P_{-2}(T)P_2(T)^2\) | 12 | 8 |

Thus the five distinct degree-six Weil polynomials occur with multiplicities \(6,4,12,8,12\), respectively, and the point-count distribution is exactly \(20\) curves with \(8\) points, \(16\) with \(12\) points, and \(6\) with \(20\) points. In particular, the maximum in this *marked coefficient family* is \(20\), attained exactly six times. The numerator and hence the complete sequence of extension-field point counts are determined by the displayed table.

## Assumptions and scope
All curves are considered over the specified field \(\mathbb F_9\). The normalization has genus \(3\), because the monic degree-eight polynomial has eight distinct geometric roots precisely on the displayed smooth locus. The smoothness condition follows because each quartic has repeated roots exactly when its coefficient equals \(\pm2=\pm1\) in characteristic three, and two different quartics of the displayed form have no common root. The two points at infinity are rational.

The multiplicities count *ordered coefficient pairs*, not distinct geometric isomorphism classes; swapping \(A\) and \(B\) produces the same equation. The theorem does not claim a classification of all genus-three curves or of all \(\mathbb F_9\)-forms of hyperelliptic Howe curves. The previously derived characteristic-three \(p\)-rank stratification of this same parameter family is not claimed as new.

## Proof
**Elliptic splitting.** Three commuting involutions on the smooth curve act by \((x,y)\mapsto(1/x,y/x^4)\), \((x,y)\mapsto(-1/x,y/x^4)\), and \((x,y)\mapsto(-x,y)\). Their three quotients are the smooth genus-one curves
\[
\begin{aligned}
 E_1 &: v^2=(u^2-A-2)(u^2-B-2),\\
 E_2 &: v^2=(u^2-A+2)(u^2-B+2),\\
 E_3 &: v^2=(u^2-Au+1)(u^2-Bu+1).
\end{aligned}
\]
For the first two quotients use \(u=x+1/x\), respectively \(u=x-1/x\), and \(v=y/x^2\); for the third use \(u=x^2,v=y\). They are defined over \(k\). The quotient by the full Klein four group has genus zero, so over any odd auxiliary prime the first cohomology splits into the three nontrivial character eigenspaces, each identified with the two-dimensional first cohomology of one elliptic quotient. Consequently, over \(k\),
\[
 L_{A,B}(T)=\prod_{j=1}^3(1-t_jT+9T^2),\qquad
 t_j=10-\#E_j(k).
\]
This statement follows from the explicit quotient maps and the character decomposition; it requires no assumption about geometric isomorphism classes.

**Exhaustive finite classification.** Encode \(a+bi\in k\) by the integer \(a+3b\), with \(a,b\in\{0,1,2\}\) and \(i^2=2\). The only excluded coefficient codes are \(1\) and \(2\). Thus the seven admissible coefficient codes are \(0,3,4,5,6,7,8\); their \(21\) unordered distinct pairs form an exhaustive list, and each corresponds to exactly two ordered pairs. The file `spectrum_21.csv` contains every one of these \(21\) pairs, with all three elliptic traces and the genus-three point count.

For each monic quartic on the right of an elliptic quotient equation let \(Q_j(u)\) be its value at \(u\in k\). Let \(\chi(0)=0\), \(\chi(z)=1\) on nonzero squares, and \(\chi(z)=-1\) on nonsquares. Since the quartic has two rational points above infinity,
\[
 \#E_j(k)=11+\sum_{u\in k}\chi(Q_j(u)),
 \quad
 t_j=-1-\sum_{u\in k}\chi(Q_j(u)).
\]
The nonzero square set in the specified representation is exactly \(\{1,2,i,2i\}\), whose integer codes are \(\{1,2,3,6\}\). Computing the above three sums on each of the \(21\) explicitly listed unordered pairs proves the five-row distribution; multiplying each row count by two gives the ordered multiplicities \(6,4,12,8,12\). Finally,
\[
 \#C_{A,B}(k)=10-(t_1+t_2+t_3)
\]
by the quotient decomposition. This yields the stated point-count distribution and its sharp maximum \(20\).

## Verification
Run `python3 verify_formula.py` and `python3 verify_extensions.py` with Python 3. Both scripts use only the standard library and each independently enumerates all \(42\) smooth ordered pairs. The former calculates elliptic traces by a direct \(\mathbb F_9\) character table, checks the complete five-polynomial distribution and directly counts curve points over \(\mathbb F_9\). The latter uses a different model of \(\mathbb F_9\) and directly counts each curve's points over \(\mathbb F_9\), \(\mathbb F_{81}\), and \(\mathbb F_{729}\), checking the three initial power sums against the independently evaluated elliptic traces. The field extensions are given by \(u^2=\theta\), where \(\theta^2+\theta+2=0\), and \(v^3-v-1=0\), respectively. The degree-two and degree-three polynomials are irreducible over \(\mathbb F_9\); their irreducibility conditions are asserted in the code. These three extension counts and the genus-three functional equation determine the full degree-six numerator independently of the quotient-factorization argument.

The actual outputs were `FORMULA_VERIFY_OK` and `EXTENSIONS_VERIFY_OK`.

## Relationship to prior work
Ohashi's *On the maximality of hyperelliptic Howe curves of genus 3* (first publicly posted December 21, 2021), especially Section 3 and Theorem 1.1, establishes the standard genus-three hyperelliptic Howe model, its elliptic quotients and a maximality theorem for the superspecial subfamily. Moriya and Kudo's *Some explicit arithmetic on curves of genus three and their applications* (first posted September 7, 2022) develops broader Richelot-isogeny and superspecial enumeration methods. Those constructions and algorithms are prior art and are not new assertions here. Neither inspected work supplies the five \(\mathbb F_9\) Weil-polynomial multiplicities or the sharp \(20\)-point maximum for the specified smooth ordered coefficient family.

The pre-existing characteristic-three \(p\)-rank strata of this family give only coarse Newton-theoretic information. They do not determine the five distinct Frobenius polynomials: in fact, different rows of the displayed table have the same \(p\)-rank. The present result is a *finite, exact zeta census*, not an independent new isogeny splitting theorem or an improved general formula for \(p\)-ranks.

## Limitations
The result is restricted to the specified normalized, ordered coefficient family over \(\mathbb F_9\), and counts repeated coefficient presentations of isomorphic curves separately. It does not assert a global maximum among all genus-three curves over \(\mathbb F_9\), a bound for arbitrary field forms of Howe curves, or a complete moduli-space classification. The direct finite computations verify the complete finite parameter set, not an infinite family of distinct field sizes. Unindexed prior arithmetic tabulations could overlap these five finite numerical results; independent external audit has not been performed.

## References
1. R. Ohashi, *On the maximality of hyperelliptic Howe curves of genus 3*, arXiv:2112.11152, first submitted 2021-12-21. https://arxiv.org/abs/2112.11152
2. T. Moriya and M. Kudo, *Some explicit arithmetic on curves of genus three and their applications*, arXiv:2209.02926, first submitted 2022-09-07. https://arxiv.org/abs/2209.02926
3. R. A. Hidalgo, *Smooth quotients of generalized Fermat curves*, arXiv:2202.12663, first submitted 2022-02-25. https://arxiv.org/abs/2202.12663
