# Sharp fourth-moment phase range for four-frequency unimodular trigonometric polynomials
## Finding
Let \(n_0<n_1<n_2<n_3\) be distinct integers and let
\[
P(x)=\sum_{j=0}^{3}c_j e^{2\pi i n_jx},\qquad |c_j|=1,
\]
on \(\mathbb T=\mathbb R/\mathbb Z\), with normalized Haar measure. Then
\[
19\le \|P\|_4^4\le 44.
\]
Both constants are sharp, and either global equality forces the frequency support to be a four-term arithmetic progression. If \(n_j=a+jd\), put
\[
\alpha=\arg\!\left(c_1^2\overline{c_0c_2}\right),\qquad
\beta=\arg\!\left(c_2^2\overline{c_1c_3}\right).
\]
Then \(\|P\|_4^4=44\) exactly when \(\alpha\equiv\beta\equiv0\pmod{2\pi}\), equivalently \(c_j=\lambda\mu^j\) for unimodular \(\lambda,\mu\). Also \(\|P\|_4^4=19\) exactly when \(\alpha\equiv\beta\pmod{2\pi}\) and \(\cos\alpha=-1/4\).

More precisely, for a four-point support \(A\subset\mathbb Z\), let \(T(A)\) be the number of three-term arithmetic progressions contained in \(A\), and let \(S(A)=1\) when the four points are centrally symmetric and \(S(A)=0\) otherwise. The only possible pairs are \((T,S)=(0,0),(1,0),(2,0),(0,1),(2,1)\), and the exact attainable ranges of \(\|P\|_4^4\) are respectively \(\{28\}\), \([24,32]\), \([20,36]\), \([20,36]\), and \([19,44]\).

The last case \((T,S)=(2,1)\) occurs exactly for a four-term arithmetic progression. Thus a four-term progression is simultaneously the support that permits the largest constructive fourth-moment interference and the strongest destructive interference among all four-frequency unimodular sums.

## Assumptions and scope
The domain is \(\mathbb T=\mathbb R/\mathbb Z\) with normalized Haar measure. Frequencies \(n_0<n_1<n_2<n_3\) are distinct integers and every coefficient has modulus one. No statement is made here for unequal coefficient magnitudes, five or more frequencies, noninteger frequencies, or exponents other than \(4\).

For a finite support \(A\), write \(T(A)\) for the number of three-element subsets \(\{{u,m,v}\}\subset A\) satisfying \(u+v=2m\). Write \(S(A)=1\) if, after ordering \(A=\{{n_0<n_1<n_2<n_3}\}\), one has \(n_0+n_3=n_1+n_2\), and \(S(A)=0\) otherwise.

## Proof
Parseval applied to \(P^2\) gives
\[
\|P\|_4^4=\sum_s\left|\sum_{{a,b\in A\atop a+b=s}}c_ac_b\right|^2.
\]
If the ten unordered pair sums \(a+b\) with \(a\le b\) were all distinct, the four diagonal pairs would each contribute \(1\), while the six off-diagonal pairs would each contribute \(4\); the baseline is therefore \(28\).

For four distinct integers there are only two possible kinds of collisions among unordered pair sums. A diagonal/off-diagonal collision is exactly a three-term progression \(u+v=2m\). Its fiber changes from the baseline contribution \(1+4=5\) to
\[
|c_m^2+2c_uc_v|^2=5+4\operatorname{{Re}}\!\left(c_m^2\overline{{c_uc_v}}\right).
\]
A collision of two different off-diagonal pairs cannot share a point, so it must be the unique partition relation \(n_0+n_3=n_1+n_2\). Its fiber changes from \(4+4=8\) to
\[
|2c_0c_3+2c_1c_2|^2=8+8\operatorname{{Re}}\!\left(c_0c_3\overline{{c_1c_2}}\right).
\]
No fiber can contain two such collisions: a fiber containing a diagonal pair and two distinct off-diagonal pairs would force one off-diagonal pair to contain the diagonal point, contradicting distinctness. Consequently
\[
\|P\|_4^4=28+4\sum_{{u+v=2m\atop \{{u,m,v}\}\subset A}}\operatorname{{Re}}\!\left(c_m^2\overline{{c_uc_v}}\right)
+8S(A)\operatorname{{Re}}\!\left(c_0c_3\overline{{c_1c_2}}\right).
\]

