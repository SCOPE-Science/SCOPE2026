# Trace strata of rank-one regular integral matrices
## Finding
Let \(A\in M_2(\mathbb Z)\) be a nonzero rank-one von Neumann regular matrix and set \(t=\operatorname{tr}(A)\). Then \(A\) is \(\operatorname{GL}_2(\mathbb Z)\)-similar to \(B(t,b)=\begin{pmatrix}t&b\\0&0\end{pmatrix}\) with \(\gcd(t,b)=1\). If \(t\ne0\), two such normal forms with the same trace are similar if and only if \(b'\equiv\pm b\pmod{|t|}\); if \(t=0\), there is one similarity class. Consequently, for \(n=|t|>0\), the similarity classes form \((\mathbb Z/n\mathbb Z)^\times/\{\pm1\}\), with one class for \(n=1,2\) and \(\varphi(n)/2\) classes for \(n>2\). Exactly one class in every trace stratum is fine: the class represented by \(b\equiv\pm1\pmod n\). Hence every rank-one regular matrix of trace \(t\) is fine exactly for \(|t|\in\{0,1,2,3,4,6\}\); for \(n>2\), the number of non-fine similarity classes at trace magnitude \(n\) is \(\varphi(n)/2-1\).

For prime \(p\ge5\), there are \((p-1)/2\) rank-one regular similarity classes at each trace \(t=\pm p\), only one of which is fine. Thus the fine-class proportion in these trace strata is \(2/(p-1)\), which tends to \(0\) along the primes. The matrix \(\begin{pmatrix}5&3\\0&0\end{pmatrix}\) used in the 2026 source is the first possible trace magnitude at which a non-fine rank-one regular similarity class occurs.

## Assumptions and scope
All matrices are \(2\times2\) matrices over \(\mathbb Z\). Similarity means conjugacy by \(\operatorname{GL}_2(\mathbb Z)\). A nonzero element is called fine when it is a sum of a unit and a nilpotent. The finding concerns only nonzero rank-one von Neumann regular matrices; it does not classify invertible matrices, higher-dimensional matrices, or matrices over other coefficient rings.

The motivating 2026 paper proves that a nonzero singular matrix in \(M_2(\mathbb Z)\) is von Neumann regular exactly when its entries are collectively coprime, and uses \(\begin{pmatrix}5&3\\0&0\end{pmatrix}\) as a regular non-fine witness. The 2016 fine-ring paper proves that \(\begin{pmatrix}a&b\\0&0\end{pmatrix}\) is fine exactly when \(b\equiv\pm1\pmod a\).

## Proof
Let \(A\) be nonzero, rank one, and regular. By Theorem 3.2 of Al-Mallah--Călugăreanu, the entries of \(A\) have greatest common divisor \(1\). Equivalently, the first determinantal divisor of \(A\) is \(1\), so its Smith normal form is \(\operatorname{diag}(1,0)\). Hence
\[
A=u v^{\mathsf T}
\]
for primitive integer vectors \(u,v\in\mathbb Z^2\). In particular, \(\operatorname{im}(A)=\mathbb Zu\), and
\[
t=\operatorname{tr}(A)=v^{\mathsf T}u.
\]
Choose \(w\in\mathbb Z^2\) such that \((u,w)\) is a unimodular basis. In this basis, \(A\) has matrix
\[
B(t,b)=\begin{pmatrix}t&b\\0&0\end{pmatrix},\qquad b=v^{\mathsf T}w.
\]
Since \(v\) is primitive and \((u,w)\) is unimodular, the coordinate row \((t,b)=v^{\mathsf T}(u,w)\) is primitive, so \(\gcd(t,b)=1\). This proves existence of the normal form.

Assume next that \(t\ne0\). The image of \(B(t,b)\) over \(\mathbb Q\) is the unique eigenspace for the nonzero eigenvalue \(t\). Therefore, if
\[
P^{-1}B(t,b)P=B(t,b')
\]
with \(P\in\operatorname{GL}_2(\mathbb Z)\), then \(P\) preserves the primitive line \(\mathbb Ze_1\). Thus
\[
P=\begin{pmatrix}\varepsilon&m\\0&\delta\end{pmatrix},
\qquad \varepsilon,\delta\in\{\pm1\},\quad m\in\mathbb Z.
\]
A direct multiplication gives
\[
P^{-1}B(t,b)P
 =B\bigl(t,\varepsilon tm+\varepsilon\delta b\bigr).
\]
Hence similarity implies \(b'\equiv\pm b\pmod{|t|}\). Conversely, if this congruence holds, suitable choices of \(\varepsilon,\delta,m\) in the displayed formula give a conjugating matrix, so the congruence is also sufficient.

If \(t=0\), primitivity forces \(|b|=1\); the two matrices \(B(0,1)\) and \(B(0,-1)\) are conjugate by a diagonal unimodular matrix. Hence there is exactly one trace-zero class.

Now fix \(n=|t|>0\). The condition \(\gcd(t,b)=1\) says exactly that the residue of \(b\) is a unit modulo \(n\), while similarity identifies a residue with its negative. Thus the trace stratum is \((\mathbb Z/n\mathbb Z)^\times/\{\pm1\}\). For \(n>2\), multiplication by \(-1\) has no fixed point on the unit group, so the number of classes is \(\varphi(n)/2\); for \(n=1,2\), there is one class.

Fineness is invariant under similarity, because conjugating a decomposition into a unit plus a nilpotent preserves both properties. Corollary 5.4 of Călugăreanu--Lam says that \(B(t,b)\) is fine exactly when \(b\equiv\pm1\pmod t\). Hence exactly one similarity class in each nonzero trace stratum is fine. At trace zero, \(b=\pm1\), and the same criterion (or the explicit decomposition \(B(0,1)=\begin{pmatrix}0&1\\-1&0\end{pmatrix}+\begin{pmatrix}0&0\\1&0\end{pmatrix}\)) shows that the unique class is fine.

Therefore all classes at trace magnitude \(n>0\) are fine exactly when \((\mathbb Z/n\mathbb Z)^\times=\{\pm1\}\), equivalently \(\varphi(n)\le2\). The standard classification of the positive integers with \(\varphi(n)\le2\) gives \(n\in\{1,2,3,4,6\}\). Including \(t=0\) yields the stated set \(\{0,1,2,3,4,6\}\). For \(n>2\), subtracting the single fine class from the total gives \(\varphi(n)/2-1\) non-fine classes.

## Verification
The proof is symbolic and does not infer an infinite statement from computation. The included script `verify_rank_one_fine.py` performs two bounded sanity checks: it verifies the stated upper-triangular conjugation formula over a finite parameter box, and it enumerates unit residues modulo \(n\le100\) to confirm the class-count formula and the exceptional magnitudes \(1,2,3,4,6\). Its output ends with `CHECK_OK`.

The critical external premises were checked in primary sources: Theorem 3.2 of the 2026 paper gives the regularity/content criterion for singular \(2\times2\) matrices, while Corollary 5.4 of the 2016 paper gives the exact fine criterion for the row normal form.

## Relationship to prior work
Al-Mallah and Călugăreanu introduce regular-fine rings and show that \(M_2(\mathbb Z)\) is not regular-fine by exhibiting the single regular non-fine matrix \(\begin{pmatrix}5&3\\0&0\end{pmatrix}\). They do not classify the rank-one regular locus by similarity or determine how fineness is distributed across its trace strata.

Călugăreanu and Lam prove the coordinate criterion for a matrix already in the form \(\begin{pmatrix}a&b\\0&0\end{pmatrix}\), but do not combine it with a similarity classification of the regular rank-one locus. The older integral-similarity literature, including Shevchenko--Sidorov and the later general algorithmic work of Eick--Hofmann--O'Brien, addresses integral matrix similarity itself; it predates the 2026 regular-fine question and does not state the fine-locus stratification above. In particular, the Eick--Hofmann--O'Brien algorithm is formulated for matrices in \(\operatorname{GL}_n(\mathbb Q)\), whereas the matrices here are singular.

The new point is therefore not a new general similarity algorithm, but the exact coupling of the primitive rank-one similarity invariant with fineness: each trace stratum has a residue-class quotient, and fineness selects exactly its distinguished identity orbit.

## Limitations
The argument is specific to rank one in \(M_2(\mathbb Z)\). It does not determine fine decompositions for arbitrary singular matrices over other principal ideal domains, nor does it address higher-rank regular matrices in larger matrix rings. The 2006 second-order integral-similarity paper was identifiable and bibliographically inspected, but its full text was not available in the accessible source used here; it remains a residual risk for whether the bare residue-class normal form appears there. That risk does not cover the fine-locus statement, since fine elements were introduced later and the exact coupling uses the 2016 fine criterion together with the 2026 regularity setting.

## References
1. O. Al-Mallah and G. Călugăreanu, “Rings whose von Neumann regular elements are fine,” *International Electronic Journal of Algebra* 40 (2026), 198–209. DOI: `10.24330/ieja.1943809`. Published online May 4, 2026.
2. G. Călugăreanu and T. Y. Lam, “Fine rings: A new class of simple rings,” *Journal of Algebra and Its Applications* 15 (2016), 1650173. DOI: `10.1142/S0219498816501735`.
3. V. N. Shevchenko and S. V. Sidorov, “On the similarity of second-order matrices over the ring of integers,” *Russian Mathematics* 50(4) (2006), 56–63.
4. B. Eick, T. Hofmann, and E. A. O'Brien, “The conjugacy problem in \(\operatorname{GL}(n,\mathbb Z)\),” *Journal of the London Mathematical Society* 100 (2019), 731–756. DOI: `10.1112/jlms.12246`.
