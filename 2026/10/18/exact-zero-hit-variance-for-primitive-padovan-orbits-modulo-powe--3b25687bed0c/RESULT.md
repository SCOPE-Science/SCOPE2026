# Exact zero-hit variance for primitive Padovan orbits modulo powers of two

## Finding

For every integer \(k\geq1\), consider the recurrence
\[
u_{n+3}=u_{n+1}+u_n\pmod{2^k}
\]
with an initial triple \((u_0,u_1,u_2)\in(\mathbb Z/2^k\mathbb Z)^3\) having at least one odd coordinate. Call such a triple *primitive*. Time shift identifies two triples if one is a cyclic translate of the other along the recurrence. Every primitive triple lies on a cycle of exact length
\[
T_k=7\cdot2^{k-1},
\]
and there are exactly \(N_k=4^{k-1}\) such cycles. For each cycle \(C\), let \(Z_k(C)\) be the number of positions \(0\leq n<T_k\) where \(u_n=0\pmod{2^k}\).

Under the uniform distribution on the \(N_k\) cycles,
\[
\boxed{\mathbb E[Z_k]=3,\qquad \mathbb E[Z_k^2]=k+8,\qquad \operatorname{Var}(Z_k)=k-1.}
\]
In particular, the average zero count is independent of modulus, while its variance grows exactly linearly in the exponent.

## Assumptions and scope

All recurrences, cycles, and equalities are in the residue ring \(R_k=\mathbb Z/2^k\mathbb Z\), and \(k\) is any positive integer. Zero means the zero residue, not an integer zero before reduction. The probability space is the finite set of primitive cycles with uniform counting measure; because all cycles have the same length, this agrees with uniform primitive initial states. Nonprimitive triples are deliberately excluded, and no assertion is made about their possibly shorter periods or about odd prime powers.

Write
\[
Q=\begin{pmatrix}0&1&0\\0&0&1\\1&1&0\end{pmatrix},\quad e=(1,0,0),\quad v=(u_0,u_1,u_2)^{\mathsf T}.
\]
Then the shifted state is \(Q^nv\) and the observed term is \(eQ^nv\). The determinant of \(Q\) is one.

## Proof

**1. Primitive periods.** Direct integral matrix multiplication gives
\[
Q^7=I+2B,\qquad B=\begin{pmatrix}0&1&1\\1&1&1\\1&2&1\end{pmatrix},\qquad \det B=1,
\]
and
\[
Q^{14}=I+4D,\qquad D=\begin{pmatrix}2&4&3\\3&5&4\\4&7&5\end{pmatrix},\qquad \det D=1.
\]
Since the characteristic polynomial \(X^3+X+1\) is irreducible over \(\mathbb F_2\), \(Q\) has order seven modulo two, acts transitively on the seven nonzero binary states, and \(Q^d-I\) is invertible modulo two whenever \(7\nmid d\).

For every positive integer \(t=2^ju\) with \(u\) odd, repeated squaring, followed by taking an odd power, yields an integral matrix \(H_t\), invertible modulo two, such that
\[
Q^{7t}=I+2^{j+1}H_t.
\]
For \(j=0\), \(H_t\equiv B\pmod2\). For \(j\geq1\), \(H_t\equiv D\pmod2\). This follows because \((I+2^aH)^2=I+2^{a+1}(H+2^{a-1}H^2)\), and \(a\geq2\) in every squaring step after \(Q^{14}\); odd powers leave the leading parity matrix unchanged. Invertibility follows from the displayed determinant identities. Consequently \(Q^{7t}v\equiv v\pmod{2^k}\) for primitive \(v\) if and only if \(2^{j+1}\) is divisible by \(2^k\). Combining this with the order-seven action modulo two shows that the exact period of every primitive \(v\) is \(T_k=7\cdot2^{k-1}\).

There are \(2^{3k}-2^{3(k-1)}=7\cdot2^{3k-3}\) primitive initial triples. Dividing by the common period gives \(N_k=4^{k-1}\) distinct cycles.

**2. Two-time zero constraints.** For each lag \(d\in\{0,1,\ldots,T_k-1\}\), define
\[
C_d=\#\{v\in R_k^3:\ v\text{ primitive},\ ev=0,\ eQ^dv=0\}.
\]
Plainly \(C_0=2^{2k}-2^{2(k-1)}=3\cdot4^{k-1}\). For \(d\ne0\), let \(h_d\) be the minimum of \(k\) and the two binary valuations of the second and third entries of the first row of \(Q^d\), with the valuation of zero interpreted as infinity. The first row has at least one of those entries nonzero modulo \(2^k\), and
\[
h_d=\begin{cases}
0,&7\nmid d,\\
1+\nu_2(d/7),&7\mid d.
\end{cases}
\]
Indeed, if \(7\nmid d\), the first row of \(Q^d\bmod2\) is not \((1,0,0)\), since \(Q^d-I\bmod2\) is invertible. When \(d=7t\), the displayed expansion supplies the valuations: the second and third coordinates of \(eB\bmod2\) are \((1,1)\); those of \(eD\bmod2\) are \((0,1)\). Since \(1\leq t<2^{k-1}\), the resulting \(h_d\) is at most \(k-1\).

