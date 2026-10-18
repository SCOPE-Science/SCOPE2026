# Jordan-type point counts for bounded-power matrices over finite dual numbers

## Finding

Let \(q\) be any prime power, \(n\ge 0\), \(d\ge 3\), and \(R_q=\mathbb F_q[\varepsilon]/(\varepsilon^2)\). For each partition \(\lambda\vdash n\) with largest part at most \(d\), let \(m_s\) be the number of parts equal to \(s\), with \(1\le s\le d\). Define
\[
 c(\lambda)=\sum_{j=1}^{d}\left(\sum_{s=j}^{d}m_s\right)^2,
 \qquad
 r_d(\lambda)=\sum_{a,b=1}^{d}m_am_b\max\{0,a+b-d\},
\]
\[
 P_h(q)=\prod_{j=1}^{h}(1-q^{-j}), \qquad
 g_n(q)=|\operatorname{GL}_n(\mathbb F_q)|=\prod_{j=0}^{n-1}(q^n-q^j).
\]
The exact Jordan-type generating polynomial for matrices \(X\in M_n(R_q)\) satisfying \(X^d=0\), graded by the Jordan blocks of their reduction \(\bar X\), is
\[
 \boxed{\mathcal J_{n,d}(q;z_1,\ldots,z_d)=
 \sum_{\substack{\lambda\vdash n\\ \lambda_1\le d}}
 \frac{g_n(q)\,q^{n^2-c(\lambda)-r_d(\lambda)}}{\prod_{s=1}^{d}P_{m_s}(q)}
 \prod_{s=1}^{d}z_s^{m_s}.}
\]
In particular, the exact number is \(\mathcal J_{n,d}(q;1,\ldots,1)\); each summand, despite its rational-product notation, is an integer. For fixed reduction \(A\in M_n(\mathbb F_q)\) of Jordan type \(\lambda\), the number of its bounded-power lifts is exactly
\[
 \boxed{q^{n^2-r_d(\lambda)}.}
\]
The decisive rank formula holds over every field, independently of characteristic: on a pair of nilpotent Jordan blocks of sizes \(a,b\le d\), the linearization of the \(d\)-th matrix power has rank exactly \(\max\{0,a+b-d\}\).

## Assumptions and scope

Matrix powers are ordinary associative powers; \(\varepsilon^2=0\). A reduction Jordan type is defined by the nilpotent operator \(\bar X\) on the \(n\)-dimensional vector space over \(\mathbb F_q\). For the empty partition set \(\lambda_1=0\). In the zero-dimensional case take the unique empty matrix, \(g_0(q)=1\), and empty products equal to one. The theorem requires \(d\ge3\); the exponent-two case is outside this claim. No assumption that the characteristic exceeds \(d\) is made.

For example, for \(d=3\) the total counts at \(n=2\) and \(n=3\) simplify to
\[
 \mathcal J_{2,3}(q;1,1,1)=q^5+q^4-q^3,
\]
\[
 \mathcal J_{3,3}(q;1,1,1)=q^9+(q^3-1)(q+1)q^8+(q^3-1)(q^3-q)q^6.
\]
Thus the totals for \((q,n,d)=(2,2,3),(3,2,3),(2,3,3),(2,3,4)\) are respectively \(40,297,8576,16640\).

## Proof

**1. Reduce the power equation.** Every matrix is uniquely \(X=A+\varepsilon B\) with \(A,B\in M_n(\mathbb F_q)\). Direct multiplication gives
\[
 X^d=A^d+\varepsilon\mathcal L_{A,d}(B),\qquad
 \mathcal L_{A,d}(B)=\sum_{i=0}^{d-1}A^iBA^{d-1-i}.
\]
Thus \(X^d=0\) if and only if \(A^d=0\) and \(B\in\ker\mathcal L_{A,d}\). For nilpotent \(A\), the Jordan decomposition has all block sizes at most \(d\).

**2. Calculate the linearization rank without characteristic restrictions.** Choose a Jordan basis for \(A\). Its blocks of the linear operator \(\mathcal L_{A,d}\), indexed by ordered pairs of Jordan summands of sizes \(a,b\), act on the matrix space \(M_{a\times b}(\mathbb F_q)\). On identifying that space with the quotient \(\mathbb F_q[x,y]/(x^a,y^b)\) using the standard shift bases (reversing the right-hand basis if necessary), the operator is multiplication by
\[
 F_d(x,y)=\sum_{i=0}^{d-1}x^iy^{d-1-i}.
\]
Since \((x-y)F_d=x^d-y^d=0\) in this quotient, the image is spanned by \(F_d,xF_d,x^2F_d,\ldots\). If \(a+b\le d\), then \(F_d=0\). Otherwise \(x^tF_d\) is nonzero precisely for \(0\le t\le a+b-d-1\): indeed the term \(x^{t+i}y^{d-1-i}\) survives for some \(i\) exactly when \(d-b\le i\le a-1-t\); all its coefficients are one and no monomials collide. These nonzero terms have different homogeneous degrees and are linearly independent. The rank is therefore \(\max\{0,a+b-d\}\), even when the field characteristic divides \(d\).

