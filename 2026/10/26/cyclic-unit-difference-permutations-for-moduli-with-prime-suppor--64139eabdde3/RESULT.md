# Cyclic unit-difference permutations for moduli with prime support \(\{3,p\}\)

## Finding

Let \(p\ge5\) be a prime, and let \(a,b\ge1\) be integers. Put \(n=3^a p^b\) and let \(U(n)=(\mathbb Z/n\mathbb Z)^\times\). There is a circular ordering \((x_0,\ldots,x_{\varphi(n)-1})\) of every member of \(U(n)\), exactly once, such that
\[
\{x_i-x_{i+1}\pmod n:0\le i<\varphi(n)\}=U(n),
\]
where the final subscript is interpreted cyclically. Thus both the vertices and the ordered cyclic adjacent differences are reduced residue systems modulo \(n\).

The proof supplies a constructive prime-power lifting lemma: whenever an odd integer \(m>1\) admits such an ordering and an odd prime \(q\mid m\), the modulus \(mq\) also admits such an ordering.

## Assumptions and scope

All congruences are of ordinary integers. The group \(U(n)\) consists of the residues relatively prime to \(n\). A circular ordering is a list of length \(\varphi(n)\) whose last entry is adjacent to its first; the oriented edge from \(x_i\) to \(x_{i+1}\) is labelled \(x_i-x_{i+1}\pmod n\), not its absolute value. The claim is for precisely two distinct prime divisors, one of which is \(3\). No condition is imposed on the positive exponents.

## Proof

**Step 1: a base cycle modulo \(3p\).** Fix a primitive root \(g\) modulo the prime \(p\). Since \(p\ge5\), choose \(c\in\mathbb F_p^\times\setminus\{1,g\}\). Let \([r,s]_{3,p}\) denote the unique integer residue modulo \(3p\) that is \(r\) modulo \(3\) and \(s\) modulo \(p\). For each \(0\le t<p-1\), define
\[
 A_t=[1,g^t]_{3,p},\qquad B_t=[2,cg^t]_{3,p}.
\]
Take the circular ordering
\[
 A_0,B_0,A_1,B_1,\ldots,A_{p-2},B_{p-2},
\]
with \(A_{p-1}=A_0\). As \(t\) runs through \(0,\ldots,p-2\), both \(g^t\) and \(cg^t\) exhaust \(\mathbb F_p^\times\). Therefore the \(A_t\) exhaust the units that are \(1\) modulo \(3\), and the \(B_t\) exhaust those that are \(2\) modulo \(3\). These sets are disjoint and together form \(U(3p)\).

The oriented differences have CRT components
\[
 A_t-B_t=[2,(1-c)g^t]_{3,p},\qquad
 B_t-A_{t+1}=[1,(c-g)g^t]_{3,p}.
\]
Here \(1-c\not\equiv0\pmod p\) and \(c-g\not\equiv0\pmod p\). Hence the first set of \(p-1\) differences exhausts exactly the units congruent to \(2\pmod3\); the second set exhausts exactly the units congruent to \(1\pmod3\). In particular, every cyclic edge (including the closing edge) exists and is labelled with a distinct unit. This proves the claim for \(3p\).

**Step 2: a lifting lemma for every odd prime divisor.** Let \(m>1\) be odd and suppose \(x_0,\ldots,x_{L-1}\), where \(L=\varphi(m)\), is a circular unit-difference ordering modulo \(m\). Then \(L\) is even. Let \(q\ge3\) be prime with \(q\mid m\). Define \(\alpha_i=1\) when \(i\) is even and \(\alpha_i=2\) when \(i\) is odd. For \(0\le r<q\) and \(0\le i<L\), put
\[
 y_{rL+i}=x_i+mr\alpha_i\pmod{mq}.
\]
Read these \(qL\) entries in lexicographic order of \((r,i)\) and close the list cyclically. For fixed \(i\), \(r\mapsto y_{rL+i}\) gives all \(q\) lifts of \(x_i\pmod m\), because \(\alpha_i\in\{1,2\}\) is invertible modulo the odd prime \(q\). Every unit modulo \(mq\) reduces to a unit modulo \(m\), and every lift of such a unit remains a unit modulo \(mq\), since \(q\mid m\). Thus the \(y\)'s list all \(U(mq)\) exactly once.

