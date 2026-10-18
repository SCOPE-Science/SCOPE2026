# A ternary Cartier-rank filtration and zero Mordell–Weil groups in a quasi-elliptic family

## Finding

Let \(k=\overline{\mathbb F}_3\). For every integer \(s\geq1\) put \(q=3^s\), and let \(C_s\) be the smooth projective model of the hyperelliptic curve
\[
C_s:\quad y^2=t^{2q+2}-t.
\]
Its genus is \(q\). Write \(\mathcal C_s\) for the Cartier operator on \(H^0(C_s,\Omega^1_{C_s})\), and set \(r_j=\dim_k\operatorname{im}(\mathcal C_s^j)\) for every integer \(j\geq0\), with \(\mathcal C_s^0\) the identity. Then **every iterate has an exact rank**:
\[
r_j=\begin{cases}
2^j3^{s-j},&0\leq j\leq s,\\
2^{2s-j},&s\leq j\leq2s,\\
0,&j\geq2s+1.
\end{cases}
\]
Thus the Jacobian of \(C_s\) has \(3\)-rank zero and \(a\)-number \(3^{s-1}\). The Cartier nilpotence index is exactly \(2s+1\), since \(r_{2s}=1\) and \(r_{2s+1}=0\).

There is also a quasi-elliptic consequence. Let \(S_s\to\mathbb P^1_k\) be the relatively minimal regular quasi-elliptic surface whose generic fiber has affine equation
\[
u^3=v-(t^{2q+2}-t)v^3
\]
with its distinguished zero section. Its Mordell–Weil group is **trivial**:
\[
\operatorname{MW}(S_s)=0.
\]
Here the surface is the relatively minimal regular model of the indicated generic-fiber group curve; no assertion is made about the classification of other quasi-elliptic surfaces.

## Assumptions and scope

