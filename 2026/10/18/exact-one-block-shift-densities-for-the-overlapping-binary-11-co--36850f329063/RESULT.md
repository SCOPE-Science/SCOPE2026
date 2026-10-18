# Exact one-block shift densities for the overlapping binary \(11\)-count

## Finding
Let \(r(n)\) be the number of overlapping occurrences of the word \(11\) in the usual binary expansion of the nonnegative integer \(n\). For every \(j\ge0\) and \(k\ge1\), put \(t_{j,k}=2^j(2^k-1)\), and define the natural density
\[
 p_{j,k}=\lim_{X\to\infty}\frac{1}{X}\#\{0\le n<X:r(n+t_{j,k})\ge r(n)\}.
\]
All these densities exist. They are given exactly by
\[
\begin{array}{c|cccc}
 & k=1&k=2&k=3&k\ge4\\\hline
 j=0&13/16&47/64&87/128&83/128\\
 j\ge1&23/32&43/64&5/8&39/64
\end{array}.
\]
In particular the sharp lower bound within *every shift having one maximal block of ones* is \(p_{j,k}\ge39/64>1/2\); equality holds precisely when \(j\ge1\) and \(k\ge4\). The exact constancy for all longer blocks is not merely an asymptotic statement.

## Assumptions and scope
The binary expansion of \(n\) is padded by zeros at its high end; \(r(0)=0\), and each pair of adjacent one-bits contributes one occurrence. Both \(j\) and \(k\) are arbitrary integers in the ranges above. All densities refer to \(n\) tending to infinity through **all** nonnegative integers, not to a selected residue class. A shifted binary block with a single maximal run has uniquely the form \(2^j(2^k-1)\). The proof does not address shifts having two or more maximal runs.

## Proof
Write \(d(t,n)=r(n+t)-r(n)\). Conditional on even and odd starting integers, let \(a_t(m)\) and \(b_t(m)\) be the respective natural densities of \(d(t,2n)=m\) and \(d(t,2n+1)=m\). Their existence and the elementary binary recursions follow from Proposition 3.2 of Sobolewski--Spiegelhofer [1]; alternatively they follow by conditioning on the final two binary digits and using \(r(2n)=r(n)\), \(r(4n+1)=r(n)\), \(r(4n+3)=r(2n+1)+1\).

Use the Laurent probability generating functions \(A_t(z)=\sum_m a_t(m)z^m\), \(B_t(z)=\sum_m b_t(m)z^m\). Every rational expression below is expanded in the annulus \(|z|>1/2\), where \((2z-1)^{-1}=\sum_{h\ge1}2^{-h}z^{-h}\), and evaluated on \(|z|=1\). The unconditional law is \(C_t(z)=(A_t(z)+B_t(z))/2\), and \(p(t)=1-\sum_{m<0}[z^m]C_t(z)\).

The starting laws are
\[
 A_1(z)=\frac{1+z}{2},\qquad B_1(z)=\frac{z(1+z)}{2(2z-1)}.
\]
For every positive integer \(u\), conditioning on the low bits gives
\[
\begin{aligned}
 A_{4u}&=B_{4u}=\frac{A_{2u}+B_{2u}}2,\\
 A_{4u+1}&=\frac{A_{2u}+zB_{2u}}2,&B_{4u+1}&=\frac{A_{2u+1}+z^{-1}B_{2u+1}}2,\\
 A_{4u+2}&=\frac{A_{2u+1}+B_{2u+1}}2,&B_{4u+2}&=\frac{zA_{2u+1}+z^{-1}B_{2u+1}}2,\\
 A_{4u+3}&=\frac{zA_{2u+1}+B_{2u+1}}2,&B_{4u+3}&=\frac{A_{2u+2}+z^{-1}B_{2u+2}}2.
\end{aligned}
\]
The cases \(t=2,3\) are obtained from the same low-bit identities with the base laws; in particular
\[
 A_2=\frac{A_1+B_1}{2},\quad B_2=\frac{zA_1+z^{-1}B_1}{2},\quad
 A_3=\frac{zA_1+B_1}{2},\quad B_3=\frac{A_2+z^{-1}B_2}{2}.
\]
Furthermore
\[
 A_4=B_4=U(z):=\frac{z(1+z)^2}{4(2z-1)},
\]
and the even-shift relations imply \(A_{2^h}=B_{2^h}=U\) for every \(h\ge2\).

