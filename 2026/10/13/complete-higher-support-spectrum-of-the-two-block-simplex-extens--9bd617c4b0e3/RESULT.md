# Complete higher-support spectrum of the two-block simplex extension
## Finding
Let \(m\ge 3\), and let \(\bar C\) be the binary code in Theorem 6.6 of Li--Chen--Jin--Qu obtained from the binary simplex code of dimension \(m\) by adjoining two constant blocks of lengths \(n''\) and \(n'-n''\), where \(n',n''\) are positive even integers, \(n'\equiv 2\pmod 4\), and \(0<n''<n'\). For \(1\le r\le m\), put
\[
B_r=2^m-2^{m-r}
\]
and write \(\genfrac{[}{]}{0pt}{}{a}{b}_2\) for the Gaussian binomial coefficient, interpreted as zero when \(b<0\) or \(b>a\). Then the complete distribution of support sizes of \(r\)-dimensional subcodes of \(\bar C\) is
\[
\begin{array}{c|c}
\text{support size} & \text{number of subcodes}\\ \hline
B_r & \genfrac{[}{]}{0pt}{}{m-2}{r}_2\\
B_r+n'' & \genfrac{[}{]}{0pt}{}{m-1}{r}_2-\genfrac{[}{]}{0pt}{}{m-2}{r}_2\\
B_r+n'-n'' & \genfrac{[}{]}{0pt}{}{m-1}{r}_2-\genfrac{[}{]}{0pt}{}{m-2}{r}_2\\
B_r+n' & \genfrac{[}{]}{0pt}{}{m}{r}_2-2\genfrac{[}{]}{0pt}{}{m-1}{r}_2+\genfrac{[}{]}{0pt}{}{m-2}{r}_2.
\end{array}
\]
If two displayed support sizes coincide, their multiplicities are added. Consequently the complete generalized Hamming-weight hierarchy is
\[
d_r(\bar C)=
\begin{cases}
2^m-2^{m-r},&1\le r\le m-2,\\
2^m-2+\min\{n'',n'-n''\},&r=m-1,\\
2^m-1+n',&r=m.
\end{cases}
\]
Thus the two appended blocks leave every generalized Hamming weight below codimension one equal to the simplex value and change only the top two entries of the hierarchy.

## Assumptions and scope
The code is exactly the Theorem 6.6 construction: a simplex generator has rows \({\bf u}_1,\ldots,{\bf u}_m\), the first appended block has column type \(e_1+e_2\) repeated \(n''\) times, and the second appended block has column type \(e_1\) repeated \(n'-n''\) times. The statement concerns Hamming supports of linear subcodes over \(\mathbb F_2\). It does not assert any new self-orthogonality or minimality criterion; those properties are premises supplied by the source construction.

## Proof
Identify coefficient vectors for the generator rows with \(\mathbb F_2^m\). The simplex block contains one copy of every nonzero column vector in \(\mathbb F_2^m\). If \(U\le \mathbb F_2^m\) has dimension \(r\), a simplex coordinate indexed by a nonzero vector \(v\) is absent from the support of the corresponding subcode exactly when \(u\cdot v=0\) for every \(u\in U\), equivalently \(v\in U^\perp\). Since \(U^\perp\) contains \(2^{m-r}-1\) nonzero vectors, every \(r\)-subcode has exactly
\[
(2^m-1)-(2^{m-r}-1)=B_r
\]
supported coordinates in the simplex block.

The first appended block is governed by the linear functional \(\ell_1(a)=a_1+a_2\), while the second is governed by \(\ell_2(a)=a_1\). Put
\[
H_1=\ker \ell_1,\qquad H_2=\ker \ell_2,\qquad K=H_1\cap H_2.
\]
Then \(H_1,H_2\) are distinct hyperplanes and \(K\) has dimension \(m-2\). The first appended block contributes nothing exactly when \(U\subseteq H_1\); the second contributes nothing exactly when \(U\subseteq H_2\). Hence the four support patterns are classified by whether \(U\) lies in both, exactly one, or neither hyperplane.

There are \(\genfrac{[}{]}{0pt}{}{m-2}{r}_2\) subspaces contained in \(K\). For either fixed hyperplane there are \(\genfrac{[}{]}{0pt}{}{m-1}{r}_2-\genfrac{[}{]}{0pt}{}{m-2}{r}_2\) subspaces contained in that hyperplane but not in \(K\). Inclusion--exclusion leaves
\[
\genfrac{[}{]}{0pt}{}{m}{r}_2-2\genfrac{[}{]}{0pt}{}{m-1}{r}_2+\genfrac{[}{]}{0pt}{}{m-2}{r}_2
\]
subspaces contained in neither hyperplane. Adding the corresponding block lengths gives the stated complete spectrum.

For \(r\le m-2\), an \(r\)-subspace can be chosen inside \(K\), so the minimum support is exactly \(B_r\). For \(r=m-1\), containment in \(K\) is impossible; the two special hyperplanes \(H_1\) and \(H_2\) activate respectively only one appended block, so the minimum is \(B_{m-1}+\min\{n'',n'-n''\}\). For \(r=m\), the only subcode is the whole code and all \(2^m-1+n'\) coordinates are supported.

## Verification
The standalone verifier `verify.py` constructs the simplex generator from all nonzero columns of \(\mathbb F_2^m\), appends the two column types from Theorem 6.6, enumerates every subspace of the coefficient space for two independent examples, and compares the exact support spectrum with the formula above. For \((m,n',n'')=(3,6,2)\), it obtains
\[
r=1:\ \{4:1,6:2,8:2,10:2\},\quad
r=2:\ \{8:1,10:1,12:5\},\quad
r=3:\ \{13:1\},
\]
so the hierarchy is \((4,8,13)\). Its \(r=1\) distribution exactly reproduces the source's Example 6.7 weight enumerator. For \((m,n',n'')=(4,10,4)\), the verifier obtains hierarchy \((8,12,18,25)\), and its \(r=1\) distribution exactly reproduces Example 6.8. The replay terminates with `VERIFY_OK`.

## Relationship to prior work
Li--Chen--Jin--Qu determine the ordinary weight distribution of this family in Theorem 6.6 and Table VIII; that is precisely the \(r=1\) layer of the spectrum above. Their Examples 6.7 and 6.8 provide independent finite checks of that layer. The source does not state generalized Hamming weights or higher-dimensional support multiplicities for this family.

The classical simplex contribution \(B_r=2^m-2^{m-r}\) is standard. Qiao--Du determine weight hierarchies for a different defining-set family of few-weight binary codes, and Meng--Liu--Liu--Wang--Zheng determine weight hierarchies for two different defining-set self-orthogonal families. Those results motivate the invariant but do not cover the repeated two-functional extension here. A distinct recent systematic-simplex family generated by \([I_m\mid S_2(m)]\) has a different appended block and a different higher-support formula; it does not imply the four-pattern hyperplane spectrum above.

## Limitations
The theorem is specific to the two repeated appended column types in Theorem 6.6. It does not classify arbitrary extensions of simplex codes, arbitrary self-orthogonal few-weight codes, or generalized weights for the later bent-function family in the same source. No claim is made that the ordinary weight distribution alone determines the higher-support spectrum.

## References
1. K. Li, H. Chen, W. Jin, L. Qu, *Characterization and constructions of binary self-orthogonal singly-even linear codes*, arXiv:2507.12240v1, first public 2025-07-16; later published as *Constructions of binary self-orthogonal singly-even wide minimal linear codes with few weights*, Designs, Codes and Cryptography 94, article 186 (2026), doi:10.1007/s10623-026-01921-y. See Theorem 6.6, Table VIII, and Examples 6.7--6.8.
2. X. Qiao, X. Du, *Weight distributions and weight hierarchies of a class of binary linear codes with a few weights*, Advances in Mathematics of Communications 19 (2025), 245--258, doi:10.3934/amc.2023056.
3. K. Meng, C. Liu, H. Liu, X. Wang, D. Zheng, *The weight distributions and weight hierarchies of two classes of self-orthogonal codes*, Advances in Mathematics of Communications 23 (2026), 127--145, doi:10.3934/amc.2026016.
4. V. K. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory 37 (1991), 1412--1418, doi:10.1109/18.133259.
