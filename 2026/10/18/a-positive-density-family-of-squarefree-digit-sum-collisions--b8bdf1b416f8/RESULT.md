# A positive-density family of squarefree digit-sum collisions

## Finding
Let \(S_b(n)\) be the sum of the digits of the positive integer \(n\) in base \(b\), and set \(H_b(n)=nS_b(n)\). For every integer \(b\ge 11\), define
\[
X_b=b(2b-3),\qquad Y_b=(b-2)(2b-3).
\]
Then \(X_b>Y_b>0\), and \(H_b(X_b)=H_b(Y_b)\). Both integers are squarefree if and only if \(3\nmid b\) and each of \(b\), \(b-2\), \(2b-3\) is squarefree.

The set \(\mathcal B\) of bases \(b\ge11\) satisfying this exact criterion has natural density
\[
\boxed{\delta=\frac5{18}\prod_{p\ge5\text{ prime}}\left(1-\frac3{p^2}\right)>0.}
\]
Consequently, for at least a proportion \(\delta\) of all integer bases, \(H_b\) is noninjective even when restricted to squarefree positive integers. The density concerns this explicit witness family, not the set of all bases admitting arbitrary collisions.

## Assumptions and scope
The base \(b\) ranges over ordinary positive integers \(b\ge11\). Squarefree means that no prime square divides the integer. The natural density of \(\mathcal B\) is \(\lim_{T\to\infty}T^{-1}\#\{11\le b\le T:b\in\mathcal B\}\). The numbers \(X_b\) and \(Y_b\) are ordered witnesses; no uniqueness or minimality of witnesses is asserted. The finite exclusion \(b<11\) does not affect density. The algebraic identities themselves work for \(b\ge7\).

## Proof
**Digit sums and equality.** For \(b\ge7\), the exact positional expansions are
\[
X_b=b^2+(b-3)b+0,
\qquad
Y_b=b^2+(b-7)b+6.
\]
Here all displayed coefficients are admissible base-\(b\) digits: \(0\le b-7<b\) and \(0\le6<b\). Thus \(S_b(X_b)=1+(b-3)=b-2\) and \(S_b(Y_b)=1+(b-7)+6=b\). Hence
\[
H_b(X_b)=b(2b-3)(b-2)=H_b(Y_b),
\qquad X_b-Y_b=2(2b-3)>0.
\]

**Exact squarefree criterion.** A product \(uv\) of positive integers is squarefree precisely when both factors are squarefree and coprime. Euclid's algorithm gives
\[
\gcd(b,2b-3)=\gcd(b,3),\qquad
\gcd(b-2,2b-3)=1.
\]
Applying the product criterion to \(X_b\) and \(Y_b\) proves that they are both squarefree exactly when all three linear factors are squarefree and \(3\nmid b\).

**Local prime-square restrictions.** At \(p=2\), simultaneous squarefreeness of \(b\) and \(b-2\) forces \(b\) odd, and every odd residue modulo four is allowed. The local density is \(1/2\). At \(p=3\), the restriction \(3\nmid b\) and squarefreeness of \(b-2\) leave exactly \(b\equiv1,4,5,7,8\pmod9\), giving density \(5/9\); squarefreeness of the other two linear factors imposes no further condition at three. For a prime \(p\ge5\), the excluded residues modulo \(p^2\) are the three distinct classes
\[
b\equiv0,\qquad b\equiv2,\qquad b\equiv3\cdot2^{-1}\pmod{p^2},
\]
corresponding to divisibility of \(b\), \(b-2\), and \(2b-3\) by \(p^2\). Their distinctness follows from \(p\ge5\). The allowed density is \(1-3/p^2\).

**Global density and positivity.** For each fixed prime cutoff \(P\ge5\), the Chinese remainder theorem gives the exact natural density of integers satisfying every restriction up to \(P\):
\[
\delta(P)=\frac5{18}\prod_{5\le p\le P\text{ prime}}\left(1-\frac3{p^2}\right).
\]
For \(11\le b\le T\), a failure at a prime \(p>P\) implies \(p^2\) divides one of \(b\), \(b-2\), or \(2b-3\). Such primes satisfy \(p\le\sqrt{2T}\). For each such \(p\ge5\), the three linear congruences each have one residue class modulo \(p^2\), and each contributes at most \(T/p^2+1\) integers. Therefore the number of failures at primes exceeding \(P\) is at most
\[
3T\sum_{p>P}\frac1{p^2}+3\sqrt{2T}.
\]
The corresponding upper density tends to zero as \(P\to\infty\). Hence the infinite restriction set has density \(\lim_{P\to\infty}\delta(P)\), yielding the displayed Euler product. All factors are strictly positive, and the sum \(\sum_{p\ge5}3/p^2\) converges, so their infinite product is strictly positive.

For example, \(b=13\) gives \(X_b=299=13\cdot23\), \(Y_b=253=11\cdot23\), both squarefree, and \(H_{13}(299)=H_{13}(253)=3289\).

## Verification
Run the standalone file `verify.py` using Python 3. The checks enumerate bases from \(7\) through \(30000\) for the actual digit sums and collision identity, bases from \(7\) through \(2000\) for the squarefree equivalence, and local congruence counts for the eleven listed primes from \(2\) through \(31\). These experiments test arithmetic and boundary details but do not replace the general proof. The Euler-product density follows from the Chinese remainder theorem and the explicit prime-square tail bound above.

## Relationship to prior work
Noppakaew and Pongsriiam, *Product of Some Polynomials and Arithmetic Functions*, Journal of Integer Sequences 26 (2023), Article 23.9.1, Example 11 proves noninjectivity of \(H_b\) without a squarefree restriction. Example 14 lists squarefree collisions for \(2\le b\le10\); specifically its \(b=7\) example is the special pair \((55,77)\) arising from these formulas. Their Question 30 asks whether squarefree collisions exist for every \(b\ge11\). The present result does **not** answer that universal question, but proves a positive-density infinite family of bases with explicit squarefree collisions and computes the exact density of bases admitted by this construction. Standard prime-square sieving supplies the counting mechanism; the digit-sum identity and its squarefree specialization are the problem-specific content.

## Limitations
The result proves noninjectivity only for bases in the explicitly defined set \(\mathcal B\), not for every base. It does not give the density of all bases with some squarefree collision and does not classify all witness pairs or the minimal witnesses. The proof is self-contained, but unindexed literature may contain an equivalent construction or a stronger theorem. No independent mathematical audit has been performed.

## References
Noppakaew, P., and Pongsriiam, P. (2023). *Product of Some Polynomials and Arithmetic Functions*, Journal of Integer Sequences **26**, Article 23.9.1, published 2023-11-02. https://cs.uwaterloo.ca/journals/JIS/VOL26/Pongsriiam/pong43.pdf ; journal landing page https://cs.uwaterloo.ca/journals/JIS/VOL26/Pongsriiam/pong43.html . Especially Examples 11 and 14 and Question 30.
