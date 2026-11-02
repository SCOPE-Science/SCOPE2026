# Exact radical–socle profiles and a finite-field duality law for square-zero local modules

## Finding

Let \(q\) be any prime power, \(n\ge 2\), and \(\ell\ge 2\). Consider labeled \(n\)-dimensional modules over the local algebra
\[
R_{\ell,q}=\mathbb F_q[z_1,\ldots,z_\ell]/(z_i z_j:1\le i,j\le\ell).
\]
The radical generators act as ordered matrices \((A_1,\ldots,A_\ell)\) satisfying \(A_iA_j=0\) for all \(i,j\). Put \(I=\sum_i\operatorname{im} A_i\), \(K=\bigcap_i\ker A_i\), \(t=\dim I\), and \(k=\dim K\). Thus \(I\subseteq K\). For integers \(t,h\ge0\), define
\[
F_{\ell,q}(t,h)=\sum_{a=0}^{h}\sum_{b=0}^{t}(-1)^{a+b}q^{\binom a2+\binom b2}
{h\brack a}_q{t\brack b}_q q^{\ell(h-a)(t-b)}.
\]
Here \({u\brack v}_q\) is the Gaussian coefficient, with value zero outside \(0\le v\le u\). The **complete joint radical–socle distribution** is
\[
\boxed{N_{n,\ell,q}(t,k)={n\brack k}_q{k\brack t}_q F_{\ell,q}(t,n-k)}
\qquad(0\le t\le k\le n),
\]
and the count is zero for other \((t,k)\). These are counts of labeled module structures (matrices in a fixed basis), not of isomorphism classes.

Transposition gives a duality of the full distribution:
\[
\boxed{N_{n,\ell,q}(t,k)=N_{n,\ell,q}(n-k,n-t).}
\]
In particular, if \(n=2d+1\), the two balanced strata have **exactly equal counts for every prime power**, not merely asymptotically:
\[
\boxed{N_{2d+1,\ell,q}(d,d)=N_{2d+1,\ell,q}(d+1,d+1).}
\]

For fixed \(n,\ell\), let \(q\) tend to infinity through prime powers. If \(n=2d\), the unique asymptotically dominant profile is \((t,k)=(d,d)\), with probability \(1-O_{n,\ell}(q^{-1})\). If \(n=2d+1\), the two profiles \((d,d)\) and \((d+1,d+1)\) each have limiting probability \(1/2\), with all other profiles totaling \(O_{n,\ell}(q^{-1})\). The total number of module structures is
\[
q^{(\ell+1)\lfloor n^2/4\rfloor}\bigl(1+O_{n,\ell}(q^{-1})\bigr)
\]
for even \(n\), and twice this expression for odd \(n\). [In both cases the leading exponent is \((\ell+1)\lfloor n^2/4\rfloor\).]

## Assumptions and scope

All generators and matrices are over \(\mathbb F_q\), and their indexing is ordered. The radical and socle here are those of the represented module: \(JM=I\) and \(\operatorname{soc} M=K\). The formula works in all characteristics, including characteristic two; it is not restricted to algebraically closed fields. The asymptotic statement fixes \(n,\ell\) while varying \(q\). The hypothesis \(\ell\ge2\) is essential to the asserted dominant-profile law; the exact formula itself is also valid for one generator.

## Proof

**1. Matrix realization.** Since all products of radical generators vanish in \(R_{\ell,q}\), every module gives an ordered tuple with \(A_iA_j=0\). Conversely such a tuple uniquely determines the action of the finite-dimensional algebra. Its collective image \(I\) lies in its common kernel \(K\). For fixed subspaces \(I\subseteq K\subseteq\mathbb F_q^n\), with dimensions \(t,k\), each \(A_i\) factors uniquely as
\[
\mathbb F_q^n\longrightarrow \mathbb F_q^n/K\xrightarrow{B_i} I\hookrightarrow\mathbb F_q^n.
\]
By the definitions of \(I\) and \(K\), the tuple \((B_i)\) must satisfy \(\sum_i\operatorname{im} B_i=I\) and \(\bigcap_i\ker B_i=0\). Conversely both requirements guarantee that the prescribed \(I,K\) are **exactly**, rather than only inclusively, the collective image and common kernel.

**2. Möbius inversion.** Put \(h=n-k\). Among \(\ell\) arbitrary linear maps from an \(h\)-space to a \(t\)-space, enforce trivial common kernel by summing over kernel subspaces of dimension \(a\), and enforce full joint image by summing over codimension-\(b\) target subspaces. The Möbius value of an interval of codimension \(a\) in a vector-space subspace lattice is \((-1)^a q^{\binom a2}\); similarly for \(b\). There are \({h\brack a}_q\) domain subspaces and \({t\brack b}_q\) target subspaces. For fixed such subspaces, each map factors through an \((h-a)\)-space into a \((t-b)\)-space, yielding \(q^{\ell(h-a)(t-b)}\) tuples. Double Möbius inversion gives precisely \(F_{\ell,q}(t,h)\). There are \({n\brack k}_q{k\brack t}_q\) choices of \(K\supseteq I\), proving the formula without overcounting.

**3. Duality.** The transpose tuple also has pairwise zero products (indices reverse). The row rank of the stacked matrices is \(n-k\), so the transposed tuple has collective image dimension \(n-k\). Its common kernel dimension is \(n-t\), since the transposed stack's common kernel is the annihilator of the original collective image. Transposition is a bijection, proving the duality equation and the exact odd-dimensional balanced-stratum equality.

