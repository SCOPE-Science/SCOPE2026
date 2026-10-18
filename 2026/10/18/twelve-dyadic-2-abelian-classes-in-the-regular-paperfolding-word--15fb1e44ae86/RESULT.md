# Twelve dyadic \(2\)-abelian classes in the regular paperfolding word

## Finding
Let \(p=p_1p_2\cdots\) be the binary regular paperfolding word specified by
\(p_i=1\) if the odd part of \(i\) is \(1\pmod 4\), and \(p_i=0\) if it is \(3\pmod4\). Let \(\mathcal F_N(p)\) be the set of contiguous factors of length \(N\). Two words are \(2\)-abelian equivalent when every binary factor of length one or two occurs the same number of times in both.

**Theorem.** For every integer \(k\ge3\) and \(N=2^k\), the quotient of \(\mathcal F_N(p)\) under \(2\)-abelian equivalence contains **exactly twelve classes**. More precisely, each possible number of ones
\[
\frac N2-1,\qquad\frac N2,\qquad\frac N2+1
\]
occurs with all four prescribed first/last-symbol pairs \((0,0),(0,1),(1,0),(1,1)\), and these twelve triples distinguish the \(2\)-abelian classes.

## Assumptions and scope
Indices of \(p\) and starting positions of factors begin at one. The odd part of a positive integer is obtained by removing all factors of two. Factors are contiguous in the one-sided infinite word; arbitrary starting positions are allowed. The statement concerns precisely lengths \(N=2^k\) with \(k\ge3\). The complementary convention for the paperfolding word gives the same class count by alphabet exchange.

## Proof
**1. Count of ones.** Write \(S_m(t)=\sum_{i=t}^{t+m-1}p_i\). By the defining odd-part rule,
\[
p_{2j}=p_j,\quad p_{4j+1}=1,\quad p_{4j+3}=0\qquad(j\ge0\text{ whenever the indices are positive}).
\]
In a window of length \(m\) divisible by four, exactly \(m/2\) indices are odd and exactly half of these odd indices carry ones. The even indices correspond to a consecutive window of length \(m/2\). Hence
\[
S_m(t)=\frac m4+S_{m/2}\bigl(\lceil t/2\rceil\bigr).
\]
Repeatedly applying the identity for \(m=N,N/2,\ldots,4\) yields, with \(J=\lceil t/(N/2)\rceil\),
\[
S_N(t)=\frac N2-1+p_J+p_{J+1}.
\]
Thus \(S_N(t)\) has at most the three values in the theorem.

**2. Adjacent-pair counts are forced by the ones count and endpoints.** Put \(e_i=1\) if \(p_i\ne p_{i+1}\), and \(e_i=0\) otherwise. Every two odd-indexed letters at distance two are complementary: \(p_{2j+1}\ne p_{2j+3}\). Consequently
\[
e_{2j+1}+e_{2j+2}=1\qquad(j\ge0).
\]
The \(N-1\) consecutive adjacency edges of any length-\(N\) factor split into \((N-2)/2\) of these complementary pairs and one additional edge. Their total number \(T\) of transitions therefore belongs to \(\{N/2-1,N/2\}\). Its parity is the difference of the factor's endpoints. Since \(N/2\) is even, necessarily
\[
T=\begin{cases}N/2,&\text{equal endpoints},\\N/2-1,&\text{unequal endpoints}.\end{cases}
\]
For a factor with \(K\) ones, first symbol \(a\), last symbol \(b\), and pair counts \(c_{xy}\), the identities
\[
c_{01}+c_{10}=T,\quad c_{01}-c_{10}=b-a,\quad 2c_{11}+T=2K-a-b,\quad \sum_{x,y}c_{xy}=N-1
\]
uniquely determine all four pair counts. Thus the triple \((K,a,b)\) determines the \(2\)-abelian class. Conversely, the counts of one-letter and two-letter factors recover this triple: the equations above recover \(a+b\) and \(b-a\), hence each endpoint. Therefore distinct triples give distinct classes, and the upper bound is twelve.

**3. All twelve classes occur.** For \(k\ge4\) put \(H=N/2\). Choose any one of the three odd integers \(J=1,3,11\), for which the adjacent bits are respectively \((p_J,p_{J+1})=(1,1),(0,1),(0,0)\). For each such \(J\), consider the four factors starting at
\[
t=(J-1)H+d,\qquad d\in\{2,3,4,7\}.
\]
All four starts satisfy \(\lceil t/H\rceil=J\), so step 1 supplies respectively \(K=N/2+1,N/2,N/2-1\) for the three choices of \(J\). The odd-part rule (using that \((J-1)H\) is a multiple of sixteen) gives the endpoint pairs \((1,1),(0,1),(1,0),(0,0)\), in the order \(d=2,3,4,7\). This produces all twelve triples.

For \(k=3\), so \(N=8\), explicit starts complete the remaining base case. Listed by \((K-N/2,a,b)\), the starts are:

| \(K-N/2\) | \((0,0)\) | \((0,1)\) | \((1,0)\) | \((1,1)\) |
|---|---:|---:|---:|---:|
| \(-1\) | 23 | 22 | 21 | 42 |
| \(0\) | 7 | 6 | 5 | 9 |
| \(+1\) | 15 | 3 | 4 | 1 |

Direct evaluation of \(p_i\) from its odd part verifies the twelve entries. This proves the theorem for every \(k\ge3\). \(\square\)

## Verification
Run `python3 verify.py` from the same directory as this document. The program reconstructs letters from the odd-part definition, verifies every one-count and transition identity over a growing finite set of starts for each \(N=2^k\), \(3\le k\le12\), compares the direct two-factor profiles at shorter lengths, and checks the universal witnesses and twelve base-case starts. It prints `VERIFY_OK`. Computations are consistency checks, not substitutes for the universal proof.

## Relationship to prior work
Madill and Rampersad (arXiv:1208.2856, first public 2012-08-14) determine the ordinary *one*-abelian complexity of the paperfolding word; their recurrence gives three classes at dyadic lengths. This theorem refines each of those three classes into exactly four \(2\)-abelian classes. Parreau, Rigo, Rowland, and Vandomme (arXiv:1405.3532) study \(2\)-abelian complexity of the different Thue–Morse and period-doubling words. Greinecker (arXiv:1404.3906) treats Thue–Morse \(2\)-abelian complexity. The checked results do not imply the present precise paperfolding statement.

## Limitations
Only dyadic lengths at least eight and the specified ordinary paperfolding word are covered. No exact formula for nondyadic lengths, no regularity theorem for the full \(2\)-abelian complexity function, and no statement for all generalized paperfolding words is established. Earlier equivalent formulations outside inspected literature remain possible. Independent audit has not been performed.

## References
1. B. Madill and N. Rampersad, *The abelian complexity of the paperfolding word*, arXiv:1208.2856 (2012), later *Discrete Mathematics* **313** (2013), 831–838. https://arxiv.org/abs/1208.2856
2. A. Parreau, M. Rigo, E. Rowland, and É. Vandomme, *A new approach to the 2-regularity of the \(\ell\)-abelian complexity of 2-automatic sequences*, arXiv:1405.3532 (2014), *Electronic Journal of Combinatorics* **22** (2015), P1.27. https://arxiv.org/abs/1405.3532
3. F. Greinecker, *On the 2-Abelian Complexity of the Thue–Morse Word*, arXiv:1404.3906 (2014), *Theoretical Computer Science* **593** (2015). https://arxiv.org/abs/1404.3906
