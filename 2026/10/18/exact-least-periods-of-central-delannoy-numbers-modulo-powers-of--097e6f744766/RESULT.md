# Exact least periods of central Delannoy numbers modulo powers of two

## Finding
Let \(D_n\) be the central Delannoy number
\[
D_n=\sum_{k=0}^{n}2^k\binom{n}{k}^{2},\qquad n\ge0.
\]
For each integer \(r\ge1\), let \(P(r)\) be the least positive \(h\) such that \(D_{n+h}\equiv D_n\pmod{2^r}\) holds for **every** integer \(n\ge0\). Then
\[
P(r)=\begin{cases}
1,&r=1,\\
2,&r=2,\\
4,&r=3\text{ or }r=4,\\
2^{r-2},&r\ge5.
\end{cases}
\]
In particular the least period doubles with each increase in the modulus exponent from \(r=5\) onward, after a two-level plateau at \(r=3,4\).

## Assumptions and scope
The binomial coefficient \(\binom{m}{k}\) means the ordinary integer binomial coefficient for integers \(m\ge0\) and \(k\ge0\), set to zero for \(k>m\). The valuation \(\nu_2(a)\) is the exponent of two in a nonzero integer \(a\). All indices are nonnegative integers. Pure periodicity from index zero is claimed, not eventual periodicity; only moduli \(2^r\) are considered. The classical alternative expression \(\sum_k\binom nk\binom{n+k}k\) gives the same central Delannoy numbers.

## Proof
**Uniform shift lemma.** For every integer \(s\ge2\) and every \(n\ge0\),
\[
D_{n+2^s}\equiv D_n\pmod{2^{s+2}}. \tag{1}
\]
Indeed set \(h=2^s\), \(a_k=\binom nk\), \(b_k=\binom{n+h}k\), and \(\delta_k=b_k-a_k\). By Vandermonde's identity,
\[
\delta_k=\sum_{j=1}^{\min(k,h)}\binom hj\binom n{k-j}.
\]
For \(1\le j\le h\),
\[
\nu_2\!\left(\binom{2^s}{j}\right)=s-\nu_2(j). \tag{2}
\]
To see (2), write \(\binom{2^s}j=(2^s/j)\binom{2^s-1}{j-1}\); the final binomial is odd because the binary digits of \(2^s-1\) are all one (equivalently, reduce \((1+X)^{2^s-1}\) modulo two). Consequently for \(1\le k\le s+1\),
\[
\nu_2(\delta_k)\ge s-\lfloor\log_2 k\rfloor,
\]
where a zero \(\delta_k\) can simply be treated as infinitely divisible. The difference of the \(k\)-th terms is
\[
2^k(b_k^2-a_k^2)=2^{k+1}a_k\delta_k+2^k\delta_k^2.
\]
Its first summand has valuation at least \(s+k+1-\lfloor\log_2 k\rfloor\ge s+2\). Its second has valuation at least \(2s+k-2\lfloor\log_2 k\rfloor\ge2s\ge s+2\). The elementary inequalities used here are \(k\ge\lfloor\log_2 k\rfloor+1\) and \(k\ge2\lfloor\log_2 k\rfloor\) for integers \(k\ge1\). For \(k\ge s+2\), the factor \(2^k\) itself gives the needed divisibility. Summing over all \(k\) proves (1).

**Lower bounds and boundary moduli.** Formula (1) with \(s=r-2\) gives \(P(r)\le2^{r-2}\) for \(r\ge4\), and implies period at most four for \(r=3\). The first values are \(D_0=1\), \(D_1=3\), \(D_2=13\), \(D_3=63\), \(D_5=1683\). All \(D_n\) are odd, giving \(P(1)=1\). Modulo four, the defining sum gives \(D_n\equiv1+2n^2\equiv1+2n\pmod4\), so \(P(2)=2\). For \(r=3\) and \(r=4\), a shift by two fails at \(n=0\), since \(D_2-D_0=12\), not divisible by eight or sixteen. Thus both least periods equal four.

