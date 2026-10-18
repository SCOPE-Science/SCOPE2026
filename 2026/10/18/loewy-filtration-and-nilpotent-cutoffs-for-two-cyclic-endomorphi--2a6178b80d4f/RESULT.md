# Loewy filtration and nilpotent cutoffs for two-cyclic endomorphism rings

## Finding
Let \(p\) be any prime and \(1\le a\le b\) be integers. For the abelian group \(G=C_{p^a}\oplus C_{p^b}\), write \(R=\operatorname{End}(G)\) and \(J=\operatorname{Jac}(R)\). The following formulas give **every power** of \(J\), the exact sizes of its Loewy layers, and the maximum nilpotency index of an individual nilpotent endomorphism.

If \(a=b\), then \(R=M_2(\mathbb Z/p^b\mathbb Z)\), \(J=pR\), and for every integer \(k\ge0\),
\[
|J^k|=p^{4\max(b-k,0)}.
\]
The largest nilpotency index of an element of \(R\) is \(2b\).

Suppose \(a<b\), and put \(d=b-a\). For \(k\ge1\), with each matrix entry interpreted modulo the power of \(p\) corresponding to its output row, one has the **exact additive ideals**
\[
J^k=\begin{cases}
\begin{pmatrix}p^kR_a&p^{k-1}R_a\\p^{d+k-1}R_b&p^kR_b\end{pmatrix},&d\ge2,\\[5pt]
\begin{pmatrix}p^{\lceil k/2\rceil}R_a&p^{\lfloor k/2\rfloor}R_a\\p^{1+\lfloor k/2\rfloor}R_b&p^{\lceil k/2\rceil}R_b\end{pmatrix},&d=1,
\end{cases}
\]
where \(R_e=\mathbb Z/p^e\mathbb Z\) and \(p^sR_e=0\) for \(s\ge e\). Consequently \(|J^k|=p^{h_k}\), where
\[
h_k=\begin{cases}
\max(a-k,0)+2\max(a-k+1,0)+\max(b-k,0),&d\ge2,\\[3pt]
\max(a-\lceil k/2\rceil,0)+2\max(a-\lfloor k/2\rfloor,0)+\max(b-\lceil k/2\rceil,0),&d=1.
\end{cases}
\]
Thus \(|J^k/J^{k+1}|=p^{h_k-h_{k+1}}\). The nilpotency index of \(J\), which is also the largest index of a nilpotent element when \(a<b\), is
\[
\begin{cases}2b-1,&b=a+1,\\ b,&b\ge a+2.\end{cases}
\]
For \(a=b\), the radical itself has index \(b\) despite nilpotent elements of index \(2b\). In particular, increasing the exponent gap from one to two changes the maximum index discontinuously from \(2b-1\) to \(b\).

## Assumptions and scope
All groups are finite additive groups, all endomorphisms are group homomorphisms, all ring products are composition, and nilpotency index means the smallest positive exponent with zero power. Here \(p\) is prime, and \(a,b\) are arbitrary positive integers satisfying \(a\le b\). No restriction on \(p\), including characteristic two, is required. The formulas distinguish ideal nilpotency from nilpotency of individual elements; these are not interchangeable for \(a=b\).

## Proof
**Endomorphism normal form.** If \(a<b\), an endomorphism has a unique matrix presentation
\[
\begin{pmatrix}A&B\\p^dC&D\end{pmatrix},
\qquad A,B,C\in R_a,\quad D\in R_b.
\]
The column constraints follow from the orders of generators of the two summands. Matrix multiplication is ordinary multiplication followed by reduction modulo \(p^a\) in the first output row and modulo \(p^b\) in the second. Reduction of the two diagonal entries modulo \(p\) is a surjective ring map \(R\to\mathbb F_p\times\mathbb F_p\); off-diagonal contributions to diagonal products are divisible by \(p^d\). Its kernel \(K\) consists of the matrices with \(p\mid A\) and \(p\mid D\), with unrestricted \(B,C\).

**Radical and its full filtration.** Assign the four matrix corners the minimal \(p\)-valuations
\[
W=\begin{pmatrix}1&0\\d&1\end{pmatrix}.
\]
For any \(k\ge1\), the least attainable valuation in corner \((i,j)\) of a product of \(k\) elements of \(K\) is the minimum weight of a length-\(k\) directed walk from corner index \(j\) to \(i\), with the weight of an edge given by the corresponding entry of \(W\). This is a lower bound term by term in the matrix product. It is also attained: for each such walk, multiply the associated single-corner homomorphisms \(p^{W_{i_{t+1},i_t}}E_{i_{t+1},i_t}\). Every product has precisely one potentially nonzero corner, and its coefficient is exactly the indicated power of \(p\). Since these products additively generate the ring ideal power, the minimum corner valuations characterize \(K^k\) exactly, not merely by inclusion.

