# The exact five-adic residue frequencies of derangement numbers

## Finding

Let \(D_0=1\) and \(D_n=nD_{n-1}+(-1)^n\) for integers \(n\ge1\); thus \(D_n\) is the number of fixed-point-free permutations of \(n\) objects. For every integer \(k\ge1\), put \(M=5^k\). **Theorem:** for each residue \(r\in\mathbb Z/M\mathbb Z\),

\[
\#\{0\le n<2M:D_n\equiv r\pmod M\}=c_{r\bmod5},\qquad(c_0,c_1,c_2,c_3,c_4)=(2,3,1,1,3).
\]

Therefore every residue class modulo every power of five contains infinitely many derangement numbers, and its exact natural density among the indices is

\[
\delta_{k,r}=\frac{c_{r\bmod5}}{2\cdot5^k}.
\]

The least period of the derangement sequence modulo \(M\) is \(2M\). This period was established earlier (Miska, 2015); it is included here only to normalize the new residue-frequency classification. A supplementary consequence is that five is the least prime \(p\) for which every residue class modulo every \(p^k\) is attained: derangements omit residue \(3\) modulo four and residues \(3,6\) modulo nine.

## Assumptions and scope

All indices \(n\) are nonnegative integers. A residue is counted with multiplicity of its indices, not as a distinct numerical value. The valuation \(\nu_5(z)\) for nonzero \(z\in\mathbb Z_5\) is the exponent of five dividing \(z\). The proof concerns all positive integer exponents \(k\), with no asymptotic restriction or unproved computational extrapolation. The analytic variable \(x\) below lies in the ring \(\mathbb Z_5\) of five-adic integers.

## Proof

**1. A five-adic interpolation.** Write

\[
P_j(x)=\prod_{i=0}^{j-1}(x-i),\qquad P_0(x)=1,\qquad F(x)=\sum_{j=0}^{\infty}(-1)^jP_j(x).
\]

Among any \(j\) consecutive integers, at least \(\lfloor j/5\rfloor\) have a prescribed residue modulo five. For every \(x\in\mathbb Z_5\), this implies \(\nu_5(P_j(x))\ge\lfloor j/5\rfloor\). Consequently the series for \(F\) converges uniformly on \(\mathbb Z_5\), and its reduction modulo \(5^k\) is represented by the finite integer polynomial \(\sum_{j=0}^{5k-1}(-1)^jP_j(x)\). In particular, \(x\equiv y\pmod{5^k}\) implies \(F(x)\equiv F(y)\pmod{5^k}\).

For nonnegative integers \(n\), each \(P_j(n)\) with \(j>n\) vanishes. Changing variables in the standard inclusion-exclusion formula gives

\[
D_n=n!\sum_{h=0}^n\frac{(-1)^h}{h!}=(-1)^n\sum_{j=0}^n(-1)^jP_j(n)=(-1)^nF(n).
\]

This familiar interpolation and the basic period are not asserted as new.

