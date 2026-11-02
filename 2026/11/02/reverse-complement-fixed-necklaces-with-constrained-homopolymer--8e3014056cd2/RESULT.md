# Reverse-complement-fixed necklaces with constrained homopolymer runs and GC content

## Finding

Let \(m,n\ge1\) and \(0\le g\le n\). Write \(F_m(n,g)\) for the number of cyclic-rotation equivalence classes of length-\(n\) DNA words with exactly \(g\) occurrences of G or C, maximal **cyclic** homopolymer run \(\le m\), and invariant under reverse complement up to rotation. Let \(L_m(h,t)\) count *linear* length-\(h\) DNA words of GC weight \(t\) whose homopolymer runs have length at most \(m\).

Then
\[
F_m(n,g)=\begin{cases}
\frac12 L_m(n/2,g/2),&2\mid n\text{ and }2\mid g,\\
0,&\text{otherwise}.
\end{cases}\tag{1}
\]
This identity counts all rotation necklaces, including those with a shorter fundamental period. If \(F_m^{\mathrm{prim}}(n,g)\) denotes the number of necklaces whose minimal period is \(n\), then
\[
F_m^{\mathrm{prim}}(n,g)=\sum_{d\mid\gcd(n,g)}\mu(d)F_m(n/d,g/d).\tag{2}
\]
In particular, exactly GC-balanced reverse-complement-invariant necklaces exist only at lengths divisible by four. For \(n=4h\),
\[
F_m(4h,2h)=\tfrac12 L_m(2h,h),\qquad
F_m^{\mathrm{prim}}(4h,2h)=\frac12\sum_{d\mid h}\mu(d)L_m(2h/d,h/d).\tag{3}
\]
These counts have an explicit bivariate rational specification. With
\[
a_m(z)=\sum_{j=1}^{m}z^j,\qquad b_m(z,u)=\sum_{j=1}^{m}(zu)^j,
\]
we have
\[
\sum_{h\ge1}\sum_{t=0}^{h}L_m(h,t)z^hu^t
=\frac{2(a_m+b_m+2a_mb_m)}{1-a_m-b_m-3a_mb_m}.\tag{4}
\]
The linear-word enumerator in (4) is a known type of transfer-matrix quantity; the contribution here is its exact transformation into the reverse-complement-fixed **cyclic orbit** and primitive-necklace counts (1)–(3).

For each fixed \(m\ge1\), let \(\rho_m\in(0,1)\) solve \(3\sum_{j=1}^m\rho_m^j=1\), and set
\[
\lambda_m=\rho_m^{-1},\quad A_m=\sum_{j=1}^m j\rho_m^j,\quad
B_m=\sum_{j=1}^m j^2\rho_m^j,\quad
\kappa_m=\frac4{9A_m},\quad
\sigma_m^2=\frac{2B_m-3A_m^2}{8A_m}.
\]
Then \(\sigma_m^2>0\) and, along \(4\mid n\),
\[
F_m^{\mathrm{prim}}(n,n/2)\sim
\frac{\kappa_m}{2\sqrt{\pi\sigma_m^2}}\frac{\lambda_m^{n/2}}{\sqrt n}.\tag{5}
\]
For example, at homopolymer cap \(m=3\), the total balanced fixed-necklace counts at lengths \(n=4,8,12,16,20,24\) are \(4,48,640,8804,124180,1781696\); the corresponding primitive counts are \(4,44,636,8756,124176,1781012\).

## Assumptions and scope

The alphabet is \(\Sigma=\{A,T,C,G\}\), with a *fixed-point-free* involution \(\bar A=T\), \(\bar T=A\), \(\bar C=G\), \(\bar G=C\). For an indexed word \(w=(w_0,\ldots,w_{n-1})\), rotation sends \(w_i\) to \(w_{i+r}\) (indices modulo \(n\)); reverse complement is \((\operatorname{RC}w)_i=\overline{w_{n-1-i}}\). Cyclic homopolymer cap \(m\) means that the bi-infinite periodic repetition of \(w\) has no constant factor of length \(m+1\); this convention excludes entirely constant necklaces for all \(n\), including \(n\le m\). A necklace is fixed if the rotation orbit of \(w\) equals the rotation orbit of \(\operatorname{RC}w\). We distinguish reverse-complement invariance *of an orbit* from an indexed word fixed without rotation. Primitive means least positive rotation period equal to the full length; no complement/reversal quotient beyond the stated fixed-point property is taken.

## Proof

