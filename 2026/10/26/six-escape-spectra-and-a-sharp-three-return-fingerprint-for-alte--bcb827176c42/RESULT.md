# Six escape spectra and a sharp three-return fingerprint for alternating dyadic holes

## Finding

For the binary doubling map, fix **two** length-three dyadic cylinders of equal Lebesgue measure \(1/8\). Remove the first cylinder at even times and the second at odd times. Among all \(8^2=64\) ordered choices, the survivor entropy, Lebesgue escape rate, and time-two symbolic dynamical zeta function fall into **exactly six distinct classes**. The classes, their multiplicities, and their complete zeta denominators are:

| Class | Schedules | \(Q(z)\), the time-two zeta denominator | \((F_1,F_2,F_3)\) | Perron root \(\rho\) (approx.) |
|---|---:|---|---|---:|
| A | 8 | \(1-4z+4z^2-z^3\) | \((4,8,19)\) | 2.618034 |
| B | 16 | \(1-3z+z^3\) | \((3,9,24)\) | 2.879385 |
| C | 12 | \(1-2z-3z^2-z^3\) | \((2,10,29)\) | 3.079596 |
| D | 8 | \(1-4z+3z^2-z^3\) | \((4,10,31)\) | 3.147899 |
| E | 16 | \(1-3z-z^2+z^3\) | \((3,11,33)\) | 3.214320 |
| F | 4 | \(1-3z-z^2-z^3\) | \((3,11,39)\) | 3.382976 |

Here \(F_j=|\operatorname{Fix}(\sigma^{2j}|_{X_{u,v}})|\), and \(\rho\) is the spectral radius of the period-two transition matrix. For every schedule in each row,
\[
\zeta_{u,v}(z)=\frac1{Q(z)},\qquad
h_{u,v}=\frac12\log\rho,\qquad
\gamma_{u,v}=\log2-\frac12\log\rho.
\]
The six values are strictly ordered A through F by increasing entropy (and decreasing escape rate).

The extremal survivor entropies are exactly \(\log\varphi\) and \(\log\tau\), where \(\varphi\) is the positive root of \(t^2-t-1\) and \(\tau\) the positive root of \(t^3-t^2-t-1\). Precisely eight schedules attain \(\log\varphi\), and precisely four attain \(\log\tau\). Therefore the largest and smallest escape rates are \(\log(2/\varphi)\) and \(\log(2/\tau)\), respectively. Notably, the *alternating complementary* holes `001:110` and the static hole `001:001` have identical dynamical zeta functions; similarly `010:101` and `000:000` have identical dynamical zeta functions, even though their holes move differently.

**Sharp short-period determination.** The fixed-point counts \((F_1,F_2,F_3)\), corresponding to return periods two, four, and six of the underlying shift, uniquely determine which of the six zeta functions occurs, hence all periodic-point counts and escape rates. The first two counts do **not** suffice: `000:000` and `000:001` both have \((F_1,F_2)=(3,11)\), but their third counts are \(39\) and \(33\). Thus the third return is the earliest universal complete fingerprint among all 64 schedules.

## Assumptions and scope

A binary word \(u=u_0u_1u_2\) represents the half-open dyadic interval \(H_u=[j/8,(j+1)/8)\subset[0,1)\), where \(j=4u_0+2u_1+u_2\). The interval map is \(T(x)=2x\pmod1\). For a pair of length-three words \((u,v)\), a point survives \(n\) tests if \(T^i(x)\notin H_u\) at even \(i<n\) and \(T^i(x)\notin H_v\) at odd \(i<n\). The Lebesgue escape rate is the limit of minus the logarithm of this survival probability divided by \(n\), when \(n\to\infty\).

