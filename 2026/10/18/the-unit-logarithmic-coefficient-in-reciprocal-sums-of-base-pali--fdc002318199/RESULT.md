# The unit logarithmic coefficient in reciprocal sums of base palindromes

## Finding
For every integer base \(b\ge2\), let \(s_b\) be the convergent sum of reciprocals of all positive base-\(b\) palindromes. Define
\[
H_b=\sum_{a=1}^{b-1}\frac1a,\qquad Y_b=\sum_{m=b}^{b^2-1}\frac1m,\qquad
g(b)=\frac{b+2}{b+1}H_b+\left(\frac1b+\frac2{b^2}\right)Y_b.
\]
The following uniform refinement holds:
\[
\boxed{\left|b^3\bigl(s_b-g(b)\bigr)-(2Y_b-H_b)\right|\le4.}
\]
Consequently,
\[
\boxed{\lim_{b\to\infty}\frac{b^3(s_b-g(b))}{\log b}=1,}
\]
or equivalently \(s_b=g(b)+(\log b+O(1))/b^3\). The constant \(4\) is convenient rather than asserted best possible.

## Assumptions and scope
Here a positive integer is a base-\(b\) palindrome if its unique base-\(b\) representation without leading zero reads identically in reverse. Write \(S_{b,k}\) for the reciprocal sum restricted to palindromes having exactly \(k\) digits, so \(s_b=\sum_{k\ge1}S_{b,k}\). The full sum converges: there are \((b-1)b^{\lceil k/2\rceil-1}\) length-\(k\) palindromes, and each is at least \(b^{k-1}\), yielding a geometrically convergent tail for fixed \(b\). No primality or restriction on the base is assumed. All inequalities below hold uniformly for integers \(b\ge2\).

## Proof
**Step 1 (exact first two blocks).** The one-digit palindromes give \(S_{b,1}=H_b\). Every two-digit palindrome is \((aa)_b=a(b+1)\) with \(1\le a\le b-1\), hence \(S_{b,2}=H_b/(b+1)\).

**Step 2 (uniform comparison for every longer block).** Put \(Z_b=\sum_{m=b+1}^{b^2}1/m=Y_b-(b-1)/b^2\). Fix \(k\ge4\) and the first two digits \(a,c\), where \(1\le a\le b-1\) and \(0\le c\le b-1\). Exactly \(b^{\lfloor (k-3)/2\rfloor}\) length-\(k\) palindromes have these initial digits. Each of their numerical values \(N\) lies in
\[
b^{k-2}(ab+c)\le N<b^{k-2}(ab+c+1).
\]
Since \(k-2-\lfloor(k-3)/2\rfloor=\lfloor k/2\rfloor\), summing their reciprocals proves
\[
\boxed{\frac{Z_b}{b^{\lfloor k/2\rfloor}}\le S_{b,k}\le\frac{Y_b}{b^{\lfloor k/2\rfloor}}\quad(k\ge4).}
\]
In particular, define the two nonnegative deficits
\[
E_{45}=\frac{2Y_b}{b^2}-(S_{b,4}+S_{b,5}),\qquad E_{67}=\frac{2Y_b}{b^3}-(S_{b,6}+S_{b,7}).
\]
The comparison gives
\[
0\le b^3E_{45}\le2b(Y_b-Z_b)=\frac{2(b-1)}b<2,
\qquad 0\le b^3E_{67}\le2(Y_b-Z_b)=\frac{2(b-1)}{b^2}\le\frac12.
\]
The tail \(T_b=\sum_{k\ge8}S_{b,k}\) satisfies
\[
0\le b^3T_b\le \frac{2Y_b}{b(1-1/b)}=\frac{2Y_b}{b-1}\le2,
\]
where the last inequality uses \(Y_b\le b-1\), valid term-by-term because there are \(b^2-b\) denominators, each at least \(b\). (The middle geometric-series expression is \(2Y_b/[b(1-1/b)]\).)

