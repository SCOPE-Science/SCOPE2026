# Exceptional primes and Frobenius spectra for the Fermat quartic bitangent arrangement

## Finding
Let \(k=\mathbb F_q\) be any finite field of odd characteristic \(p\). Let \(C\subset\mathbb P_k^2\) be the smooth Fermat (Dyck) quartic \(x^4+y^4+z^4=0\), and let \(\mathcal L\) be the reduced union of its \(28\) geometric bitangents. For \(m\ge2\), denote by \(P_m\) the reduced finite set of geometric points lying on **exactly** \(m\) distinct lines of \(\mathcal L\). The table gives, for every \(m\), the number of Frobenius orbits of lengths \(1\) and \(2\), written \((c_1,c_2)\). All omitted strata are empty.

| Characteristic and residue condition | \(P_2:(c_1,c_2)\) | \(P_3:(c_1,c_2)\) | \(P_4:(c_1,c_2)\) |
| --- | --- | --- | --- |
| \(p\notin\{3,5,17\}\), \(q\equiv1\pmod8\) | \((288,0)\) | \((0,0)\) | \((15,0)\) |
| \(p\notin\{3,5,17\}\), \(q\equiv3,7\pmod8\) | \((0,144)\) | \((0,0)\) | \((9,3)\) |
| \(p\notin\{3,5,17\}\), \(q\equiv5\pmod8\) | \((48,120)\) | \((0,0)\) | \((15,0)\) |
| \(p=3\), \(q\equiv3\pmod8\) | \((0,0)\) | \((0,0)\) | \((9,27)\) |
| \(p=3\), \(q\equiv1\pmod8\) | \((0,0)\) | \((0,0)\) | \((63,0)\) |
| \(p=5\), \(q\equiv5\pmod8\) | \((0,120)\) | \((16,0)\) | \((15,0)\) |
| \(p=5\), \(q\equiv1\pmod8\) | \((240,0)\) | \((16,0)\) | \((15,0)\) |
| \(p=17\) (necessarily \(q\equiv1\pmod8\)) | \((144,0)\) | \((48,0)\) | \((15,0)\) |

