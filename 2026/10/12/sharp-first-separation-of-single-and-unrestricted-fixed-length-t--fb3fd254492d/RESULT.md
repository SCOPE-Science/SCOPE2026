# Sharp first separation of single and unrestricted fixed-length tandem-duplication codes

## Finding
For integers \(q\ge2\) and \(k\ge2\), consider words of length \(n\ge k\) over \(\mathbb Z/q\mathbb Z\). A length-\(k\) tandem duplication replaces \(uvw\) by \(uvvw\) whenever \(|v|=k\). Let \(M_q(n;1,k)\) be the largest number of length-\(n\) codewords correcting zero or one such duplication; let \(M_q(n;\infty,k)\) be the largest number correcting any finite number.

Let \(a_{q,k}(s)\) be the number of length-\(s\) words over this alphabet that contain no run of \(k\) consecutive zero symbols. Set \(a_{q,k}(0)=1\). Then
\[
M_q(n;1,k)=M_q(n;\infty,k)\qquad(k\le n\le3k),
\]
and the first strict difference occurs at \(n=3k+1\), where
\[
\begin{aligned}
M_q(3k+1;1,k)&=q^k\bigl(a_{q,k}(2k+1)+a_{q,k}(k+1)+2q-1\bigr),\\
M_q(3k+1;\infty,k)&=q^k\bigl(a_{q,k}(2k+1)+a_{q,k}(k+1)+q\bigr).
\end{aligned}
\]
Their difference is exactly \(q^k(q-1)>0\).

The complete equality classification at \(n=3k+1\) gives exactly
\[
\boxed{\mathcal N_{q,k}=\left[2^{(k-1)(q-1)}
\prod_{w=2}^{k+1}(w+1)^{\binom{k+1}{w}(q-1)^w}\right]^{q^k}}
\]
labeled optimal codes, where a code means an unordered subset of the fixed labeled word space.

For the concrete binary length-seven, length-two-duplication instance,
\[
M_2(7;1,2)=84,\qquad M_2(7;\infty,2)=80,
\qquad \mathcal N_{2,2}=2{,}176{,}782{,}336.
\]
For the ternary instance, \(M_3(7;1,2)=1719\) versus \(M_3(7;\infty,2)=1701\).

## Assumptions and scope
All lengths, symbols, and error budgets are literal. Only duplications of exactly \(k\) adjacent symbols are permitted, not those of lengths at most \(k\). Both the unduplicated output of length \(n\) and each output after one duplication (length \(n+k\)) must decode uniquely. The empty sequence of duplications is allowed in the unrestricted-error model.

Define the bijective \(k\)-step derivative
\[
\phi_k(x)=(h,z),\quad h=(x_0,\ldots,x_{k-1}),\quad
z_i=x_{k+i}-x_i\pmod q\quad(0\le i<n-k).
\]
Its inverse reconstructs symbols successively from \(h\) and \(z\). A tandem duplication of exactly \(k\) symbols at site \(i\) preserves \(h\) and inserts \(k\) zero symbols into \(z\) at position \(i\).

For a derivative tail \(z=0^{e_0}b_1 0^{e_1}\cdots b_w0^{e_w}\), all \(b_i\ne0\), write the *irreducible trunk* \(r=0^{e_0\bmod k}b_1\cdots b_w0^{e_w\bmod k}\) and the *zero signature* \(s=(\lfloor e_0/k\rfloor,\ldots,\lfloor e_w/k\rfloor)\). The pair \((h,r)\) is an invariant root. In its fiber of length-\(n\) words the signature runs over nonnegative compositions of \(m=(n-k-|r|)/k\) into \(w+1\) parts, where \(w\) is the number of nonzero symbols of \(r\).

## Proof
**Root separation and local confusability.** Under a duplication the invariant \((h,r)\) stays fixed and one coordinate of the zero signature increases by one. Thus two distinct length-\(n\) words with different roots have disjoint descendant cones, while two words with the same root can produce an identical single-duplication output if and only if their weight-\(m\) signatures have \(\ell_1\)-distance \(2\). Indeed two distinct nonnegative vectors of equal weight have a common one-unit increment precisely when they differ by moving a single unit from one coordinate to another. This criterion is independently checked against literal tandem outputs in the supplied programs.

**Before the boundary.** If \(n\le3k\), the derivative tail has length at most \(2k\). Any root fiber is either of signature weight \(m=0\), a singleton; of weight \(m=1\), consisting of unit vectors that form a clique in the confusability graph; or of weight \(m=2\) with \(r\) empty, whose signature has only one coordinate and again gives a singleton. Hence every root fiber admits exactly one codeword in any maximum single-duplication-correcting code. Different root fibers do not interact, so the maximum equals the number of roots. The same number is the unrestricted-duplication optimum, as established by the classical root separation theorem.

**Boundary fiber types.** At \(n=3k+1\) the derivative tail length is \(2k+1\). Its irreducible trunk can have length only \(2k+1\), \(k+1\), or \(1\). These cases exhaust all possible signature weights.

If \(|r|=2k+1\), then \(m=0\) and its unique word is forced into every maximum. Such trunks number \(a_{q,k}(2k+1)\) per derivative prefix.

If \(|r|=k+1\), then \(m=1\) and a trunk with \(w\) nonzero symbols contributes exactly \(w+1\) possible signatures: all the unit vectors. Every pair is confusable, so each maximum selects exactly one, independently. Such trunks number \(a_{q,k}(k+1)\).