For exact topological and periodic-orbit statements, use the **two-sided phase-labelled symbolic survivor**
\[
X_{u,v}=\{x\in\{0,1\}^{\mathbb Z}: (x_i,x_{i+1},x_{i+2})\ne u\text{ if }i\text{ is even, and }\ne v\text{ if }i\text{ is odd}\}.
\]
It is invariant under \(\sigma^2\), not necessarily under \(\sigma\). The reported entropy \(h_{u,v}\) is one half the entropy of \(\sigma^2|_{X_{u,v}}\). The dynamical zeta function is that of \(\sigma^2\) on this symbolic system, **not** an assertion that boundary conventions preserve every periodic point of the interval doubling map. Dyadic boundary codings have Lebesgue measure zero and do not alter the escape rate or entropy.

## Proof

**1. Exact transfer and symbolic conjugacy.** Order the two-bit states as `00`, `01`, `10`, `11`. For a forbidden three-bit word \(w\), define the four-by-four integer matrix \(M_w\) by
\[
(M_w)_{(a,b),(b,c)}=\begin{cases}0,&(a,b,c)=w,\\1,&(a,b,c)\ne w,\end{cases}
\]
and set all nonoverlapping entries to zero. Exactly one transition of the full binary two-block de Bruijn graph is removed. Put \(P_{u,v}=M_uM_v\). A bi-infinite compatible path in its period-two graph uniquely specifies a binary survivor sequence and conversely, because each adjacent state overlaps in one bit. Consequently the time-two symbolic survivor is an edge/vertex shift for \(P_{u,v}\), and the standard finite-state path trace identity (which also follows by directly counting closed paths) gives
\[
F_j=\operatorname{tr}(P_{u,v}^{j}),\qquad
\zeta_{u,v}(z)=\det(I-zP_{u,v})^{-1}.
\]
The initial two bits give four possible starting states, and each extra transition appends one bit. Hence after \(n\) hole tests the **exact** Lebesgue survival probability is
\[
2^{-n-2}\boldsymbol1^{\mathsf T}
 M_{w_0}M_{w_1}\cdots M_{w_{n-1}}
 \boldsymbol1,\qquad w_i=\begin{cases}u,&i\text{ even},\\v,&i\text{ odd}.\end{cases}
\]
Every vector entry is nonnegative. Matrix-norm growth under repeated two-step transfer implies the logarithmic escape limit exists and equals \(\log2-\frac12\log\rho(P_{u,v})\); finite initial and final vectors cannot remove the top nonnegative spectral growth. The entropy formula follows from finite-state path growth.

**2. Exact finite classification without spectral fitting.** Complementing both words, exchanging the two temporal phases, and reversing both three-bit words preserve the symbolic periodic-point counts and entropy. These involutions generate orbits among all ordered word pairs. The following is a complete and disjoint list of representatives, with orbit size and zeta class; orbit sizes sum to \(64\):

| Representative | Orbit size | Class | Representative | Orbit size | Class |
|---|---:|---|---|---:|---|
| `000:000` | 2 | F | `000:001` | 8 | E |
| `000:010` | 4 | C | `000:011` | 8 | B |
| `000:101` | 4 | C | `000:111` | 2 | C |
| `001:001` | 4 | A | `001:010` | 8 | E |
| `001:011` | 4 | D | `001:100` | 4 | D |
| `001:101` | 8 | B | `001:110` | 4 | A |
| `010:010` | 2 | C | `010:101` | 2 | F |

A direct four-by-four integer multiplication and determinant evaluation for each representative gives the six \(Q(z)\) values in the Finding table. It is enough to compute any representative in an orbit: bit complement relabels states, phase interchange preserves nonzero eigenvalues of \(M_uM_v\) and \(M_vM_u\), and reversal conjugates the time-two shift to its inverse while preserving period parity of a length-three test. Thus the orbit table establishes the claimed classification **exhaustively**, not by sampling larger periods or fitting numerical roots. The standalone `verify.py` recomputes all 64 determinants from first principles and checks the orbit partition.

