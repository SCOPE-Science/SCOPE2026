# A depth-three separation of octonary Hadamard Haar endpoint norms from grouped binary Haar norms

## Finding
On the uniform eight-ary probability tree, use the seven real nonconstant Sylvester--Hadamard characters as local Haar contrasts, together with the global constant. Independently change the sign of **each** of these orthonormal basis coefficients, including the constant. The largest induced real \(L^\infty\)-operator norm on the \(8^d\) terminal atoms is
\[
U_8(d)=\frac{15d}{7}+\frac{13}{49}+\frac{36}{49\cdot8^d},\qquad d=0,1,2,\ldots.
\]
The corresponding ordinary dyadic Haar basis on \(2^n\) atoms has
\[
U_2(n)=\frac{2n}{3}+\frac59+\frac49\left(-\frac12\right)^n.
\]
Thus the octonary constant equals the dyadic constant at three times the depth for \(d=0,1,2\), but **strictly exceeds** it for every \(d\ge3\). This is an exact structural distinction between changing the signs of seven eight-child contrasts independently and changing signs of all binary Haar contrasts across three successive dyadic generations. Every terminal atom can serve as a maximizing evaluation point.

## Assumptions and scope
For an integer \(d\ge0\), write \(X_d=(\mathbb F_2^3)^d\), with normalized counting measure. For a finite word \(w\) of length \(j<d\), let \(C_w\) be its cylinder, of mass \(8^{-j}\). For nonzero \(a\in\mathbb F_2^3\), define the normalized contrast
\[
H_{w,a}(x)=8^{j/2}\mathbf 1_{C_w}(x)(-1)^{a\cdot x_{j+1}}.
\]
These \(8^d-1\) contrasts together with \(H_0=1\) form a real orthonormal basis. The operator \(T_\varepsilon f=\varepsilon_0\langle f,1\rangle 1+\sum_{w,a}\varepsilon_{w,a}\langle f,H_{w,a}\rangle H_{w,a}\) has each multiplier in \(\{-1,1\}\). Define \(U_8(d)=\max_\varepsilon\|T_\varepsilon\|_{L^\infty(X_d)\to L^\infty(X_d)}\); the empty-depth convention gives \(U_8(0)=1\). The binary quantity is defined in precisely the same way with the one nonconstant character at every binary split. The theorem is about real, full-generation, uniform trees and a fixed local character basis, not arbitrary orthogonal changes of that basis.

## Proof
**1. Exact row recursion.** The norm of a matrix on the real \(\ell_\infty\) space is its largest absolute row sum. Tree translations by coordinatewise XOR make all rows equivalent for optimization; fix the observation word to be all zero. Only Haar contrasts on the ancestral observation path contribute to its row. At the root, choose signs \(\sigma_a\in\{-1,1\}\) for the seven characters and put
\[
h_y=\sum_{a\ne0}\sigma_a(-1)^{a\cdot y},\qquad y\in\mathbb F_2^3.
\]
For a scalar baseline \(t\), let \(F_d(t)\) be the greatest mean absolute value of the row with baseline \(t\) and all depth-\(d\) signed ancestral contrasts. Then \(F_0(t)=|t|\), and decomposition over the eight first children gives exactly
\[
F_d(t)=\max_{\sigma\in\{-1,1\}^7}
\left\{\frac18\sum_{y\ne0}|t+h_y|+
F_{d-1}\left(\frac{t+h_0}{8}\right)\right\}.
\]
Indeed the deeper contrasts on child zero are multiplied by eight in its conditional kernel, while that child has mass one eighth. The other seven children have no deeper ancestral contributions. Independent signs at descendant nodes make the maximization exact. The global constant has sign \(\pm1\), and symmetry gives \(U_8(d)=F_d(1)\).

**2. The ten local Walsh profiles.** Each \(h_y\) is odd. Up to permutation of the seven values \((h_y)_{y\ne0}\), the 128 possible sign vectors give exactly the following ten triples \((h_0,S,Z)\), where \(S=\sum_{y\ne0}|h_y|\) and \(Z=\sum_{y\ne0}\operatorname{sgn}(h_y)\):

| \(h_0\) | \(S\) | \(Z\) |
|---:|---:|---:|
| -7 | 7 | 7 |
| -5 | 13 | -1 |
| -3 | 15 | 3 |
| -1 | 13 | -5 |
| -1 | 17 | -1 |
| 1 | 17 | 1 |
| 1 | 13 | 5 |
| 3 | 15 | -3 |
| 5 | 13 | 1 |
| 7 | 7 | -7 |

This is an exact finite identity, reproduced by `verify_octonary.py` by enumerating the 128 choices and computing each eight-point Walsh transform. In particular, the profile \((1,17,1)\) is attained by \(\sigma_a=+1\) when the Hamming weight of \(a\) is two or three and \(\sigma_a=-1\) when it is one; the corresponding eight outputs are \(1\) at child zero and a permutation of \((-3,-3,-3,1,1,1,5)\) elsewhere.

