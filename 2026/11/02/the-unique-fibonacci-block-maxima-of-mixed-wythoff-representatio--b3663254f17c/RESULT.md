# The unique Fibonacci-block maxima of mixed Wythoff representation counts

## Finding
Let \(\varphi=(1+\sqrt5)/2\), \(F_0=0\), \(F_1=1\), and \(F_{j+1}=F_j+F_{j-1}\). Set \(u(h)=\lfloor h\varphi\rfloor\) and \(v(k)=\lfloor k\varphi^2\rfloor\) for positive integers \(h,k\). Define
\[
r(n)=\#\{(h,k)\in\mathbb Z_{\ge1}^2:u(h)+v(k)=n\}.
\]
**Theorem.** For every integer \(m\ge4\),
\[
\max_{F_m\le n<F_{m+1}}r(n)=F_{m-1}-1,
\]
and the **unique** maximizer in this Fibonacci interval is \(n=F_{m+1}-2\). In particular, for every integer \(j\ge5\), the positive upper Wythoff numbers have no two-term sum equal to \(F_j-2\).

## Assumptions and scope
Both Wythoff sequences begin at index one; summands and representation indices are strictly positive. The pairs counted by \(r(n)\) have one lower and one upper Wythoff summand, so there is no order-two symmetry factor. The theorem concerns all integer indices \(m\ge4\), without a primality hypothesis. The complement identity \(r(F_j-1)=0\) for \(j\ge5\), established by Kawsumarng et al. and reproved by Shallit, is used only to establish uniqueness at the upper endpoint of each block.

## Proof
Write \(U=\{u(h):h\ge1\}\) and \(V=\{v(k):k\ge1\}\). Beatty's complementary-sequence theorem applies since \(\varphi^{-1}+\varphi^{-2}=1\): every positive integer is in exactly one of \(U,V\). Hence
\[
r(n)=\#\{k\ge1:v(k)<n\}-\#\{k\ge1:v(k)<n,\ n-v(k)\in V\}.
\]
The first count is precisely \(\lfloor n/\varphi^2\rfloor\), because \(v(k)<n\) iff \(k\varphi^2<n\), with \(n/\varphi^2\) irrational. Thus
\[
0\le r(n)\le\lfloor n/\varphi^2\rfloor. \tag{1}
\]

We first show that \(F_j-2\notin V+V\) for every \(j\ge5\), with repetitions permitted in \(V+V\). Put \(t=F_{j-2}\), \(\varepsilon=\varphi^{-(j-2)}\). Binet's formula gives
\[
F_j-t\varphi^2=(-1)^{j-2}\varepsilon,\qquad
0<t\varepsilon<1,\qquad 0<\varepsilon\le\varphi^{-3}<3-\varphi^2. \tag{2}
\]
Suppose \(v(k)+v(\ell)=F_j-2\) for positive integers \(k,\ell\). Set \(s=k+\ell\) and \(f_x=\{x\varphi^2\}\). Adding floors yields
\[
v(k)+v(\ell)=\lfloor s\varphi^2\rfloor-\delta,
\quad \delta=\lfloor f_k+f_\ell\rfloor\in\{0,1\}. \tag{3}
\]
When \(j\) is odd, \(t\varphi^2=F_j+\varepsilon\). For \(s<t\), the right side of (3) is at most \(F_j-3\), whereas for \(s\ge t\) it is at least \(F_j-1\), a contradiction.

When \(j\) is even, \(t\varphi^2=F_j-\varepsilon\). For \(s<t\), (3) is at most \(F_j-3\), and for \(s>t\) it is at least \(F_j\). Therefore \(s=t\) and \(\delta=1\). Since \(\{t\varphi^2\}=1-\varepsilon\), this implies
\[
f_k+f_\ell=2-\varepsilon,\qquad f_k>1-\varepsilon.
\]
Now \(1\le k<t\), and setting \(q=\lceil k\varphi^2\rceil\) and \(e=q-k\varphi^2=1-f_k\) gives \(0<e<\varepsilon\). The integer
\[
D=tq-kF_j=te-k\varepsilon
\]
lies strictly between \(-t\varepsilon\) and \(t\varepsilon\), both within \((-1,1)\) by (2). Hence \(D=0\). But \(\gcd(F_{j-2},F_j)=1\) forces \(t\mid k\), contradicting \(1\le k<t\). This proves the claimed exclusion in both parities.

