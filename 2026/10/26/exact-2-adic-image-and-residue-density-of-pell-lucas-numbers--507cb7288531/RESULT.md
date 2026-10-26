# Exact 2-adic image and residue density of Pell–Lucas numbers

## Finding
Let \(V_0=V_1=2\), and \(V_{n+2}=2V_{n+1}+V_n\) for every \(n\ge0\). The closure of the nonnegative-indexed Pell–Lucas numbers in the 2-adic integers is the disjoint union
\[
\overline{\{V_n:n\ge0\}}=(2+16\mathbb Z_2)\,\sqcup\,(14+16\mathbb Z_2)\,\sqcup\,(6+64\mathbb Z_2).
\]
Consequently, for every integer \(k\ge6\), the sequence visits exactly \(9\cdot2^{k-6}\) distinct residues modulo \(2^k\); its limiting proportion of attained residues is exactly \(9/64\). Equivalently, the companion sequence \(Q_n=V_n/2\) has 2-adic image \((1+8\mathbb Z_2)\sqcup(7+8\mathbb Z_2)\sqcup(3+32\mathbb Z_2)\).

## Assumptions and scope
All indices \(n\) are nonnegative integers and all moduli are positive powers of two. A residue is *attained* if it equals \(V_n\bmod2^k\) for at least one such index, not necessarily within any prescribed finite initial interval. The 2-adic closure refers to the usual projective limit of these residue images. There is no claim about odd moduli or distribution frequencies among indices.

## Proof
Write
\[
T=\begin{pmatrix}2&1\\1&0\end{pmatrix},\qquad Q_n=\tfrac12\operatorname{tr}(T^n),
\]
so \(Q_0=Q_1=1\) and \(Q_{n+2}=2Q_{n+1}+Q_n\). Every \(Q_n\) is odd. Direct matrix multiplication gives
\[
T^4=I+4B,\quad B=\begin{pmatrix}7&3\\3&1\end{pmatrix};\qquad
T^8=I+8D,\quad D=\begin{pmatrix}123&51\\51&21\end{pmatrix}.
\]
For \((r,s,d,C)\) in the four cases \((1,4,8,B)\), \((3,4,8,B)\), \((2,8,32,D)\), \((6,8,32,D)\), consider the continuous 2-adic function
\[
f_r(t)=\frac{Q_{r+st}-Q_r}{d}=\sum_{j\ge1}a_{r,j}\binom tj,\quad
 a_{r,j}=\frac{s^j\operatorname{tr}(T^rC^j)}{2d}\qquad(t\in\mathbb Z_2).
\]
The binomial series converges 2-adically because its coefficients tend to zero. Its first and second coefficients are, respectively,
\[
\begin{array}{c|rrrr}
r&1&3&2&6\\\hline
 a_{r,1}&5&29&105&3567\\
 a_{r,2}&164&956&121068&4112748
\end{array}.
\]
Every linear coefficient is odd. Moreover, for every \(j\ge2\),
\[
\nu_2(a_{r,j})\ge1+\nu_2(j!).
\]
Indeed, in the \(s=4\) cases the factor outside the trace is \(2^{2j-4}\). For \(j=2\), \(B^2=2T^4\) gives \(a_{r,2}=4Q_{r+4}\), divisible by four. For all \(j\ge3\), \(2j-4\ge1+\nu_2(j!)\). In the \(s=8\) cases the factor is \(2^{3j-6}\); the explicitly displayed second coefficients are divisible by four, and \(3j-6\ge1+\nu_2(j!)\) for \(j\ge3\). These bounds use only the integral matrices \(T,B,D\).