Ordering the support shows that at most two three-term progressions can occur. If \(S(A)=1\), central symmetry rules out exactly one three-term progression: either there are none, or the consecutive gaps are all equal, in which case there are two and \(A\) is a four-term arithmetic progression. Hence the only support types are \((0,0),(1,0),(2,0),(0,1),(2,1)\). For the first four types, the displayed formula immediately gives the exact ranges \(\{{28}\}\), \([24,32]\), \([20,36]\), and \([20,36]\); in the \((2,0)\) case the two progression phases are independent after fixing global and linear phase.

It remains to treat a four-term progression. Translation and dilation of the frequencies do not change the fourth moment, so write the support as \(\{{0,1,2,3}\}\). With
\[
\alpha=\arg\!\left(c_1^2\overline{{c_0c_2}}\right),\qquad
\beta=\arg\!\left(c_2^2\overline{{c_1c_3}}\right),
\]
the central-pair phase is \(-\alpha-\beta\), and therefore
\[
\|P\|_4^4=28+4\cos\alpha+4\cos\beta+8\cos(\alpha+\beta).
\]
Put \(u=(\alpha+\beta)/2\) and \(v=(\alpha-\beta)/2\). The nonconstant part divided by \(4\) is
\[
2\cos u\cos v+2\cos(2u).
\]
For fixed \(u\), minimizing over \(v\) gives \(-2|\cos u|+2\cos(2u)\). With \(t=|\cos u|\in[0,1]\), this is \(4t^2-2t-2\), whose minimum is \(-9/4\) at \(t=1/4\). Thus the global minimum is \(28-9=19\), and equality reduces to \(\alpha\equiv\beta\) with \(\cos\alpha=-1/4\). Maximizing over \(v\) gives \(2t+4t^2-2\), whose maximum is \(4\) at \(t=1\); hence the global maximum is \(44\), attained exactly at \(\alpha\equiv\beta\equiv0\). The latter relations are equivalent to \(c_j=\lambda\mu^j\).

## Verification
The accompanying `verify.py` reconstructs the fourth moment from exact frequency-collision fibers for every four-point subset of \(\{{0,1,\dots,18}\}\), verifies that only the five asserted support types occur, checks the idempotent values, and compares the closed formula with direct collision sums for deterministic phase samples. It also checks the displayed four-term-progression extremal witnesses. The finite computation is corroborative only; the proof above covers every integer support.

## Relationship to prior work
The Hardy--Littlewood majorant principle at even integer exponents supplies the general constructive-interference upper comparison, and Krenedits' study of three-term idempotent counterexamples emphasizes both the special role of even exponents and the four-term product examples used outside the even cases. That work does not state the exact four-frequency phase range, its five support types, or the lower extremizer at fourth moment.

Anderson--Ash--Jones--Rider--Saffari develop the harmonic-analysis setting of idempotent trigonometric polynomials and \(L^p\)-concentration. Their paper treats concentration phenomena rather than the global phase-sensitive fourth-moment classification here. Shao studies general additive-energy structure in torsion-free groups; those structural theorems do not encode unimodular coefficient phases or the exact four-point ranges.

## Limitations
The classification uses the torsion-free order structure of integer frequencies. In finite cyclic groups additional modular pair-sum collisions can occur. The result does not address the non-even Hardy--Littlewood majorant problem and does not imply an extremal theorem for more than four frequencies. An older equivalent small-cardinality formulation may exist under additive-energy or Freiman-isomorphism terminology even though no such statement was located in the checked sources.

## References
1. S. Krenedits, *Three-term idempotent counterexamples in the Hardy--Littlewood majorant problem*, arXiv:1006.0409, first public 2010-06-02; primary MSC 42A05.
2. B. Anderson, J. M. Ash, R. L. Jones, D. G. Rider, B. Saffari, *Exponential sums with coefficients 0 or 1 and concentrated \(L^p\) norms*, Annales de l'Institut Fourier 57 (2007), 1377--1404, arXiv:0705.0636.
3. X. Shao, *Large values of the additive energy in \(\mathbb R^d\) and \(\mathbb Z^d\)*, arXiv:1308.2247.
4. G. Mockenhaupt, W. Schlag, *On the Hardy--Littlewood majorant problem for random sets*, arXiv:math/0207226.