If \(|r|=1\), then either \(r=0\), giving a single signature, or \(r\) is one of the \(q-1\) nonzero symbols, giving the three weight-two signatures
\[
(2,0),\quad(1,1),\quad(0,2).
\]
They form the three-vertex path under one-duplication confusability. Its unique largest independent set consists of the two endpoints, \(\{(2,0),(0,2)\}\). Thus the \(q\) length-one roots contribute exactly \(1+2(q-1)=2q-1\) words per derivative prefix. Different roots and all \(q^k\) prefixes can be optimized independently. Summing proves the asserted one-duplication optimum and shows explicitly that every equality case has precisely the stated fiberwise form.

**Unrestricted optimum and sharp onset.** An unrestricted-duplication-correcting code contains at most one word per root, and every choice of one word per root works. The number of roots at this boundary is \(q^k[a_{q,k}(2k+1)+a_{q,k}(k+1)+q]\), proving the second formula. Subtraction gives \(q^k(q-1)>0\), whereas equality held at all preceding permitted lengths.

**Number of maximizers.** For each fixed derivative prefix, only the \(|r|=k+1\) roots allow discretionary choices. A length-\(k+1\) irreducible trunk with precisely one nonzero symbol can place it in exactly \(k-1\) interior positions, so there are \((k-1)(q-1)\) such trunks, each with two choices. For \(2\le w\le k+1\), every length-\(k+1\) word with exactly \(w\) nonzero symbols is irreducible, giving \(\binom{k+1}{w}(q-1)^w\) trunks, each with \(w+1\) choices. All other root fibers have a unique optimal selection. The choices multiply over trunks and over all \(q^k\) derivative prefixes, proving the displayed formula for \(\mathcal N_{q,k}\).

## Verification
The two supplied dependency-free Python scripts reconstruct literal duplication outputs and root signatures rather than relying on a software library for coding theory. `verify.py` exhaustively checks every word and every within-fiber subset for alphabets \(q=2,3\), duplication length \(k=2\), and all blocklengths \(2\le n\le7\), comparing the two collision predicates and the exact optimizer counts. Its final check reports binary optimum \(84\) with \(2{,}176{,}782{,}336\) labeled maxima, ternary optimum \(1719\), and the first strict gap at length seven.

`verify_general.py` independently recreates all literal channel outputs and every local independent-set problem at the first boundary for \((q,k)=(2,2),(3,2),(2,3),(2,4)\). Its independently checked first-optimum/unrestricted-optimum pairs are \((84,80)\), \((1719,1701)\), \((776,768)\), and \((6928,6912)\), respectively. Exhaustive finite checks provide corroboration only for these sample parameters; the universal theorem follows from the preceding fiber argument.

To rerun, execute `python3 verify.py` and `python3 verify_general.py`. Both scripts are standalone, use only the Python standard library, and print explicit terminal success markers. The complete output is embedded as `verification_output.txt`.

## Relationship to prior work
Jain, Farnoud, Schwartz, and Bruck (arXiv:1606.00397v1, 2016) prove that length-\(k\) tandem duplication is insertion of \(k\) zeros in the derivative, establish optimal *unrestricted*-duplication code sizes by counting roots (their Theorems 15–16), and characterize general bounded-duplication correctness using constant-weight \(\ell_1\) signatures (their Theorem 20). These general reductions and the unlimited-error optimum are prior work and are not claimed as new here. Their later construction discussion does not determine the sharp first finite length at which one-error and unlimited-error optima split, nor the all-alphabet, all-\(k\) optimizer count proved here.

Lenz, Wachter-Zeh, and Yaakobi (arXiv:1707.00052) restate the trunk/signature metric and derive finite bounds by generalized sphere packing, rather than the present threshold and equality classification. Kovačević and Tan (arXiv:1808.10328) establish sharp asymptotic single-duplication behavior, not this finite threshold. Chen and collaborators (arXiv:2003.00483) settle many general constant-weight \(\ell_1\) cases, including weight two, but do not state this cross-fiber first-onset classification or its enumerator.

The closed formulas here synthesize those foundations into a precise structural boundary and a product census of all labeled optimizers. Exact-parameter and equivalent-formulation searches found no published statement providing this sharp universal onset with equality counts.

## Limitations
The theorem concerns exactly one permissible duplication length \(k\ge2\), a code correcting zero or one duplication, and the competing code correcting an arbitrary number; it does not extend as stated to a channel allowing a range of duplication lengths or to substitutions or deletions. The exact first-onset optimizer classification does not claim later-length formulas. Absence from searches cannot establish absolute bibliographic uniqueness: an obscure or unindexed deduction of the same threshold and enumerator remains possible.

## References
1. S. Jain, F. Farnoud, M. Schwartz, and J. Bruck, “Duplication-Correcting Codes for Data Storage in the DNA of Living Organisms,” arXiv:1606.00397v1, first public June 1, 2016 (Theorems 15–16 and 20).
2. A. Lenz, A. Wachter-Zeh, and E. Yaakobi, “Bounds on Codes Correcting Tandem and Palindromic Duplications,” arXiv:1707.00052v1, 2017.
3. M. Kovačević and V. Y. F. Tan, “Asymptotically Optimal Codes Correcting Fixed-Length Duplication Errors in DNA Storage Systems,” arXiv:1808.10328v1, 2018.
4. “Optimal codes with small constant weight in \(\ell_1\)-metric,” arXiv:2003.00483, 2020.