Set \(T_k=2^k-1\). For \(k\ge3\), the odd-shift recurrence, together with the preceding power-of-two identity, yields
\[
 B_{T_k}(z)=H(z):=\frac{(1+z)^3}{8(2z-1)}.
\]
The same calculation gives
\[
 A_{T_4}(z)=J(z):=\frac{(1+z)(2z^2-z+3)(2z^2+z+1)}{32(2z-1)}.
\]
For \(k\ge4\), \(A_{T_{k+1}}=(zA_{T_k}+H)/2\). Subtracting the preceding instance of this recurrence and simplifying the initial difference gives
\[
 A_{T_5}(z)-A_{T_4}(z)=K(z):=
 \frac{(z-1)^2(z+1)(2z^2+z+2)}{64}.
\]
Consequently, **for every** \(k\ge4\),
\[
 A_{T_k}(z)=J(z)+K(z)\sum_{h=0}^{k-5}(z/2)^h,
\]
where the sum is zero for \(k=4\). Crucially, \(K\) contains no negative powers, and \(K(1)=0\). Thus increasing the run length beyond four redistributes only nonnegative outcomes, with no change at all to the negative probability tail.

Indeed polynomial division gives
\[
 J(z)=\frac{2z^4+3z^3+5z^2+7z+6}{32}+\frac{9}{32(2z-1)},
\qquad
 H(z)=\frac{4z^2+14z+19}{64}+\frac{27}{64(2z-1)}.
\]
The expansion of \((2z-1)^{-1}\) has total mass one, entirely on negative exponents. Therefore the negative masses of \(J\) and \(H\) are \(9/32\) and \(27/64\). It follows that for \(k\ge4\)
\[
 p(T_k)=1-\frac12\left(\frac9{32}+\frac{27}{64}\right)=\frac{83}{128}.
\]

For every odd positive shift \(t\), the even-shift identity reads
\[
 C_{2t}(z)=\frac{(1+z)A_t(z)+(1+z^{-1})B_t(z)}4.
\]
Further multiplication of the shift by two leaves its law unchanged, because \(A_{4t}=B_{4t}=C_{2t}\) and the low-bit recursion propagates this identity. The variation of \(C_{2T_k}\) for \(k\ge4\) is a multiple of \((1+z)K(z)\), again nonnegative in its Laurent support and zero at \(z=1\). So the negative tail is constant. The negative masses of \((1+z)J\) and \((1+z^{-1})H\) are, respectively, \(27/64\) and \(73/64\); the second calculation uses \([z^0]H=19/64\). Therefore
\[
 p(2^jT_k)=1-\frac14\left(\frac{27}{64}+\frac{73}{64}\right)=\frac{39}{64}
\qquad(j\ge1,\ k\ge4).
\]
Finally, direct exact rational substitutions of the initial laws into the displayed recurrences give the first three columns of the theorem. Their six entries are reproduced by the standalone checker, using exact fractions. Comparing all entries establishes the global minimum and its equality cases.

## Verification
The accompanying `verifier.py` uses only the Python standard library. It represents every conditional generating function as a Laurent polynomial over the common denominator \(2z-1\), checks the decisive factorization of \(K\), exact total and negative masses, the six initial entries, and 60 further exact rational one-block identities. It also compares 24 direct binary enumerations on \(0\le n<2^{18}\) against the analytic densities, allowing explicitly for truncation at the finite upper boundary. The infinite claim follows from the recurrences, factorization, and support argument above, not from finite enumeration.

## Relationship to prior work
Sobolewski and Spiegelhofer [1] introduced these exact conditional distributions and their general recursions, and asked whether the nonnegative-difference density exceeds one half for **every** shift. Their Gaussian approximation depends on the number of blocks of ones becoming large and does not settle the one-block regime. This result does not claim novelty for their general recurrence; it evaluates an entire infinite low-complexity family, identifies an exact sharp value, and shows a nonobvious stabilization of the negative tail by a polynomial cancellation. Sobolewski [2] extends Gaussian approximations to other block-counting functions, still in the regime of many blocks. The digit-*sum* correlation decomposition [3] addresses a different statistic and does not furnish these \(11\)-count densities. No general-shift conjecture is resolved.

## Limitations
This covers only one-block binary shifts; nothing is asserted about two or more runs. The density is a natural density and does not imply eventual pointwise inequalities. The rational recurrences used as input were published previously. The exact closed-family evaluation and the plateau are the asserted contribution; independent verification of publication priority has not been performed. Finite executable tests cannot replace the recurrence proof. No convergence rate for finite counting intervals is claimed.

## References
[1] B. Sobolewski and L. Spiegelhofer, *Block occurrences in the binary expansion*, arXiv:2309.00142v1, first posted August 31, 2023, Sections 2 and 3, especially Proposition 3.2. https://arxiv.org/html/2309.00142v1

[2] B. Sobolewski, *On the behavior of binary block-counting functions under addition*, arXiv:2412.15851v1, first posted December 20, 2024, Sections 1 and 4. https://arxiv.org/html/2412.15851v1

[3] B. Sobolewski and L. Spiegelhofer, *Decomposing the sum-of-digits correlation measure*, arXiv:2411.07779v1, first posted November 12, 2024. https://arxiv.org/abs/2411.07779