**3. The global affine envelope.** Inductively, suppose on \(|t|\le1\) that \(F_{d-1}(t)=A+B|t|\) with \(1/7\le B\le1\). Since every \(h_y\) is an odd nonzero integer and \(|t|\le1\), each \(|t+h_y|=|h_y|+t\operatorname{sgn}(h_y)\), including the boundary points. Furthermore \(|(t+h_0)/8|\le1\). Therefore each of the ten Bellman actions is the affine expression
\[
A+\frac{S+B|h_0|+t(Z+B\operatorname{sgn}(h_0))}{8}.
\]
For \(0\le t\le1\), the maximum is
\[
A+\frac{17+B+(1+B)t}{8}.
\]
To verify this **for all** \(B\in[1/7,1]\) and \(t\in[0,1]\), subtract each tabulated affine expression from \(17+B+(1+B)t\). The difference is bilinear in \((B,t)\), and therefore has its minimum over the rectangle at one of its four corners. Substitution of the ten displayed triples at \((B,t)\in\{1/7,1\}\times\{0,1\}\) gives forty nonnegative exact rational numbers. The profile \((1,17,1)\) gives equality for all \(B,t\). For negative \(t\), negate all seven signs to obtain the symmetric envelope. Thus
\[
A_d=A_{d-1}+\frac{17+B_{d-1}}8,\qquad
B_d=\frac{1+B_{d-1}}8,
\]
with \(A_0=0\), \(B_0=1\). Solving,
\[
B_d=\frac17+\frac6{7\cdot8^d},\quad
A_d=\frac{15d}{7}+\frac6{49}\left(1-8^{-d}\right).
\]
Hence \(F_d(1)=A_d+B_d\) is precisely the stated octonary formula, for **all** nonnegative integer depths. Since the same maximizing profile can be chosen at every ancestral node after translating the target word to zero, every terminal atom can be a norming row. Choosing the input to be the sign of that row attains the operator norm.

**4. Comparison with three dyadic generations.** The analogous binary Bellman recursion has two actions with local values \((\sigma,-\sigma)\). On \(|t|\le1\), the affine shape coefficients obey \(a_n=a_{n-1}+(1+b_{n-1})/2\), \(b_n=(1-b_{n-1})/2\), starting with \((a_0,b_0)=(0,1)\). Solving gives \(U_2(n)=2n/3+5/9+(4/9)(-1/2)^n\). Consequently
\[
U_8(d)-U_2(3d)=
\frac{63d-128+(324-196(-1)^d)8^{-d}}{441}.
\]
The numerator vanishes for \(d=0,1,2\). For each \(d\ge3\), its first two terms already sum to a positive number, and the remaining term is positive as well. This proves the strict depth-three separation and all equality cases asserted for the comparison.

## Verification
Run `python3 verify_octonary.py` (Python standard library only). The script recomputes the ten Walsh profiles from all \(2^7\) sign vectors, verifies all forty rational corner inequalities of the infinite-depth envelope, compares a separate recursively maximized Bellman program with the closed affine solution through depth four, and checks the sharp constructive kernel row by exact summation over all terminal words through depth six. It checks the grouped dyadic comparison independently. In a completed execution all tests passed. Finite-depth experiments alone are not used to justify the all-depth theorem: the exact four-corner affine certificate and induction do so.

## Relationship to prior work
Kazarian, Kazaryan and San-Antolín (arXiv:1410.4888, first posted 2014-10-17), Section 3.2 and Section 4, introduce general \(m\)-rank Haar systems and establish unconditional bases for \(1<p<\infty\). Their theorem does not give the finite-depth sharp real \(L^\infty\) signed norm for the specific eight-child Hadamard contrast basis, and it does not compare it with grouped binary generations. Osękowski (2013, DOI below) proves sharp restricted weak-type estimates for classical Haar projections and martingale transforms, a different norm and multiplier regime. The dyadic exact endpoint formula and the known four-child Hadamard/binary two-generation coincidence motivate—but do not imply—the octonary calculation: the local eight-child action has ten Walsh profiles and an optimizer profile with nontrivial sign structure. The claim is the complete octonary all-depth formula and the depth-three crossover, not generic \(m\)-adic unconditionality or a previously established dyadic case.

## Limitations
Only real independent signs are allowed; general complex phases, rotations of the seven-dimensional local contrast space, biased children, pruning, and infinite-depth uniform endpoint boundedness are outside the claim. Constants are maximum norms of **finite** transforms, not uniform bounds as depth tends to infinity. The local order-eight character spectra are elementary Walsh computations and are not individually claimed new. A prior unindexed paper might contain an equivalent closed expression; that bibliographic risk remains. Independent audit has not been performed.

## References
- A. Osękowski, “Sharp Inequalities for the Haar System and Fourier Multipliers,” *Journal of Function Spaces and Applications* (2013), DOI: `10.1155/2013/646012`, first published 2013-12-05.
- K. S. Kazarian, S. S. Kazaryan and Á. San-Antolín, “Wavelets in weighted norm spaces,” arXiv:`1410.4888` (submitted 2014-10-17), especially Sections 3.2 and 4.
