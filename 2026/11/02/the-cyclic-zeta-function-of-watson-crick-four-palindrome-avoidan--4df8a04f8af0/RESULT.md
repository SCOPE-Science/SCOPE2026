# The cyclic zeta function of Watson–Crick four-palindrome avoidance

## Finding

Let \(\Sigma=\{A,T,C,G\}\), with Watson–Crick complementation \(\bar A=T\), \(\bar T=A\), \(\bar C=G\), and \(\bar G=C\). A circular word of length \(n\geq1\) is **admissible** when none of its \(n\) cyclic consecutive four-letter windows belongs to
\[
\mathcal P=\{ab\bar b\bar a:a,b\in\Sigma\}.
\]
There are exactly sixteen forbidden windows. The position indices of every window are read modulo \(n\), including when \(n<4\). Write \(C_n\) for the number of admissible **indexed** words of length \(n\): words whose position zero is distinguished, with the four letters labeled.

**Theorem.** The dynamical zeta function of this cyclic avoidance language is
\[
\boxed{\displaystyle
\exp\!\left(\sum_{n\ge1}\frac{C_n}{n}z^n\right)=
\frac{1}{(1-z^2)^3(1+z^2)^2D_3(z)D_-(z)^2D_+(z)}}
\]
with the explicitly evaluated factors
\[
\begin{aligned}
D_3(z)&=1-3z-2z^2-3z^3,\\
D_-(z)&=1-z+z^2-4z^3+2z^4-3z^5,\\
D_+(z)&=1+z+z^2+4z^3+2z^4+3z^5.
\end{aligned}
\]
This equality holds as a formal power series over \(\mathbb Q\), not merely through a finite degree. In particular,
\[
(C_1,C_2,\ldots,C_{12})=
(4,12,64,228,744,2904,10420,39012,145900,546792,2046532,7670472).
\]
The number \(N_n\) of **primitive oriented rotation necklaces** (primitive circular words modulo rotation, but not reversal, complementation, or alphabet permutation) is therefore exactly
\[
\boxed{\displaystyle N_n=\frac1n\sum_{d\mid n}\mu(d)C_{n/d}.}
\]
For example, \((N_1,\ldots,N_6)=(4,4,20,54,148,472)\).

The corresponding constraint-system capacity is
\[
\lim_{n\to\infty}\frac{\log_2 C_n}{n}=
\log_2\lambda\simeq1.90586939877\text{ bits per base},
\]
where \(\lambda\simeq3.74734654030721\) is the unique positive root in \((3,4)\) of \(\lambda^3-3\lambda^2-2\lambda-3=0\). This is the capacity for **local consecutive length-four palindrome avoidance**, not for global secondary-structure avoidance.

## Assumptions and scope

Only four fixed, labeled bases and the fixed-point-free Watson–Crick complement involution are used. Circular words are oriented, and a length-four window may wrap around the boundary more than once for short periods. No constraints involving distant pairs of complementary length-two factors are imposed. All enumeration and asymptotic assertions cover every integer \(n\ge1\).

## Proof

**1. Finite-state bijection.** Use the \(64\) ordered triples \((a,b,c)\in\Sigma^3\) as states. Form a directed transition
\[
(a,b,c)\longrightarrow(b,c,d)
\]
for each \(d\in\Sigma\), except when \(a=\bar d\) and \(b=\bar c\). These are precisely the transitions that would complete a forbidden factor \(ab\bar b\bar a\). Let \(M\) be the corresponding \(64\times64\) integer adjacency matrix. Reading an indexed \(n\)-periodic sequence around the overlap graph gives one rooted closed walk of length \(n\), and conversely every such closed walk uniquely determines the indexed periodic word. This bijection remains valid when \(n=1,2,3\), because the overlap identities enforce the necessary repeated letters. Hence
\[
C_n=\operatorname{tr}(M^n)\qquad(n\ge1).
\]

**2. Exact determinant evaluation.** The characteristic polynomial, evaluated without floating-point arithmetic, is
\[
\begin{aligned}
\det(xI-M)={}&x^{36}(x-1)^3(x+1)^3(x^2+1)^2\\
&\cdot(x^3-3x^2-2x-3)\\
&\cdot(x^5-x^4+x^3-4x^2+2x-3)^2\\
&\cdot(x^5+x^4+x^3+4x^2+2x+3).
\end{aligned}
\]
For a completely reproducible exact-integer certificate for this nontrivial finite identity, `verify.py` constructs the transition graph explicitly, computes each integer trace through length \(64\) by a closed-walk recurrence, and applies the Newton determinant identities. If \(d_k=[z^k]\det(I-zM)\) and \(d_0=1\), these identities are
\[
kd_k=-\sum_{j=1}^{k}\operatorname{tr}(M^j)d_{k-j},
\qquad 1\le k\le64.
\]
The code performs these integer sums and checks all \(65\) coefficients, including the zero coefficients above degree \(28\), against the displayed product. Thus its verification is a complete finite **symbolic polynomial equality** for the specified matrix, not an inference from a few terms of a sequence. The stated characteristic polynomial and all the factors in the theorem are equivalent by substituting \(z=1/x\) and multiplying by \(z^{64}\).

