# Three extremal genus-two classes over \(\mathbf F_5\) and a Frobenius branch trichotomy

## Finding
Let \(C\) be a geometrically smooth, projective, geometrically connected genus-two curve over \(\mathbf F_5\). Then \(\#C(\mathbf F_5)\le 12\). Equality holds for exactly **three** \(\mathbf F_5\)-isomorphism classes. Their six geometric Weierstrass points have Frobenius orbit partitions exactly \((2,4)\), \((3,3)\), and \((6)\), one class per partition. Their Frobenius characteristic (Weil) polynomials, in that order, are
\[
T^4+6T^3+18T^2+30T+25,\quad T^4+6T^3+19T^2+30T+25,\quad T^4+6T^3+17T^2+30T+25.
\]
Here \(T\) is the characteristic-polynomial variable, and all coefficients are listed in descending powers; the corresponding zeta numerator is obtained by replacing the roots \(\alpha_i\) with the factors \(1-\alpha_i t\). Equivalently these three classes have \(\#C(\mathbf F_{25})=26,28,24\), respectively. **The upper bound and the existence of maximal-point curves are established background; the classification and branch–zeta refinement are the asserted finding.**

| Affine model \(y^2=f(x)\) | Branch orbit partition | Number of eligible binary sextic equations | \(\#C(\mathbf F_{25})\) | Middle Weil coefficient |
|---|---|---:|---:|---:|
| \(f(x)=x^6+4x^4+1\) | \((2,4)\) | 120 | 26 | 18 |
| \(f(x)=4x^6+3x^4+x^2+1\) | \((3,3)\) | 40 | 28 | 19 |
| \(f(x)=x^6+2x^5+2x^4+2x^3+x^2+1\) | \((6)\) | 80 | 24 | 17 |

## Assumptions and scope
All curves and isomorphisms are defined over \(\mathbf F_5\); smooth means geometrically smooth. The unique genus-two hyperelliptic involution yields a degree-two map to a genus-zero quotient; every smooth genus-zero curve over a finite field has a rational point, so this quotient is a split projective line, and in odd characteristic a homogeneous squarefree binary sextic \(F(X,Z)=\sum_{i=0}^{6}a_iX^iZ^{6-i}\) gives its model \(Y^2=F(X,Z)\) in the appropriate weighted projective presentation. A change of rational base coordinates is given by \(\operatorname{PGL}_2(\mathbf F_5)\), while a lift differing by a square scaling of \(F\) defines the same curve. Every class is represented; scaling by a nonsquare gives its quadratic twist. For a squarefree sextic, the unordered Frobenius degrees of its roots are the degrees of its irreducible factors over \(\mathbf F_5\).

## Proof
**1. Rational-point bound and exact equality test.** The hyperelliptic map has six rational points in its base \(\mathbf P^1(\mathbf F_5)\). Every fiber contains at most two rational points, hence \(\#C(\mathbf F_5)\le 12\). Equality holds if and only if each of the six fibers consists of two distinct rational points, equivalently \(F(a,1)\in\{1,4\}\) for every \(a\in\mathbf F_5\) and \(F(1,0)\in\{1,4\}\). Thus all six rational base fibers are unramified and split. Since the leading coefficient must be nonzero, such a sextic is necessarily of degree six in the chosen affine coordinate.

**2. Exhaustive small parameter space.** Fix five values \(v_0,\dots,v_4\in\{1,4\}\), and let \(R_v(x)\) be the unique polynomial of degree at most four interpolating the values \(R_v(j)=v_j\) for \(j=0,\ldots,4\). Every polynomial having exactly these five values can be written uniquely
\[
f(x)=R_v(x)+(x^5-x)(a x+b),\qquad a\in\{1,4\},\quad b\in\mathbf F_5.
\]
Here \(a\) is its sextic leading coefficient and represents the rational fiber over infinity. The exact complete family therefore has \(2^5\cdot2\cdot5=320\) binary sextic equations. Exact Euclidean gcd of \(f\) and \(f'\) (over \(\mathbf F_5[x]\)) leaves 240 squarefree sextics and rejects 80. Squarefreeness is equivalent to *geometric* smoothness of the genus-two double cover in characteristic five. Exact monic irreducible factorization of each smooth sextic gives the frequency table \((2,4):120\), \((3,3):40\), \((6):80\), with no other partition. This computation is given by `interpolation_check.py`, which derives its 320 candidates without using the direct-coefficient search.

**3. Arithmetic classification.** Enumerate all \(\operatorname{PGL}_2(\mathbf F_5)\) matrices: there are 120. Each acts on binary sextics by substitution. Include the two square scalars \(\{1,4\}\), giving an action of 240 transformations on the qualifying sextics. Because a scalar matrix multiplies a sextic by a square sixth power, the action is independent of the representative of a projective matrix after allowing these scalars. Any \(\mathbf F_5\)-isomorphism between genus-two curves descends, by uniqueness of their hyperelliptic involution, to such a base transformation; the remaining scaling is necessarily a square. Thus its orbits are exactly the arithmetic curve isomorphism classes. Direct exact orbit enumeration (`extremal_f5.py`) yields the three explicitly displayed representatives with orbit sizes 120, 40, and 80, and effective stabilizer orders 2, 6, and 3. The three orbits are disjoint because their branch partitions differ, and their sizes sum to 240. Therefore they comprise every candidate, yielding precisely three classes.

**4. Frobenius polynomials.** For each representative a separate exact count enumerates the 25 affine values over \(\mathbf F_{25}\) and the two points above infinity, using \(\mathbf F_{25}=\mathbf F_5[v]/(v^2+v+2)\). The counts are 26, 28, and 24. Let \(s_1=6-\#C(\mathbf F_5)=-6\) and \(s_2=26-\#C(\mathbf F_{25})\). Newton's identity gives the second characteristic-polynomial coefficient \(A_2=(s_1^2-s_2)/2=(10+\#C(\mathbf F_{25}))/2\), namely 18, 19 and 17. The functional equation fixes the remaining coefficients, proving the displayed polynomials. The independent `weil_check.py` uses an alternate quadratic-field presentation; `extremal_f5_invariants.py` also factors the three polynomials exactly and independently checks the \(\mathbf F_{25}\) counts.

## Verification
Run `python extremal_f5.py`, `python interpolation_check.py`, and `python weil_check.py` in the directory containing all three scripts. The first relies only on the Python standard library; the second requires SymPy; the third is standard library only. The accompanying files `extremal_f5.out`, `interpolation_check.out` and `weil_check.out` give the observed exact output. The third script is arithmetically independent of the original quadratic extension used to inspect branch invariants; full field enumeration is exact and finite. There is no random sampling and no field-extension cutoff used to infer squarefreeness. The group orbit computation exhausts all 240 qualifying equations; it does not rely on pattern matching or title-level classification.

## Relationship to prior work
Vermeulen, *Curves of fixed gonality with many rational points*, arXiv:2102.00900v1 (2021), studies the degree-times-\(q+1\) upper bound and existence constructions at larger genera; it does not supply the exact three genus-two \(\mathbf F_5\)-classes or distinguish their branch partitions. Faber–Vermeulen, *Abelian covers of the projective line*, arXiv:2202.12969v1 (2022), similarly studies large genus and fixed gonality, not this exact small-genus arithmetic classification. Nart, *Counting hyperelliptic curves* (arXiv:math/0703549, 2007) provides a general finite-field orbit-counting framework for hyperelliptic curves but does not, in the portions examined, enumerate the all-six-fibers-split locus, its branch partitions, or its Weil-polynomial frequencies. The general 12-point bound, existence of extremal examples, and general PGL orbit principle are **not** claimed as novel. A published complete machine-readable curve catalogue might subsume this small-field census; no demonstrated statement-level coverage of the exact joint classification was identified in the inspected sources.

## Limitations
This is an exact classification only for genus two over \(\mathbf F_5\), not an asymptotic or all-finite-fields theorem. The 240 equations are coordinate-dependent and not 240 distinct curves. The statement that the trichotomy is absent from literature is a best-knowledge comparison, not a certification of priority; comprehensive enumerations or unpublished tables could imply it. The equations give genuine geometric smoothness because squarefreeness is exact. Self-review does not constitute independent auditing.

## References
1. F. Vermeulen, *Curves of fixed gonality with many rational points*, arXiv:2102.00900v1, 2021. https://arxiv.org/abs/2102.00900
2. X. Faber and F. Vermeulen, *Abelian covers of the projective line with fixed gonality and many rational points*, arXiv:2202.12969v1, 2022. https://arxiv.org/abs/2202.12969
3. E. Nart, *Counting hyperelliptic curves*, arXiv:math/0703549, 2007. https://arxiv.org/abs/math/0703549
4. G. Cardona, *On the number of curves of genus 2 over a finite field*, Finite Fields and Their Applications, 2003; consulted at bibliographic/abstract level, not as verified full-text noncoverage.
