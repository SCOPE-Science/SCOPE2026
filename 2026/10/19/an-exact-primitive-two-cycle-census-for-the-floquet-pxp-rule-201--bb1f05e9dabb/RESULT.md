# An exact primitive-two-cycle census for the Floquet–PXP Rule 201 automaton

## Finding

On every even periodic binary ring of size \(L=2m\geq4\), let \(F=O\circ E\) be the deterministic Floquet–PXP Rule 201 map: \(E\) toggles all even sites with two zero neighbors, and then \(O\) toggles all odd sites with two zero neighbors. All toggles within one parity layer are simultaneous.

Define a \(16\times16\) nonnegative integer matrix \(T\) indexed by four-bit words. For a four-bit word \(a b c d\) and bit \(e\), put \(T_{abcd,bcde}=1\) precisely when the five-bit word \(abcde\) is *not* in

\[
\mathcal B=\{00000,00001,01001,01010,10000,10010\},
\]

and put all other entries equal to zero. Here \(bcde\) means shift left one bit and append \(e\). Then

\[
\#\operatorname{Fix}(F^2)=\operatorname{tr}(T^{2m}),\qquad
\#\operatorname{Fix}(F)=\mathrm{Luc}_{m}^{2},
\]

where the Lucas numbers are \(\mathrm{Luc}_0=2\), \(\mathrm{Luc}_1=1\), and \(\mathrm{Luc}_{m+2}=\mathrm{Luc}_{m+1}+\mathrm{Luc}_{m}\). In particular, the number of distinct *primitive period-two orbits* is exactly

\[
C_{2m}=\frac{\operatorname{tr}(T^{2m})-\mathrm{Luc}_m^{2}}{2}.
\]

The characteristic polynomial of \(T\) has the exact factorization

\[
\det(zI-T)=z^8(z^2+1)(z^6-z^5-z^4-z^2-z+1).
\]

Writing \(\rho=1.781643598608\ldots\) for the unique real root above \(1\) of the sextic factor, one has

\[
C_{2m}=\frac12\rho^{2m}+O(\varphi^{2m})\qquad(m\to\infty),
\]

where \(\varphi=(1+\sqrt5)/2\). Hence the shortest nontrivial Floquet recurrence sector has exact exponential growth rate \(\rho\), with \(\rho>\varphi\). For \(L=4,6,8,10,12,14,16,18\), respectively, the numbers of primitive period-two orbits are \(2,6,26,100,350,1204,4050,13470\).

## Assumptions and scope

The ring has \(L\ge4\) even sites labeled modulo \(L\), with bits \(x_j\in\{0,1\}\). Each parity layer updates the central bit at site \(j\) by

\[
x_j\longmapsto x_j\oplus (1-x_{j-1})(1-x_{j+1}),
\]

while leaving all opposite-parity bits unchanged; \(\oplus\) is Boolean addition modulo two. There is no nearest-neighbor exclusion imposed on initial strings. A *period-two orbit* is a two-element set \(\{x,F(x)\}\) satisfying \(F^2(x)=x\) but \(F(x)\ne x\). For \(L=4\), the two entries \(x_{j-2}\) and \(x_{j+2}\) in a cyclic five-site window refer to the same physical site; the cyclic transfer construction automatically enforces that identification.

## Proof

**1. Two half steps reduce to a local commutation test.** Each parity layer is an involution, because it does not change the neighboring bits controlling its toggles. Consequently \(F^{-1}=E\circ O\), and

\[
F^2(x)=x\quad\Longleftrightarrow\quad O E(x)=E O(x).
\]

At any site \(j\), abbreviate the five initial bits by \((a,b,c,d,e)=(x_{j-2},x_{j-1},x_j,x_{j+1},x_{j+2})\). In one ordering of the half steps, site \(j\) is toggled if and only if \(u=(1-b)(1-d)=1\). In the reverse ordering, its neighbors have first been toggled, conditionally on their own neighbors, so the center is toggled if and only if

\[
 u'=[1-(b\oplus(1-a)(1-c))]\,[1-(d\oplus(1-c)(1-e))]=1.
\]

