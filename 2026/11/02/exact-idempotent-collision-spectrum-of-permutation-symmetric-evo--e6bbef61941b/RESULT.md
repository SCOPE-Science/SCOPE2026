# Exact idempotent-collision spectrum of permutation-symmetric evolution algebras

## Finding

Fix an integer \(n\ge3\). Over \(\mathbb C\), let \(E_n(a,b)\) have natural basis \(e_1,\ldots,e_n\) and multiplication
\[
e_i e_j=0\quad(i\ne j),\qquad e_i^2=a e_i+b\sum_{j=1}^n e_j.
\]
Thus the structure matrix is \(aI_n+bJ_n\), with determinant \(a^{n-1}(a+nb)\). Assume \(a(a+nb)\ne0\), so this evolution algebra is perfect. Let \(N_n(a,b)\) count **distinct** solutions of \(x^2=x\) in the underlying complex vector space, including zero.

**Theorem (complete collision census).** If \(b=0\), then \(N_n(a,0)=2^n\). If \(b\ne0\), set \(r=a/b\in\mathbb C\setminus\{0,-n\}\). Then
\[
N_n(a,b)=\begin{cases}
2^{n-1}+1-\dfrac12\mathbf1_{2\mid n}\binom{n}{n/2},&r=n,\\[2mm]
2^n-\binom nk,&r\ne n\text{ and }r^2=4k(n-k)\text{ for some }1\le k<n/2,\\[2mm]
2^n,&\text{otherwise}.
\end{cases}
\]
For \(r\ne n\), at most one integer \(k\) qualifies. The sharp minimum over all perfect members of this family is
\[
\boxed{2^{n-1}+1-\frac12\mathbf1_{2\mid n}\binom n{n/2}.}
\]
It is attained at \(r=n\) and is attained **only** there for \(n\ge4\). For \(n=3\), the additional minimizers are \(r=\pm2\sqrt2\). The minima at dimensions \(3,4,5,6\) are \(5,6,17,23\), respectively. In particular, no perfect member in this full permutation-symmetric family has only one nonzero idempotent when \(n\ge3\).

## Assumptions and scope

All fields in the theorem are \(\mathbb C\); statements count geometric points, **not** scheme-theoretic multiplicities. The symmetric matrix is parametrized as \(aI_n+bJ_n\), so its diagonal entries are \(a+b\), and off-diagonal entries are \(b\). Perfection is equivalent to its invertibility. A simultaneous nonzero rescaling of the natural basis multiplies \((a,b)\) by a common scalar and preserves the number of idempotents. We may consequently normalize \(a+nb=1\). For \(b\ne0\) this gives \(a=r/(r+n)\) and \(b=1/(r+n)\).

## Proof

**1. Constant solutions and the two-value restriction.** Write \(x=\sum_{i=1}^n x_i e_i\) and \(S=\sum_j x_j^2\). The idempotent equations are
\[
x_i=a x_i^2+bS\qquad (1\le i\le n).\tag{1}
\]
Every coordinate is a root of the same quadratic polynomial \(aT^2-T+bS\). Since \(a\ne0\), an idempotent has at most two distinct coordinates. All-constant solutions of (1) are the zero vector and \((a+nb)^{-1}(1,\ldots,1)\). These are distinct by perfection. For \(b=0\), equations (1) decouple as \(x_i\in\{0,a^{-1}\}\), yielding \(2^n\) solutions. Henceforth assume \(b\ne0\).

**2. Exact parameterization of nonconstant solutions.** Suppose \(x\) is nonconstant, with \(k\) coordinates equal to \(u\) and the remaining \(n-k\) equal to \(v\), where \(1\le k<n\) and \(u\ne v\). Subtracting two instances of (1) gives
\[
(u-v)\bigl(1-a(u+v)\bigr)=0,
\]
so \(u+v=a^{-1}\). Equation (1) also gives \(bS=u-au^2=a uv\). Neither \(u\) nor \(v\) can be zero: if one were, then \(S=0\) would follow from the last identity, but exactly one of \(u,v\) would remain nonzero, so \(S=k u^2+(n-k)v^2\ne0\) over \(\mathbb C\), a contradiction. Set \(t=u/v\). Then
\[
kt^2-rt+(n-k)=0,\qquad
v=\frac1{a(1+t)},\qquad u=\frac{t}{a(1+t)}.\tag{2}
\]
Conversely, every subset of size \(k\) and every root of (2) with \(t\ne1\) give an idempotent by these assignments. Indeed \(t=0\) is impossible since \(n-k>0\), and \(t=-1\) is impossible since the left side of (2) at \(-1\) equals \(n+r\ne0\). Then the displayed \(u,v\) obey \(u+v=a^{-1}\) and \(bS=a uv\), which recover (1). This proves exhaustiveness.

**3. Complementary-subset identification.** Every nonconstant idempotent is described exactly twice by the parameterization (2): once by its \(k\)-element set of \(u\)-coordinates and once by the complementary \((n-k)\)-element set of \(v\)-coordinates, where \(t\) is replaced by \(t^{-1}\). There are no other duplications because the vector has precisely two distinct coordinate values.

