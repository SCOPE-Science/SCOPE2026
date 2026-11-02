# Uniform valuation shells of square-zero matrices over finite chain rings

## Finding

Let \(R\) be a finite commutative chain ring of length \(d\geq 1\), with maximal ideal \((\pi)\), residue field of cardinality \(q\), and \(\pi^d=0\). For an entry \(a\in R\), define \(\nu(a)\) by \(a\in(\pi^{\nu(a)})\setminus(\pi^{\nu(a)+1})\), with \(\nu(0)=d\). For a matrix \(X\in M_2(R)\), set \(\nu(X)\) to the minimum valuation of its four entries. Put \(h=\lceil d/2\rceil\).

**Uniform shallow-shell theorem.** For every integer \(s\) with \(0\leq s<h\),
\[
\#\{X\in M_2(R): X^2=0,\ \nu(X)=s\}=(q^2-1)q^{2d-2}.
\]
The count does not depend on \(s\), on the characteristic, or on the isomorphism type of \(R\) once \(q,d\) are fixed. All matrices with \(\nu(X)\geq h\) are square-zero, and their total number is \(q^{4\lfloor d/2\rfloor}\). Consequently,
\[
\#\{X\in M_2(R):X^2=0\}
=\lceil d/2\rceil(q^2-1)q^{2d-2}+q^{4\lfloor d/2\rfloor}.
\]
In particular, the first totals are \(q^2\) at length one, \(2q^4-q^2\) at length two, and \((2q^2-1)q^4\) at length three.

**Limit law.** Fix a residue-field size \(q\). For any sequence of such rings with lengths \(d\to\infty\), choose \(X_d\) uniformly among square-zero matrices. Then \(\nu(X_d)/d\) converges in distribution to the uniform probability measure on \([0,1/2]\), whose density on the interior of that interval is \(2\).

## Assumptions and scope

A finite commutative chain ring is a finite commutative local ring whose ideals form a chain. It has a generator \(\pi\) of its maximal ideal and a unique integer \(d\geq 1\) satisfying \(\pi^d=0\) and \(\pi^{d-1}\ne0\), with the convention that \(d=1\) covers fields. Every quotient \(R/(\pi^k)\) has \(q^k\) elements, and its residue field has \(q\) elements. The theorem requires no restriction on the characteristic or on \(q\) beyond \(q\) being a prime power. All matrix counts concern distinct matrices over the indicated ring, not similarity classes. The deep shell aggregates \(h\leq\nu(X)\leq d\), including the zero matrix.

For \(R=\mathbb F_q[t]/(t^d)\), the theorem counts exactly the square-zero elements in the matrix centralizer of \(J_d(0)\oplus J_d(0)\) over \(\mathbb F_q\). For \(R=\mathbb Z/p^d\mathbb Z\), it gives a mixed-characteristic instance with the same profile at \(q=p\).

## Proof

**Lemma 1 (primitive square-zero orbit).** Let \(S\) be a finite commutative chain ring of length \(k\geq1\) and residue cardinality \(q\). Exactly \((q^2-1)q^{2k-2}\) matrices \(Y\in M_2(S)\) satisfy \(Y^2=0\) and \(\nu(Y)=0\).

Indeed, reduction modulo the maximal ideal makes \(\bar Y\) a nonzero square-zero matrix of size two over the residue field. Therefore \(\bar Y\) has rank one. Choose a vector \(\bar v\) not in its kernel. The pair \((\bar Y\bar v,\bar v)\) is a basis. Lifting \(\bar v\) to \(v\in S^2\), Nakayama's elementary local-basis criterion shows that \((Yv,v)\) is an \(S\)-basis. Since \(Y(Yv)=0\) and \(Yv=Yv\), the matrix of \(Y\) in this basis is \(N=\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}\). Conversely, every conjugate of \(N\) is primitive and square-zero.

The invertible centralizer of \(N\) consists exactly of \(\begin{psmallmatrix}a&b\\0&a\end{psmallmatrix}\) with \(a\in S^\times\), \(b\in S\), and has cardinality \((q^k-q^{k-1})q^k\). Reduction to the residue field gives
\[
|\operatorname{GL}_2(S)|=q^{4(k-1)}(q^2-1)(q^2-q).
\]
Orbit-stabilizer therefore yields
\[
|\operatorname{GL}_2(S)\cdot N|
=\frac{q^{4(k-1)}(q^2-1)(q^2-q)}{(q^k-q^{k-1})q^k}
=(q^2-1)q^{2k-2},
\]
proving the lemma.

