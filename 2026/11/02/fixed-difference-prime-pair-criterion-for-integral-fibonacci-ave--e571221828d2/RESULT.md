# Fixed-difference prime-pair criterion for integral Fibonacci averages

## Finding
Let \(F_0=0\), \(F_1=1\), and \(F_{n+2}=F_{n+1}+F_n\). For distinct primes \(5<p<q\), put \(d=q-p\), necessarily a positive even integer, \(n=pq\), and \(S_n=\sum_{j=1}^{n}F_j=F_{n+2}-1\). Set
\[
A_d=\begin{cases}0,&d=2,\\F_{d-3}-1,&d\ge4,\end{cases}
\qquad B_d=F_{d+3}-1.
\]
Write \(\chi_\ell=(5/\ell)\in\{-1,+1\}\) for the Legendre symbol at an odd prime \(\ell\ne5\).

**Exact local residue law.** The congruences are
\[
S_{pq}\equiv
\begin{cases}A_d,&\chi_p=-1,\\B_d,&\chi_p=+1\end{cases}\pmod p,
\qquad
S_{pq}\equiv
\begin{cases}A_d,&\chi_q=+1,\\B_d,&\chi_q=-1\end{cases}\pmod q.
\]
Thus \(pq\mid S_{pq}\) if and only if the indicated residue vanishes modulo each corresponding prime. This is a complete criterion in terms of the fixed-gap Fibonacci integers \(A_d,B_d\), without calculating the Fibonacci number indexed by \(pq+2\).

**Sharp gap dichotomy.** If \(d\in\{2,4\}\), then
\[
pq\mid S_{pq}\quad\Longleftrightarrow\quad p\equiv2\pmod5.
\]
For each fixed even \(d\ge6\), there are only finitely many such prime pairs. More precisely, every pair satisfying \(pq\mid S_{pq}\) obeys
\[
5<p\le F_{d+3}-1,\qquad q=p+d.
\]
The theorem does not assert that infinitely many prime pairs of gap \(2\) or \(4\) exist in the required congruence class.

## Assumptions and scope
All primes in the theorem are distinct and exceed \(5\); the exclusion is needed for the nonzero discriminant \(5\) in the finite-field argument. The term 'gap' means the difference \(q-p\) and does not require that the two primes be consecutive. Fibonacci indices in intermediate calculations may be negative, using the unique bi-infinite extension \(F_{-m}=(-1)^{m+1}F_m\) for \(m\ge1\). All divisibility is ordinary divisibility in the integers.

## Proof
Let
\[
Q=\begin{pmatrix}1&1\\1&0\end{pmatrix}.
\]
Since \(\det Q=-1\), this matrix is invertible over every finite field and for every integer exponent. The Fibonacci recurrence gives
\[
Q^k=\begin{pmatrix}F_{k+1}&F_k\\F_k&F_{k-1}\end{pmatrix}\qquad (k\in\mathbb Z).
\]
The characteristic polynomial is \(T^2-T-1\), with discriminant \(5\). For every odd prime \(\ell>5\), its roots are distinct and nonzero in an algebraic closure of \(\mathbb F_\ell\). If \(\chi_\ell=+1\), they belong to \(\mathbb F_\ell^\times\), so diagonalization and Fermat's theorem yield
\[
Q^{\ell-1}=I\pmod\ell.
\]
If \(\chi_\ell=-1\), the two roots \(\alpha,\beta\in\mathbb F_{\ell^2}\) are exchanged by Frobenius: \(\alpha^\ell=\beta\) and \(\beta^\ell=\alpha\). Their product is \(-1\), so \(\alpha^{\ell+1}=\beta^{\ell+1}=-1\). Therefore
\[
Q^{\ell+1}=-I\pmod\ell.
\]
The matrix congruences are valid over \(\mathbb F_\ell\), since the scalar matrices are fixed by extension of scalars.

Now write \(d=q-p\). Two exact integer identities are
\[
pq+1=(p+1)(q-1)+(2-d)
      =(p-1)(q+1)+(d+2).
\]
Modulo \(p\), if \(\chi_p=-1\), use \(Q^{p+1}=-I\) in the first decomposition. Because \(q-1\) is even, \(Q^{pq+1}=Q^{2-d}\pmod p\). If \(\chi_p=+1\), use \(Q^{p-1}=I\) in the second decomposition to get \(Q^{pq+1}=Q^{d+2}\pmod p\). Modulo \(q\), use the second decomposition when \(\chi_q=-1\): since \(p-1\) is even, \(Q^{pq+1}=Q^{d+2}\pmod q\). Use the first decomposition when \(\chi_q=+1\) to get \(Q^{pq+1}=Q^{2-d}\pmod q\). Taking the upper-left entries gives \(F_{pq+2}\equiv F_{3-d}\) or \(F_{d+3}\) as indicated.

