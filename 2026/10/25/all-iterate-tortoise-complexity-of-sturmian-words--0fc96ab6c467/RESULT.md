# All-iterate tortoise complexity of Sturmian words

## Finding
Let \(\alpha\in(0,1)\) be irrational, and let \(\mathcal L_\alpha(n)\) be the set of distinct length-\(n\) factors of any binary Sturmian word of slope \(\alpha\), with symbol \(1\) having frequency \(\alpha\). For a binary finite word \(w\), define \(T(w)\) by removing the leftmost occurrence of \(1\) and appending a \(1\); leave an all-zero word unchanged. For every integer \(k\ge 2\) and \(n\ge1\), put
\[
\rho_{\alpha,k}(n)=\bigl|\{T^k(w):w\in\mathcal L_\alpha(n)\}\bigr|.
\]
Then the **complete two-parameter profile** is
\[
\boxed{\rho_{\alpha,k}(n)=n+1-\min\!\left\{n-1,\left\lfloor\frac{k}{\alpha}\right\rfloor\right\}
=\max\!\left\{2,n+1-\left\lfloor\frac{k}{\alpha}\right\rfloor\right\}.}
\]
At length zero the image count is one. The same proof also works for \(k=1\), but the substantive assertion here concerns every \(k\ge2\).

Writing \(B_k=\lfloor k/\alpha\rfloor\), this says the image count is two for all \(1\le n\le B_k+1\), then grows with slope one. Since the Abelian complexity of a Sturmian word is two at all positive lengths, the first disagreement with Abelian complexity occurs at length \(B_k+2\), so the abelian-agreement cutoff introduced for tortoise complexity equals \(B_k+1\). Moreover the family of all iterated profiles determines the slope: \(\lim_{k\to\infty} k/B_k=\alpha\). These are consequences of the boxed formula, not separate independent classifications.

## Assumptions and scope
The symbols are ordered \(0<1\). The map \(T\) is the restriction of the Defant--Kravitz tortoise operator to binary words: each iteration transfers the leftmost \(1\) to the right end. The exponent \(k\) means exactly \(k\) iterations, with repetitions beyond the number of ones leaving a sorted word unchanged.

An equivalent specification of the factor language is obtained from the lower mechanical coding
\[
W_n(x)_i=\lfloor x+(i+1)\alpha\rfloor-\lfloor x+i\alpha\rfloor,
\quad 0\le i<n,\quad 0\le x<1.
\]
Irrational rotation is dense, so every open interval of phase values is visited by shifts of any such coding. Thus the set of these words is precisely \(\mathcal L_\alpha(n)\) for every Sturmian sequence with slope \(\alpha\), regardless of intercept. Irrationality is essential to the simple statement about distinct boundaries: no positive integer multiple of \(\alpha\) is integral. We make no claim here for arbitrary periodic words at lengths beyond their period, or for nonbinary alphabets.

