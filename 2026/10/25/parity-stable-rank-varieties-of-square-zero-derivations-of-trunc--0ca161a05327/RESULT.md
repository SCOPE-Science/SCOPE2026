# Parity-stable rank varieties of square-zero derivations of truncated polynomial algebras

## Finding

Let \(k\) be any field of characteristic \(2\), let \(m\geq1\), and put \(A_n=k[t]/(t^n)\). For \(n=2m\) or \(n=2m+1\), let \(\mathcal Z_{n,r}\) be the **reduced** locally closed \(k\)-variety of \(k\)-linear derivations \(D:A_n\to A_n\) satisfying \(D^2=0\) and having \(k\)-linear rank exactly \(r\). Then, for **both** choices of \(n\), the variety is a point for \(r=0\), empty for \(r>m\), and admits the following explicit isomorphism types for \(1\leq r\leq m\):

\[
\mathcal Z_{2m,r}\;\cong\;\mathcal Z_{2m+1,r}\;\cong\;
\begin{cases}
\mathbb A_k^{2r-2}\times(\mathbb A_k^2\setminus\{0\}),&1\leq r\leq\lfloor m/2\rfloor,\\
\mathbb G_{m,k}\times\mathbb A_k^{m-1},&\lfloor m/2\rfloor<r\leq m.
\end{cases}
\]

These are isomorphisms of the indicated **reduced rank loci**, not assertions that the possibly nonreduced scheme cut out by \(D^2=0\) is reduced. Thus the two adjacent truncations have isomorphic square-zero-derivation rank varieties, despite different algebra dimensions.

In particular, over every finite field \(k=\mathbb F_q\), with \(q\) a power of \(2\), write \(h=\lfloor m/2\rfloor\). The exact rank-generating polynomial is the same for \(n=2m\) and \(n=2m+1\):

\[
\sum_{D^2=0}z^{\operatorname{rank}_kD}
=1+\sum_{r=1}^{h}(q^2-1)q^{2r-2}z^r
+\sum_{r=h+1}^{m}(q-1)q^{m-1}z^r.
\]

Consequently, the total number of square-zero derivations is
\[
q^{2h}+(m-h)(q-1)q^{m-1}.
\]

Each such \(D\) determines a differential complex \(A_n\xrightarrow{D}A_n\); its homology \(\ker D/\operatorname{im}D\) has dimension \(n-2r\) on the rank-\(r\) stratum. The result therefore also enumerates these homology dimensions for all square-zero differential structures arising from derivations.

## Assumptions and scope

The field has characteristic exactly \(2\), but need not be perfect or finite for the geometric classification. A derivation is \(k\)-linear and obeys the ordinary Leibniz identity. The equation \(D^2=0\) refers to the square of the resulting \(k\)-linear endomorphism, rather than a square-zero element of the algebra or a degree-one graded derivation. The rank loci carry their reduced induced structures. In positive rank we consider genuine derivations, without identifying them under algebra automorphisms. The finite-field formulas use a cardinality \(q=2^e\), \(e\geq1\).

## Proof

**Parameterization and square-zero criterion.** Every derivation is uniquely \(D_f=f(t)\,\partial_t\), where \(f=\sum_{j=0}^{n-1}c_jt^j\). The relation \(t^n=0\) requires \(n t^{n-1}f=0\), so the coefficient \(c_0\) is arbitrary when \(n\) is even and must vanish when \(n\) is odd. In characteristic \(2\), the square of any derivation is again a derivation because the cross term in the second Leibniz identity is \(2D(a)D(b)=0\). Since \(D_f^2(t)=f f'\), the condition \(D_f^2=0\) is **equivalent** to \(f f'=0\) modulo \(t^n\).

For nonzero \(f\), let \(v=\operatorname{ord}_t(f)\) and write \(f=t^v u\) with \(u\) a unit. Then \(f f'=0\) if and only if \(f'\equiv0\pmod {t^{n-v}}\). Because
\[
f'=\sum_{\substack{j\geq1\\j\text{ odd}}}c_jt^{j-1},
\]
this says precisely that every \(c_j\) with \(j\) odd and \(j\leq n-v\) vanishes. This coefficient criterion is necessary and sufficient over every characteristic-two field.

**Rank criterion.** Differentiating all classes in \(A_n\) gives the \(m\)-dimensional span \(W=\operatorname{span}_k\{1,t^2,\ldots,t^{2m-2}\}\) when \(n\) equals either \(2m\) or \(2m+1\). Thus \(D_f(A_n)=fW\). Multiplication by \(f=t^vu\) on \(W\) has linearly independent pivot degrees \(v,v+2,\ldots\) below \(n\); multiplication by \(u\) cannot change their independence. Therefore
\[
\operatorname{rank}_k(D_f)
=\min\left\{m,\left\lceil\frac{n-v}{2}\right\rceil\right\}.
\]
Only \(f=0\) gives rank zero.

**Low ranks.** Fix \(1\leq r\leq h=\lfloor m/2\rfloor\). For \(n=2m\), rank \(r\) forces \(v\in\{2(m-r),2(m-r)+1\}\). Since \(2(m-r)\geq m\) and the first allowed valuation is even, the square-zero coefficient criterion is automatic. Thus exactly the polynomials
\[
f=t^{2(m-r)}(a+bt+t^2w(t)),\qquad (a,b)\ne(0,0),
\]
with \(w\) having precisely \(2r-2\) arbitrary coefficients, form the rank-\(r\) locus. Its reduced variety is \(\mathbb A_k^{2r-2}\times(\mathbb A_k^2\setminus\{0\})\).

