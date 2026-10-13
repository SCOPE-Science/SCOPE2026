# Quadratic-sum control of local repair multiplicities in the two newly resolved trinomial trace codes
## Finding
For every odd integer \(m\ge5\), let \(D\subset\mathbb F_{2^m}^{*}\) be the common punctured value set of classes (a) and (b) in Wang–Xiong–Yuan–Qiu–Zheng–He, and let \(C_D\) be its binary trace code. For \(d\in D\), let \(\rho(d)\) be the number of weight-three words of \(C_D^{\perp}\) whose support contains coordinate \(d\), and put \(G_4(d)=\sum_{y\in\mathbb F_{2^m}}(-1)^{\operatorname{Tr}(y^{17}+d y^3)}\). Then \(\rho(d)=2^{m-3}-G_4(d)/8\). If \(G_4(d)\ne0\), then \(|G_4(d)|=2^{(m+r)/2}\) for some \(r\in\{1,3,5,7\}\); hence \(\rho(d)\in\{2^{m-3}\}\cup\{2^{m-3}\pm2^{(m+r-6)/2}:r\in\{1,3,5,7\}\}\). Moreover \(\sum_{d\in D}\rho(d)=2^{m-3}(2^{m-1}-1)\), so \(\rho\) is never constant on \(D\). Consequently the weight-three dual supports are not a \(1\)-design and the code is not coordinate-transitive. For \(m\ge9\), the displayed range is strictly positive, so every coordinate has locality two but the number of two-helper recovery pairs is necessarily nonuniform.

The formula turns the local incidence geometry of the minimum dual words into the same quadratic exponential sums that occur in the recent resolution of Ding's coding conjectures, but in a different role: the source uses these sums to control global Hamming weights of another defining-set family, whereas here they control the number of weight-three parity checks through each individual coordinate.

## Assumptions and scope
Let \(m\ge5\) be odd and put \(q=2^m\). The two trinomials are
\[
f_1(x)=x^{2^m-17}+x^{(2^m+19)/3}+x
\]
and
\[
f_2(x)=x^{2^m-2^{m-4}-1}+x^{2^m-(2^{m-2}+4)/3}+x.
\]
Their common punctured image is \(D=\operatorname{Im}(f_1)\setminus\{0\}=\operatorname{Im}(f_2)\setminus\{0\}\), as proved in the recent source. The trace code is
\[
C_D=\left\{\bigl(\operatorname{Tr}(ad)\bigr)_{d\in D}:a\in\mathbb F_q\right\}.
\]
The source proves \(|D|=q/2\), \(\dim C_D=m\), and \(d(C_D^\perp)=3\). The present claim concerns only classes (a) and (b), because the exact Walsh identity used below is the one that closes those two previously unresolved classes.

For a coordinate \(d\in D\), \(\rho(d)\) counts weight-three dual words containing that coordinate. In binary codes a support determines its nonzero word, so \(\rho(d)\) is also the number of two-helper parity-check recovery pairs through \(d\).

## Proof
A binary vector supported on three distinct coordinates \(d,y,z\in D\) lies in \(C_D^\perp\) exactly when
\[
d+y+z=0.
\]
Indeed, orthogonality to every trace codeword is equivalent to \(\operatorname{Tr}(a(d+y+z))=0\) for every \(a\in\mathbb F_q\), and the trace pairing is nondegenerate. Therefore, with
\[
N_d=|D\cap(D+d)|,
\]
the involution \(y\mapsto y+d\) pairs the ordered solutions and gives
\[
\rho(d)=\frac{N_d}{2}.
\]

Let \(f=1_D\) and define its Walsh transform by
\[
W_f(a)=\sum_{x\in\mathbb F_q}(-1)^{f(x)+\operatorname{Tr}(ax)}.
\]
Because \(|D|=q/2\), the Boolean autocorrelation
\[
A_f(d)=\sum_{x\in\mathbb F_q}(-1)^{f(x)+f(x+d)}
\]
satisfies \(A_f(d)=4N_d-q\). Fourier inversion gives
\[
A_f(d)=q^{-1}\sum_{a\in\mathbb F_q}W_f(a)^2(-1)^{\operatorname{Tr}(ad)}.
\]

The recent source proves the precise Dillon–Dobbertin identity
\[
W_f(a)=W_Q\!\left(a^{17/3}\right),\qquad Q(x)=\operatorname{Tr}(x^3),
\]
where division by \(3\) is taken modulo \(q-1\). Since \(m\) is odd, the cube map permutes \(\mathbb F_q\). The polar form of \(Q\) has radical \(\langle1\rangle_{\mathbb F_2}\). Translation by \(1\) shows that \(W_Q(b)\) can be nonzero only when \(\operatorname{Tr}(b)=1\), and the standard quadratic-form evaluation then gives
\[
W_Q(b)^2=
\begin{cases}
2^{m+1},&\operatorname{Tr}(b)=1,\\
0,&\operatorname{Tr}(b)=0.
\end{cases}
\]
Consequently
\[
A_f(d)=2\sum_{a:\operatorname{Tr}(a^{17/3})=1}(-1)^{\operatorname{Tr}(ad)}.
\]
Write \(a=y^3\). Then \(a^{17/3}=y^{17}\), and for \(d\ne0\),
\[
\sum_{y\in\mathbb F_q}(-1)^{\operatorname{Tr}(dy^3)}=0.
\]
Using the trace-one indicator therefore yields
\[
A_f(d)=-\sum_{y\in\mathbb F_q}(-1)^{\operatorname{Tr}(y^{17}+dy^3)}=-G_4(d).
\]
Hence
\[
N_d=\frac{q-G_4(d)}4,\qquad
\rho(d)=\frac{q-G_4(d)}8=2^{m-3}-\frac{G_4(d)}8.
\]