It remains to exclude the half-period for \(r\ge5\). Write \(r=t+3\), with \(t\ge2\), and put \(h=2^t\). The candidate half-period is \(h\), while (1) gives the period \(2h\) modulo \(2^{t+3}\). For \(t=2\), the explicit difference \(D_5-D_1=1680\) has valuation four, so shift four fails modulo \(32\). For \(t\ge3\), use \(n=1\). The \(k=1\) term of \(D_{h+1}-D_1\) is
\[
2\bigl((h+1)^2-1\bigr)=2^{t+2}(1+2^{t-1}), \tag{3}
\]
which has valuation exactly \(t+2\). For every \(2\le k\le h+1\), the binomial coefficient identity
\[
\binom{h+1}{k}=\frac{h(h+1)}{k(k-1)}\binom{h-1}{k-2}
\]
shows that \(\nu_2\!\left(\binom{h+1}{k}\right)=t-\nu_2(k(k-1))\), since the last binomial and \(h+1\) are odd. Thus the corresponding \(k\)-th term \(2^k\binom{h+1}{k}^2\) has valuation
\[
k+2t-2\nu_2(k(k-1))\ge2t\ge t+3. \tag{4}
\]
The first inequality follows because the even member of \(k,k-1\) is at most \(k\), and \(2\lfloor\log_2k\rfloor\le k\) for every \(k\ge2\). Hence (3) alone determines the residue modulo \(2^{t+3}\):
\[
\nu_2(D_{2^t+1}-D_1)=t+2\quad(t\ge3). \tag{5}
\]
So the half-period always fails.

Finally, if a sequence is purely periodic with period a power of two \(H\), its least positive period divides \(H\): apply the division algorithm to any two periods, and use the difference-of-periods property on indices \(n\ge0\). Therefore a proper least period would divide \(H/2\). The exhibited failure of \(H/2\) proves that \(H\) is least. Combining the cases yields the claimed formula for every \(r\ge1\). \(\square\)

## Verification
The included standard-library program `verify.py` recomputes all relevant congruences for \(1\le r\le12\), performs explicit half-period witness tests, checks the binomial valuations used in (2) and (4), and reports `VERIFY_OK` upon success. This finite replay tests the proof but does not replace the infinite-index arguments above.

## Relationship to prior work
Sun's work on generalized central trinomial coefficients identifies \(D_n=T_n(3,2)\) and develops arithmetic congruences, but does not state the least-index-period classification here. Lengyel investigates \(2\)-adic differences and limits of Delannoy numbers, including specific prime-power-index families and conjectured exact valuations; those results concern related but not identical quantifiers. The present theorem requires a shift congruence valid **uniformly in every initial index** and a matching obstruction to every potential smaller period. Rowland–Yassawi establish general finite-automaton methods for algebraic sequences modulo prime powers; existence of an automaton alone does not imply or identify a pure exact period. Petersen's Delannoy adic dynamical system concerns path-space dynamics, not termwise residues of the central sequence. The literature comparison was bounded; an earlier equivalent statement outside the inspected sources remains possible.

## Limitations
No period claim is made for odd prime powers or arbitrary composite moduli; no exact valuation formula for arbitrary shifts is claimed, and no conjectures in Lengyel's paper are asserted resolved. Search and inspection cannot prove the nonexistence of equivalent published formulas. A finite checker is supporting evidence, not an independent mathematical audit.

## References
1. Zhi-Wei Sun, *Congruences involving generalized central trinomial coefficients*, arXiv:1008.3887 (initial public version 2010-08-23), especially the Delannoy identity in the introduction, https://arxiv.org/abs/1008.3887.
2. Tamás Lengyel, *On some \(p\)-adic properties and supercongruences of Delannoy and Schröder numbers*, INTEGERS 21 (2021), article A86, https://math.colgate.edu/~integers/v86/v86.pdf.
3. Eric Rowland and Reem Yassawi, *Automatic congruences for diagonals of rational functions*, arXiv:1310.8635, https://arxiv.org/abs/1310.8635.
4. Karl Petersen, *An adic dynamical system related to the Delannoy numbers*, arXiv:1105.5505, https://arxiv.org/abs/1105.5505.
