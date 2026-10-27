# Nine-sheeted extremal Belyi covers: 900 isomorphism classes and their deck groups

## Finding

There are exactly \(900\) isomorphism classes over \(\mathbb C\) of connected covers
\(f:C\to\mathbb P^1\) of degree \(9\) having a single point of ramification index
\(9\) over each of the **fixed, labeled** target points \(0,1,\infty\) and no other branch points.
Every source curve has genus \(4\), so these attain the lower bound \(\deg(f)=2g(C)+1\).
The distribution of deck-transformation-group orders, retaining the map to the labeled target, is
\[
\begin{array}{c|rrr}
|\operatorname{Aut}(f)|&1&3&9\\ \hline
\#\text{ isomorphism classes}&895&2&3
\end{array}.
\]
In particular the total number is \(895+2+3=900\). The two nontrivial group types are necessarily cyclic.

## Assumptions and scope

All curves and covers are smooth, projective and connected over \(\mathbb C\). An isomorphism
of covers is an isomorphism of source curves commuting with \(f\); it does **not** permute
\(0,1,\infty\) or modify the target coordinate. The prescribed ramification passport is
\(((9),(9),(9))\). Such a triple of branch-cycle permutations is transitive automatically.
Riemann--Hurwitz gives \(2g-2=-18+3(9-1)=6\), hence \(g=4\).

## Proof

**Monodromy reduction.** By the Riemann existence correspondence, the covers are conjugacy
classes of triples \((\sigma,\tau,\upsilon)\in S_9^3\) in which all permutations are
\(9\)-cycles and \(\sigma\tau\upsilon=1\). Fix
\(\sigma=(0\ 1\ 2\ 3\ 4\ 5\ 6\ 7\ 8)\). The remaining simultaneous conjugation
freedom is the centralizer \(\langle\sigma\rangle\cong C_9\). It acts on
\[
\mathcal T=\{\tau\in S_9:\tau\text{ and }\sigma\tau\text{ are }9\text{-cycles}\}
\]
by conjugation. The deck group of the corresponding cover is the stabilizer of \(\tau\)
inside \(C_9\).

**Identity fixed points.** The classical full-cycle connection-coefficient formula, also
rederived using symmetric-group characters in the 2026 reference below, gives
\[
|\mathcal T|=\frac{8!}{9}\sum_{r=0}^{8}\frac{(-1)^r}{\binom8r}
=\frac{8!}{9}\cdot\frac95=8064.
\]
For completeness, the character formula follows by multiplying the indicator class sum
of all \(9\)-cycles twice in the character basis. Only hook representations
\((9-r,1^r)\) contribute; they have degree \(\binom8r\) and character \((-1)^r\)
on a \(9\)-cycle. The finite sum above is directly evaluable. It is also independently
verified by enumerating once each of the \(8!=40320\) choices for the cyclic order of
\(\tau\) starting at \(0\), as in the accompanying verifier.

**Order-three fixed points.** Let \(h=\sigma^3\). Its orbits are the three residue-class
blocks \(B_r=\{r,r+3,r+6\}\) for \(r\in\mathbb Z/3\mathbb Z\). Every element of
\(C_{S_9}(h)\) is described by a permutation \(\rho\in S_3\) of these blocks and
three internal translations \((a_0,a_1,a_2)\in(\mathbb Z/3\mathbb Z)^3\), after fixing
coordinates along the \(h\)-orbits. It is a \(9\)-cycle exactly when \(\rho\) is a
\(3\)-cycle and the accumulated translation \(s=a_0+a_1+a_2\) is nonzero.

The block permutation of \(\sigma\) is \(r\mapsto r+1\), with accumulated translation
\(1\). For \(\sigma\tau\) to be a \(9\)-cycle, \(\rho\) must also be
\(r\mapsto r+1\), because the inverse block \(3\)-cycle would give the identity
block permutation after multiplication by \(\sigma\). In the surviving case the total
translation of \(\sigma\tau\) is \(s+1\). Thus \(s\ne0\) and \(s+1\ne0\), so
\(s=1\) in \(\mathbb Z/3\mathbb Z\). Exactly \(3^2=9\) translation triples meet this
condition. Therefore \(|\operatorname{Fix}(\sigma^3)|=9\), and the same holds for
\(\sigma^6\).

