# Dyadic \(3\)-Abelian stability and uniform refinement in the regular paperfolding word

## Finding

Let \(f=f_0f_1\cdots\) be the regular binary paperfolding word defined by \(f_0=0\), \(f_{2t}=t\bmod2\), and \(f_{2t+1}=f_t\) for all integers \(t\ge0\). Two words are \(r\)-Abelian equivalent when all their contiguous factors of lengths at most \(r\) have the same multiplicities. Denote by \(\mathcal P_f^{(r)}(n)\) the number of equivalence classes among **all** length-\(n\) contiguous factors of the infinite word \(f\).

**Theorem.** For every integer \(k\ge5\),
\[
\mathcal P_f^{(3)}(2^k)=36.
\]
At the preceding dyadic length, \(\mathcal P_f^{(3)}(16)=32\). For each \(k\ge5\), all twelve \(2\)-Abelian classes at length \(2^k\) split into exactly three \(3\)-Abelian classes. At length sixteen, ten \(2\)-Abelian classes split into three classes and the remaining two into one class. At \(k\ge5\), the 36 classes have exactly twelve classes each with \(2^{k-1}-1\), \(2^{k-1}\), and \(2^{k-1}+1\) ones.

## Assumptions and scope

The word is zero-indexed and is fixed by the recurrence above; equivalently, \(f_t=1\) precisely when the odd part of \(t+1\) is congruent to three modulo four. The alphabet is \(\{0,1\}\), factors are **contiguous**, and equivalence counts multiplicities of **distinct factor words** rather than the number of their occurrences. The theorem concerns infinite-word factors at dyadic lengths, not just factors seen in a bounded prefix. The refinement statement uses the natural implication from \(3\)-Abelian to \(2\)-Abelian equivalence.

## Proof

**1. Exact boundary-state recurrence.** For \(h\ge1\) and \(s\ge0\), put
\[
\delta_h(s)=\sum_{i=s}^{s+2^h-1}f_i-2^{h-1},\qquad
T_h=\{(\delta_h(s),f_s,f_{s+2^h-1},s\bmod2):s\ge0\}.
\]
The eight states of \(T_1\) are exactly \((x+y-1,x,y,p)\) with \(x,y,p\in\{0,1\}\). The following starting indices witness all eight states, in the order \((x,y,p)=(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1)\):
\[
0,\ 3,\ 4,\ 1,\ 2,\ 11,\ 10,\ 5.
\]
The defining recurrence separates a length-\(2^{h+1}\) factor starting at an even or an odd index into a fixed alternating parity sequence and a length-\(2^h\) factor. For \(h\ge1\) the former has exactly \(2^{h-1}\) ones. Thus, writing \((d,x,y,p)\) for a state,
\[
T_{h+1}=
\{(d,p,y,0):(d,x,y,p)\in T_h\}
\cup\{(d,x,p,1):(d,x,y,p)\in T_h\}.
\tag{1}
\]
This is an equality, since every starting index is even or odd and every smaller starting index occurs. Iterating gives \(|T_1|=8\), \(|T_2|=16\), \(|T_3|=20\), and
\[
T_4=\{-1,0,1\}\times\{0,1\}^3.
\]
The full set on the right is fixed by (1), so \(T_h=T_4\) for all \(h\ge4\). In particular, every possible dyadic ones-count deviation is one of \(-1,0,1\).

**2. Four-block reduction of length-three frequencies.** Fix \(k\ge4\), put \(m=2^{k-2}\), and consider a factor beginning at \(4j+r\), where \(0\le r\le3\). Let \(e=j\bmod2\). The consecutive four-blocks of \(f\) are exactly
\[
B_j=(0,e,1,f_j),\qquad B_{j+1}=(0,1-e,1,f_{j+1}).
\]
For \(e,b\in\{0,1\}\), let \(Q_a(e,b)\), \(0\le a\le3\), be the following ordered length-three words:
\[
Q_0(e,b)=0e1,\quad Q_1(e,b)=e1b,\quad
Q_2(e,b)=1b0,\quad Q_3(e,b)=b0(1-e).
\]
Here each displayed expression denotes concatenation of the indicated single binary symbols. Write \(\mathbf e_{uvw}\) for the standard basis vector indexed by \(uvw\in\{0,1\}^3\) and put \(H_{e,b}=\sum_{a=0}^3\mathbf e_{Q_a(e,b)}\).

