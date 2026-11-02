# Rational bitangent counts constrained by Jacobian two-torsion of plane quartics

## Finding

Let \(C/\mathbb F_q\) be any smooth geometrically connected plane quartic with \(q\) odd, let \(J=\operatorname{Jac}(C)\), let \(r=\dim_{\mathbb F_2}J(\mathbb F_q)[2]\), and let \(b\) count the \(\mathbb F_q\)-rational geometric bitangent lines, hyperflexes included. Then \((r,b)\) must appear in the following complete table. The third column counts the corresponding elements of the abstract binary symplectic group, *not* the number of plane quartics.

| Rational two-torsion rank \(r\) | Rational bitangents \(b\) | Elements of \(\mathrm{Sp}_6(\mathbb F_2)\) |
|---:|---:|---:|
| 0 | 0 | 304,128 |
| 0 | 1 | 304,640 |
| 1 | 0 | 151,200 |
| 1 | 1 | 306,432 |
| 1 | 2 | 151,200 |
| 2 | 0 | 11,340 |
| 2 | 1 | 53,760 |
| 2 | 2 | 75,600 |
| 2 | 3 | 48,384 |
| 2 | 4 | 13,860 |
| 3 | 2 | 7,560 |
| 3 | 4 | 13,860 |
| 3 | 6 | 7,560 |
| 4 | 4 | 315 |
| 4 | 8 | 945 |
| 4 | 10 | 672 |
| 5 | 16 | 63 |
| 6 | 28 | 1 |