Since \(d\) is even, \(F_{3-d}=F_{d-3}\) for \(d\ge4\) by the negative-index sign rule, and \(F_{3-2}=F_1=1\). Subtracting \(1\) proves the stated local congruences. The Chinese remainder theorem, together with \(p\ne q\), proves the necessary-and-sufficient criterion for \(pq\mid S_{pq}\).

For \(d=2\) one has \((A_d,B_d)=(0,4)\); for \(d=4\) one has \((A_d,B_d)=(0,12)\). Because \(p,q>5\), neither prime divides \(B_d\). Thus integrality requires \(\chi_p=-1\) and \(\chi_q=+1\). The quadratic character of \(5\) at these primes is \(+1\) exactly for residues \(1,4\pmod5\), and \(-1\) exactly for residues \(2,3\pmod5\). With \(q=p+d\) and \(d\in\{2,4\}\), the two character requirements reduce exactly to \(p\equiv2\pmod5\).

Finally fix an even \(d\ge6\). Then \(A_d=F_{d-3}-1\ge1\) and \(B_d=F_{d+3}-1>A_d\) are fixed positive integers. For every qualifying pair, the first local congruence forces \(p\mid A_d\) or \(p\mid B_d\); hence \(p\le B_d\). There are only finitely many such primes and each determines \(q=p+d\). This proves the explicit bound and finiteness.

## Verification
Run the standalone standard-library checker with `python3 checkers/verify.py`. It constructs every prime pair \((p,q)\) with \(5<p<q\le6000\) and even difference \(2\le q-p\le140\). For each of the 14,028 pairs, it independently computes \(F_{pq+2}-1\pmod{pq}\) by fast doubling, compares both local residues against the fixed-gap formula, and checks the complete divisibility criterion. It separately verifies the gap-\(2\) and gap-\(4\) characterization and the fixed-gap bound; representative qualifying pairs include \((7,11)\), \((17,19)\), \((11,29)\), \((37,41)\), and \((151,199)\). All checks use exact integer arithmetic. Finite testing does not replace the general field-theoretic proof.

## Relationship to prior work
Fatehizadeh and Yaqubi (2022) study integral averages of Fibonacci numbers and give an implicit congruence criterion \(F_{n+2}\equiv1\pmod n\). Křížek and Somer (2024) develop more general recurrence-period criteria and explicitly exhibit the semiprime \(319=11\cdot29\). Flynn-Connolly (first posted April 14, 2025) proves infinitely many odd indices with integral Fibonacci average and notes the difficulties of a semiprime treatment. The present statement is different: an evaluated, necessary-and-sufficient local residue law valid for **every** prime pair of a prescribed even difference, including a sharp two-gap distinction and an explicit bound for every larger fixed gap. An index sequence of the same average-integrality condition, OEIS A124456, records examples but not this prime-pair gap classification. The derivation uses classical finite-field Fibonacci matrix identities rather than a new prime-distribution theorem.

## Limitations
This is a conditional classification of prime pairs and does not prove their infinitude at gaps \(2\) or \(4\). The case where a prime is \(2\), \(3\), or \(5\) is excluded rather than silently extrapolated. For \(d\ge6\), the theorem is a finite reduction and explicit bound; it does not tabulate all qualifying pairs for arbitrary large \(d\). Independent assessment of historical priority, including the possibility of an earlier equivalent matrix-congruence formulation, is outstanding.

## References
1. O. Flynn-Connolly, *On the divisibility of sums of Fibonacci numbers*, arXiv:2504.09938 (first version April 14, 2025); later in *Integers* **25** (2025), A87. https://arxiv.org/abs/2504.09938
2. A. Fatehizadeh and D. Yaqubi, *Average of the Fibonacci Numbers*, *Journal of Integer Sequences* **25** (2022), Article 22.2.6. https://cs.uwaterloo.ca/journals/JIS/VOL25/Yaqubi/yaq6.pdf
3. M. Křížek and L. Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, *Integers* **24** (2024), A36. https://math.colgate.edu/~integers/y36/y36.pdf
4. OEIS A124456, *Numbers dividing the sum of the first n Fibonacci numbers and not divisible by 24*. https://oeis.org/A124456