All statements are over an algebraically closed field of characteristic exactly \(3\). The exponent \(s\) is an arbitrary positive integer. The polynomial \(f_s(t)=t^{2q+2}-t\) has distinct roots: \(f'_s(t)=2t^{2q+1}-1\), which equals \(-1\) at the root \(0\) and \(1\) at each root satisfying \(t^{2q+1}=1\). As \(\deg f_s=2q+2\), standard hyperelliptic geometry yields genus \(q\) and regular differentials \(t^{j-1}dt/y\), \(1\leq j\leq q\).

The Cartier operator is inverse-Frobenius-semilinear, not \(k\)-linear. Its image dimensions are nevertheless well defined, and the matrix coefficients below lie in \(\mathbb F_3\), so the usual semilinear twisting leaves all matrix powers unchanged.

## Proof

**1. Cartier coefficients.** In the indicated differential basis, the standard hyperelliptic Cartier–Manin formula (with the left-column convention of Achter–Howe, Section 3.1) gives the matrix \(B=(b_{ij})_{1\leq i,j\leq q}\), where \(b_{ij}\) is the inverse-Frobenius cube root of the coefficient of \(t^{3i-j}\) in \(f_s(t)\). Since \(f_s(t)=t^{2q+2}-t\) and its coefficients belong to \(\mathbb F_3\),
\[
b_{ij}=\begin{cases}
-1,&j=3i-1,\\
1,&j=3i-(2q+2),\\
0,&\text{otherwise}.
\end{cases}
\]
The first alternative occurs precisely when \(1\leq i\leq q/3\); the second when \(2q/3+1\leq i\leq q\). In each row at most one entry is nonzero. The two sets of nonzero columns are disjoint because their indices are respectively \(2\) and \(1\) modulo \(3\), and within each set the indices are distinct. Hence the matrix is a *partial signed permutation matrix*. Its powers retain that property, and \(\operatorname{rank}(B^j)\) counts exactly those row indices admitting a path of length \(j\) through its nonzero entries. The inverse-Frobenius twists of \(B\) equal \(B\) over \(k\), so these are also the ranks of \(\mathcal C_s^j\).

**2. Ternary dynamics.** Encode the row index \(i\) by the \(s\)-digit base-three word for \(i-1\), allowing leading zeros. The nonzero row-to-column move replaces
\[
0w\longmapsto w1,\qquad2w\longmapsto w0,
\]
and terminates when the leading digit is \(1\). (The displayed words have length \(s\); \(w\) has length \(s-1\).) The identities follow directly from the formulas \(j=3i-1\) and \(j=3i-(2q+2)\).

For \(0\leq j\leq s\), exactly the initial words whose first \(j\) digits are each \(0\) or \(2\) survive \(j\) moves. There are \(2^j3^{s-j}\) such words. After \(s\) moves, every surviving initial digit \(0\) has become \(1\), and every surviving initial digit \(2\) has become \(0\), in their original order. To survive an additional \(j-s\) moves (for \(s\leq j\leq2s\)), the first \(j-s\) original digits must therefore all be \(2\), while the remaining \(2s-j\) original digits can each be \(0\) or \(2\). This leaves precisely \(2^{2s-j}\) words. At \(2s\) steps only the all-\(2\) word survives; it has become the all-\(1\) word and terminates on its next step. This establishes the rank formula for every integer \(s\geq1\) and every iterate \(j\geq0\).

**3. Jacobian invariants.** The geometric \(3\)-rank equals the stable Cartier rank. The formula makes all sufficiently high Cartier iterates zero, so the stable rank is zero. The \(a\)-number is \(\dim\ker\mathcal C_s=q-r_1=q-2q/3=q/3=3^{s-1}\).

**4. Mordell–Weil consequence.** Put \(n=q/3+1\). Then \(\deg f_s=2q+2=6n-4\), which lies in Katsura's required degree interval \([6n-5,6n]\), and
\[
f_s(t)=(-1)^3t+(t^{2q/3})^3t^2
\]
is the normalized form in his equation (4.1). At a root \(\alpha\) of \(f'_s\), \(\alpha\neq0\) and \(f''_s(\alpha)=2\alpha^{2q}\neq0\), so the valuation of \(f_s(t)-f_s(\alpha)\) at \(t-\alpha\) is exactly \(2\). Hence Assumption (*) in Katsura, Section 4, holds; its additional cubic-leading-term clause does not arise. Katsura's Theorem 4.1 identifies the Mordell–Weil group with the subgroup \(H_0\) of the stable Frobenius/Cartier fixed-point space \(H\) attached to \(C_s\). Since the Cartier operator is nilpotent, \(H=0\), so \(H_0=0\), proving \(\operatorname{MW}(S_s)=0\).

## Verification

The accompanying standalone Python 3 file `cartier_check.py` forms the coefficient matrix directly from its two monomials over \(\mathbb F_3\), verifies its partial-permutation property, computes the ranks of its successive powers by exact integer path counting, independently derives each step from base-three words, and compares the resulting rank sequences with the closed formulas for \(1\leq s\leq6\). To reproduce: `python3 cartier_check.py`. The successful execution prints `VERIFY_OK digit_shift_and_exact_rank_profiles s=1..6`. These are finite corroborating computations; the digit proof above is the proof for unbounded \(s\).

## Relationship to prior work

Katsura, arXiv:2609.23430v1, Section 4 and Theorem 4.1, relates Mordell–Weil groups of quasi-elliptic surfaces to the stable Cartier/Frobenius part of a related hyperelliptic curve, but does not present this power-of-three family or its complete rank filtration. Achter–Howe, arXiv:1710.10726, Section 3, gives and clarifies the general hyperelliptic Cartier–Manin coefficient formula and semilinear convention; the specialized ternary combinatorics and all-iterate rank enumeration are additional arguments here. Garton–Thunder–Weir, arXiv:2403.00120, address distributions and dimensions of \(a\)-number strata, rather than this explicit family's all-iterate filtration. The general matrix and subgroup results are credited to those sources, and only their concrete all-parameter specialization established here is asserted as a candidate new statement.

## Limitations

The result determines ranks of Cartier iterates and two Jacobian invariants, not the complete isomorphism class of the Jacobian's \(3\)-torsion group scheme or its Newton polygon. Nilpotent Cartier is equivalent to \(3\)-rank zero, **not** by itself to supersingularity in the Newton-polygon sense. The quasi-elliptic conclusion concerns exactly the specified minimal regular surfaces; it does not classify their individual fibers or all surfaces covered by Katsura's general theory. The existence of older implicit calculations cannot be completely excluded; exact historical priority is not independently certified.

## References

1. T. Katsura, *Mordell–Weil groups of quasi-elliptic surfaces in characteristic 3*, arXiv:2609.23430v1 (first public version 2026-09-20), Sections 2–4 and Theorem 4.1. https://arxiv.org/abs/2609.23430
2. J. D. Achter and E. W. Howe, *Hasse–Witt and Cartier–Manin matrices: A warning and a request*, arXiv:1710.10726, especially Section 3.1. https://arxiv.org/abs/1710.10726
3. D. Garton, J. L. Thunder and C. Weir, *The distribution of a-numbers of hyperelliptic curves in characteristic three*, arXiv:2403.00120. https://arxiv.org/abs/2403.00120