For \(n=2m+1\), the two allowed valuations are \(2(m-r)+1\) and \(2(m-r)+2\). Every polynomial with either valuation also satisfies \(f f'=0\) because the smaller one exceeds \(n/2\). The same normal form, now with initial factor \(t^{2(m-r)+1}\), gives the identical isomorphism type. In these normal forms, \(w\) ranges over polynomials of degree less than \(2r-2\), with the evident empty convention when \(r=1\).

**High ranks.** Fix \(h<r\leq m\). In the even truncation, valuation must be exactly \(v=2(m-r)\): the alternative odd valuation would violate the square-zero coefficient criterion. The coefficient \(c_v\) is nonzero. There are \(2r-1\) positions above \(v\); precisely \(2r-m\) of their odd-indexed coefficients are forced to vanish by \(j\leq n-v=2r\). Therefore precisely \(m-1\) higher coefficients remain free. The rank locus is \(\mathbb G_{m,k}\times\mathbb A_k^{m-1}\).

In the odd truncation, valuation must be \(v=2(m-r+1)\). The smaller odd candidate is excluded by the square-zero criterion. Of the \(2r-2\) positions above \(v\), exactly \(2r-m-1\) odd-indexed coefficients are forced to vanish by \(j\leq n-v=2r-1\). Again the leading coefficient is nonzero and exactly \(m-1\) further coefficients are free. This yields the same variety. The displayed forced-coefficient counts are nonnegative because \(r>\lfloor m/2\rfloor\). The low- and high-rank cases exhaust all nonzero \(f\), proving the classification.

**Finite fields and homology.** Over \(\mathbb F_q\), the point, punctured affine plane, affine space, and multiplicative group have respectively \(1\), \(q^2-1\), \(q^d\), and \(q-1\) points. The formulas follow. Summing the low-rank geometric progression gives \(q^{2h}-1\); adding the zero map and \(m-h\) high-rank strata gives the total. Finally, \(D^2=0\) implies \(\operatorname{im}D\subseteq\ker D\), and rank-nullity gives \(\dim_k(\ker D/\operatorname{im}D)=n-2r\).

## Verification

The accompanying standard-library program `verify_square_zero.py` enumerates the coefficients of every admissible derivation, computes \(D_f^2(t)\) by truncated polynomial multiplication, constructs the full \(n\times n\) matrix of \(D_f\), and row-reduces over \(\mathbb F_2\) and \(\mathbb F_4\). It does **not** use the claimed valuation/rank formula in the exhaustive branch. It compares the observed rank histogram with the stated formula for \(2\leq n\leq12\) over \(\mathbb F_2\) and \(2\leq n\leq7\) over \(\mathbb F_4\); all \(17\) cases pass. The infinite-family claim is established by the coefficient proof above, not by these finite experiments.

## Relationship to prior work

Avramov–Buchweitz–Iyengar (first public version 2006) study square-zero **module endomorphisms** and general class/rank bounds. Their square-zero-matrix results do not impose Leibniz and do not enumerate derivations of \(k[t]/(t^n)\). Premet (first public version 2014) studies invariant theory and regular derivations of a **multivariable prime-truncated algebra in characteristic greater than two**, not these characteristic-two square-zero rank varieties. Skryabin (2014) counts **all nilpotent elements** of the Jacobson–Witt derivation Lie algebra of the algebra with relations \(x_i^p=0\); its one-variable characteristic-two case agrees at truncation length two but does not imply the rank-stratified laws for arbitrary truncation length. Previously known ranks of **all** derivations of a one-variable truncated polynomial ring also do not decide which derivations satisfy \(D^2=0\), nor the isomorphism types of that restricted locus. The term “square-zero derivation” is also used in the literature for maps preserving square-zero elements in a different sense; that notion is not used here.

## Limitations

No assertion is made in odd characteristic, about unreduced scheme structure, conjugacy-orbit classifications, graded dg-algebra structures, or higher nilpotency exponents such as \(D^3=0\). The literature searches and primary-source comparisons described above support noncoverage by the inspected results but cannot establish absolute priority against all historical literature. The rank varieties are considered before quotienting by algebra automorphisms.

## References

1. L. L. Avramov, R.-O. Buchweitz and S. Iyengar, *Class and rank of differential modules*, arXiv:math/0602344 (first public version 2006-02-16), especially the introduction and §6 on square-zero matrices. https://arxiv.org/abs/math/0602344
2. A. Premet, *Regular derivations of truncated polynomial rings*, arXiv:1405.2426 (first public version 2014-05-10), especially §1 and its characteristic restriction. https://arxiv.org/abs/1405.2426
3. S. Skryabin, *Nilpotent elements in the Jacobson–Witt algebra over a finite field*, *Transformation Groups* 19 (2014), 927–940, DOI 10.1007/s00031-014-9270-0, especially the introduction and Theorem 3.4. Author-hosted manuscript: https://shelly.kpfu.ru/e-ksu/docs/F1143899874/sskr032.pdf
4. J. Zhou, D. Wang and Q. Zhang, *Square-zero derivations of matrix algebras over commutative rings*, *Linear and Multilinear Algebra* 58 (2010), 239–243, DOI 10.1080/03081080802443091 (terminological distinction, abstract only).