Comparison of the two output bits at every site shows that the half-step maps commute *on the given string* exactly when \(u=u'\) at every cyclic site. Exhausting the \(32\) possible five-bit words gives precisely the six forbidden patterns \(\mathcal B\) displayed above. This is a finite truth-table lemma, reproducible independently by the included checker, and is valid for both site parities.

**2. The cyclic word language gives a transfer trace.** A closed walk of length \(L\) in the four-bit overlap graph for \(T\) is uniquely a labeled cyclic binary word of length \(L\) whose every five-bit window avoids \(\mathcal B\). The overlap edges impose each successive four-bit state, including the wrap-around transitions. Conversely, each admissible labeled cyclic word determines a unique closed walk. Thus \(\#\operatorname{Fix}(F^2)=\operatorname{tr}(T^L)\) for every even \(L\ge4\).

**3. Count stationary strings.** If \(F(x)=x\), every even bit must survive its single even-layer update, so all even-layer toggles must be inactive. The same holds for every odd bit in the subsequent odd layer. Because no even bit was toggled, the second condition is evaluated on the initial configuration as well. Hence on each of the two parity sublattices (each a cyclic word of length \(m\)) there can be no adjacent zeros. The number of cyclic binary words of length \(m\) with no adjacent zeros is \(\mathrm{Luc}_m\), including for \(m=2\) with its periodic interpretation. This follows by taking the trace of the standard two-state no-00 transfer matrix, whose eigenvalues solve \(z^2-z-1=0\). The two parity strings are independently chosen; therefore \(\#\operatorname{Fix}(F)=\mathrm{Luc}_m^2\).

Every point fixed by \(F^2\) but not by \(F\) belongs to a primitive orbit of size exactly two; division by two gives \(C_{2m}\).

**4. Characteristic polynomial and growth.** Exact integer characteristic-polynomial computation (the included checker uses the Faddeev–LeVerrier recurrence) yields the displayed factorization. The nonzero eigenvalues consist of the two roots of \(z^2+1\) and six reciprocal roots of the palindromic sextic. For the latter, put \(t=z+z^{-1}\); the sextic equation is equivalent to

\[
t^3-t^2-4t+2=0.
\]

This cubic has one root in each of \((-2,-1)\), \((0,1)\), and \((2,3)\): the signs at the five endpoints certify these intervals, and there can be no others. The first two roots give four distinct unit-modulus complex roots, while the last gives the reciprocal positive pair \(\rho>1\) and \(\rho^{-1}<1\). Therefore

\[
\operatorname{tr}(T^{2m})=\rho^{2m}+O(1).
\]

Since \(\mathrm{Luc}_m^2=\varphi^{2m}+O(1)\) and \(\rho>\varphi\), the claimed asymptotic follows. The eigenvalues in this argument are distinct except the zero eigenvalue, which has no effect on positive-power traces; diagonalizability of any zero-eigenvalue Jordan blocks is not needed.

## Verification

The standalone Python 3 script `verify.py` uses only the standard library. It independently enumerates the five-bit rule, constructs \(T\), computes the degree-16 characteristic polynomial with exact integer arithmetic, and compares \(\operatorname{tr}(T^L)\) with a second implementation of the original staggered automaton, exhaustively for every state of the even rings \(4\le L\le16\). It also checks the fixed-point Lucas formula, orbit parity/divisibility, and the exact values through \(L=18\). The symbolic factorization and the listed counts were reproduced from the staged `verify.py` file rather than relying on an external table. Exact enumeration is an independent finite check, not the proof for all ring sizes: the local commutation argument and cyclic trace bijection provide the all-size proof.

## Relationship to prior work

Rule 201 and the alternating-even/odd Floquet protocol are defined in Wilkinson, Klobas, Prosen and Garrahan (2020). That work analyzes integrable soliton motion and a nearest-neighbor-excluded sector, without stating an all-ring formula for prime-two Floquet cycles. Klobas (first public June 25, 2026) derives influence matrices and multi-time local correlations for this model. Yang, Wang and Wang (first public June 17, 2026) independently develop an influence-matrix bootstrap and examine other periodic and nonthermal sectors. Neither paper's inspected body/appendix supplies this specific full-state-space period-two trace or its forbidden-window polynomial.

Macauley, McCammond and Mortveit (2008), Section 5, study the **same local Wolfram rule 201** applied in arbitrary sequential orders. Their orbit-group decomposition counts connected orbits under the group generated by *all individual site flips*, including Lucas/Fibonacci orbit sizes; Proposition 5.7 counts transpositions of an **individual local update**. Neither count specifies the two-cycles of the single fixed staggered *global composition* considered here. Their general framework does not imply the displayed sextic or length-uniform two-cycle census without a further order-specific calculation.

## Limitations

The result concerns only period one and primitive period two of the *classical permutation* on unrestricted finite even rings, not higher primitive periods, quantum linear-combination dynamics, transport coefficients, thermodynamic local correlations, or perturbation stability. The asymptotic is for even ring lengths. The relationship-to-prior-work conclusion is based on the inspected primary material and searches; another exact cycle classification outside these sources remains a residual originality risk. No independent external audit has been performed.

## References

1. K. Klobas, *Exact subsystem dynamics in the deterministic Floquet-PXP model*, arXiv:2606.27337v1 (first public June 25, 2026). https://arxiv.org/abs/2606.27337
2. B. L. Wilkinson, K. Klobas, T. Prosen and J. P. Garrahan, *Exact solution of the Floquet-PXP cellular automaton*, arXiv:2006.06556v1 (2020). https://arxiv.org/abs/2006.06556
3. X.-Y. Yang, H.-R. Wang and Z. Wang, *Solving Nonequilibrium Dynamics via Influence Matrix Bootstrap: Floquet-PXP Model*, arXiv:2606.19430v1 (first public June 17, 2026). https://arxiv.org/abs/2606.19430
4. M. Macauley, J. McCammond and H. S. Mortveit, *Dynamics Groups of Asynchronous Cellular Automata*, arXiv:0808.1238v1 (2008), especially Section 5, Rule 201. https://arxiv.org/abs/0808.1238