**Lemma 2 (constant shallow shells).** Fix \(0\leq s<h\). Multiplication by \(\pi^s\) identifies, entry by entry, \(R/(\pi^{d-s})\) bijectively with the ideal \((\pi^s)\subseteq R\). Thus every \(X\) with \(\nu(X)=s\) has a unique form \(X=\pi^sY\), with \(Y\) primitive over \(R/(\pi^{d-s})\). The square-zero equation is equivalent to \(Y^2\equiv0\pmod{\pi^{d-2s}}\), because \(2s<d\). Put \(k=d-2s\geq1\). The reduction of \(Y\) to \(R/(\pi^k)\) is primitive, and every primitive solution modulo \(\pi^k\) has exactly \(q^{4s}\) independent lifts to a matrix modulo \(\pi^{d-s}\). By Lemma 1, the number in the \(s\)-th shell is
\[
q^{4s}(q^2-1)q^{2k-2}
=(q^2-1)q^{2d-2},
\]
independent of \(s\).

**Deep shell and limit.** If every entry of \(X\) lies in \((\pi^h)\), then every entry of \(X^2\) lies in \((\pi^{2h})=0\). The ideal \((\pi^h)\) has \(q^{d-h}=q^{\lfloor d/2\rfloor}\) elements, giving \(q^{4\lfloor d/2\rfloor}\) matrices. These and the shallow shells partition the complete square-zero locus, proving the total.

The ratio of the deep mass to the mass of any single shallow shell is exactly \(1/(q^2-1)\) for odd \(d\), and \(q^2/(q^2-1)\) for even \(d\). It stays bounded as \(d\to\infty\), whereas there are \(h\sim d/2\) equally populated shallow shells. Hence the total deep mass is \(O(1/d)\); the rescaled shallow-shell uniform law is a Riemann sum converging to the uniform law on \([0,1/2]\). This proves the limit.

## Verification

The included `verify.py` program constructs two independent classes of chain-ring examples: truncated polynomial rings and prime-power residue rings. It enumerates all \(2\times2\) matrices in twenty small instances, tests the four entries of \(X^2\) directly, and compares exact valuation profiles with the theorem. The polynomial-ring cases include the nonprime residue field \(\mathbb F_4\). The last line is `VERIFY_OK: 20 finite configurations`. Reproduce with `python verify.py` in an environment with Python 3 and no third-party packages. These computations are finite corroboration; Lemmas 1 and 2 establish the unrestricted statement.

## Relationship to prior work

Bogdanić, Đurić, Koljančić, Oblak and Šivic (arXiv:2212.08425, submitted December 16, 2022) classify the nilpotent Jordan types that occur in the centralizer of two equal nilpotent Jordan blocks. Their Section 2 identifies this centralizer with \(M_2(\mathbb F_q[t]/(t^d))\), and Section 3 classifies possible Jordan partitions rather than the valuation-resolved numbers of square-zero elements. The present theorem quantitatively refines this natural centralizer problem and extends the finite count to arbitrary finite commutative chain rings.

Carnevale, Shechter and Voll (arXiv:1709.02717) enumerate traceless matrices over finite local quotients by image sizes and elementary divisors; such linear trace-and-rank restrictions do not by themselves impose the nonlinear equation \(X^2=0\). Cheong, Liang and Strand (arXiv:2209.03626) count solutions of matrix polynomial equations modulo prime powers under a square-free reduction hypothesis. This hypothesis excludes the repeated-root polynomial defining square-zero matrices. Brawley's 1982 index-counting work discusses general finite rings and might imply an unrefined total for some rings, but indexing by nilpotency degree does not itself resolve how the solutions split across entry-valuation shells.

## Limitations

Only \(2\times2\) matrices are classified, and the ring must be commutative with a principal chain of ideals; no formula is claimed for higher matrix sizes or arbitrary finite local rings. The deep region is counted in aggregate, not resolved into the individual valuations of its automatically square-zero entries. The limit concerns increasing ring lengths and fixed residue-field size, not increasing matrix size. Published treatments using alternate descriptions of local matrix orbits may contain equivalent shell identities; this priority risk is not mathematically eliminated by search alone.

## References

1. D. Bogdanić, A. Đurić, S. Koljančić, P. Oblak, and K. Šivic, *Jordan structures of nilpotent matrices in the centralizer of a nilpotent matrix with two Jordan blocks of the same size*, arXiv:2212.08425 (first posted December 16, 2022), https://arxiv.org/abs/2212.08425.
2. A. Carnevale, S. Shechter, and C. Voll, *Enumerating traceless matrices over compact discrete valuation rings*, arXiv:1709.02717 (2017), https://arxiv.org/abs/1709.02717.
3. G. Cheong, Y. Liang, and M. Strand, *Polynomial equations for matrices over integers modulo a prime power and the cokernel of a random matrix*, arXiv:2209.03626 (2022), https://arxiv.org/abs/2209.03626.
4. J. V. Brawley, *Counting matrices by Drazin index*, SIAM Journal on Algebraic and Discrete Methods **3** (1982), 30–34, https://doi.org/10.1137/0603003.
