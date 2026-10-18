# Almost-realizability rigidity for Raney number sequences

## Finding
For all positive integers \(p,r\), put
\[
R_{p,r}(n)=\frac{r}{pn+r}\binom{pn+r}{n}\qquad(n\geq1).
\]
The positive-integer sequence \((R_{p,r}(n))_{n\geq1}\) is **almost realizable** (some positive integer multiple counts fixed points of all iterates of a self-map) **if and only if** \((p,r)=(1,1)\). In that sole case, \(R_{1,1}(n)=1\) for all \(n\), realized by the identity map on a singleton.

The obstruction is explicit. For every prime \(\ell>\max\{p,r\}\),
\[
R_{p,r}(\ell)-R_{p,r}(1)\equiv p-r\pmod\ell.
\]
On the diagonal \(p=r=s\geq2\), where that prime test vanishes, every odd prime \(\ell>2s\) satisfies
\[
R_{s,s}(2\ell)-R_{s,s}(\ell)-R_{s,s}(2)+R_{s,s}(1)
\equiv \frac{s(s-1)}2\pmod\ell.
\]
These two residues exclude every nontrivial parameter pair because infinitely many primes cannot divide a fixed nonzero integer.

## Assumptions and scope
All parameters \(p,r,n\) are positive integers; prime indices \(\ell\) are ordinary rational primes, and \(\ell\) is chosen larger than explicitly stated fixed parameters. The indexing begins at \(n=1\). The numbers are integers: for the unique integral formal power series \(U(z)\) satisfying \(U(z)=1+zU(z)^p\), Lagrange inversion gives
\[
[z^n]U(z)^r=\frac rn\binom{pn+r-1}{n-1}=R_{p,r}(n).
\]
The recurrence for \(U\) ensures integral coefficients, hence \(R_{p,r}(n)\in\mathbb Z_{>0}\). Equivalently, these are the standard Raney numbers counting generalized plane-tree structures, as in Beagley--Drube [1].