Now fix \(m\ge4\) and take \(j=m+1\), \(t=F_{j-2}=F_{m-1}\). Formula (2), together with \(2+\varepsilon<\varphi^2\) and \(3-\varepsilon>\varphi^2\), yields the exact floor bounds
\[
\left\lfloor\frac{F_j-2}{\varphi^2}\right\rfloor=t-1,
\qquad
\left\lfloor\frac{F_j-3}{\varphi^2}\right\rfloor\le t-2. \tag{4}
\]
At \(n_*=F_j-2\), the exclusion \(n_*\notin V+V\) makes the second count in the complementary-sequence expression vanish. Hence \(r(n_*)=t-1\). By (1) and (4), every \(n\le F_j-3\) in \([F_{j-1},F_j)\) has \(r(n)\le t-2\). The only other point of the interval is \(F_j-1\), where \(r(F_j-1)=0\) by the cited, established \(U+V\)-complement theorem. As \(t-1\ge1\), the maximizer is unique and the displayed maximum follows. \(\square\)

## Verification
The accompanying standard-library Python program `verify.py` uses exact integer square roots to evaluate both Beatty sequences and direct integer pair enumeration (not floating-point approximations). Running `python3 verify.py` returns `VERIFY_OK fibonacci_blocks=13 F_m_range=4..16 largest_endpoint=1597 complement_up_to=1597`. It tests all Fibonacci intervals from indices four through sixteen, the upper-sum exclusion at indices five through seventeen, and Beatty complementarity through 1597. This is finite corroboration; the infinite assertion follows from the proof above.

## Relationship to prior work
Ashburn's *Proofs of some OEIS conjectures on Wythoff sums, Fibonacci and Lucas words* (first public 2026-10-04, arXiv:2610.04842v1, Section 3, Theorem 1) studies this **same function** and identifies precisely the arguments at which it takes values zero, one, and two; it does not state Fibonacci-block extrema. Shallit's *Sumsets of Wythoff Sequences, Fibonacci Representation, and Beyond* (arXiv:2006.04177v1, Sections 10–11) gives a 12-state recognizer for \(V+V\), and a rank-19 linear representation algorithm for mixed-sum counts; neither inspected section gives the block maximum or its unique location. OEIS A259598 lists the mixed-sum counts, and A335229 lists \(V+V\) elements, but neither inspected entry states the theorem. The exclusion \(F_j-2\notin V+V\), proved above directly, is a sufficient intermediate statement rather than a claim that the entire older sumset characterization is new.

## Limitations
The result gives a maximum and its location on Fibonacci blocks, not a closed pointwise formula for every \(r(n)\). The prior exact automata and linear-representation frameworks could permit another derivation; no claim of exhaustive historical priority or independent mathematical verification is made. The computation covers finite inputs only. The theorem's uniqueness assertion uses the published \(U+V\) complement theorem, clearly identified above.

## References
1. A. Ashburn, *Proofs of some OEIS conjectures on Wythoff sums, Fibonacci and Lucas words*, arXiv:2610.04842v1 (2026-10-04), https://arxiv.org/html/2610.04842v1, Section 3.
2. J. Shallit, *Sumsets of Wythoff Sequences, Fibonacci Representation, and Beyond*, arXiv:2006.04177v1 (2020-06-07), https://arxiv.org/html/2006.04177v1, Sections 7, 10, 11.
3. S. Kawsumarng, T. Khemaratchatakumthorn, P. Noppakaew, and P. Pongsriiam, *Sumsets associated with Wythoff sequences and Fibonacci numbers*, Period. Math. Hung. (2020), DOI:10.1007/s10998-020-00343-0 (complement theorem as restated in references 1–2).
4. OEIS, A259598, https://oeis.org/A259598; and A335229, https://oeis.org/A335229 (entries accessed 2026-10-27 UTC).
