# Exact maximal-cycle census for five-site binary cellular automata

## Finding

**Theorem (sharp maximum and exact census).** For every Boolean function \(f:\mathbb F_2^4\to\mathbb F_2\), put
\[
 (T_f(x))_i=f(x_{i+1},x_{i+2},x_{i+3},x_{i+4}),\qquad i\in\mathbb Z/5\mathbb Z.
\]
If \(T_f\) is bijective, every primitive temporal orbit has period at most \(30\). Exactly \(96\) functions attain that maximum. Of these, \(32\) have cycle profile \((1,1,30)\) (two distinct fixed points and one period-30 orbit), and \(64\) have profile \((2,30)\) (one period-two orbit and one period-30 orbit). Their algebraic-normal-form degrees are distributed as \(4\) of degree one, \(16\) of degree two, and \(76\) of degree three. Overall, \(472\) functions give bijective \(T_f\), with \(28\) distinct cycle profiles.

## Assumptions and scope

The space is **exactly** \(\mathbb F_2^5\); no claim concerns all ring lengths. Input truth tables are enumerated in binary order: integer \(t\in\{0,\ldots,65535\}\) represents \(f_t\) with \(f_t(a_1,a_2,a_3,a_4)\) equal to bit at address \(a_1+2a_2+4a_3+8a_4\). Algebraic degree is the highest support size of any nonzero squarefree coefficient of the algebraic normal form. Cycle profile lists lengths with multiplicity. The associated six-input bipermutive rule is \(g(u_0,\ldots,u_5)=u_0\oplus u_5\oplus f(u_1,u_2,u_3,u_4)\); on a five-site periodic diagonal, \(u_0=u_5\), leaving the above cyclic rule.

## Proof

**Bound.** Write \(R(x_0,x_1,x_2,x_3,x_4)=(x_4,x_0,x_1,x_2,x_3)\). Because \(T_f\) is a cyclic local rule, \(T_fR=RT_f\). The rotation \(R\) has precisely two fixed states (the constant words), and its remaining thirty states form six orbits of size five. If \(T_f\) is bijective, it permutes the two fixed states among themselves and permutes the six five-element rotation orbits among themselves. Hence every temporal orbit among nonconstant states is contained in a union of at most six five-element rotation orbits, so its length is at most \(30\). The two constant states admit temporal periods at most two. Consequently no bijective map in this class has a longer primitive cycle.

**Balance restriction.** If \(T_f\) is bijective, every output coordinate has exactly \(16\) ones over the \(32\) equally weighted five-bit inputs. Each four-bit input of \(f\) appears twice in any fixed coordinate, hence \(f\) has exactly \(8\) ones in its 16-entry truth table. The top algebraic-normal-form coefficient is the parity of those 16 entries, so degree-four functions cannot be bijective in this family. This explains the degree bound structurally.

**Exact enumeration certificate.** `VERIFY.py` exhausts all \(2^{16}=65{,}536\) Boolean truth tables in the precisely specified order. For each truth table it computes, without sampling, the images of all \(2^5=32\) configurations. One procedure accepts a bijection precisely when its 32 outputs are distinct. An independent procedure constructs the images of the eight representatives of the rotation orbits and accepts precisely when the two singleton representatives map bijectively to the constant configurations and the remaining six representatives map into six distinct size-five rotation orbits. As \(T_f\) commutes with rotation, each restricted map on a size-five orbit is automatically a bijection onto its image orbit; therefore the orbit criterion is equivalent to global bijectivity. The program asserts exact agreement for all 65,536 inputs.

Every accepted permutation is decomposed into its disjoint temporal cycles by walking until each initial state returns. The code counts the cycle profiles and uses a four-variable Boolean Möbius transform to determine the algebraic-normal-form degree. Final assertions check exactly \(472\) permutations and \(28\) profiles; exactly \(96\) include length \(30\), partitioned as \(32\) profiles \((1,1,30)\) and \(64\) profiles \((2,30)\), with degrees \(4,16,76\) in ascending degree order. Thus the exhaustive finite computation proves the exact count and witnesses attainability; the preceding rotation argument proves maximality. Representative truth-table integers include \(2295\) (cubic, \((2,30)\)), \(2805\) (quadratic, \((2,30)\)), \(15555\) (affine of degree one, \((2,30)\)), and \(33646\) (cubic, \((1,1,30)\)). An independent truth-table interpreter replays each representative.

## Verification

Execute `python3 VERIFY.py` with a standard Python 3 interpreter; it has no third-party dependencies. It prints `VERIFY_OK` upon checking all \(65{,}536\) rules, the independently constructed rotation-orbit bijectivity condition, all accepted permutations' commutation with rotation, and the complete maximal-orbit tally. Complete enumeration here is a finite proof of the count, not a sample-based extrapolation. The mathematical rotation bound applies to every possible rule of this fixed size. Source code is bundled with this result.

## Relationship to prior work

Dennunzio, Gadouleau and Mariot (2026) introduce the diagonal-transversal/invertible-periodic-CA correspondence and establish diameter six as the first setting permitting nonlinear examples. This correspondence and the existence of nonlinear examples are prior work. The contribution here is the **temporal maximal-orbit census** (exactly 96 attain the symmetry bound, with split profiles and algebraic-degree counts) of the resulting five-site periodic maps. Mariot (2022) enumerates maximal periods for a different dynamical system induced by **pairs of orthogonal cellular automata** on a double-width state space; its full-text dynamical definition and linear Sylvester-matrix classifications concern a different transformation. Manzoni, Mariot and Menara (2026) survey CA-generated Latin squares and orthogonality rather than these five-site temporal cycle profiles.

## Limitations

The theorem is an exact, finite-scale classification for **five sites**, not an asymptotic theorem in system size, a proof of pseudorandomness, or a characterization of all invertible CA. The motivating 2026 preprint's complete manuscript was unavailable for comparison; its accessible abstract reports the diagonal criterion and existence search but does not discuss the stated maximal temporal-cycle census. Therefore residual publication-priority risk remains. Independent validation has not been performed.

## References

1. A. Dennunzio, M. Gadouleau, L. Mariot, *On the transversals of Latin squares generated by nonlinear bipermutive cellular automata*, arXiv:2605.18875v1 (first public 2026-05-15), https://arxiv.org/abs/2605.18875 .
2. L. Mariot, *Enumeration of Maximal Cycles Generated by Orthogonal Cellular Automata*, arXiv:2203.02726v1 (2022), https://arxiv.org/abs/2203.02726 .
3. L. Manzoni, L. Mariot, G. Menara, *Combinatorial designs and cellular automata: A survey*, Discrete Applied Mathematics 379 (2026), 656–674, DOI:10.1016/j.dam.2025.10.014 .
