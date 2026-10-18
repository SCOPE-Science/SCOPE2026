# Exact \(2\)-adic orbit stratification for divisible-by-four Fibonacci coefficients

## Finding

For integers \(k\ge1\) and \(c\neq0\) with \(4\mid c\), define the invertible state map
\[
T_{c,k}(a,b)=(b,a+cb)\pmod{2^k},\qquad h=\nu_2(c)\ge2.
\]
Let \(C_{k,h}(L)\) count the disjoint cycles with **least** period \(L\). When \(k\le h\), the complete distribution is
\[
C_{k,h}(1)=2^k,\qquad C_{k,h}(2)=\frac{2^{2k}-2^k}{2},
\]
and all other multiplicities vanish. When \(k>h\), it is
\[
C_{k,h}(1)=2^h,\quad C_{k,h}(2)=\frac{2^{2h}-2^h}{2},\quad
C_{k,h}(2^j)=3\cdot2^{2h+j-4}\ \ (2\le j\le k-h+1),
\]
with no other least periods. In particular, the **total number of cycles** is
\[
\#\operatorname{Cycles}(T_{c,k})=
\begin{cases}
2^{2k-1}+2^{k-1},& k\le h,\\
3\cdot2^{h+k-2}-2^{2h-2}+2^{h-1},& k>h.
\end{cases}
\]
More finely, if \(F_j=\#\operatorname{Fix}(T_{c,k}^{2^j})\), then for every \(j\ge0\),
\[
F_0=2^{\min(k,h)},\qquad F_j=2^{2\min(k,h+j-1)}\quad(j\ge1).
\]
All coefficients with the same finite \(h\ge2\) have identical orbit distributions at all moduli \(2^k\), hence their state permutations are conjugate as permutations of their finite sets. This need not be a linear conjugacy: traces distinguish coefficient residues.

## Assumptions and scope

The parameter \(c\) is any nonzero (positive or negative) multiple of four; \(h\) is its finite ordinary two-adic valuation. The modulus exponent \(k\) is any positive integer. Each cycle is counted once, independently of the chosen initial state. The cases of odd \(c\), coefficients \(c\equiv2\pmod4\), and \(c=0\) are outside the assertion.

## Proof

Write the integer companion matrix as
\[
M=\begin{pmatrix}0&1\\1&c\end{pmatrix},\qquad\det M=-1.
\]
It is invertible modulo every power of two. First,
\[
M-I=\begin{pmatrix}-1&1\\1&c-1\end{pmatrix}
\]
has an entry of absolute value one and determinant \(-c\). Its two integer Smith invariant factors are therefore \(1\) and \(|c|\). The number of solutions of \((M-I)v\equiv0\pmod{2^k}\) is exactly \(F_0=2^{\min(k,h)}\).

Second, multiplication gives the **exact integer-matrix identity**
\[
M^2-I=cM=2^h uM,
\]
where \(u=c/2^h\) is odd. Put \(U_1=uM\), an integer matrix with odd determinant. We inductively prove for every integer \(j\ge1\) that
\[
M^{2^j}-I=2^{h+j-1}U_j,\qquad\det U_j\equiv1\pmod2.
\]
If the identity holds at \(j\), squaring yields
\[
M^{2^{j+1}}-I=2^{h+j}
\bigl(U_j+2^{h+j-2}U_j^2\bigr).
\]
The exponent \(h+j-2\ge1\), so \(U_{j+1}\equiv U_j\pmod2\) and is also invertible modulo two. This completes the induction without assumptions on \(u\) beyond oddness.

Since each \(U_j\) is invertible over \(\mathbb Z/2^k\mathbb Z\), the fixed-point congruence for \(M^{2^j}\) is equivalent to \(2^{h+j-1}v=0\pmod{2^k}\). There are precisely \(2^{2\min(k,h+j-1)}\) solutions. That proves the asserted formula for \(F_j\). In particular, \(M^{2^J}=I\pmod{2^k}\) whenever \(J\ge1\) and \(h+J-1\ge k\), so **every orbit length is a power of two**.

The states fixed by the iterate with exponent \(2^j\) are exactly the states on cycles whose least periods divide \(2^j\). Consequently,
\[
C_{k,h}(1)=F_0,\qquad C_{k,h}(2^j)=\frac{F_j-F_{j-1}}{2^j}\quad(j\ge1).
\]
Substitution of the proved fixed-point counts gives the two displayed cases, including both boundary conditions \(k=1\) and \(k=h\). Summing their nonzero multiplicities gives the stated total. Distinct matrices with traces not congruent modulo \(2^k\) cannot be conjugate by invertible linear changes of coordinates, while equality of finite permutation cycle types supplies an ordinary bijective conjugacy. This proves all assertions.

## Verification

The supplied standalone `verify.py` uses exact integer arithmetic. It exhaustively traverses the \(2^{2k}\) states for each of 18 positive and negative coefficients divisible by four and for each \(1\le k\le8\), comparing the complete cycle-size multiset with the formulas (144 independent parameter pairs). It also checks integer matrix powers and that the normalized differences \((M^{2^j}-I)/2^{h+j-1}\) have odd determinant for \(1\le j\le8\). The program outputs `VERIFY_OK` on success. Exhaustive finite tests corroborate, but do not replace, the all-exponent induction above.

## Relationship to prior work

Work on modular \(k\)-Fibonacci sequences traditionally focuses on the canonical orbit starting from a distinguished pair. Falcón and Plaza study canonical periods modulo general integers. Brent's generalized-recurrence theorem supplies a powerful primitive-initial-state result **under irreducibility of the recurrence polynomial modulo two**. The characteristic polynomial here reduces to \((X+1)^2\) modulo two; consequently, that irreducible case does not contain this assertion. Previously examined Pell coefficients with \(\nu_2(c)=1\) lie in a different layer and are excluded here. The point of the present theorem is the parameter-uniform **entire-state** orbit census in the repeated-root regime, including a sharp change once \(k>h\).

## Limitations

The claim concerns only the divisible-by-four, nonzero coefficient family; it does not give a classification for all recurrence coefficients or general composite moduli. Existing broad recurrence theory may imply portions of the result under a reformulation not found in the inspected sources. The full text of Falcón and Plaza's 2009 modular-period paper was not accessible for direct line-by-line comparison; only bibliographic details and its abstract were accessible. The mathematical derivation is complete for the displayed scope; any unindexed earlier equivalence remains an originality risk.

## References

- R. P. Brent, *On the periods of generalized Fibonacci recurrences*, Mathematics of Computation 63 (1994), 389–401; arXiv:1004.5439v1 (public version dated 2010-04-30), https://arxiv.org/html/1004.5439v1.
- S. Falcón and Á. Plaza, *k-Fibonacci sequences modulo m*, Chaos, Solitons & Fractals 41 (2009), 497–504, https://doi.org/10.1016/j.chaos.2008.02.014.
- S. Falcón, *Generalized Fibonacci Sequences Generated from a k–Fibonacci Sequence*, Journal of Mathematics Research 4 (2012), https://doi.org/10.5539/jmr.v4n2p97.
- İ. Gültekin and Y. Taşyurdu, *On Period of the Sequence of Fibonacci Polynomials Modulo m*, Discrete Dynamics in Nature and Society (2013), https://doi.org/10.1155/2013/731482.