**3. Ordering and extrema.** Since each \(M_w\) equals the full two-block adjacency matrix minus a rank-one matrix, \(\operatorname{rank}(P_{u,v})\le3\). Thus \(\det(I-zP)\) has degree at most three, with the listed characteristic polynomial \(\lambda^4Q(1/\lambda)\). Nonnegative-matrix theory gives a positive Perron eigenvalue; each of the six cubic factors has exactly one real root above \(5/2\). Exact rational sign calculations isolate their largest positive roots in the mutually disjoint intervals \((2.61,2.63)\), \((2.87,2.89)\), \((3.07,3.09)\), \((3.14,3.15)\), \((3.21,3.22)\), and \((3.38,3.39)\), respectively. The derivatives of the cubic factors are strictly positive for \(\lambda\ge5/2\), hence these are the Perron roots and their ordering is rigorous. For class A,
\(Q(z)=(1-z)(1-3z+z^2)\), so \(\rho=\varphi^2\). For class F, if \(\tau^3=\tau^2+\tau+1\), then \(\rho=\tau^2\), as verified by substitution into \(\lambda^3-3\lambda^2-\lambda-1=0\). The extremal counts follow from the representative orbit sizes.

**4. Sharp three-return fingerprint.** Newton's identities reconstruct all coefficients of \(Q(z)\) from \(\operatorname{tr}P\), \(\operatorname{tr}P^2\), and \(\operatorname{tr}P^3\) because \(\det P=0\). The six fixed-point triples in the table are distinct. The exhibited pair with equal first two counts and unequal third count proves the cutoff three is optimal.

## Verification

Running `python verify.py` uses only the Python standard library. It independently enumerates all 64 ordered pairs, forms de Bruijn transfer matrices, computes \(\det(I-zP)\) from signed principal minors, constructs all 14 symmetry orbits, and verifies the six class multiplicities. It also directly enumerates all binary strings for \(n=0,\ldots,8\) hole tests (576 exact comparisons) and all periodic strings for return periods \(j=1,\ldots,5\) (320 exact comparisons). The calculations additionally check exact rational brackets isolating the six Perron roots. Finite checks certify the **finite 64-case determinant classification** and corroborate the general trace and survival identities; the displayed algebra gives the proof of all-period formulas.

## Relationship to prior work

Georgiou, Dettmann and Altmann (2012) analyze finite Markov holes and their dependence on periodic overlaps for a static-hole setting. Livorati, Georgiou, Dettmann and Leonel (2013) investigate periodic moving and breathing holes of the doubling map, using Ulam approximations and analytical overlap estimates rather than an exact 64-schedule three-bit zeta census. Bonanno, Cristadoro and Lenci (2021) classify maximal escape for **one fixed forbidden word**, not alternating two-word phase constraints. General transfer matrices, de Bruijn graphs, and zeta determinants are established tools and are **not** asserted to be new. The contribution claimed here is the exact six-stratum exhaustive phase diagram and the sharp three-return distinguishing property for the canonical period-two, depth-three moving-hole family.

## Limitations

This is an exact classification for binary length-three cylinders with time period two. It is not a classification for arbitrary cylinder lengths, general continuous moving holes, or general periods; it does not assert conjugacy between schedules that share a zeta function. Symbolic periodic counts do not automatically coincide with interval periodic counts at binary endpoints. Although relevant primary sources were inspected, an earlier equivalent finite enumeration could exist; priority needs independent literature verification.

## References

1. O. Georgiou, C. P. Dettmann, E. G. Altmann, *Faster than expected escape for a class of fully chaotic maps*, arXiv:1207.7000 (first public 2012-07-30). https://arxiv.org/abs/1207.7000
2. A. L. P. Livorati, O. Georgiou, C. P. Dettmann, E. D. Leonel, *Escape through a time-dependent hole in the doubling map*, arXiv:1312.7030 (first public 2013-12-25). https://arxiv.org/abs/1312.7030
3. C. Bonanno, G. Cristadoro, M. Lenci, *Maximal escape rate for shifts*, arXiv:2112.14248 (first public 2021-12-28). https://arxiv.org/abs/2112.14248
4. Standard finite-type symbolic dynamics: de Bruijn path presentations, matrix Perron theory and the Artin–Mazur trace/determinant identity (background methods only).
