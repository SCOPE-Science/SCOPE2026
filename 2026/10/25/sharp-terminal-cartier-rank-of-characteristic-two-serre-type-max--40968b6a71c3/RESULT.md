# Sharp terminal Cartier rank of characteristic-two Serre-type maximal curves

## Finding
For every odd integer \(n\ge3\), put \(m=(2^n+1)/3\). On the smooth projective curve \(X_n\) over an algebraically closed field of characteristic two with affine equation \(y^4+y=x^m\), the Cartier operator \(\mathcal C\) acting semilinearly on regular one-forms satisfies
\[
\operatorname{im}(\mathcal C^{n-1})=\operatorname{span}\left\{x^{(2\cdot4^r-2)/3}\,dx:0\le r\le(n-3)/2\right\},\qquad
\operatorname{rank}(\mathcal C^{n-1})=(n-1)/2,\qquad\mathcal C^n=0.
\]
Consequently, its nilpotency index is exactly \(n\), and the number of Jordan chains of maximal length \(n\) is \((n-1)/2\). The rank means dimension of the image over the algebraically closed field; the semilinearity is harmless for ranks and nilpotent-chain lengths.

## Assumptions and scope
Fix odd \(n=2k+3\ge3\) and \(k\ge0\); write \(I=\sum_{a=1}^k4^a\), with the empty sum zero. Then \(m=2I+3\) is odd. The smooth projective normalization of \(y^4+y=x^m\) has a unique point at infinity, genus \(g=3(m-1)/2=2^{n-1}-1\), and its canonical differential basis is
\[
\mathcal B=\{x^i y^j\,dx:0\le j\le2,\ i\ge0,\ 4i+jm\le 3m-5\}.
\]
This follows from the pole orders \(\operatorname{ord}_\infty(x)=-4\), \(\operatorname{ord}_\infty(y)=-m\), \(\operatorname{ord}_\infty(dx)=3m-5\); the listed forms are independent by their distinct pole orders and number \(g\). In particular the three index ranges for \(j=0,1,2\) are, respectively, \(0\le i\le3I/2+1\), \(0\le i\le I\), and \(0\le i\le I/2-1\). The last range is empty when \(k=0\).

## Proof
In characteristic two, \(\mathcal C(f^2h\,dx)=f\mathcal C(h\,dx)\) and \(\mathcal C(x^i dx)=0\) for even \(i\), whereas \(\mathcal C(x^i dx)=x^{(i-1)/2}dx\) for odd \(i\). Since \(y^4=y+x^m\), the entire Cartier action on the basis is
\[
\begin{array}{c|cc}
 &i\text{ odd}&i\text{ even}\\\hline
j=0 &( (i-1)/2,0)&0\\
j=1 &( (i-1)/2,2)&((i+m-1)/2,0)\\
j=2 &( (i-1)/2,1)&0
\end{array}
\]
where a pair denotes the exponent and the power of \(y\) of the output differential. The Frobenius-semilinearity acts on coefficients, which are all one in this matrix.

A sequence beginning with \(j=1\) that survives successive transitions between \(j=1\) and \(j=2\) must start at an odd index. Each pair of such transitions divides \(i+1\) by four: after \(2r\) transitions, the index is \(s=(i+1)/4^r-1\). Continuing these pairs until \(n-1=2k+2\) steps is impossible, because it would require \(i\ge4^{k+1}-1>I\). Thus every surviving sequence must leave \(j=1\) at an even index \(s\) after \(r\) pairs, for some \(0\le r\le k\). Its first \(j=0\) index is \(e=I+1+s/2\). To survive the remaining \(t=2(k-r)+1\) Cartier steps in \(j=0\) we require \(e\equiv 2^t-1\pmod{2^t}\).