## Proof
**1. A zero-position order lemma.** For a binary word \(w\) of length \(n\), let its zeros be at one-indexed positions \(z_1<\cdots<z_r\). When the first \(k\) ones are transferred to the right, the \(i\)-th zero shifts left past precisely \(\min\{k,z_i-i\}\) ones. Its new position is therefore
\[
\boxed{z'_i=\max\{i,z_i-k\}.}
\]
This formula also covers words containing fewer than \(k\) ones, because further iterations fix the fully sorted word. Suppose two binary words \(u,v\) of the same length have at least as many zeros in every prefix of \(u\) as in the corresponding prefix of \(v\). Then \(u\) has at least as many zeros as \(v\), and its \(i\)-th zero occurs no later than the \(i\)-th zero in \(v\) for each common zero rank. The displayed map preserves these inequalities. Hence \(T^k(u)\) still has at least as many zeros in each prefix as \(T^k(v)\). In particular \(T^k(u)\le_{\rm lex}T^k(v)\): the first differing bit, if any, must be zero on the left and one on the right.

**2. Order the Sturmian factors by phase.** For \(0\le x<y<1\), the number of ones in the first \(j\) characters of \(W_n(x)\) is \(\lfloor x+j\alpha\rfloor\), which is no greater than \(\lfloor y+j\alpha\rfloor\). The corresponding number of zeros is therefore no smaller. By Step 1, \(T^k(W_n(x))\) is lexicographically nondecreasing as the phase \(x\) increases. Consequently every image appears in one contiguous block of the phase-ordered factors, and the number of distinct images is the number of original phase cells minus the number of adjacent cell boundaries across which the image does not change.

**3. Find every phase boundary.** The length-\(n\) mechanical factors change only at the distinct points \(x_j=\{-j\alpha\}\), for \(0\le j\le n\), where braces mean fractional part. These points partition the phase interval into exactly \(n+1\) nonempty cells, corresponding to distinct factors. The point \(x_0=0\) is an endpoint rather than an interior boundary. At \(x_n\), only the final bit changes; its two neighboring factors have different numbers of ones, and their tortoise images cannot be equal because \(T\) preserves letter counts.

For each interior boundary \(x_j\) with \(1\le j<n\), exactly two adjacent input bits change. The neighboring factors are
\[
p\,01\,s\quad\text{and}\quad p\,10\,s,
\qquad |p|=j-1.
\]
Their \(k\)-fold tortoise images coincide precisely when \(p\) contains fewer than \(k\) ones: then the displayed swapped \(1\) belongs to the first \(k\) ones and gets transferred to the end in either word. If \(p\) contains at least \(k\) ones, all transfers take place inside the shared prefix and the different adjacent bits remain visible.

Since \(x_j=\lceil j\alpha\rceil-j\alpha\), the stable prefix has exactly
\[
|p|_1=\lfloor x_j+(j-1)\alpha\rfloor
=\lceil j\alpha\rceil-1
\]
ones. Therefore this boundary merges under \(T^k\) if and only if \(j\alpha<k\). For irrational \(\alpha\), the number of indices \(j\) satisfying \(1\le j<n\) and \(j\alpha<k\) is exactly
\[
\min\left\{n-1,\left\lfloor\frac{k}{\alpha}\right\rfloor\right\}.
\]
Subtracting this number from the \(n+1\) factor cells gives the asserted image count. The cutoff and slope-recovery consequences follow immediately. \(\square\)

## Verification
The included standalone Python program `verify_tortoise.py` computes mechanical factor sets for the coprime rational test slopes \(a/q\), with denominators \(q=11,19,37,53,101,211\) and factor lengths below their periods. It compares independent implementations of the \(k\)-fold operator: repeated deletion-and-append versus the zero-position formula from Step 1. It checks the predicted expression for \(k=1,\ldots,8\), covering 114,832 parameter instances, and separately cross-checks the phase-discontinuity factor construction and a long-period approximation to Fibonacci slope. A run of the program returned `VERIFY_OK` and `FIBONACCI_APPROX_OK`. These are finite regression checks, not substitutes for the irrational all-length proof.

To reproduce: run `python3 verify_tortoise.py` with a standard Python 3 interpreter. No nonstandard dependencies, remote resources, or external certificates are required.

## Relationship to prior work
Defant and Kravitz introduced the tortoise operator for general words. Campbell and Rampersad introduced the iterated tortoise complexity of infinite words, established results for Thue--Morse and paperfolding, and specifically invited extensions to Sturmian sequences. Their general bounded-deficit result for one iteration does not calculate the \(k\)-dependent deficit for Sturmian words. The present theorem gives that deficit **for every iteration count at once** and computes the paper's abelian-agreement cutoff in this new setting.

The \(k=1\) specialization is not asserted as the novel content. The new structural ingredient is the zero-position order lemma together with a phase-by-phase collision count applicable to all \(k\ge2\). Earlier studies of rotation codings and of finite-word stack sorting do not by themselves imply the two-parameter formula. No priority claim is made against unexamined or unindexed sources.

## Limitations
The theorem is exact only for binary Sturmian factor languages with irrational slope. It does not evaluate the same invariant for general binary linear-complexity words, paperfolding, Thue--Morse, or multi-letter codings. The supplied regression data are finite; the universal assertion depends on the written proof. Originality is evaluated against the specifically cited and searched literature, not independently certified against all possible publications.

## References
1. J. M. Campbell and N. Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811 (first posted 2026-04-28), especially Sections 3--4 and 7. https://arxiv.org/abs/2604.25811
2. C. Defant and N. Kravitz, *Stack-sorting for Words*, arXiv:1809.09158 (first posted 2018-09-24); published in *Australasian Journal of Combinatorics* 77 (2020). https://arxiv.org/abs/1809.09158
3. M. Morse and G. A. Hedlund, *Symbolic dynamics II: Sturmian trajectories*, American Journal of Mathematics 62 (1940), 1--42 (classical Sturmian factor background).
