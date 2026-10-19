# A Catalan substitution law for subsequence universality of Dyck words

## Finding

Let \(\mathcal D_n\) be the set of Dyck words with \(n\) zeros and \(n\) ones: every prefix has at least as many zeros as ones. For \(w\in\mathcal D_n\), let \(I(w)\) be the largest integer \(k\) such that every binary word of length \(k\) occurs as an order-preserving (not necessarily consecutive) subsequence of \(w\). Set
\[
A_{n,k}=|\{w\in\mathcal D_n:I(w)=k\}|,
\qquad H(t,u)=\sum_{n,k\ge0}A_{n,k}t^nu^k.
\]
Then \(H\) is the unique formal power series with constant term one satisfying
\[
\boxed{(1-t)(H-1)=tu(1-tu)H^2.}
\]
Equivalently, writing \(C_j=\frac1{j+1}\binom{2j}{j}\) for the Catalan numbers,
\[
\boxed{H(t,u)=\sum_{j\ge0}C_j\left(\frac{tu(1-tu)}{1-t}\right)^j.}
\]
For every \(n\ge k\ge1\) this yields the explicit exact formula
\[
\boxed{A_{n,k}=\sum_{j=\lceil k/2\rceil}^{k}(-1)^{k-j}C_j\binom{j}{k-j}\binom{n-k+j-1}{j-1}.}
\]
Also \(A_{0,0}=1\), while \(A_{n,0}=0\) for \(n\ge1\), and \(A_{n,k}=0\) for \(k>n\). For each fixed positive \(k\), \(A_{n,k}\) is exactly a polynomial in \(n\) on all integers \(n\ge k\), of degree \(k-1\) with leading coefficient \(C_k/(k-1)!\). In particular,
\[
A_{n,k}=\frac{C_k}{(k-1)!}\,n^{k-1}+O_k(n^{k-2})
\quad (k\ge2,\ n\to\infty),
\]
while \(A_{n,1}=1\) for every \(n\ge1\).

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). Zero is an opening step and one a closing step. The empty word is in \(\mathcal D_0\) and has index zero. Counts distinguish linear words, not cyclic rotations. All generating functions are formal power series in \(t,u\) with integer coefficients; no analytic convergence is assumed. The result covers all pairs of nonnegative integers \((n,k)\) under these conventions. It makes no claim about multiple parenthesis types, arbitrary balanced binary words that dip below zero, or gap-constrained subsequences.

## Proof

**Greedy arches and the index.** Scan a binary word from left to right, remembering whether the unfinished block has seen no letter, only zero, or only one. When the other letter arrives, close the shortest block containing both letters, increase a counter by one, and reset to the state with no seen letter. The counter is exactly \(I(w)\). Indeed, choosing the requested next symbol from each of \(k\) complete blocks embeds every binary length-\(k\) pattern. Conversely, if there are exactly \(k\) complete blocks, concatenate their respective last letters and then a letter absent from the leftover suffix. This length-\((k+1)\) pattern is absent: its first required letter cannot occur before the end of the first block, and the same greedy earliest-occurrence reasoning inductively forces the \(j\)-th required letter to be at or after the end of block \(j\); the final missing letter cannot be found in the suffix. This is the standard arch characterization, also recorded in Adamson (2023, Theorem 2.4).

**Weighted three-state transitions.** Order the memory states as \(E\) (empty), \(Z\) (zero already seen), and \(O\) (one already seen). Give a factor \(u\) to each transition closing an arch. The matrices for reading zero and one, respectively, are
\[
L=\begin{pmatrix}0&1&0\\0&1&0\\u&0&0\end{pmatrix},
\qquad
R=\begin{pmatrix}0&0&1\\u&0&0\\0&0&1\end{pmatrix}.
\]
Each matrix entry records the weight of a deterministic state transition; product weights count complete arches. Let \(M(t,u)\) be the sum of the weighted transition matrices of all Dyck words, with \(t\) for each opening-closing pair. The unique first-return decomposition \(w=0v1s\), for \(v,s\) Dyck, gives the identity
\[
M=\mathbf 1+tLMRM.
\]
The first symbol of every nonempty Dyck word is zero and its last is one. Therefore the first two rows of \(M-\mathbf1\) agree and its column corresponding to memory state \(Z\) is zero. Write
\[
M=\begin{pmatrix}1+a&0&b\\a&1&b\\c&0&1+d\end{pmatrix}.
\]
Multiplying the displayed matrices gives, exactly,
\[
\begin{aligned}
a&=t\big((a+b)c+u(a+1)\big),\\
b&=t\big((a+b)d+a+(u+1)b\big),\\
c&=tu(a+b+1)c,\\
d&=tu(a+b+1)(d+1).
\end{aligned}
\]
Since \(1-tu(a+b+1)\) has formal constant term one, the equation for \(c\) forces \(c=0\). Therefore \(a=tu/(1-tu)\). The sought generating function is the sum of the first row of \(M\), namely \(H=1+a+b\), because the scan begins in state \(E\). The last equation gives
\[
d=\frac{tuH}{1-tuH}.
\]
Inserting \(b=H-1/(1-tu)\), this expression for \(d\), and \(a=tu/(1-tu)\) into the equation for \(b\), then clearing the formal-series units, gives
\[
(1-t)(H-1)-tu(1-tu)H^2=0.
\]
All operations are valid in \(\mathbb Z[u][[t]]\). The equation determines each positive-degree coefficient of \(H\) from lower degrees and the constant term, establishing existence and uniqueness as a formal series.

