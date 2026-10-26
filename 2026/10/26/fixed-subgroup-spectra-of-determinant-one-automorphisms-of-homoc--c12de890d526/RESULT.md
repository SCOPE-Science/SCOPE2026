# Fixed-subgroup spectra of determinant-one automorphisms of homocyclic rank-two groups
## Finding
Let \(p\) be any prime and \(a\ge1\) an integer. For the determinant-one automorphism group \(H=\operatorname{SL}_2(\mathbb Z/p^a\mathbb Z)\), the fixed subgroups have a complete, exact isomorphism-type distribution as follows. Write \(C_{p^0}=1\), \(s=p(p^2-1)\), and \(v=p(p^2-p-1)\). For \(0\le i\le j\le a\), set \(N_{p,a}(i,j)=|\{T\in H:\ker(T-I)\cong C_{p^i}\oplus C_{p^j}\}|\). Then
\[
N_{p,a}(i,j)=
\begin{cases}
v p^{3(a-1)},& i=j=0,\\
(p^2-1)(p-1)p^{3(a-i-1)-(j-i)},&0\le i<j<a,\\
(p^2-1)p^{2(a-i-1)},&0\le i<j=a,\\
p^2(p-1)p^{3(a-i-1)},&1\le i=j<a,\\
1,&i=j=a.
\end{cases}
\]
In particular, all these profiles occur, and their counts sum to \(s p^{3(a-1)}=|H|\). The number \(R(T)\) of Reidemeister classes equals \(|\ker(T-I)|=p^{i+j}\).