**Reflection-pairing formula.** Let \(X_{m,n,g}\) be the finite set of indexed words satisfying the cyclic cap and GC weight. The dihedral-type maps \(S_r=R^r\operatorname{RC}\), \(r=0,\ldots,n-1\), commute with the constraints. Double-count the pairs \((w,r)\in X_{m,n,g}\times\{0,\ldots,n-1\}\) satisfying \(S_rw=w\). For a necklace of least period \(p\mid n\), its rotation orbit contains \(p\) distinct indexed words. If it is invariant under reverse complement, each indexed representative is fixed by exactly \(n/p\) of the maps \(S_r\); if it is not invariant, none fixes it. Thus every invariant necklace contributes precisely \(n\) pairs, *regardless of its period*. Therefore
\[
F_m(n,g)=\frac1n\sum_{r=0}^{n-1}|\operatorname{Fix}_{X_{m,n,g}}S_r|.\tag{6}
\]

If \(n\) is odd, each reflection of the \(n\)-cycle fixes a vertex, requiring a base to equal its Watson–Crick complement; no fixed word exists. If \(n\) is even, exactly \(n/2\) reflections have two fixed vertices, again impossible; the other \(n/2\) have axes through opposite *edges*, so every position is paired with a distinct position. Fix any edge-axis reflection. Any fixed word consists of an arbitrary first semicircular segment \(v\) of length \(n/2\), followed by its reverse complement (with an appropriate choice of starting boundary). Each mirror pair preserves the GC/AT category, so the full GC count is twice the GC count of \(v\). At the two junctions between \(v\) and \(\operatorname{RC}v\), adjacent bases are complementary and necessarily different. Consequently the cyclic cap on the full word is equivalent to the ordinary linear cap on \(v\), without any extra boundary restriction. Such a reflection therefore fixes exactly \(L_m(n/2,g/2)\) words when \(g\) is even, and zero otherwise. Substitution in (6) gives (1).

**Primitive Möbius inversion.** The rotational least period \(p\) of a GC-weight-\(g\) length-\(n\) word divides \(n\). Writing it as \(d=n/p\) repetitions forces \(d\mid g\), and the shorter word has weight \(g/d\). The reverse-complement condition of a power is equivalent to the condition for its primitive root: if two powers are rotationally equal, their length-\(p\) primitive necklaces agree. Thus
\[
F_m(n,g)=\sum_{d\mid\gcd(n,g)}F_m^{\mathrm{prim}}(n/d,g/d).
\]
Möbius inversion yields (2). Since balance requires \(g=n/2\) and both \(n,g\) even, we obtain \(4\mid n\), with formula (3) after noting that only divisors of \(h=n/4\) can survive the parity constraint in (2).

**Rational enumerator.** Split runs into two GC-class types: A/T runs have series \(a_m\), C/G runs have series \(b_m\). The first run has two choices of base within either type. Upon changing runs, a run of the same type has exactly one different base available, while a run of the other type has two choices. Summing all nonempty sequences of runs gives the two-type transfer system
\[
\begin{pmatrix}U_A\\U_G\end{pmatrix}
=\begin{pmatrix}2a_m\\2b_m\end{pmatrix}
+\begin{pmatrix}a_m&2a_m\\2b_m&b_m\end{pmatrix}
\begin{pmatrix}U_A\\U_G\end{pmatrix},
\]
where the components count words classified by the type of their final run. Inverting the matrix and summing the two components gives (4). This is an independently checkable form of familiar linear run-length enumerations, not a new general transfer-matrix method.

**Sharp balanced primitive asymptotic.** At \(u=1\), the rational series in (4) simplifies to
\[
H_m(z,1)=\frac{4a_m(z)}{1-3a_m(z)}.
\]
Because all coefficients of \(a_m\) are nonnegative and the underlying four-base run automaton has closed walks of lengths two and three, \(z=\rho_m\) is its unique dominant pole. Its coefficient residue is \(\kappa_m=4/(9A_m)\), whence \(\sum_tL_m(N,t)\sim\kappa_m\lambda_m^N\). To control the weight distribution, put \(u=e^s\) in (4) and let \(\rho(s)\) solve \(1-a_m(\rho)-b_m(\rho,e^s)-3a_mb_m=0\) near zero. Implicit differentiation yields
\[
-\left.\frac{d}{ds}\log\rho(s)\right|_{s=0}=\frac12,
\qquad
-\left.\frac{d^2}{ds^2}\log\rho(s)\right|_{s=0}
=\sigma_m^2=\frac{2B_m-3A_m^2}{8A_m}.
\]
The finite run-state automaton is primitive and its GC statistic is strongly aperiodic: among closed two-letter cycles it realizes GC totals zero, one and two (for example A–T, A–C and C–G). The standard finite-state aperiodic local central limit theorem therefore gives the **local**, not merely distributional, estimate
\[
L_m(N,N/2)\sim\frac{\kappa_m\lambda_m^N}{\sqrt{2\pi\sigma_m^2N}}
\quad\text{through even }N.
\]
The same cycle argument guarantees \(\sigma_m^2>0\). In (3), every term with divisor \(d\ge2\) grows at most polynomially times \(\lambda_m^{N/d}\), exponentially smaller than the leading term since \(\lambda_m>1\). Inserting \(N=n/2\) proves (5).

