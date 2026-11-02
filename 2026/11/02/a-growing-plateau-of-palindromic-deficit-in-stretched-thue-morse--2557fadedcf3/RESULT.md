# A growing plateau of palindromic deficit in stretched Thue–Morse words

## Finding

Let \(\mu(0)=01\), \(\mu(1)=10\), and \(\mathbf t=\mu^\omega(0)\). For every integer \(M\ge1\) put \(h_M(0)=a\), \(h_M(1)=a^M b\), and \(\mathbf u_M=h_M(\mathbf t)\). Let \(p_M(n)\) be its factor complexity and \(P_M(n)\) its palindromic complexity, with distinct contiguous factors counted once. Define the local gap
\[
T_M(n)=p_M(n+1)-p_M(n)+2-P_M(n)-P_M(n+1).
\]
Then, for every integer \(M\ge1\) and every integer \(n\) with \(2M+3\le n\le3M+4\),
\[
\boxed{T_M(n)=2.}
\]
Indeed, putting \(N=2M+3\), one has \(p_M(N)=3M+6\) and, for \(1\le t\le M+1\),
\[
p_M(N+t)=3M+7+3t,\qquad
P_M(N+t)=\begin{cases}2,&M+t\text{ odd},\\1,&M+t\text{ even}.\end{cases}
\]
Furthermore \(P_M(N)+P_M(N+1)=4\) and \(P_M(3M+5)=0\). The Brlek–Reutenauer identity implies the consequence \(D(\mathbf u_M)\ge M+2\), where \(D\) is palindromic defect.

## Assumptions and scope

The alphabet \(\{a,b\}\) is labeled and \(M\) ranges over all positive integers; the source infinite word is the standard Thue–Morse fixed point. A factor is a contiguous block. A word \(w\) is right special if both \(wa\) and \(wb\) occur. The 2026 source proves uniform recurrence, aperiodicity, and reversal closure of \(\mathbf u_M\); the present argument also independently checks the exact short-factor premises needed below. The theorem concerns a growing initial interval after the first deficit length, not all lengths.

## Proof

**1. Exact Thue–Morse gap catalogue.** Between two consecutive occurrences of \(1\) in \(\mathbf t\) there are \(r\in\{0,1,2\}\) zeros. Successive gap parameters are unequal. In fact, the **complete** set of three consecutive gap parameters is
\[
\mathcal G_3=\{(0,1,2),(0,2,0),(0,2,1),(1,0,1),(1,0,2),
(1,2,0),(1,2,1),(2,0,1),(2,0,2),(2,1,0)\}.
\]
This is an exact finite check, not an inference from a long prefix. Every factor of length at most \(16\) of \(\mathbf t\) lies in one of the four words \(\mu^4(00),\mu^4(01),\mu^4(10),\mu^4(11)\), since \(\mu^4\) has constant length \(16\) and all four two-letter factors occur. None contains \(000\), and a three-gap pattern is encoded by the binary factor \(1 0^{r_1}1 0^{r_2}1 0^{r_3}1\), whose length is at most \(10\). Inspecting the four 32-letter words yields exactly the displayed list, certified by `verify_gap_catalog.py`.

It follows that successive \(b\)'s in \(\mathbf u_M\) are separated by \(M+r\) occurrences of \(a\), with gap parameter \(r\) from this catalogue. In particular every \(a\)-run has length at most \(M+2\).

**2. Base counts.** Put \(N=2M+3\). At length \(N\), factors with one \(b\) number \(3\) (the outside \(a\)-runs have lengths \((M,M+2),(M+1,M+1),(M+2,M)\)); those with two \(b\)'s number \((M+2)+(M+1)+M=3M+3\), indexed by the internal gap parameter \(r=0,1,2\). There are no factors with zero or three \(b\)'s. Thus \(p_M(N)=3M+6\). At length \(N+1\), one-, two-, and three-\(b\) factors number respectively \(2,3M+6,2\), hence \(p_M(N+1)=3M+10\). The three-\(b\) patterns at this length have gap parameters \((0,1)\) or \((1,0)\). Palindromes at \(N\) include one one-\(b\) factor, plus either one or two two-\(b\) factors according to the parity of \(M\); at \(N+1\) there are respectively two or one palindromic two-\(b\) factors. Thus \(P_M(N)+P_M(N+1)=4\).

**3. All right-special factors on the plateau.** For \(1\le t\le M+1\), put \(n=N+t\). Every length-\(n\) factor contains a \(b\). A right-special factor must end in precisely \(a^M\) or \(a^{M+1}\): any shorter terminal run can only be followed by \(a\), and a terminal \(a^{M+2}\) can only be followed by \(b\). A right-special length-\(n\) factor cannot contain just one \(b\): its required initial \(a\)-run would exceed \(M+2\), except at \(t=1\) with suffix \(a^{M+1}\), where the required preceding gap \(2\) excludes one of the two possible right extensions. It also cannot contain three or more \(b\)'s. Three \(b\)'s followed by \(a^M\) require length at least \(3M+4\); equality forces internal gaps \((0,1)\) or \((1,0)\), neither permitting both right extensions, by \(\mathcal G_3\). Four \(b\)'s are even longer.

