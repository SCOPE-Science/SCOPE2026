# Cyclotomic cancellation and signed residue recurrences for two-digit radix sets

## Finding
Let \(q\ge3\) be odd and \(b\ge3\). Fix an allowed nonzero digit \(a\) with \(1\le a<b\) and \(\gcd(q,ab)=1\). For each length \(L\ge0\), count all strings of exactly \(L\) positions with digits \(0,a\), including initial zeros, by
\[
 C_L(r)=\#\left\{\epsilon\in\{0,1\}^L:\sum_{j=0}^{L-1}a\epsilon_jb^j\equiv r\pmod q\right\},\quad r\in\mathbb Z/q\mathbb Z.
\]
Let \(H=\langle b\rangle\) be the subgroup of units modulo \(q\), and set \(t=|H|\).

**Positive orbit:** If \(2\in H\), then for every \(L\ge0\) and every residue \(r\),
\[
 C_{L+t}(r)=C_L(r)+\frac{2^{L+t}-2^L}{q}.
\]
Thus \(C_{L+t}(r)-2^{L+t}/q=C_L(r)-2^L/q\).

**Negative orbit:** If \(-2\in H\) and \(2\notin H\), define \(e=(-1)^t\) and \(S=a\sum_{u\in H}u\pmod q\). For every \(L\ge0\) and residue \(r\),
\[
 C_{L+t}(r)=e\,C_L(r+S)+\frac{2^{L+t}-e2^L}{q}.
\]
The rational-looking additive terms are integers. Consequently the absolute discrepancy obeys a signed translate recurrence,
\[
 C_{L+t}(r)-\frac{2^{L+t}}q
 =e\left(C_L(r+S)-\frac{2^L}q\right).
\]
In either orbit, for every \(L\) and \(r\),
\[
 \left|C_L(r)-\frac{2^L}{q}\right|\le 2^{t-1}.
\]
Two concrete consequences: for the digits \(\{0,1\}\), the counts modulo \(7\) in base \(3\), and modulo \(9\) in base \(4\), differ by at most one between any two residues for **every** length.

## Assumptions and scope
The digit length counts strings with leading zeros: each string is a unique integer in \([0,b^L)\). The modulus is any odd integer, not necessarily a prime or prime power. Coprimality of \(a\) and \(b\) with \(q\) is essential to avoid Fourier characters that vanish on the digit difference; the orbit hypotheses are sufficient conditions only, not asserted to be necessary. All formulas include \(L=0\), when the empty string represents zero. In the signed case the residue argument \(r+S\) is interpreted modulo \(q\).

## Proof
Let \(\zeta=\exp(2\pi i/q)\). For each additive character index \(h\in\{0,\ldots,q-1\}\), set
\[
 \widehat C_L(h)=\sum_{r=0}^{q-1}C_L(r)\zeta^{hr}
 =\prod_{j=0}^{L-1}(1+\zeta^{ha b^j}).
\]
This is an identity obtained by expanding the independent binary digit choices. Clearly \(\widehat C_L(0)=2^L\). For \(h\ne0\), every \(ha u\) with \(u\in H\) is nonzero modulo \(q\), since \(a,u\) are units. Therefore every denominator below is nonzero, and
\[
 P_h:=\prod_{u\in H}(1+\zeta^{hau})
 =\prod_{u\in H}\frac{1-\zeta^{2hau}}{1-\zeta^{hau}}.
\]
If \(2\in H\), multiplication by \(2\) permutes \(H\); numerator and denominator are the same multiset, so \(P_h=1\). The sequence \(b^j\) runs once through \(H\) in each block of length \(t\), yielding \(\widehat C_{L+t}(h)=\widehat C_L(h)\) for every nonzero \(h\).

