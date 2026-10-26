# Exact \(2\)-adic residue densities for semi-Narayana partition numbers

## Finding
Let \(c(n)\) count partitions of \(n\) into powers of two, each power occurring zero, once, or three times. For \(n\geq 1\), put \(v(n)=(c(n),c(n-1),c(n-2))\), with \(c(-1)=0\). For each \(r\geq1\), let \(q=2^r\). The natural density of positive integers \(n\) satisfying \(v(n)\equiv(a,b,d)\pmod q\) exists and equals
\[
\begin{cases}
\displaystyle\frac{1}{q^3-(q/2)^3},&\text{if at least one of }a,b,d\text{ is odd},\\
0,&\text{if all three are even}.
\end{cases}
\]
In particular, the density of \(c(n)\equiv a\pmod q\) is \(8/(7q)\) for odd \(a\), and \(6/(7q)\) for even \(a\). Equivalently, \(\nu_2(c(n))=0\) has natural density \(4/7\), and \(\nu_2(c(n))=j\) has natural density \(3/(7\cdot2^j)\) for each fixed integer \(j\geq1\).

## Assumptions and scope
The coefficients are defined by the formal series
\[
\sum_{n\geq0}c(n)x^n=\prod_{j\geq0}(1+x^{2^j}+x^{3\cdot2^j}).
\]
Set \(c(-1)=0\) only for the indicated boundary state, and use the standard recurrence \(c(0)=c(1)=1\), \(c(2m)=c(m)\), \(c(2m+1)=c(m)+c(m-1)\) for \(m\geq1\). A natural density means \(\lim_{X\to\infty}X^{-1}\#\{1\leq n\leq X:\text{the asserted congruence holds}\}\). The theorem quantifies over all \(r\geq1\) and all residue triples modulo \(2^r\).

## Proof
**1. Binary matrices.** The recurrence gives \(v(2n)=Av(n)\) and \(v(2n+1)=Bv(n)\) for \(n\geq1\), where
\[
A=\begin{pmatrix}1&0&0\\0&1&1\\0&1&0\end{pmatrix},\qquad
B=\begin{pmatrix}1&1&0\\1&0&0\\0&1&1\end{pmatrix},\qquad
v(1)=\begin{pmatrix}1\\1\\0\end{pmatrix}.
\]
Both matrices have determinant \(-1\). They therefore act as permutations on triples modulo every \(2^r\). The root state is primitive (at least one coordinate odd), and that property is invariant under both maps. Thus nonprimitive triples cannot occur.

**2. Every primitive state is attainable.** Modulo two, the orbit of \((1,1,0)\) under \(A,B\) is precisely the seven nonzero triples; this is verified directly by the matrices. Write \(I\) for the identity and put
\[
E=\begin{pmatrix}0&0&0\\0&1&1\\0&1&0\end{pmatrix},\qquad
D=\begin{pmatrix}0&0&0\\0&1&0\\0&0&1\end{pmatrix}.
\]
Direct multiplication gives \(A^3\equiv I+2E\pmod4\) and \(A^6\equiv I+4D\pmod8\). Successively squaring the second identity proves, for every \(r\geq2\),
\[
A^{3\cdot2^{r-1}}\equiv I+2^rD\pmod{2^{r+1}}.
\]
Write \(L_1=A^3\) and \(L_r=A^{3\cdot2^{r-1}}\) for \(r\geq2\), and \(T_1=E\), \(T_r=D\) for \(r\geq2\). Each \(L_r\) acts trivially modulo \(2^r\), and on a lift of parity state \(u\in\mathbb F_2^3\) it adds \(2^rT_ru\) modulo \(2^{r+1}\).

A conjugate \(WL_rW^{-1}\) adds \(2^r(WT_rW^{-1})u\) modulo \(2^{r+1}\). Here \(W\) is any word in \(A,B\), evaluated modulo two when forming its effect. All inverses can be expressed by positive powers modulo \(2^{r+1}\) because \(A,B\) are finite-order permutations there. The following table gives, for each nonzero \(u\), three word choices whose displacement vectors \((WT_1W^{-1})u\) form a basis of \(\mathbb F_2^3\), followed by three choices for \(T_r=D\). The empty word is \(I\), and the letters \(0,1\) mean respectively \(A,B\) in left-to-right matrix products.

| Parity state \(u\) | Three words for \(E\) | Three words for \(D\) |
|---|---|---|
| 001 | \(I,B,BAB\) | \(I,AB,A^2B\) |
| 010 | \(I,B,AB\) | \(I,B,B^2\) |
| 011 | \(I,B,BAB\) | \(I,B,AB^2\) |
| 100 | \(B,BAB,AB\) | \(B,B^2,AB^2\) |
| 101 | \(I,B,BAB\) | \(I,B,B^2\) |
| 110 | \(I,BAB,AB\) | \(I,B^2,AB^2\) |
| 111 | \(I,B,BAB\) | \(I,B,B^2\) |

The fourteen determinant calculations over \(\mathbb F_2\) all equal one. They can be checked by multiplying the displayed matrices; the accompanying self-contained verifier checks all of them. Hence, for any given primitive state at modulus \(2^r\), products of three conjugates reach all eight possible lifts modulo \(2^{r+1}\) without changing the reduction modulo \(2^r\). Since the base orbit at modulus two contains all nonzero triples, induction proves that the orbit modulo \(2^r\) contains **every primitive triple** for all \(r\geq1\). Each state in this orbit occurs as \(v(n)\) for some positive \(n\), because finite inverse matrices can be represented by positive words.

**3. Uniform limiting distribution for all natural cutoffs.** Fix \(r\). Read an integer's binary expansion from its leading \(1\); its trailing bits apply independently chosen maps \(A,B\). This is a finite Markov chain on the primitive triples modulo \(2^r\). The preceding orbit result makes the chain irreducible. It is aperiodic, since the primitive state \((1,0,0)\) is fixed by \(A\). Both transition maps are permutations, so the transition matrix is doubly stochastic. Thus the unique stationary law is uniform on the \(q^3-(q/2)^3\) primitive triples, and convergence to it holds from *every* starting state.

For clarity, convergence on blocks \([2^k,2^{k+1})\) alone is not being substituted for natural density. Given \(\varepsilon>0\), choose a fixed suffix length \(t\) such that applying \(t\) random bits sends any initial primitive state to within \(\varepsilon\) of the uniform law. Decompose the integers up to an arbitrary cutoff \(X\) into maximal aligned binary-prefix cylinders. All cylinders having at least \(t\) free suffix bits have their state distribution within \(\varepsilon\) of uniform. The remaining cylinders contain at most \(O(2^t\log X)\) integers (in fact a sharper bound is possible), which is \(o(X)\). Their contribution therefore vanishes after division by \(X\). Letting first \(X\to\infty\) and then \(\varepsilon\to0\) proves uniform *natural* density over the primitive triples.

**4. Marginals and valuations.** There are \(q^3-(q/2)^3=7q^3/8\) primitive triples. If the first coordinate \(a\) is odd, there are \(q^2\) such triples with that coordinate. If it is even, there are \(q^2-(q/2)^2=3q^2/4\). Dividing yields respectively \(8/(7q)\) and \(6/(7q)\). The \(j=0\) valuation density is the sum over odd residues mod two, namely \(4/7\). For each fixed \(j\geq1\), exactly one residue class modulo \(2^{j+1}\) has valuation \(j\), namely \(2^j\pmod{2^{j+1}}\). Its density is \(6/(7\cdot2^{j+1})=3/(7\cdot2^j)\). This completes the proof.

## Verification
Run `python3 verify_semi_narayana.py` using Python 3 and no additional packages. The script checks the matrix-lifting identities at eleven increasing powers of two, the seven-state base orbit, all fourteen explicit determinant-one conjugation witnesses, exact primitive-state reachability modulo \(2,4,8,16,32\), and independent generation-function and recurrence coefficients through index \(8191\). Finite reachability computations are diagnostics; the unbounded assertion follows from the displayed induction and standard finite Markov-chain convergence.

## Relationship to prior work
Ballantine and Beck [1, §7, especially Theorem 7.3] identify these coefficients as semi-Narayana cows numbers and show they are even precisely for integers congruent to \(3,5,6\pmod7\). Our mod-two marginal agrees with that known \(3/7\) even density, but the uniform **triple distribution modulo each power of two** and the exact higher-valuation densities are additional conclusions. Anders [2] studies nonstandard binary representation counts and summed growth, not these local residue laws. The OEIS entry [3] gives the generating function and elementary identities, not the asserted residue distributions. Sobolewski [4] studies a different, unrestricted binary partition generating function.

## Limitations
This establishes asymptotic densities for fixed moduli \(2^r\), without an explicit error term uniform as \(r\to\infty\), and without claims about other primes or the joint distribution of separated nonconsecutive coefficients. Prior general matrix-product theory may imply some ingredients; an earlier unindexed or implicit form of the full theorem cannot be excluded. Independent mathematical audit and priority verification have not been performed.

## References
[1] C. Ballantine and G. Beck, *Partitions enumerated by self-similar sequences*, arXiv:2303.11493v1 (first posted 20 March 2023), §7, Theorem 7.3. https://arxiv.org/abs/2303.11493

[2] K. Anders, *Counting Non-Standard Binary Representations*, Journal of Integer Sequences **19** (2016), Article 16.3.3.

[3] OEIS A120562, *Semi-Narayana cows sequence*. https://oeis.org/A120562

[4] B. Sobolewski, *Values of Binary Partition Function Represented by a Sum of Three Squares* (2023), concerning unrestricted binary partitions.
