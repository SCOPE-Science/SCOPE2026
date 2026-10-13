# A strict second-order packing--covering gap for doubly-even binary codes
## Finding
Let \(C\subseteq\mathbb F_2^n\) be a binary doubly-even linear code with \(2\le \dim C\le n-2\). Then
\[
d_2(C)\le 2R_2(C).
\]
Equivalently, for the second generalized packing radius
\[
\delta_2(C)=\left\lfloor\frac{d_2(C)-1}{2}\right\rfloor,
\]
one has the strict packing--covering inequality
\[
\delta_2(C)\le R_2(C)-1.
\]
Thus equality in the generalized packing--covering inequality is impossible at order two for every doubly-even binary code in the admissible range.

## Assumptions and scope
A binary code is **doubly even** when every codeword has Hamming weight divisible by \(4\). For a linear code \(C\), the second generalized Hamming weight \(d_2(C)\) is the least support size of a two-dimensional subcode.

For a \(2\times n\) binary matrix \(X\), write \(\operatorname{wt}_{\mathrm{col}}(X)\) for the number of its nonzero columns, and let \(C^2\) be the set of \(2\times n\) matrices whose two rows lie in \(C\). The second generalized covering radius has the equivalent matrix form
\[
R_2(C)=\max_{X\in\mathbb F_2^{2\times n}}\min_{Y\in C^2}\operatorname{wt}_{\mathrm{col}}(X-Y).
\]
The inequalities below use only these definitions and elementary rank facts. The restriction \(2\le \dim C\le n-2\) is the standard admissible order-two range in the recent generalized packing--covering literature.

## Proof
Put \(d=d_2(C)\) and \(r=R_2(C)\). Choose a two-dimensional subcode \(D\le C\) with support size \(d\), and choose a rank-two generator matrix \(M\in\mathbb F_2^{2\times n}\) for \(D\). Outside \(\operatorname{Supp}(D)\) the columns of \(M\) are zero. After fixing a basis of \(D\), each nonzero column of \(M\) is one of the three vectors
\[
(1,0)^{\mathsf T},\qquad (0,1)^{\mathsf T},\qquad (1,1)^{\mathsf T}.
\]
Let their multiplicities be \(a,b,c\), respectively. The three nonzero words of \(D\) then have weights
\[
a+c,\qquad b+c,\qquad a+b.
\]
Because \(D\) is a subcode of the doubly-even code \(C\), all three numbers are divisible by \(4\). Hence
\[
2a=(a+c)+(a+b)-(b+c)\equiv0\pmod4,
\]
and similarly \(2b\equiv2c\equiv0\pmod4\). Therefore \(a,b,c\) are all even. In particular \(d=a+b+c\) is even.

Split the support of \(M\) into two sets \(A\) and \(B\) by putting exactly half of each projective column class in each set. Thus every class of multiplicity \(m\) contributes \(m/2\) columns to \(A\) and \(m/2\) to \(B\), and
\[
|A|=|B|=d/2.
\]
Define \(X\in\mathbb F_2^{2\times n}\) by taking \(X_{|j}=M_{|j}\) for \(j\in A\) and \(X_{|j}=0\) otherwise. By the definition of \(r\), there is \(Y\in C^2\) with
\[
\operatorname{wt}_{\mathrm{col}}(X-Y)\le r.
\]
Set \(Z=M-Y\in C^2\).

Assume for contradiction that \(d\ge2r+2\). Then
\[
\operatorname{wt}_{\mathrm{col}}(Y)
\le |A|+r=d/2+r\le d-1,
\]
and, because \(Z=(M-X)+(X-Y)\), the same estimate gives
\[
\operatorname{wt}_{\mathrm{col}}(Z)\le d-1.
\]
No matrix in \(C^2\) of column-support size below \(d=d_2(C)\) can have rank two. Hence \(\operatorname{rank}Y\le1\) and \(\operatorname{rank}Z\le1\). Since \(M=Y+Z\) has rank two, both ranks are exactly one.

We now record the elementary rank-one decomposition needed below. Since the row spaces of \(Y\) and \(Z\) are contained in the row space of \(M\), there are \(2\times2\) matrices \(P,Q\) with \(Y=PM\) and \(Z=QM\). Because \(M\) has full row rank and \(M=Y+Z\), one has \(P+Q=I\). Moreover \(P\) and \(Q=I-P\) both have rank one. Thus \(\det P=\det(I-P)=0\), so \(\operatorname{tr}P=1\); Cayley--Hamilton gives \(P^2=P\). Consequently \(\operatorname{im}P\) and \(\ker P\) are distinct one-dimensional subspaces of \(\mathbb F_2^2\), and \(\ker(I-P)=\operatorname{im}P\).

