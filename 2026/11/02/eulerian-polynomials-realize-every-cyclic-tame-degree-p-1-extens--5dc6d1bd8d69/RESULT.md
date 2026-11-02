# Eulerian polynomials realize every cyclic tame degree-\(p-1\) extension of \(\mathbb Q_p\)

## Finding
For every odd prime \(p\), let the monic descent Eulerian polynomial be
\[
E_n(X)=\sum_{j=0}^{n-1}\left\langle {n\atop j}\right\rangle X^j,\qquad n\ge1,
\]
where the coefficient counts permutations of \(n\) letters with exactly \(j\) descents. For each \(0\le t\le p-2\), the polynomial \(E_{p+t}\) admits a unique monic factorization over \(\mathbb Z_p\) of the form
\[
E_{p+t}(X)=F_{p,t}(X)G_{p,t}(X),\qquad
\deg F_{p,t}=p-1,\quad\deg G_{p,t}=t,
\]
with
\[
F_{p,t}(X)\equiv1+X+\cdots+X^{p-1},\qquad
G_{p,t}(X)\equiv E_{t+1}(X)\pmod p.
\]
The distinguished factor satisfies
\[
\frac{F_{p,t}(1)}p\equiv-\frac1{t+1}\pmod p,
\]
and \(F_{p,t}(1+Y)\) is Eisenstein at \(p\). For **any** root \(\alpha\) of \(F_{p,t}\), the associated local field has the explicit isomorphism
\[
\boxed{\mathbb Q_p(\alpha)\simeq
\mathbb Q_p\!\left(\sqrt[p-1]{\frac p{t+1}}\right).}
\]
As \(t\) ranges from \(0\) to \(p-2\), these \(p-1\) fields are pairwise nonisomorphic and exhaust **all** cyclic totally tamely ramified extensions of \(\mathbb Q_p\) of degree \(p-1\).

## Assumptions and scope
The prime \(p\) is odd; \(t\) is an integer with \(0\le t\le p-2\). The ring \(\mathbb Z_p\), field \(\mathbb Q_p\), reduction \(\pmod p\), and valuation \(\nu_p(p)=1\) are conventional. The Eulerian normalization has constant coefficient 1, leading coefficient 1, and \(E_n(1)=n!\). Some references instead use \(A_n(X)=XE_n(X)\); that is not the polynomial called \(E_n\) here. The factor \(F_{p,t}\) is defined by the specified **local** Hensel lifting; no assertion is made that \(E_{p+t}\) is irreducible over \(\mathbb Q\) for \(t>0\). Every statement is for the entire indicated range of primes and indices, not just those computed.