## Verification

The included standalone file `verify.py` reproduces the full algebraic generating-function coefficient identity through length twelve for run caps one through four. Separately, it enumerates every indexed circular word for lengths one through eight with run caps one through three, forms actual rotation necklaces, independently tests reverse-complement invariance and rotational primitivity, and compares every allowed GC weight against (1) and (2). Additional integer dynamic-programming checks cover caps one through four, lengths through eighty, including the printed balanced counts. Execute `python3 verify.py`; the expected output starts with `VERIFY_OK`.

The exhaustive checks are finite consistency checks. They are not substitutes for the all-length reflection double count, run decomposition and Möbius proof above; the asymptotic follows from the explicitly identified primitive finite-state automaton and local limit theorem, not from numerical extrapolation.

## Relationship to prior work

Immink and Cai (2018), Sections IV–V, give exact and approximate counting for **linear** GC-balanced/homopolymer-constrained DNA words; their full original preprint was inspected. The linear enumeration here is a transparent equivalent run-transfer expression and is not claimed as original. Nguyen, Cai, Immink and Kiah (2020) construct linear constrained codes with GC and run limits; their full accessible preprint was inspected. Taki Eldin and Matsui (2020) address *cyclic reverse-complement and constant-GC-content DNA codes*, using irreducible finite-field cyclic codes and trace functions to construct code families; the published abstract was read, but the paper's full text could not be accessed. Their disclosed objective differs from counting **all** RC-invariant rotation necklaces at fixed GC and bounded cyclic runs, yet this is the strongest unresolved full-text comparison. Fimmel, Michel, Starman and Strüngmann (2018) concern self-complementary circular *genetic-code word sets*, rather than enumerating length-variable DNA strings under this combined constraint. The general Burnside and Möbius tools used here are classical. The specific reflection-to-linear bijection, sharp parity obstruction, weighted primitive orbit enumeration and associated asymptotic for this combined family were not located in the inspected literature.

## Limitations

The result concerns combinatorial cyclic strings and exact reverse-complement *orbit symmetry*. It is not an error-correcting-code construction, minimum Hamming distance theorem, or guarantee of absence of DNA secondary structure; it does not imply a physical molecule necessarily forms a hairpin. The full text of the 2020 Taki Eldin–Matsui paper was unavailable; independent literature verification remains necessary for priority. Symmetry count is not the count of all constrained necklaces or the number of orbits after **quotienting** by reverse complement (those are different invariants). The asymptotic is for fixed \(m\) only, along balanced lengths divisible by four.

## References

1. K. A. S. Immink and K. Cai, *Properties and constructions of constrained codes for DNA-based data storage*, arXiv:1812.06798v1, public December 14, 2018, https://arxiv.org/html/1812.06798v1 .
2. T. T. Nguyen, K. Cai, K. A. S. Immink and H. M. Kiah, *Capacity-Approaching Constrained Codes with Error Correction for DNA-Based Data Storage*, arXiv:2001.02839v1, public January 9, 2020, https://arxiv.org/html/2001.02839v1 .
3. R. Taki Eldin and H. Matsui, *Run-Length Constraint of Cyclic Reverse-Complement and Constant GC-Content DNA Codes*, IEICE Trans. Fundamentals E103-A(1), 325–333 (2020), doi:10.1587/transfun.2019EAP1053, https://doi.org/10.1587/transfun.2019EAP1053 .
4. E. Fimmel, C. J. Michel, M. Starman and L. Strüngmann, *Self-complementary circular codes in coding theory*, Theory in Biosciences 137, 51–65 (2018), doi:10.1007/s12064-018-0259-4, https://pubmed.ncbi.nlm.nih.gov/29532441/ .
