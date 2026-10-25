# Exact 2-adic valuation on the exceptional Tripell progression

## Finding

Let \((T_n)_{n\ge0}\) be defined by
\[
T_0=0,\quad T_1=1,\quad T_2=2,\quad T_{n+3}=2T_{n+2}+T_{n+1}+T_n.
\]
On the exceptional progression \(n=1280+1792t\), where \(t\) is any nonnegative integer, there is a unique \(\tau\in\mathbb Z_2\) such that
\[
\boxed{\nu_2(T_{1280+1792t})=9+\nu_2(t-\tau)\quad(t\ge0).}
\]
Here \(\nu_2\) is the two-adic valuation extended to \(\mathbb Z_2\), with \(\nu_2(0)=+\infty\). The root is uniquely specified by compatible residues; for example,
\[
\tau\equiv0\pmod8,\quad \tau\equiv8\pmod{64},\quad
\tau\equiv72\pmod{128},\quad \tau\equiv200\pmod{256},\quad
\tau\equiv712\pmod{1024}.
\]

## Assumptions and scope

The recurrence and initial conditions above are the only assumptions. The index parameter is an integer \(t\ge0\). The result resolves the exact two-adic valuation on the one exceptional progression in the published partial valuation classification; it does not classify other index classes or valuations at odd primes.

## Proof

Use the companion matrix and state vector
\[
M=\begin{pmatrix}2&1&1\\1&0&0\\0&1&0\end{pmatrix},\quad
v_0=\begin{pmatrix}2\\1\\0\end{pmatrix},\quad
v_n=M^n v_0=\begin{pmatrix}T_{n+2}\\T_{n+1}\\T_n\end{pmatrix},
\]
and let \(e_3=(0,0,1)^T\). Direct multiplication gives
\[
M^7=I+2E,\qquad E=\begin{pmatrix}272&149&107\\107&58&42\\42&23&16\end{pmatrix}.
\]
Modulo two, \(E+E^2\equiv H\), where
\[
H=\begin{pmatrix}1&0&1\\1&1&1\\1&1&0\end{pmatrix}\not\equiv0\pmod2.
\]
For every \(r\ge1\), the binomial expansion yields
\[
M^{7\cdot2^r}\equiv I+2^{r+1}(E+E^2)\pmod{2^{r+2}}.
\]
Indeed, the linear and quadratic terms contribute \(2^{r+1}E\) and \(2^{r+1}E^2\) modulo \(2^{r+2}\); for \(j\ge3\), the valuation of \(2^j\binom{2^r}{j}\) is at least \(r+2\). Hence, for every \(j\ge0\),
\[
M^{1792\cdot2^j}=I+2^{j+9}H_j,\qquad H_j\equiv H\pmod2.
\]
A direct modular matrix-power calculation also gives
\[
T_{1280}\equiv4096\pmod{8192},\qquad
M^{1792}\equiv I\pmod{512},
\]
and
\[
e_3^T M^{1280}H v_0\equiv1\pmod2.
\]
Consequently every \(T_{1280+1792t}\) is divisible by \(2^9\), so
\[
F(t):=T_{1280+1792t}/2^9
\]
is an integer for every nonnegative integer \(t\).

Take integers \(t>s\ge0\), and write \(t-s=2^j u\) with \(u\) odd. The matrix lift above implies
\[
M^{1792(t-s)}-I\equiv 2^{j+9}uH_j\pmod{2^{j+10}}.
\]
Since \(M^{1792s}\equiv I\pmod2\), it follows that
\[
F(t)-F(s)\equiv 2^j u\,e_3^TM^{1280}Hv_0\equiv2^j\pmod{2^{j+1}}.
\]
Thus
\[
\nu_2(F(t)-F(s))=j=\nu_2(t-s).
\]
So \(F\) is an isometry on the nonnegative integers for the two-adic metric. Because the nonnegative integers are dense in \(\mathbb Z_2\), it extends uniquely to an isometry \(F:\mathbb Z_2\to\mathbb Z_2\). For every \(m\), this isometry induces an injective, hence bijective, map on the finite ring \(\mathbb Z/2^m\mathbb Z\). Therefore there is exactly one residue \(\tau_m\pmod{2^m}\) with \(F(\tau_m)\equiv0\pmod{2^m}\). These residues are compatible and determine a unique \(\tau\in\mathbb Z_2\) with \(F(\tau)=0\).

For every integer \(t\ge0\), the isometry identity now gives
\[
\nu_2(F(t))=\nu_2(F(t)-F(\tau))=\nu_2(t-\tau),
\]
which is the claimed formula after multiplying back by \(2^9\). Exact modular lifting gives the initial root residues listed in the Finding section. This proves both the valuation formula and uniqueness of the two-adic root.

## Verification

The standalone `verify.py` checks the exact matrix powers modulo powers of two, the odd coefficient \(e_3^TM^{1280}Hv_0\), the initial residue \(T_{1280}\bmod 2^{13}\), divisibility on 129 indices of the exceptional progression, 496 finite isometry comparisons, and the unique root lifts through \(2^{20}\). It prints `VERIFY_OK` and \(\tau\equiv534216\pmod{2^{20}}\). These finite checks corroborate the calculations; the matrix-lifting and completion argument establish the infinite claim.

## Relationship to prior work

Bravo, Díaz, and Ramírez give a partial two-adic valuation formula for the Tripell sequence in Theorem 1.3 of their 2020 paper. For \(n\equiv6\pmod{14}\), they obtain \(\nu_2(T_n)=\nu_2(n)+1\) except when \(n\equiv1280\pmod{1792}\); their proof explicitly notes that its induction does not handle this exceptional case. The same exception and limitation are reproduced in Chapter 5, Theorem 5.3 and Remark 5.1 of Díaz Noguera's 2022 doctoral thesis. The present result supplies an exact valuation law on that very progression by identifying a unique two-adic root and proving the normalized sequence is an isometry. It does not alter the previously established formulas on the other index classes.

## Limitations

The root \(\tau\) is specified two-adically and by its compatible residues, not by an elementary closed form. The theorem is limited to the exceptional progression for this Tripell recurrence. Searches were targeted rather than exhaustive, and an unindexed equivalent treatment remains a bibliographic risk. Independent mathematical audit has not been performed.

## References

1. J. J. Bravo, M. Díaz, and J. L. Ramírez, “The 2-adic and 3-adic valuation of the Tripell sequence and an application,” *Turkish Journal of Mathematics* 44 (2020), 131–141. DOI: 10.3906/mat-1907-40. First published online 11 November 2019. https://doi.org/10.3906/mat-1907-40
2. M. del C. Díaz Noguera, *p-adic valuation and linear forms in Fibonacci-like recurrence sequences*, doctoral thesis, Universidad del Cauca (June 2022), Chapter 5, Theorem 5.3 and Remark 5.1. https://repositorio.unicauca.edu.co/handle/123456789/4945
3. OEIS Foundation, sequence A077939, Tripell sequence definition and bibliography (not a source for the exceptional valuation law). https://oeis.org/A077939