Thus the geometric weak combinatorics has exactly three bad odd primes: \(3\), \(5\), and \(17\). The respective multiplicity vectors \((\#P_2,\#P_3,\#P_4)\) are \((0,0,63)\), \((240,16,15)\), and \((144,48,15)\), versus \((288,0,15)\) at every other odd prime. No intersection has multiplicity exceeding \(4\). The reduced finite étale scheme \(P_m\) has zeta function \(Z(P_m,T)=(1-T)^{-c_1}(1-T^2)^{-c_2}\); consequently, the entire reduced intersection set has the product of these zeta functions. Every intersection becomes rational over \(\mathbb F_{q^2}\), and all are already rational over \(\mathbb F_q\) if and only if \(q\equiv1\pmod8\).

## Assumptions and scope
All claims concern this **literal diagonal plane quartic**, not a twist. A bitangent includes a hyperosculating tangent (one point of contact of order four). The incidence sets \(P_m\) are **reduced supports**, not the possibly nonreduced Jacobian singular subscheme of the line union. The characteristic is odd. The displayed \(28\) bitangents are geometric lines, not necessarily rational over the base field; Frobenius denotes arithmetic \(q\)-power Frobenius on their geometric coefficients and intersection points.

## Proof
Choose a primitive eighth root \(\zeta\) over an algebraic closure, so \(\zeta^4=-1\). Twelve explicit hyperosculating bitangents are
\[
H_{xy,j}:x-\zeta^j y=0,\qquad H_{xz,j}:x-\zeta^j z=0,\qquad H_{yz,j}:y-\zeta^j z=0,\qquad j\in\{1,3,5,7\}.
\]
The remaining sixteen are
\[
O_{a,b}:x+\zeta^{2a}y+\zeta^{2b}z=0,\qquad 0\le a,b<4.
\]
The first restriction gives a fourth power; for the second, writing \(A=\zeta^{2a}\) and \(B=\zeta^{2b}\), one obtains the **polynomial identity**
\[
(x^4+y^4+z^4)|_{x=-Ay-Bz}=2(A^2y^2+AByz+B^2z^2)^2.
\]
Both identities hold in every odd characteristic. These \(28\) lines are pairwise distinct there: the eighth roots remain distinct, and a form with three nonzero coefficients cannot equal one with only two. Completeness follows from the classical count of \(28\) odd theta characteristics/bitangents of a smooth plane quartic in characteristic different from two. In characteristic three the sixteen quadratic contacts also coalesce to fourth-order contacts; the lines remain distinct.

For the incidence computation use the integral cyclotomic ring \(R=\mathbb Z[t]/(t^4+1)\), with \(t\) representing \(\zeta\). Each line has the above coefficient vector in \(R^3\). For each unordered pair of lines, take its cross product as a projective intersection. The complete set of lines through this point is obtained by the exact dot-product test. Distinct projective points have distinct incidence subsets because any common pair of lines has only one intersection. The exact enumeration yields \(288\) subsets of size two and \(15\) of size four; the incidence identity \(288+15\binom42=\binom{28}2=378\) verifies that every pair is accounted for. This generic complex count is also recorded in Janasz--Pokora--Zieliński, Proposition 3.2 (their Dyck quartic).

To prove that there are **no further bad primes**, compute the determinant \(\Delta_{ijk}\in R\) of every unordered triple of line coefficient vectors. There are \(60\) identically zero determinants, corresponding to the \(15\) fourfold points. For the other \(3216\), compute the positive integer norm \(\prod_{u\in\{1,3,5,7\}}\sigma_u(\Delta_{ijk})\), where \(\sigma_u(t)=t^u\). The **complete** norm histogram (norm: multiplicity) is
\[
1:384,\quad2:64,\quad4:864,\quad8:384,\quad9:192,\quad16:560,\quad17:192,\quad32:96,\quad36:192,\quad64:192,\quad256:64,\quad400:32.
\]
These numbers sum to \(3216\). Their prime support is exactly \(\{2,3,5,17\}\). For any other odd prime, no previously nonconcurrent triple can become concurrent modulo that prime: a zero reduction would force its rational norm to be divisible by the prime. Line distinctness was already established, so the **entire incidence configuration** remains unchanged.

At \(p=3,5,17\) the exact pairwise intersection tests are repeated over splitting fields. For \(p=3\), use \(\mathbb F_3[t]/(t^2-t-1)\); for \(p=5\), use \(\mathbb F_5[t]/(t^2-2)\); for \(p=17\), take \(t=2\in\mathbb F_{17}\). Each selected \(t\) has order eight. Exhaustive cross-product/dot-product enumeration gives, respectively, \(63\) fourfold points; \(240\) double, \(16\) triple, \(15\) fourfold points; and \(144\) double, \(48\) triple, \(15\) fourfold points. In each case the weighted pair count equals \(378\), proving completeness over the algebraic closure rather than just over a chosen finite field. There are no higher-multiplicity points. The characteristic-three case has an additional geometric explanation: the Fermat quartic is the Hermitian unital in \(\mathbb P^2(\mathbb F_9)\), whose \(28\) rational points have \(28\) tangents meeting at the other \(63\) projective points, with four tangents through each.

Finally arithmetic Frobenius sends \(t\mapsto t^q\). On the labels it maps \(H_{*,j}\mapsto H_{*,qj\bmod8}\) and \(O_{a,b}\mapsto O_{qa\bmod4,qb\bmod4}\). Applying these permutations to **the complete incidence subsets**, and counting their orbits, proves every row of the table. Since \(q\) is odd, \(q^2\equiv1\pmod8\), so the orbit lengths are at most two. The exceptional-characteristic results for quadratic extensions follow by squaring Frobenius. Fixed-point and zeta-function assertions follow for the reduced finite étale point schemes.

## Verification
Run `python3 verify.py` with Python 3.9 or newer; no third-party packages are needed. The script constructs all \(28\) lines in \(R\), enumerates all \(\binom{28}{2}=378\) pairs and \(\binom{28}{3}=3276\) triples, and computes every nonzero norm by multiplying four conjugates **exactly**. It asserts the full norm histogram and checks the generic Frobenius orbit spectra for all four residues modulo eight. It then reconstructs the three exceptional finite-field splitting rings and exhaustively asserts the incidence and Frobenius spectra, including quadratic extension fixedness. `verify_output.txt` is an actual successful execution transcript ending in `VERIFY_OK`. The finite algorithm is exhaustive on this \(28\)-line model, while the norm-divisibility argument supplies the universal all-prime step. No numerical extrapolation is used.

## Relationship to prior work
The twelve hyperosculating and sixteen other bitangents, and their characteristic-zero geometry, descend from classical studies of the Dyck configuration; Edge's 1944 discussion explicitly recounts this decomposition. Plaumann--Sturmfels--Vinzant (2010), and Dalla Piazza--Fiorentino--Salvati Manni (2014), develop general bitangent theory. Janasz--Pokora--Zieliński (arXiv 2023) give the **already known** characteristic-zero counts \(288\) ordinary double and \(15\) quadruple points, as well as explicit complex incidence tables. Bethea--Brazelton (2024) determine automorphism-group actions on the bitangents of symmetric quartics; those are not arithmetic Frobenius actions on reduced intersection strata. The result here is **only** the complete odd-characteristic degeneration classification and the finite-field arithmetic orbit/zeta data, not the known complex incidence counts or the existence of the \(28\) bitangents.

## Limitations
This classifies reduced geometric crossings of the distinguished \(28\)-line arrangement over finite fields of odd characteristic. It does not compute the scheme-theoretic local Jacobian algebras, their deformation multiplicities, or analogous data in characteristic two or for twisted plane quartics. Characteristic-three tangent behavior is special; the table concerns the reduced lines and their crossings, not a claim that all tangencies remain ordinary. Historical priority for the exact modular degeneration and Frobenius tables has not been independently audited; classical equations may encode implicit derivations of these numbers.

## References
1. W. L. Edge, *The geometrical construction of Maschke's quartic surfaces*, received 1944, section “Dyck's Plane Configuration”, DOI: `10.1017/S0013091500024378`. Classical \(12+16\) bitangent decomposition.
2. D. Plaumann, B. Sturmfels, C. Vinzant, *Quartic Curves and Their Bitangents*, arXiv:`1008.4104` (first submitted 2010-08-24), especially introductory bitangent identities and sections on the Fermat quartic.
3. F. Dalla Piazza, A. Fiorentino, R. Salvati Manni, *Plane quartics: the matrix of bitangents*, arXiv:`1409.5032` (first submitted 2014-09-17).
4. M. Janasz, P. Pokora, M. Zieliński, *On arrangements of smooth plane quartics and their bitangents*, arXiv:`2308.16514` (first submitted 2023-08-31), Proposition 3.2 and Section 3.2.
5. C. Bethea, T. Brazelton, *Bitangents to symmetric quartics*, arXiv:`2410.09242` (first submitted 2024-10-11), especially Section 4.2.
