# Cyclotomic Frobenius classification of the Klein quartic's bitangents in odd characteristic

## Finding

Let \(p\) be any odd prime other than \(7\), and let \(C_p\subset\mathbb P^2_{\mathbb F_p}\) be the smooth Klein-model plane quartic
\[
C_p:\quad X^3Y+Y^3Z+Z^3X=0.
\]
Let \(B_p\) denote its finite reduced scheme of geometric bitangent lines, where a hyperflex line meeting the quartic with multiplicity four at one point is included. The degree of \(B_p\) is \(28\). The exact Frobenius orbit distribution is

| \(p\pmod 7\) | Orbits of Frobenius on the \(28\) bitangents | \(\#B_p(\mathbb F_p)\) | Smallest common splitting extension |
|---|---|---:|---|
| \(1\) | \(1^{28}\) | \(28\) | \(\mathbb F_p\) |
| \(6\) | \(1^4 2^{12}\) | \(4\) | \(\mathbb F_{p^2}\) |
| \(2,4\) | \(1^1 3^9\) | \(1\) | \(\mathbb F_{p^3}\) |
| \(3,5\) | \(1^1 3^1 6^4\) | \(1\) | \(\mathbb F_{p^6}\) |

Equivalently, for all \(m\geq1\),
\[
\#B_p(\mathbb F_{p^m})=1+3\mathbf1_{p^m\equiv1\,\mathrm{or}\,6\pmod7}+24\mathbf1_{p^m\equiv1\pmod7}.
\]
The zeta functions of \(B_p\), in the same four rows, are
\[
(1-T)^{-28},\qquad (1-T)^{-4}(1-T^2)^{-12},\qquad
(1-T)^{-1}(1-T^3)^{-9},\qquad
(1-T)^{-1}(1-T^3)^{-1}(1-T^6)^{-4}.
\]
Over characteristic zero, the splitting field of all \(28\) bitangents of the same Klein-model quartic is exactly \(\mathbb Q(\zeta_7)\); its six Galois actions on the bitangents have the displayed residue-class cycle profiles. No result here concerns the different arithmetic models obtained by coordinate changes over extensions, nor the characteristic-two seven-bitangent configuration or the singular characteristic-seven plane model.

## Assumptions and scope

Here \(\zeta=\zeta_7\) is a primitive seventh root of unity, \(K=\mathbb Q(\zeta)\), \(\Phi_7(t)=1+t+\cdots+t^6\), and \(R=\mathbb Z[\zeta,1/7]\). All projective-line coordinates below are normalized in the dual affine chart with nonzero coefficient of \(Z\): a line is \(Z+aX+bY=0\). Calculations over \(K\) are exact, using the basis \(1,\zeta,\ldots,\zeta^5\), not numerical approximations. All statements about arithmetic Frobenius concern the literal displayed plane equation over \(\mathbb F_p\).

## Proof

**1. Smoothness.** At a singular geometric point of the quartic the three partial derivatives are
\[
3X^2Y+Z^3,\qquad X^3+3Y^2Z,\qquad Y^3+3Z^2X.
\]
If any coordinate vanishes, all three gradients force all coordinates to vanish, impossible projectively. If all coordinates are nonzero, multiplying the three gradient equations yields \(28(XYZ)^3=0\). Thus no singularity exists in the stated odd characteristics other than possibly \(7\), which is excluded. A smooth plane quartic in characteristic different from two has precisely \(28\) geometric bitangents (allowing hyperflexes).

**2. Exact integral orbit.** The line \(\ell_0:X+Y+Z=0\) is a bitangent because
\[
F(X,Y,-X-Y)=-(X^2+XY+Y^2)^2,
\qquad F=X^3Y+Y^3Z+Z^3X.
\]
Define \(t_1=\zeta-\zeta^6\), \(t_2=\zeta^2-\zeta^5\), \(t_3=\zeta^4-\zeta^3\), and the matrices
\[
D=\operatorname{diag}(\zeta^4,\zeta^2,\zeta),\quad
H=\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix},\quad
T=\begin{pmatrix}t_1&t_2&t_3\\t_2&t_3&t_1\\t_3&t_1&t_2\end{pmatrix}.
\]
They induce projective automorphisms of the Klein quartic (the classical Klein group matrices). Direct computation in \(\mathbb Z[\zeta]/(\Phi_7)\) gives \(T^2=-7I\) and \(F(Tv)=49F(v)\); the other two matrices preserve \(F\) exactly. Apply the matrices on the right to row vectors of line coefficients, and normalize the last coordinate to \(1\) after every operation. Exact polynomial reduction modulo \(\Phi_7\) yields a closed orbit of precisely \(28\) distinct vectors \((a_i,b_i,1)\). Moreover, every coefficient \(a_i,b_i\) lies in \(\mathbb Z[\zeta]\) without denominators. Each vector gives a bitangent, because the group generators preserve the curve. The included exact verifier independently checks the square restriction equations for all \(28\) lines, and the entire orbit is generated without relying on an unverified list.