For \(u,t\in\mathbb Z_2\) and any \(j\ge1\), the polynomial identity for falling factorials implies
\[
\binom tj-\binom uj\in \frac{t-u}{j!}\,\mathbb Z_2.
\]
The coefficient bounds therefore show that the sum of terms of degree at least two is twice a 1-Lipschitz function. Since \(a_{r,1}\) is odd,
\[
\nu_2(f_r(t)-f_r(u))=\nu_2(t-u).
\]
Thus \(f_r\) induces an injection on every finite quotient \(\mathbb Z/2^k\mathbb Z\), hence a bijection; its image is all \(\mathbb Z_2\). Nonnegative integers are dense in \(\mathbb Z_2\), so the actual nonnegative-index subsequences have closures
\[
\begin{aligned}
\overline{\{Q_{1+4t}:t\ge0\}}&=1+8\mathbb Z_2,\\
\overline{\{Q_{3+4t}:t\ge0\}}&=7+8\mathbb Z_2,\\
\overline{\{Q_{2+8t}:t\ge0\}}&=3+32\mathbb Z_2,\\
\overline{\{Q_{6+8t}:t\ge0\}}&=99+32\mathbb Z_2=3+32\mathbb Z_2.
\end{aligned}
\]
It remains to treat indices divisible by four. The standard trace-doubling identity, using \(\det T=-1\), gives \(Q_{2m}=2Q_m^2-(-1)^m\). Hence \(Q_{4m}=2Q_{2m}^2-1\equiv1\pmod{16}\) because \(Q_{2m}\) is odd. This class is already contained in \(1+8\mathbb Z_2\). All indices have now been covered, proving the stated three-coset closure for \(Q_n\). Multiplication by two proves the result for \(V_n\).

For \(k\ge6\), the two disjoint classes modulo 16 each have \(2^{k-4}\) lifts modulo \(2^k\), while the class modulo 64 has \(2^{k-6}\) lifts. The total is \(2\cdot2^{k-4}+2^{k-6}=9\cdot2^{k-6}\), whose ratio to \(2^k\) is \(9/64\).

## Verification
The included `verify.py` independently constructs the matrices and checks the four linear and quadratic binomial coefficients. It verifies the divisibility inequalities for indices \(2\le j<30\) as a guard against arithmetic mistakes, and separately enumerates complete recurrence-state cycles modulo \(2^k\) for \(1\le k\le15\). This computation independently agrees with the exact three-coset prediction for every \(6\le k\le15\). The proof of the infinite statement is the preceding symbolic 2-adic argument, not the finite enumeration.

## Relationship to prior work
Bragman and Rowland, *Limiting density of the Fibonacci sequence modulo powers of a prime* (arXiv:2202.00704; first publicly submitted 2022-02-01), determine the analogous density for the ordinary Fibonacci sequence and establish a framework of piecewise 2-adic interpolation. The present claim instead concerns the different companion Pell–Lucas recurrence and gives the *entire image*, not only its density. Lang and Lang, *Three term recurrence and residue completeness* (arXiv:1307.7463), Proposition 5.2, prove exactly when the Pell–Lucas sequence is residue-complete; in particular it is not complete modulo powers of two. That statement neither enumerates the attained residues nor implies the three-coset classification or its \(9/64\) density. These antecedents and closely related published recurrence-period results were compared; an unindexed equivalent description remains possible.

## Limitations
No formula is asserted for odd-prime images or the frequencies of individual residues in the index period. The claim is not a claim of publication priority or independent proof auditing. Prior work on general recurrence residue-distribution may offer another route to the result. The 2-adic argument is self-contained, while the literature comparison is limited to the sources identified here and the search coverage available at review.

## References
1. N. Bragman and E. Rowland, *Limiting density of the Fibonacci sequence modulo powers of a prime*, arXiv:2202.00704 (first submitted 2022-02-01), https://arxiv.org/abs/2202.00704.
2. C. L. Lang and M. L. Lang, *Three term recurrence and residue completeness*, arXiv:1307.7463 (2013), https://arxiv.org/abs/1307.7463; especially Proposition 5.2.
3. A. Sanna, *On the number of residues of linear recurrences*, arXiv:2109.05734 (2021). General context for residue-image sizes of linear recurrences.
