# Temporal cycle profiles of five-site diagonal binary cellular automata

## Finding

For a Boolean function \(f:\mathbb F_2^4\to\mathbb F_2\), define the labeled five-site map
\[
(T_f(x))_i=f(x_{i+1},x_{i+2},x_{i+3},x_{i+4}),\qquad i\in\mathbb Z/5\mathbb Z.
\]
Among the bijective maps \(T_f\), the largest temporal period is **30**. Exactly **96** generating functions attain it: **32** have cycle profile \((1,1,30)\), and **64** have profile \((2,30)\). Of the 96 functions, **4** have algebraic-normal-form degree one, **16** degree two, and **76** degree three. The bijective maps realize **28** different cycle profiles in total.

Dennunzio, Gadouleau and Mariot already counted the **472** bijective rules in this family ([1], §4). The contribution here is the temporal cycle census within that previously enumerated family, not the number of its members.

## Assumptions and scope

The ring has exactly five sites, and rules and configurations are labeled, not counted up to rotation, reversal or affine equivalence. A temporal period is the least positive number of updates returning a configuration to itself. A cycle profile is the sorted list of all cycle lengths, including multiplicity. The truth-table integer \(t\) encodes \(f(a_1,a_2,a_3,a_4)\) as its bit at address \(a_1+2a_2+4a_3+8a_4\). Algebraic degree is the largest cardinality of a support with a nonzero coefficient in the squarefree algebraic normal form over \(\mathbb F_2\).

The motivating family is the diagonal of the Latin squares associated with diameter-six bipermutive rules [1]. For \(g(u_0,\ldots,u_5)=u_0\oplus u_5\oplus f(u_1,u_2,u_3,u_4)\), the two end inputs agree on the five-site diagonal and cancel. Invertibility identifies the diagonal transversals in this class; the temporal census asks how this permutation of diagonal labels acts when iterated, in particular whether it can traverse the whole nonconstant sector.

## Proof

**Rotation bound.** Let \(R(x_0,x_1,x_2,x_3,x_4)=(x_4,x_0,x_1,x_2,x_3)\). The update is cyclically uniform, hence \(T_fR=RT_f\). The two constant configurations are precisely the fixed points of \(R\), and the remaining thirty configurations lie in six \(R\)-orbits of size five. If \(T_f\) is bijective, the constant configurations are invariant as a set and the remaining configurations are invariant as a set. Consequently a temporal cycle has length at most 30. To have length 30 it must traverse every nonconstant configuration, leaving exactly the two possible profiles \((1,1,30)\) and \((2,30)\).

In quotient terms, a period-30 rule must cycle through all six nonconstant rotation classes. Conversely, if that quotient permutation is a six-cycle, then \(T_f^6 x=R^s x\) on a chosen representative, for some \(s\bmod 5\). By commutation, the same shift applies on the whole class. If \(s=0\), the return period there is six; otherwise the shift has order five and the temporal period is thirty. Thus invertibility alone does not entail a single nonconstant cycle.

**Balance restriction.** For a bijection, each output coordinate attains 1 on exactly 16 configurations. Each input of \(f\) occurs twice for that coordinate, so \(f\) has eight ones. The full-support algebraic-normal-form coefficient is the parity of the truth table and vanishes; hence no reversible rule here has degree four.

**Finite census.** `VERIFY.py` ranges over all integers \(0\le t<2^{16}\) representing the truth tables and computes all 32 configurations' images. Distinctness of all these images is equivalent to bijectivity. A second test uses one representative of each rotation class: the two singleton representatives must map bijectively to the constant configurations, and the six other representatives must map into distinct size-five classes. In the latter case, commutation with \(R\) maps the five rotations of each representative to the five distinct rotations of its image, so the test is also sufficient for bijectivity. The program compares the tests on the whole domain.

For each accepted permutation the program walks every disjoint cycle once; sorting the lengths gives its profile. For algebraic degree, Boolean Möbius inversion computes each coefficient for support \(S\) as the XOR of the truth-table values at all submasks of \(S\). In the census, 28 profiles occur. Exactly 96 permutations contain a 30-cycle, with the stated profile and degree counts. For example, the truth-table integers 2295 (cubic), 2805 (quadratic), and 15555 (affine of degree one) each have profile \((2,30)\), and 33646 (cubic) has profile \((1,1,30)\). These examples witness sharpness, and the exhaustive tally supplies the exact counts.

## Verification

Run `python3 VERIFY.py` with Python 3 and the standard library. The program checks both bijectivity tests, rotation equivariance, the temporal and degree tallies, and the example truth tables via a separate interpreter. Its reversible-rule total, 472, reproduces the count in [1, §4] as a consistency check. This is finite exhaustive evidence for the specified ring, not a search over ring lengths or a statistical extrapolation.

## Relationship to prior work and limitations

Reference [1], Remark 2 and Theorem 3.1, relates diagonal transversals to periodic cellular automata, and §4 enumerates all \(2^{16}\) diameter-six generating functions, reporting 472 reversible rules of which 456 are nonlinear. That enumeration determines which class to study and its size, not the temporal decomposition reported here. Reference [2] instead studies periods of maps constructed from *pairs* of orthogonal cellular automata on double-width states; its dynamical system differs from the single five-site diagonal permutation. Reference [3] surveys the design correspondence. These comparisons do not establish publication priority. The census applies only to the specified five-site rule family and does not characterize reversibility or periods at other ring lengths.

## References

1. A. Dennunzio, M. Gadouleau, and L. Mariot, *On the transversals of Latin squares generated by nonlinear bipermutive cellular automata*, arXiv:2605.18875v1 (2026), https://arxiv.org/html/2605.18875v1.
2. L. Mariot, *Enumeration of Maximal Cycles Generated by Orthogonal Cellular Automata*, arXiv:2203.02726v1 (2022), https://arxiv.org/abs/2203.02726.
3. L. Manzoni, L. Mariot, and G. Menara, *Combinatorial designs and cellular automata: A survey*, Discrete Applied Mathematics 379 (2026), 656–674, DOI:10.1016/j.dam.2025.10.014.