For \(0\le i<L-1\), the edge at position \((r,i)\) has difference
\[
 (x_i-x_{i+1})+mr(\alpha_i-\alpha_{i+1})\pmod{mq}.
\]
The coefficient \(\alpha_i-\alpha_{i+1}\) is \(1\) or \(-1\), so as \(r\) runs over its \(q\) values these are all lifts of the original unit difference \(x_i-x_{i+1}\pmod m\). The edge from \((r,L-1)\) to \((r+1,0)\), with \(r+1\) interpreted modulo \(q\) at the final closing edge, has difference
\[
 (x_{L-1}-x_0)+m\bigl((\alpha_{L-1}-\alpha_0)r-\alpha_0\bigr)\pmod{mq}.
\]
Because \(L\) is even, \(\alpha_{L-1}=2\) and \(\alpha_0=1\); the coefficient of \(r\) is exactly \(1\). These are all lifts of the last original unit difference. Since the original \(L\) differences are pairwise distinct modulo \(m\), their \(q\)-element lift families are pairwise disjoint. Therefore the lifted cycle has every unit modulo \(mq\) exactly once as an oriented adjacent difference. This proves the lemma.

**Step 3: arbitrary positive exponents.** Begin with the Step 1 cycle modulo \(3p\). Apply Step 2 with \(q=3\) exactly \(a-1\) times, and then with \(q=p\) exactly \(b-1\) times. At every step the chosen odd prime divides the current modulus. The resulting cycle modulo \(3^a p^b\) satisfies the finding. \(\square\)

## Verification

The included standalone `verify.py` implements a primitive-root search modulo the base prime, the explicit CRT base cycle, and the universal lifting construction. It checks that each generated list and its complete cyclic difference set are both exactly the reduced residue system, using exact integer arithmetic and a separate gcd calculation. Run `python3 verify.py`. The tested family has \(137\) distinct moduli \(3^a p^b\) with \(p\le53\), \(1\le a,b\le4\), and \(3^a p^b\le100000\), totalling \(1{,}041{,}828\) verified vertices and oriented edges. The largest checked modulus is \(89{,}373\). The computer tests are finite; the proof in Steps 1–3 covers all stated exponents and primes. For illustration, one cycle modulo \(15\) is \((1,8,7,11,4,2,13,14)\).

## Relationship to prior work

Zhi-Wei Sun, *Some new problems in additive combinatorics* (arXiv:1309.1679, initially public on September 6, 2013), Theorem 1.4, constructs the required circular ordering for **odd prime powers**, using powers of a primitive root. Remark 1.4 conjectures the assertion for every odd integer greater than two. The construction here gives the mixed-prime family \(3^a p^b\) and an exponent-lifting mechanism. Neither is a direct specialization of the prime-power case because every claimed modulus has two distinct prime factors. The general odd-modulus conjecture, if true, would imply this family, but is not established by that theorem.

The property is also a rainbow Hamilton cycle on the induced unit-vertex subgraph of the additive unitary Cayley graph: edge labels are the unit differences, each appearing once. Dejter and Giudici (1995) study the ambient unitary Cayley graph, whose vertex set is all residues, and note decompositions into length-\(n\) Hamilton cycles. This does not give a cycle on just the \(\varphi(n)\) unit vertices with each oriented unit difference exactly once. Nor does a generic complete-mapping theorem for the entire additive group give the required unit-restricted single cycle.

## Limitations

No claim is made for odd moduli with two distinct prime factors neither of which is \(3\), or with three or more distinct prime factors. The claim does not resolve Sun's conjecture for all odd moduli. Computational examples do not certify uniqueness or publication priority. Equivalence with an unindexed result about cyclic group sequences or unitary Cayley graphs remains a bibliographic possibility. Independent mathematical assessment has not been conducted.

## References

1. Zhi-Wei Sun, *Some new problems in additive combinatorics*, arXiv:1309.1679, first public September 6, 2013; see Theorem 1.4, its proof, and Remark 1.4. https://arxiv.org/abs/1309.1679
2. The same article, updated text published in *Nanjing University Journal of Mathematics Biquarterly* 36 (2019), no. 2, pp. 134–155, available as arXiv:1309.1679v9. https://arxiv.org/pdf/1309.1679
3. I. J. Dejter and R. E. Giudici, *On unitary Cayley graphs*, J. Combin. Math. Combin. Comput. 18 (1995), 121–124, author-supplied public full text https://www.researchgate.net/publication/265586967_On_unitary_Cayley_graphs .
