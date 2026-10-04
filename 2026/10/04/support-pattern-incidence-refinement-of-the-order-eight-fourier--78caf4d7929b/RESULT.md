# Support-pattern incidence refinement of the order-eight Fourier uncertainty diagram
## Finding
For the unnormalized order-eight discrete Fourier transform on \(\mathbb Z_8\), define
\[
I_8(k,\ell)=\#\bigl\{(S,T):S,T\subseteq\mathbb Z_8,\ S,T\neq\varnothing,\ |S|=k,\ |T|=\ell,\ \exists f\neq0:\operatorname{supp}(f)=S,\ \operatorname{supp}(\widehat f)=T\bigr\}.
\]
Then, with rows indexed by \(k=1,\ldots,8\) and columns by \(\ell=1,\ldots,8\),
\[
\begin{pmatrix}
0 & 0 & 0 & 0 & 0 & 0 & 0 & 8 \\
0 & 0 & 0 & 8 & 0 & 32 & 128 & 28 \\
0 & 0 & 0 & 32 & 0 & 1056 & 384 & 56 \\
0 & 8 & 32 & 148 & 2176 & 1736 & 544 & 70 \\
0 & 0 & 0 & 2176 & 2816 & 1536 & 448 & 56 \\
0 & 32 & 1056 & 1736 & 1536 & 784 & 224 & 28 \\
0 & 128 & 384 & 544 & 448 & 224 & 64 & 8 \\
8 & 28 & 56 & 70 & 56 & 28 & 8 & 1
\end{pmatrix}.
\]
Consequently there are exactly \(20{,}929\) realizable ordered pairs \((S,T)\) of nonempty time and frequency supports.

The affine time-frequency symmetries
\[
(S,T)\longmapsto(a+uS,b+u^{-1}T),
\qquad a,b\in\mathbb Z_8,\quad u\in\mathbb Z_8^\times,
\]
partition the \(20{,}929\) realizable pairs into exactly \(205\) orbits. Their orbit-size distribution is
\[
1^1,\ 2^2,\ 4^7,\ 8^{22},\ 16^{19},\ 32^{18},\ 64^{30},\ 128^{72},\ 256^{34},
\]
where \(q^m\) here means \(m\) orbits of size \(q\). Adjoining Fourier duality \((S,T)\mapsto(T,-S)\) gives exactly \(108\) orbits, with sizes
\[
1^1,\ 4^2,\ 8^3,\ 16^{12},\ 32^9,\ 64^{13},\ 128^{17},\ 256^{34},\ 512^{17}.
\]

## Assumptions and scope
Write \(\zeta_8=e^{2\pi i/8}\) and use
\[
\widehat f(r)=\sum_{x\in\mathbb Z_8} f(x)\zeta_8^{rx}.
\]
Changing the Fourier normalization or conjugating the root changes no support set. The ordered pair \((S,T)\) records the actual locations of the nonzero coordinates, not only the two support cardinalities. The claim is a finite classification for order eight.

## Proof
Fix nonempty \(S,T\subseteq\mathbb Z_8\), let \(Z=\mathbb Z_8\setminus T\), and let
\[
A_{Z,S}=(\zeta_8^{rs})_{r\in Z,\ s\in S}.
\]
A vector supported inside \(S\) has Fourier transform vanishing outside \(T\) exactly when its coefficient vector lies in \(K=\ker A_{Z,S}\).

There is a vector in \(K\) with every time coordinate in \(S\) nonzero and every Fourier coordinate in \(T\) nonzero if and only if all of the following hold: \(\operatorname{rank}A_{Z,S}<|S|\); deleting any one column leaves the rank unchanged; and adjoining any one row indexed by \(t\in T\) raises the rank by one. The second condition says that no coordinate functional on \(K\) is identically zero. The third says the same for each desired Fourier-coordinate functional. If all these finitely many functionals are nonzero on \(K\), their proper kernels cannot cover the complex vector space \(K\), so one vector avoids all of them simultaneously. Conversely, failure of any condition forces a required coordinate to vanish for every vector in \(K\).

The supplied verifier evaluates this criterion for every one of the \((2^8-1)^2=65{,}025\) ordered nonempty support-set pairs. Every matrix rank is computed exactly in
\[
\mathbb Q(\zeta_8)=\mathbb Q[z]/(z^4+1)
\]
with rational coefficients, so no floating-point zero test occurs. Summing the resulting incidence matrix gives \(20{,}929\).

Time translation, modulation, and multiplication of the cyclic index by a unit preserve exact support realizability and induce the stated affine action. Exhausting that finite group gives \(205\) affine orbits. Fourier inversion sends exact support pairs by \((S,T)\mapsto(T,-S)\); adjoining this symmetry and recomputing the finite orbits gives \(108\).

## Verification
Run `python verify_z8_support_incidence.py`. The script uses only the Python standard library. It constructs the full \(256\times256\) rank table over \(\mathbb Q(\zeta_8)\), applies the exact-support rank criterion to all \(65{,}025\) nonempty support-set pairs, verifies the displayed incidence matrix and total, and recomputes both orbit partitions. A successful replay ends with `VERIFY_OK`.

## Relationship to prior work
Meshulam established sharp divisor-based lower bounds for finite-group Fourier support. Delvaux and Van Barel studied rank-deficient submatrices of Fourier matrices of prime-power order and the associated Hamming-weight uncertainty profile. Bonami and Ghobber explicitly distinguish exact-support questions, but their classified cyclic prime-power family is \(\mathbb Z_{p^2}\), not \(\mathbb Z_8\).

Yang, Zhang, Wang, Geng, and Chen later study the uncertainty diagram of a general DFT. Their Lemma 2 gives a rank criterion equivalent in substance to the exact-support criterion above, and their order-eight panel records which cardinality pairs \((k,\ell)\) occur or are holes. In particular, that publication owns the size-level order-eight uncertainty diagram. The present claim is different: it counts, for every size pair, how many actual ordered support-set pairs \((S,T)\) are realizable, and then classifies those support patterns under two explicit symmetry groups. The published size diagram is only the zero-versus-positive shadow of the matrix \(I_8\) and does not determine its entries or orbit counts.

## Limitations
This is an exact finite invariant of the order-eight DFT, not a formula for all cyclic groups. The incidence counts depend on support locations, while the final orbit counts depend on the explicitly stated symmetry actions. Targeted searches found no prior table of these counts or orbit totals, but differently phrased or poorly indexed prior computations remain a residual originality risk.

## References
1. R. Meshulam, *An uncertainty inequality for finite abelian groups*, arXiv:math/0312407, first posted 2003-12-22.
2. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Fourier matrices*, K.U. Leuven Report TW 470, September 2006; later Linear Algebra Appl. 429 (2008), 1587--1605.
3. A. Bonami and S. Ghobber, *Equality cases for the uncertainty principle in finite Abelian groups*, arXiv:1003.5060, first posted 2010-03-26.
4. Y.-H. Yang, B.-B. Zhang, X.-L. Wang, S.-J. Geng, and P.-Y. Chen, *Characterizing Kirkwood-Dirac nonclassicality and uncertainty diagram based on discrete Fourier transform*, arXiv:2303.17203, first posted 2023-03-30.
