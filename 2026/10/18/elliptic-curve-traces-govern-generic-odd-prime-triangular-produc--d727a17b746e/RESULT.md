# Elliptic-curve traces govern generic odd-prime triangular-product square densities

## Finding
Let \(p\ge5\) be a prime and \(n\in\mathbb Z\) satisfy \(p\nmid n(1+64n)\). Let \(a,b\) be independent normalized Haar-uniform elements of \(\mathbb Z_p\), write \(T(t)=t(t+1)/2\), and set
\[
\delta_p(n)=\Pr\bigl(T(a)T(b)+n\text{ is a square in }\mathbb Z_p\bigr).
\]
Write \(m=1+64n\pmod p\), and let \(\chi_p\) be the quadratic character of \(\mathbb F_p\), extended by \(\chi_p(0)=0\). The smooth genus-one quartic
\[
E_{p,n}:\quad v^2=(u^2-1)(u^2-m)
\]
has two rational points at infinity and Frobenius trace \(a_p(E_{p,n})=p+1-\#E_{p,n}(\mathbb F_p)\). Then the density is exactly
\[
\boxed{\delta_p(n)=\frac12+
\frac{1+p\chi_p(n)(3+\chi_p(m))}{2p^2}
-\frac{p-3-a_p(E_{p,n})}{2p(p+1)}.}
\]
In particular, the density depends only on \(n\bmod p\) throughout the natural smooth-discriminant locus, and the Hasse bound gives the uniform prime-asymptotic profile
\[
\delta_p(n)=\frac12+
\frac{\chi_p(n)(3+\chi_p(1+64n))-1}{2p}
+O(p^{-3/2}),
\]
where the implied constant is absolute. For example, \(\delta_5(2)=4/75\) and \(\delta_7(1)=149/196\).

## Assumptions and scope
The prime \(p\) is any rational prime at least five, \(n\) is any ordinary integer with \(p\nmid n\) and \(p\nmid(1+64n)\), and the two input indices range independently over all of \(\mathbb Z_p\), including zero. A square means an element of \(\{t^2:t\in\mathbb Z_p\}\), not just a nonzero square modulo \(p\). The two excluded residue classes are precisely where the branch polynomial below acquires a singular zero modulo \(p\); no claim is made for those classes or for primes two and three. The elliptic model is understood as the smooth projective completion of the displayed affine quartic.

## Proof
**Uniform change of variables.** Because \(2\in\mathbb Z_p^\times\), the substitutions \(u=2a+1\) and \(v=2b+1\) are independent Haar-preserving bijections. Since \(T(a)=(u^2-1)/8\), the requested expression is a square exactly when
\[
F(u,v)=(u^2-1)(v^2-1)+64n
\]
is a square; multiplication by \(64=8^2\) does not change squarehood.

**Every zero class is smooth.** Modulo \(p\), the two partial derivatives are \(2u(v^2-1)\) and \(2v(u^2-1)\). If both vanish, either \(u=v=0\), where \(F=1+64n\), or \(u^2=v^2=1\), where \(F=64n\). The hypothesis excludes both possibilities on the zero locus. Consequently, for each class \((u_0,v_0)\in\mathbb F_p^2\) with \(F(u_0,v_0)=0\), an appropriate one-coordinate implicit-function substitution identifies \(F/p\) on its residue ball with a Haar-uniform element of \(\mathbb Z_p\). The conditional probability that \(F\) is a square in this ball is
\[
\frac12\sum_{j\ge0}(1-p^{-1})p^{-(2j+1)}=\frac1{2(p+1)}.
\]
For a residue class with nonzero \(F\), the entire ball gives square values exactly if \(\chi_p(F)=1\).

**Finite-character reduction.** Denote by \(A\) the number of classes with \(\chi_p(F)=1\), by \(Z\) the number with \(F=0\), and set \(S=\sum_{u,v\in\mathbb F_p}\chi_p(F(u,v))\). Then
\[
\delta_p(n)=\frac{A}{p^2}+\frac{Z}{2p^2(p+1)},\qquad
A=\frac{p^2-Z+S}{2},
\]
and hence
\[
\delta_p(n)=\frac12+\frac{S}{2p^2}-\frac{Z}{2p(p+1)}.
\]
To evaluate \(S\), fix \(u\). At \(u=\pm1\), the inner sum over \(v\) is \(p\chi_p(n)\). For \(u\ne\pm1\), it is \(-\chi_p(u^2-1)\), except when \(u^2=m\), when an additional \(p\chi_p(u^2-1)=p\chi_p(n)\) occurs. This uses the elementary identity
\[
\sum_{v\in\mathbb F_p}\chi_p(Av^2+B)=
\begin{cases}-\chi_p(A),& A\ne0,\ B\ne0,\\
(p-1)\chi_p(A),& A\ne0,\ B=0.
\end{cases}
\]
The hypotheses ensure that \(m\notin\{0,1\}\), so the number of roots of \(u^2=m\) is \(1+\chi_p(m)\), none equal to \(\pm1\). Finally \(\sum_u\chi_p(u^2-1)=-1\), giving
\[
S=1+p\chi_p(n)(3+\chi_p(m)).
\]

**The elliptic trace.** Because \(n\not\equiv0\pmod p\), no zero of \(F\) has \(u=\pm1\). For each other \(u\), the number of possible \(v\) is \(1+\chi_p((u^2-1)(u^2-m))\). Thus
\[
Z=p-2+\sum_{u\in\mathbb F_p}\chi_p((u^2-1)(u^2-m)).
\]
The four roots of the quartic are distinct over an algebraic closure because \(m\notin\{0,1\}\). Its projective smooth completion has exactly two \(\mathbb F_p\)-rational points at infinity. Counting its affine solutions gives
\[
\#E_{p,n}(\mathbb F_p)=p+2+\sum_u\chi_p((u^2-1)(u^2-m)),
\quad Z=p-3-a_p(E_{p,n}).
\]
Substitution proves the boxed exact identity.

**Uniform bias.** Hasse's inequality \(|a_p(E_{p,n})|\le2\sqrt p\) and elementary rearrangement of the exact identity yield
\[
\delta_p(n)-\left[\frac12+
\frac{\chi_p(n)(3+\chi_p(m))-1}{2p}\right]
=\frac2{p(p+1)}+\frac1{2p^2}+\frac{a_p(E_{p,n})}{2p(p+1)},
\]
which is uniformly \(O(p^{-3/2})\). This completes the proof.

## Verification
Run `python verify.py` with Python 3 and no external packages. The program independently enumerates the finite-field residue classes, the character sum and quartic trace for every generic parameter modulo primes \(5,7,11,13,17,19,23,29\). It verifies \(108\) finite-field parameter cases and \(5\) further modular-bracketing cases. For the latter, a nonzero square modulo \(p^k\) certifies a genuine local square, while a zero residue remains undecided. The exact uncertainty width is checked against \(Z/p^{k+1}\). Those tests support, but do not establish, the infinite-prime theorem; the preceding argument is the proof.

## Relationship to prior work
Bagchi and Zhou-Zheng, *Diophantine m-tuples of Triangular Numbers* (arXiv:2608.27697, first posted August 27, 2026), study the same triangular-pair condition and establish qualitative local solvability outside the prime three. Their presented results do not evaluate the Haar probability or relate its dependence on the shift to an elliptic Frobenius trace. Kazalicki and Naskręcki, *Diophantine triples and K3 surfaces* (arXiv:2101.11705), use elliptic curves to count a different finite-field Diophantine-triple configuration; no equivalence to the two-variable shifted triangular-product local density has been established. Quadratic-character sums, smooth \(p\)-adic lifting, and Hasse's inequality are classical inputs, not newly claimed methods. The new asserted contribution is the exact combined density-to-elliptic-trace identity on the canonical smooth parameter locus, including its explicit first-order quadratic-character bias.

## Limitations
The formula is not asserted at the exceptional classes \(n\equiv0\pmod p\) or \(1+64n\equiv0\pmod p\): singular \(p\)-adic residue balls then demand further valuation analysis. It does not count global integer solutions, describe Diophantine triples, evaluate individual elliptic traces in elementary terms, or make claims beyond the specified local density. Although targeted searches identified no statement of this exact density formula, an earlier implicit consequence of general local-zeta or genus-one point-counting theory cannot be excluded solely by those searches.

## References
1. S. Bagchi and C. Zhou-Zheng, *Diophantine m-tuples of Triangular Numbers*, arXiv:2608.27697 (initial submission August 27, 2026), https://arxiv.org/abs/2608.27697.
2. M. Kazalicki and B. Naskręcki, *Diophantine triples and K3 surfaces*, arXiv:2101.11705 (2021), https://arxiv.org/abs/2101.11705.
3. Hasse's theorem on the number of points of an elliptic curve over a finite field (classical bound on the Frobenius trace).
