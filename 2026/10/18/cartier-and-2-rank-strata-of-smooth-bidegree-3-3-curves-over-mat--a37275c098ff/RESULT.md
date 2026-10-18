# Cartier and \(2\)-rank strata of smooth bidegree-\((3,3)\) curves over \(\mathbf F_2\)

## Finding
Let \(S=\mathbf P^1_{\mathbf F_2}\times\mathbf P^1_{\mathbf F_2}\) and let \(\mathcal C\) denote the set of nonzero sections \(F\in H^0(S,\mathcal O_S(3,3))\) whose vanishing curves \(C_F\) are geometrically smooth. Such a curve has genus \(4\). Write \(f(C_F)\) for the \(2\)-rank of its Jacobian and \(a(C_F)\) for the \(a\)-number, equivalently the dimension of the kernel of Frobenius on \(H^1(C_F,\mathcal O_{C_F})\). The **complete joint distribution**, with equations and \(\mathbf F_2\)-isomorphism classes counted separately, is

| \(f\) | \(a\) | Nonzero equations | Isomorphism classes |
|---:|---:|---:|---:|
| 0 | 1 | 1,008 | 18 |
| 1 | 1 | 720 | 12 |
| 2 | 1 | 1,728 | 32 |
| 3 | 1 | 3,528 | 51 |
| 4 | 0 | 9,036 | 139 |
| **Total** | | **16,020** | **252** |

In particular, **every geometrically smooth bidegree-\((3,3)\) curve on the split quadric over \(\mathbf F_2\) has \(a\)-number at most one**, and the only nonordinary \(a\)-number is exactly one. The ordinary locus contains \(9,036\) defining equations in \(139\) isomorphism classes. This concerns the split-quadric family over \(\mathbf F_2\), not all characteristic-two genus-four curves or all genus-four curves over \(\mathbf F_2\).

## Assumptions and scope
Throughout \(k=\mathbf F_2\). Fix homogeneous coordinates \([U:V]\) and \([S:T]\) on the two factors. Each nonzero section is uniquely
\[
F=\sum_{0\le i,j\le3}c_{ij}\,U^iV^{3-i}S^jT^{3-j},\qquad c_{ij}\in k,
\]
and is encoded by the positive integer \(m=\sum_{i,j}c_{ij}2^{4i+j}\), with \(1\le m\le65,535\). There is no quotient by rescaling because \(k^\times=\{1\}\). "Smooth" means smooth over \(\overline{k}\), not merely at all \(k\)-rational points. We count abstract \(k\)-isomorphism classes only **within this split-quadric family**.

For \(F\) smooth, its canonical sheaf is \(\omega_{C_F}\cong\mathcal O_{C_F}(1,1)\). The canonical embedding determines a unique containing smooth quadric; hence an abstract \(k\)-isomorphism between two curves in this family extends to an automorphism of \(S\). Such automorphisms form \(\operatorname{PGL}_2(k)^2\rtimes C_2\), of order \(72\). Consequently coefficient orbits under this group coincide with abstract isomorphism classes in this family.

## Proof
**1. The Hasse–Witt calculation.** The sequence
\[
0\longrightarrow\mathcal O_S(-3,-3)\xrightarrow{F}\mathcal O_S\longrightarrow\mathcal O_{C_F}\longrightarrow0
\]
identifies \(H^1(C_F,\mathcal O_{C_F})\) with \(H^2(S,\mathcal O_S(-3,-3))\). On the standard Čech cover the latter has the four basis classes
\[
e_{ij}=x^{-i}y^{-j},\qquad i,j\in\{1,2\},
\]
where \(x=U/V\) and \(y=S/T\). Absolute Frobenius on the curve is induced by taking second powers and multiplying by \(F\) on the ambient top-cohomology model. Thus, after fixing the ordered basis \((e_{11},e_{12},e_{21},e_{22})\), the matrix \(H(F)\) of Frobenius has entries
\[
H(F)_{(k,\ell),(i,j)}=c_{2i-k,\,2j-\ell},\qquad i,j,k,\ell\in\{1,2\},
\]
where coefficients outside the range \(0,\ldots,3\) are zero. Each entry is a particular one of the \(16\) binary input coefficients. The formula agrees, up to simultaneous ordering of the basis, with the characteristic-two Hasse–Witt formula used by Dragutinović. The equality \(a(C_F)=4-\operatorname{rank}H(F)\) follows from the Frobenius/Cartier duality. Because every coefficient lies in \(\mathbf F_2\), Frobenius iterates have ordinary matrix product, so
\[
f(C_F)=\operatorname{rank}H(F)^4.
\]
This is the stable rank of the \(4\)-dimensional Frobenius module; exponent four suffices by Fitting decomposition.

**2. Exhaustive negative certificates.** The finite coefficient space contains \(2^{16}-1=65,535\) nonzero sections. `enumerate.cpp` loops through all geometric points of the four standard affine charts with coordinates over \(\mathbf F_{2^m}\), for each \(1\le m\le6\). At each point the simultaneous equations \(F=F_x=F_y=0\) are **linear equations in the sixteen coefficients over \(\mathbf F_2\)**. Their full binary kernels are enumerated by exact Gaussian elimination and marked singular. For each marked section a concrete tuple \((m,x,y)\), including which coordinates are infinity, is recorded in `singular_witnesses.tsv`. Exactly \(49,515\) sections receive negative witnesses. The separate program `verify_witnesses.py` checks the irreducibility of each field polynomial and recomputes all three vanishing conditions directly for all \(49,515\) witnesses. Only \(16,020\) sections remain unlabelled at this stage. Importantly, failure to find a singular point through degree six is **not** used to infer geometric smoothness.

