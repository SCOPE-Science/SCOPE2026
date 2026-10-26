# Fourteen-term oases for infinitely many augmented-happy bases

## Finding

For an integer base \(b\ge2\) and a nonnegative integer \(c\), let \(S_{[c,b]}\) send a positive integer to \(c\) plus the sum of the squares of its base-\(b\) digits. An *oasis of length* \(h\) is a set of \(h\) consecutive nonnegative integers \(c\), each admitting a positive fixed point of \(S_{[c,b]}\). Write \(L(b)\) for the largest oasis length in base \(b\).

**Theorem.** The smallest integer base admitting a fourteen-term oasis is \(b=28\), and \(L(28)=14\). Furthermore, infinitely many distinct even bases admit fourteen-term oases. An explicit increasing family begins with \(b=28\) and is defined below by an integral Pell-type recurrence. In particular, the largest oasis length is at least fourteen in infinitely many bases.

The intervening exact values are \(L(22)=11\), \(L(24)=9\), and \(L(26)=11\). For \(b=28\), a minimal-start fourteen-term oasis is the interval of augmenting constants \([8686,8699]\).

## Assumptions and scope

All integers \(b\ge2\) use standard nonnegative base-\(b\) digits. For \(0\le x,y,z<b\), define the three-digit *defect*
\[
D_b(x,y,z)=x b^2+y b+z-x^2-y^2-z^2.
\]
When \(x>0\), the integer \(x b^2+y b+z\) is a positive three-digit fixed point of \(S_{[c,b]}\) precisely when \(c=D_b(x,y,z)\ge0\).

For \(n\ge0\), define positive integers \(u_n,t_n\) starting from \((u_0,t_0)=(1,8)\) by
\[
\begin{aligned}
u_{n+1}&=13741001u_n+71351280t_n+179115300,\\
t_{n+1}&=71351280u_n+370497401t_n+930070960.
\end{aligned}
\]
Let
\[
 m_n=(5t_n+2u_n+14)/4,\qquad b_n=2m_n,
 \qquad C_n=11b_n^2-121+m_n^2.
\]
The theorem asserts that \(m_n\) is a positive integer, the bases \(b_n\) strictly increase, and every \(c\in\{C_n-13,\ldots,C_n\}\) is an oasis parameter for base \(b_n\). This claim does not assert a formula for \(L(b)\) for every even base.

## Proof

**1. An elementary twelve-of-fourteen construction.** Write \(b=2m\). For any \(1\le x<b\), put \(C=x b^2-x^2+m^2\). For \(s\in\{0,1,2,3\}\) and \(z\in\{0,2,3,4\}\),
\[
D_b(x,m-s,z)=C-\bigl(s^2+z(z-1)\bigr).
\]
Among the offsets \(q\in\{0,1,\ldots,13\}\), the expression \(s^2+z(z-1)\) attains *exactly* all values except \(5\) and \(8\). One explicit witness list, giving \((s,z)\) for increasing \(q\), is
\[
0:(0,0),\ 1:(1,0),\ 2:(0,2),\ 3:(1,2),\ 4:(2,0),\
6:(0,3),\ 7:(1,3),\ 9:(3,0),\ 10:(2,3),\ 11:(3,2),\
12:(0,4),\ 13:(1,4).
\]
These are valid digits for every even \(b\ge28\) with \(m\ge14\).

**2. Filling the two missing parameters.** Put
\[
 Q(u,t)=2t^2-(10u+5)t-2u^2-28u+22.
\]
Suppose \(u\ge1\) is odd, \(t\ge8\) is divisible by four, and \(Q(u,t)=0\). Set \(m=(5t+2u+14)/4\), \(b=2m\), \(x=11\), and \(C=11b^2-121+m^2\). These assumptions give \(m\ge14\), all required digits in \([0,b-1]\), and both leading digits \(11\) and \(12\) strictly between zero and \(b\). Direct expansion yields
\[
\begin{aligned}
D_b(12,m-t,b-u)-(C-5)&=-Q(u,t)/2=0,\\
D_b(12,m-t-5,b-u-2)-(C-8)&=-Q(u,t)/2=0.
\end{aligned}
\]
Together with Step 1 this explicitly represents *each* integer from \(C-13\) through \(C\) by a different three-digit fixed-point witness. All these augmenting constants are positive.