For \(j\in A\),
\[
(X-Y)_{|j}=(I-P)M_{|j},
\]
which vanishes exactly when the column class of \(M_{|j}\) is \(\operatorname{im}P\). For \(j\in B\),
\[
(X-Y)_{|j}=-PM_{|j},
\]
which vanishes exactly when its column class is \(\ker P\). These are two distinct projective classes. If their total multiplicities in the support are \(m_1\) and \(m_2\), the exact half split therefore gives precisely \((m_1+m_2)/2\) zero columns of \(X-Y\) inside \(\operatorname{Supp}(D)\). Since \(m_1+m_2\le d\),
\[
\operatorname{wt}_{\mathrm{col}}(X-Y)
\ge d-\frac{m_1+m_2}{2}
\ge \frac d2
\ge r+1,
\]
contradicting the choice of \(Y\). Therefore \(d\le2r+1\). Because \(d\) is even, in fact
\[
d_2(C)=d\le2r=2R_2(C).
\]
Finally,
\[
\delta_2(C)=\left\lfloor\frac{d-1}{2}\right\rfloor=\frac d2-1\le r-1=R_2(C)-1.
\]

## Verification
The accompanying `verify.py` performs two finite consistency checks that are separate from the symbolic proof. First, it exhaustively enumerates every two-dimensional binary subspace of lengths \(4,5,6,7\), retains the doubly-even ones, computes \(R_2\) directly from the defining minimax problem, and verifies both displayed inequalities. There are no doubly-even two-dimensional codes at lengths \(4\) and \(5\); at length \(6\) there are \(15\), all with \((d_2,R_2)=(6,4)\); at length \(7\) there are \(105\), all with \((d_2,R_2)=(6,5)\).

Second, the script checks the parity lemma for every triple \((a,b,c)\) with \(0\le a,b,c\le20\): whenever \(a+c\), \(b+c\), and \(a+b\) are divisible by \(4\), all three multiplicities are even. The expected final line is `VERIFY_OK`.

These finite computations are checks only; the theorem for arbitrary length follows from the proof above.

## Relationship to prior work
Essayag and Zabokritskiy study the same generalized packing--covering problem and, in arXiv:2609.19098, prove \(d_t(C)\le2R_t(C)+1\) when the alphabet size satisfies \(q\ge R_t(C)\), as well as the conjectured \(+2\) bound for bounded redundancy. Their paper has primary MSC2020 94B05 and was first public on 2026-09-16. In the binary case their \(+1\) theorem applies only when \(R_t(C)\le2\); it does not imply the present bound for arbitrary doubly-even codes.

Yu and Schwartz prove the universal order-two inequality
\[
d_2(C)\le2R_2(C)+2.
\]
Their proof partitions the projective column multiset of a minimum-support two-dimensional subcode and then uses a rank-one idempotent decomposition. The doubly-even condition supplies an additional structural fact absent in the general argument: all three binary projective multiplicities are even, so every projective class can be split exactly in half. That exact split removes the two-unit slack.

Alfarano, Marino, Neri, and Trombetti subsequently prove the full generalized packing--covering conjecture for every linear code, again with the universal bound \(d_t(C)\le2R_t(C)+2\). Their full text contains no doubly-even or divisible-code specialization. Focused searches using the doubly-even, \(4\)-divisible, generalized-covering, and second-order formulations located these general results and classical Type-II covering work, but no statement implying the class-wide strict order-two gap above.

## Limitations
The theorem is specific to binary doubly-even codes and to order two. It does not claim the analogous one-unit packing-radius gap for merely even binary codes, for nonbinary divisible codes, or for higher generalized orders. It also does not determine \(R_2(C)\) for any particular infinite family. The literature comparison reduces but cannot eliminate the risk of an older equivalent statement under different terminology.

## References
1. I. B. Essayag and A. L. Zabokritskiy, “Auxiliary Codes and the Generalized Packing-Covering Conjecture,” arXiv:2609.19098; first public 2026-09-16. See the introduction, Theorem 1.2, and Theorem 3.1.
2. G. Yu and M. Schwartz, “On the Generalized Packing and Covering Radii of Codes,” arXiv:2609.14477v1, 2026. See Section 3, especially Lemmas 3--4 and Theorem 5.
3. G. N. Alfarano, G. Marino, A. Neri, and R. Trombetti, “A proof of the generalized packing-covering conjecture,” arXiv:2609.34910v1, 2026. See Theorem 1.1 and the proof outline.