For the value range, \(G_4(d)\) is the quadratic-form sum of
\[
Q_d(y)=\operatorname{Tr}(y^{17}+dy^3).
\]
Its polar radical \(R_d\) satisfies
\[
z^{256}+d^{16}z^{32}+d^8z^8+z=0.
\]
When \(m\ge9\), this is a nonzero linearized polynomial of \(2\)-degree at most \(8\), so \(\dim_{\mathbb F_2}R_d\le8\); for \(m=5,7\) the trivial bound \(\dim R_d\le m\) is stronger. Because an alternating form has even rank and \(m\) is odd, \(r=\dim R_d\) is odd, hence \(r\in\{1,3,5,7\}\). A quadratic Boolean sum is either zero or has magnitude \(2^{(m+r)/2}\), which gives the stated list of possible \(\rho(d)\).

Finally the recent source computes
\[
A_3(C_D^\perp)=\frac{2^m(2^m-2)}{48}.
\]
Double-counting incidences between coordinates and weight-three dual words gives
\[
\sum_{d\in D}\rho(d)=3A_3(C_D^\perp)=2^{m-3}(2^{m-1}-1).
\]
Since \(|D|=2^{m-1}\), the average value is \((2^{m-1}-1)/4\), which is not an integer. Therefore \(\rho\) cannot be constant. The weight-three supports are not a \(1\)-design, and coordinate transitivity is impossible because coordinate automorphisms preserve the minimum-dual-word incidence numbers.

For \(m\ge9\), the largest possible subtraction in the range is \(2^{(m+1)/2}<2^{m-3}\), so every \(\rho(d)\) is positive. Thus every coordinate then has a two-helper recovery pair, but the number of such pairs is nonuniform.

## Verification
The accompanying `verify.py` uses only integer arithmetic and exact polynomial-basis arithmetic in \(\mathbb F_{2^m}\). For \(m=5,7,9\), it independently reconstructs both trinomials, verifies that their punctured images coincide and have size \(2^{m-1}\), computes every \(\rho(d)\) directly from pairs \(y,y+d\in D\), computes every \(G_4(d)\) from its defining character sum, and checks \(8\rho(d)=2^m-G_4(d)\) coordinate by coordinate. It also checks the Pless-derived total \(A_3=2^m(2^m-2)/48\) and the allowed nonzero quadratic-sum magnitudes.

The exact finite outputs are
\[
m=5:\quad \{\rho=0:1,\ \rho=4:15\},
\]
\[
m=7:\quad \{\rho=14:22,\ \rho=16:28,\ \rho=18:14\},
\]
and
\[
m=9:\quad \{\rho=60:72,\ \rho=64:129,\ \rho=68:54,\ \rho=72:1\}.
\]
These computations are finite anchors only; the all-odd-\(m\) statement is proved symbolically above.

## Relationship to prior work
Wang–Xiong–Yuan–Qiu–Zheng–He prove that classes (a) and (b) have the common defining set \(D\), establish the Walsh identity with the Gold function, derive the three-weight enumerator, and obtain \(A_3(C_D^\perp)\) and dual distance \(3\). Their paper also introduces the sums \(G_h(b)\) in the distinct Dillon–Dobbertin family and analyzes their possible values via quadratic radicals. It does not state the coordinatewise incidence identity \(\rho(d)=2^{m-3}-G_4(d)/8\), the resulting non-\(1\)-design conclusion, or the coordinate-transitivity obstruction.

Ahmadi–Shafaeiabr prove that all eleven punctured trinomial value sets are Singer difference sets and settle the coding statement for classes (c)–(k), while explicitly leaving classes (a) and (b) to a separate conjectural reduction. Their full preprint does not classify the weight-three dual supports through individual coordinates.

Focused searches for the exact trinomials, Singer-difference-set trace codes, weight-three dual supports, coordinate incidence, locality, autocorrelation, and the \(G_4\) quadratic sum found no source implying the displayed local formula. The closest database hits concern unrelated recovery-set incidence problems, weight-three cover-free families, and global code spectra rather than this defining set.

## Limitations
The theorem gives an exact local formula and a finite list of possible repair multiplicities, but it does not determine the multiplicity of each \(G_4\)-value for every odd \(m\). That remaining distribution problem is comparable to the rank-and-sign classification of the relevant quadratic sums. The result is restricted to the two newly resolved classes (a) and (b), not to the other nine trinomial classes. The finite verifier checks only \(m=5,7,9\) and is not a substitute for the symbolic proof.

A residual originality risk is that an unindexed paper on Dillon–Dobbertin difference sets or local structure of projective three-weight codes may contain an equivalent autocorrelation-to-incidence specialization. No such statement was located in the primary full texts or focused searches used here.

## References
1. X. Wang, S. Xiong, M. Yuan, J. Qiu, D. Zheng, J. He, *Six Families of Binary Codes Arising from Ding's Conjectures*, arXiv:2609.37093v1, first public 2026-09-29.
2. O. Ahmadi, M. Shafaeiabr, *Difference sets and tri-weight linear codes from trinomials over binary fields*, arXiv:2108.10042v1, first public 2021-08-23; journal version: *Finite Fields and Their Applications* 89 (2023), 102195.
3. J. F. Dillon, H. Dobbertin, *New cyclic difference sets with Singer parameters*, *Finite Fields and Their Applications* 10 (2004), 342–389.