**Catalan expansion and coefficient extraction.** The Catalan series \(C(x)=\sum_{j\ge0}C_jx^j\) is the unique formal series with constant term one satisfying \(C=1+xC^2\). Substituting \(x=tu(1-tu)/(1-t)\) yields the claimed \(H\). For \(k\ge1\), the coefficient of \(u^k\) in the \(j\)-th summand is zero unless \(\lceil k/2\rceil\le j\le k\). In that range it equals
\[
(-1)^{k-j}C_j\binom{j}{k-j}\frac{t^k}{(1-t)^j}.
\]
Using \([t^{n-k}](1-t)^{-j}=\binom{n-k+j-1}{j-1}\) proves the exact formula. For fixed \(k\ge1\) these binomial coefficients are polynomials in \(n\) of degrees \(j-1\). The unique term with maximal degree comes from \(j=k\), giving the stated leading coefficient. Finally, setting \(u=1\) recovers \(H(t,1)=C(t)\), the classical Catalan count of Dyck words, supplying an independent normalization check.

## Verification

The bundled standard-library program `verify.py` independently constructs the Dyck words up to semilength eight, explicitly tests the presence of every binary subsequence pattern through the corresponding universality index, and compares with the closed formula. An independent height-and-arch-state transfer recurrence checks all coefficients through semilength 27. It also checks the fixed-index Catalan finite differences for \(1\le k\le17\). The program prints `ALL FINITE CHECKS PASSED (infinite proof is in RESULT.md)` upon completion. These finite computations are corroboration, not the justification for the all-length theorem; that justification is the exact formal-matrix derivation above.

For orientation, the index counts for semilengths \(n=1,2,3,4,5,6\), listed in increasing positive index, are respectively \((1)\), \((1,1)\), \((1,3,1)\), \((1,5,7,1)\), \((1,7,18,15,1)\), and \((1,9,34,56,31,1)\). Each row sums to its Catalan number.

## Relationship to prior work

The arch characterization used here is established in work on scattered-factor universality and appears as Theorem 2.4 of Adamson (2023). Adamson (2023) gives counting/ranking algorithms for unrestricted words. Adamson, Fleischmann, Huch, Koß, Manea, and Nowotka (2023) extend counting and ranking to regular languages; the ordinary unbounded-depth Dyck language is not regular, and their finite-automaton theorem does not imply the exact Catalan substitution law without an additional derivation. Mol, Rampersad, and Shallit (2023) analyze Dyck factors of automatic words and their nesting/repetition properties, not the joint universality-index enumeration of all Dyck words. The classical Dyck path count \(C_n\) follows on setting \(u=1\), but does not resolve the refined coefficients. The displayed scalar algebraic identity and its Catalan-leading polynomial coefficients are the contribution assessed here.

## Limitations

The formula is for the one-type Dyck language over two symbols and the ordinary, unconstrained scattered-subsequence relation. The proof is self-contained modulo elementary Catalan enumeration and the standard arch characterization, independently justified above. No claim is made about multi-type Dyck words, first-order corrections to random-index limit laws, or independent validation. A non-indexed or uninspected prior source could contain an equivalent enumeration; literature searches cannot certify absolute novelty.

## References

1. Duncan Adamson, *Ranking and Unranking k-subsequence universal words*, arXiv:2304.04583, first posted 2023-04-10. https://arxiv.org/abs/2304.04583
2. Duncan Adamson, Pamela Fleischmann, Annika Huch, Tore Koß, Florin Manea, Dirk Nowotka, *k-Universality of Regular Languages*, arXiv:2311.10658, first posted 2023-11-17. https://arxiv.org/abs/2311.10658
3. Lucas Mol, Narad Rampersad, Jeffrey Shallit, *Dyck Words, Pattern Avoidance, and Automatic Sequences*, arXiv:2301.06145, first posted 2023-01-15. https://arxiv.org/abs/2301.06145
