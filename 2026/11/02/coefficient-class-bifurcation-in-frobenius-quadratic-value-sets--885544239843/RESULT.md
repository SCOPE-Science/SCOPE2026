# Coefficient-class bifurcation in Frobenius–quadratic value sets

## Finding

Let \(q\) be an arbitrary odd prime power, \(L=\mathbb F_{q^2}\), and \(a\in L^\times\). Define
\[
F_a:L\longrightarrow L,\qquad F_a(x)=x^q+a x^2,
\quad N_j(a)=\#\{y\in L:\#F_a^{-1}(y)=j\}.
\]
Set \(U=\{z\in L^\times:z^{q+1}=1\}\) and \(h=h(a)=\#\{z\in U:z^3=a^{1-q}\}\). Every fiber has size at most four, and the **entire coefficient-dependent distribution** is
\[
\boxed{\begin{aligned}
N_0&=\frac{3(q^2-1)}8,\\
N_1&=\frac{2q^2+q+5-2h}{6},\\
N_2&=\frac{(q-1)^2}{4}+h-1,\\
N_3&=\frac{q+1-2h}{2},\\
N_4&=\frac{q^2-4q-5+8h}{24}.
\end{aligned}}
\]
All other \(N_j\) vanish. More explicitly, if \(q\not\equiv2\pmod3\), then \(h=1\). If \(q\equiv2\pmod3\), then \(h=3\) for exactly \((q^2-1)/3\) cubic coefficients and \(h=0\) for exactly \(2(q^2-1)/3\) noncubic coefficients. For these **noncubic coefficients**, the new branch is
\[
\boxed{(N_0,N_1,N_2,N_3,N_4)
=\left(\frac{3(q^2-1)}8,\frac{2q^2+q+5}6,
\frac{q^2-2q-3}4,\frac{q+1}2,\frac{q^2-4q-5}{24}\right).}
\]
The value-set size in all coefficient classes is \((5q^2+3)/8\). In particular, the new noncubic branch has \((q+1)/2\) targets with precisely three preimages, whereas the cubic branch has only \((q-5)/2\). At \(q=5\) this changes the four-preimage count from one (cubic coefficient) to zero (noncubic coefficient).

## Assumptions and scope

Finite fields are of odd characteristic, including characteristic three. The field \(L\) is the unique degree-two extension of \(\mathbb F_q\). The coefficient \(a\) is any nonzero element of \(L\). The norm-one group \(U\) is cyclic with \(q+1\) elements. Counts classify target values, not source elements. The coefficient \(a=0\) gives the Frobenius permutation and is outside the statement. The normalized unit-coefficient result is a previously determined special case, not a separate novel claim here.

## Proof

**1. A quartic bound.** Fix a target \(y\). The equation \(x^q+a x^2=y\) implies \(x^q=y-a x^2\). Taking its \(q\)-th power and using \(x^{q^2}=x\) gives
\[
x=y^q-a^q(y-a x^2)^2.
\]
Thus every preimage is a root of the degree-four polynomial
\[
P_y(X)=a^{q+2}X^4-2a^{q+1}yX^2+X+a^q y^2-y^q.
\]
Its leading coefficient is nonzero, so no target has more than four distinct preimages. Every four-element fiber has sum zero because the cubic coefficient vanishes.

**2. Exact collision pairs.** For an ordered pair of distinct preimages \((x,z)\), let \(\Delta=x-z\ne0\). Subtraction of the two map values yields
\[
\Delta^{q-1}=-a(x+z).
\]
For each \(\Delta\in L^\times\), this equation and \(x-z=\Delta\) determine exactly one ordered collision pair:
\[
x=\frac{\Delta-\Delta^{q-1}/a}{2},\qquad
z=\frac{-\Delta-\Delta^{q-1}/a}{2}.
\]
Consequently the number of ordered distinct collision pairs equals \(q^2-1\), and
\[
\sum_{j=0}^4j(j-1)N_j=q^2-1.\tag{1}
\]

**3. An exact norm-one triple parametrization.** Put \(\eta=a^{q-1}\in U\), \(c=\eta^{-1}\). For an ordered triple \((x,y,z)\) of pairwise distinct preimages of one target define
\[
\alpha=a(x+y),\qquad \beta=a(x+z),\qquad\gamma=a(y+z).
\]
The collision relation gives \(\alpha,\beta,\gamma\in U\), all distinct. The identity \(x-y=(\beta-\gamma)/a\) and the formula
\[
(\beta-\gamma)^{q-1}=-\frac1{\beta\gamma}
\qquad(\beta,\gamma\in U,\ \beta\ne\gamma)
\]
imply \(\alpha\beta\gamma=c\). Conversely every ordered triple of distinct \(\alpha,\beta,\gamma\in U\) satisfying \(\alpha\beta\gamma=c\) reconstructs
\[
x=\frac{\alpha+\beta-\gamma}{2a},\quad
y=\frac{\alpha+\gamma-\beta}{2a},\quad
z=\frac{\beta+\gamma-\alpha}{2a}.
\]
The same pair-difference identity verifies that the reconstructed points have the same image, so this correspondence is bijective. Write \(m=q+1\) and \(h=\#\{u\in U:u^3=c\}\). Of the \(m^2\) product-\(c\) triples without the distinctness restriction, each equality of two coordinates gives \(m\) triples, and all pairwise-equality intersections consist of the same \(h\) diagonal triples. Inclusion-exclusion therefore yields exactly
\[
T=m^2-3m+2h=6N_3+24N_4
\tag{2}
\]
ordered distinct triples.

**4. Which triples extend to four points?** Let \(w=-(x+y+z)\), the sole possible fourth root, by Step 1. For example,
\[
w-x=-\frac{\alpha+\beta}{a},\qquad
w+x=-\frac\gamma a.
\]
If \(\alpha+\beta\ne0\), then
\[
(w-x)^{q-1}=\frac1{\eta\alpha\beta}=\gamma=-a(w+x),
\]
so \(F_a(w)=F_a(x)\). Cyclically, if no two of \(\alpha,\beta,\gamma\) are opposite, \(w\) is a fourth distinct preimage. If one pair is opposite, \(w\) equals one of the three points, and a different fourth preimage is forbidden by the quartic. At most one pair can be opposite because the three coordinates are distinct.

For the designated opposite pair \(\alpha=-\beta\), the product condition forces \(\gamma=-c/\alpha^2\). It is distinct from both \(\alpha\) and \(-\alpha\) unless \(\alpha^3=-c\) or \(\alpha^3=c\). The two exceptions are disjoint in odd characteristic. Each equation has exactly \(h\) solutions in \(U\), because multiplying by \(-1\) exchanges their solution sets. Thus \(m-2h\) triples have this designated opposite pair, and the total number of nonextendible ordered triples is \(3(m-2h)=6N_3\). It follows that
\[
N_3=\frac{m-2h}2,\qquad
N_4=\frac{m^2-6m+8h}{24}.
\]

**5. Remaining counts.** Equations (1) and (2), together with the target-count and source-count identities \(\sum_jN_j=q^2\) and \(\sum_jjN_j=q^2\), give successively
\[
N_2=\frac{(q-1)^2}4+h-1,\quad
N_1=\frac{2q^2+q+5-2h}6,\quad
N_0=\frac{3(q^2-1)}8.
\]
The image-size formula follows from \(q^2-N_0\). Each rational expression is integral because it counts an explicit finite set.

**6. Exact coefficient classification.** The homomorphism \(u\mapsto u^3\) on \(U\), of order \(m=q+1\), has kernel size \(e=\gcd(3,m)\). Consequently \(h\) equals either \(0\) or \(e\). If \(e=1\), \(h=1\) for every coefficient. If \(e=3\), the condition \(h=3\) is equivalent to \(a\) being a cube in \(L^\times\): since \(a^{q-1}\in U\), and \(q-1\equiv1\pmod3\), a cubic character of \(L^\times\) takes \(a^{q-1}\) to the same cubic character value as \(a\). The cyclic group \(L^\times\) has \((q^2-1)/3\) cubes and \(2(q^2-1)/3\) noncubes. This completes the full coefficient-dependent classification. \(\square\)

## Verification

A standalone Python 3 program (\(\texttt{verify.py}\)) directly constructs each tested finite-field tower and evaluates all input fibers for every tested coefficient, independently of the proof's triple parametrization. It tests complete coefficient sets for field orders \(3,5,7,9,11,13\), and selected coefficients for orders \(17,23,25,49\). In all, 493 coefficient configurations passed. Both cubic and noncubic classes were checked over \(q=5,11,17,23\). Run \(\texttt{python verify.py}\) from the package. This finite verification does not substitute for the proof for every prime power.

## Relationship to prior work

Mullen, Wan, and Wang [1] establish general bounds for multivariate polynomial value sets over finite fields, not coefficient-resolved fiber histograms. A normalized unit-coefficient spectrum of \(x^q+x^2\) is also already known and is not claimed as original; scaling covers its cubic-coefficient class, but not the noncubic coefficients when \(q\equiv2\pmod3\). Indeed \(x\mapsto bx\) changes the quadratic coefficient by the factor \(b^{2-q}\), whose image has index \(\gcd(q-2,q^2-1)=3\) in this regime. The missing noncubic classes have genuinely different numbers of three- and four-preimage targets. The novel contribution is the exact noncubic branch and the complete coefficient census, rather than the shared value-set size or the previously known normalized special case.

## Limitations

The result is restricted to quadratic extensions in odd characteristic, with a nonzero quadratic coefficient. It does not address higher extension degrees, characteristic two, or dynamical cycle counts. The exact value-set cardinality is unchanged between cubic classes, so only the finer target-fiber distribution detects the distinction. Historical priority remains subject to incomplete discovery of less accessible literature; independent mathematical audit has not been performed.

## References

[1] G. L. Mullen, D. Wan, and Q. Wang, *Value sets of polynomial maps over finite fields*, *Quarterly Journal of Mathematics* 64 (2013), 1191–1196, DOI 10.1093/qmath/has026. Public online date 2012-10-17; accessible preprint arXiv:1210.8119v1 (2012-10-30).