Each pair of opposite-direction crossings costs \(d\), whereas two diagonal steps cost \(2\). For \(d\ge2\), crossing pairs cannot improve the weight of a walk, so the four minimum weights, by rows, are \(k,k-1,d+k-1,k\). For \(d=1\), maximize crossing pairs: the four weights are \(\lceil k/2\rceil,\lfloor k/2\rfloor,1+\lfloor k/2\rfloor,\lceil k/2\rceil\). This proves both displayed ideals. In either case these valuations eventually exceed the output exponents, so \(K\) is nilpotent. A nilpotent ideal is contained in the Jacobson radical, and the quotient \(R/K\cong\mathbb F_p\times\mathbb F_p\) is semisimple. Hence \(J=K\). Each entry \(p^sR_e\) contains exactly \(p^{\max(e-s,0)}\) elements, giving the displayed sizes and all Loewy quotient orders.

**Sharp cutoffs for unequal exponents.** For \(d\ge2\), the formula yields \(J^b=0\); the diagonal endomorphism \(\operatorname{diag}(0,p)\) satisfies \(f^{b-1}\ne0\), so the maximal nilpotency index is \(b\). For \(d=1\), the formula yields \(J^{2b-1}=0\) but \(J^{2b-2}\ne0\); indeed
\[
f=\begin{pmatrix}0&1\\p&0\end{pmatrix}
\]
has \(f^2\) equal to scalar multiplication by \(p\) on both summands, and \(f^{2b-2}\ne0\) on the larger summand. Since \(R/J\) has no nonzero nilpotents, the nilpotent elements of \(R\) are exactly the elements of \(J\), proving maximality.

**Equal exponents.** When \(a=b\), reduction of \(M_2(R_b)\) modulo \(p\) has semisimple quotient \(M_2(\mathbb F_p)\), hence its radical is \(pM_2(R_b)\), with the stated filtration. If \(f\) is nilpotent, its reduction is a nilpotent \(2\times2\) matrix and therefore has square zero; consequently \(f^2\in pM_2(R_b)\) and \(f^{2b}=0\). The same matrix \(f=\begin{psmallmatrix}0&1\\p&0\end{psmallmatrix}\) satisfies \(f^2=pI\) and \(f^{2b-1}\ne0\), including at \(b=1\), establishing the sharp index \(2b\).

## Verification
The included standard-library Python program `checker.py` constructs the endomorphism rings explicitly for several finite prime powers, multiplies matrices using their distinct row moduli, generates the additive ideal powers without calling the displayed formula, and compares their cardinalities with the formulas above. It also checks the exact maximal cutoff on every radical element for seven unequal-exponent cases and the sharp equal-exponent witnesses for four cases. Run `python3 checker.py`; the expected final line is `ALL_CHECKS_PASSED`. These finite tests supplement but do not replace the all-exponents proof.

## Relationship to prior work
The matrix representation of endomorphisms of finite abelian \(p\)-groups is classical and appears in A. Mader, *The Automorphism Group of Finite Abelian \(p\)-Groups* (2012). P. Keef, *Jacobson radicals, abelian \(p\)-groups and the \(\oplus_c\)-topology* (first publicly published April 16, 2024), investigates Jacobson radicals for broader, often infinite, group classes. P. Senden, *The Reidemeister spectrum of finite abelian groups* (2023), studies fixed points of endomorphisms. The proposed contribution is the explicit full Loewy-power/quotient cardinality profile for every pair of cyclic summands together with its sharp three-way nilpotent-element cutoff, not the classical endomorphism normal form or the mere existence of a nilpotent radical.

## Limitations
The formula concerns exactly two cyclic primary summands, not general invariant-factor decompositions with three or more summands, and makes no statement about complete similarity or conjugacy classes of individual endomorphisms. Earlier general monographs on endomorphism rings may contain equivalent radical-power formulas not located in this literature examination; novelty therefore remains subject to that risk.

## References
1. A. Mader, *The Automorphism Group of Finite Abelian \(p\)-Groups*, Ann. Sci. Math. Québec 36 (2012), 559–575. https://www.labmath.uqam.ca/~annales/volumes/36-2/PDF/559-575.pdf
2. P. Keef, *Jacobson radicals, abelian \(p\)-groups and the \(\oplus_c\)-topology*, Rend. Sem. Mat. Univ. Padova 155 (2026), 23–40; first online April 16, 2024. https://doi.org/10.4171/RSMUP/162
3. P. Senden, *The Reidemeister spectrum of finite abelian groups*, Proc. Edinburgh Math. Soc. 66 (2023), 940–959. https://doi.org/10.1017/S0013091523000500
4. P. A. Krylov, A. V. Mikhalev and A. A. Tuganbaev, *The Jacobson Radical of the Endomorphism Ring*, in *Endomorphism Rings of Abelian Groups* (2003), pp. 135–180, DOI 10.1007/978-94-017-0345-1_4 (potential broader-coverage comparison; full chapter not inspected).
