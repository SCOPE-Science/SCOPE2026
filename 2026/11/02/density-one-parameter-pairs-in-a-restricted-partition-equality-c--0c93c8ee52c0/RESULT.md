# Density-one parameter pairs in a restricted-partition equality conjecture

## Finding
For each integer \(a\ge3\), let \(P_a(N)\) count the nonnegative integer solutions of \(r+2s+at=N\). For **every** pair of integers \(3\le a<b\) such that \(ab\) is not a perfect square, there exist infinitely many distinct positive integer pairs \((X,Y)\) satisfying
\[
P_a(X)=P_b(Y).
\]
More precisely, infinitely many solutions occur with \(X\) divisible by \(2a\) and \(Y\) divisible by \(2b\). Consequently, among parameter pairs \(3\le a<b\le H\), the proportion for which this infinite-solution assertion is proved is \(1-O(\log H/H)\). This establishes the density-one parameter case of Tengely and Ulas's Conjecture 4.6 (2021), not its remaining square-product cases.

## Assumptions and scope
The variables \(a,b\) are fixed integers with \(3\le a<b\) and nonsquare \(ab\). Partitions are unordered and their allowed part sizes are exactly \(\{1,2,a\}\) and \(\{1,2,b\}\), respectively. All arithmetic is over ordinary nonnegative integers; the solutions constructed have positive partition arguments.

Put \(d_c=\lfloor c/2\rfloor+2\). For each integer \(c\ge3\) and \(n\ge0\), direct partition enumeration gives
\[
P_c(2cn)=\sum_{j=0}^{2n}\left(\left\lfloor\frac{cj}{2}\right\rfloor+1\right)=cn^2+d_cn+1.
\]
The first equality fixes the normalization for both parities of \(c\).

## Proof
**Step 1 (a fixed quadratic section).** The displayed partition sum counts the number of \(1\)- and \(2\)-part decompositions remaining after choosing the number of \(c\)-parts. Summing yields \(P_c(2cn)=cn^2+d_cn+1\) when \(c\) is even or odd; in the odd case precisely \(n\) summands have a half-integer discarded by the floor.

**Step 2 (Pell transport and an invariant).** Since \(ab\) is positive and nonsquare, classical Pell theory supplies positive integers \(u,v\) with
\[
u^2-abv^2=1,\qquad u>1,\quad v>0.
\]
Set
\[
T=\begin{pmatrix}u&av\\bv&u\end{pmatrix},\qquad J=\begin{pmatrix}b&0\\0&-a\end{pmatrix}.
\]
A direct multiplication gives \(\det T=1\) and \(T^{\mathsf T}JT=J\). Hence \(bX^2-aY^2\) is constant along iterates \((X,Y)^{\mathsf T}\mapsto T(X,Y)^{\mathsf T}\).

**Step 3 (the integral congruence lattice).** Reduce \(T\) modulo \(2ab\). Its determinant is \(1\), so it belongs to the finite group \(\mathrm{GL}_2(\mathbb Z/(2ab)\mathbb Z)\); therefore some integer \(h\ge1\) satisfies \(T^h\equiv I\pmod{2ab}\). Define for \(j\ge1\)
\[
\begin{pmatrix}X_j\\Y_j\end{pmatrix}
=T^{hj}\begin{pmatrix}d_a\\d_b\end{pmatrix},\qquad
n_j=\frac{X_j-d_a}{2a},\quad m_j=\frac{Y_j-d_b}{2b}.
\]
The congruence shows that \(n_j,m_j\) are integers. All entries of \(T\) are positive, and the starting coordinates \(d_a,d_b\) are positive, so \(n_j,m_j>0\) and both grow strictly as \(j\) increases.

**Step 4 (partition equality).** By the invariant and the initial vector,
\[
bX_j^2-aY_j^2=b d_a^2-a d_b^2.
\]
Expanding \(X_j=2an_j+d_a\) and \(Y_j=2bm_j+d_b\) gives
\[
4ab\bigl(an_j^2+d_an_j-bm_j^2-d_bm_j\bigr)=0.
\]
Thus \(an_j^2+d_an_j+1=bm_j^2+d_bm_j+1\); Step 1 gives \(P_a(2an_j)=P_b(2bm_j)\). Distinctness and positivity from Step 3 prove infinitely many positive solutions.

**Step 5 (parameter density).** If \(ab\) is a square, there is a unique squarefree integer \(s\) such that \(a=sr^2\), \(b=st^2\), and \(r<t\). Hence the number of pairs \(3\le a<b\le H\) not covered by the nonsquare condition is bounded above by
\[
\sum_{s\le H}\binom{\lfloor\sqrt{H/s}\rfloor}{2}
\le\frac H2\sum_{s\le H}\frac1s=O(H\log H).
\]
There are \(\Theta(H^2)\) total eligible ordered-by-size pairs, proving the stated proportion.

For example, taking \((a,b)=(3,4)\) and the Pell solution \(7^2-12\cdot2^2=1\) yields \((n,m)=(7,6)\) after one matrix step, and
\[
P_3(42)=169=P_4(48).
\]

## Verification
The supplementary `verify_partition_pell.py` uses only integer arithmetic. It independently checks the quadratic partition-section formula against direct enumeration, searches Pell fundamental units by continued fractions, checks that the claimed matrix orders exist modulo \(2ab\) for many small nonsquare parameter pairs, and checks the resulting polynomial equalities, positivity, distinctness, and congruences. It also checks \(P_3(42)=P_4(48)=169\) by direct enumeration. Its finite tests are not a substitute for Steps 1–5 of the proof.

Run `python3 verify_partition_pell.py`; its expected last line is `VERIFY_OK`.

## Relationship to prior work
Tengely and Ulas, *Equal values of certain partition functions via Diophantine equations*, first publicly posted on 10 February 2021 as arXiv:2102.05352, prove the quadratic residue-class formulas (Theorem 4.1). Their Theorem 4.5 obtains infinitely many solutions under the simultaneous conditions that \(a,b\) are divisible by four and that at least one of \(a/2,b/2\) is nonsquare; their Conjecture 4.6 proposes infinite solutions for all \(3\le a<b\). The present nonsquare-product theorem is a distinct broad criterion, including \((a,b)=(3,4)\) and every pair with one odd parameter and nonsquare product. Neither theorem subsumes the other: the earlier result can also cover square-product pairs. The main new step is the determinant-one Pell action that preserves both the quadratic equality and, after taking a power, both integer congruence lattices. This is an application of classical Pell theory, not a new Pell existence theorem.

## Limitations
The argument does **not** handle parameter pairs for which \(ab\) is a perfect square, and it does not prove the full Conjecture 4.6. The constructive exponent \(h\) may be large; no uniform small bound or least-solution formula is asserted. The proof of originality is based on the inspected 2021 primary paper and targeted research searches, not on exhaustive coverage of every unindexed or later publication. The computations verify finite examples, not the infinite theorem.

## References
1. Szabolcs Tengely and Maciej Ulas, *Equal values of certain partition functions via Diophantine equations*, arXiv:2102.05352, initial posting 2021-02-10. https://arxiv.org/abs/2102.05352
2. Szabolcs Tengely and Maciej Ulas, *Equal values of certain partition functions via Diophantine equations*, Research in Number Theory **7**, article 67 (2021), DOI:10.1007/s40993-021-00293-7. https://link.springer.com/article/10.1007/s40993-021-00293-7
3. Classical Pell-equation existence theorem and unit action on indefinite binary quadratic forms, used only in its standard form.