Put \(u=k-r\), \(I_u=\sum_{a=1}^{u}4^a\). Reducing \(I+1\) modulo \(2^t=2\cdot4^u\) makes this congruence equivalent to
\[
 s\equiv I_u\pmod{4^{u+1}}.
\]
The basis bound \(i\le I\) yields \(0\le s\le I/4^r<4^{u+1}\), so \(s=I_u\) uniquely. The corresponding initial index is
\[
i_r=4^r(I_u+1)-1=\sum_{a=r}^{k}4^a-1\quad (0\le r\le k).
\]
It lies in the basis range, all required intermediate indices have the requisite parity, and the final output exponent equals
\[
 (e+1)/2^{2u+1}-1=(2\cdot4^r-2)/3.
\]
These are \(k+1\) distinct outputs.

There are no further contributions. An initial \(j=0\) term needs initial index at least \(2^{2k+2}-1\) to survive \(2k+2\) successive halvings, whereas its basis index is at most \(3I/2+1<2^{2k+2}-1\). An initial \(j=2\) term either dies immediately (even index) or reaches \(j=1\) after one step with index \(s_0\le I/4-1<4^k-1\) when \(k\ge1\). To survive the remaining \(2k+1\) steps, it must either alternate through \(k\) pairs, which requires initial \(j=1\) index at least \(4^k-1\), or exit after \(r<k\) pairs into \(j=0\). In the latter case, survival of the remaining \(2(k-r)\) halvings gives the congruence \(s\equiv I_{k-r}\pmod{2\cdot4^{k-r}}\), forcing its initial \(j=1\) index to be at least \(4^r(I_{k-r}+1)-1\ge4^k-1\), another contradiction. For \(k=0\), no \(j=2\) basis terms occur.

Therefore the stated \(k+1\) output forms form the exact image of \(\mathcal C^{n-1}\). Every terminal exponent \((2\cdot4^r-2)/3\) is even, so another Cartier application kills every output. Since \(k+1\ge1\), the nilpotency index is precisely \(n\), completing the proof.

## Verification
The accompanying standalone script `cartier_2n_verifier.py` constructs the complete differential basis, applies the exact Cartier transition rule, and checks the claimed image and subsequent vanishing for \(n=3,5,7,9,11,13,15\). It returns `CARTIER_LAST_ITERATE_CHECKS_PASSED`. These finite checks corroborate, but do not replace, the parameter-uniform congruence proof. The terminal ranks in those cases are respectively \(1,2,3,4,5,6,7\), with final exponent sets beginning \(\{0\},\{0,2\},\{0,2,10\}\).

## Relationship to prior work
Shafighi, *The a-number of the Serre-type maximal curves of Abdón–Bezerra–Quoos* (2026), gives the curve family, canonical differential basis, and one-step Cartier action, and calculates its a-number; the inspected article does not establish the explicit rank of the penultimate Cartier iterate or the exact maximal-chain multiplicity. Almeida–Tafazolian–Vieira, *a-Numbers, higher Cartier ranks and maximality of van der Geer–van der Vlugt curves* (2026), motivates higher Cartier ranks as natural refined invariants of Jacobians but studies a different curve class. General Cartier nilpotence bounds for maximal curves do not determine whether the last permitted iterate is nonzero or its rank.

## Limitations
The theorem addresses this particular characteristic-two Serre-type family, not arbitrary maximal curves or all Ekedahl–Oort invariants. The semilinear Cartier module may have additional shorter blocks; they are not classified here. No independent external audit has been performed. Priority can be affected by older general theorems on iterated Cartier operators that were not exhaustively ruled out.

## References
- M. Shafighi, *The a-number of the Serre-type maximal curves of Abdón–Bezerra–Quoos*, arXiv:2610.15266v1 (2026), especially the differential basis and Cartier formula.
- Almeida, Tafazolian, Vieira, *a-Numbers, higher Cartier ranks and maximality of van der Geer–van der Vlugt curves*, arXiv:2610.17476v1 (2026).
- Abdón, Bezerra, Quoos, original construction of the Serre-type maximal curves, as referenced in arXiv:2610.15266v1.