**3. Generating function and primitive orbits.** The formal matrix identity
\[
-\log\det(I-zM)=\sum_{n\ge1}\frac{\operatorname{tr}(M^n)}n z^n
\]
proves the asserted zeta formula for every degree. Each primitive orbit of length \(d\) contributes exactly \(d\) indexed points to \(C_n\) whenever \(d\mid n\). Consequently \(C_n=\sum_{d\mid n}dN_d\), and Möbius inversion gives the necklace formula.

**4. Capacity.** The graph is strongly connected, as checked by a complete forward and reverse reachability search on the explicitly defined finite graph, and has a self-loop at the state \((A,A,A)\). Its nonnegative adjacency matrix is therefore primitive. Row sums are either \(3\) or \(4\), so its Perron root is in \([3,4]\). From the characteristic polynomial, the only positive real eigenvalue in that interval is the unique root of \(x^3-3x^2-2x-3\), because the other real nontrivial factors are strictly positive for \(x\ge3\). Perron–Frobenius theory now yields the stated exponential growth and capacity. The root and logarithm are numerical approximations of explicitly defined algebraic constants.

## Verification

The standalone standard-library Python program `verify.py` contains every matrix construction, integer recurrence, and polynomial needed above. Execute it with `python3 verify.py`; a successful run terminates with `VERIFY_OK`. It compares the full \(64\)-coefficient exact determinant computation against the factorization, verifies strong connectivity, and independently enumerates every indexed quaternary word of length at most \(8\) for cyclic counts. It additionally checks an auxiliary linear-word recurrence for alphabet sizes \(2,4,6,8\) through length \(16\). Those short enumerations are cross-checks; the all-length proof rests on the exact characteristic-polynomial identity, closed-walk bijection, and formal matrix logarithm.

## Relationship to prior work

Lamprea-Burgunder, Ludin, and Mäser (2011) identify the sixteen reverse-complement palindromic four-mers and study their empirical frequencies across genomes; they do not provide the circular avoidance zeta function. Chu, Wang, and Zhang (first public April 22, 2023) study **stronger** secondary-structure avoidance: they forbid reverse-complementary pairs of length-two factors at arbitrary nonoverlapping positions, rather than only adjacent pairs forming a four-mer, and therefore obtain a different capacity. A 2023 MathOverflow discussion describes the standard de Bruijn transfer-matrix route and the alternate-position complement bijection from *linear binary* reverse-complement palindrome avoidance to ordinary-palindrome avoidance. Those general methods and their linear specialization are acknowledged; the contribution here is the evaluated quaternary **cyclic** spectrum and resulting exact zeta/necklace formulas. Alternating complementation of letters in odd-periodic words changes the wraparound boundary condition, so linear statements cannot be transferred indiscriminately to all cyclic periods. Simpson (2014) studies a different extremal question concerning the number of palindromes in circular words.

## Limitations

This is exact for the specified local motif-avoidance language only. It makes no claim to exclude all biological hairpins, stem loops, or spatially separated reverse-complement pairs. The simple finite-state and determinant methodology is classical; the claimed mathematical distinction is the explicit evaluated all-length quaternary circular factorization, not invention of transfer matrices or the staggered binary equivalence. The possibility of a previously published but unindexed equivalent evaluation remains unresolved. The result has received only self-review; no independent audit is claimed.

## References

1. H. Chu, C. Wang, Y. Zhang, *Improved constructions of secondary structure avoidance codes for DNA sequences*, arXiv:2304.11403 (first public April 22, 2023), https://arxiv.org/abs/2304.11403 .
2. E. Lamprea-Burgunder, P. Ludin, P. Mäser, *Species-specific Typing of DNA Based on Palindrome Frequency Patterns*, DNA Research 18 (2011), 117–124, https://doi.org/10.1093/dnares/dsr004 .
3. *Number of Binary String*, MathOverflow discussion and answer, April 14–15, 2023, https://mathoverflow.net/questions/444770/number-of-binary-string .
4. J. Simpson, *Palindromes in circular words*, Theoretical Computer Science 550 (2014), 66–78, https://doi.org/10.1016/j.tcs.2014.07.012 .