## Proof
**1. The prime-block congruence.** Eulerian numbers satisfy the standard inclusion-exclusion formula
\[
\left\langle {n\atop j}\right\rangle
=\sum_{i=0}^{j+1}(-1)^i\binom{n+1}{i}(j+1-i)^n.
\]
For \(n=p\) and \(0\le j\le p-1\), all terms except \(i=0,1\) vanish modulo \(p\). (At the upper endpoint, the potentially extra term \(i=p\) has zero base.) Fermat's congruence gives \(\left\langle {p\atop j}\right\rangle\equiv(j+1)^p-j^p\equiv1\pmod p\). Consequently, writing \(\Phi_p(X)=1+X+\cdots+X^{p-1}\),
\[
E_p(X)\equiv\Phi_p(X)\equiv(X-1)^{p-1}\pmod p.
\]
The Eulerian recurrence is
\[
E_{n+1}(X)=(1+nX)E_n(X)+X(1-X)E_n'(X).
\]
In characteristic \(p\), \((1-X)\Phi_p'(X)=\Phi_p(X)\). Substituting \(E_{p+t}\equiv\Phi_p E_{t+1}\) into the recurrence, using \(p+t\equiv t\pmod p\), yields \(E_{p+t+1}\equiv\Phi_p E_{t+2}\). Induction proves
\[
\boxed{E_{p+t}(X)\equiv\Phi_p(X)E_{t+1}(X)\pmod p}
\]
for every \(0\le t\le p-2\).

**2. The distinguished Hensel factor.** The polynomial \(E_{t+1}\) has degree \(t\), is monic, and satisfies \(E_{t+1}(1)=(t+1)!\), a unit modulo \(p\). Thus the two monic factors \(\Phi_p=(X-1)^{p-1}\) and \(E_{t+1}\) are coprime over \(\mathbb F_p\). Monic Hensel lifting produces the indicated unique factorization in \(\mathbb Z_p[X]\). Since \(E_{p+t}(1)=(p+t)!\) and \(p\le p+t\le2p-2\), exactly one factor \(p\) divides this factorial; \(G_{p,t}(1)\) is a unit. Thus \(\nu_p(F_{p,t}(1))=1\). Moreover, Wilson's theorem gives
\[
\frac{(p+t)!}{p}=(p-1)!\prod_{a=1}^{t}(p+a)
\equiv-t!\pmod p,
\]
while \(G_{p,t}(1)\equiv(t+1)!\pmod p\). Dividing yields
\[
\frac{F_{p,t}(1)}p\equiv-\frac1{t+1}\pmod p.
\]

**3. Eisenstein and the Kummer class.** Since \(F_{p,t}(X)\equiv(X-1)^{p-1}\pmod p\), the translated polynomial \(F_{p,t}(1+Y)\) is monic of degree \(e=p-1\), has all nonleading coefficients divisible by \(p\), and has constant term divisible by \(p\) but not \(p^2\). It is Eisenstein, so \(K=\mathbb Q_p(\alpha)\) has degree \(e\), is totally ramified, and \(\pi=\alpha-1\) is a uniformizer. The translated polynomial identity and the preceding constant-term computation imply, in its residue field,
\[
\frac{\pi^e}{p}\equiv-\frac{F_{p,t}(1)}p
\equiv\frac1{t+1}\pmod{\pi}.
\]
Therefore the unit \(u=\pi^e/(p/(t+1))\) satisfies \(u\equiv1\pmod\pi\). Since \(e=p-1\) is coprime to \(p\), Hensel's lemma applied to \(W^e-u\) at \(W=1\) produces \(w\in\mathcal O_K^\times\) with \(w^e=u\). Put \(\eta=\pi/w\). Then \(\eta^e=p/(t+1)\) and \(\nu_K(\eta)=1\), so \(K=\mathbb Q_p(\eta)\). Finally, \(\mathbb Q_p\) contains the \(e\)-th roots of unity (their distinct reductions lift by Hensel), hence \(K/\mathbb Q_p\) is cyclic, Galois, and tame of degree \(e\).

**4. No repetitions and no missing fields.** The standard tame Kummer classification may also be proved directly here: any cyclic totally ramified extension of degree \(e=p-1\) admits a uniformizer \(\varpi\); its Eisenstein equation gives \(\varpi^e/p\) a nonzero residue \(a\in\mathbb F_p^\times\), and a principal-unit \(e\)-th-root adjustment makes \(\varpi^e=p\widetilde a\), for any chosen lift \(\widetilde a\in\mathbb Z_p^\times\) of \(a\). Thus every such field is some \(\mathbb Q_p(\sqrt[e]{p\widetilde a})\), with exactly \(p-1\) possible residue classes. Conversely, because \(\mu_e\subset\mathbb Q_p\), Kummer theory says two degree-\(e\) radical fields coincide precisely when their classes in \(\mathbb Q_p^\times/(\mathbb Q_p^\times)^e\) generate the same cyclic subgroup. The classes of \(p/(t+1)\) all have valuation \(1\pmod e\). If \([p/(s+1)]=[p/(t+1)]^j\), equality of valuations modulo \(e\) forces \(j\equiv1\pmod e\); then equality of unit classes requires \((s+1)/(t+1)\) to be an \(e\)-th power of a unit. Every such power reduces to 1 in \(\mathbb F_p^\times\), so \(s=t\). There are exactly \(p-1\) distinct fields and the list is exhaustive.

For example, for \(p=3\), \(E_3(X)=1+4X+X^2\) and \(E_4(X)=1+11X+11X^2+X^3\). Their distinguished quadratic factors generate the two ramified quadratic fields \(\mathbb Q_3(\sqrt3)\) and \(\mathbb Q_3(\sqrt{3/2})\).

## Verification
The standalone file `eulerian_tame_verify.py` constructs all Eulerian coefficients from the independent descent recurrence, reconstructs the modulo-\(p\) prime blocks, and performs a full monic Hensel step modulo \(p^2\). It checks the distinguished factor evaluation and residue-unit labels for all indices in the complete prime blocks at \(p=3,5,7,11,13\), 34 pairs total. This is finite corroboration; the universal assertions follow from the proof above. Run with `python3 eulerian_tame_verify.py` using only Python's standard library.

## Relationship to prior work
Cao and Pan (2006), Theorem 1.1, give congruences for residue-class sums of Eulerian numbers, not a classification of fields generated by prime-block polynomial factors. Sharma and Straus (1974), Theorems 6–8, use translated Eisenstein arguments for certain Euler–Frobenius determinant polynomials; the prime-index irreducibility phenomenon and Eisenstein method are therefore **not** asserted to be new here. Iijima, Sasaki, Takahashi and Yoshinaga (2019), Theorems 1.1 and 1.2, establish and characterize Eulerian polynomial congruences **modulo powers of \(X-1\)**, not the coefficientwise mod-\(p\) prime-block factorization or the resulting local Kummer field census. Local Kummer classification is standard. The contribution considered here is the simultaneous realization, with exact residue-unit class, of all \(p-1\) tame cyclic local extension types by one natural contiguous family of Eulerian polynomials.

## Limitations
The factorization is over \(\mathbb Z_p\); it does not assert global irreducibility or global Galois groups of the original Eulerian polynomials. It treats odd primes and the specific block \(p\le n\le2p-2\), and identifies only one distinguished local factor at each index. The local Kummer classification and the Eulerian recurrence are established background; only the explicit combination and exhaustion is presented as a prospective new result. Independently establishing originality against every possible specialist reference is not claimed.

## References
1. H.-Q. Cao and H. Pan, *Congruences on Stirling numbers and Eulerian numbers*, arXiv:math/0608564, first publicly submitted 2006-08-23, especially Theorem 1.1. https://arxiv.org/abs/math/0608564
2. A. Sharma and E. G. Straus, *On the Irreducibility of a Class of Euler Frobenius Polynomials*, *Canadian Mathematical Bulletin* **17** (1974), 265–273, DOI:10.4153/CMB-1974-052-x, Theorems 6–8. https://doi.org/10.4153/CMB-1974-052-x
3. K. Iijima, K. Sasaki, Y. Takahashi and M. Yoshinaga, *Eulerian polynomials and polynomial congruences*, *Contributions to Discrete Mathematics* **14** (2019), 46–54, DOI:10.55016/ojs/cdm.v14i1.62485, Theorems 1.1–1.2. https://cdm.ucalgary.ca/article/download/62485/53775/201267