If \(-2\in H\), multiplication by \(2\) sends \(H\) onto \(-H\). Thus
\[
 P_h=\prod_{u\in H}\frac{1-\zeta^{-hau}}{1-\zeta^{hau}}
 =(-1)^t\zeta^{-ha\sum_{u\in H}u}=e\zeta^{-hS}.
\]
Here \(e=(-1)^t\) and \(S=a\sum_{u\in H}u\pmod q\). Therefore \(\widehat C_{L+t}(h)=e\zeta^{-hS}\widehat C_L(h)\) for \(h\ne0\). Fourier inversion gives the two claimed recurrences by comparing the zero character separately: the transform of \(r\mapsto C_L(r+S)\) is \(\zeta^{-hS}\widehat C_L(h)\), and a constant function of residue \(r\) contributes only at character zero. The additive constant must be \((2^{L+t}-e2^L)/q\). It is an integer because \(2=\pm b^j\pmod q\) in the respective cases, whence \(2^t\equiv e\pmod q\).

Subtracting the uniform mean gives a pure periodic or signed permutation on the vector of discrepancies. For every \(L\), reduce \(L\) by repeated subtraction of \(t\) to a length \(s<t\). The absolute discrepancy at length \(L\) equals one of the absolute discrepancies at length \(s\). Since \(0\le C_s(r)\le2^s\), one has \(\lvert C_s(r)-2^s/q\rvert\le2^s\le2^{t-1}\). This proves the uniform bound.

For \((q,b,a)=(7,3,1)\), the subgroup is all six nonzero residues and \(2\in H\); the finite initial lengths \(0\le s<6\) have maximum count minus minimum count equal to one. The positive recurrence preserves that difference for every subsequent length. For \((q,b,a)=(9,4,1)\), \(H=\{1,4,7\}\), \(t=3\), \(-2=7\in H\), \(2\notin H\), and \(S=3\); the initial lengths \(s=0,1,2\) have range one. The signed recurrence subtracts and permutes counts, preserving the range for every later length. Hence both examples are perfectly balanced for all lengths.

## Verification
The accompanying standalone file `checker.py` uses exact integer residue-count dynamic programming, independently forms the right sides of the two recurrences, and checks 373 length/parameter comparisons on admissible moduli \(7,9,11,15,23,25,27,49\), with multiple bases/digit choices. It also verifies 540 complete-prefix balancing cases for the stated two examples and an additional base-\(4\), modulo-\(7\) example. The proof above, not the finite tests, establishes the assertions for unbounded lengths and all eligible moduli. Run `python3 checker.py` with an ordinary Python 3 interpreter; no third-party packages are required.

## Relationship to prior work
Erdős, Mauduit and Sárközy (1998) studied distribution in residue classes for missing-digit integers. Aloui (published 6 January 2015) treats the same digit-restricted objects and, in its introduction and Corollary 2.2, records quantitative asymptotic equidistribution results. Those cited statements yield errors that can grow with digit length; they do not state the exact positive-orbit/signed-orbit recurrences or a universal bounded **absolute** discrepancy. The present contribution is the special multiplicative-orbit cancellation that collapses the entire nontrivial character product to a root of unity, an arithmetic refinement of the familiar generating-function factorization. Later work on Markov chains supplies qualitative necessary and sufficient equidistribution conditions but its stated results are likewise not the exact block identity. It is possible that this elementary orbit simplification appears implicitly in less searchable sources; originality is not independently certified.

## Limitations
No assertion concerns arbitrary cutoffs other than the radix endpoints \(b^L\), nor arbitrary digit sets, bases that fail the subgroup condition, or relative discrepancy at a variable modulus. These are two sufficient orbit cases, not a classification of all parameter choices having bounded discrepancy. There is no independent mathematical audit.

## References
1. P. Erdős, C. Mauduit, A. Sárközy, *On arithmetic properties of integers with missing digits. I. Distribution in residue classes*, Journal of Number Theory 70 (1998), 99–120.
2. K. Aloui, *Sur les entiers ellipséphiques: somme des chiffres et répartition dans les classes de congruence*, Periodica Mathematica Hungarica 70 (2015), 171–208; published online 6 January 2015; DOI: 10.1007/s10998-014-0066-8.
3. *Distribution of integers with digit restrictions via Markov chains*, Ergodic Theory and Dynamical Systems (2026), DOI: 10.1017/etds.2025.10256; introduction, Corollary A, and stated main results.
