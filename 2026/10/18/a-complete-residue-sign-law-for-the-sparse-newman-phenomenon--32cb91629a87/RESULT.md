# A complete residue-sign law for the sparse Newman phenomenon

## Finding
For an integer \(n\geq0\), let \(\epsilon_j(n)\in\{0,1\}\) denote its binary digits, and put
\[
\tau(n)=(-1)^{\sum_{j\geq0}\epsilon_j(n)},\qquad
\alpha(n)=\sum_{j\geq0}(-1)^j\epsilon_j(n).
\]
For an odd integer \(q=2h+1\geq3\), a residue \(r\in\mathbb Z/q\mathbb Z\), and \(N\geq0\), write
\[
D_q(r,N)=\sum_{0\leq n<N\atop \alpha(n)\equiv r\pmod q}\tau(n),\qquad
d_q(r)=\min\{\bar r,q-\bar r\},
\]
where \(\bar r\in\{0,\ldots,q-1\}\) represents \(r\). Then
\[
\boxed{(-1)^{d_q(r)}D_q(r,N)\geq0\quad(q\geq3\text{ odd},\;r\bmod q,\;N\geq0).}
\]
Moreover \(D_q(0,N)>0\) for **every** \(N\geq1\).

Consequently, if \(b\geq2\) is an even integer, \(q\geq3\) is any odd divisor of \(b+1\), and \(A_b\) is the set of nonnegative integers with only digits \(0,1\) in base \(b\), then for every real \(X>0\),
\[
(-1)^{d_q(r)}\sum_{\substack{m\in A_b,\;0\leq m<X\\m\equiv r\pmod q}}(-1)^{s_b(m)}\geq0,
\quad\text{and the sum at }r=0\text{ is strictly positive}.
\]
Here \(s_b(m)\) is the ordinary base-\(b\) digit sum. Thus the even-digit-count majority at multiples of \(b+1\) holds at **every** positive cutoff, not just eventually; additionally every other residue possesses a fixed nonnegative or nonpositive bias determined solely by its distance to zero.

## Assumptions and scope
All sums are finite, and all statements quantify over arbitrary odd \(q\geq3\), all residues, and all integer prefixes. There is no asymptotic assumption. The base-\(b\) corollary assumes \(b\) even and \(q\mid b+1\), so \(q\) is odd and \(b\equiv-1\pmod q\). A zero value for a nonzero residue is permitted; the zero-residue bias is always strictly positive for a nonempty prefix.

## Proof
Fix \(q=2h+1\) and identify residues with \(-h,-h+1,\ldots,h\). For \(k\geq0\), let
\[
G_k(r,N)=\sum_{0\leq n<N\atop \alpha(n)\equiv r\pmod q}\tau(n)
\quad(0\leq N\leq 2^k),\qquad F_k(r)=G_k(r,2^k).
\]
At length zero, \(F_0(0)=1\) and all other entries vanish. The binary high-digit split gives, for \(s=(-1)^{k-1}\) and \(0\leq u\leq 2^{k-1}\),
\[
G_k(r,N)=G_{k-1}(r,N)\ (N\leq2^{k-1}),\qquad
G_k(r,2^{k-1}+u)=F_{k-1}(r)-G_{k-1}(r-s,u),
\]
and hence \(F_k(r)=F_{k-1}(r)-F_{k-1}(r-s)\).

**Complete even blocks.** Write \(F_{2m}(r)=(-1)^{|r|}A_{m,|r|}\) for \(-h\leq r\leq h\). This holds at \(m=0\), where \(A_{0,0}=1\) and other coefficients are zero. A pair of transitions multiplies the vector by \(2I-P-P^{-1}\), where \(P\) cyclically shifts residues by one. Directly at the two ends and in the interior, the coefficients satisfy
\[
\begin{aligned}
A_{m+1,0}&=2A_{m,0}+2A_{m,1},\\
A_{m+1,j}&=A_{m,j-1}+2A_{m,j}+A_{m,j+1}\quad(1\leq j<h),\\
A_{m+1,h}&=A_{m,h-1}+A_{m,h}.
\end{aligned}
\]
Thus all \(A_{m,j}\) are nonnegative and \(A_{m,0}>0\). In particular, for every even length, \(F_{2m}(r)\) has sign \((-1)^{|r|}\), allowing zeros.

**Prefix interval induction.** An interval \([0,z]\) means the closed real interval with endpoints \(0,z\), independently of the sign of \(z\). We establish simultaneously:

(E) At even length \(k=2m\), \(G_k(r,N)\in[0,F_k(r)]\) for every residue and every prefix.

(O) At odd length \(k=2m+1\), for every \(r\ne-h\), \(G_k(r,N)\in[0,F_k(r)]\). At the exceptional residue \(r=-h\), the odd complete-block sum is zero but \(G_k(-h,N)\in[0,F_{2m}(-h)]\).