In particular, if \(\#J(\mathbb F_q)[2]\ge8\), then \(C\) has at least two rational bitangents. If \(\#J(\mathbb F_q)[2]\ge16\), it has at least four. Ranks \(5\) and \(6\) force respectively \(16\) and \(28\) rational bitangents. The only abstractly possible counts of rational bitangents are \(0,1,2,3,4,6,8,10,16,28\). Every listed pair is realized by an *abstract symplectic Frobenius element*, but the table does **not** assert that every pair is realized by a plane quartic over any chosen field.

## Assumptions and scope

Characteristic is different from two. The quartic is smooth, projective and geometrically connected, and its degree-four plane embedding is canonical. A bitangent means a geometric line meeting \(C\) in a divisor twice an effective divisor of degree two; hyperflex lines are included. Rationality means the line (equivalently its corresponding odd theta characteristic) is fixed by geometric Frobenius. The stated rank is the dimension of the fixed subspace of the Galois action on the six-dimensional vector space \(J[2](\overline{\mathbb F}_q)\), and not the rank of the entire rational Jacobian group.

The classification is **necessary** for each plane quartic, and **exact** for the ambient symplectic action. Arithmetic realizability of all abstract rows is not claimed. The table is independent of field size, beyond the assumption of odd characteristic.

## Proof

**1. Reduction to 28 odd quadratic forms.** Put \(V=J[2](\overline{\mathbb F}_q)\), equipped with its nondegenerate alternating Weil pairing \(B\). Standard theta-characteristic theory canonically identifies theta characteristics with the quadratic refinements \(Q\colon V\to\mathbb F_2\) of \(B\), and identifies the 28 odd characteristics with the odd refinements. For a nonhyperelliptic genus-three curve, an odd characteristic has a unique effective divisor of degree two and defines exactly one geometric bitangent; both constructions respect Galois. This reduces rational bitangent counting to fixed odd refinements of a symplectic Frobenius action \(M\in\mathrm{Sp}(V,B)\). Rational two-torsion is \(\ker(M-I)\).

**2. Explicit fixed-refinement equations.** Fix symplectic coordinates \((a_1,b_1,a_2,b_2,a_3,b_3)\in\mathbb F_2^6\), with
\[
 B(x,y)=\sum_{i=1}^{3}(a_i(x)b_i(y)+b_i(x)a_i(y)),\qquad Q_0(x)=\sum_{i=1}^{3}a_i(x)b_i(x).
\]
Every refinement is uniquely \(Q_t(x)=Q_0(x)+B(t,x)\), for \(t\in V\), and it is odd precisely when \(Q_0(t)=1\). There are exactly \(28\) such vectors. If \(e_1,\ldots,e_6\) is the standard basis and \(M\) is symplectic, then \(Q_t(Mx)+Q_t(x)\) is linear in \(x\). Hence \(Q_t\) is Frobenius-fixed if and only if the following *six* scalar equations all hold:
\[
Q_0(Me_j)+B(t,Me_j+e_j)=0\quad (j=1,\ldots,6).
\]
In particular, it is sufficient to check these equations at basis vectors rather than at all \(64\) vectors; the supplementary verifier nevertheless checks all \(64\) vectors for each row witness.

**3. Exhaustive enumeration, with independent constructions.** Every symplectic matrix is uniquely determined by an ordered symplectic basis. Choose an initial nonzero vector in \(63\) ways and its dual in \(32\) ways; then choose a hyperbolic pair in its symplectic complement in \(15\cdot8\) ways, and the last pair in \(3\cdot2\) ways. This gives exactly
\[
63\cdot32\cdot15\cdot8\cdot3\cdot2=1{,}451{,}520
\]
distinct matrices, equal to the abstract symplectic group order. For every such basis, calculate \(r=6-\operatorname{rank}(M-I)\) by binary Gaussian elimination, then count odd vectors \(t\) solving the six equations. Summing over the complete enumeration produces the table. The first standalone C program uses this symplectic-basis enumeration without any group generators. A second program generates the entire group from eight explicit symplectic transvections, independently computes the same \((r,b)\) counts and produces one explicit matrix witness for each row. The output tables agree in every entry and their multiplicities add to \(1{,}451{,}520\). Each witness is independently checked by a separate Python program for pairing preservation on all \(64^2\) vector pairs, for its fixed-space rank, and for preservation of each of the \(28\) odd forms on every one of \(64\) vectors. See Verification.

**4. A geometric existence principle.** An arbitrary \(M\in\mathrm{Sp}(V,B)\) always fixes some quadratic refinement. Indeed, if \(Q_0\) is any refinement, then \(x\mapsto Q_0(Mx)+Q_0(x)\) is a linear functional vanishing on \(\ker(M-I)\); by rank-nullity it lies in the image of the adjoint of \(M-I\), and so can be canceled by adding \(B(t,x)\). The fixed refinements therefore form an affine space over \(\ker(M-I)\), of size \(2^r\). For any fixed refinement \(Q\), the parity of its translate by a fixed vector \(t\) changes by \(Q(t)\). If \(r\ge4\), \(Q\) cannot vanish on the entire fixed space, because this would be a totally isotropic subspace of dimension greater than three. If \(r=3\), a totally singular fixed three-space would be Lagrangian; in a symplectic splitting, a symplectic automorphism fixing it pointwise has form \((u,v)\mapsto(u+Av,v)\), with \(A\) symmetric. Preservation of the refinement and total singularity force \(A\) to be alternating. Every alternating \(3\times3\) matrix is singular, which would force a fixed vector outside the three-space, a contradiction. Thus the fixed space supports a nonzero restriction of the quadratic refinement for \(r\ge3\). For completeness, the restriction \(Q|_{\ker(M-I)}\) is a nonconstant binary polynomial of degree at most two. Both it and its complement have at least \(2^{r-2}\) nonzero values, by the elementary minimum-weight bound for degree-two Boolean polynomials: writing such a polynomial as \(f(x_1,\ldots,x_{r-1})+x_rg(x_1,\ldots,x_{r-1})\), either \(g=0\) and the weight doubles by induction, or \(g\neq0\), is affine linear, and every input with \(g=1\) contributes exactly one output equal to one. This gives the structural bound \(b\ge 2^{r-2}\) for \(r\ge3\); the exhaustive table sharpens it for ranks five and six and classifies every possible joint pair.

## Verification

The package includes source files `verification/symplectic_bases.c` and `verification/transvections_bfs.c`, numerical `verification/counts.csv`, and all eighteen witness matrices in `verification/witnesses.csv`. Running `python3 verification/replay.py` from any directory (with a C compiler available as `cc`) compiles both enumerators into a temporary directory, recomputes the complete group census twice, compares all eighteen rows, and independently verifies the witnesses by an exhaustive check over sixty-four vectors. The recorded execution output ends in `VERIFY_OK`.

This is a finite, exhaustive group-theoretic computation, not a proof by finite-field sampling. It supplies a theorem for *every* smooth plane quartic in odd characteristic because the standard odd-theta and Weil-pairing reduction applies uniformly. The programs do not enumerate moduli of plane quartics and make no assertion that every abstract matrix action occurs for a specific field.

## Relationship to prior work

The equivalence between the 28 bitangents and odd theta characteristics, the \(\mathrm{Sp}_6(\mathbb F_2)\) action, and its 28-point permutation representation are classical. Plaumann–Sturmfels–Vinzant (2010) give the bitangent/Cayley-octad/Steiner geometry and methods. Bergvall (2023) treats level-two structures, their stabilizers, arithmetic and topology, including finite-field counts of *moduli spaces*. The ATLAS tabulates the permutation representation on 28 objects. Frame (1951) classifies the conjugacy classes and characters of the bitangent symmetry group. These inputs are not claimed as new.

The specific assessed result is the **joint, quantitative dependency** of rational bitangent counts on the fixed rank of rational Jacobian two-torsion, together with all eighteen multiplicities and witnesses and the consequent sharp universal thresholds. None of the accessible primary materials inspected states this joint table. The table is derivable from full classical group-action data, and the precise historical novelty of the evaluated joint table remains subject to inspection of additional older class tables. This is not a claim that the possible fixed-point spectra of the 28-point action alone are new.

## Limitations

Characteristic two is excluded. The census is over symplectic *elements*, not plane quartic isomorphism classes, rational moduli points, or a probability distribution of actual curve Frobenius types. Geometric realization of every row over each finite field remains unproved; do not interpret the element multiplicities as curve counts. One relevant older primary text (Frame, 1951) was not available for page-level comparison; its conjugacy-class data may imply parts of the table.

## References

1. D. Plaumann, B. Sturmfels, C. Vinzant, *Quartic Curves and Their Bitangents*, arXiv:1008.4104v1 (24 August 2010), https://arxiv.org/abs/1008.4104.
2. O. Bergvall, *Arithmetic and topology of classical structures associated with plane quartics*, European Journal of Mathematics 9 (2023), article 117, DOI 10.1007/s40879-023-00711-3.
3. J. S. Frame, *The classes and representations of the groups of 27 lines and 28 bitangents*, Ann. Mat. Pura Appl. 32 (1951), 83–119, DOI 10.1007/BF02417955 (bibliographic description checked; complete text not inspected).
4. ATLAS of Finite Group Representations, *Symplectic group \(S_6(2)\), permutation representation on 28 points*, https://brauer.maths.qmul.ac.uk/Atlas/v3/permrep/S62G1-p28B0.