A sequence \((a_n)_{n\ge1}\) is realizable if there is a self-map \(T\) of a set with \(a_n=\#\operatorname{Fix}(T^n)\) for every \(n\ge1\). It is almost realizable if \((M a_n)\) is realizable for at least one fixed positive integer \(M\). For such a multiple, the Dold divisibility conditions require
\[
n\mid M\sum_{d\mid n}\mu(n/d)a_d\quad\text{for every }n\ge1.
\]
Only this necessary condition is used to establish nonrealizability; no sign assumptions are needed in the obstruction. See [2,3].

## Proof
**Integral formula.** The stated Lagrange-inversion identity follows by writing \(W=U-1=z(1+W)^p\), so
\[
[z^n](1+W(z))^r=\frac rn[t^{n-1}](1+t)^{pn+r-1}.
\]
For positive integer parameters, coefficient integrality also follows combinatorially [1].

**Off the parameter diagonal.** Suppose \(p\ne r\). Let \(\ell>\max\{p,r\}\) be prime. Lucas's binomial congruence in base \(\ell\) gives
\[
\binom{p\ell+r}{\ell}\equiv\binom p1\binom r0=p\pmod\ell.
\]
Because \(p\ell+r\equiv r\not\equiv0\pmod\ell\), division in the formula for \(R\) yields \(R_{p,r}(\ell)\equiv p\pmod\ell\). Directly \(R_{p,r}(1)=r\). Thus at the prime index \(\ell\) the Möbius sum is congruent to \(p-r\) modulo \(\ell\). If a fixed positive integer \(M\) made the sequence realizable, Dold divisibility would force \(\ell\mid M(p-r)\) for **every** sufficiently large prime \(\ell\), contradicting \(M(p-r)\ne0\).

**On the diagonal.** Put \(p=r=s\geq2\). Simplification gives
\[
a_n=R_{s,s}(n)=\frac{1}{n+1}\binom{s(n+1)}n,
\quad a_1=s,\quad a_2=\frac{s(3s-1)}2.
\]
For odd primes \(\ell>2s\), Lucas's theorem (now applied with the denominator \(n+1\) invertible modulo \(\ell\)) yields
\[
a_\ell\equiv \binom s1=s\pmod\ell,
\qquad
 a_{2\ell}\equiv \binom{2s}2=s(2s-1)\pmod\ell.
\]
The four divisors of \(2\ell\) are \(1,2,\ell,2\ell\). Their Möbius-weighted sum is consequently
\[
\begin{aligned}
(\mu*a)(2\ell)
&=a_{2\ell}-a_\ell-a_2+a_1\\
&\equiv s(2s-1)-s-\frac{s(3s-1)}2+s\\
&=\frac{s(s-1)}2\pmod\ell.
\end{aligned}
\]
The residue on the right is a fixed nonzero integer. If a fixed multiplier \(M\) made \((Ma_n)\) realizable, Dold divisibility at \(2\ell\) would imply \(\ell\mid M s(s-1)/2\) for every odd prime \(\ell>2s\). This is impossible. Note that reduction modulo \(\ell\) is enough: divisibility by \(2\ell\) necessarily implies divisibility by \(\ell\).

**Exceptional parameter pair.** At \((p,r)=(1,1)\), the definition reduces to \(R_{1,1}(n)=\frac1{n+1}\binom{n+1}{n}=1\). A singleton fixed by its unique self-map has one fixed point at every iterate; hence the sequence is realizable, completing the proof. \(\square\)

## Verification
The standalone Python 3 standard-library checker `artifacts/verify.py` evaluates Raney numbers by exact integer arithmetic and independently verifies the displayed modular certificates for a finite parameter-and-prime grid. Replay from the same directory with `python3 artifacts/verify.py`. The resulting checked output is stored in `artifacts/verify_output.txt`. Checks cover 2,880 positive integer values, 1,942 prime-index congruences, 203 diagonal twice-prime Möbius congruences, and 200 constant-sequence terms. The all-parameter theorem follows from the unrestricted modular proof above, **not** from the finite checks.

## Relationship to prior work
Beagley and Drube [1] define the same two-parameter Raney numbers and give general tree interpretations; their enumerative results do not assert dynamical almost-realizability criteria. Byszewski, Graff, and Ward [2] survey Dold sequences, dynamic realizability and almost-realizability, and record the earlier result that a polynomial Dold sequence must be constant; this already addresses the polynomial subfamily \(p=1\), but not the nonpolynomial full Raney classification. Zhang [3] proves that the ordinary Catalan-number sequence \(R_{2,1}(n)\) (among other combinatorial sequences) is not almost realizable. The prime-index obstruction used here is akin to Zhang's Catalan argument, and the use of twice-prime Möbius sums is related to Zhang's treatment of Motzkin numbers. Zhang's Theorem 21 concerns the Catalan, Motzkin and Schröder sequences, not all Raney parameter pairs, and does not state the diagonal \(p=r\) criterion. The new assertion is the complete uniform two-parameter classification, including its fixed nonzero diagonal obstruction.

## Limitations
The classification assumes integer \(p,r\geq1\), indexes \(n\geq1\), and the standard unshifted Raney sequence. It says nothing about separately shifting or subsequencing the index, replacing parameters by arbitrary reals, or about other generalized Catalan families. The result is a statement of necessary Dold obstructions plus the one trivial realizable case; it does not supply a general positive dynamical construction. Literature comparisons do not rule out an equivalent theorem in unindexed or inaccessible sources. There has been no independent audit or formal proof-assistant certification.

## References
[1] J. E. Beagley and P. Drube, *Generalized Catalan Numbers and the Enumeration of Planar Embeddings*, arXiv:1501.07137v1 (2015), https://arxiv.org/pdf/1501.07137.

[2] J. Byszewski, G. Graff, and T. Ward, *Dold sequences, periodic points, and dynamics*, arXiv:2007.04031v4 (2021), https://arxiv.org/html/2007.04031v4.

[3] G.-R. Zhang, *Realizability of Some Combinatorial Sequences*, arXiv:2302.09454v1 (first public 19 February 2023), revised 2024, *J. Integer Sequences* **27** (2024), Article 24.3.3, https://arxiv.org/html/2302.09454v2.