The base case \(k=0\) is immediate. Assume (E) at even length \(2m\), and append an odd-positioned *highest* binary digit, whose alternating-digit contribution is \(+1\). Except for \(r=-h\), the adjacent residues \(r\) and \(r-1\) have opposite prescribed signs (nonnegative and nonpositive in some order). Therefore the first-half interval \([0,F_{2m}(r)]\) and the second-half interval \(F_{2m}(r)-[0,F_{2m}(r-1)]\) are both contained in \([0,F_{2m}(r)-F_{2m}(r-1)]\), proving (O) for these residues. At the unique seam \(r=-h\), cyclic symmetry gives \(F_{2m}(-h)=F_{2m}(h)\); the two halves instead lie between zero and this common value, and \(F_{2m+1}(-h)=0\), as required.

Conversely assume (O) at length \(2m+1\); the next highest digit contributes \(-1\), so its second half is \(F_{2m+1}(r)-G_{2m+1}(r+1,u)\). For all \(r\) except \(h\) and \(-h\), adjacent odd-block endpoints have opposite signs and the same interval argument proves (E). At \(r=h\), the anomalous next residue is \(-h\), whose prefixes lie between zero and \(F_{2m}(-h)\). The odd complete sums at these sites are
\[
F_{2m+1}(h)=(-1)^h(A_{m,h}+A_{m,h-1}),\quad F_{2m+1}(-h)=0,\quad F_{2m}(-h)=(-1)^hA_{m,h}.
\]
The first half lies in \([0,F_{2m+1}(h)]\); subtracting any point in \([0,(-1)^hA_{m,h}]\) from \(F_{2m+1}(h)\) stays in that same interval. At \(r=-h\), the first half is in \([0,(-1)^hA_{m,h}]\), while the second half is the negative of a prefix at \(-h+1\), which ranges over \([0,(-1)^{h-1}(A_{m,h-1}+A_{m,h})]\). Both halves thus lie in \([0,(-1)^h(A_{m,h-1}+A_{m,h})]\), precisely \([0,F_{2m+2}(-h)]\). This proves (E) at the next even length and closes the induction.

Every arbitrary prefix of binary integers is represented by \(G_k(r,N)\) for sufficiently large \(k\). (E) and (O), together with the endpoint sign formulas, yield \((-1)^{|r|}G_k(r,N)\geq0\) for every residue, including \(-h\). To prove strict positivity at zero, induct on \(k\) and the two halves: prefixes \(N\leq2^{k-1}\) inherit strict positivity from the lower level; for larger prefixes, \(G_k(0,N)=F_{k-1}(0)-G_{k-1}(-s,u)\), where \(F_{k-1}(0)>0\) and \(G_{k-1}(-s,u)\leq0\) by the proven sign law. The initial nonempty prefix is \(G_0(0,1)=1\).

Finally the increasing map from binary digit words to base-\(b\) digit words, \(\sum_j\epsilon_j2^j\mapsto\sum_j\epsilon_jb^j\), takes every cutoff in \(A_b\) to a consecutive prefix of binary words; it preserves digit parity. Since \(b\equiv-1\pmod q\), it also takes the base-\(b\) residue to \(\alpha(n)\pmod q\). The preceding statement transfers to every real \(X>0\).

## Verification
The accompanying standalone `check_newman.py` verifies the complete-vector recurrence, every residue-sign inequality at every finite prefix of lengths at most twelve for all odd moduli from \(3\) to \(31\), and complete-block inequalities to length \(119\) for eight moduli. The exact run checked \(122{,}865\) individual finite prefixes; all assertions passed. These finite checks are corroboration rather than substitutes for the interval induction above. The exceptional seam and the case \(q=3\) are included in both the proof and tests.

## Relationship to prior work
Newman established perpetual positivity for ordinary binary multiples of \(3\). Drmota and Stoll, *Newman's phenomenon for generalized Thue–Morse sequences* (2008), establish sharp residue statements in the ordinary sequence for modulus \(3\) and investigate unrestricted base-\(g\) digit expansions. Those are different sampling families from sparse base-\(b\) \(0/1\)-digit sets. Somu, *On Newman's phenomenon in higher bases* (arXiv:1511.03236, 10 November 2015), treats exactly these sparse digit sets and proves eventual positivity for certain moduli; the present result strengthens its odd-divisor-of-\(b+1\) case to every positive cutoff and simultaneously resolves the sign of every residue. The odd-modulus alternating binary digit-sum formulation is intrinsic, independent of the base. Neither inspected primary statement gives this uniform all-prefix residue classification.

## Limitations
The method proves a sign law, not a numerical lower growth estimate or a complete classification of equality at nonzero residues. Even moduli and moduli not dividing \(b+1\) are not addressed by the sparse-base corollary. An equivalent formulation outside the inspected literature remains a priority risk; self-review is not an independent audit.

## References
1. S. T. Somu, *On Newman's phenomenon in higher bases*, arXiv:1511.03236v1, first public 10 November 2015. https://arxiv.org/abs/1511.03236
2. M. Drmota and T. Stoll, *Newman's phenomenon for generalized Thue–Morse sequences*, Discrete Mathematics 308 (2008), 1191–1208. https://www.dmg.tuwien.ac.at/drmota/newman.pdf ; DOI:10.1016/j.disc.2007.03.069
3. M. Drmota and M. Skałba, *Rarified sums of the Thue–Morse sequence*, Transactions of the American Mathematical Society 352 (2000), 609–642. DOI:10.1090/S0002-9947-99-02295-4