**3. Infinitely many admissible parameters.** The seed \((u,t)=(1,8)\) satisfies \(Q(u,t)=0\), with \(m=14\), \(b=28\), and \(C=8699\). Introduce
\[
U=58u+81,\qquad V=4t-10u-5.
\]
A polynomial identity gives
\[
U^2-29V^2-10940=-232Q(u,t).
\]
Let \(a=192119201\) and \(d=35675640\). Direct integer multiplication gives \(a^2-29d^2=1\). Hence the norm-preserving transformation
\[
(U,V)\longmapsto(aU+29dV,\ dU+aV)
\]
preserves \(Q(u,t)=0\). Substituting \(U=58u+81\) and \(V=4t-10u-5\) gives *exactly* the integral affine recurrence in the assumptions. In particular every term satisfies \(Q=0\). Its first component remains odd; the second remains divisible by four, as seen by reduction of the recurrence modulo \(2\) and \(4\). All recurrence coefficients are positive, so \(u_n,t_n,m_n,b_n\) are strictly increasing (apart from no initial ambiguity), and Step 2 applies for every \(n\). Therefore infinitely many distinct bases admit fourteen-term oases.

**4. The first base and its exact maximum.** The odd-base obstruction in Swart et al. (2019), Theorem 3(2), gives \(L(b)=1\) for every odd \(b\). Their Theorem 11 gives all even values through \(b=20\), none exceeding nine. Their Theorem 10 proves that the maximum oasis length is at most the maximum length of a consecutive run among the finite *mirage values* \(D_b(x,y,z)\), \(0\le x,y,z<b\), excluding the zero integer. Exhaustive integer enumeration of those values for bases \(22,24,26,28\) gives maximum run lengths \(11,9,11,14\), respectively. Each maximizing run has positive augmenting constants and therefore consists of actual fixed-point parameters, so these bounds are attained. The positive longest run for \(b=28\) is \([8686,8699]\), also furnished by the explicit seed construction above. Hence no smaller base has an oasis of length fourteen and \(L(28)=14\).

## Verification

The accompanying Python 3 program `verify.py` needs no third-party dependencies. Run `python verify.py` in the directory containing this result. It exhaustively enumerates the entire three-digit mirage spectrum for every even base from \(2\) through \(28\), checks the finite maximum lengths, and independently checks all fourteen explicit digit witnesses for the first four Pell-family bases. It checks the recurrence's Pell norm and exact integer identities at those initial iterates. The unrestricted infinite conclusion follows from the algebraic norm identity, parity preservation, positivity, and direct witness formulas in the proof; no finite calculation is used as an infinite proof.

## Relationship to prior work

Baker Swart, Crook, Grundman, Hall-Seelig, Mei, and Zack (2019) introduced oases, proved five-term oases in every even base at least six, and determined exact maximal oasis lengths for the even bases through twenty. Their Theorem 4 supplies infinitely many translated oases *within any one fixed base*, a different statement from the infinitely many **distinct bases** carrying fourteen-term oases here. Their Theorems 10 and 11 justify the finite maximality calculation and the lower-base comparison. The earlier fixed-point classification by Baker Swart et al. (2016 preprint; 2018 journal) establishes properties of digit-square augmented fixed points but does not assert this infinite fourteen-oasis family.

## Limitations

This result guarantees length at least fourteen for one explicit infinite Pell-type family; it does not classify every base admitting fourteen-term oases, establish uniform growth of maximal oasis lengths, or prove a maximality formula for large family members. The exact maximality claim is only for the first base \(28\). An unindexed equivalent construction could exist; independent priority and independent mathematical audit are not claimed.

## References

1. B. Baker Swart, S. Crook, H. G. Grundman, L. Hall-Seelig, M. Mei, and L. Zack, *Fixed Points of Augmented Generalized Happy Functions II: Oases and Mirages*, Journal of Integer Sequences **22** (2019), Article 19.5.5; preprint arXiv:1908.02194 (first posted 2019-08-06). https://cs.uwaterloo.ca/journals/JIS/VOL22/Grundman/grun9.pdf
2. B. Baker Swart, K. Beck, S. Crook, C. Eubanks-Turner, H. G. Grundman, M. Mei, and L. Zack, *Fixed Points of Augmented Generalized Happy Functions*, Rocky Mountain J. Math. **48** (2018), 47–58; preprint arXiv:1611.02983. https://arxiv.org/abs/1611.02983