There are \(m_a m_b\) ordered Jordan-block pairs of sizes \(a,b\). Consequently \(\operatorname{rank}\mathcal L_{A,d}=r_d(\lambda)\) and \(\dim\ker\mathcal L_{A,d}=n^2-r_d(\lambda)\). Exactly \(q^{n^2-r_d(\lambda)}\) choices of \(B\) work for each \(A\).

**3. Count each reduction orbit.** The similarity class of the nilpotent Jordan matrix of type \(\lambda\) has size \(g_n(q)/|C_{\mathrm{GL}_n}(A)|\). Its full matrix centralizer has dimension \(c(\lambda)=\sum_j(\lambda_j')^2\), because \(\dim\operatorname{Hom}_{\mathbb F_q[t]}(\mathbb F_q[t]/(t^a),\mathbb F_q[t]/(t^b))=\min(a,b)\). The unit group of that centralizer has order
\[
 |C_{\mathrm{GL}_n}(A)|=q^{c(\lambda)}\prod_{s=1}^{d}P_{m_s}(q).
\]
To verify this expression directly, its endomorphism algebra has semisimple quotient \(\prod_sM_{m_s}(\mathbb F_q)\); the Jacobson radical has dimension \(c(\lambda)-\sum_sm_s^2\). Invertibility is detected in that quotient, giving \(q^{c-\sum m_s^2}\prod_s|\mathrm{GL}_{m_s}(\mathbb F_q)|\), equal to the displayed formula. Multiply the orbit size by the lift count from Step 2 and sum over partitions. This gives the polynomial and proves the theorem.

## Verification

The independent arithmetic checker `check.py` computes the linearization directly using matrix multiplication and finite-field Gaussian elimination, rather than using the rank formula in the proof. It checks all ordered block-size pairs through exponent seven over prime fields of sizes \(2,3,5,7\). It additionally enumerates every residue and every dual part for \((q,n,d)=(2,1,3),(2,2,3),(3,2,3),(2,3,3),(2,3,4),(2,3,2)\) and compares the resulting full counts with the Jordan-orbit formula. All tests passed. The final exponent-two test is a boundary compatibility check, not a novel exponent-two assertion. Execute `python check.py` with Python 3; no third-party libraries are needed.

## Relationship to prior work

Danchev, García, and Gómez Lozano, *Decompositions of Matrices into Potent and Square-Zero Matrices* (arXiv:2102.10460, first available 2021-02-20), establish structural decompositions over finite rings with square-zero radicals and prove existence of square-zero lifts under regularity hypotheses. Those statements do not determine the Jordan-type count of solutions to \(X^d=0\) for arbitrary \(d\ge3\). Qi and Cui, *Eigenvalues and Jordan Forms of Dual Complex Matrices* (arXiv:2306.12428), study spectral/Jordan normal forms over dual complex numbers, not finite-field point counts by reduction type. The exponent-two case is outside the present claim. Restricting to a single Jordan block does not determine the mixed-block contributions in the formula above.

## Limitations

The result counts matrices, not similarity classes of matrices over the dual-number ring. The arithmetic checks cover selected prime fields and small sizes, whereas the general theorem follows from the characteristic-free proof. No assertion is made that all possible related Hall-polynomial, jet-scheme, or module-enumeration literature has been exhaustively indexed or inspected; such a reformulation is a residual originality risk. 

## References

- P. Danchev, E. García, M. Gómez Lozano, *Decompositions of Matrices into Potent and Square-Zero Matrices*, arXiv:2102.10460 (2021), https://arxiv.org/pdf/2102.10460.
- L. Qi and C. Cui, *Eigenvalues and Jordan Forms of Dual Complex Matrices*, arXiv:2306.12428 (2023), https://arxiv.org/pdf/2306.12428.
- A. Knutson and P. Zinn-Justin, *A scheme related to the Brauer loop model*, arXiv:math/0503224 (2005), https://arxiv.org/abs/math/0503224; related square-zero schemes, not the claimed bounded-power count.