Subject to \(ev=0\), write \(v=(0,b,c)^{\mathsf T}\). The other condition is a linear equation \(\alpha b+\beta c=0\pmod{2^k}\) with \(\gcd(\alpha,\beta,2^k)=2^{h_d}\). There are exactly \(2^{k+h_d}\) pairs \((b,c)\) satisfying it, of which exactly half have \(b,c\) both even: after division by \(2^{h_d}\), the induced primitive linear map to \(\mathbb Z/2^{k-h_d}\mathbb Z\) has a kernel of size \(2^{k-h_d}\), every element with \(2^{2h_d}\) lifts; reduction modulo two of its kernel is a one-dimensional subspace, giving equally many primitive and even pairs. Therefore
\[
C_d=2^{k+h_d-1}\qquad(1\leq d<T_k).
\]

**3. Exact lag sum and moments.** Put \(N=N_k=2^{2k-2}\). There are precisely \(6\cdot2^{k-1}\) lags with \(7\nmid d\), and each contributes \(C_d/N=2^{1-k}\); their total contribution is six. All remaining nonzero lags are \(d=7t\) with \(1\leq t<2^{k-1}\). For each \(j\in\{0,\ldots,k-2\}\) there are \(2^{k-2-j}\) such lags with \(\nu_2(t)=j\), each contributing \(C_d/N=2^{j+2-k}\), so each valuation class contributes exactly one. Thus
\[
\frac1N\sum_{d=0}^{T_k-1}C_d=3+6+(k-1)=k+8.
\]

Let \(Z(v)\) count zeros along the cycle of a primitive state \(v\). Cyclic time-shift preserves it. By changing variables \(v\mapsto Q^nv\),
\[
\sum_{v\text{ primitive}}Z(v)=T_kC_0,\qquad
\sum_{v\text{ primitive}}Z(v)^2=T_k\sum_{d=0}^{T_k-1}C_d.
\]
Each cycle supplies exactly \(T_k\) primitive states, hence \(\sum_C Z_k(C)=C_0=3N\) and \(\sum_C Z_k(C)^2=\sum_d C_d=N(k+8)\). The asserted two moments and variance follow. This also includes \(k=1\), when the nonzero-multiple-of-seven lag sum is empty.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. It checks the two integral matrix identities and determinants, confirms the exact lag valuations and resulting moment identities for all \(1\leq k\leq9\), and independently enumerates every primitive cycle and its zero count for all \(1\leq k\leq5\). Execute `python3 verify.py` from the extracted package; the expected terminal statement is `VERIFY_OK`. The infinite assertions rest on the matrix and counting argument above, not on finite computations.

## Relationship to prior work

Taş and Karaduman, *The Padovan Sequences in Finite Groups* (2014), establish periodicity and the prime-power lifting of the period for the standard Padovan sequence and investigate group-valued orbits. Their Section 2 treats one prescribed initial sequence; the current claim concerns **all primitive initial triples** and the **exact second moment of zero hits across their cycles**. The present period calculation has methodological overlap with their period-lifting theorem but the new observable and statistical quantifiers are different. Taş, Deveci, and Karaduman, *The Fibonacci-Padovan Sequences in Finite Groups* (first publicly dated 17 November 2014), is a separate higher-order recurrence and is included to anchor the dated archival literature. Kamlovskii's 2009 and 2013 studies of occurrence frequencies over Galois rings treat the broader theory of local-ring recurrences, with results framed as frequency estimates; the available abstracts do not state this exact Padovan cycle-averaged moment. Those broader works could contain a general implication requiring closer inspection.

## Limitations

This is an exact result only for the stated third-order recurrence modulo powers of two and primitive initial states. It does not give the full distribution of \(Z_k\), the maximal possible zero count, or an odd-prime analogue. It does not establish that the formula is the first possible mathematical derivation; stronger unexamined general frequency theorems or alternate presentations could cover it. The most relevant 2009 and 2013 general frequency papers were available in abstract form, but their complete English texts could not be inspected. Their possible implication is a substantial residual priority risk. The literature search is not a mathematical proof of originality. Independent review has not been performed.

## References

1. S. Taş and E. Karaduman, *The Padovan Sequences in Finite Groups*, Chiang Mai J. Sci. **41** (2014), 456–462. Full text: https://www.thaiscience.info/journals/Article/CMJS/10932734.pdf .
2. S. Taş, Ö. Deveci, and E. Karaduman, *The Fibonacci-Padovan Sequences in Finite Groups*, Maejo Int. J. Sci. Technol. **8** (2014), 279–287, published online 17 November 2014. https://mijst.mju.ac.th/vol8/279-287.pdf .
3. O. V. Kamlovskii, *Frequency Characteristics of Linear Recurrence Sequences over Galois Rings*, Sbornik Math. **200** (2009), 499–519. https://www.mathnet.ru/eng/sm4528 .
4. O. V. Kamlovskii, *Frequency Characteristics of Coordinate Sequences of Linear Recurrences over Galois Rings*, Izvestiya Math. **77** (2013), 1130–1154. https://geodesic.mathdoc.fr/item/IM2_2013_77_6_a2/ .