Hence the right-special factors have exactly two \(b\)'s. They are **precisely**
\[
A_t=a^t b a^M b a^{M+1},\quad
B_t=a^t b a^{M+1} b a^M,\quad
C_t=a^{t-1}b a^{M+2}b a^M,
\]
with \(A_t,C_t\) present for \(1\le t\le M+1\) and \(B_t\) present exactly for \(1\le t\le M\). To check this exhaustively, write a candidate as \(a^x b a^{M+g}b a^{M+r}\), where \(r\in\{0,1\}\), \(g\in\{0,1,2\}\), and \(x=t+1-g-r\). When \(r=0\), a following \(b\) requires the *next* gap \(0\), so \(g\in\{1,2\}\); the two available right continuations follow from triples \((2,1,0),(0,1,2)\) for \(g=1\), and \((0,2,0),(0,2,1)\) for \(g=2\). For \(g=1\), at \(t=M+1\) the initial \(a\)-run has length \(M+1\), ruling out the necessary \((0,1,2)\) witness, and no alternate triple supplies both extensions. When \(r=1\), the next gaps \(1\) and \(2\) are required, which forces \(g=0\); triples \((1,0,1),(1,0,2)\) realize them even at \(t=M+1\). There are no other possibilities. As every binary right-special factor contributes one to the first difference of factor complexity, this proves
\[
p_M(n+1)-p_M(n)=\begin{cases}3,&1\le t\le M,\\2,&t=M+1.\end{cases}
\]
Together with the base counts, telescoping gives \(p_M(N+t)=3M+7+3t\) throughout \(1\le t\le M+1\).

**4. Palindromic factors.** For \(1\le t\le M+1\), a length-\(N+t\) palindrome can have only two occurrences of \(b\). There are no zero-\(b\) factors; a centered one-\(b\) factor of these lengths either has impossible parity or requires the forbidden consecutive gap pair \((2,2)\); a centered three-\(b\) factor would have equal successive internal gaps; and four \(b\)'s require length at least \(3M+5\). If the internal two-\(b\) gap is \(g\in\{0,1,2\}\), the two exterior \(a\)-runs must both have length
\[
x=(M+1+t-g)/2.
\]
The triples \((1,0,1),(0,1,2),(0,2,0)\) show that every choice with integral \(x\) is attained (using \((0,1,2)\) for \(g=1\) when \(t\le M\)). Thus there are two palindrome choices when \(M+t\) is odd and one otherwise.

At the next length \(3M+5\), there are no palindromes. A centered two-\(b\) factor would require internal gap \(g=1\) and exterior runs of length \(M+1\), which would require a gap triple \((r,1,s)\) with both \(r,s\ge1\); the catalogue has none. Three \(b\)'s would require equal adjacent gaps. A palindrome with four \(b\)'s would need a triple \((0,1,0)\) of internal gaps to fit, which does not occur; the other cases are excluded by length.

**5. Deficit and consequence.** At \(n=N\) the complexity increment is \(4\), while \(P_M(N)+P_M(N+1)=4\). For \(n=N+t\), \(1\le t\le M\), the increment is \(3\), and adjacent palindrome counts sum to \(3\). At \(t=M+1\), the increment is \(2\), with palindrome counts \(2\) and \(0\). In every case \(T_M(n)=2\). Reversal closure of the factor language, established in the cited source, permits the Brlek–Reutenauer identity \(2D(\mathbf u_M)=\sum_{n\ge0}T_M(n)\) with nonnegative summands. Its \(M+2\) exhibited contributions therefore yield \(D(\mathbf u_M)\ge M+2\).

## Verification

The standalone program `verify_gap_catalog.py` checks the gap catalogue exactly using the four substituted two-letter blocks and prints its full list. The independent `verify_factors.py` computes all factors from the four length-\(32\) substituted two-letter blocks and checks every claimed equation for \(1\le M\le35\). For every \(M\ge1\), a transformed length-\(32\) substituted letter block has length \(16(M+2)>3M+5\), so the four block-pair method is exact for each checked \(M\), rather than a finite-prefix approximation. The all-\(M\) proof is the symbolic case analysis above, not extrapolation from \(35\) cases.

## Relationship to prior work

Kim and Kwon, arXiv:2609.16596v1 (September 15, 2026), prove the universal low-factor-complexity equality theorem and show \(T_M(2M+3)=2\) for the stretched Thue–Morse family. Their full Sections 4–5 state the initial-scale count, but not the persistence interval or the explicit right-special classification above. The previously known Brlek–Reutenauer defect identity is used only for the final lower-bound corollary. The new content is the full growing interval \(2M+3\le n\le3M+4\) with its exact complexity and palindromic profiles.

## Limitations

The interval is a guaranteed plateau, not asserted to be maximal. The theorem gives only a lower bound on the total palindromic defect and makes no claim of exact defect or a complete profile at larger lengths. No independent mathematical audit has been performed.

## References

1. D. H. Kim and S. Kwon, *On the number of palindromic factors of low complexity words*, arXiv:2609.16596v1 (first submitted September 15, 2026), Sections 1, 4 and 5. https://arxiv.org/html/2609.16596
2. L. Balková, E. Pelantová and Š. Starosta, work on the Brlek–Reutenauer conjecture, as referenced in Kim–Kwon, Section 5. The identity \(2D=\sum_n T(n)\) is used in its established reversal-closed form.