**2. The noncritical five-adic derivative table.** Differentiate the polynomial factors termwise. In every derivative term for \(P_j'(x)\), one of \(j\) consecutive factors has been removed, so at least \(\lfloor j/5\rfloor-1\) remaining factors are divisible by five. These valuations grow without bound; hence the derivative series converges uniformly. For \(j\ge10\), every derivative term has a factor divisible by five, and for \(j\ge5\), \(P_j(x)\equiv0\pmod5\). Thus evaluating only the indicated finite polynomials gives the exact residue table

\[
\begin{array}{c|ccccc}
a\bmod5&0&1&2&3&4\\\hline
F(a)\bmod5&1&0&1&3&4\\
F'(a)\bmod5&1&3&4&2&4
\end{array}
\]

Every listed derivative is a unit in \(\mathbb Z_5\). To verify the table reproducibly, for \(F(a)\) sum \((-1)^jP_j(a)\) over \(0\le j<5\); for \(F'(a)\), sum \((-1)^j\sum_{i<j}\prod_{0\le h<j,\,h\ne i}(a-h)\) over \(0\le j<10\).

**3. Exact isometry on five-adic residue disks.** Fix \(a\in\{0,1,2,3,4\}\) and take distinct \(x,y\in a+5\mathbb Z_5\). The polynomial difference quotient is

\[
\frac{P_j(x)-P_j(y)}{x-y}
=\sum_{i=0}^{j-1}
\left(\prod_{h<i}(x-h)\right)
\left(\prod_{h>i}(y-h)\right).
\]

For \(j\ge10\), the \(j\) indices include at least two congruent to \(a\pmod5\). Each summand deletes at most one index; hence the displayed quotient is zero modulo five. The quotient series also converges five-adically, because every summand has at least \(\lfloor j/5\rfloor-1\) factors divisible by five. For the remaining finite terms, reduction modulo five sends both \(x,y\) to \(a\), so the quotient reduces to \(P_j'(a)\). Thus

\[
\frac{F(x)-F(y)}{x-y}\equiv F'(a)\not\equiv0\pmod5,
\]

and therefore

\[
\nu_5(F(x)-F(y))=\nu_5(x-y)\quad\text{whenever }x\equiv y\pmod5\text{ and }x\ne y.
\]

This also proves that each disk \(a+5\mathbb Z_5\) maps **bijectively** onto \(F(a)+5\mathbb Z_5\): injectivity is the isometry. For surjectivity modulo \(5^h\), suppose a solution \(x_h\equiv a\pmod5\) has been constructed. Its five candidate lifts are \(x_h+t5^h\) for \(t=0,1,2,3,4\). The quotient congruence above implies

\[
F(x_h+t5^h)\equiv F(x_h)+t5^hF'(a)\pmod{5^{h+1}},
\]

so exactly one lift matches any prescribed target residue at the next level. The compatible lifts converge in \(\mathbb Z_5\). Hence for each \(k\ge1\), every target \(u\pmod{5^k}\) has exactly one solution \(x\pmod{5^k}\) inside each disk with \(F(a)\equiv u\pmod5\), and no other solutions.

**4. Complete residue frequencies.** The five entries in the value row show that the numbers of solutions of \(F(x)\equiv r\pmod{5^k}\), according to \(r\bmod5\), are

\[
(m_0,m_1,m_2,m_3,m_4)=(1,2,0,1,1).
\]

Because \(5^k\) is odd, in any consecutive block of \(2\cdot5^k\) indices each class \(x\pmod{5^k}\) appears exactly once at an even index and exactly once at an odd index. By \(D_n=(-1)^nF(n)\), the frequencies of \(D_n\equiv r\) are therefore \(m_r+m_{-r}\), or exactly \((2,3,1,1,3)\). In addition, \(F(n+5^k)\equiv F(n)\pmod{5^k}\) and the parity repeats after \(2\cdot5^k\), so this is a full period and the asserted densities follow.

For clarity, the least period is indeed \(2\cdot5^k\): any period of odd length would translate the even-branch image \(\{0,1,3,4\}\subset\mathbb F_5\) onto the odd-branch image \(\{0,1,2,4\}\), which is impossible. If an even period \(T\) were not divisible by five, invariance under translation by \(T\pmod5\) would force \(F\pmod5\) to be constant, contrary to the table. Finally, if \(5\mid T\) but \(5^k\nmid T\), the exact local isometry gives \(F(n+T)\not\equiv F(n)\pmod{5^k}\). The least-period fact is previously known, and only independently rederived here.

**5. Minimal prime.** Modulo four, the derangement recurrence has period four and image \(\{0,1,2\}\), so a residue is missed. Modulo nine, its period is eighteen and the image is \(\{0,1,2,4,5,7,8\}\), missing \(3,6\). These are the only primes less than five, and the five-adic census supplies full coverage at every power of five.

## Verification

The standalone script `verify.py` independently computes the derivative table by integer polynomial arithmetic, enumerates every value of the derangement recurrence modulo \(5^k\) for \(1\le k\le6\) over complete periods, confirms the five-entry frequency pattern at every residue, checks the minimal periods, and verifies the modular-four and modular-nine omissions. Run with `python3 verify.py` using only the standard library. The six tested exponents include \(5^6=15625\) target residues and \(31250\) indices in the last complete period. The script tests finite cases; Steps 1–5 prove the universal claim.

## Relationship to prior work

Sun and Zagier (2010), arXiv:1008.1573, gave prime-modulus Bell/derangement congruences, not the present complete census for every power of five. Sun, Wu and Zhuang (2010), arXiv:1009.2929, generalized polynomial congruences. Miska (2015), arXiv:1508.01987, established the exact general modular period and developed Hensel methods for related derangement divisibility and valuation questions; neither the basic period nor general Hensel lifting is claimed as new here. O'Desky and Richman (2020), arXiv:2012.04615, developed five-adic-compatible interpolation and continuity methods in a broader setting. The contribution assessed here is specifically the nonvanishing derivative table at all five disks, complete all-level residue multiplicity formula, and resulting universal five-adic coverage, which were not identified as statements of the inspected works.

## Limitations

No independent audit has been performed. The theorem does not describe frequency distributions for arbitrary primes or moduli containing multiple prime factors, nor the distribution of derangement integers by size (the densities count **indices**). Historical priority remains subject to specialist literature not located in this comparison. Finite computational checks cannot establish an infinite congruence statement independently of the proof.

## References

- Zhi-Wei Sun and Don Zagier, *On a curious property of Bell numbers*, first arXiv submission 2010-08-09, https://arxiv.org/abs/1008.1573.
- Yidong Sun, Xiaojuan Wu, and Jujuan Zhuang, *Congruences on the Bell polynomials and the derangement polynomials*, first arXiv submission 2010-09-15, https://arxiv.org/abs/1009.2929.
- Piotr Miska, *Arithmetic Properties of the Sequence of Derangements and its Generalizations*, first arXiv submission 2015-08-09, https://arxiv.org/abs/1508.01987.
- Andrew O'Desky and David Harry Richman, *Derangements and the \(p\)-adic incomplete gamma function*, first arXiv submission 2020-12-08, https://arxiv.org/abs/2012.04615.