**4. Generic and discriminant-collision strata.** The discriminant in (2) is
\[
\Delta_k=r^2-4k(n-k).
\]
If \(r\ne n\), substituting \(t=1\) gives \(n-r\ne0\); thus all quadratic roots yield nonconstant solutions. Each \(k\)-subset contributes two roots unless \(\Delta_k=0\), in which case it contributes one. The number of nonconstant solutions is therefore one half the total number of subset-root incidences. Generically this gives \((2\sum_{k=1}^{n-1}\binom nk)/2=2^n-2\). A repeated root for a pair of complementary sizes \(k,n-k\) reduces the total by \(\binom nk\), since the half-weighted two losses equal that binomial coefficient. Equality \(\Delta_{n/2}=0\), when \(n\) is even, would force \(r=\pm n\); the value \(r=-n\) is excluded by perfection, and \(r=n\) is treated separately. On \(1\le k<n/2\), the quantities \(k(n-k)\) strictly increase, so no two distinct such \(k\) can simultaneously collide. Adding the two constant solutions proves the second and third lines of the formula.

**5. The exceptional symmetry parameter \(r=n\).** Now (2) factors as \((t-1)(kt-(n-k))=0\). The root \(t=1\) produces an all-equal vector and is excluded from the nonconstant parameterization. The remaining root is \(t=(n-k)/k\), distinct from \(1\) precisely when \(2k\ne n\). Consequently each nonempty proper subset, except those of size \(n/2\) when \(n\) is even, determines one nonconstant idempotent; complementary subsets encode the same vector. Their number is
\[
\frac{2^n-2-\mathbf1_{2\mid n}\binom n{n/2}}2.
\]
Adding the two constant solutions gives the first line.

**6. Sharpness and uniqueness.** For every integer \(1\le k<n/2\), the two disjoint subset layers of sizes \(k\) and \(n-k\), together with the empty and full subsets, show that \(\binom nk\le 2^{n-1}-1\); hence any collision with \(r\ne n\) has at least \(2^{n-1}+1\) idempotents. When \(n\) is even, this is strictly greater than the value at \(r=n\). When \(n\) is odd, the inequality is strict for \(n\ge5\), since there are further nonempty subset layers besides the two symmetric layers and endpoints. For \(n=3\), equality occurs exactly at \(k=1\), giving the two exceptional ratios \(r=\pm2\sqrt2\). This completes the theorem. \(\square\)

## Verification

The accompanying standalone `verify.py` reconstructs every idempotent described by (2), checks the defining quadratic equations directly over 42 representative numerical parameter cases with \(3\le n\le8\), and compares distinct-vector counts against the formula. It separately constructs rational-coordinate idempotents and verifies the formula by exact rational arithmetic at \(r=n\) for nine dimensions \(3\le n\le11\). Finally, independent Gröbner-basis elimination for \(n=3\) checks the generic ratio \(r=1\) and exceptional ratio \(r=3\). The resulting output is:

```
VERIFY_OK exact_r_equals_n_cases= 9 numeric_parameter_cases= 42 groebner_cases=2
```

Run `python3 verify.py` with Python 3 and SymPy installed. Numerical fingerprints in the 42 parameter cases are finite-precision corroboration; all-dimensional exhaustion and the exact complex-field classification follow only from the proof above.

## Relationship to prior work

The October 2026 survey by Kaygorodov, Martín González and Viruel formulates the general fixed-point equations for evolution-algebra idempotents and gives general upper bounds; it also explicitly discusses the difficulty of finding a one-nonzero-idempotent example within three-dimensional symmetric families (Section 2.1.4, Conjecture 6 discussion). The present theorem computes the **complete distinct-solution count** along the perfect full-permutation-symmetric rank-one perturbation family in every dimension and identifies every exceptional parameter. It neither proves nor disproves the survey's conjecture for arbitrary evolution algebras.

An earlier mathematical census of idempotents for loopless complete-graph evolution algebras over finite fields handles the **single matrix** \(J_n-I_n\), corresponding to the fixed ratio \(r=-1\), including modular arithmetic effects. Its two-coordinate method motivates this comparison, but that fixed matrix and its finite-field counts do not determine the complex-parameter collision strata and sharp all-family minimum here. Hu's October 2026 work on triply transitive permutation images classifies symmetry of perfect evolution-algebra automorphisms, and mentions symmetric support matrices, but does not count element-level idempotents. Papers on random perfect evolution algebras determine distributions or averages over much larger matrix ensembles rather than this parameterized exact count. No claim is made to priority for the shared elementary quadratic-root reduction.

## Limitations

The result assumes an algebraically closed field of characteristic zero, nonzero determinant, and full permutation symmetry. It counts distinct idempotent **elements**, not their multiplicities, automorphism orbits, or field-of-definition over finite fields. It gives a rigorous obstruction within one symmetric family, not a classification of all perfect evolution algebras or a resolution of Conjecture 6. Older classifications of homogeneous or permutation-invariant nonassociative algebras might implicitly cover some formulas; no claim of absolute historical novelty or independent certification is made.

## References

1. I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1, first publicly posted 15 October 2026. https://arxiv.org/html/2610.22248v1
2. P. Cadavid, M. L. Rodiño Montoya and P. M. Rodríguez, *On the isomorphisms between evolution algebras of graphs and random walks*, arXiv:1710.10516 (2017). https://arxiv.org/abs/1710.10516
3. X. García-Martínez and A. Pérez-Rodríguez, *A note on complete evolution algebras*, arXiv:2512.12418v1 (2025). https://arxiv.org/abs/2512.12418
4. X. Hu, *Triply Transitive Natural Permutation Images of Idempotent Evolution Algebras*, preprints.org:202610.0914 (2026), Sections 2–3. https://www.preprints.org/manuscript/202610.0914