**3. Geometric positive certificates.** `orbits.py` constructs the full \(72\)-element automorphism group by tensor-product actions on the two binary cubic spaces and interchange of the two factors. It partitions the \(16,020\) survivors into exactly \(252\) orbits, with orbit-size frequencies \(6:1,\ 12:2,\ 18:3,\ 24:7,\ 36:40,\ 72:199\). For every orbit representative, and on each of all four affine charts, it computes the exact reduced Gröbner basis of
\[
\bigl(F,\partial_xF,\partial_yF\bigr)\subset\mathbf F_2[x,y].
\]
In all \(252\times4=1,008\) cases this ideal is the unit ideal. By the geometric Jacobian criterion this excludes singular points over **every** extension and over the algebraic closure. Thus every one of the \(16,020\) survivors is geometrically smooth. Every other nonzero form has an independently checkable singular witness, establishing that the census is complete.

**4. Invariant and orbit enumeration.** On every smooth mask the C++ implementation constructs \(H(F)\), computes \(4-\operatorname{rank}H(F)\) and \(\operatorname{rank}H(F)^4\), and tallies the results. Independently, `classify.py` constructs \(H(F)\) with separately written binary linear algebra and multiplies each class invariant by its orbit size from `orbit_reps.txt`. Both computations give the displayed five bins and their class counts. The row total is \(16,020\) equations and \(252\) classes. In particular, none of the \(252\) smooth orbits has \(\operatorname{rank}H(F)\le2\), which proves the claimed \(a\)-number bound.

## Verification
The complete original bytes of the four programs, their input certificates, and their recorded outputs accompany this result. A portable replay from the package's extraction directory is:

```sh
g++ -O3 -std=c++17 enumerate.cpp -o enumerate
./enumerate > enumeration.txt 2> enum_stderr.txt
python3 orbits.py > orbit_output.txt
python3 verify_witnesses.py > verify_output.txt
python3 classify.py > classify_output.txt
```

`enumerate.cpp` regenerates `candidates.txt` and `singular_witnesses.tsv`; `orbits.py` regenerates `orbit_reps.txt`; `classify.py` regenerates `statistics.txt`. The direct-witness checker does not trust the kernel enumerator: it substitutes each encoded section into the three defining singularity equations. The positive Gröbner checks do not trust bounded-degree sampling: they test ideals over the polynomial ring. The separate invariant tally is by orbit representatives, whereas the C++ tally is by every smooth form. The saved log files give the actual output of these operations, and the main count agrees in both routes.

## Relationship to prior work
Xarles (first publicly posted 15 July 2020) enumerated genus-four \(\mathbf F_2\)-isomorphism classes and gave arithmetic data, including L-polynomials. Its pre-existing classification is the starting background; we do **not** claim discovery of the \(252\) split-quadric isomorphism classes, the \(16,020\) smooth equations, or the existence of the five possible \(2\)-ranks in isolation. In principle \(2\)-rank information can be recovered from Weil polynomials, so the \(2\)-rank margins alone are also not our originality claim.

Camacho-Navarro studies genus-four Cartier data and gives calculations in odd residue characteristics, but her inspected examples do not tabulate this binary split-quadric family. Dragutinović studies genus-four characteristic-two Ekedahl–Oort strata, gives the same Hasse–Witt matrix for the \((3,3)\) model, and proves a **pre-existing** impossibility for type \([4,3]\) of a Jacobian of a smooth genus-four curve; those are not claimed as new. The precise additional assertion here is the complete **joint** equation-weighted and isomorphism-weighted \((2\text{-rank},a\text{-number})\) distribution for all smooth split-quadric curves over the smallest field, and in particular the absence of **every** \(a\ge2\) within that finite family. Neither checked work presented that exact complete five-bin distribution.

## Limitations
This is a result about the split smooth-quadric family over precisely \(\mathbf F_2\). It does not claim the same bound over extensions, other finite fields, on nonsplit or singular quadrics, or for hyperelliptic curves. It does not classify full Ekedahl–Oort types beyond the stated \((f,a)\) invariants. Completeness rests on reproducible exact finite arithmetic together with the verified four-chart Gröbner tests, not on a symbolic characteristic-independent classification. A full human priority audit has not been performed: a derived table from previously published electronic census data or an unindexed equivalent calculation could predate this enumeration. No independent scientific audit is claimed.

## References
1. X. Xarles, *A census of all genus 4 curves over the field with 2 elements*, arXiv:2007.07822v1 (2020-07-15), especially the trigonal classification and arithmetic tables.
2. C. Camacho-Navarro, *The a-number, p-rank and Cartier points of genus 4 curves*, arXiv:2012.08705v1 (2020-12-16), methods and studied characteristics.
3. D. Dragutinović, *Supersingular curves of genus four in characteristic two*, arXiv:2301.12897v1 (2023-01-30); Proc. Amer. Math. Soc. 152 (2024), 2333–2347, DOI 10.1090/proc/16792; characteristic-two Hasse–Witt matrix, EO restrictions, and \(\mathbf F_2\) data.