**4. Leading degrees.** For a feasible stratum set \(h=n-k\), so \(t+h\le n\). Its containing subspace-pair count has leading order \(q^{k(n-k)+t(k-t)}\). The unconstrained \(\ell\)-map count is \(q^{\ell th}\). Therefore an upper bound for the stratum degree is
\[
\delta(t,h)=n(t+h)-t^2-h^2+(\ell-1)th.
\]
For the balanced, full-rank profiles with \(t+h=n\), the collective kernel and collective cokernel restrictions each fail with probability \(O_{n,\ell}(q^{-1})\): a union bound over domain lines has at most \(O(q^{h-1-\ell t})\) failure probability, and a union bound over target hyperplanes has at most \(O(q^{t-1-\ell h})\). Since \(\ell\ge2\) and the balanced dimensions differ by at most one, both exponents are at most \(-1\) (when \(n\ge2\)). Thus the upper bound is attained with leading coefficient one.

Writing \(u=t+h\le n\) and \(v=h-t\), the upper bound becomes
\[
\delta=nu+\frac{\ell-3}{4}u^2-\frac{\ell+1}{4}v^2.
\]
For \(\ell\ge2\), \(u\mapsto nu+(\ell-3)u^2/4\) is strictly increasing on \([0,n]\). The largest possible bound occurs at \(u=n\) and minimal \(|v|\), namely the single balanced profile for even \(n\) or the two balanced profiles for odd \(n\). Every other integer profile has degree at most \((\ell+1)\lfloor n^2/4\rfloor-1\), by comparing \(u=n-1\) and the next admissible \(|v|\) to the balanced case. A finite sum of lower-degree stratum counts is therefore a relative \(O(q^{-1})\) contribution. Both odd balanced profiles have exactly equal cardinality by Step 3 and each has leading coefficient one. This proves all limiting probabilities and the stated leading total count.

## Verification

The supplied dependency-free `verify.py` builds every square-zero matrix in eight small prime-field configurations, constructs mutually annihilating ordered tuples, independently computes collective-image ranks and common-kernel dimensions by row reduction, and compares the resulting full table against the double-Möbius expression. It also checks odd-dimensional dual equality. Run `python3 verify.py` in the directory containing the extracted file; the recorded result was `VERIFY_OK`.

For example, when \((q,n,\ell)=(2,3,2)\), the count by \((t,k)\) is \((0,3):1\), \((1,1):42\), \((1,2):63\), \((2,2):42\), totaling \(148\). This finite example is a check, not a proof of the unrestricted theorem.

## Relationship to prior work

The **objects and qualitative geometry** are classical, and no claim is made to discovering their representation-theoretic stratification. Bleher–Chinburg–Huisgen-Zimmermann (2014, Theorem 3.12) explicitly treat this very \(\ell\)-loop square-zero algebra over algebraically closed fields; they classify irreducible components and generic radical/socle behavior. Morrison (1980, §5) treats the two-loop case by module types and open orbits. Schröer studies irreducible components of annihilating nilpotent pairs, a larger class including the two-loop square-zero locus. These works cover parts of the geometric backdrop and can anticipate which profiles are geometrically possible; the present claim is the **labeled finite-field count for every pair of exact radical and socle dimensions**, together with the exact duality of all finite-field profile multiplicities and its quantitative leading-coefficient consequences.

Huang (arXiv:2110.15566, first posted 2021-10-29) gives generating functions for pairs with \(AB=BA=0\), but does **not** impose every square \(A_i^2=0\) or refine by simultaneous image/kernel profiles, and concerns the nodal algebra rather than this square-zero local quotient. Deng–Hua (arXiv:2103.00636) count absolutely indecomposable quiver representations with nilpotent relations rather than these labeled radical/socle multiplicities. Bondarenko–Gerasimova–Sergeichuk (arXiv:0812.2155) give canonical forms for mutually annihilating pairs, not this exact joint point count. The subspace-Möbius technique itself is standard and is not claimed as new.

## Limitations

The result counts labeled modules, not isomorphism classes, indecomposable classes, or finer Jordan-type distributions. For \(\ell=1\) the exact count remains correct but the dominance statement must be modified. The asymptotics are in field size, not module dimension. Other literature might contain the same finite-field double-rank refinement under the language of subspace arrangements or Hall algebras, despite the directly inspected sources not stating it; exhaustive priority and independent validation are not claimed.

## References

- Yifeng Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity*, arXiv:2110.15566 (first public version 2021-10-29), https://arxiv.org/abs/2110.15566.
- Frauke M. Bleher, Ted Chinburg, Birge Huisgen-Zimmermann, *The geometry of finite dimensional algebras with vanishing radical square*, arXiv:1407.3045 (2014), especially §3.C, Theorem 3.12, https://arxiv.org/abs/1407.3045.
- Bangming Deng, Jiuzhao Hua, *Counting Representations of Quivers Respecting Nilpotent Relations over Finite Fields*, arXiv:2103.00636 (2021), https://arxiv.org/abs/2103.00636.
- Kent Morrison, *The Scheme of Finite Dimensional Representations of an Algebra*, §5 (1980), https://aimath.org/~morrison/Research/SchemeFinDimReps.pdf.
- Jan Schröer, *Varieties of Pairs of Nilpotent Matrices Annihilating Each Other*, arXiv:math/0211293 (2002), https://arxiv.org/abs/math/0211293.
- V. M. Bondarenko, T. V. Gerasimova, V. V. Sergeichuk, *Pairs of mutually annihilating operators*, arXiv:0812.2155 (2008), https://arxiv.org/abs/0812.2155.
