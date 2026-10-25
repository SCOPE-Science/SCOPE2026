# The first Ehrhart nonpositive sums of two hypersimplices: an exact dimension cutoff

## Finding

For integers \(n\ge2\) and \(1\le k,\ell\le n-1\), let
\[
\Delta_{k,n}=\{x\in[0,1]^n:\sum_{i=1}^n x_i=k\},\qquad
P_{n;k,\ell}=\Delta_{k,n}+\Delta_{\ell,n}.
\]
Every \(P_{n;k,\ell}\) is a lattice polytope of dimension \(n-1\). Its Ehrhart polynomial is written \(L_{n;k,\ell}(t)=\#(tP_{n;k,\ell}\cap\mathbb Z^n)\). All coefficients here refer to the ordinary monomial basis, including the strictly positive constant coefficient.

**Finite-dimensional sharp cutoff.** Every sum of two nontrivial hypersimplices with \(2\le n\le13\) has a strictly positive Ehrhart polynomial. At \(n=14\), exactly five parameter classes, modulo swapping the ranks and simultaneously replacing both by their complements, have a negative coefficient, and each has exactly one negative coefficient: the quadratic one. With the canonical representative \((k,\ell)=(k,14-r)\), the five classes and coefficients are

| \((k,r)\) | \([t^2]L_{14;k,14-r}(t)\) |
| --- | ---: |
| \((3,5)\) | \(-2743/118800\) |
| \((3,7)\) | \(-687323/79200\) |
| \((4,4)\) | \(-883961/29700\) |
| \((4,6)\) | \(-230425/2376\) |
| \((5,5)\) | \(-5523479/39600\) |

All other coefficients for these classes, and every coefficient of every other two-hypersimplex sum with \(n=14\), are strictly positive. The \((3,7)\) instance was already exhibited by Li and St. Dizier [1]; it is included for completeness, **not** proposed as a new counterexample. Thus dimension \(13\) is the first dimension admitting an Ehrhart-nonpositive Minkowski sum of two nontrivial hypersimplices. The scope is this particular family, not all generalized permutahedra or all Schubitopes.

## Assumptions and scope

An Ehrhart-positive lattice polytope is one whose ordinary power-basis Ehrhart coefficients are all strictly positive. Both ranks lie strictly between \(0\) and \(n\), so both hypersimplices are full-dimensional in the hyperplane of constant coordinate sum. Their Minkowski sum consequently has dimension \(n-1\), measured in its intrinsic affine lattice. Integer translations and unimodular affine reflections preserve its Ehrhart polynomial.

Interchanging \(k,\ell\) preserves \(P\); sending \(x\) to \(2\mathbf1-x\) exchanges \((k,\ell)\) with \((n-k,n-\ell)\). Every orbit has exactly one representative \((k,\ell)=(k,n-r)\) with
\[
1\le k\le r,\qquad k+r\le n.
\]
These conditions avoid omitted or doubly counted classes. They produce \(252\) parameter classes for \(2\le n\le14\), split into \(203\) at \(n\le13\) and \(49\) at \(n=14\).

## Proof

**1. Membership lemma valid for all ranks.** Fix a canonical triple \((n,k,r)\), write \(\ell=n-r\), and let \(t\ge0\). A vector \(x\in\mathbb R^n\) belongs to \(t(\Delta_{k,n}+\Delta_{\ell,n})\) if and only if
\[
0\le x_i\le2t,\qquad \sum_i x_i=(k+\ell)t,\qquad
\sum_i(x_i-t)_+\le kt.
\tag{1}
\]
The forward implication follows from \(x=u+v\), with \(0\le u_i,v_i\le t\), \(\sum u_i=kt\), and \(\sum v_i=\ell t\). Indeed, \((x_i-t)_+\le u_i\).

Conversely, let \(a_i=(x_i-t)_+\) and \(b_i=\min(t,x_i)\). To decompose \(x=u+v\) it is enough to find \(u_i\in[a_i,b_i]\) with \(\sum u_i=kt\). The lower endpoint sums to \(A=\sum a_i\le kt\). Since \(b_i=x_i-a_i\), the upper endpoint sums to \((k+\ell)t-A\ge\ell t\ge kt\), the last inequality using \(k+r\le n\). The interval of possible sums of the independent closed intervals \([a_i,b_i]\) therefore contains \(kt\). The chosen \(u\) and \(v=x-u\) satisfy all defining constraints. This proves (1), including degenerate boundaries.

**2. An exact finite counting identity.** Translate the dilation by \(-t\mathbf1\), writing \(y=x-t\mathbf1\). Then condition (1) becomes
\[
y_i\in[-t,t],\quad \sum_i y_i=(k-r)t,\quad
A(y)=\sum_i(y_i)_+\le kt.
\]
Let \(B(y)=\sum_i(-y_i)_+\). Necessarily \(B=A+(r-k)t\). Define \(C_t(s,a)\) as the number of ordered \(a\)-tuples of positive integers at most \(t\) having sum \(s\), with \(C_t(0,0)=1\) and \(C_t(s,0)=0\) for \(s\ne0\). For \(a\ge1\), upper-bounded stars and bars gives
\[
C_t(s,a)=\sum_{j=0}^{a}(-1)^j\binom aj
\binom{s-jt-1}{a-1},
\tag{2}
\]
where the binomial coefficient is zero whenever its upper argument is smaller than its lower nonnegative argument. Choose \(a\) positive and \(b\) negative coordinate positions, with disjoint supports, and then their positive integer magnitudes. The remaining \(n-a-b\) coordinates are zero. This yields, for each integer \(t\ge1\), the exact identity
\[
\boxed{L_{n;k,n-r}(t)=
\sum_{s=0}^{kt}\sum_{a+b\le n}
\binom{n}{a}\binom{n-a}{b}
C_t(s,a)C_t(s+(r-k)t,b).}
\tag{3}
\]
At \(t=0\), \(L(0)=1\). Every term in (3) counts one disjoint sign pattern and magnitude assignment, so no overcounting occurs.

**3. Polynomial reconstruction and exhaustive cutoff certificate.** Ehrhart's theorem makes \(L\) a polynomial of degree \(d=n-1\). Therefore the \(n\) exact values \(L(0),\ldots,L(n-1)\) determine it uniquely. If \(\delta_j=\sum_{i=0}^j(-1)^{j-i}\binom ji L(i)\) denotes its \(j\)-th forward difference, the exact Newton formula is
\[
L(t)=\sum_{j=0}^{n-1}\delta_j\binom tj.
\tag{4}
\]
Expanding each falling factorial into the power basis gives rational coefficients with exact integer arithmetic; this is not floating-point sampling. Equations (1)--(4), combined with the explicitly bounded enumeration of canonical parameter triples, constitute a terminating proof of all claimed signs. The included standalone `verify.py` recomputes every coefficient, requires strict positivity for all \(203\) classes with \(n\le13\), and requires the exact five exceptional classes with the exact displayed negative quadratic coefficients at \(n=14\). The complete list of \(252\) power-basis coefficient vectors is recorded in `coefficients.csv`; no rows or intermediate degrees are omitted. The source file implements (2)--(4) directly using arbitrary-precision integers and rational arithmetic.

**4. Independent count check.** The program separately counts, coordinate by coordinate, the integer \(y_i\in[-t,t]\) satisfying the displayed sum and positive-part budget. The dynamic programming state is \((\sum_{i\text{ processed}} y_i,\sum_{i\text{ processed}}(y_i)_+)\); its transition adds each of the \(2t+1\) possible next integer coordinates. This does not use the composition/binomial formula (3). It agrees with (3) in \(503\) independently evaluated cases, including degree-determining end dilations on the five exceptional classes. This independent check is supplemental: the finite exhaustive computation and identity (3), not extrapolation from those \(503\) tests, support the universal quantifiers stated above.

## Verification

The deliverable includes `verify.py` and `coefficients.csv` beside this file. On Python 3, run `python3 verify.py` in the directory containing both. Successful verification reports `EXACT_OK` with `orbits=252`, `low_dim_orbits=203`, `ambient_14_orbits=49`, `negative_classes=5`, and `independent_counts=503` and prints the five coefficients. It reconstructs the CSV and independently checks the lattice counts, so the certificate can be checked without third-party computational algebra packages. The provided CSV is not needed as an unverified oracle.

## Relationship to prior work

Li and St. Dizier [1, Sections 3--4] disproved Ehrhart positivity for Schubitopes, already giving the \(n=14\), \((k,\ell)=(3,7)\) example and its exact negative quadratic coefficient. Their published computation and polytope-membership method motivate this finite-dimension analysis. The present claim does not reclassify their example as new: it determines the least dimension **within all two-hypersimplex sums**, establishes positivity for all lower dimensions, and completely classifies the five symmetry classes at the first failure dimension. These conclusions require comparisons across \(252\) exact Ehrhart polynomials and are not asserted in [1].

Ferroni [2] proved Ehrhart positivity for individual hypersimplices; this does not imply positivity of their Minkowski sums. Jochemko and Ravichandran [3] established nonnegativity of the linear Ehrhart coefficient for generalized permutahedra, but this neither supplies the full higher-coefficient cutoff nor the five-class classification. The present enumeration is consistent with both results. Historical originality remains subject to broader independent bibliographic review.

## Limitations

The theorem concerns exactly two hypersimplex summands with nontrivial ranks and ambient dimension at most \(14\). It does not classify higher-dimensional sums, arbitrary numbers of summands, all Schubitopes, or all generalized permutahedra. The positivity in dimensions at most \(12\) is established by a complete finite calculation with a reproducible exact-arithmetic certificate, not by a uniform symbolic positivity formula in unbounded dimension. No independent scientific audit has been performed, and historical priority beyond the inspected primary sources is not guaranteed.

## References

1. Yupeng Li and Avery St. Dizier, *Schubitopes are not Ehrhart positive*, arXiv:2608.00377, first public version 2026-08-01; especially Sections 3--4, https://arxiv.org/html/2608.00377v2 .
2. Luis Ferroni, *Hypersimplices are Ehrhart Positive*, arXiv:1911.10146, https://arxiv.org/abs/1911.10146 .
3. Katharina Jochemko and Mohan Ravichandran, *Generalized permutahedra: Minkowski linear functionals and Ehrhart positivity*, *Mathematika* (2022), DOI:10.1112/mtk.12122 .