Set \(j=2s+e\), \(h=k-3\), and choose \((d,x,y,p)\in T_h\) from starting index \(s\). The number of ones among odd-indexed \(f_t\) for \(j\le t<j+m\) is \(m/4+d\). Among even-indexed \(f_t\) there are exactly \(m/4\) ones. Consequently, the sum of the four starting-triple vectors over the \(m\) full four-blocks is
\[
B(m,d)=\frac m4\sum_{e,b\in\{0,1\}}H_{e,b}
+d(H_{1,1}-H_{1,0}).
\tag{2}
\]
The first and last block symbols needed for boundary corrections are
\[
(v,z)=(p,y)\quad(e=0),\qquad (v,z)=(x,p)\quad(e=1).
\]
The actual length-\(2^k\) factor has \(2^k-2\) length-three starting positions. Its triple-frequency vector is \(C_3=B(m,d)-R_r\), where the correction vectors are
\[
\begin{aligned}
R_0&=\mathbf e_{Q_2(1-e,z)}+\mathbf e_{Q_3(1-e,z)},\\
R_1&=\mathbf e_{Q_0(e,v)}+\mathbf e_{Q_3(1-e,z)},\\
R_2&=\mathbf e_{Q_0(e,v)}+\mathbf e_{Q_1(e,v)},\\
R_3&=\mathbf e_{Q_1(e,v)}+\mathbf e_{Q_2(e,v)}.
\end{aligned}
\tag{3}
\]
To verify (3), list the possible starting offsets modulo four. For offsets zero, one, and two, deleting the two starting triples outside the factor gives the first three lines. For offset three, the extra starting triple in block \(j+m\) cancels the triple at offset zero in block \(j\), since \(m\) is even and both blocks have the same parity; the last line follows. No unseen symbols enter the calculation.

The last two symbols of the factor are
\[
S_0=(1,z),\quad S_1=(z,0),\quad S_2=(0,e),\quad S_3=(e,1).
\tag{4}
\]
Given the triple counts \(C_3\) and suffix \(S_r\), all two-gram and one-gram counts are uniquely reconstructed by
\[
C_2(uv)=C_3(uv0)+C_3(uv1)+\mathbf1_{\{S_r=uv\}},
\]
\[
C_1(u)=C_2(u0)+C_2(u1)+\mathbf1_{\{\text{last}(S_r)=u\}}.
\tag{5}
\]
Equations (1)--(5) therefore give the **entire** \(3\)-Abelian signature of every length-\(2^k\) factor from a state in \(T_{k-3}\), the parity \(e\), and the offset \(r\). Conversely every such choice occurs: by the definition of \(T_h\), every state has a witnessing starting index, and any \(e,r\) can be used to form a valid factor beginning at \(4(2s+e)+r\). Thus the image of this finite map is exactly the set of signatures for the infinite word.

**3. Exact finite image calculation.** Apply the explicit integer formulas (2)--(5) to all \((d,x,y,p)\in T_h\), both values of \(e\), and all four values of \(r\). Group the resulting signatures by their first six entries (the complete \(2\)-Abelian signature), then count the distinct full fourteen-entry signatures. The complete finite calculation is:

| \(h=k-3\) | \(|T_h|\) | \(2\)-Abelian classes | \(3\)-Abelian classes | sizes of the \(2\)-Abelian fibers |
| --- | ---: | ---: | ---: | --- |
| \(1\) | 8 | 12 | 32 | two fibers of size 1, ten of size 3 |
| \(2\) | 16 | 12 | 36 | twelve fibers of size 3 |
| \(3\) | 20 | 12 | 36 | twelve fibers of size 3 |
| \(\ge4\) | 24 | 12 | 36 | twelve fibers of size 3 |

The final row is one finite computation because \(T_h\) has already stabilized. The standalone `verify_paperfolding_3abelian.py` contains executable formulas for every entry of this table, including its weight-resolved classification. It generates the states using the exact recurrence rather than sampling long words. For \(k\ge5\), the classes split equally among the three allowed ones-count values, each with twelve classes. This proves all assertions.

## Verification

Run `python3 verify_paperfolding_3abelian.py` with a standard Python 3 interpreter. The exact finite-state computation verifies \(|T_h|=8,16,20,24\), enumerates all signature images through \(h=8\), and explicitly confirms that the saturated 24-state case has 36 signatures, with twelve \(2\)-Abelian signatures each refining to exactly three \(3\)-Abelian signatures. The proof of the infinite continuation is the fixed-point identity (1), not extrapolation.

As an independent check, the program generates 32,768 paperfolding bits in two ways (the recursive definition and the odd-part test), computes all factors at dyadic lengths from 16 to 1024, and checks their actual one-, two-, and three-gram frequencies against (2)--(5). It observes the known \(4n\) distinct factors at each of those lengths and verifies equality of the direct and symbolic signature sets. These direct-prefix checks are corroborative; completeness for **all** infinite factors follows from the exact state decomposition in the proof.

## Relationship to prior work

Madill and Rampersad (arXiv:1208.2856, publicly available 2012) proved the regularity and recurrences for the **ordinary Abelian** complexity of the regular paperfolding word. This establishes contextual information at dyadic lengths but does not determine length-three factor multiplicities or \(3\)-Abelian refinements. Parreau, Rigo, Rowland, and Vandomme (arXiv:1405.3532, publicly available 2014) examined the \(2\)-Abelian complexities of the period-doubling and Thue--Morse words and the Abelian complexities of associated block codings. Their general language is relevant, but their results do not imply the present paperfolding \(3\)-Abelian classification. Allouche's general paperfolding factor-complexity result, independently tabulated as OEIS A337120, concerns the number of distinct factors without Abelian identification. Thus an ordinary-factor count of \(4n\), or a dyadic \(2\)-Abelian class count of twelve, does not determine the additional multiplicity refinement proved here.

## Limitations

The theorem treats dyadic lengths \(2^k\) for \(k\ge4\) of the **ordinary** regular paperfolding word. It does not classify non-dyadic lengths, generalized paperfolding instruction sequences, all \(r\)-Abelian complexities, or regularity of the complete \(3\)-Abelian complexity sequence. The proof is self-contained apart from standard definitions; the finite image calculation is small and auditable by the included program. The novelty comparison is based on inspected and discoverable literature and cannot rule out an unpublished or unindexed equivalent theorem.

## References

1. B. Madill and N. Rampersad, *The abelian complexity of the paperfolding word*, arXiv:1208.2856v1 (first posted 2012-08-14), later *Discrete Mathematics* 313 (2013), 831--838. https://arxiv.org/abs/1208.2856.
2. A. Parreau, M. Rigo, E. Rowland, and E. Vandomme, *A new approach to the 2-regularity of the ell-abelian complexity of 2-automatic sequences*, arXiv:1405.3532v1 (2014-05-14), later *Electronic Journal of Combinatorics* 22 (2015), P1.27. https://arxiv.org/abs/1405.3532.
3. J.-P. Allouche, *The number of factors in a paperfolding sequence*, *Bulletin of the Australian Mathematical Society* 46 (1992), 23--32.
4. OEIS Foundation, A337120, factor complexity of the regular and generalized paperfolding sequences. https://oeis.org/A337120.