**3. Distinct reduction at every permitted prime.** For each pair of different lines, compute the two integer norms \(N_{K/\mathbb Q}(a_i-a_j)\) and \(N_{K/\mathbb Q}(b_i-b_j)\). If the two lines coincided modulo any prime ideal over a rational prime \(p\), then \(p\) would divide both norms. Exhaustive exact integer resultants show that every prime factor of every pairwise greatest common divisor belongs to
\[
\{2,7,29,43,71\}.
\]
For \(p=29,43,71\), all six primitive seventh roots lie in \(\mathbb F_p\); substituting each of them in every one of the \(28\) normalized vectors gives \(28\) distinct reductions in each of the eighteen complete residue tests. Thus no two vectors collide for any odd prime different from \(7\). The \(28\) integral orbit members exhaust all geometric bitangents for every such characteristic. This also independently certifies geometric completeness in the potentially problematic primes \(29,43,71\), where a single-coordinate eliminant may have repeated roots.

**4. Cyclotomic Galois action.** For \(r\in(\mathbb Z/7\mathbb Z)^\times\), the automorphism \(\sigma_r\) of \(K\) sends \(\zeta\) to \(\zeta^r\). It permutes the exact list of \(28\) coefficient pairs. Exhaustive substitution and equality checks in \(K\) give the cycle profiles
\[
\begin{array}{c|c}
r&\text{cycle profile}\\\hline
1&1^{28}\\
2,4&1^1 3^9\\
3,5&1^1 3^1 6^4\\
6&1^4 2^{12}
\end{array}
\]
The presence of a six-cycle shows that \(K\) is exactly the characteristic-zero splitting field, not merely an upper bound. For each \(p\ne2,7\), the cyclotomic extension is unramified and arithmetic Frobenius sends \(\zeta\) to \(\zeta^p\) modulo any prime above \(p\). Because distinct reductions were established for every permitted prime, the same permutation profiles describe geometric bitangents over \(\mathbb F_p\). The splitting degrees and zeta functions follow from the lengths of Frobenius cycles. For any extension degree \(m\), taking the \(m\)-th power of Frobenius gives the displayed point-count formula.

## Verification

The reproducible script `verify.py` uses SymPy's exact rational polynomial and resultant arithmetic. It constructs the orbit using the three explicit matrices, checks the quartic identities, checks the binary-quartic square conditions at all \(28\) lines, reconstructs all six Galois cycle profiles, computes the pairwise norm sieve for every unordered pair, checks all exceptional prime roots, and independently counts rational bitangents over nine representative prime fields. Running `python verify.py` with `requirements.txt` installed yields the captured exact output in `verify.out`, ending in `VERIFY_OK`. The computationally exhaustive steps are finite and the reduction argument turns them into statements valid for every allowed prime; the finite sample field counts are corroboration, not the proof of the universal claim.

## Relationship to prior work

Klein's and Elkies's explicit representation matrices, rational bitangent, and geometric order-168 symmetry are essential antecedents. Plaumann–Sturmfels–Vinzant give general exact bitangent algorithms, not this prime-by-prime arithmetic classification. Janasz–Pokora–Zieliński compute complex incidence properties of the Klein bitangent arrangement, not its cyclotomic Frobenius permutation. Elsenhans–Jahnel study abstract admissible Galois actions on bitangents, not this model's complete finite-field distribution. A previous computation for the literal Klein model over \(\mathbb F_5\) gives the \(p\equiv5\pmod7\) row and is strictly subsumed here. The contribution is the complete uniform modulo-seven law over every odd prime outside the bad reduction, including a distinct-reduction certificate at all primes and the exact characteristic-zero splitting field. It is not a claim to originality of the underlying automorphism matrices or the fact that plane quartics possess \(28\) bitangents.

## Limitations

This concerns one particular rational plane model; coordinate changes defined over extensions can yield different arithmetic forms, and results for isomorphic curves over algebraic closures must not be silently transferred to their base-field line schemes. Characteristic two has only seven geometric bitangents; the displayed characteristic-seven plane equation is singular. The geometric and arithmetic results are proved with exact finite certificates and classical facts, but historical priority remains subject to independent literature verification; especially, the classical group representation already makes the Frobenius calculation possible in principle. Integral formulas and the finite prime verification are reproducible, but independent scientific audit has not been performed.

## References

- N. D. Elkies, *The Klein Quartic in Number Theory*, MSRI Publications 35 (1998), especially Sections 1.1, 1.3, 2.2 and 3.3, https://library.slmath.org/books/Book35/files/elkies.pdf.
- D. Plaumann, B. Sturmfels and C. Vinzant, *Quartic Curves and Their Bitangents*, first public arXiv submission 2010-08-24, https://arxiv.org/abs/1008.4104.
- M. Janasz, P. Pokora and M. Zieliński, *On arrangements of smooth plane quartics and their bitangents*, first public arXiv submission 2023-08-31, https://arxiv.org/abs/2308.16514.
- A.-S. Elsenhans and J. Jahnel, *On plane quartics with a Galois invariant Steiner hexad*, first public arXiv submission 2017-07-31, https://arxiv.org/abs/1708.00071.