**Order-nine fixed points.** A \(9\)-cycle commuting with \(\sigma\) is
\(\tau=\sigma^k\) for \(\gcd(k,9)=1\). The product \(\sigma\tau=\sigma^{k+1}\)
is a \(9\)-cycle exactly when \(\gcd(k+1,9)=1\). The possibilities are
\(k\in\{1,4,7\}\), giving three fixed points for each of the six generators of
\(C_9\).

**Burnside and stabilizers.** Burnside's formula now yields
\[
\#(\mathcal T/C_9)=\frac{8064+2\cdot9+6\cdot3}{9}=900.
\]
There are three orbits of length \(1\) (deck group \(C_9\)); removing these from the
nine elements fixed by the subgroup of order \(3\) leaves six elements, forming two
orbits of length \(3\) (deck group \(C_3\)). The remaining \(8064-9=8055\)
elements form \(895\) orbits of length \(9\) (trivial deck group). This proves the
claimed distribution.

## Verification

Run the accompanying dependency-free program from the package directory:

```sh
python3 verify.py
```

The program enumerates all \(40320\) cyclic orders for \(\tau\), filters the
\(8064\) admissible products, explicitly partitions the admissible set into
\(C_9\)-orbits, and independently counts fixed points for the order-three and
order-nine elements. The exact expected output includes
`AUTOMORPHISM_ORDER_COUNTS=1:895,3:2,9:3`,
`UNROOTED_BELYI_COVERS=900`, and `VERIFY_OK`.
This is a finite exhaustive certificate for the degree-\(9\) statement, not an
extrapolation from small samples.

## Relationship to prior work

Djounvouna, *Belyi's theorem: coverings, dessins, and fields of definition*,
Section 8.2, gives the full-cycle mass formula and explicitly records, for degree
\(9\), that the unweighted number lies between \(896\) and \(8064\). It identifies
three cyclic cases but leaves the exact unweighted total unresolved there.
The result above computes that exact total and determines every possible deck-group
order in this passport.

Ellingham and Ellis-Monaghan count oriented dipole embeddings under various symmetries,
including all vertex-labeled cases without imposing a one-face condition; they
explicitly distinguish their enumeration from the genus distribution. The present
passport corresponds to one-face oriented embeddings of a nine-edge dipole with the
two vertices distinguished. Andrews--Jackson--Visentin study dipole genus series;
rooted/genus enumerations and the present unrooted, symmetry-stratified count are
different enumerative questions. Direct equivalent coverage in a less-accessible
older map-enumeration source remains a priority risk.

## Limitations

The result counts maps with a labeled three-point target, not abstract source curves,
not maps modulo permutations of branch values, and not arithmetic Galois orbits or
fields of definition. It does not classify monodromy subgroup isomorphism types
beyond deck groups. The comparison with the 1994 genus-series paper was limited
to its accessible abstract; an implicit equivalent older statement cannot be
completely excluded. No independent validation has been performed.

## References

1. D. Djounvouna, *Belyi's theorem: coverings, dessins, and fields of definition*, arXiv:2609.19053v1 (2026), especially Section 8.2, Example 8.10.
2. M. N. Ellingham and J. A. Ellis-Monaghan, *A Catalog of Enumeration Formulas for Bouquet and Dipole Embeddings Under Symmetries*, arXiv:2206.09226v1 (2022), especially the introduction and Part I, Section 3.
3. G. E. Andrews, D. M. Jackson and T. I. Visentin, *A Hypergeometric Analysis of the Genus Series for a Class of 2-Cell Embeddings in Orientable Surfaces*, SIAM J. Math. Anal. 25 (1994), 243--255, DOI:10.1137/S0036141092229549.