**Step 3 (three-digit deficit is the harmonic sum to bounded error).** Every three-digit palindrome is \((aca)_b=ab^2+cb+a\). Write \(t=ab+c\) and
\[
D_b=\frac{Y_b}b-S_{b,3}=\sum_{a=1}^{b-1}\sum_{c=0}^{b-1}\frac{a}{bt(bt+a)}\ge0.
\]
Equivalently,
\[
b^3D_b=\sum_{a=1}^{b-1}\sum_{c=0}^{b-1}\frac{ba}{t^2(1+a/(bt))}.
\]
Let \(A_b=\sum_{a,c}ba/t^2\). Since \(ab\le t<(a+1)b\), for each \(a\),
\[
\frac{a}{(a+1)^2}\le b a\sum_{c=0}^{b-1}\frac1{(ab+c)^2}\le\frac1a.
\]
It follows that \(0\le H_b-A_b\) and, by an exact telescoping identity,
\[
H_b-A_b\le\sum_{a=1}^{b-1}\left(\frac1a-\frac{a}{(a+1)^2}\right)
=1-\frac1b+\sum_{j=2}^{b}\frac1{j^2}<\sum_{j=1}^{\infty}\frac1{j^2}<\frac74.
\]
Also, by \(0\le1-1/(1+x)\le x\) for \(x\ge0\),
\[
0\le A_b-b^3D_b\le\sum_{a,c}\frac{a^2}{(ab+c)^3}
\le\frac{H_b}{b^2}\le\frac{b-1}{b^2}\le\frac14.
\]
Therefore \(0\le H_b-b^3D_b<2\).

**Step 4 (assembly).** Combining the exact first two blocks, the three-digit expression and the two deficit definitions gives the exact identity
\[
s_b-g(b)=\frac{2Y_b}{b^3}-D_b-E_{45}-E_{67}+T_b.
\]
Multiplication by \(b^3\), followed by subtraction of \(2Y_b-H_b\), yields
\[
b^3(s_b-g(b))-(2Y_b-H_b)
=(H_b-b^3D_b)-b^3E_{45}-b^3E_{67}+b^3T_b.
\]
The four terms lie respectively in \([0,2]\), \([-2,0]\), \([-1/2,0]\), and \([0,2]\); hence their sum is in \([-5/2,4]\), proving the asserted absolute bound. Finally \(H_b=\log b+\gamma+O(1/b)\), \(Y_b=\log b+O(1/b)\), so \(2Y_b-H_b=\log b-\gamma+O(1/b)\). Division by \(\log b\) gives the displayed limit, with coefficient exactly \(1\).

## Verification
The self-contained script `check.py`, run with `python3 check.py`, enumerates palindromes through seven digits for bases \(2\) through \(6\) using exact rational arithmetic. It independently computes \(H_b,Y_b,S_{b,k}\), checks the block comparisons and the three-digit deficit, then brackets the *infinite* reciprocal sum by an explicit analytically bounded geometric tail. It tests that this certified rational interval satisfies the theorem. Tests passed in all five bases. This finite test does not establish the general theorem; Steps 1–4 constitute the proof.

## Relationship to prior work
The sum was posed as Problem B-441 by Jeffrey Shallit in 1980 and its convergence proved in the solution published by H. Klauser in *Fibonacci Quarterly* 19 (1981), p. 469. Phunphayap and Pongsriiam, *Reciprocal Sum of Palindromes*, *Journal of Integer Sequences* 22 (2019), Article 19.8.6, Theorem 4, use exactly the same main term \(g(b)\) and prove an explicit bound \(s_b-g(b)=O(\log b/b^3)\) together with a nonzero positive limsup after that normalization. Their Theorems 1 and 5 bound individual lengths and give a harmonic-number expansion, respectively. The finite limit with explicit leading coefficient \(1\), and the uniformly bounded centered residual, are more precise than those reported statements. The proof above is self-contained rather than an invocation of their block lemma.

## Limitations
The limit concerns the base \(b\to\infty\), not the number of digits at fixed base, and the uniform numerical constant \(4\) has not been optimized. Searches and inspection of the original main source cannot exclude an equivalent previously published refinement under a different normalization. No independent audit or external formal verification was performed.

## References
1. J. Shallit, Problem B-441 (1980); H. Klauser, solution, “Sum of Base-b Palindrome Reciprocals,” *Fibonacci Quarterly* 19 (1981), 469. https://www.fq.math.ca/Scanned/19-5/elementary19-5.pdf
2. P. Phunphayap and P. Pongsriiam, “Reciprocal Sum of Palindromes,” *Journal of Integer Sequences* 22 (2019), Article 19.8.6, Theorems 1, 4–5. https://cs.uwaterloo.ca/journals/JIS/VOL22/Pongsriiam/pong32.pdf ; preprint https://arxiv.org/abs/1803.00161
3. OEIS A244162, base-two palindrome reciprocal constant; entry dated June 21, 2014. https://oeis.org/A244162