For fixed \(t\ge0\) and every \(a>t\), the probability that \(\log_pR(T)=t\) is exactly the coefficient of \(z^t\) in
\[
F_p(z)=\frac{v}{s}+\frac{(p^2-1)(p-1)}s\frac{z}{p-z}\frac1{1-z^2/p^3}+\frac{p^2(p-1)}s\frac{z^2}{p^3-z^2}.
\]
The coefficients of \(F_p\) form a probability distribution. Hence \(\log_pR(T)\) converges in distribution, with mean \(F_p'(1)=p^2(p^2+p+2)/((p-1)^2(p+1)(p^2+p+1))\). The full fixed-subgroup profile is finer than the Reidemeister number.

## Assumptions and scope
The ground group is \(G=(\mathbb Z/p^a\mathbb Z)^2\); the chosen automorphisms preserve the standard alternating area form, equivalently have determinant one. This is not a statement about the entire group \(\operatorname{GL}_2\) or higher-rank automorphisms. All primes, including \(p=2\), and all exponents \(a\ge1\) are included. The finite cyclic factor \(C_1\) denotes the trivial group.

## Proof
**Smith invariant reduction.** Let \(R=\mathbb Z/p^a\mathbb Z\), \(T\in H\), and \(B=T-I\). The Smith diagonal of \(B\) over the chain ring \(R\) is \(\operatorname{diag}(p^i,p^j)\), with \(0\le i\le j\le a\) and \(p^a=0\); this follows by choosing a matrix entry of minimum valuation as pivot and eliminating its row and column, then using divisibility for the second pivot. Its kernel is \(C_{p^i}\oplus C_{p^j}\), establishing the interpretation of the indices. The group \(H\) has cardinality \(s p^{3(a-1)}\) because every element of \(\operatorname{SL}_2(\mathbb F_p)\) has \(p^{3(a-1)}\) lifts.

**The \(i=0\) layer.** For \(T\in\operatorname{SL}_2(\mathbb F_p)\), \(\det(T-I)=2-\operatorname{tr}(T)\). There are exactly \(p^2\) trace-two matrices: they are \(I+N\), for the \(p^2\) nilpotent \(2\)-by-\(2\) matrices \(N\), including zero. It follows that exactly \(v=s-p^2\) residual matrices have \(T-I\) invertible, giving the first formula after lifting. The remaining nonidentity unipotents, exactly \(p^2-1\), have a rank-one \(T-I\) modulo \(p\). For each such residue, at least one off-diagonal entry of \(T\) is nonzero. Assuming its upper-right entry is a unit (the other case is symmetric), parametrizing \(T=\begin{psmallmatrix}x&y\\z&w\end{psmallmatrix}\) with \(z=(xw-1)/y\) shows that the trace \(x+w\) is uniform among its \(p^{a-1}\) lifts of the fixed residual trace. Thus the second Smith exponent is precisely the truncated valuation of \(2-\operatorname{tr}(T)\), giving for \(1\le j<a\) the count \((p^2-1)(p-1)p^{3(a-1)-j}\), and at \(j=a\) the count \((p^2-1)p^{2(a-1)}\). These are the asserted cases with \(i=0<j\).

**Higher valuation layers.** Fix \(1\le i<a\) and write \(T=I+p^i C\), where \(C\) is a matrix modulo \(p^{a-i}\), not identically zero modulo \(p\). Put \(k=a-i\). The determinant-one condition becomes
\[
\operatorname{tr}(C)+p^i\det(C)\equiv0\pmod{p^k}.
\]
Writing \(C=\begin{psmallmatrix}x&y\\z&w\end{psmallmatrix}\), solve uniquely
\[
w=\frac{-x+p^i yz}{1+p^i x}\pmod{p^k}.
\]
Hence \(x,y,z\) range independently over \(\mathbb Z/p^k\mathbb Z\), and modulo \(p\), the matrix \(C\) is traceless. Of all \(p^3\) traceless residual matrices, exactly \(p^2\) are singular: zero and the \(p^2-1\) nonzero nilpotents. Thus \(p^2(p-1)\) are invertible. These give \(j=i\), with \(p^{3(k-1)}\) lifts, proving the diagonal count.

For the \(p^2-1\) nonzero nilpotent residual matrices, note the exact identity
\[
\det C=-\frac{x^2+yz}{1+p^i x}.
\]
At a nonzero traceless nilpotent residual matrix at least one of \(y,z\) is a unit. The polynomial \(x^2+yz\) therefore varies bijectively as that unit's partner varies, so \(\det C\) is uniformly distributed over the \(p^{k-1}\) residues divisible by \(p\), conditional on each such residue matrix. Consequently, for \(i<j<a\), the proportion with second exponent \(j\) is \((p-1)/p^{j-i}\), and for \(j=a\) it is \(p^{-(k-1)}\). Multiplying by \((p^2-1)p^{3(k-1)}\) yields the two remaining formulas. Finally \(T=I\) is the unique case \(i=j=a\). The counting arguments partition every \(T\in H\) exactly once.

**Stabilized law.** For a fixed \(t<a\), the boundary cases \(j=a\) are impossible. After dividing all other counts by \(s p^{3(a-1)}\), the \(i=0\) mass at \(t=0\) equals \(v/s\), each off-diagonal pair \(0\le i<j\) has mass \((p^2-1)(p-1)p^{-(2i+j)}/s\), and each \(1\le i=j\) has mass \(p^2(p-1)p^{-3i}/s\). Summing these geometric series yields \(F_p(z)\). Direct substitution gives \(F_p(1)=1\); all coefficients are nonnegative. Because coefficients stabilize exactly and have total limiting mass one, the laws converge (indeed in total variation) to \(F_p\). Differentiating the rational function gives the displayed mean.

## Verification
The standalone program `verify_sl2_profiles.py` enumerates all determinant-one matrices for seven small prime-power rings. It computes the Smith invariants directly from entries and the determinant and checks the complete formula. For five configurations, it additionally enumerates the fixed subgroup itself, computes its subgroups annihilated by powers of \(p\), and reconstructs invariant factors independently. The recorded output is `verification_output.txt`. Across all configurations, the program verifies \(4302\) determinant-one automorphisms, including \(1110\) independently reconstructed fixed subgroups. The infinite assertion follows from the proof, not the finite checks.

## Relationship to prior work
Senden determines the Reidemeister **spectrum**, namely which fixed-point cardinalities are possible, for arbitrary finite abelian groups; his paper does not provide this determinant-one fixed-subgroup multiplicity law. Friedman–Washington's random-matrix cokernel distribution and Cheong–Huang's later polynomial push-forward theorem treat Haar-random matrices with independently distributed entries and condition on their residue. Those results cover analogous unrestricted matrix counts and therefore prohibit claiming the corresponding \(\operatorname{GL}_2\) specialization as independent. They do not directly give the determinant-one joint Smith-type counts here: conditioning on \(\det T=1\) correlates the entries and requires a separate trace-fiber argument. Hassain studies representation theory and congruence subgroups of compact \(\operatorname{SL}_2\); the inspected material does not state this fixed-subgroup counting distribution. Earlier specialized conjugacy-class tables may imply portions of the result indirectly; that remains a priority risk.

## Limitations
This is a rank-two homocyclic and determinant-one result; it does not establish corresponding formulas for arbitrary finite abelian groups, other determinant fibers, or higher ranks. The numerical checks cover finitely many cases and are not a substitute for proof. Published priorities beyond the inspected primary literature may contain equivalent formulas, especially in special-linear congruence-group enumeration. No independent audit is claimed.

## References
- Pieter Senden, *The Reidemeister spectrum of finite abelian groups* (arXiv:2205.15740, first public 2022-05-31), https://arxiv.org/pdf/2205.15740.
- Gilyoung Cheong and Yifeng Huang, *Cohen–Lenstra distributions via random matrices over complete discrete valuation rings with finite residue fields* (arXiv:1812.11728), https://arxiv.org/pdf/1812.11728.
- Gilyoung Cheong and Yifeng Huang, *The cokernel of a polynomial push-forward of a random integral matrix with concentrated residue* (arXiv:2310.09491, first public 2023-10-14), https://arxiv.org/pdf/2310.09491.
- M. Hassain, *Construction of representations of compact special linear groups of degree two* (arXiv:2209.00919), https://arxiv.org/pdf/2209.00919.
